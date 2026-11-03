---
article_id: 24073518519063
category: Originação de Grãos (OG)
content_hash: 04c5ad8c629caf4983c27ce17d0710e0c21459db2f60a300f85486847ad3542b
fetched_at: '2026-06-28T22:45:42.687799+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada na atualização do romaneio
type: support-article
updated_at: '2025-06-23T15:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24073518519063-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-na-atualiza%C3%A7%C3%A3o-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24073518503703) Tempo aproximado para leitura: **00:01:10 min****Dúvida**Como fazer para obter o **Ponto de Entrada na atualização do romaneio**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**Para solucionar essa dúvida, efetue o seguinte passo:

**1.** Acesse os dados do romaneio logo após sua atualização do Ponto de Entrada;

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGA250C | Funções de atualização do romaneio. | |
| **País(es):** | Todos |

# **Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar romaneio de produção. |
| **Programa Fonte:** | OGA250C |
| **Retorno:** | |  |  | | --- | --- | | **Nome** | **Descrição** | | OG250ATLZ | Permite acessar os dados do romaneio que já está atualizado.   * Tem como parâmetro a filial do romaneio e o número do romaneio. | |

# **Exemplo:**

**#include 'protheus.ch'**

**#include 'parmtype.ch'**

//A execução deste PE não influencia na rotina independente do que este PE retorne. user function OG250ATLZ()

    Local cFilRom := PARAMIXB[1]        
    Local cNumRom := PARAMIXB[2]

    DbSelectArea( "NJJ" )   
    DbSetOrder( 1 )

   If NJJ->( DbSeek( cFilRom + cNumRom ) )  
          alert("Achou o romaneio atualizado: " + cNumRom )  
     endIf

   Return .T.
