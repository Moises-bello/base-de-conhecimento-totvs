---
article_id: 28481986473623
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 60f1ef5f43f0d26acf00461d5954ca6c26a86798bdc57f9fb4b0b10468ee52d5
fetched_at: '2026-06-28T22:39:08.234415+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - ERROR: Is not allowed
  more than one source with same name. Rename your source:'
type: support-article
updated_at: '2025-03-12T12:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28481986473623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-ERROR-Is-not-allowed-more-than-one-source-with-same-name-Rename-your-source
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28481969829271) Tempo aproximado para leitura: **00:07:00 min** **Dúvida**Ao compilar um Execauto, Ponto de entrada ou customização, o sistema retorna o ERROR: Is not allowed more than one source with same name. Rename your source:  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**

Este erro ocorre quando a função a qual esta compilando já foi compilada em outro fonte antes, e depois não foi excluido, para localizar isso, segue passo a passo

1 - No VSCode localize o ambiente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28790931504279)

2 - Clique com o botão direito do Mouse e selecione a opção "Functions Inspector";

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28790914962711)

3 - Pesquise a função a qual esta sendo reportada no erro;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28790914963223)

4 - Caso apareça mais de 1 U\_ será necessário localizar o fonte criado, ou até mesmo renomear o atual para Exclui-lo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28790931511703)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
