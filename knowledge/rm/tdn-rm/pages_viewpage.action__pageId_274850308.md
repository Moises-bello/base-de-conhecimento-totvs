---
content_hash: 6cfb19b88588ebe24423045525f26ea11d33f7fc76d202974cc697cdd7f07d8d
fetched_at: '2026-06-29T00:08:34.884000+00:00'
page_id: '274850308'
product: rm
source: tdn-rm
title: RMFIS00005_Parametrização do Processo F100
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274850308
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.x |
| **Ocorrência:** | Parametrização do F100 |
| **Ambiente:** |  |
| **Passo a passo:** | Para a geração do F100 é necessário parametrizar o processo F100 no RM Liber(executável do módulo).    Acesse o menu Opções | Parâmetros |Processos |    Selecione o processo EFD PIS/COFINS e clique no botão Grupos/Sub-Grupos que está circulado em vermelho. O processo será aberto para edição.    Do lado direito da tela selecione o registro que é criado pelo conversor e dê um duplo clique para editá-lo.    Clique na guia Filtros e clique no botão Incluir    Informe o Tipo de Documento, o Tipo da Operação, a Base de cálculo, a Natureza da Base de Cálculo do Crédito, a data para seleção dos lançamentos financeiros e a conta contábil. Deverá ser incluído um registro para cada Tipo de Documento que irá gerar informações para o F100.  **Somente poderão ser parametrizados os tipos de documento que não possuem modelo de Documento vinculado.**        Na guia Tributos, informe os Tributos PIS e COFINS com seus respectivos CST.      Concluído o cadastro feche a tela de processos.  Antes de gerar a rotina, deverá executar o Cálculos das contribuições Doc não Escriturados. Acesse o menu Nova MDI Utilitários | Cálculos das contribuições Doc não Escriturados.    Este processo irá incluir os Tributos de Pis e Cofins nos Lançamentos Financeiros.  Este processo pode ser executado quantas vezes for necessário antes dos períodos de serem encerrados os Períodos de Apuração. |
| **Observações:** |  |
