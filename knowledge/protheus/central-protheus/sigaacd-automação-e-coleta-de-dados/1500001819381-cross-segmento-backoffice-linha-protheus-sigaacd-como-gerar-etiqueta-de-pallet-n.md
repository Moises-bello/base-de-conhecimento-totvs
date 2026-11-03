---
article_id: 1500001819381
category: SIGAACD - Automação e Coleta de Dados
content_hash: 6193fb6e0ae9240ca0a8be4d815bbf299fa898b64c66180f25252e3d59b073f3
fetched_at: '2026-06-28T22:39:12.583896+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como gerar etiqueta
  de pallet na rotina ACDV230   '
type: support-article
updated_at: '2023-08-16T12:38:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001819381-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-gerar-etiqueta-de-pallet-na-rotina-ACDV230
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16804925109399) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como gerar etiqueta de pallet na **rotina ACDV230**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

1. Segue abaixo de como deve ser gerado etiqueta de Pallet no ACD.

![GIF1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100632694)

2. Processo via Tera Term para geração da etiqueta de Pallet.

![20210121_103341.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360100632734)

3. Parâmetro para gerar a etiqueta **MV\_ACDCB0** = 01, é gerado primeiramente uma etiqueta de produto e depois a etiqueta de Pallet.

4. Pode ser gerada também a etiqueta de Pallet via rotina ACDI011 conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001741962)

Ao selecionar Pallet e clicar na lupa vai aparecer essa mensagem:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102801193)

Para corrigir essa mensagem é necessário cria os índices da etiqueta de pallet através dessa documentação:

[Criação de Índice na tabela CB0](https://tdn.totvs.com/pages/releaseview.action?pageId=547242795)

Caso desejar, esta anexo a SXB em .dtc com a consulta padrão para agilizar a montagem.

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
