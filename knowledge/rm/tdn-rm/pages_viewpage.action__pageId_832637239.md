---
content_hash: bbe9c6ab14ca1a7c1e5e6e148e92da41230ae6e1cfae437db48b8d670f56d1bb
fetched_at: '2026-06-29T00:11:49.386414+00:00'
page_id: '832637239'
product: rm
source: tdn-rm
title: DT - Fórmula Visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832637239
version: 13
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Fórmula Visual |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-9093](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9093) |

## **02.** **VERSÕES**

Lembrando que, será a partir dos patches:

* 12.1.2306.238
* 12.1.2310.179
* 12.1.2402.115 e superiores

## **03.** **SITUAÇÃO/REQUISITO**

Ao tentar cadastrar um funcionário utilizando a atividade "adicionar registro" via fórmula visual, o sistema apresenta o seguinte erro: "**A coluna 'ROWVALIDA' não pertence à tabela PFunc.**"

## **04.** **SOLUÇÃO**

**1. Correção do problema da coluna ROWVALIDA:**

Identificamos o problema principal que afetava a coluna ROWVALIDA e implementamos uma correção no produto.

**2. Adição da coluna ISFVISUAL:**

Para que o recurso de geração automática de chapa funcione devidamente, é necessário adicionar a coluna **ISFVISUAL** na estrutura da fórmula visual. Você pode fazer isso facilmente usando a atividade "Criar Coluna".

**3. Preenchimento dos campos complementares:**

Devido a algumas limitações da fórmula visual, é necessário que preencha manualmente os campos complementares dentro do produto. Para facilitar esse processo, preparamos alguns prints que ilustram passo a passo como fazer isso.

É necessário adicionar a atividade "Criar coluna" dentro da estrutura da fórmula conforme a imagem abaixo. Essa atividade é necessária para funcionamento do recurso de Geração Automática de chapa:

Essa atividade dever ser criada conforme a imagem abaixo.

Devido à limitação de admissão via Fórmula Visual, para preencher os campos complementares, é necessário realizar esse preenchimento diretamente no Produto, na tela de Cadastro do funcionário.

Menu Funcionário | Campos Complementares:

Menu Funcionário | Campos Compl(Pessoa)

Para mais informações:
