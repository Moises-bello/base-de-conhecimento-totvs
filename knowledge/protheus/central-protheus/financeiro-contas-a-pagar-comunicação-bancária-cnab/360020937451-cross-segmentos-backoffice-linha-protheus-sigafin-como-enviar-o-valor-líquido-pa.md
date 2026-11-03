---
article_id: 360020937451
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ad7fa0bbe66b345b39c8b1f99c9667c2f48b687423f1124e98e88bd96eadd54c
fetched_at: '2026-06-28T22:37:55.381883+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como enviar o valor
  líquido para banco através do Arquivo de Cobrança
type: support-article
updated_at: '2022-08-18T02:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020937451-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-enviar-o-valor-l%C3%ADquido-para-banco-atrav%C3%A9s-do-Arquivo-de-Cobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como enviar o valor líquido para banco através do Arquivo de Cobrança (FINA150).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
  
**Solução**  
Caso a retenção dos impostos: PIS,COFINS, CSLL ou IRRF seja na baixa, é possível encaminhar o valor líquido da NF via remessa de cobrança através da rotina Borderô de Recebimento com Impostos (FINA061).   
Assim que incluir os títulos a receber no borderô será retido os impostos, sendo assim, é gerado o borderô de impostos através do valor líquido da NF. E através deste borderô é gerado o arquivo de remessa de cobrança.
