---
content_hash: 0674b3d0cfd09dfd7cfed03f4bf739bd82f17657f2c74c4b06a6da6032067002
fetched_at: '2026-06-29T00:11:39.800459+00:00'
page_id: '789984672'
product: rm
source: tdn-rm
title: PDC - Andamento da Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/PDC+-+Andamento+da+Obra
version: 2
---

Ao acessar o menu de **Andamento da Obra**, no *PDC*, o sistema apresenta um filtro por Empreendimento, a partir do qual serão apresentados os gráficos com as informações dos percentuais das etapas de andamento de obra cadastrados:

* **Percentual Geral Concluído:** É a média dos percentuais de avanço de todas as etapas de andamento de obra cadastradas para o empreendimento da subunidade selecionada;
* **Percentual de Etapa Concluído:** É o percentual de avanço etapas de andamento de obra cadastradas para o empreendimento da subunidade selecionada;

Cabe ressaltar que o cálculo deste *Percentual Geral Concluído* é obtido através da *S**o**ma de todos os PERCENTUAIS, Multiplicado pelo seu respectivo PESO*, tudo isso divido pela Soma de caba um destes PESOS, conforme exemplificado na consulta abaixo:

Andamento da Obra PDC

SELECT ROUND(SUM(X.PERCENTUAL\*X.PESO)/SUM(X.PESO),2) AS 'ANDAMENTO DA OBRA'  
FROM   (  
                 SELECT    XEMPREENDIMENTOMEDICAO.CODCOLIGADA,  
                           XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR,  
                           XEMPREENDIMENTOMEDICAO.CODMEDICAO,  
                           XEMPREENDIMENTOMEDICAO.DESCRICAO,  
                           XEMPREENDIMENTOMEDICAO.PESO,  
                           SUM(XEMPREENDIMENTOMEDICAOVALOR.PERCENTUAL) PERCENTUAL  
                 FROM      XEMPREENDIMENTOMEDICAO (NOLOCK)  
                 LEFT JOIN XEMPREENDIMENTOMEDICAOVALOR(NOLOCK)  
                 ON        XEMPREENDIMENTOMEDICAO.CODCOLIGADA = XEMPREENDIMENTOMEDICAOVALOR.CODCOLIGADA  
                 AND       XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR = XEMPREENDIMENTOMEDICAOVALOR.COD\_PESS\_EMPR  
                 AND       XEMPREENDIMENTOMEDICAO.CODMEDICAO = XEMPREENDIMENTOMEDICAOVALOR.CODMEDICAO  
                 WHERE     (  
                                     XEMPREENDIMENTOMEDICAO.MODULO = 2  
                           AND       ((  
                                                         XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR = 1)))  
                GROUP BY   XEMPREENDIMENTOMEDICAO.CODCOLIGADA,  
                           XEMPREENDIMENTOMEDICAO.COD\_PESS\_EMPR,  
                           XEMPREENDIMENTOMEDICAO.CODMEDICAO,  
                           XEMPREENDIMENTOMEDICAO.PESO,  
                           XEMPREENDIMENTOMEDICAO.DESCRICAO) X
