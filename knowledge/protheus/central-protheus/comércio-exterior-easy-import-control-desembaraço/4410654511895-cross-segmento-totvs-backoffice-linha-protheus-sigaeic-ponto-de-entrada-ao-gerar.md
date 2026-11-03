---
article_id: 4410654511895
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 0f50b2a87055a5874051dd6d5c0ec24e0f6d0367edc2e71bddee5e2608247873
fetched_at: '2026-06-28T22:39:50.140215+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  ao gerar complemento de valor na rotina recebimento de importação
type: support-article
updated_at: '2021-10-13T20:47:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410654511895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-ao-gerar-complemento-de-valor-na-rotina-recebimento-de-importa%C3%A7%C3%A3o
---

**Dúvida**Há  um ponto de entrada para modificar o armazém que está sendo levado para a SD3 no momento da geração do complemento de valor da nota fiscal de importação (EICDI161)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**

Pode ser utilizado o ponto de entrada **DI161EXECAUTO** e deve modificar é a variável **aAutoItens**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** | **Obrigatório** |
| **DI161EXECAUTO** | Caracter | Permite a alteração da capa e dos itens da rotina de Movimentação Interna Modelo 2 para a integração com o MATA241. |  |

Variável:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Nome** | **Tipo** | **Escopo** | **Pode Alterar** | **Descrição** |
|  | **aAutoItens** | Array | Private | Sim | Array contendo os itens de Movimentos Internos para a integração com o MATA241 |

**Saiba mais**

[EICDI161 - Complemento de Valor da Nota Fiscal](https://tdn.totvs.com/display/public/PROT/EICDI161+-+Complemento+de+Valor+da+Nota+Fiscal)
