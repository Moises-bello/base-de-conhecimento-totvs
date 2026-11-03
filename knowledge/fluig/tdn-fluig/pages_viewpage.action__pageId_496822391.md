---
content_hash: b3a35dc8c06fd6b5be87e1c7fa2e3bb697d3b03819349d24a9b6fac387722b2c
fetched_at: '2026-06-28T21:35:27.186751+00:00'
page_id: '496822391'
product: fluig
source: tdn-fluig
title: Integração de aplicativos externos com o Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496822391
version: 8
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é exemplificar a criação de um workflow para ser integrado com um aplicativo externo.

# Caso de uso

A empresa x necessita de um processo de solicitação de compra. A solicitação será iniciada por um usuário “comum” onde será incluído os dados da compra como categoria, justificativa de compra, fornecedor e a lista de produtos. Ao iniciar o processo um email deverá ser disparado para o fornecedor com a URL de acesso para uma página pública contendo os dados dos produtos para cotação. Após informar os valores dos produtos e submeter, o processo deverá ficar pendente com o gestor da área de compra para aprovação. Após aprovado um novo email é enviado para o fornecedor confirmando a solicitação de compra. O processo ficará pendente com o fornecedor até que ele submeta o envio dos produtos. Nesse momento o processo ficará pendente com a equipe de recebimento que fará a conferência dos produtos e finaliza o processo.

**Figura 1 - Workflow solicitação de compra.**

# Criação do Workflow (BPM)

Acesse a documentação completa em <http://tdn.totvs.com/x/dPwlE>

O workflow base e seu formulário foram criados pelo próprio desenhador de processos do BPM, após isso foi importado no Fluig dev studio e realizado as customizações necessárias. Para criar um novo processo acesse: Processos > Configurar Processos > Adicionar

Workflow

Todo o fluxo do processo foi feito apenas arrastando os componentes em tela. Para dúvidas referentes a processos segue toda documentação detalhada <http://tdn.totvs.com/x/widbB>.

Para criar um formulário para o processo acesse a opção Formulário dentro da criação/edição do processo:

                                                                                                         **Figura 2 - Criar formulário**

A partir deste ponto foi necessário apenas arrastar os componentes em tela.

## Customizando o processo

Para customizar o processo e o formulário é necessário ter instalado e configurado o Fluig studio. Acompanhe os passos a seguir:

0.5falsefluig\_studiofade1Passo 1

* Instalar Fluig studio <http://tdn.totvs.com/x/oxVbB>

2Passo 2

* Configurar Fluig studio <http://tdn.totvs.com/x/RYSbC>

3Passo 3

* Configurar servidor [http://tdn.totvs.com/x/UhgSCw#1-p1](http://tdn.totvs.com/x/UhgSCw)

4Passo 4

* Criar um novo projeto Fluig <http://tdn.totvs.com/x/UhgSCw>

5Passo 5

* Importar o processo criado na sessão "Criação do Workflow (BPM)"

### Envio de e-mail

#### Template de e-mail

Toda documentação referente a customização de templates de e-mail está disponível em  <http://tdn.totvs.com/x/BJLCC>

Para criar um novo template simples de e-mail acompanhe os passos a seguir:

Template emailTemplate emailPasso 1

* Criar um template de email em HTML ([Template HTML](https://github.com/fluig/workflow-solicitacao-de-compra/blob/master/workflow/layout_email/email_universo_totvs.html))

xml1Template de e-mailtrue
Fluig
  

|  |
| --- |
| ${MESSAGE} |
