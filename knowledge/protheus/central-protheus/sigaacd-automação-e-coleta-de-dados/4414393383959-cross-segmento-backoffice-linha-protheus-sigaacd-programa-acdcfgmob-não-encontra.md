---
article_id: 4414393383959
category: SIGAACD - Automação e Coleta de Dados
content_hash: 7848fe15205090b33a943073036578c1f2753c888353bf40e300a7f590e465c7
fetched_at: '2026-06-28T22:39:13.768297+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Programa ACDCFGMOB
  não encontrado no seu ambiente. '
type: support-article
updated_at: '2021-11-29T22:00:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414393383959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Programa-ACDCFGMOB-n%C3%A3o-encontrado-no-seu-ambiente
---

**Dúvida**

Ao acessar e sincronizar o app Meu Coletor de Dados, o sistema retorna a seguinte mensagem:

**"Programa ACDCFGMOB não encontrado no seu ambiente. Favor atualizar o Protheus com o ultimo pacote referente ao Mobile."**

![acd.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4414393000983/acd.PNG)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

A mensagem "Programa ACDCFGMOB não encontrado" é apresentada porque em seu AppServer.ini existe a TAG abaixo:

**[HTTPURI]**  
**Module=46**  
  
Para que a mensagem não seja apresentada, é necessário estar com o ambiente e rotinas do meu coletor  atualizados e comentar essa TAG conforme exemplo abaixo, desta forma o sistema irá apresentar os serviços do Meu Coletor de Dados com sucesso.

**;[HTTPURI]**  
**;Module=46**

Abaixo o link de acumulados do meu coletor de dados:

[Pacote acumulado Meu coletor de Dados](https://tdn.totvs.com/pages/releaseview.action?pageId=527830949)

**Observação:** Essa TAG deve ser informada somente se não tiver as licenças FULL e T em seu ambiente. 

**Saiba mais:**

*[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)*

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
