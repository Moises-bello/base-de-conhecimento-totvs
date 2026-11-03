---
content_hash: 7f41eea06b31f1115ce9cf23ed97058a33b78021cabf88f553c919258b86b2f2
fetched_at: '2026-06-29T00:05:48.588906+00:00'
page_id: '1025242467'
product: rm
source: tdn-rm
title: DT - Smart View - Contrato de Trabalho
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Smart+View+-+Contrato+de+Trabalho
version: 10
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Smart View - Contrato de Trabalho |
| País: | Brasil |
| Épico | [DRHROTRM-14854](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14854) |

## **02. VERSÃO**

12.1.2602 e superiores

## **03. S****ITUAÇÃO/REQUISITO**

Elaborar um relatório que reúna os dados dos relatórios, abaixo, adaptando-os ao novo modelo de ferramenta com o uso do Smart View:

* **FOPREL00046 – Contrato de Trabalho (Modelo 1)**
* **FOPREL00047 – Contrato de Trabalho (Modelo 2)**
* **FOPREL00048 – Contrato de Trabalho a Título de Experiência**

**FOPREL00046:**

**FOPREL00047:**

**FOPREL00048:**

## **04. SOLUÇÃO**

Foi disponibilizado o objeto de negócios e o relatório no Smart View como um modelo unificado dos 3 relatórios de contrato de experiência. Este novo relatório possui informações semelhantes entre eles para melhorar a usabilidade e padronização.

| Campo relatório | Tabela e campo |
| --- | --- |
| Empresa | GCOLIGADA.NOMEFANTASIA |
| Endereço | GCOLIGADA.RUA |
| Cidade | GCOLIGADA.CIDADE |
| UF | GCOLIGADA.ESTADO |
| CNPJ | GCOLIGADA.CGC |
| Nome do Funcionário | PFUNC.NOME |
| Matrícula | PFUNC.CHAPA |
| Departamento | PSECAO.DESCRICAO |
| CTPS | PPESSOA.CARTEIRATRAB + PPESSOA.SERIECARTTRAB |
| PIS/PASEP | PFUNC.DTCADASTROPIS |
| CPF | PPESSOA.CPF |
| RG | PPESSOA.CARTIDENTIDADE |
| Dados Bancários | PFUNC.CODAGENCIAPAGTO + PFUNC.CONTAPAGAMENTO + PFUNC.OPBANCARIA + PFUNC.TPCONTABANCARIA |
| Salário | PFUNC.SALARIO |
| Horário do trabalho | AHORARIO |
| Data do Prazo do contrato | PFUNC.TEMPRAZOCONTR |
| Data de prorrogação do contrato | PFUNC.FIMPRAZOPRORROGCONTR |

## **05. DEMAIS INFORMAÇÕES**

* Smart View e RM
