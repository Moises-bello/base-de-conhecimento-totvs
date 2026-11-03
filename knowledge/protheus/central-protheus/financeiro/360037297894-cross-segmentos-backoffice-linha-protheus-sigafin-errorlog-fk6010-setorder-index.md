---
article_id: 360037297894
category: Financeiro
content_hash: 4448e4cd3aa1d46bf2242366df354606852466a633aacb9736300be0495c271a
fetched_at: '2026-06-28T22:38:02.959499+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Error.log FK6010:
  SetOrder - Index not found - Falta de Índice '
type: support-article
updated_at: '2022-06-21T00:06:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037297894-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Error-log-FK6010-SetOrder-Index-not-found-Falta-de-%C3%8Dndice
---

*****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*****Tempo aproximado para leitura: ****00:03:00 min****

**Ocorrência**FK6010: SetOrder - Index not found - Falta de Índice

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**O problema ocorre por falta de índice da tabela **FK6**.

**Solução**Verifique em seu ambiente os índices conforme modelo abaixo, caso contrário crie os índices ausente.

![](https://totvssuporte.zendesk.com/attachments/token/7hQyjAVAmoHm22DvycqHVlID3/?name=inline-1780472185.png)

**Saiba mais:**Caso não tenha cadastrado algum campo na tabela **FK6**, execute o atualizador de dicionário e base de dados - **UPDDISTR**[Atualizar o Dicionário de Dados do Protheus 12](http://tdn.totvs.com/pages/releaseview.action?pageId=271415266)

<http://tdn.totvs.com/pages/viewpage.action?pageId=181965468>
