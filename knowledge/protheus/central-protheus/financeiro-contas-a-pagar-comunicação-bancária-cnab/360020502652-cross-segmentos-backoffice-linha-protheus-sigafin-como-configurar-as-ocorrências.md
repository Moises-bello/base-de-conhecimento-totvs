---
article_id: 360020502652
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: a9a33182e300ed8ce703ae17fba80f1f638acee4d0e781f17228c3d3373c4ac4
fetched_at: '2026-06-28T22:37:55.095925+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus- SIGAFIN - Como configurar as Ocorrências
  CNAB
type: support-article
updated_at: '2026-06-12T17:29:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020502652-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-configurar-as-Ocorr%C3%AAncias-CNAB
---

***D*****úvida**  
Como configurar as Ocorrências CNAB?  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução**  
A configuração das ocorrências **CNAB** é realizada banco a banco, via rotina **FINA140**.

O **tipo da ocorrência** determina se a mesma será tratada como ocorrência de **envio**, **retorno** ou **pagamento**:

|  |  |
| --- | --- |
| **Tipos de Ocorrências** | **Formas de uso** |
| X5\_CHAVE | X5\_DESCRI |
| --E | Ocorrências de envio |
| --P | Ocorrências do Contas a Pagar - Envio/retorno |
| --R | Ocorrencia de Retorno Contas a Receber |

No layout específico de cada banco, são informadas quais são as "referências" das ocorrências bancárias, que deverão ser vinculadas às ocorrências do sistema.

Exemplo:  
**EB\_REFBAN**:  
Referência bancária "10" - classifica um pagamento/recebimento efetuado.

**EB\_OCORR**:  
Ocorrência do sistema "06" - liquidação normal (baixa)

|  |  |
| --- | --- |
| **Ocorrências Retorno Cobrança - FINA200** |  |
| 06 -07 -08 -36 -37 -38 | Baixa de título |
| 03 -15 -16 -17 -40 -41 -42 -52 -53 | Título rejeitado |
| 39 | Indica reciclagem |
| 02 | Entrada confirmada |

|  |  |
| --- | --- |
| **Ocorrências Retorno Pagamento - FINA430** |  |
| 01 - 06 - 07 - 08 | Baixa título |
| 03 | Título rejeitado |
| 02 | Entrada confirmada |
