---
content_hash: 674d58152687214a3b16e67155051224cfcef5994fadeada415541d422e842b9
fetched_at: '2026-06-29T00:11:16.193922+00:00'
page_id: '664181273'
product: rm
source: tdn-rm
title: DT - FISCAL01-17445 - Agrupamento CNO
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+FISCAL01-17445+-+Agrupamento+CNO
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-Reinf Eventos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17445 |

## **02. SITUAÇÃO/REQUISITO**

Cliente possui aquisição de serviços para filial matriz e filial 2 de um mesmo Cli/For com o mesmo CNPJ, e mesma obra (CNO). Ao gerar o Evento R-2010, o sistema não está agrupando por CNO, está gerando dois eventos separados, sendo um para a matriz e outro para a filial. Ao consultar o envio um evento é transmitido com sucesso e o outro retorna com a mensagem abaixo:

Falha ao processar o evento de identificador 284 e tipo R-2010: O evento foi rejeitado, pelo(s) seguinte(s) motivo(s):

Código MS1028: Não é permitido o envio de mais de um evento para o mesmo contribuinte, num mesmo período de apuração para um mesmo estabelecimento e prestador, exceto se for para retificação de um evento enviado anteriormente ou se o evento anterior tiver sido excluído

Registro: evtServTom - XPATH: /Reinf/evtServTom

## **03. SOLUÇÃO**

Ajuste na geração dos eventos R2010 e R2020. É possível ter um mesmo projeto para duas filiais distintas (com mesma raiz de cnpj). Nesse cenário há agrupamento em um único evento.
