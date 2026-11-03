---
content_hash: 4dc906ceab6c8364432459ebb23f7dd8d9f8779d59b1b5332a64663719f908f9
fetched_at: '2026-06-29T00:05:52.196107+00:00'
page_id: '1058200239'
product: rm
source: tdn-rm
title: FOPTRP0031 - Demonstrativo Contábil da Folha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058200239
version: 14
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

**A partir dos patches:**

+ 12.1.2606 e Superiores

## **02. V****ISÃO GERAL**

Este objeto de negócio foi desenvolvido para extrair os lançamentos contábeis originados da Folha de Pagamento utilizando o [objeto de negócio de contabilização](https://tdn.totvs.com/pages/viewpage.action?pageId=1058469154), permitindo a conferência detalhada dos débitos, créditos e centros de custo antes ou após a integração contábil.

#### **Regras de Filtro (Importante)**

Para garantir a performance e a segurança dos dados, o objeto possui uma lógica de filtros obrigatórios:

**Importante - Regras de Preenchimento:** O objeto exige que todos os parâmetros declarados recebam um valor para processar a requisição. Para alternar entre os tipos de filtro, utilize a lógica abaixo:

* **Filtrar por Lote:** Informe o(s) número(s) do(s) lote(s) e preencha os campos de Mês e Ano com **-1**.
* **Filtrar por Período:** Preencha o Mês e o Ano desejados e informe o valor **-1** no campo de Lote.
* **Coligada:** Este campo é mandatório e deve sempre receber um código de coligada válido.

|  |  |  |
| --- | --- | --- |
| Coligada | PFUNC.CODCOLIGADA | Filtra código de coligada. |
| Codlote | PFUNC.CHAPA | Filtra pela matrícula do funcionário. |
| Mês referência | PPARTIDA.DATA | Filtra o mês de lançamento |
| Ano referência | PPARTIDA.DATA | Filtra o ano de lançamento |

A visualização do relatório será conforme o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Complemento |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| --- | --- | --- |
| Nome da empresa | GCOLIGADA.NOMEFANTASIA | Lista o nome da empresa |
| CNPJ | GCOLIGADA.CGC | Lista o CNPJ da empresa |
| Período | PPARTIDA.DATA | Lista a data do periodo |
| Descrição da conta | CCONTA.DESCRICAO | Lista a descrição da conta |
| Centro de custo | PPARTIDA.CODCUSTO | Lista o código de custo |
| Verbas/Eventos | PPARTIDA.CODHISTP | Lista o código do evento |
| Descrição da Verba/Evento | CHISTP.DESCRICAO | Lista a descrição do evento |
| Contábil | PPARTIDA.VALOR | Lista o valor contábil |
| Débito | PPARTIDA.VALOR | Lista o valor |
| Crédito | PPARTIDA.VALOR | Lista o valor |
| Contrapartida | PPARTIDA.CREDITO | Lista o valor crédito (contrapartida) |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Ações', e configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros selecionados para geração do relatório.

  Filtro:

**DICAS:**

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.
* Só podemos colocar um mês para geração da contabilização. Não temos a opção de filtrar por período.

## **04. TABELAS UTILIZADAS**

* CLCTLOTE
* PPARTIDA
* GCOLIGADA
* GFILIAL
* CCONTA
* CHISTP
