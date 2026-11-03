---
content_hash: a6993256942fab7d157481ab306bdcedc3443daa19772ca72a37094a79ffa338
fetched_at: '2026-06-29T00:12:14.168952+00:00'
page_id: '966221192'
product: rm
source: tdn-rm
title: DT - Smart View - Declaração de Encargos de Família para Fins de Imposto de
  Renda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=966221192
version: 11
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart View - Declaração de Encargos de Família para Fins de Imposto de Renda |
| País: | Brasil |
| Épico | [DRHROTRM-14207](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14207) |

## **02. VERSÃO**

12.1.2510 e superiores.

## **03. S****ITUAÇÃO/REQUISITO**

Migrar o relatório **FOPREL00053 - Declaração Encargos Família para Fins IR** para o novo modelo de ferramenta utilizando o Smart View e melhorar a usabilidade.

## **04. SOLUÇÃO**

Foi disponibilizado o objeto de negócios e o relatório no Smart View, a nova ferramenta de análise de dados da TOTVS. Este novo relatório possui a interface mais amigável para o usuário.

| Campo relatório | Tabela e campo |
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
| CPF | PPESSOA.CPF |
| RG | PPESSOA.CARTIDENTIDADE |
| Nº | PFDEPEND.NRODEPEND |
| Nome completo do dependente | PFDEPEND.NOME |
| Relação dependente | PCODPARENT.DESCRICAO |
| Data de nascimento | PFDEPEND.DTNASCIMENTO |

## **05. DEMAIS INFORMAÇÕES**

Smart View e RM
