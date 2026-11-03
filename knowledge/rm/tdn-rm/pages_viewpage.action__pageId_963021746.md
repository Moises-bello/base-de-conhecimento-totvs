---
content_hash: dec93c8c05617b46f1d91268584b5eb0453ce10658e5a897f128f83047a7eb97
fetched_at: '2026-06-29T00:12:14.002794+00:00'
page_id: '963021746'
product: rm
source: tdn-rm
title: Importação Empréstimos FEBRABAN / Crédito do Trabalhador - Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963021746
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Exemplo de Empréstimo Crédito do Trabalhador referente a Importação Empréstimos FEBRABAN / Crédito do Trabalhador - Inclusão.

## **02. EXEMPLO DE UTILIZAÇÃO**

Dados Fictícios

Para esse exemplo será incluído via [Importação Empréstimos FEBRABAN / Crédito do Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719677&draft=true) usando um arquivo CSV com os seguintes dados fictícios, sendo que onde tem informações com XXXX  deve ser trocado pelos dados da base de teste::

IfConcessoraCodigo;IfConcessoraDescricao;Contrato;Cpf;Matricula;InscricaoEmpregadorCodigo;InscricaoEmpregadorDescricao;NumeroInscricaoEmpregador;NomeTrabalhador;NomeEmpregador;DataInicioContrato;DataFimContrato;CompetenciaInicioDesconto;CompetenciaFimDesconto;TotalParcelas;ValorParcela;ValorEmprestimo;ValorLiberado;QtdPagamentos;QtdEscrituracoes;CategoriaTrabalhadorCodigo;CategoriaTrabalhadorDescricao;Competencia;InscricaoEstabelecimentoCodigo;InscricaoEstabelecimentoDescricao;NumeroInscricaoEstabelecimento  
001;Banco do Brasil;XXXXXXXXXX;XXXXXXXXXXX;XXXXXXXXXX;1;CNPJ;XX.XXX.XXX/XXXX-XX;FULANO DE TAL;XXXXXXXXXX;22/04/2025;;05/2025;04/2028;36;500;18000;15000;0;0;101;Empregado - Geral, inclusive o empregado público da administração direta ou indireta contratado pela CLT;04/2025;1;CNPJ;XX.XXX.XXX/XXXX-XX

Após execução do processo acima o cadastro de empréstimo ficou com os seguintes dados:

Observação:

O Código do empréstimo é a soma do Prefixo com o Sequencial cadastrado no parametrizador em folha normal [Crédito Trabalhador](https://tdn.totvs.com.br/pages/viewpage.action?pageId=937259572)

## **03.****TABELAS UTILIZADAS**

* PFFINANC
* PFEMPRT
* PFDESCEMPRT
