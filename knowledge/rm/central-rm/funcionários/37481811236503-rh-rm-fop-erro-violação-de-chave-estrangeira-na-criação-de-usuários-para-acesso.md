---
article_id: 37481811236503
category: Funcionários
content_hash: 7852601d90e79fdba1aa884645a92266c5d0d18eb240b98a8785afdb3a635c19
fetched_at: '2026-06-28T22:47:03.137360+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Erro Violação de chave estrangeira na criação de usuários para
  acesso ao RM Portal
type: support-article
updated_at: '2026-01-06T20:26:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37481811236503-RH-RM-FOP-Erro-Viola%C3%A7%C3%A3o-de-chave-estrangeira-na-cria%C3%A7%C3%A3o-de-usu%C3%A1rios-para-acesso-ao-RM-Portal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37481811227287) Tempo aproximado para leitura: **00:01:48 min**  
  
**Ocorrência**  
Ao executar a rotina de inclusão de usuários para Acesso ao RM Portal, é apresentado a mensagem de erro "**Violação de chave estrangeira**".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37481811228183)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse erro ocorre, quando a parametrização global de segurança do sistema, está habilitado para validar a complexidade de senha na criação do usuário.

**Solução**  
A rotina de criação de usuários considera apenas duas opções de senha padrão: **CPF** ou **último nome** do colaborador em **letras maiúsculas**. Caso a política de senha configurada nos Parâmetros Globais exija critérios que não são atendidos por essa rotina — como, por exemplo, o uso de caracteres especiais —, será necessário acessar o módulo **Serviços Globais** > **Ambiente** > **Parâmetros Globais** > **Segurança** e desmarcar o parâmetro “**Validar complexidade de senha no cadastro**” para permitir a criação do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37481811229719)

**Observação**: Ao desmarcar este parâmetro, a validação de complexidade da senha será desconsiderada apenas no momento da criação do usuário. Nas alterações posteriores de senha, continuará sendo obrigatório que a nova senha atenda aos requisitos definidos na política de segurança.  
Como boa prática, durante a criação do usuário, é possível marcar o parâmetro **“Usuário deve alterar senha no próximo login**”, garantindo que a senha seja alterada no primeiro acesso.

**Saiba mais:**

[**RH - RM - FOP - Como criar usuário de acesso ao RM Portal para funcionários**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000142561-RH-RM-FOP-Como-criar-usu%C3%A1rio-de-acesso-ao-RM-Portal-para-funcion%C3%A1rios)

[**Framework - Linha RM - Frame - Validar complexidade de senha no cadastro**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28478997125399-Framework-Linha-RM-Frame-Validar-complexidade-de-senha-no-cadastro)
