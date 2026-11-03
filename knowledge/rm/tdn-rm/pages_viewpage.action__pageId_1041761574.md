---
content_hash: e323183811a772c04b52185225c8bde4fc2318fc1b70495b9bc5eb6f21648fed
fetched_at: '2026-06-29T00:05:49.791666+00:00'
page_id: '1041761574'
product: rm
source: tdn-rm
title: FOPTRP0025 - Ficha de Salário Família
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1041761574
version: 24
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2602 e Superiores
* [DT - Smart View - Ficha de Salário Família](https://tdn.totvs.com/pages/viewpage.action?pageId=1041777263)

## **02. V****ISÃO GERAL**

Relatório para emitir lista dos dependentes de salário-família. Nesse relatório temos os seguintes filtros disponíveis:

|  |  |  |
| --- | --- | --- |
| CHAPA | Filtra pela chapa do funcionário. | PFUNC.CHAPA |
| CPF | Filtra pela situação do funcionário. | PPESSOA.CPF |
| Seção | Filtra pelo tipo de funcionário. | PFUNC.CODSECAO |
| Situação | Filtra pela filial associada ao funcionário. | PFUNC.CODSITUACAO |
| Filial | Filtra pela chapa do funcionário. | PFUNC.CODFILIAL |
| Tipo Funcionário | Filtra pelo valor do salário do funcionário | PFUNC.CODTIPO |
| Data de Admissão | Filtra data Admissão | PFUNC.DATAADMISSAO |

A visualização do relatório será conforme o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponíveis:

| Campo do Relatório | Campo da Tabela | Complemento |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| Empresa | GCOLIGADA.NOMEFANTASIA |  |
| CNPJ | GCOLIGADA.CGC |  |
| Endereço | GCOLIGADA.RUA |  |
| Bairro | GCOLIGADA.BAIRRO |  |
| CEP | GCOLIGADA.CEP |  |
| Cidade | GCOLIGADA.CIDADE |  |
| UF | GCOLIGADA.ESTADO |  |
| DADOS DO EMPREGADO | | |
| CHAPA | PFUNC.CHAPA |  |
| NOME | PFUNC.NOME |  |
| CTPS | PPESSOA.CARTEIRATRABALHO |  |
| SÉRIE | PPESSOA.SERIECARTTRABALHO |  |
| DATA DE ADMISSÃO | PFUNC.DATAADMISSAO |  |
| DATA DE DEMISSÃO | PFUNC.DATADEMISSAO |  |
| ENDEREÇO | PPESSOA.RUA |  |
| BAIRRO | PPESSOA.BAIRRO |  |
| CEP | PPESSOA.CEP |  |
| CIDADE | PPESSOA.CIDADE |  |
| UF | PPESSIA.ESTADO |  |
| DEPENDENTES | | |
| NUMERO ORDEM | PFDEPEND.NRODEPEND |  |
| NOME DO FILHO | PFDEPEND.NOME | exceto PFDEPEND.GRAUPARENTESCO = 6 e 7 |
| DATA DE NASCIMENTO | PFDEPEND.DTNASCIMENTO |  |
| CPF | PFDEPEND.CPF |  |
| CARTÓRIO | PFDEPEND.CARTORIO |  |
| NUMERO REGISTRO | PFDEPEND.NROREGISTRO |  |
| NUMERO LIVRO | PFDEPEND.NROLIVRO |  |
| NUMERO FOLHA | PFDEPEND.NROFOLHA |  |
| MATRICULA | PFDEPEND.CHAPA |  |

## **03.  EXEMPLO DE UTILIZAÇÃO**

1)Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

3) Filtros selecionados para geração do relatório.

DICA

* É necessário que todos os campos do filtro sejam preenchidos.  Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GFILIAL
* GDEPTO
* PSECAO
* PFUNC
