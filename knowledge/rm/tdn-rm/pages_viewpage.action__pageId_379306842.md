---
content_hash: e275c4beb17357afb7ccef82c9a21d4f9a66f26efffae7d0218a328595b23b56
fetched_at: '2026-06-29T00:09:02.404345+00:00'
page_id: '379306842'
product: rm
source: tdn-rm
title: Configuração da Tag CustomErros Mode e StackTraceVisible no FrameHTML (WebAPI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379306842
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo

---

     Este documento tem por objetivo especificar as possíveis configurações para a Tag CustomErros Mode e StackTraceVisible, presentes no Web.config do FrameHtml (WebAPI), que tem a função de permitir customizar, exibir ou ocultar informações sobre mensagens de erro da aplicação e ocultar o rastreamento da pilha (StackTrace), respectivamente.

    A tag CustomErros pode ser configurada das seguintes formas:

* <customErrors mode="RemoteOnly" />
* <customErrors mode="Off" />
* <customErrors mode="On" />

 A tag StackTraceVisible pode ter os valores true or false:

* <add key="StackTraceVisible" value="true" />
* <add key="StackTraceVisible" value="false" />

Essas tags estão presentes no arquivo do Web.config do FrameHtml (WebAPI).

# CustomErros Mode

---

     Veja abaixo a diferença entre cada modo de utilização da tag:

**RemoteOnly:**  Ao utilizar essa configuração, as mensagens de erro do sistema serão exibidas de forma diferente no servidor e no client. Tag: <customErrors mode="RemoteOnly" />

 - Para usuários que estão executando a aplicação em máquinas que não são o servidor Web a mensagem de erro exibida será a customizada;

Exemplo:

Na tela de Login do portal Frame HTML, foi incluída a senha errada do usuário. No acesso feito de uma máquina virtual que não é o servidor da aplicação, o erro retornado foi:

 - Para usuários que estão executando a aplicação em máquinas do servidor Web, o erro exibido será o real erro que o server retorna, contendo o StackTrace  e Origem do erro.

Exemplo:

Foi repetido o teste do passo anterior e na tela de Login do portal Frame HTML, foi incluída a senha errada do usuário. Porém, agora, o acesso foi feito diretamente da máquina que é o servidor da aplicação. O erro retornado foi:

 **ON:** Ao utilizar essa configuração, as mensagens de erro do sistema serão exibidas customizadas, independente do usuário estar no servidor ou no client. Tag:**<customErrors mode="On" />**

**OFF:**  Ao utilizar essa configuração, as mensagens de erro do sistema serão exibidas tal qual são retornadas pelo server, com as informações do erro, como StackTrace e Origem do erro. Tag:**<customErrors mode="Off" />**

# StackTraceVisible

---

     A configuração dessa tag determina se o StackTrace será exibido ou não, quando algum erro for exibido. Entretanto, existe uma regra para que o resultado não conflite com o valor configurado na tag CustomErros Mode:

* A tag StackTraceVisible prevalece sobre a tag CustomErros Mode desde que o CustomErros Mode configurado exiba, por padrão, a pilha de erros.  
  Dessa forma, a tag StackTraceVisible afetará ambientes com <customErrors mode="Off" /> ou no server configurado com <customErrors mode="RemoteOnly" />.
* A partir da versão 12.1.2310 por padrão o valor será "false", a menos que seja definido no web.config.
falsefalse

**Produto:** Framework

false

**Versão:** 12.1.18 ou Superior

false

**Processo:** Configuração da Tag CustomErros Mode

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
