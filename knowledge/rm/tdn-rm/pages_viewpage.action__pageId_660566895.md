---
content_hash: 62e02a7ca9a7073c9d22cfb82b305cde50b7f0d9360eea29950e5e234ffbd7a9
fetched_at: '2026-06-29T00:11:13.420657+00:00'
page_id: '660566895'
product: rm
source: tdn-rm
title: RM Portal -  Gestão de Férias - Ocultar Autônomos e Diretores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=660566895
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Construção Obras e Projetos  TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | RM Portal |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-1641](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-1641) |

## **2. SITUAÇÃO/REQUISITO**

Ao acessar o módulo de Gestão de Férias no RM Portal são apresentados os funcionários do tipo de funcionário 'A - Autônomo' e 'D - Diretor'. O cliente necessita que não sejam apresentados na tela de Gestão de Férias, pois Autônomos e Diretores não tem direito a férias, tornando desnecessária a apresentação deles nesta tela.

## **03. SOLUÇÃO**

Foi criado em  RH | Folha de Pagamento | Configurações | Parametrizador | RM Portal | Grupo de Acesso | Supervisores, o parâmetro 'Ocultar Autônomos e Diretores na Gestão de Férias'. Ao marcar este parâmetro não serão apresentados os funcionários do tipo de funcionário 'A - Autônomo' e 'D - Diretor' na tela de Gestão de Férias.

**1) Cadastro de funcionários:**

**a) Diretor:**

**b) Autônomo:**

**2) Tela de parâmetros - Supervisores:**

**a)** Tela de **Gestão de Férias - RM Portal** - Com o parâmetro '**Ocultar Autônomos e Diretores na Gestão de Férias**' - **Desmarcado**:

**3) Tela de parâmetros - Supervisores:**

Tela de **Gestão de Férias - RM Portal** - Com o parâmetro '**Ocultar Autônomos e Diretores na Gestão de Férias**' - **Marcado**:

## **04. DEMAIS INFORMAÇÕES**

O default do parâmetro será desmarcado. Caso o usuário queira utilizar o recurso, deverá editar os grupos de acesso existentes e marcar o parâmetro.

## **05. ASSUNTOS RELACIONADOS**

**[Parâmetros do RM Portal](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719215)**

**[Atualizações - Reforma Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=287073735)**
