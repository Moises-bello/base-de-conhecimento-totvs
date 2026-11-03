---
article_id: 1500011996061
category: Financeiro - Contas a Pagar - PIX
content_hash: 978328d7d7f1f06ead25470f6266e3f2bb4e4c53a777fd587bb73da5a7af575a
fetched_at: '2026-06-28T22:38:11.332065+00:00'
product: protheus
section_id: 1500001550462
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA420 - Funções do
  layout do CNAB para envio de remessa de PIX no Contas a Pagar
type: support-article
updated_at: '2021-05-24T15:00:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011996061-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA420-Fun%C3%A7%C3%B5es-do-layout-do-CNAB-para-envio-de-remessa-de-PIX-no-Contas-a-Pagar
---

**Dúvida**Quais funções devo inserir no meu layout do CNAB para enviar uma remessa de PIX no Contas a Pagar?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - A partir da versão 12.1.23  
  
**Solução**Estão disponíveis as seguintes novas funções para uso no configurador CNAB Modelo 2

* **FNRETPIX(**nOpcao**)**
  + Com o parâmetro 1, a função retornará o Tipo de Chave PIX ativa para o fornecedor selecionado
  + Com o parâmetro 2, a função retornará a Chave PIX ativa para o fornecedor selecionado
  + Com o parâmetro 3, a função retornará se a transferência (Modelo 45) será através de conta corrente ou chave PIX (neste caso, uma chave deve estar configurada no fornecedor selecionado)
* **FNURLPIX()**
  + Retornará a URL extraída do QR Code informado no título posicionado

**Saiba Mais**[https://tdn.totvs.com/pages/releaseview.action?pageId=569478747#Pagamentosinstant%C3%A2neos-PIX-04.CONTASAPAGAR](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747#Pagamentosinstant%C3%A2neos-PIX-03.CONTASARECEBER)
