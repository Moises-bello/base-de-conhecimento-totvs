---
content_hash: 3c784adc7349e3ca25a807178e9313abe17f749ae8dda85c9959c7ea20d2ec1a
fetched_at: '2026-06-29T00:05:48.607744+00:00'
page_id: '1025243671'
product: rm
source: tdn-rm
title: FOPTRP0023 - Contrato de Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPTRP0023+-+Contrato+de+Trabalho
version: 4
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2602 e superiores.

## **02. V****ISÃO GERAL**

Relatório para emitir as informações do Contrato de Trabalho. Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| CPF | Filtra pelo CPF | PFUNC.CPF |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Filial | Filtra pela Filial | PFUNC.FILIAL |
| Tipo Funcionário | Filtra pelo tipo funcionário | PFUNC.CODTIPO |
| Data Admissão | Filtra pela data admissão | PFUNC.DATAADMISSAO |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| Campo relatório | Tabela e campo | Complemento |
| --- | --- | --- |
| **DADOS EMPRESARIAIS** | | |
| Empresa | GCOLIGADA.NOMEFANTASIA |  |
| CNPJ | GCOLIGADA.CGC |  |
| Endereço | GCOLIGADA.RUA |  |
| Número | GCOLIGADA.NUMERO |  |
| Complemento | GCOLIGADA.COMPLEMENTO |  |
| Bairro | GCOLIGADA.BAIRRO |  |
| **DADOS CADASTRAIS** | | |
| Matrícula | PFUNC.CHAPA |  |
| Nome | PFUNC.NOME |  |
|  |  |  |
| **DADOS CONTRATUAIS** | | |
| Tipo Admissão | PFUNC.TIPOADMISSAO, PTPADMISSAO.DESCRICAO | Descrição |
| Data Admissão | PFUNC.DATAADMISSAO |  |
| Recebimento | PFUNC.CODRECEBIMENTO, PCODRECEB.DESCRICAO | Descrição |
| Salário | PFUNC.SALARIO |  |
| Tipo Contrato | PFUNC.TIPOCONTRATOPAZO | Descrição |
| Data Fim Contrato | PFUNC.FIMPRAZOCONTR |  |
| Data de Prorrogação do Contrato | PFUNC.FIMPRAZOPRORROGCONTR |  |
| Horário do Trabalho | AHORARIO |  |
| **DOCUMENTOS** | | |
| CPF | PPESSOA.CPF |  |
| Identidade | PPESSOA.CARTIDENTIDADE |  |
| **DADOS BANCÁRIOS** | | |
| Banco | PFUNC.CODBANCOPAGTO |  |
| Agência | PFUNC.CODAGENCIAPAGTO |  |
| No. Conta | PFUNC.CONTAPAGAMENTO |  |
| Operação Conta | PFUNC.OPBANCARIA |  |
| Tipo Conta | PFUNC.TPCONTABANCARIA | Descrição |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Totvs Compartilhamento, e realize a importação do relatório.

**2)** Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Mais Ações' depois em 'Executar no Smart View'.

Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

Apesar do nome do filtro estar como Matrícula, o filtro utilizado é de **Chapa** funcionário.

DICA

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* AHORARIO
* PFUNC
* PPESSOA
* PTPADMISSAO
* PCODRECEB
