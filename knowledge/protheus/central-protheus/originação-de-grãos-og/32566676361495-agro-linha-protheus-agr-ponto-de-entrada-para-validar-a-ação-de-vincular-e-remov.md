---
article_id: 32566676361495
category: Originação de Grãos (OG)
content_hash: 3e6f424c4da2789dcc8b1554ecf5c8640e01b5645e23529874b8776c68a8e25e
fetched_at: '2026-06-28T22:45:43.084541+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Ponto de Entrada para validar a ação de vincular
  e remover vínculo do Painel Financeiro
type: support-article
updated_at: '2025-07-14T19:50:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32566676361495-Agro-Linha-Protheus-AGR-Ponto-de-Entrada-para-validar-a-a%C3%A7%C3%A3o-de-vincular-e-remover-v%C3%ADnculo-do-Painel-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32566676281239) Tempo aproximado para leitura: **00:01:25 min**  
  
**Dúvida**  
Como funciona o **Ponto de Entrada para validar a ação de vincular e remover vínculo do** **Painel Financeiro**?  
  
**Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
**Características do Requisito:**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Agroindústria |
| **Módulo:** | SIGAAGR |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | OGC110 | Comissões Simuladas | |
| **Ponto de entrada:** | OGC110C7 |
| **País(es):** | Todos |
| **Pacote:** | 12.1.23 |

**Ponto de Entrada:**

|  |  |
| --- | --- |
| **Localização:** | Ao confirmar Pedido de Compra de Comissão |
| **Programa Fonte:** | OGC110C7 |
| **Função:** | Permitir manipular dados do Pedido. |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **OGC110C7** | Nenhum | Envia como parâmetro array dos dados do cabeçalho e itens do pedido | Não | |

**Exemplo:**

Função do usuário OGC110C7()  
Local aCab := aClone(PARAMIXB[1])  
Local aLinha := aClone(PARAMIXB[2])  
  
aAdd( aLinha, {"C7\_SEUCAMPO" , '' , Nil } )  
  
Return {aCab,aLinha}
