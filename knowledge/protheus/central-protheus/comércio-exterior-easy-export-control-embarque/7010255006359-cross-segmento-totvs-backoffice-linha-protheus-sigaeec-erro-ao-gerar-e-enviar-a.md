---
article_id: 7010255006359
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 875bdd3459e5b042211dd7571b92e0c5a36d76b228fb8cda5a715b67fc47707f
fetched_at: '2026-06-28T22:36:56.557975+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro ao gerar
  e enviar a DUE após o Embarque do pedido de exportação
type: support-article
updated_at: '2022-06-24T18:53:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7010255006359-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-ao-gerar-e-enviar-a-DUE-ap%C3%B3s-o-Embarque-do-pedido-de-exporta%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **03:00 min** **Dúvida**Quando temos um Embarque de Exportação que utiliza CPF, a rotina está apresentando a seguinte mensagem ao gerar e enviar a DUE referente ao processo em questão, como corrigir?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7009952597143/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões  
  
**Solução**Neste caso, é necessário verificar como os campos "**EK1\_RESPDE** " e "**EEC\_RESPDE**" foram preenchidos e se estão de acordo com o **CPF** informado dentro da **rotina de Embarque**.   
Já houve um exemplo em que o CPF informado possuía um "underline" ao final do campo mencionado (**EEC\_RESPDE**) ocasionando a mensagem reportada.
