---
content_hash: 91448ec0d9994dbb4ddc8555c5b43adad3bec5c8cc37c97010425e53c8a05705
fetched_at: '2026-06-29T00:11:39.914432+00:00'
page_id: '790657164'
product: rm
source: tdn-rm
title: FOPTRP0002 - Lista de Aniversariantes
type: documentation
url: https://tdn.totvs.com/display/LRM/FOPTRP0002+-+Lista+de+Aniversariantes
version: 19
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VERSÕES**

false

**A partir dos patches:**

* 12.1.2310 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir lista de aniversariantes. Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Mês | Filtra pelo mês desejado do ano. | PFUNC.CODSITUACAO |
| Cód. Situação | Filtra pela situação do funcionário. | PFUNC.CODTIPO |
| Cod. Tipo | Filtra pelo tipo de funcionário. | PFUNC.CODFILIAL |
| Matrícula | Filtra pela filial associada ao funcionário. | PFUNC.CHAPA |
| Filial | Filtra pela chapa do funcionário. | PFUNC.SALARIO |
| Salário | Filtra pelo valor do salário do funcionário. |  |
| Idade | Filtra por uma idade especifica digitada. Calculo da idade é considerado conforme o ano da geração. Exemplo: data da geração 22/08/2023 e data de nascimento 15/12/1989. Idade que será apresentada é 34 anos. |  |
| Cod. Departamento | Filtra pela seção do cadastro de funcionários. | PFUNC.SECAO |
| Centro de Custo | Filtra pelo centro de custo da seção do funcionários. | PSECAO.NROCENCUSTOCONT |
| Nome | Filtra pelo nome. | PFUNC.NOME |
| Exibir Salário | Opção para exibir ou não exibir o campo no relatório. |  |
| Exibir Centro de Custo | Opção para exibir ou não exibir o campo no relatório. |  |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| **Campo** | **Campo na Tabela** |
| --- | --- |
| Código da Filial | PFUNC.CODFILIAL |
| Matricula | PFUNC.CHAPA |
| Nome | PFUNC.NOME |
| Departamento | PSECAO.NOME |
| Código Centro de Custo | PSECAO.NROCENCUSTOCONT |
| Descrição Centro de Custo | PCCUSTO.NOME |
| Salário | PFUNC.SALARIO |
| Idade | Calculo da idade é considerado conforme o ano da geração. Exemplo: data da geração 22/08/2023 e data de nascimento 15/12/1989. Idade que será apresentada é 34 anos. |
| Aniversário | PPESSOA.DTNASCIMENTO |
| Código da Coligada | PFUNC.CODCOLIGADA |
| Situação | PFUNC.CODSITUACAO |
| Tipo | PFUNC.CODTIPO |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

DICA

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* A impressão da logo só ocorrerá caso uma coligada seja selecionada no filtro.
* Clicando no ícone  o relatório é apresentado em tela inteira.
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GFILIAL
* GDEPTO
* PSECAO
* PFUNC
