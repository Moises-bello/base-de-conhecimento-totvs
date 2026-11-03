---
article_id: 360025393071
category: Configurador
content_hash: 1e3b9314029e8cd2d22fae18fc2a93c8ae6627f7d18dcd3c144d163254bcecf1
fetched_at: '2026-06-28T22:42:18.985075+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Configurar o SMTP para envio de relatórios por
  e-mail
type: support-article
updated_at: '2026-02-06T13:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-Framework-Linha-Protheus-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail
---

**Dúvida**Como configurar o envio de relatórios por e-mail no Protheus?  
  
**Ambiente**Protheus – Configurador – A partir da versão 11  
  
**Solução**Segue abaixo procedimento de como configurar o envio de relatórios por e-mail (configuração de E-mail / Proxy), utilizando como exemplo uma conta do Gmail. Para outros provedores de e-mail (SMTP), favor consultar as informações com seu provedor e substituir nos campos correspondentes.  
  
1. Acesse o Configurador > Ambiente > E-mail/Proxy > **Configurar**  
![Picture_2017-01-19_11_42_50.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023943091)

|  |
| --- |
| Obs. 1: atualmente a maioria dos provedores SMTP utilizam uma porta diferente da padrão, geralmente usam a 465 ou 587. Essa porta deve ser informada no campo do endereço do SMTP, logo após o endereço, utilizando :###   Obs. 2: o Gmail utiliza a porta 465 quando a segurança utilizada é a SSL e a porta 587 quando a segurança é a TLS (o tipo de segurança será configurado na próxima tela da configuração de E-mail/Proxy) |

![Picture_2017-01-19_11_54_22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023943151)  
  
![Picture_2017-01-19_11_55_14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023915412)  
  
2. Se o Appserver do Protheus está em um servidor que tenha um Proxy configurado, é necessário ativar a opção **Utilizar servidor de Proxy** e preencher as informações da tela acima.  
  
**Configurando com a utilização do Office 365 (Office Online) como provedor SMTP**Se for utilizar o Office365 como SMTP, utilize as informações abaixo, substituindo nos respectivos campos do exemplo das imagens acima:  
  
**Página 1**  
Servidor SMTP:  
smtp.office365.com:587  
Conta:  
[seu\_email@seudominio.com.br](mailto:seu_email@seudominio.com.br)  
Senha:  
Sua senha  
Servidor necessita de autenticação?  
SIM  
Time-out em segundos:  
120  
E-mail utilizado no campo FROM:  
\* Obrigatoriamente o mesmo e-mail da Conta  
  
**Página 2**  
Protocolo de recebimento:  
POP3  
Utiliza SMTP Extended?  
Sim  
Utiliza segurança TLS?  
Sim  
Utiliza segurança SSL?  
Sim  
  
Ao efetuar um teste de envio com sucesso, uma **mensagem de confirmação** deverá ser exibida, conforme exemplo abaixo:  
  
![Picture_2017-01-19_11_55_59.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023943211)
