---
article_id: 115004726487
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: a80ec842bf4c5fd011178d39b6a71be5e5c714a1bfce2cad0d668cd656e312b0
fetched_at: '2026-06-28T22:37:55.188248+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - BackOffice Linha Protheus - SIGAFIN - Como faço o envio de
  Pagamento Antecipado para o CNAB
type: support-article
updated_at: '2021-09-01T17:48:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726487-Cross-Segmento-BackOffice-Linha-Protheus-SIGAFIN-Como-fa%C3%A7o-o-envio-de-Pagamento-Antecipado-para-o-CNAB
---

**Dúvida**Como faço o envio de Pagamento Antecipado para o CNAB?

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12

**Solução**Um pagamento antecipado a fornecedor pode ser realizado utilizando a comunicação bancária (CNAB).  
Para que isso ocorra, deve-se proceder da seguinte forma:

* Na inclusão de um PA (**FINA050**) é necessário definir as seguintes perguntas dos parâmetros F12  
  **Gera Cheque para Adiantamento ? = NÃO**  
  **Movimento Banco sem Cheque ? NÃO**
* Na rotina de geração de borderôs, gere um borderô de adiantamentos
* A atualização do saldo bancário ocorrerá no processamento do retorno do CNAB

**Saiba mais:**  
Para maiores informações, acesse: <http://tdn.totvs.com/pages/viewpage.action?pageId=229769493>
