---
article_id: 32790982248599
category: Originação de Grãos (OG)
content_hash: b7a11eb397c94d9d5d0cec108d56c075200afc1e290ae136caf80ec9e2da9d1e
fetched_at: '2026-06-28T22:45:42.981940+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Manipular Dados da geração
  de produção no romaneio por produção
type: support-article
updated_at: '2025-06-13T20:59:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32790982248599-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Manipular-Dados-da-gera%C3%A7%C3%A3o-de-produ%C3%A7%C3%A3o-no-romaneio-por-produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32790982237207) Tempo aproximado para leitura: **00:01:50 min****Dúvida**Como funciona o **Ponto de Entrada para Manipular Dados da geração de produção no romaneio por produção**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

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

#include '[protheus.ch](http://protheus.ch/)'  
#include '[parmtype.ch](http://parmtype.ch/)'

user function OGX013GER()

     Local aCab := aClone(PARAMIXB[1])  
     Local aItens := aClone(PARAMIXB[2])  
     Local aRet := {} //Customizações do usuário

     aAdd( aItens, {"D3\_MEUCAMPO" , 'VALOR' , Nil } )

     aRet := {aCab,aItens}

Return aRet
