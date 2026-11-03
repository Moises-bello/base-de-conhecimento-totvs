---
article_id: 32568414000023
category: Originação de Grãos (OG)
content_hash: c6f7ca3914125c7e35436d21e0fb7cc5488878f0832e2ab1c18377e5e1c96373
fetched_at: '2026-06-28T22:45:42.905367+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para controlar dados específicos
  do Pedido de Venda
type: support-article
updated_at: '2025-06-04T19:40:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32568414000023-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-controlar-dados-espec%C3%ADficos-do-Pedido-de-Venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32568413992983) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O Ponto de Entrada para controlar dados específicos do **Pedido de Venda**. Como funciona?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGX008 | Geração do Documento de Saída | |
| **Ponto de Entrada:** | OGX008PV |
| **País(es):** | Todos |
| **Versões/Release:** | 11.80.16 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite controlar dados específicos do Pedido de Venda. |
| **Localização:** | MenuDef |
| **Programa Fonte:** | OGX008 |
| **Função:** | OGX008PV |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **OGX008PV** | Array | Parâmetros enviados: {aCab,aItens} | NÃO | |

**Exemplo:**

#Include '[Protheus.ch](http://protheus.ch/)'  
#include "[fwmvcdef.ch](http://fwmvcdef.ch/)"

User Function **OGX008PV**()  
                Local aCab := aClone(PARAMIXB[1])  
                Local aItens := aClone(PARAMIXB[2])  
                Local aRet := {} //Customizações  
                  
                aAdd( aCab, {"C5\_MEUCAMPO"  , 'Valor'       , Nil } )  
                  
                aRet := {aCab,aItens}  
                  
                Return aRet
