---
content_hash: 95cb2c6223968db2b82aa5a233c3688079ac0ea20a6fe05ab1c94904b3ae8cc6
fetched_at: '2026-06-29T00:11:50.498617+00:00'
page_id: '841679400'
product: rm
source: tdn-rm
title: Impressão de Parciais em Lote
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841679400
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Impressão de Parciais em Lote**
3. **Imprimir Relatórios**

sumarioVisão Geral

## **01. VISÃO GERAL**

Este módulo tem como objetivo efetuar a geração de relatórios referente as parciais, como Extrato ou Guias TISS.

O processamento dos relatórios permite a visualização de um arquivo PDF ou impressão direta.

Todos os itens processados são gerados em apenas um arquivo PDF.

Impressão de Parciais em Lote

## **02. IMPRESSÃO DE PARCIAIS EM LOTE**

O módulo de Impressão de Parciais em Lote está localizado em Faturamento > Particular e Convênios > Impressão de Parciais em Lote.

Ao acessar o módulo, a nova tela será exibida sem exibir a tela de filtro padrão do RM.  
O filtro deve ser feito utilizando os campos no módulo, que são:

* Unidade de faturamento - Obrigatório
* Convênio - Obrigatório
* Apenas convênios ativos  
  Este campo por padrão fica marcado, e define se retornará apenas convênios ativos ao efetuar a pesquisa dos convênios.
* Período - Obrigatório  
  Início e fim de um período, por padrão sendo o primeiro e último dia do mês atual.
* Paciente - Opcional
* Tipo Paciente - Opcional  
  Com as opções Todos, Externos e Internos
* Status Conta - Opcional  
  Com as opções Todos, Cancelado, Elaboração, Em Aberto, Fechado, Importado e Liberado para Faturamento
* Status Parcial - Opcional  
  Com as opções Todos, Cancelado, Elaboração, Faturada, Importado e Liberada

Após preencher os filtros, deve-se clicar no botão "Filtrar", e os registros serão carregados exibindo dados do atendimento, parcial e paciente.

Imprimir Relatórios

## **03. IMPRIMIR RELATÓRIOS**

Nesta rotina foi adicionado o processo "Imprimir Relatórios", onde este permite a seleção de um ou vários registros.

Ao executar o processo, será exibida uma tela para que o usuário informe:

* Tipo de Conta  
  Seleção única com as opções "Conta Convênio" e "Conta Particular"
* Tipo de Relatório  
  Seleção múltipla com as opções "Extrato", "Guia TISS" e "Relação"
* Tipo de Geração  
  Seleção única com as opções "Visualizar" e "Imprimir"
* Ordenação de Impressão

Após selecionar as opções desejadas e clicar em "Executar", a geração dos relatórios será efetuada.

Ao fim do processamento, se a opção "Tipo de Geração" estiver selecionada "Visualizar", serão exibidos os relatórios gerados com base nos registros selecionados e opções selecionadas na tela do  processo.

E se a opção "Tipo de Geração" estiver selecionada "Imprimir", exibirá uma tela de configurações de impressão.

Uma observação, é que os relatórios gerados de Extrato e Guia TISS, são os mesmos existentes na elaboração de contas.

Estes são processados um a um, ou seja, se selecionar três registros e marcar as opções Extrato e Guia TISS, serão gerados seis relatórios.

Já o relatório de relação sempre será gerado apenas um relatórios com os dados de todos os registros selecionados, agrupados por convênio.
