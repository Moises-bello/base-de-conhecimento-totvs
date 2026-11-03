---
content_hash: 4a21f334d9dc0adfdc1523c883af4301adf81e0342421fdfc9e7cbc595bb4f67
fetched_at: '2026-06-29T00:11:43.099306+00:00'
page_id: '802003513'
product: rm
source: tdn-rm
title: FOPTRP0006 - Relatório de Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802003513
version: 12
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310.112  e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir Histórico Salarial.  Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Código Cargo | Filtra pelo cargo atual do funcionário. | PFUNCAO.CARGO |
| Centro de Custo | Filtra pelo centro de custo cadastrado na seção do funcionário. | PSECAO.NROCENCUSTOCONT |
| Código Coligada | Filtra pelo código da coligada. | PFUNC.CODCOLIGADA |
| Código Departamento | Filtra pelo código de departamento cadastrado na seção do funcionário. | PSECAO.CODDEPTO |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Data Filtro | Filtra pela data de mudança do histórico salarial do funcionário. O filtro de data é aplicado sobre o campo DTMUDANCA. Funcionários que não possuem registros de alteração salarial a partir da data informada são omitidos da listagem, pois o objetivo do relatório é apresentar a evolução salarial e não apenas o cadastro estático. | PFHSTSAL.DTMUDANCA |
| Exibir Salário | Opção para exibir ou não exibir o campo no relatório. |  |
| Filial | Filtra pelo código de filial do funcionário. | PFUNC.CODFILIAL |
| Imprime Histórico | Exibe ou não o histórico do funcionário. | (Sim - 1-Exibir / Não - 2-Não exibir) |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Tipo Pagamento | Filtra pelo tipo de pagamento para o funcionário. | PFUNC.CODRECEBIMENTO |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário.

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| **Campo** | **Campo na Tabela** |
| --- | --- |
| Nome da Coligada | NOME |
| Matricula | CHAPA |
| Nome | NOME |
| Tipo de Pagto | CODRECEBIMENTO |
| Departamento | NOME |
| Código Centro de Custo | NROCENCUSTOCONT |
| Salário Atual | SALARIO |
| Função Atual | NOME |
| Cargo Atual | NOME |
| Dt Alteração | DTMUDANCA |
| Dt Process. | DATADEREFERENCIA |
| Motivo | MOTIVO |
| Função | NOME |
| Cargo | NOME |
| Carga Horária | JORNADA |
| Salário Mês | SALARIO |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2)  Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório.

DICA

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* PFUNC
* PFUNCAO
* PSECAO
* PCARGO
* PFHSTSAL
* PFHSTFCO
