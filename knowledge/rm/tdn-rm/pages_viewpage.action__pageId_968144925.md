---
content_hash: 6d8868816532c12a974daa104a18171c1609a837fcea985c45e40f8608730311
fetched_at: '2026-06-29T00:12:14.601083+00:00'
page_id: '968144925'
product: rm
source: tdn-rm
title: FOPTRP0020 - Lista de Dependentes do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=968144925
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

* 12.1.2510 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir listagem de dependentes e apresenta as incidências de salário família e IRRF. Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Código da Coligada | Filtra pelo código da coligada. | PFUNC.CODCOLIGADA |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Incidência Salário Família | Filtra o tipo de incidência desejado (Mostrar todos, Sim ou Não) | PFDEPEND.INSSALFAM OU [REGRA DE CACULO](https://tdn.totvs.com/display/public/LRM/Dependentes) |
| Incidência  de IRRF | Filtra o tipo de incidência desejado (Mostrar todos, Sim ou Não) | PFDEPEND.INCIRRF |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Grau de Parentesco | Filtra o graus de parentesco do dependente | PFDEPEND.GRAUPARENTESCO |
| Imprime Funcionário sem dependente | Exibe ou não o funcionário sem dependente. | (0-Não / 1-Sim) |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| **Campo** | **Campo na Tabela** |
| --- | --- |
| Empresa | GCOLIGADA.NOMEFANTASIA |
| Endereço | GCOLIGADA.RUA |
| Cidade | GCOLIGADA.CIDADE |
| UF | GCOLIGADA.ESTADO |
| CNPJ | GCOLIGADA.CGC |
| Departamento | PSECAO.DESCRICAO - PSECAO.DESCRICAO |
| Matrícula | PFUNC.CHAPA |
| Títular | PFUNC.NOME |
| Situação Atual | PFUNC.CODSITUACAO |
| Nome Completo Dependente | PFDEPEND.NOME |
| Relação Dependente | PFDEPEND.GRAUPARENTESTO |
| Data de Nascimento | PFDEPEND.DTNASCIMENTO |
| Idade | Calculo da idade é considerado conforme o ano da geração. Exemplo: data da geração 22/08/2025 e data de nascimento 15/12/1989. Idade que será apresentada é 36 anos. |
| Incidência Salário Família | PFDEPEND.INSSALFAM OU [REGRA DE CACULO](https://tdn.totvs.com/display/public/LRM/Dependentes) |
| Incidência  de IRRF | PFDEPEND.INCIRRF |

## **03. EXEMPLO DE UTILIZAÇÃO**

**1)** Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

2) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

Escolha o relatório desejado e vá em 'Mais Ações' depois em 'Anexos da Execução de Recurso do Smart View'. Configure os filtros necessários e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

DICA

* É necessário que todos os campos do filtro sejam preenchidos. Para adicionar um filtro, clique no ícone correspondente.
* Para gerar todos os resultados, configure o filtro com a opção "-1".
* Os ícones  do relatório oferecem diversas opções, como pesquisa, impressão, salvar, entre outros serviços disponíveis.

## **04. TABELAS UTILIZADAS**

* GCOLIGADA
* PSECAO
* PCODSITUACAO
* PCODPARENT
* PFUNC
* PFDEPEND
