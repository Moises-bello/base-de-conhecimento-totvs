---
article_id: 19786344061207
category: Materiais - Compras (SIGACOM)
content_hash: bf9cc3362331dbb736b254d78b0d5b3aed244cbd9886abe7a91364a28f9f76c8
fetched_at: '2026-06-28T22:41:20.117156+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA116 - Como funciona
  o rateio no CTE?
type: support-article
updated_at: '2023-12-13T17:09:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19786344061207-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA116-Como-funciona-o-rateio-no-CTE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19786340036375) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Qual é o conceito do sistema referente à declaração de rateio na MATA116 Conhecimento de Frete?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**

Por padrão, o sistema considera que o rateio que está sendo declarado na MATA116 é referente ao serviço de frete que está sendo contratado. Dessa forma, ele deve ser declarado em "Outras Ações" -> Rat. CC.

Porém, o rateio que foi declarado na Nota fiscal de origem não será puxado no CTE. Trata-se de um conceito padrão do sistema, devido os pontos abaixo:

1. Em um mesmo CTE podem ser selecionados diversas notas de origem, mediante isso, o sistema não saberia a qual rateio de qual nota acatar
2. O rateio declarado na nota de origem diz respeito ao rateio dos produtos, dos itens da nota. Já o rateio do CTE é referente ao serviço de frete que está sendo contatado e pago. Não são rateios equivalentes.
3. O CTE é espelho dos itens da nota de origem no tocante a trazer corretamente as informações que constam explicitamente na nota (valor unitário, código do produto, nf de origem em casos de devolução de vendas, entidades contábeis digitadas na linha do item SD1). Porém, o rateio é algo particular de cada regra de negócio. Dessa forma, deverá ser declarado em referência ao serviço que está sendo contratado no CTE.

As entidades contábeis que forem digitadas na linha do item do documento de entrada serão trazidas para o CTE.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Nota de Conhecimento de Frete (MATA116)?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiY3%2F7SUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBq2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMjIwNDMxMi1Dcm9zcy1TZWdtZW50b3MtVG90dnMtQmFja29mZmljZS1Qcm90aGV1cy1TSUdBQ09NLUNvbW8taW5jbHVpci1Ob3RhLWRlLUNvbmhlY2ltZW50by1kZS1GcmV0ZS1NQVRBMTE2LQY7CFQ6DnNlYXJjaF9pZEkiKTM3NTA0NTYzLTFhMTItNDM1ZC1iMmQxLWMwMmFjNTk0NmZhMgY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiGmNvbmhlY2ltZW50byBkZSBmcmV0ZQY7CFQ6EnJlc3VsdHNfY291bnRpAukD--84a9ef2468bd66183f2f702099cd188e9415b028)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada Conhecimento de Frete - MATA116](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj3gwTTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBqGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMjU3NDA3MS1Dcm9zcy1TZWdtZW50b3MtVG90dnMtQmFja29mZmljZS1Qcm90aGV1cy1TSUdBQ09NLVBvbnRvcy1kZS1FbnRyYWRhLUNvbmhlY2ltZW50by1kZS1GcmV0ZS1NQVRBMTE2LQY7CFQ6DnNlYXJjaF9pZEkiKThkMDhhZmU4LWNiMTEtNGQ1Yy1hYTE4LTk5ZjBlZDVlNmFjOAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiK2NvbmhlY2ltZW50byBkZSBmcmV0ZSBwb250byBkZSBlbnRyYWRhBjsIVDoScmVzdWx0c19jb3VudGkC6gM%3D--f2ddd154064bc23dfa5276082350f3c9593387bb)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
