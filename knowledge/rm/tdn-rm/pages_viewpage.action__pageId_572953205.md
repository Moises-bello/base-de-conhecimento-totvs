---
content_hash: 4410ad9eeb0cd773205573ce6599870e09639b8bb96ef9623d74ed45e6ba718c
fetched_at: '2026-06-29T00:10:52.468928+00:00'
page_id: '572953205'
product: rm
source: tdn-rm
title: Validação Senha TISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572953205
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

**Para atendimento Externo:**

Caso exista mais de uma Guia de Consulta ou de SPSADT para o atendimento utilizando o mesmo número de guia, as seguintes validações serão executadas:

* Verifica se as “Senhas” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Senhas distintas. Número da guia: 12112”.

* Verifica se o “Tipo de Guia” são iguais, caso não, retorna a mensagem de erro “O número de guia foi utilizado para tipos diferentes. Número da guia: 12112”.

* Verifica se a “Data da Guia” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Datas Distintas. Número da guia: 12112”.

* Verifica se as “Datas de Validade da Senha” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Datas de Validade distintas. Número da guia: 12112”.

**Para atendimento Interno:**

Caso exista mais de uma Guias de Resumo de internação ou de Prorrogação para o atendimento utilizando o mesmo número de guia, as seguintes validações serão executadas:

* Verifica se as “Senhas” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Senhas distintas. Número da guia: 11111”.

* Verifica se o “Tipo de Guia” são iguais, caso não, retorna a mensagem de erro “O número de guia foi utilizado para tipos diferentes. Número da guia: 11111”.

* Verifica se a “Data da Guia” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Datas Distintas. Número da guia: 11111”.

* Verifica se as “Datas de Validade da Senha” são iguais, caso não, retorna a mensagem de erro “A guia foi registrada com Datas de Validade distintas. Número da guia: 11111”.

## **02. EXEMPLO DE UTILIZAÇÃO**

## **03. TABELAS UTILIZADAS**

* SZATENDAUTORIZ

]]>
