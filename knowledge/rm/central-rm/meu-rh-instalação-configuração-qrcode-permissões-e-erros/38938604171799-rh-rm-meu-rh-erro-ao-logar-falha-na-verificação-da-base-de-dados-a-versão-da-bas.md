---
article_id: 38938604171799
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 3320fff84688987526850fe88db30b52d33abee7727a898dbe40aefc764410f9
fetched_at: '2026-06-28T22:47:29.443286+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: 'RH - RM - Meu RH - Erro ao logar: Falha na verificação da base de dados! A
  versão da Base de Dados é mais recente'
type: support-article
updated_at: '2026-03-11T17:32:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38938604171799-RH-RM-Meu-RH-Erro-ao-logar-Falha-na-verifica%C3%A7%C3%A3o-da-base-de-dados-A-vers%C3%A3o-da-Base-de-Dados-%C3%A9-mais-recente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38938604157079) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar o login no Meu RH, é apresentado a mensagem de erro "Falha na verificação da base de dados! A versão da Base de Dados é mais recente que a versão do aplicativo!".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38938629972247)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH – Todas as versões  
  
**Causa**  
Esse incidente ocorre quando há **divergência de versão entre a base de dados e as bibliotecas do RM ou do RM Portal**.

Por exemplo:

* A **Base de Dados** foi migrada para a versão **12.1.2602**
* Porém o **RM / RM Portal** está na versão **12.1.2510**

Nesse cenário, as versões ficam **diferentes entre si**, ocasiona o erro em questão.  
  
**Solução**  
Para o funcionamento correto, é necessário a **Biblioteca RM**, **RM Portal** e **Base de dados** estejam sempre na mesma versão/patch. Exemplo:

* Versão Biblioteca RM: **12.1.2602**
* Versão RM Portal: **12.1.2602**
* Versão Base de dados: **12.1.2602**

Caso exista divergência entre essas camadas, é necessário realizar a atualização do RM / Portal ou da Base de Dados, garantindo que todas estejam na mesma versão.

Para saber como identificar a versão da Biblioteca RM e RM Portal, acesse: [RH - RM - Meu RH - Como verificar Versão e Patch da Biblioteca RM e Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402311146263-RH-RM-Meu-RH-Como-verificar-Vers%C3%A3o-e-Patch-da-Biblioteca-RM-e-Meu-RH)

Para saber como identificar a versão da Base de dados, acesse: [Framework - Linha RM - Frame - Identificar a versão da base de dados](http://centraldeatendimento.totvs.com/hc/pt-br/articles/360007205952-Framework-Linha-RM-Frame-Identificar-a-vers%C3%A3o-da-base-de-dados)

**Saiba Mais:**

[**Framework - Linha RM - Frame - Como atualizar o release da biblioteca RM**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115016056328-Framework-Linha-RM-Frame-Como-atualizar-o-release-da-biblioteca-RM)
