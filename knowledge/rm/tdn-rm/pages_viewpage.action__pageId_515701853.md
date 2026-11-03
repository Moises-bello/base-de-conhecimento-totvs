---
content_hash: 79bbc7757fb8b5f516580621bd774c96e5e3cbc57bf233d6ece0a14fc9ba8297
fetched_at: '2026-06-29T00:10:27.024630+00:00'
page_id: '515701853'
product: rm
source: tdn-rm
title: Utilizando a atividade "Importar registros na tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515701853
version: 9
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Importar registros na tabela" tem por função clonar o DataTable de sua estrutura, recriar as rows e adiciona-las no DataSet.

**02. EXEMPLO DE UTILIZAÇÃO**

Descrição dos campos da atividade "Importar registros na tabela":

**Atividade:**

* **Nome:**Nome da atividade
* **Descrição:** Descrição da atividade
* **Habilitado:** Define se a atividade estará em uso ou não.

**Geral:**

* **DataSet:** Representa um cache de dados na memória.
* **DataTable:** Especifica o suporte para inicialização transacionada.

**RM.NET:**

* **Dados do Usuário:** Dados do usuário (OwnerData) de parâmetro da execução da atividade

**Exemplo de Utilização:**

     Abaixo exemplos de utilização da atividade:

* Executar uma consulta SQL de um BD externo (utilizando a [Atividade Executar Consulta SQL](https://tdn.totvs.com/x/hJi2C)) e adicionar em um ReadView as colunas de um outro banco.
* Utilizar duas [Atividade](https://tdn.totvs.com/x/ogLvC) [Ler Visão](https://tdn.totvs.com/x/ogLvC) (GCOLIGADA e GUSUARIO por exemplo) e utilizar a "Atividade de importar registros na tabela" para adicionar a tabela de usuário dentro do DataSet de Coligada. Com isso o DataSet passa a ter duas tabelas.
