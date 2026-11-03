---
content_hash: 6301e9056582cc9580dd7a30530331ffd1b49ab0ed5a731f26c75646c2ef8ca7
fetched_at: '2026-06-29T00:11:54.580928+00:00'
page_id: '854368321'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Rateio por Centro de Custo da Seção do Funcionário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=854368321
version: 20
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Lançamento Financeiro - Rateio por centro de custo da seção do funcionário |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10413](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10413) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.233
* 12.1.2402.181
* 12.1.2406.114 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Possibilitar a geração do Lançamento Financeiro tipo  "**25-DCTFWeb Folha**" e "**26-Total Guia INSS DCTFWeb 13º Salário**" rateado pelo centro de custo cadastrado na seção do funcionário. 

## **04. SOLUÇÃO**

Disponibilizamos o parâmetro "**Ratear pelo centro de custo da seção do funcionário**" no cadastro do lançamento financeiro.

**1)** Após a liberação da versão será necessário executar o script de criação do novo campo no sistema através do sistema **RM.Atualizador.exe.**

**2)**Menu Encargos | Financeiro | Cadastros Financeiros | Parâmetros, marque o parâmetro "**Ratear pelo centro de custo da seção do funcionário**", conforme abaixo:

**2)** Menu Administração de Pessoal | Seções | Aba Dados Contábeis, preencha o campo "**Número do Centro de Custo**" na seção do funcionário conforme demonstrado abaixo:

3) Menu Encargos | Financeiro | Lançamentos, verifique que o lançamento foi rateado para o centro de custo informado na seção do funcionário.

ATENÇÃO:

1. O parâmetro "**Ratear pelo centro de custo da seção do funcionário**" ficará habilitado somente para os tipos de lançamento "**25-DCTFWeb Folha**" e "**26-Total Guia INSS DCTFWeb 13º Salário**" quando o parâmetro "**Utiliza Cálculo Por Centro de Custo**", existente em Parametrizador | Folha Normal | Cálculo, NÃO estiver marcado.
2. Caso a seção do funcionário não tenha um centro de custo cadastrado, o sistema emitirá uma mensagem informando sobre a ausência.

**Exemplo:** "Os lançamentos financeiros não foram gerados devido aos seguintes motivos: A seção COM\_DEP Comercial não possui centro de custo cadastrado."

## **05. DOCUMENTAÇÃO**
