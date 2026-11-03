---
article_id: 37779606978583
category: Meu RH - Férias
content_hash: 902228f5fc915f0f9287686aea5737421bbffa1b8ad6c7dc101b6924f14d6d3c
fetched_at: '2026-06-28T22:47:31.616868+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Erro ao solicitar férias "O servidor SMTP requer uma conexão
  segura ou o cliente não foi autenticado".
type: support-article
updated_at: '2026-01-19T17:50:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37779606978583-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-O-servidor-SMTP-requer-uma-conex%C3%A3o-segura-ou-o-cliente-n%C3%A3o-foi-autenticado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37779606963991) Tempo aproximado para leitura: **00:02:04 min**  
  
**Ocorrência**  
Ao tentar realizar a solicitação de férias no Meu RH, é apresentado a mensagem de erro:

*"Não foi possível enviar o e-mail de assunto: Criação de nova sugestão de férias. Erro: O servidor SMTP requer uma conexão segura ou o cliente não foi autenticado. A resposta do servidor foi: 5.7.0 Authentication Required. For more information, go to Possíveis causas do erro: - Usuário e/ou senha incorretos; - Firewall ou anti-vírus barrando o envio de e-mail; - Domínio errado ou preenchido sem necessidade; - Impossibilidade de conexão com o servidor de e-mail."![](https://centraldeatendimento.totvs.com/hc/article_attachments/37779606965271)*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse erro ocorre quando o [envio de e-mails de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010160561-RH-RM-Meu-RH-Envio-de-e-mails-autom%C3%A1ticos-em-solicita%C3%A7%C3%A3o-de-f%C3%A9rias) está habilitado, porém a parametrização global de envio de e-mails no RM não está configurada corretamente.  
  
**Solução**  
Para solucionar este erro, acesse no RM o módulo **Serviços Globais** > **Ambiente** > **Parâmetros** > **Parâmetros Globais**. Na aba **Envio de E-mails**, preencha corretamente os campos Servidor STMP, Usuário, Senha, Domínio e Porta.

![](https://tdn.totvs.com/download/attachments/69763106/image2013-10-9%2011%3A52%3A17.png?version=1&modificationDate=1381330090000&api=v2&effects=drop-shadow)

Após realizar as parametrizações, clique no ícone em formato de “Raio” para validar o teste de envio. É necessário que seja exibido o alerta informando que a mensagem foi enviada com sucesso. Com esse retorno no RM, o envio de e-mail do Meu RH passará a funcionar corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37779606967319)

Caso seja apresentada a mensagem de erro no Meu RH: *“Erro ao sugerir Férias, não é possível enviar um email sem que o endereço seja informado”*, para correção deve-se seguir as orientações deste artigo: [RH - RM - Meu RH - Erro ao sugerir Férias, não é possível enviar um email sem que o endereço seja informado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418045249303-RH-RM-Meu-RH-Erro-ao-sugerir-F%C3%A9rias-n%C3%A3o-%C3%A9-poss%C3%ADvel-enviar-um-email-sem-que-o-endere%C3%A7o-seja-informado)

**Saiba mais:**

[Envio de email - LINHA RM](https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM)

[Framework - Linha RM - Frame - Utilização da Ferramenta Testa E-mail Global](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058979593-Framework-Linha-RM-Frame-Utiliza%C3%A7%C3%A3o-da-Ferramenta-Testa-E-mail-Global)
