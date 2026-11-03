---
article_id: 39459492233879
category: SIGAACD - Automação e Coleta de Dados
content_hash: 66f266d9155b4cc9a7d2d1441b0bce88e940f741c5c05a5bea6df74a0d20bd13
fetched_at: '2026-06-28T22:39:12.818429+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados
  tem como usar a Pré-Separação?
type: support-article
updated_at: '2026-04-02T11:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39459492233879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-tem-como-usar-a-Pr%C3%A9-Separa%C3%A7%C3%A3o
---

No aplicativo Meu Coletor de Dados não é possível gerar uma Ordem de Separação pela Pré-Separação por Pedido de Venda, apenas a separação tradicional. A sugestão é registrar essa melhoria na Central Colaborativa TOTVS. É possível finalizar a Pré-Separação usando o emulador SIGAACD via VTDEBUG ou Tera Term com sessão TELNET configurada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459492199063) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Por nativo do aplicativo Meu Coletor de Dados, temos como gerar uma Ordem de Separação pela Pré-Separação?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
No aplicativo Meu Coletor de Dados, não temos a funcionalidade de utilização da Pré-Separação por Pedido de Venda.

**Exemplo do Processo:**

1. Cria um Pedido de venda com quantidade liberada;![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459619970967)
2. Gera uma Ordem de Separação por Pedido de Venda, com a pergunta Pré-Separação igual SIM; ![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459583348759)![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459619973143)![imagem4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459619974551)![imagem6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459619975831)
3. No aplicativo Meu Coletor de Dados seleciono o documento dessa Ordem;![imagem7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459656799639)![imagem8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459656801943)![imagem7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459656799639)![imagem9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459645277463)
4. Agora inicio a separação informando o código do Produto e Quantidade;![imagem9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459759654679)![imagem10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459779414935)![imagem11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459759663511)
5. Clico em Confirmar para finalizar a separação;
6. No Protheus apresenta a legenda em andamento e não finaliza por completo a separação, ficando em andamento;![image13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459908668311)![image14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459952649879)

   **OBSERVAÇÃO:**

A situação reportada nessa solicitação trata-se de uma sugestão de melhoria no produto e deve ser incluída na [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [**Portal do Cliente**](http://suporte.totvs.com/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!

Para conhecer mais sobre as suas **funcionalidades** clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27733078485399-Central-do-Cliente-TOTVS-Central-Colaborativa-Funcionalidades-Dispon%C3%ADveis)**​**.

Você pode acompanhar as suas **sugestões** e **comentários** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**

Acompanhe as **Novidades da Release** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).

```
Caso tenha acesso ao emulador SIGAACD padrão, através do Tera Term ou VTDEBUG, aonde tenha
a sessão TELNET configurada no seu AppServer.ini do ambiente do Rest.

Possa usar essa configuração para finalizar a Pré-Separação, pela rotina Ordem de Separação.
```

1. Acessar o emulador VTDEBUG ou Tera Term conforme a imagem abaixo;

   ![image15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39459944361751)![image16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39460006876311)![image17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39460034187543)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)
