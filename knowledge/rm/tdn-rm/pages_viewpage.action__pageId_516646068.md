---
content_hash: 33b7faf489aafa032809fc5f257c4359f8a373a96bc2f573b596a77840aff8c6
fetched_at: '2026-06-29T00:10:27.794464+00:00'
page_id: '516646068'
product: rm
source: tdn-rm
title: 6362394 FISCAL01-10349 DT - NFS-e - 'ValorDeducoes' informado sem definir o
  'NumeroDeducao'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516646068
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | NFS-e |
| Ticket: | 6362394 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10349 |

## **02. SITUAÇÃO/REQUISITO**

Rejeição: Nfs-e Curitiba - 'ValorDeducoes' informado sem definir o 'NumeroDeducao' respectivo. - POSIÇÃO RPS - 1  
Tal rejeição é apresentada quando o cliente informou em seu xml o valor da dedução, a prefeitura informa através da rejeição que o numero da dedução deve ser informado.

## **03. SOLUÇÃO**

Foi realizado um ajuste para a geração da tag "numerodedu" da NFS-e, no grupo TCSERVIÇOS, que a partir de agora, para o município de Curitiba, passa a ser gerado com base no campo complementar "numeroencap"

O campo complementar deverá ser criado no movimento:
