---
article_id: 37059977420951
category: Integração
content_hash: 14014cef0d9e2ee8c7b3900c46d2b6d345d1113167a663c14e9d7d4414b13256
fetched_at: '2026-06-28T22:46:34.622136+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO - Erro Incorrect login or password na integração com Clockin
type: support-article
updated_at: '2025-12-16T14:37:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37059977420951-RH-RM-PTO-Erro-Incorrect-login-or-password-na-integra%C3%A7%C3%A3o-com-Clockin
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37060009906967) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao realizar o processo de importação de batidas com integração Clockin, é apresentado o erro no log:   
  
*Http content: {"applicationErrorCode":null,"errorCode":401,"errorMessage":"**Incorrect login or password**.","possibleResponsibleField":"**userLogin/password**"}*  
*Geração de token de autenticação finalizada com erro.*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 12.1

**Causa**  
Esse incidente ocorre, pois o usuário e senha utilizados nos parâmetros da integração estão incorretos.  
  
**Solução**  
Para solucionar o erro, realize os seguintes passos:

1. Acesse o módulo RM Totvs Automação de Ponto;
2. Navegue até a guia de Configurações;
3. Selecione a opção Parametrizador;
4. Clique em Iniciais;
5. Vá até a seção Integração;
6. Redigite o usuário e a senha específicos para a integração (avalie se o Nome organização e Nome do Ambiente também estão preenchidos corretamente). Avance as etapas até a conclusão do assistente.

![carol.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37059977411607)

7. Após ajustes, realize novamente o processo de importação de batidas.
