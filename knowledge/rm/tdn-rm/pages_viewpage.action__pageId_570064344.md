---
content_hash: e0539a8bef4abf6374d0eb31f40aa65f044f01d8c73f9bc143ec5e7ca49fb4e2
fetched_at: '2026-06-29T00:10:52.121954+00:00'
page_id: '570064344'
product: rm
source: tdn-rm
title: DT - Geração de Remessa de Pagamento Layout Múltiplas Remessas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570064344
version: 16
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Totvs Gestão Financeira |
| Função: | Geração de arquivo de remessa de pagamento |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FINANCEIRO01-15115 |

## **02. SITUAÇÃO/REQUISITO**

Facilitar a geração do arquivo de remessa de pagamentos para layouts de múltiplas remessas bancárias,  onde a finalidade será a geração de um único arquivo. Desta forma, o sistema não irá gerar um arquivo por convênio, mas somente um arquivo com todas remessas empilhadas.

## **03. SOLUÇÃO**

Criação do processo Remessa de Pagamento Layout Múltiplas Remessas para possibilitará à geração somente um arquivo de remessa de pagamento para vários convênio. O layout a ser utilizado no processo deverá ser especificado no manual do banco com a **finalidade de geração de múltiplas remessas** em um único arquivo. Isto é, o layout permitirá a geração de um único arquivo com **várias remessas empilhadas**. Exemplo:

| Remessa | Arquivo |  |
| --- | --- | --- |
| Remessa 1 | Cabeçalho | Seq00001 |
|  | Documento 1 | Seq00002 |
|  | Documento 2 | Seq00003 |
|  | Rodapé | Seq00004 |
| Remessa 2 | Cabeçalho | Seq00001 |
|  | Documento 1 | Seq00002 |
|  | Documento 2 | Seq00003 |
|  | Rodapé | Seq00004 |
| Remessa 3 | Cabeçalho | Seq00001 |
|  | Documento 1 | Seq00002 |
|  | Documento 2 | Seq00003 |
|  | Rodapé | Seq00004 |

O processo ficará disponível no menu Movimentações Bancarias → Integração Bancária → Processo Múltiplas Remessas → Remessa de Pagamento.

Será preciso conceder permissão de acesso ao menu para execução do processo e a permissão será através do perfil associado ao usuário de acessoa ao sistema.

O processo terá os campos:

* Identificador do Lote do Borderô de Pagamentos: Informar o número do lote gerado pela execução do processo . É possível também pesquisar pela descrição do borderô de pagamentos.
* Diretório de Destino: Informar o diretório de destino onde o arquivo será salvo.
* Nome do Arquivo: Nome do arquivo de remessa a ser gerado.

  ATENÇÃO

  A definição do nome do arquivo a ser gerado, pode ser composto de uma parte fixa e uma parte variável.

  Na parte variável pode ser usado, o seguinte:  
  # = caracter para definir o número sequencial da remessa, com zero a esquerda  
  DDMM, MMYYYY ou DDMMYYYY = informação da data de geração da remessa

  Eemplo: R240\_COOP\_DDMMYYYY\_#####.TXT => R240\_COOP\_04102016\_00001.TXT
* Extensão: Informar a extensão do arquivo de remessa a ser gerado
* Layout de Remessa: Informar o layout a ser utilizado na geração do arquivo que possibilitar o empilhamento de múltiplas remessas.

A estrutura do layout a ser usado no gerador de saída para esse processo é um pouco diferente dos layouts já existentes para as remessas de pagamento.

ATENÇÃO

Como objetivo desse processo é a geração de um único arquivo com **várias remessas empilhadas.** É necessário verificar se o banco tem **layout para tal objetivo** antes da utilização do mesmo**.**

   O layout a ser criado no gerador de saída tem que ter as seguintes características:

* No tipo de contexto Parâmetros da Geração deve ter os parâmetros :
  + Borderos: Parâmetro do tipo filtro onde no campo "Tabela" deve usar a tabela "Borderô de Pagamento"
  + DataSistema: Parâmetro do tipo data
  + IdLoteBordero: Parâmetro do tipo número inteiro
* No tipo de contexto Conjunto de Dados deve as seguintes características:
  + Aba Propriedades
    - Tabela Base: Utilizar a tabela de "Lançamento" (FLAN)
    - Filtro: Usar o campo FBordero.IdLoteBordero com link no IdLoteBordero do contexto de parâmetros de geração
    - Filtro do Usuário: Utilizar como tabela base no filtro do usuário a tabela "Borderô de Pagamentos" (FBORDERO)
    - Campos: Para obter o número da remessa do convênio o link deve ser da tabela "Lançamento" (FLAN) para a tabela "Borderô de Pagamentos" (FBORDERO). E da  tabela "Borderô de Pagamentos" (FBORDERO) para a tabela "Preparação dados pré-processados na geração remessa de pagamentos para layout bancário múltiplas remessas" (FPREPAREREMPAG)

      ATENÇÃO

      A tabela "Preparação dados pré-processados na geração remessa de pagamentos para layout bancário múltiplas remessas" (FPREPAREREMPAG) é utilizada somente no processo Geração de Remessa de Pagamento Layout Múltiplas Remessas.
  + Aba Parâmetros:
    - Parâmetro IdLoteBordero: Fazer link com o IdLoteBordero  do contexto de parâmetros de geração
    - Filtro do Usuário: Fazer link com o Borderos do contexto de parâmetros de geração

## **04. DEMAIS INFORMAÇÕES**

**1. Esse processo tem o objeto de gerar o arquivo de remessa de pagamento com a utilização do layout de múltiplas remessas do banco. Isto é, um layout que permite a geração de um único arquivo com várias remessas empilhadas 2. O arquivo gerado será pelo identificador de lote do Borderô de Pagamentos. O arquivo será gerado de acordo com as informações presentes nos campos abaixos. Esses campos serão preenchidos automaticamente pelas informações presente no primeiro convênio encontrado pelo identificador de lote. 3. Os borderôs serão filtrados internamente para carregar apenas borderôs autorizados que possuem lançamentos.IMPORTANTE!**

## **05. ASSUNTOS RELACIONADOS**


div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
.aui-tabs.horizontal-tabs>.tabs-menu>.menu-item.active-tab a::after {
background: #FF9900; !important
}
.menu-item.active-tab {
border-bottom: none !important;
}
]]>
