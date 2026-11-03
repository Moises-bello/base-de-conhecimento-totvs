---
article_id: 32079984222359
category: Originação de Grãos (OG)
content_hash: 0f038e988aa372ec2b33448d51facf4ca03c94e9372754a3674b062c8c5566e9
fetched_at: '2026-06-28T22:45:43.113659+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada Romaneio com Pesagem
type: support-article
updated_at: '2025-08-18T14:00:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32079984222359-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-Romaneio-com-Pesagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32079964640151) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**O que indica a tabela **Ponto de Entrada Romaneio com Pesagem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA250 | Romaneio com Pesagem | |
| **Ponto de Entrada:** | **OG250PES** |
| **País(es):** | Todos |
| **Versões/Release:** | 12.1.17 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite executar operações customizadas antes da pesagem do romaneio. |
| **Localização:** | OGA250PESA |
| **Programa Fonte:** | OGA250 |
| **Função:** | OGA250PESA |

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'

**USER FUNCTION OG250PES()**

**Local cRoman := PARAMIXB[1]**  
**Local lRet := .T.**

**If 1 = 1**  
**lRet := .F.**  
**EndIf**  
**If !lRet**  
**Alert('**Romaneio**: ' + cRoman + '** Não pode ser pesado**!')**  
**EndIf**

**RETURN lRet**// SE RETORNAR FALSO NÃO PERMITIRÁ A PESAGEM DO ROMANEIO

A função deve retornar **Verdadeiro** para o romaneio seja pesado ou **Falso** para não ser permitida a pesagem.
