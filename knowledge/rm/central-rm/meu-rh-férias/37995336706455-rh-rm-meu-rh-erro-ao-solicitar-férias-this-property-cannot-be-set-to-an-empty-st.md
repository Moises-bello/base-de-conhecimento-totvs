---
article_id: 37995336706455
category: Meu RH - Férias
content_hash: 9edbaf0b6750ac85bb90fe55e8412f327f6bc694e38c5b5a829ebea162da6fb4
fetched_at: '2026-06-28T22:47:31.596744+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: 'RH - RM - Meu RH - Erro ao solicitar férias "This property cannot be set to
  an empty string. Parameter name: value".'
type: support-article
updated_at: '2026-01-28T19:36:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37995336706455-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-This-property-cannot-be-set-to-an-empty-string-Parameter-name-value
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37995336694807) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao tentar realizar a solicitação de férias no Meu RH, é apresentado a mensagem de erro: "This property cannot be set to an empty string. Parameter name: value".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995307501975)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse erro ocorre quando o[**envio de e-mails de férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010160561-RH-RM-Meu-RH-Envio-de-e-mails-autom%C3%A1ticos-em-solicita%C3%A7%C3%A3o-de-f%C3%A9rias) está habilitado, porém a parametrização global de envio de e-mails no RM não está configurada corretamente.  
  
**Solução**  
Para solucionar este erro, acesse no RM o módulo Serviços Globais > Ambiente > Parâmetros > Parâmetros Globais. Na aba Envio de E-mails, preencha corretamente os campos Servidor STMP, Usuário, Senha, Domínio e Porta.

![](https://tdn.totvs.com/download/attachments/69763106/image2013-10-9%2011%3A52%3A17.png?version=1&modificationDate=1381330090000&api=v2&effects=drop-shadow)

Após realizar as parametrizações, clique no ícone em formato de “Raio” para validar o teste de envio. É necessário que seja exibido o alerta informando que a mensagem foi enviada com sucesso. Com esse retorno no RM, o envio de e-mail do Meu RH passará a funcionar corretamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37995307505815)

**Saiba mais:**

[Envio de email - LINHA RM](https://tdn.totvs.com/display/public/LRM/Envio+de+email+-+LINHA+RM)

[Framework - Linha RM - Frame - Utilização da Ferramenta Testa E-mail Global](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058979593-Framework-Linha-RM-Frame-Utiliza%C3%A7%C3%A3o-da-Ferramenta-Testa-E-mail-Global)

[RH - RM - Meu RH - Erro ao solicitar férias "O servidor SMTP requer uma conexão segura ou o cliente não foi autenticado".](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37779606978583-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-O-servidor-SMTP-requer-uma-conex%C3%A3o-segura-ou-o-cliente-n%C3%A3o-foi-autenticado)
