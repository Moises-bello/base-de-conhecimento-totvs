---
article_id: 33558099171735
category: TOTVS Agro - Comercialização (Linha Protheus)
content_hash: dd8102067e57cad3f59be5fa05fd3616fae349d0983b0585f5afb56e86eea3ed
fetched_at: '2026-06-28T22:45:34.097388+00:00'
product: protheus
section_id: 1500000623182
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para manipulação dos Itens de
  Movimento Interno
type: support-article
updated_at: '2026-02-27T17:47:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33558099171735-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-manipula%C3%A7%C3%A3o-dos-Itens-de-Movimento-Interno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558106786199) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para manipulação dos Itens de Movimento Interno**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA750 | Romaneio de Saída | |
| **Ponto de entrada:** | AGR75ID3 |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de entrada para a adição de campos personalizados. |
| **Localização:** | Rotina de Romaneio de Saída |
| **Eventos:** | O Ponto de Entrada é executado antes da execução da rotina automática. |
| **Programa Fonte:** | AGRA750 |
| **Função:** | AGRA750 |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aRet** | Variedade | Contém a matriz dos campos da tela. | Sim | |

**Exemplo:**

**#Incluir '**[**Protheus.ch**](http://protheus.ch/)**'**

**Função de usuário AGR75ID3()**

**aRet local:= {}**

**AADD(aRet, {'CAMPO', 'CONTEÚDO', Nil})**

**Retornar aRet**
