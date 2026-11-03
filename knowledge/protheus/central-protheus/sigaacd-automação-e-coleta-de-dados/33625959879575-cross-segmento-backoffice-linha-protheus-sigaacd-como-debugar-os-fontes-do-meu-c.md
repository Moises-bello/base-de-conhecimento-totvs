---
article_id: 33625959879575
category: SIGAACD - Automação e Coleta de Dados
content_hash: 60e63d9b0af20573811f65e08140c2ffdec539af0a2ac12cf51c97775ad8b51f
fetched_at: '2026-06-28T22:39:12.552095+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como debugar os fontes
  do meu coletor de dados?
type: support-article
updated_at: '2026-04-14T19:59:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33625959879575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-debugar-os-fontes-do-meu-coletor-de-dados
---

O artigo explica como depurar fontes de Automação e Coleta de Dados (ACD) usando emuladores como teraterm no ambiente TOTVS Backoffice (Linha Protheus). Para isso, é necessário configurar o VSCODE. Se a versão do release for 12.1.2310 ou inferior, o debug pode ser feito via Smartclient local; se for 12.1.2410 ou superior, apenas via WebApp. O artigo fornece links para guias detalhados de configuração no GitHub e descreve o processo de conexão e execução do debug, incluindo como iniciar o serviço, conectar ao ambiente, e usar o emulador para depurar o código fonte.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33625959878551) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar a depuração dos códigos-fonte em dispositivos móveis, quando se utiliza um coletor de dados por meio de emuladores, como o Tera Term ou outros?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.   
  
**Solução**  
Para realizar a depuração dos códigos-fonte de ACD, utilizando o Tera Term ou outro emulador de coletor de dados, é necessário primeiramente configurar o VSCode.

A depuração pode ser realizada por meio do Smartclient local, caso a versão seja 12.1.2310 ou inferior. Para versões iguais ou superiores a 12.1.2410, a depuração deve ser realizada exclusivamente via WebApp.

**Configuração 1** - Siga as instruções abaixo para a configuração do VSCode de forma **local (Smartclient):**  
[Clique aqui](https://github.com/totvs/tds-vscode/blob/master/docs/debugger.md#:~:text=TOTVS%20Language%20Debug%20(padr%C3%A3o)) para validar todo o processo detalhado dessa configuração em nosso GitHub.

**Configuração 2 -** Siga as instruções abaixo para a configuração do VSCode de forma **Web (WebApp-Smartclient)**  
[Clique aqui](https://github.com/totvs/tds-vscode/blob/master/docs/debugger.md#:~:text=TOTVS%20Language%20Web%20Debug%20(HTML)) para validar todo o processo detalhado dessa configuração em nosso GitHub.

**Importante****:** Para Debug de serviços externos como TeraTerm, API's, REST, etc, Localize a definição de executor que será utilizada e adicione a chave "enableMultiThread": true.

![unnamed.webp](https://centraldeatendimento.totvs.com/hc/article_attachments/39747755216279)

**Após a configuração de acordo com suas necessidades, bem como a configuração do depurador, iniciar o debug é um processo simples:**

Inicie o serviço do ambiente ao qual deseja se conectar e realize a conexão. No exemplo, utilizaremos o ambiente ONC2410, já conectado e pronto para uso.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33626215897367)

Após conectar ao ambiente, basta iniciar o executor já previamente configurado, conforme as instruções anteriores, para utilização da **configuração 1 ou 2.**

Clique no botão **PLAY** para iniciar o debug e, em seguida, preencha o nome da rotina com o conteúdo **XXXX e confirme.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33626373896599)

Uma guia será aberta no navegador que você configurou para depuração via web ou Smartclient local. A imagem abaixo ilustra a tela correta, pois ela congela uma instância inexistente; **mantenha a guia ativa.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33626227256855)

Após isso, posicione seu código-fonte e pontos de parada conforme sua necessidade, e inicie seu emulador. Dessa forma, você conseguirá realizar a depuração do código-fonte utilizando o emulador, conforme o exemplo abaixo, que apresenta o código da rotina "**Mestre de Inventário**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33626336046743)

Dessa forma, você pode realizar a depuração dos códigos-fonte via Tera Term ou emulador de sua preferência.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
