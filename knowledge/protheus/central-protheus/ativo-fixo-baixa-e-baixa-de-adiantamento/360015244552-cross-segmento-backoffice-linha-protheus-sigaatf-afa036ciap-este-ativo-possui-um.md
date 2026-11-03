---
article_id: 360015244552
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 1f47f2579769224db60fa277a5750d2c92de1a38eaea1f2d5189a2d968a5b61e
fetched_at: '2026-06-28T22:41:55.496266+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - AFA036CIAP - Este Ativo
  possui um código CIAP que já sofreu baixa com esse motivo nesta data
type: support-article
updated_at: '2023-11-20T16:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015244552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-AFA036CIAP-Este-Ativo-possui-um-c%C3%B3digo-CIAP-que-j%C3%A1-sofreu-baixa-com-esse-motivo-nesta-data
---

**Ocorrência**

 Ao tentar realizar a baixa de um bem(ATFA036), ocorre a seguinte mensagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010396692)

**Ambiente**

Protheus – Ativo Fixo – 12.1.17

**Causa**

Devido a um conceito do sistema , ao realizar a baixa de um bem com Ciap o sistema não permite que haja outra baixa de um bem com as mesma características :

* Mesma data
* Mesmo motivo de baixa
* Mesmo código de Ciap

**Solução**

Para solucionar a questão deve ser avaliado a melhor forma para realizar a baixa do bem, pois o sistema só permite efetuar uma baixa com o mesmo **CIAP e motivo** **uma vez ao dia.**
