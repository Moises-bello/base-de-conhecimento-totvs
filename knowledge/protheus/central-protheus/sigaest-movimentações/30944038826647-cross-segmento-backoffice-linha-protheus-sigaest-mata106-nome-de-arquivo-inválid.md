---
article_id: 30944038826647
category: SIGAEST - MOVIMENTAÇÕES
content_hash: f1701760d6ba3d9e044d36994ecddec64501d8fd6aa1a91cba9108321b887826
fetched_at: '2026-06-28T22:38:55.735583+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Nome de
  arquivo inválido ou inexistente [samples/wf/MATA106_Mail001.html]
type: support-article
updated_at: '2025-03-28T13:26:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30944038826647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-Nome-de-arquivo-inv%C3%A1lido-ou-inexistente-samples-wf-MATA106-Mail001-html
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30944038808343) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao gerar a rotina Pré-Requisição ocorre um error.log *"Nome de arquivo inválido ou inexistente [samples/wf/MATA106\_Mail001.html] on WFERROR"* como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**Normalmente este erro ocorre porque não tem o arquivo MATA106\_Mail001, informado na pasta WF do Protheus.

1- Na sua estrutura do Protheus é necessário criar essa pasta protheus\_data\**samples**\**wf**

2- Com a pasta WF criada, informar o arquivo MATA106\_Mail001 para o momento que gerar a Pré-Requisição(MATA106) não apresentar o error.log.

3- É necessário ter o parâmetro [MV\_ENVREQ](https://tdn.totvs.com/pages/releaseview.action?pageId=698626259) habilitado, para o envio do e-mail na geração da pré-requisição.

4- Segue o arquivo no final do artigo.

Atenção: Alguns ambientes Linux, necessitam que o nome do arquivo seja escrito com letras minúsculas, caso contrário, o mesmo não será localizado:

![Linux.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30993226797079)

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
