---
article_id: 31175815271447
category: Originação de Grãos (OG)
content_hash: a559df45e7588e00aa704a44f469adf7dc87fcc415ed15b47847327cb11c259f
fetched_at: '2026-06-28T22:45:42.974226+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para Integração com o Documento
  de Entrada
type: support-article
updated_at: '2025-06-13T21:16:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31175815271447-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-Integra%C3%A7%C3%A3o-com-o-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31175815254679) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como testar o **Ponto de Entrada para Integração com o Documento de Entrada**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRUTIL01 | Funções de Uso Genérico | |
| **Ponto de Entrada:** | AGRP9NFE |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Permite dar prosseguimento da integração com o documento de entrada (SF1 x NP9). |
| **Localização:** | Rotina de integração com documento de entrada (SF1 x NP9). |
| **Programa Fonte:** | AGRUTIL01 |
| **Função:** | AGRP9NFE |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lAgrPE** | Logico | Se .T. prossegue com a integração.  Sem parâmetros | Não | |

****Exemplo:****

#Include '[Protheus.ch](http://protheus.ch/)'  
  
User Function AGRP9NFE()

     Local lAgrPE := .T.

    Alert("Exemplo de Alerta para integração com o documento de entrada SF1 x NP9")

   // Customizações abaixo //

    Return lAgrPE
