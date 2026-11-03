---
content_hash: 903f559b1dc224e3b50c9cc03d63163ff98ecd5c02fd38d06bfb74f19979b4a7
fetched_at: '2026-06-29T00:10:22.537846+00:00'
page_id: '497194737'
product: rm
source: tdn-rm
title: DEDUANALYTICS-1308 DT Processo no RM para extração dos dados para o GoodData
  via TOTVS Fast Analytics
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497194737
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Fast Analytics |
| Função: | Processo de Extração para o GoodData |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUANALYTICS-1308 |

## **02. SITUAÇÃO/REQUISITO**

Clientes que utilizam Cloud da TOTVS precisam executar o processo de extração via RM para realizar extrações esporádicas, sem depender do agendamento ou de um analista do Cloud para isso.

## **03. SOLUÇÃO**

Foi criado um processo no RM Integrações que permite a execução de uma extração de qualquer conjunto de fatos para o GoodData.

Para o correto funcionamento desse processo, será necessário informar o caminho do arquivo Java.exe e AgentFastAnalytics.jar (presente dentro do diretório de configuração do TOTVS Fast Analytics) através do parametrizador do TOTVS Business Analytics:

Além disso, a estrutura de pastas e arquivos do diretório de instalação do TOTVS Fast Analytics não pode ser alterada (um diretório de query, arquivo my.properties e run.bat por grupo de Fatos - Alunos, Contabilidade e Financeiro)
