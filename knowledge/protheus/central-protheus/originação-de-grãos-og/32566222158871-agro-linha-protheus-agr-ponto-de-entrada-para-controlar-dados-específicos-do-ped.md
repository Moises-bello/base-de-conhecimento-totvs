---
article_id: 32566222158871
category: Originação de Grãos (OG)
content_hash: e8cd62a43d62d11c900f628f758e6d2571e152d98989145e1544cdce272f3b08
fetched_at: '2026-06-28T22:45:42.894672+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para controlar dados específicos
  do Pedido de Exportação na Integração com o EEC
type: support-article
updated_at: '2025-06-03T21:23:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32566222158871-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-controlar-dados-espec%C3%ADficos-do-Pedido-de-Exporta%C3%A7%C3%A3o-na-Integra%C3%A7%C3%A3o-com-o-EEC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32566222146967) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O Ponto de Entrada para controlar dados específicos do **Pedido de Exportação na Integração** com o **EEC**. Como funciona?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA710 | Instrução de Embarque | |
| **Ponto de Entrada:** | OGA710P1 e OGA710P2 |
| **País(es):** | Todos |
| **Versões/Release:** | 12 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite controlar dados específicos do Pedido de Exportação na integração com o EEC. |
| **Localização:** | XEECAP100I |
| **Programa Fonte:** | OGA710 |
| **Função:** | OGA710P1 e OGA710P2 |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **OGA710P1** | Array | Parâmetros enviados: {aFilOri,aSafra} | NÃO | | **OGA710P2** | Array | Parâmetros enviados: {aCab,aItens,aAux} | NÃO | |

**Exemplo:**

* **FONTES ESPECÍFICOS CRIADOS PELO CLIENTE SLC.**

#Include '[Protheus.ch](http://protheus.ch/)'  
#include "[fwmvcdef.ch](http://fwmvcdef.ch/)"

User Function **OGA710P1**()  
                Local aFilOri := aClone(PARAMIXB[1])  
                Local aSafra := aClone(PARAMIXB[2])

                Local cPedido := ''      
                Local aRet := {} //Customizações

                //Fonte específico do cliente       

                aRet := cPedido  
                  
                Return aRet
