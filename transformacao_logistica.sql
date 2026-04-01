-- Criando a tabela base para o projeto de Logística
CREATE TABLE Fato_Logistica (
    ID_Pedido VARCHAR(20) PRIMARY KEY,
    Transportadora VARCHAR(50),
    Data_Pedido DATE,
    Data_Entrega_Prometida DATE,
    Data_Entrega_Real DATE,
    Destino VARCHAR(50),
    Valor_Frete DECIMAL(10,2),
    Status_Extravio INT -- 0 para Não, 1 para Sim
);
-- Processo de ETL e Cálculo de OTIF via SQL
WITH Base_Limpa AS (
    -- 1. Limpeza e tratamento: Se não foi entregue, assume a data atual para cálculo
    SELECT 
        ID_Pedido,
        Transportadora,
        Data_Pedido,
        Data_Entrega_Prometida,
        COALESCE(Data_Entrega_Real, CAST(GETDATE() AS DATE)) AS Data_Final,
        Destino,
        Valor_Frete
    FROM Fato_Logistica
    WHERE Status_Extravio = 0 -- Focando a análise de prazo apenas em pedidos não extraviados
),

Calculo_Prazos AS (
    -- 2. Calculando a diferença de dias entre o prometido e o realizado
    SELECT *,
        DATEDIFF(day, Data_Entrega_Prometida, Data_Final) AS Dias_Atraso
    FROM Base_Limpa
),

Classificacao_OTIF AS (
    -- 3. Definindo o flag de On-Time (No Prazo)
    -- Se Dias_Atraso for <= 0, o pedido foi entregue no prazo (On-Time)
    SELECT *,
        CASE 
            WHEN Dias_Atraso <= 0 THEN 1 
            ELSE 0 
        END AS No_Prazo
    FROM Calculo_Prazos
)

-- 4. Resultado Final: Agregação por Transportadora e Destino
-- Exatamente o que você usou para alimentar os gráficos no Power BI
SELECT 
    Transportadora,
    Destino,
    COUNT(ID_Pedido) AS Total_Pedidos,
    SUM(No_Prazo) AS Pedidos_No_Prazo,
    ROUND(CAST(SUM(No_Prazo) AS FLOAT) / COUNT(ID_Pedido) * 100, 2) AS Percentual_OTIF
FROM Classificacao_OTIF
GROUP BY Transportadora, Destino
ORDER BY Percentual_OTIF DESC;