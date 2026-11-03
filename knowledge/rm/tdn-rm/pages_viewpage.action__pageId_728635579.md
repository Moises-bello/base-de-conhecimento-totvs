---
content_hash: c025e023ec4c00c0f71fcebdf5360f2d19b58e9969329f2865a0f06ad8328cd1
fetched_at: '2026-06-29T00:11:27.636273+00:00'
page_id: '728635579'
product: rm
source: tdn-rm
title: Integração com o TOTVS Assinatura Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728635579
version: 2
---

# **01. VISÃO GERAL**

---

A seguir, demonstraremos como funciona a integração com o *TAE*, que é utilizada em várias visões dentro do RM.

# **02. CONFIGURAÇÃO**

---

A configuração da integração pode ser realizada no menu de **Parâmetros Globais**, na opção **Integração com Totvs Assinatura Eletrônica**.

# **03. ACESSANDO**

---

Ao acessar uma tela de cadastro que possui a integração, basta clicar no botão marcado abaixo:

Caso seja o primeiro acesso, a tela de login do TAE será aberta:

ObservaçãoO usuário utilizado aqui será o responsável pelo envio dos documentos.

# **04. TELA PADRÃO**

---

A seguinte tela apresentada é a tela padrão. Cada implementação pode ter suas customizações que mudam o design da tela.

falseConfigurando o Aplicativo Confiável no ADFSIdentificação

Nesta primeira tela temos informações dadas pelo sistema:

* Identificador
* Status do envelope:
  + Não localizado
  + Pendente
  + Assinado parcialmente
  + Finalizado
  + Rejeitado

E a propriedade que pode ser alterada:

* Nome do envelope
Documentos

Nesta tela é possível acrescentar documentos a serem enviados para a assinatura.

Ao apertar o botão , uma tela de seleção de documentos do sistema aparecerá.

É possível inserir vários documentos, e apagá-los sem problema até que o envio seja realizado.

Destinatários

Na tela de Destinatários é possível selecionar os destinatários dos documentos:

* Assinante: serão os destinatários que precisam assinar o documento para que haja a conclusão;
* Validador: destinatários que precisam validar o documento antes da conclusão.

É possível incluir e excluir destinatários até que o documento seja enviado.
