---
article_id: 4412256366871
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: aa6ac08b87be128cf05814bd094eebd305a80ddae51866f5665ba2884bcc1735
fetched_at: '2026-06-28T22:39:50.145075+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  nas opções do menu do Recebimento de Importação
type: support-article
updated_at: '2021-11-04T20:54:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412256366871-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-nas-op%C3%A7%C3%B5es-do-menu-do-Recebimento-de-Importa%C3%A7%C3%A3o
---

**Dúvida**Preciso de um ponto de entrada na rotina de Recebimento de Importação (EICDI154) que tenha validação .T. ou .F. quando clico nas opções do menu. Exemplo, preciso fazer uma validação antes de geração da nota complementar se essa validação retornar .F. não permite gerar a nota complementar.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões

**Solução**É possível utilizar o ponto de entrada **INICIA\_VARIAVEIS**, modificando a variável lLoop para .T. Reforçando que este ponto de entrada é para o cenário onde o parâmetro **MV\_TEM\_DI** **= F (desabilitado)**.

**Saiba mais**[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)
