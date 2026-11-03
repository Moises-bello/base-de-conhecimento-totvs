---
article_id: 33566640771607
category: TOTVS Agro - Comercialização (Linha Protheus)
content_hash: b9f09bbbd4377fb23ee12d2933bbae20ded701737f37adabc7f5bbbbe9f64136
fetched_at: '2026-06-28T22:45:34.068439+00:00'
product: protheus
section_id: 1500000623182
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para manipulação dos dados da
  Ordem de Produção
type: support-article
updated_at: '2026-02-27T17:46:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33566640771607-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-manipula%C3%A7%C3%A3o-dos-dados-da-Ordem-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33566640745367) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para manipulação dos dados da Ordem de Produção**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA600 | Cadastro de Fardão | |
| **Ponto de entrada:** | AGR600OP |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para a manipulação dos dados, antes da execução da rotina automática, para o desenvolvimento do OP. |
| **Localização:** | Rotina de Cadastro de Fardão. |
| **Eventos:** | O Ponto de Entrada é executado antes da execução da rotina automática. |
| **Programa Fonte:** | AGRA600 |
| **Função:** | AGRA600 |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aRet** | Variedade | Contemple a matriz dos campos da tela. | Sim | |

**Exemplo:**

**#Incluir '**[**Protheus.ch**](http://protheus.ch/)**'**

**Função de usuário AGR600OP()**

**aRet local:= {}**

**AADD(aRet, {'CAMPO'  , 'CONTEÚDO'  ,Nil})**

**Retornar aRet**
