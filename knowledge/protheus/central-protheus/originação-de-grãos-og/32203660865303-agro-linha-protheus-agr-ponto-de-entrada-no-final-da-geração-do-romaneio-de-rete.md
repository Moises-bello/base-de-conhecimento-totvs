---
article_id: 32203660865303
category: Originação de Grãos (OG)
content_hash: 9d3eeb525a94ec5be68b2b4b68bbec38fd56c60ccc21b6c6cdfdeef2ec82c938
fetched_at: '2026-06-28T22:45:42.719412+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada no final da geração do romaneio
  de retenção do serviço de armazenagem
type: support-article
updated_at: '2025-08-20T20:01:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32203660865303-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-no-final-da-gera%C3%A7%C3%A3o-do-romaneio-de-reten%C3%A7%C3%A3o-do-servi%C3%A7o-de-armazenagem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32203672501271) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como confirmar um **Ponto de Entrada no final da geração do romaneio de retenção do serviço de armazenagem**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agronegócio |
| **Módulo:** | Gestão de Agronegócio |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA261 | Serviços de armazenagem | |
| **Ponto de Entrada:** | OGA261RRET |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 e superior. |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar um serviço de armazenagem do tipo Retenção (quebra-técnica) é gerado um romaneio de devolução de depósito. Esse ponto é acionado após o término de geração e atualização desse romaneio. |
| **Programa Fonte:** | OGA261RRET |
| **Função:** | Permitir realizar ações no romaneio gerado pela confirmação do serviço de retenção. |
| Parâmetros: | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB[1] | Char | Código do romaneio gerado na confirmação do serviço de retenção. | Não | |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lContinua** | Lógico | Indica se o retorno do ponto de entrada foi com sucesso.  .T. = Continua a confirmação do serviço de armazenagem;  .F. = Cancela a confirmação do serviço de armazenagem e realiza um *rollback* da transação. | Não | |

**Exemplo:**

|  |
| --- |
| `USER FUNCTION OGA261RRET()`    `Local cRoman as char`  `Local lRet as logical`    `cRoman := PARAMIXB[1]`  `lRet := .T.`    `If Empty(cRoman)`  `lRet := .F.`  `EndIf`    `RETURN lRet` |
