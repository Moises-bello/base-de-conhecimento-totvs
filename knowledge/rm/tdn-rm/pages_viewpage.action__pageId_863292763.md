---
content_hash: b9b8c4ea4b3e10338f4dc4429bf467c9edeb9c299e0fae590489a69fe13c4553
fetched_at: '2026-06-29T00:11:55.686613+00:00'
page_id: '863292763'
product: rm
source: tdn-rm
title: FISCAL01-23027 - Processo de Encerramento - Detalhamento da Apuração do Período
  dos Tributos PIS/COFINS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=863292763
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | Processo de Encerramento |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23027 |

## **02. SITUAÇÃO/REQUISITO**

O Anexo - **Detalhamento da Apuração** - será necessário ajustar o Processo de Encerramento de período para buscar as informações nova tabela "DLANCFISCAL" - **"Pré-Processamento Apuração Fiscal"** disponível em Obrigações Acessórias  
Estas informações estarão gravadas na base a partir do Processo de Pré-processamento realizado anteriormente.  
Deve-se ler os dados com Base nas Datas do Período de Apuração deserializar o Lançamento Fiscal e buscar as informações dos Itens para gerar os Registros do Detalhamento da Apuração do Período de Apuração.  
Deve ser considerado Itens dos Lançamentos de entrada e saída que tem na Sub Pasta outros Tributos - tributo PIS\COFINS com o Tipo Tributo (DTRIBUTO.TIPOTRIBFISC 10 PIS e 11 COFINS).

## **03. SOLUÇÃO**

Implementação do Processo de Encerramento do período com origem dos dados da tabela “DLANCFISCAL”.

Disponível à partir da biblioteca 12.1.2402
