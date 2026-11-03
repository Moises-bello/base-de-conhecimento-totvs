---
article_id: 33453497314967
category: Originação de Grãos (OG)
content_hash: 6a4bf9991055a8d8e75d29ea54e28168e5627d2b2f685e9e91326852e087e280
fetched_at: '2026-06-28T22:45:43.026500+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Manipular dados na geração
  de produção - Romaneio por produção
type: support-article
updated_at: '2025-07-14T18:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33453497314967-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Manipular-dados-na-gera%C3%A7%C3%A3o-de-produ%C3%A7%C3%A3o-Romaneio-por-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33453497299863) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para** **Manipular dados na geração de produção - Romaneio por produção**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGX013 | Funções do romaneio por produção | |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar romaneio de produção. |
| **Programa Fonte:** | OGX013 |
| **Retorno:** | |  |  | | --- | --- | | **Nome** | **Descrição** | | OGX013GER | Permitir manipular dados da movimentação simples na geração de ordem de produção do romaneio.   * Tem como parâmetro array do cabeçalho e itens da ordem da movimentação. | |

**Exemplo:**

**#include '**[**protheus.ch**](http://protheus.ch/)**'**  
**#include '**[**parmtype.ch**](http://parmtype.ch/)**'**

**user function OGX013GER()**

**Local aCab := aClone(PARAMIXB[1])**  
**Local aItens := aClone(PARAMIXB[2])**  
**Local aRet := {} //Customizações do usuário**

**aAdd( aItens, {"D3\_MEUCAMPO" , 'VALOR' , Nil } )**

**aRet := {aCab,aItens}**

**Return aRet**
