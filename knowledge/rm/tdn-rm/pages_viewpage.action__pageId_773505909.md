---
content_hash: 90e914fcf3f517a2e3f512e5b219b33c2839a64200af62d04c7637b0d162e671
fetched_at: '2026-06-29T00:11:36.730348+00:00'
page_id: '773505909'
product: rm
source: tdn-rm
title: 'DT - S-2299: Retificação da data de demissão rescisão judicial'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=773505909
version: 17
---

## **01. DADOS GERAIS**

| Produto: | TOTVS RH |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-2299 - Rescisão |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6125](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6125) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2209.244
* 12.1.2302.169
* 12.1.2306.113

## **03. SITUAÇÃO/REQUISITO**

Como proceder no sistema TOTVS Folha de Pagamento para informar ao eSocial uma alteração retroativa na data de demissão de um evento S-2299 já enviado ao governo, devido a uma decisão judicial que modificou a data de demissão?

## **04. SOLUÇÃO**

De acordo com as informações presentes no Manual de Orientação do eSocial (MOS), versão S-1.1 do leiaute, deverá utilizar a tag <indRemun> para indicar que o evento S-2299 corresponde a um desligamento reconhecido judicialmente, ocorrido antes das competências em que já foram informadas remunerações no eSocial. Com essa abordagem, torna-se dispensável excluir as remunerações referentes a competências posteriores.    

A fim de atender às orientações do eSocial, foram realizadas as seguintes alterações no tratamento do produto:

Cadastro de Rescisão:

* O campo "Data Fim Quarentena" será desabilitado quando o campo "Indicativo Remuneração Após o Desligamento" estiver preenchido com o valor 2.
* Foi adicionado o campo "Data Desligamento Judicial".

**Observação:** O usuário deve informar a data de desligamento determinada pelo juiz no processo judicial. Este campo só será habilitado quando o valor "2" for inserido no campo "Indicativo Remuneração Após o Desligamento".

**Exemplo:** Se um funcionário foi desligado em 15/01/2023, recebeu as verbas rescisórias em janeiro/2023 e o juiz determinou que a demissão deveria ter ocorrido em 25/12/2022, o usuário deve preencher o campo "Data Desligamento Judicial" com a data de 25/12/2022 (determinada pela justiça). Ao preenchê-la, o sistema gerará um gatilho de retificação do evento S-2299, contendo as seguintes informações:

* O campo <dtDeslig> preenchido com a data informada no novo campo "Data Desligamento Judicial" (25/12/2022).
* O campo <indRemun> preenchido com o indicativo de situação de remuneração após o desligamento igual a 2.
* O campo <dtFimRemun> preenchido com a data informada no campo "Data de Desligamento" da rescisão (15/01/2023).

   

ATENÇÃO - LEMBRETE

Para realizar a tratativa mencionada acima, é imprescindível executar o script por meio da versão correta do sistema RM.Atualizador.exe.
