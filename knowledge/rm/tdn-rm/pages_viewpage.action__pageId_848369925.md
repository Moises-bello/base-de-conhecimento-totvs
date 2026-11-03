---
content_hash: 0fb44a37c056ac4847d3ccb6a771cbab75a2aae0fc146cfa68b8ede63ef1e5d2
fetched_at: '2026-06-29T00:11:51.441431+00:00'
page_id: '848369925'
product: rm
source: tdn-rm
title: Regra de Valores para Deduções e Compensações.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848369925
version: 12
---

#f5f5f5#363636noneGerar Valores de Dedução/Compensação mesmo com Prejuízo

## **Conteúdo**



### **01. Introdução****1**

Criado uma opção no evento tributário para buscar os valores de Deduções e/ou Compensações, mesmo quando há prejuízo no período, flexibilizando assim o comportamento do sistema conforme regras do validador ECF.

A opção está disponível apenas nas abas de Dedução e Compensação, com origem contábil e terá efeito no regime tributário do Lucro Real para os tributos IRPJ e CSLL.

### **02. Cadastro****2**

O cadastro do evento tributário foi atualizado com a opção: "**Não zerar se prejuízo**". Quando marcado os valores de origem contábil que são informados nas abas Deduções e Compensações serão considerados na simulação, no detalhamento da apuração e no arquivo ECF.

Opção: Não zerar se prejuízo

**03. Simulação do Evento Tributário****3**

Na simulação do evento tributário, os valores de Deduções e Compensações serão exibidos caso a opção "**Não zerar se prejuízo**" esteja marcada.

Imagem

**04. Efeito no período de apuração****4**

Caso a opção "**Não zerar se prejuízo**" esteja marcada, na apuração dos tributos IRPJ e CSLL as deduções e compensações serão consideradas no detalhamento, mesmo quando ocorrer prejuízo.

Imagem

**05. Efeito na rotina ECF****5**

Na geração da ECF os valores de Deduções e Compensações serão gerados conforme detalhamento da apuração, no exemplo abaixo foi considerado o valor de compensação mesmo com prejuízo no mês 05/2023:

Imagem#f5f5f5#363636Outras informações


* [Regras Gerais (Eventos Tributários)](https://tdn.totvs.com/pages/viewpage.action?pageId=422546090)
