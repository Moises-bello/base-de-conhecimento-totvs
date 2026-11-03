---
content_hash: 506633c4efec16031a714d48e4604cbe81467687b5281e6721a59005e596ff61
fetched_at: '2026-06-29T00:11:27.312099+00:00'
page_id: '722644785'
product: rm
source: tdn-rm
title: API de Consulta de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/API+de+Consulta+de+Contrato
version: 3
---

# Objetivo

---

Esse documento tem o objetivo de exemplificar o uso da API para retornar informações dos saldos de contrato por período.

# 1 - API de Consulta de Contrato

---

Esta API retorna uma lista com os dados de medição dos itens do contrato conforme o tipo (Exemplo: Serviço ou Insumo), e parâmetros utilizados (Exemplo: Se utilizar PI+R) . Essas informações são as mesmas que são apresentadas na tela de medição ou de consumo, que é acessada no anexo de períodos do contrato.

**Máscara de Url: [http://localhost:8051/api/construction-projects/v1/contract-measure-info](http://localhost:8051/api/construction-projects/v1/contract-measure-info "Follow link")**

#### **Obs:** Caso o período informado não existe na base de dados será retornado o ultimo período disponível.

**Método de entrada:** Post

**Exemplo de Request**

|  |  |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 | Exemplo de API:  **Request:**  {     "companyId": 1,     "projectId": 2,     "contractId": 2,     "period": "0001" } |

**Consulta de saldos do contrato:**

Para a consulta de saldo do contrato vamos utilizar a mesma API que foi construída para consultar saldo de contrato por período. A diferença será que quando não enviar o Período, a API vai retornar o saldo de todo o contrato.

**Máscara de Url: [http://localhost:8051/api/construction-projects/v1/contracts?companyId=1&projectId=2&contractId=2](http://localhost:8051/api/construction-projects/v1/contracts?companyId=1&projectId=2&contractId=2 "Follow link")**

**Método de entrada:** Post
