---
content_hash: bcf199cdab9c7a717a966f042de2ed0b872691519a7e106ac99fab8e9cee4cac
fetched_at: '2026-06-29T00:05:57.633371+00:00'
page_id: '179700232'
product: rm
source: tdn-rm
title: Habilitar e Desabilitar Captcha na tela de Login
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitar+e+Desabilitar+Captcha+na+tela+de+Login
version: 1
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.82.36 e superiores |
| **Processo** | **:** | RM Portal - Web |
| **Subprocesso** | **:** | Habilitar e Desabilitar Captcha na tela de Login. |
| **Data da publicação** | **:** | 28/11/2014 |

O Captcha é um mecanismo de seguraça no qual o usuário é submetido à um teste cognitivo a fim de validar o uso do sistema por um humano e não por uma máquina.

A partir da versão 11.82.36.114 e superiores, o captcha é exibido automaticamente para o usuário na terceira tentativa de login.

Para alterar essa configuração, utiliza-se a tag no web.config:

**<add key="LoginTimesForCaptcha" value="7" />**

O valor determina a quantidade de tentativas de login sem sucesso para que o captcha seja exibido. Colocando o valor 0 (zero) o recurso pode ser desabilitado.
