---
article_id: 32568039081623
category: Originação de Grãos (OG)
content_hash: 6b0d6033a3e567ea74c84207c7180babeac499eb75edcfad143261b7caded065
fetched_at: '2026-06-28T22:45:42.678902+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada após confirmação do romaneio
type: support-article
updated_at: '2025-06-04T19:39:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32568039081623-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-ap%C3%B3s-confirma%C3%A7%C3%A3o-do-romaneio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32568039062167) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O Ponto de Entrada após confirmação do romaneio. Como funciona?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGX008 | Função para geração do documento de saída | |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar um romaneio. |
| **Programa Fonte:** | OGX008 |
| **Nome do PE:** | |  |  | | --- | --- | | **Nome** | **Descrição** | | OGX008PG | Permitir que o usuário possa intervir logo após a inclusão do romaneio e antes do lançamento da Nota Fiscal. OBS: O retorno do PE não interfere em nada na continuação da rotina.   * Recebe a filial e número do pedido gerado. | |

**Exemplo:**

#include '[protheus.ch](http://protheus.ch/)'  
#include '[parmtype.ch](http://parmtype.ch/)'

//A execução deste PE não influencia na rotina, ou seja, independente do que este  
// PE retorne, a emissão de nota do pedido de venda, que já foi gravado antes deste  
// PE ser executado, será feita.  
user function OGX008PG()

Local cFilPed := PARAMIXB[1]  
Local cNumPed := PARAMIXB[2]

        DbSelectArea( "SC5" )  
        DbSetOrder( 1 )  
        If SC5->( DbSeek( cFilPed + cNumPed ) )  
                alert("Achou o pedido")  
        endIf  
  
        DbSelectArea( "SC6" )  
        DbSetOrder( 1 ) //C6\_FILIAL+C6\_NUM+C6\_ITEM+C6\_PRODUTO  
        If SC6->( DbSeek( cFilPed + cNumPed ) )  
                alert("Achou o item do pedido")  
        endIf  
  
Return .T.
