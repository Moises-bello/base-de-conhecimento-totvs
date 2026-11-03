---
content_hash: 60f7bf94b2a05e671a6d6e23925c8f0f583e4ae0c8157381a88e1713d4fa4b72
fetched_at: '2026-06-29T00:08:49.329371+00:00'
page_id: '329037148'
product: rm
source: tdn-rm
title: Saúde da Aplicação - Cockpit
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329037148
version: 28
---

# Índice:

---

* Objetivo:
* Especificação:

# Objetivo:

---

     Este documento tem por objetivo especificar o **bloco Saúde da Aplicação do Cockpit**.

# 1 - Especificação:

---

.confluence-information-macro {
width: calc(100% - 25px);
background: #fff !important;
border: 0;
-moz-border-radius: 0px !important;
-webkit-border-radius: 0px !important;
border-radius: 0px !important;
color: #333;
margin: 10px 0 1em 0;
min-height: 20px;
padding: 10px;
position: relative;
}
.confluence-information-macro p.title{
padding-left: 20px;
margin-top: 0px;
margin-bottom: 5px;
}
.confluence-information-macro .confluence-information-macro-icon.aui-iconfont-error{
color: #fff;
}
.confluence-information-macro-warning{
background-color: #d04437 !important;
color: #fff;
}
.confluence-information-macro-information{
border: 1px solid #aab8c6 !important;
}
]]>

# 1.1 - Bloco Saúde da Aplicação e Verificação de Serviços:

---

Para acessar a tela do **Cockpit** acesse, em qualquer módulo, o Menu **Ambiente** >> **Cockpit**,

Na tela do **Cockpit,** observe que para cada servidor conhecido, um bloco de informações é apresentado. Esse bloco de informações possui grupos distintos, que são:

* Processos
* Servidores de Aplicação
* Saúde da Aplicação

Nesse documento iremos explicar apenas o bloco **"Saúde da Aplicação"**.

Vamos descrever os componentes desse grupo.

| N° | Componente | Descrição do Componente |
| --- | --- | --- |
| **1** | Ícone de Status | Situação da Saúde do Servidor Conhecido/ Situação do Processo Executado (Visual) |
| **2** | Situação da Aplicação / Situação do Processo Executado | Aqui é apresentado de forma textual a situação da saúde do servidor conhecido/ situação do processo executado dentro do grupo **"Saúde da Aplicação"**. Refere-se aos processos executados pelos botões **(4, 5 e 6)**. |
| **3** | Descrição dos Serviços Indisponíveis. | Aqui é apresentado de forma textual os serviços indisponíveis que poderão ser recuperados através do Processo de Recuperar Serviços **(Botão 6)**. |
| **4** | Verificação Rápida | Realiza uma verificação superficial dos serviços do Host do RM para um determinado servidor conhecido. |
| **5** | Verificação Completa | Realiza uma verificação de todos os serviços do Host do RM para um determinado servidor conhecido. |
| **6** | Recuperar Serviços | O processo de Recuperar Serviços tentará recuperar todos os serviços que por algum motivo se tornaram indisponíveis. |

Vamos Iniciar a **Verificação Rápida** para tentar descobrir se algum serviço está indisponível e se poderá impactar na Saúde do Servidor Conhecido.

**1**- Clique no botão **Verificação Rápida (4):**

Você poderá obter dois resultados:

* **Sucesso**  
  Se a **Verificação Rápida** for executada com sucesso, quer dizer que não foi identificado serviço indisponível (lembrando que uma busca superficial é feita nesse caso), o que é um ótimo indicativo. Caso deseje, poderá executar a **Verificação Completa**para ter certeza que realmente não há nenhum serviço indisponível que poderá impactar na Saúde do Servidor.

* **Falha**  
  Se o **Ícone (1)**for vermelho (critico) e o **Texto (2)**for **"Indisponivel",**algum problema ocorreu no processo de Verificação, então execute novamente o processo de**Verificação Rápida.**

  Observação

  Caso essa mensagem persista, verifique se o servidor está offline.

Agora iremos realizar a **Verificação Completa**para confirmar  se algum serviço está indisponível.

**2** - Clique no botão **Verificação Completa (5):**

Você poderá obter 2 resultados:

* **Sucesso**Caso a ****Verificação Completa**** termine em sucesso, quer dizer que todos os serviços do host do ****RM**** estão ativos e disponíveis para uso, ou seja, tanto a aplicação quanto o servidor estarão em sua atividade plena.

* **Falha (Atenção)**  
  Caso a **Verificação Completa** termine em **falha**, verifique:
  + - **O Status da Aplicação:**
      * se o **Ícone (1)** for amarelo (atenção) e o **Texto (2)** for **"Indisponível"**, confira em seguida o campo **Serviços Indisponíveis (3)**e verifique se algum serviço foi apresentado. Caso algum serviço tenha sido apresentado selecione-o, e clique no botão **Recuperar Serviços (6)**.

* + - se o **Ícone (1)**for vermelho (critico) e o **Texto (2)**for **"Indisponivel",**algum problema ocorreu no processo de Verificação, então execute novamente o processo de**Verificação Completa.**

      Observação

      Caso essa mensagem persista, verifique se o servidor está offline.

Se a **Verificação Completa** apontar algum serviço indisponível, devemos recuperar esses serviços, para que a saúde do servidor conhecido seja recuperada.

**3** - Para isso selecione o(s) serviço(s) indisponível(is) e clique no botão **Recuperar Serviços (6):**

Observação

Os serviços selecionados serão recuperados e uma nova**Verificação Completa** é realizada, podendo gerar os dois resultados vistos acima, no segundo apêndice.

Atenção

Se a situação **(Status)** da Saúde da Aplicação estiver como **Indisponível** juntamente com o **Ícone Amarelo**, clique no botão **Recuperar Serviços (6)** até que a Situação **(Status)** mude para **"Verificação Completa Finalizada"**.

# 1.2 - Verificação Total:

---

Iremos abordar agora sobre a **Verificação Total**.

A **Verificação Total** tem o objetivo de verificar/analisar a saúde de todos os servidores conhecidos.

A **Verificação Total** pode ser feita de dois modos:

* **Verificação Rápida**
* **Verificação Completa**

Tudo o que foi dito na seção **1.1 - Bloco Saúde da Aplicação e Verificação de Serviços** serve para a **Verificação Total.** A diferença é que as verificações são realizadas em todos os servidores conhecidos.

No exemplo abaixo, perceba que a **Verificação Completa** realizada no servidor **BHN0501030950:8050,** não culminou em sucesso, um serviço **(GatewayService)**não estava disponível no momento, porém a **Verificação Completa** no servidor **BHN0509503010:8050** terminou com sucesso, indicando perfeita saúde nesse servidor.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Saúde da Aplicação - Cockpit

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
