---
article_id: 6766370650647
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 135e686aa4bae143db319a36ebd3442e379f47fefbeac136e33cf24cf521a55f
fetched_at: '2026-06-28T22:47:29.495391+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Erro ao enviar e-mail sem o endereço do remetente
type: support-article
updated_at: '2025-02-10T12:06:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6766370650647-RH-RM-Meu-RH-Erro-ao-enviar-e-mail-sem-o-endere%C3%A7o-do-remetente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:15 min******Ocorrência****

Ao tentar realizar o procedimento de troca de senha do usuário utilizando o Meu RH é apresentado a mensagem de erro, **Não é possível enviar um e-Mail sem que o endereço do remetente seja informado. Por favor preencha o e-mail da Coligada, no Cadastro de Coligadas**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.32  
  
**Causa**Falta de parametrizações no envio de e-mails nos **Parâmetros Globais.**

**Solução**Acessar **Ambiente | Parâmetros | Parâmetros Globais | Envio de E-Mails.**

Os parâmetros devem ser preenchidos corretamente e então clicar sobre o ícone ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6764941239575/mceclip1.png)para que seja realizado o teste de envio de e-mails.  
  
**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6764918074391/mceclip0.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6766128051735/mceclip2.png)**

Infelizmente existem fatores externos que podem influenciar neste processo, como conexão com a internet, firewall, antivírus, e outras aplicações que podem bloquear processos de envio de e-mail.

Fica a cargo do cliente analisar estes bloqueios externos e liberar que o aplicativo possa realizar o procedimento.

**Importante**

O RM necessita da configuração de relay habilitada, pois irá autenticar no servidor de e-mail com o usuário que está nas configurações globais e enviar como remetente outro usuário(definido nas configurações de parâmetros globais).

**Observação**

Em ambiente **N camadas**, o servidor de Jobs é o responsável pela execução dos processos, incluindo a rotina de processos que enviam e-mail. Dessa forma, considerando esse tipo de ambiente, deve-se realizar o teste de envio de e-mail no servidor de Jobs, e realizar as devidas liberações, quando for necessário bem como no servidor de aplicação.

Em ambiente **local** todas as máquinas de usuários que forem realizar o envio de e-mail, devem receber as liberações de segurança (Firewall, antivírus, proxy, e quaisquer outros aplicativos/configurações de segurança).

**Saiba mais**

Para obter informações adicionais, acesse o link: [RM - Envio de e-mails](https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM#EnviodeemailLINHARM-Configura%C3%A7%C3%A3odateladeenviodee-mails:)
