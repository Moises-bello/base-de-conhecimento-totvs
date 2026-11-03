---
content_hash: 3727f9ccaf291914b9904755785dbc28f4b106383cb1b8820469b278b11d6e50
fetched_at: '2026-06-29T00:09:49.668899+00:00'
page_id: '435105345'
product: rm
source: tdn-rm
title: Valida Distrato em Aberto com Plano de Financiamento gerado
type: documentation
url: https://tdn.totvs.com/display/LRM/Valida+Distrato+em+Aberto+com+Plano+de+Financiamento+gerado
version: 1
---

**Valida Distrato em Aberto com Plano de Financiamento gerado**

---

Este processo verifica se existem distratos com plano de financiamento gerado, mas que não geraram lançamentos financeiros, que poderiam gerar inconsistências ao migrar para a versão de revitalização.  
   
  
   
   
Para saber exatamente quais são as vendas que possuem distratos nessa situação a ferramenta faz a seguinte consulta:  
   
**SELECT** XVENDA.CODCOLIGADA, XVENDA.NUM\_VENDA **AS** NUMVENDA        
**FROM** XVENDA  
**WHERE** EXISTS  
      (**SELECT** 1  
         **FROM** XPARCELAPAGAMENTO  
         JOIN   XREGRACOMPONENTEVENDA  
         **ON** (XREGRACOMPONENTEVENDA.CODCOLIGADA = XPARCELAPAGAMENTO.CODCOLIGADA   
                AND XREGRACOMPONENTEVENDA.NUM\_VENDA = XPARCELAPAGAMENTO.NUM\_VENDA   
                AND  XREGRACOMPONENTEVENDA.COD\_GRUPO = XPARCELAPAGAMENTO.COD\_GRUPO   
                AND  XREGRACOMPONENTEVENDA.ORIGEMREGRA = 2)  
        **WHERE** XPARCELAPAGAMENTO.CODCOLIGADA = XVENDA.CODCOLIGADA  
          AND XPARCELAPAGAMENTO.NUM\_VENDA = XVENDA.NUM\_VENDA)           
          AND EXISTS (**SELECT** 1 **FROM** XDISTRATO **WHERE** XDISTRATO.NUMVENDA =XVENDA.NUM\_VENDA AND XDISTRATO.COD\_SIT\_DISTRATO IN (10,90))  
**ORDER** **BY** XVENDA.CODCOLIGADA, XVENDA.NUM\_VENDA  
   
   
Esta consulta não precisa ser executada, pois é realizada internamente pela ferramenta e tem caráter ilustrativo Se for encontrado algum distrato com plano de financiamento e sem lançamento financeiro, será exibida a visão de distratos para que o usuário decida registro a registro se cancelar o distrato efetivar e gerar os lançamentos financeiros.
