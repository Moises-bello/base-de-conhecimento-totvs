---
content_hash: 173f91d636457262a495e92ff69ee73d39c79899ffaaf6a7c8b4b3440b3d35a8
fetched_at: '2026-06-29T00:09:50.173225+00:00'
page_id: '435105424'
product: rm
source: tdn-rm
title: Relatórios - Vendas Canceladas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105424
version: 13
---

Relatório responsável por retornar  os dados das vendas que foram canceladas, havendo ou não distrato.

**Pré-condições:**

**1-** O usuário deve ter permissão para executar os relatórios de Empreendimentos. As permissões podem ser acessadas em: TOTVS RM / Serviços Globais/ Segurança/ Perfis/ Sistema - Incorporação.

**2-** O usuário deve ter importado a estrutura dos relatórios abaixo, acessando: TOTVS RM / Serviços Globais/Gestão/ RM Reports/ Processo/ Importar Estrutura de Relatório.

* VC001 Vendas Canceladas

**3-** Ter efetuado o Distrato de um contrato de venda através do anexo: **Contratos/ Contrato de Venda/ Anexo / Distrato Contratual.**

**Executando os Relatórios**

**Passo 1-** Acesse: TOTVS RM/ Projetos/ Incorporação/ Relatórios/ Vendas Canceladas.

**Passo 2-** Será exibido o formulário responsável por gerar o relatório desejado. Os  campos de preenchimento obrigatório são exibidos na tela destacados em negrito. Os campos do formulário são:

* **Relatório:** Campo responsável por definir qual relatório será executado, de acordo com as estruturas de relatório que foram importadas na pré-condição 2.
* **Lista de Empreendimentos:** Lista de filtragem por empreendimento. Permite adicionar até 10 empreendimentos, e eles podem ser excluídos da lista
* **Período:** Data de Início e Fim para definir um período  de pesquisa por contratos de venda cancelados
* **Lista do Tipo de Cancelamento:** Define uma lista de tipos de cancelamentos  a fim de filtrar o relatório.

**Passo 3-** Preencha os campos e clique em "Executar"

Atenção

Caso não haja vendas canceladas no período solicitado, o sistema exibirá a exceção abaixo, em uma janela à parte:
