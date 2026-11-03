---
content_hash: 95a6fda6baab068c4d89ba1b95b3f059633c59ec9e8cca0aedf892ff1594c177
fetched_at: '2026-06-29T00:12:14.006109+00:00'
page_id: '963022204'
product: rm
source: tdn-rm
title: Importação Empréstimos FEBRABAN / Crédito do Trabalhador - Alteração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963022204
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Importação Empréstimos FEBRABAN / Crédito do Trabalhador - Alteração.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

IMPORTANTE:

Para identificar se já existe o empréstimo cadastrado para o colaborador será verificado a existência de empréstimo com o mesmo número de contrato e matrícula eSocial do cadastro de funcionários e assim processar a alteração do cadastro de empréstimo via [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true).

Quando for necessário uma alteração, a importação poderá ocorrer nos campos:

* Comp. final desc. Mês e Comp. final desc. Ano (se ocorrer negociação) - 05/2028
* Nro. Parcela - 37
* Nro. Parcelas Pagas - 1
* Valor Original - 18126
* Valor da Parcela - 503.5

Então usando o arquivo com os mesmos dados de matricula e contrato a importação alterará os campos listados acima

IfConcessoraCodigo;IfConcessoraDescricao;Contrato;Cpf;Matricula;InscricaoEmpregadorCodigo;InscricaoEmpregadorDescricao;NumeroInscricaoEmpregador;NomeTrabalhador;NomeEmpregador;DataInicioContrato;DataFimContrato;CompetenciaInicioDesconto;CompetenciaFimDesconto;TotalParcelas;ValorParcela;ValorEmprestimo;ValorLiberado;QtdPagamentos;QtdEscrituracoes;CategoriaTrabalhadorCodigo;CategoriaTrabalhadorDescricao;Competencia;InscricaoEstabelecimentoCodigo;InscricaoEstabelecimentoDescricao;NumeroInscricaoEstabelecimento  
001;Banco do Brasil;XXXXXXXXXX;XXXXXXXXXXX;XXXXXXXXXX;1;CNPJ;XX.XXX.XXX/XXXX-XX;FULANO DE TAL;XXXXXXXXXX;22/04/2025;;05/2025;05/2028;37;503.5;18126;15000;1;1;101;Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT;04/2025;1;CNPJ;XX.XXX.XXX/XXXX-XX

Após execução do processo acima o cadastro de empréstimo ficou com os seguintes dados alterados.

## **03.** **TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
