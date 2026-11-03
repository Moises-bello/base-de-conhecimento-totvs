---
article_id: 33567258447511
category: TOTVS Agro - Comercialização (Linha Protheus)
content_hash: 4ef3175447f99c54fe85ce66255c3e6955dcb11190d8d98f7679efb6c7c657d2
fetched_at: '2026-06-28T22:45:34.083839+00:00'
product: protheus
section_id: 1500000623182
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para manipulação dos dados de
  Apontamento da Produção
type: support-article
updated_at: '2026-02-27T17:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33567258447511-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-manipula%C3%A7%C3%A3o-dos-dados-de-Apontamento-da-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33567242090775) Tempo aproximado para leitura: **00:01:20 min**  
  
**Dúvida**  
Como funciona um **Ponto de Entrada para manipulação dos dados de Apontamento da Produção**?  
  
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
| **Ponto de Entrada:** | AGR600PR |
| **País(es):** | Todos |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Descrição:** | Ponto de Entrada para a manipulação dos dados, antes da execução da rotina automática, para o Apontamento de Produção. |
| **Localização:** | Rotina de Cadastro de Fardão. |
| **Eventos:** | O Ponto de Entrada é executado antes da execução da rotina automática. |
| **Programa Fonte:** | AGRA600 |
| **Função:** | AGRA600 |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **aRet** | Array | Contém os dados que serão enviados à rotina de Apontamento de Produção | Sim | |

**Exemplo:**

**#Include '**[**Protheus.ch**](http://protheus.ch/)**'**

**User Function AGR600PR()**

**Local aRet:= {}**

**AADD(aRet, {'CAMPO' , 'DADOS' ,Nil})**

**Return aRet**
