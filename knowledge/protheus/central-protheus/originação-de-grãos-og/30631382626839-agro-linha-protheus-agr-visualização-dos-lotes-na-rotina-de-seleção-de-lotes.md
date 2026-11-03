---
article_id: 30631382626839
category: Originação de Grãos (OG)
content_hash: 0ba67b64b354d0f27cd5ec3f50914f02c439232b62b3bcfd4475214239cf1756
fetched_at: '2026-06-28T22:45:45.971869+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Visualização dos lotes na rotina de Seleção de
  Lotes
type: support-article
updated_at: '2025-07-08T19:45:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30631382626839-Agro-Linha-Protheus-AGR-Visualiza%C3%A7%C3%A3o-dos-lotes-na-rotina-de-Sele%C3%A7%C3%A3o-de-Lotes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30631369559959) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**O que indica a tabela **Visualização dos lotes na rotina de Seleção de Lotes**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agronegócio |
| **Módulo:** | Gestão de Agronegócio |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA870A | Função chamada a partir da opção alterar/incluir a rotina AGRA870 | |
| **Ponto de entrada:** | AG870AA9 |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 e superior. |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | AGRF4LOTE() |
| **Programa Fonte:** | AGRA870A |
| **Função:** | Permitir tratamento de visualização dos lotes na tela de seleção de lotes conforme filtros. |
| Parâmetros: | | Nome | Tipo | Descrição | Obrigatório | | --- | --- | --- | --- | | PARAMIXB[1] | caractere | Consulta | Não | | PARAMIXB[2] | caractere | Alias ​​(NP9TEMP) | Não | | PARAMIXB[3] | caractere | Pedido | Não | | PARAMIXB[4] | caractere | Item | Não | | PARAMIXB[5] | caractere | Produto | Não | | PARAMIXB[6] | lógica | Se utilizado direcionamento do item do pedido | Não | |
| **Retorno:** | |  |  |  | | --- | --- | --- | | **Tipo** | **Descrição** | **Obrigatório** | | caractere | Retorne a regra para validar se o registro deve ser exibido na tela de lotes | Não | |

**Exemplo:**

USER FUNCTION AG870AA9()  
  
//customizações  
cValid := " "  
  
RETURN cValid
