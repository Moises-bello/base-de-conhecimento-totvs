---
article_id: 360020300972
category: ADVPL - Classe e Função
content_hash: d785af55f35a666bc69ce62888b40d61995f44e004a35e8c28b649b038309fae
fetched_at: '2026-06-28T22:40:19.205877+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: cannot
  resolve the collation conflict'
type: support-article
updated_at: '2024-01-31T10:25:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020300972-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-cannot-resolve-the-collation-conflict
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Estou fazendo uma *query* em uma customização utilizando dois bancos com colações (*collations*) diferentes, e ao executar o comando é gerado o seguinte erro:

```
Cannot resolve the collation conflict between "Latin1_General_BIN" and "SQL_Latin1_General_CP1_CI_AS" in the equal to operation.
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Este erro ocorre quando são utilizados bancos com colações diferentes (construídos com configurações diferentes) para efetuar um instrução de junção (*join*).

A colação é a codificação de caracteres existente no banco de dados (semelhante ao *encoding*).  
  
**Solução**Verificar se a empresa fabricante do banco de dados disponibiliza alguma função de conversão de colação.  
  
Exemplo

```
SELECT   
    SB1.B1_COD, SB1.B1_DESC,   
    SB1.B1_TIPO, SB5.B5_CEME  
FROM  
    SB1990 AS SB1  
LEFT JOIN  
    SB5990 AS SB5  
    ON SB1.B1_COD COLLATE Latin1_General_CI_AI = SB5.B5_COD COLLATE Latin1_General_CI_AI  
ORDER BY  
    SB1.R_E_C_N_O_ DESC;  
GO
```
