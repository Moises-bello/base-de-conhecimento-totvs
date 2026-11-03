---
content_hash: 8e43711025c9d9f2892c10f66038f3c527a5bd0e4b02fe421e9cfee51415a82b
fetched_at: '2026-06-29T00:11:54.511904+00:00'
page_id: '853901989'
product: rm
source: tdn-rm
title: Segurança de Captcha e bloqueio por tentativas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853901989
version: 3
---

Atenção

Ao utilizar o Captcha, o bloqueio por quantidade de tentativas é desativado e para utilizar o bloqueio por quantidade de tentativas, é necessario desativar o Captcha.

## **O que é Captcha e como implementá-lo no Corpore.Net**

O Captcha é um importante mecanismo de segurança utilizado para diferenciar o acesso ao sistema por humanos e máquinas. Este recurso submete o usuário a um teste cognitivo, garantindo que o acesso seja realizado por uma pessoa real e não por um robô automatizado.

A partir da versão 11.82.36.114 do Corpore.Net, o Captcha é exibido automaticamente para o usuário na terceira tentativa de login. Isso adiciona uma camada extra de segurança, prevenindo ataques de força bruta e acessos não autorizados ao sistema.

## **Como ativar o Captcha no Corpore.Net:**

Para ativar o Captcha, é necessário incluir uma configuração específica no arquivo `web.config` do Corpore.Net. Esta configuração deve informar o uso do Captcha e definir o número de tentativas de login permitidas antes que o Captcha seja exibido. Caso o valor da configuração seja "0", o recurso do Captcha será desativado.

Segue um exemplo de como configurar o AppSetting no `web.config`:

### Exemplos:

Ativado com limite de 1 falha: <add key="LoginTimesForCaptcha" value="1" />

Ativado com limite de 5 falhas: <add key="LoginTimesForCaptcha" value="5" />

Desativado: <add key="LoginTimesForCaptcha" value="0" />

Exibição do Captcha para validação do acesso.

## **Bloqueio por tentativas falhas:**

O tempo de bloqueio do usuário é medido em MINUTOS.

## **Comportamento na MDI:**

Após as tentativas configuradas, mesmo com uma senha correta, o usuário permaneceu bloqueado na MDI.

Após o período de bloqueio configurado, o usuário poderá tentar fazer login novamente, desde que suas credenciais sejam válidas.

## **Comportamento no Corpore.Net:**

Após exceder o número de tentativas configuradas, mesmo que o usuário insira a senha correta, ele permanecerá bloqueado no Corpore.Net pelo tempo configurado.

**Referencia documentação antiga:**
