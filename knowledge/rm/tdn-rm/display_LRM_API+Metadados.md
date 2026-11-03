---
content_hash: 0709801fd3decd40492ceb28f09e9fb1062f5a4ef617a96286518dae88921720
fetched_at: '2026-06-29T00:10:46.820402+00:00'
page_id: '556378600'
product: rm
source: tdn-rm
title: API Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/API+Metadados
version: 4
---

# Sumário

---

10Sumário

# Objetivo

---

     Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

# 1 - Métodos

---

     Existem duas APIs de Metadados: uma para buscar a estrutura (schema) do metadado em formato compatível com o componente [Dynamic Form do PO-UI](https://po-ui.io/documentation/po-dynamic-form) e outra para os dados registrados no formulário.

**Schema API**

Esta API retorna a estrutura do metadado, como já informado acima. Ela aceita apenas o método GET e deve ser chamada da seguinte forma:

Chamada Schema API

http://{domínio}:{porta}/api/framework/v1/metadata/schema/form/{idProjeto}

Nesta chamada, *idProjeto* representa o código do Projeto de Metadados que foi gerado.

**Data API**

Esta API possui os verbos GET, POST, PUT e DELETE e permite o gerenciamento dos dados do formulário gerado. Ela deve ser chamada da seguinte forma:

Chamada Dados API

http://{domínio}:{porta}/api/framework/v1/metadata/data/{idProjeto}

# 1.1 - GET Schema API

---

Veremos agora mais detalhes sobre a API de schema de Metadados.

GET Schema APIExpandirExemplo de resultado

O resultado da API depende dos campos cadastrados no formulário dinâmico. Segue abaixo um exemplo de resposta desta API.

Ver resultado JSONjsResultado JSONtrue

# 1.2 - Data API

---

As regras e dados informados na API de dados para os preenchimentos do Metadado informado na requisição depende dos campos e configurações dos mesmos dentro projeto criado.

Chamada Data API

Segue abaixo um exemplo de retorno de dados em uma chamada de busca de listagem para um formulário com o schema do exemplo acima.

ExpandirjsExemplo de GET Alltrue

O funcionamento da API em todos os verbos se dá conforme o [Padrão de API TOTVS](https://tdn.totvs.com/display/public/INT/Guia+de+implementacao+das+APIs+TOTVS). No entanto, algumas funcionalidades como seleção de colunas, paginação, objetos complexos e tabelas relacionadas ainda não estão disponíveis.
