---
content_hash: 95f26fd34623fcd1b53b112914f5ff6550caf4ec6d7b2a15a8dc72cefffce45d
fetched_at: '2026-06-29T00:12:14.181264+00:00'
page_id: '966224723'
product: rm
source: tdn-rm
title: FOPTRP0019 - Declaração de Encargos de Família para Fins de IR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=966224723
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

* 12.1.2510 e Superiores

## **02. V****ISÃO GERAL**

Relatório para emitir listagem de dependentes com incidência em IRRF. Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Código da Coligada | Filtra pelo código da coligada. | PFUNC.CODCOLIGADA |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Imprime Funcionário sem dependente | Exibe ou não o funcionário sem dependente. | (0-Não / 1-Sim) |
| Data Admissão | Filtra período para impressão validando a data de admissão do funcionário | PFUNC.DATAADMISSAO |

A visualização do relatório será de acordo com o filtro inserido via visão do Smart View, sendo esse filtro incluído pelo usuário. 

Nesse relatório temos os seguintes campos nos objetos de negócio disponível:

| **Campo** | **Campo na Tabela** |
| --- | --- |
| Empresa | GCOLIGADA.NOMEFANTASIA |
| Endereço | GCOLIGADA.RUA |
| Cidade | GCOLIGADA.CIDADE |
| UF | GCOLIGADA.ESTADO |
| CEP | GCOLIGADA.CEP |
| CNPJ | GCOLIGADA.CGC |
| Inscrição Estadual | GCOLIGADA.INSCRICAOESTADUAL |
| Nome do declarante | PFUNC.NOME |
| Matrícula | PFUNC.CHAPA |
| Departamento | PSECAO.DESCRICAO |
| CTPS | PPESSOA.CARTEIRATRAB |
| Série | PPESSOA.SERIECARTTRAB |
| Endereço | PPESSOA.RUA + PPESSOA.BAIRRO + PPESSOA.CIDADE + PPESSOA.ESTADO |
| CEP | PPESSOA.CEP |
| Estado Civil | PCODESTCIVIL.DESCRICAO |
| CPF Funcionário | PPESSOA.CPF |
| RG | PPESSOA.CARTIDENTIDADE |
| Número de Dependente | PFDEPEND.NRODEPEND |
| Nome Completo Dependente | PFDEPEND.NOME |
| CPF Dependente | PFDEPEND.CPF |
| Relação Dependente | PFDEPEND.GRAUPARENTESTO |
| Data de Nascimento | PFDEPEND.DTNASCIMENTO |

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

* GCOLIGADA
* PCODESTCIVIL
* PPESSOA
* PFUNC
* PFDEPEND
