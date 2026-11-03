---
article_id: 360018868272
category: ADVPL - Classe e Função
content_hash: 98ec5a5cb52804cf6bf4c1b4cfc5d12e556aec68dfdd480ac0c67224558e71d5
fetched_at: '2026-06-28T22:40:17.156922+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Restrições de acessos
  a rotinas especificas '
type: support-article
updated_at: '2023-09-01T13:14:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018868272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Restri%C3%A7%C3%B5es-de-acessos-a-rotinas-especificas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como restringir o acesso de um usuário em uma rotina específica?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
Para efetuar restrições de rotinas específicas dentro do Protheus, acessar o **SIGACFG** com o cadastro do Administrador  
1. Acesse o menu **Usuário** > **Senhas** > **Usuários**;

![KCSCFG1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014922751/KCSCFG1.png)  
2. Selecione o usuário que deseja restringir o acesso, e clique na opção **Alterar**;

![KCSCFG2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014889492/KCSCFG2.png)  
3. Acesse **restrições de acessos** e depois **ambientes**;

![KCSCFG3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014923091/KCSCFG3.png)

4. Para selecione a rotina que deve ter acesso restrito ao usuário, clique em **Outras Ações** > **Restrição de rotina do menu**;

![KCSCFG4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014923251/KCSCFG4.png)

5. Selecione a rotina desejada e clique em **Acessos.****Nesta opção existe a possibilidade de restringir o acesso do usuário a todos os itens da rotina ou apenas alguns. Neste exemplo, será restringido o acesso do usuário para efetuar a Inclusão e Alteração de informações:**

**![KCSCFG5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014890312/KCSCFG5.png)**

Quando o usuário for acessar a rotina **FINA010**(exemplo) ao tentar clicar sobre a opção **"Incluir" ou "Alterar**", o sistema apresentará a seguinte mensagem:

![KCSCFG6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014890512/KCSCFG6.png)
