---
content_hash: 1959f0438c9fad5dbd71d66915381b2e409009399e877799cdb280ddf937311c
fetched_at: '2026-06-29T00:11:51.482258+00:00'
page_id: '848809539'
product: rm
source: tdn-rm
title: Relatório com Fonte de Dados Não Suportada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=848809539
version: 2
---

## Índice:

---

2

# Código de Referência

---

false

**report-with-unsupported-data-source**

# Contexto

---

Algumas fontes de dados, como **Provedores de Dados** não são suportadas pela aceleração para o Smart View e a conversão de um detalhe relacionado à estas resultará na geração do detalhe sem dados no Smart View. Entretanto o relatório ainda poderá ser acelerado, a fim de aproveitar o layout deste, porém é necessário solicitar ao produto responsável pela **Fonte de Dados** do RM Reports o desenvolvimento de um **Objeto de Negócio** do Smart View compatível com os dados referentes àquela Fonte de Dados.

false

O relatório terá seu layout convertido para aproveitá-lo em um futuro Objeto de Negócio no Smart View

false

Relatórios com Fonte de Dados externa entretanto não serão acelerados de nenhuma forma e deverão ser reconstruídos do zero. Vide: 

# Procedimento

---

É necessário solicitar ao produto responsável pela **Fonte de Dados** a ser utilizada que seja desenvolvido um **Objeto de Negócio** nativo do Smart View referente à antiga Fonte de Dados, para uso do relatório no Smart View.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2310

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
