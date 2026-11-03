---
article_id: 360063880833
category: Financeiro - Contas a Receber - LCDPR
content_hash: b0a3924f144ab0f1230fc2bf2978ce3025a241036b39d720b5d9a8464a895614
fetched_at: '2026-06-28T22:38:15.846034+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFIN - FINA820 - Qual
  cpf será levado para o extrator do lcdpr no bloco Q100
type: support-article
updated_at: '2022-03-24T18:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063880833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Qual-cpf-ser%C3%A1-levado-para-o-extrator-do-lcdpr-no-bloco-Q100
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:02 min**

**Dúvida**Qual cpf será levado para o extrator do lcdpr no registro Q100?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12  
  
**Solução**No **LCDPR** irá considerar primeiro o CPF do **cliente**/**fornecedor** (**SA1** / **SA2**), se estiver preenchido. Caso a **SA1** e **SA2** não estiver preenchido com o CPF do **cliente**/**fornecedor** o sistema irá na **SE5** buscar e por o último irá levar o CPF do declarante.

**Importante:**  
O LCDPR sempre terá que levar um CPF para o arquivo gerado.
