---
content_hash: d39d30351b4c88e4e81d253e2d3b175a6cd07d947fd859760318586e63ca5bb9
fetched_at: '2026-06-29T00:09:24.662175+00:00'
page_id: '423937984'
product: rm
source: tdn-rm
title: Faturamento por Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Faturamento+por+Lote
version: 12
---

No TOTVS Gestão de Estoques, compras e faturamentos, um lote representa um filtro para um ou mais contratos a serem faturados de uma só vez, em um determinado intervalo de datas ou que sejam de um mesmo cliente/fornecedor. O Lote pode conter contratos "periódicos" ou "não periódicos".  
Através da tela de Lotes de Contratos são incluídos os lotes, e posteriormente faturados. Nesta tela também é possível consultar o faturamento dos lotes, excluir ou cancelar o faturamento já feito, ou copiar um lote já criado para posteriormente alterá-lo.  
Para cada tentativa mal sucedida de faturamento, um log é gerado informando a(s) causas do fracasso. Para visualizar este log é preciso editar o lote e acessar a aba "Mensagens do Arquivo de Log"

**Filtros dos Contratos**

São considerados, ao faturar o Lote, os contratos que estejam de acordo com os **Filtros Obrigatórios** e **Filtros Opcionais** informados no cadastro do Lote.

Na pasta **Filtro do Contrato** \ **Filtros Obrigatórios** quando selecionado no campo **Natureza do Contrato** a opção **Arrendamento Mercantil,** no campo **Tipo de faturamento dos itens** será apresentado apenas a opção **Periódico.**Este campo não poderá ser alterado ao realizar alterações no Faturamento do Lote.

Na pasta **Filtros Opcionais** o campo **Dia Faturamento** é habilitado somente quando o parâmetro [Contratos | Definições de Faturamento de Contrato 2/3 | Vencimento em dias fixos](http://tdn.totvs.com/pages/viewpage.action?pageId=423938209)  está marcado.

**Cancelamento e Exclusão de um Faturamento**

A diferença entre o cancelamento e a exclusão do faturamento que no primeiro os movimentos gerados não são excluídos, apenas cancelados, já o segundo exclui todos os movimentos gerados pelo faturamento.

**Faturamento pela tela de Manutenção de Contratos**

Toda vez que um contrato é faturado pela tela de Manutenção de contratos um lote é gerado referente ao faturamento do contrato. E todas as alterações feitas pela tela de Lotes (faturamento, cancelamento e exclusão) refletem sobre os status dos itens de contrato vinculados no Lote.

Maiores Informações

* [Como Fazer - Reajuste de Contrato no Faturamento](http://tdn.totvs.com/display/LRM/Reajuste+de+Contrato+por+Faturamento)
* [Como Fazer - Previsão Financeira do Contrato por Medição](http://tdn.totvs.com/pages/viewpage.action?pageId=4813050)
* [Como Fazer - Faturamento de Itens de Contrato sem Vigência Definida](http://tdn.totvs.com/pages/viewpage.action?pageId=4813162)
* [Como Fazer - RSS de Contratos a Vencer nos próximos 30 dias](http://tdn.totvs.com/pages/viewpage.action?pageId=4813114)

Anexos

---
