---
article_id: 28452729906583
category: SIGAACD - Automação e Coleta de Dados
content_hash: f7ee617e32f143c7e92166d0ffe2d0a8f3b6f4106aea3e6e80edf14582d13c12
fetched_at: '2026-06-28T22:39:13.829036+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Somente o operador
  pode dar continuidade a este inventário.
type: support-article
updated_at: '2024-12-11T18:24:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28452729906583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Somente-o-operador-pode-dar-continuidade-a-este-invent%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729806615) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como resolver a mensagem " Somente o operador pode dar continuidade a este inventário, contagens igual 1".   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Essa mensagem ocorre, quando somente o operador Administrador faz um inventário com somente uma contagem, segue os anexos com o passo a passo da mensagem por nativo do Protheus.

1. Criando um Mestre de Inventário com somente **uma** contagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452740384919)

2. Acessar o Tera Term com o operador Administrador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729814551)

3. Informo o mestre de inventário no caminho, Atualização, Estoque, Inventário. Coloco a contagem que desejo para aquele operador para dar andamento no inventário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452740397207)

4. Ao fazer a contagem acesso o monitor na rotina Mestre de Inventário(ACDA030), da contagem realizada segue a imagem. ![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729828759)

5. Vou acessar o Tera Term agora com outro operador, no mesmo mestre e apresenta a mensagem por nativo do Protheus, informando que somente aquele operador pode dar continuidade aquele mestre, que foi aberto com somente uma contagem.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729835287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452740412439)

6. Para não apresentar essa mensagem, é necessário criar um novo Mestre de inventário com **duas** contagens.![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452740421143)

7. Vou acessar  o Tera Term com o Administrador e dar andamento ao inventário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729856151)

8. Veja no Monitor a nova contagem realizada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729859991)

9. Vou acessar com um novo Operador para dar andamento ao mesmo Mestre de Inventário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729864855)![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452740447255)

10. Verifica que não apresentou a mensagem novamente, com um novo operador com um Mestre com duas contagens ou mais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729873815)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28452729877143)

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
