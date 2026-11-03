---
content_hash: 91cd47f37f1b7bcc15230266dd67db98e311f8c25928b6adbc727e822492a2c6
fetched_at: '2026-06-29T00:11:36.506489+00:00'
page_id: '772826118'
product: rm
source: tdn-rm
title: 'DT - Lançamento Financeiro: Opção para desconsiderar autônomo nos tipos "25-DCTFWeb
  Folha" e "26-Total Guia INSS DCTFWeb 13º Salário"'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772826118
version: 15
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Lançamento Financeiro |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6116](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6116) |

## **01. VERSÕES**

**A partir das Versões:**

* 12.1.2209.243
* 12.1.2302.167
* 12.1.2306.111

## **02. SITUAÇÃO/REQUISITO**

Na geração do lançamento financeiro para os tipos "25-DCTFWeb Folha" e "26-Total Guia INSS DCTFWeb 13º Salário", o sistema está sempre considerando os autônomos TOTVS Gestão Financeira durante o processo, não tendo a opção para desconsiderá-los.

## **03. SOLUÇÃO**

Disponibilizado o parâmetro "Desconsiderar Autônomos TOTVS Gestão Financeira" nos parâmetros do lançamento financeiro para os tipos "25-DCTFWeb Folha" e "26-Total Guia INSS DCTFWeb 13º Salário".

**ATENÇÃO:** Com o intuito de evitar divergências durante a conferência, o **Relatório de Conferência de INSS Patronal** sempre levará em consideração os autônomos registrados no TOTVS Gestão Financeira. Portanto, o parâmetro "Desconsiderar Autônomos TOTVS Gestão Financeira" não será aplicado no referido relatório. Essa abordagem visa garantir a consistência e a coerência dos registros, facilitando o processo de verificação e prevenindo possíveis discrepâncias.

ATENÇÃO:

Para realizar a tratativa mencionada acima, é imprescindível executar o script por meio da versão correta do sistema RM.Atualizador.exe.
