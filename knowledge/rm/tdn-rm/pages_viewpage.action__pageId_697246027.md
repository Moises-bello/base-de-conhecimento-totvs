---
content_hash: 84f8deae7904acc7e32be0549bee3c6f500eaef65d91614a66cca4b2051be7c1
fetched_at: '2026-06-29T00:11:21.547967+00:00'
page_id: '697246027'
product: rm
source: tdn-rm
title: Liberação de acesso as URL's externas necessário no servidor web e aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697246027
version: 13
---

Segue a lista de URL's externas de terceiros que são utilizadas no Portal do Aluno.  Para o correto funcionamento do portal, será necessário que o servidores web onde estão instalado o portal precise ter acesso liberado ao links relacionados.

Alguns do links externos de terceiros utilizados no Portal do Aluno, são configurados pelo próprio cliente, através de parâmetros no RM.exe

## **01. Recaptcha do Google**

Valida a SECRET\_KEY do Recaptcha definido no Web.Config do Portal do Aluno. 

A URL utilizada para esta funcionalidade é  <https://www.google.com/recaptcha/api/siteverify>

## **02. Login via Facebook**

Realizar acesso único utilizando a conta do Facebook no login do portal. Para mais informações acesse

A URL utilizada para esta funcionalidade é informada nas parametrizações conforme o documento acima.

## **03. Login via Google**

Realizar acesso único utilizando a conta do Google no login do portal. Para mais informações acesse

A URL utilizada para esta funcionalidade é informada nas parametrizações conforme o documento acima.

## **04. Integração com Prova Fácil**

URL para a geração do token. Para mais informações acesse

A URL utilizada para esta funcionalidade é  <https://sso.provafacilnaweb.com.br/universallogin/generate-token>

## **05.****Plataforma de pagamento digital CyberSource**

A cybersource é uma plataforma de pagamentos digitais.. Para mais informações acesse

As URL's utilizadas para esta funcionalidade são

<https://ics2wstesta.ic3.com:443/commerce/1.x/transactionProcessor>

<https://ics2wsa.ic3.com/commerce/1.x/transactionProcessor>

<https://api.cybersource.com>

## **06.****Plataforma de pagamento digital Checkout Cielo**

A checkout cielo uma plataforma de pagamentos digitais.. Para mais informações acesse

A URL utilizada para esta funcionalidade é <https://cieloecommerce.cielo.com.br/api/public/v1/orders>.

## **07.****Plataforma de pagamento digital BuyPage Cielo**

A buypage clielo uma plataforma de pagamentos digitais.. Para mais informações acesse

A URL utilizada para esta funcionalidade é <https://ecommerce.cbmp.com.br/servicos/ecommwsec.do>.

## **08.****Plataforma de pagamento digital GetNet**

A getnet uma plataforma de pagamentos digitais.. Para mais informações acesse

As URL's utilizadas para esta funcionalidade são

URL ckeckout:  
<https://checkout.getnet.com.br/loader.js>  
URL autenticação:  
<https://api.getnet.com.br/auth/oauth/v2/token>  
URL cancelamento:  
<https://api.getnet.com.br/v1/payments/cancel/request>

## **09.****Plataforma de pagamento digital eRede**

A eRede uma plataforma de pagamentos digitais.. Para mais informações acesse

A URL utilizada para esta funcionalidade é <https://api.userede.com.br/erede/v1/transactions>
