---
article_id: 4421898159639
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 04a0d3fe96679c9a90dff7233d2e5b23dca9ecd07c84f1a0b8b33e210beb8eca
fetched_at: '2026-06-28T22:39:07.990068+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  MATA010 - Error.log
  "Evento inválido on BOPROTHEUSEVENTVIEWER:UPDEVENT" ao criar ou efetuar cópia de
  produto '
type: support-article
updated_at: '2022-02-07T19:03:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421898159639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Error-log-Evento-inv%C3%A1lido-on-BOPROTHEUSEVENTVIEWER-UPDEVENT-ao-criar-ou-efetuar-c%C3%B3pia-de-produto
---

**Dúvida**

Ao criar um novo ou fazer uma copia de um produto apresenta o error.log "Evento inválido on BOPROTHEUSEVENTVIEWER:UPDEVENT", o que fazer para corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Ao criar um novo produto ou fazer uma cópia do mesmo, caso apresente o error.log abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421883954711/mceclip0.png)

Para corrigir deverá validar na tabela SX5, o campo X5\_CHAVE se o conteúdo "033", encontra-se deletado ou não possui esse registro na tabela conforme print abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421891187991/mceclip1.png)

Caso estiver deletado, favor verificar com o time de Tecnologia da Informação (TI) para que possa voltar a ativar ou ser criada essa chave na tabela SX5.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421891257111/mceclip2.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
