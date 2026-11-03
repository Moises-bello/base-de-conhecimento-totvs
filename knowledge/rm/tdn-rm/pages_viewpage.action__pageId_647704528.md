---
content_hash: e1ae7d2c694755a4b9422657225f0d1405ced6d374b6c930f4470709281bd929
fetched_at: '2026-06-29T00:11:11.517755+00:00'
page_id: '647704528'
product: rm
source: tdn-rm
title: Serviços - TOTVS API Services
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=647704528
version: 15
---

# Índice

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é esclarecer sobre os serviços pagos disponíveis pelo TOTVS API Services e os pré-requisitos para requisição aos mesmos.

# Introdução

---

       O TOTVS API Services é um serviço pago que realiza consultas em entidades públicas e os disponibiliza para qualquer solução TOTVS através de APIs padronizadas, independente do serviço público de consulta. Os serviços disponibilizados pelo mesmo são listados abaixo e dependem do mínimo esforço para consumo dos mesmos.

# Adesão

---

       Para que o cliente posso consumir este serviço é necessário que o mesmo possua licença de algum produto TOTVS que suporte a integração com o TOTVS API Services ou que possa ser customizado. A adesão e os planos disponíveis estão disponíveis na [TOTVS Store](https://totvs.store/).

Atenção

Consultar a linha de produto pra saber se a mesma possui suporte ao TOTVS API Services

# Serviços disponíveis

---

Apenas os serviços abaixo estão disponíveis no plano pago, ou seja, os demais serviços do Mashup continuam funcionando normalmente.

| Serviço |
| --- |
| *Receita Federal - Consulta de CNPJ* |
| *Receita Federal - Consulta de CPF* |
| *Receita Federal - Consulta de CPF e CNPJ* |
| *Receita Federal - Consulta Simples Nacional* |
| *Sintegra - Consulta Nacional ao Cadastro* |
| *Sintegra - Consulta Unificada ao Cadastro* |
| *Suframa - Consulta Situação Fornecedor* |

Alteração dos endpoints

Para que não tenhamos quebra nas requisições existente para os serviços acima, as chamadas existentes ao Mashup não serão alteradas. Sendo necessário apenas o envio dos headers conforme descrito no tópico abaixo.

Demais Serviços

Os demais serviços disponíveis no Mashup continuam com acesso livre, caso tenhamos alterações, a lista acima sofrerá revisão.

# Pré-requisitos

---

Para que o produto possa consumir estes serviços é necessário o envio das propriedades abaixo no *header* da requisição.

Abaixo as informações obrigatórias e opcionais enviadas via cabeçalho.

| Propriedade | Exigência | Descrição |
| --- | --- | --- |
| **totvsmashup-api-key** | Obrigatório | Após adesão ao plano do TOTVS API Services, é disponibilizado para o cliente uma API KEY. Esta chave deve ser informada ao produto para que a mesma seja enviada em todas requisições realizadas ao Mashup. |
| **totvsmashup-product-name** | Obrigatório | O Produto envia seu nome. Ex.: (RM | PROTHEUS | DATASUL) |
| **totvsmashup-product-module** | Obrigatório | O Produto envia seu módulo que está consumindo o serviço do TOTVS API Services. Ex.: (Fopxxxx | SIGAFAT) |
| **totvsmashup-customer-ls-id** | Opcional | O Produto envia o ID do cliente no License Server; |
| **totvsmashup-product-routine** | Opcional | O Produto envia sua rotina que está consumindo o serviço do TOTVS API Services. Ex.: (FopFuncAction | mata030) |
