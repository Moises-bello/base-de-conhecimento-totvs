---
article_id: 360007203832
category: Administração de Pessoal
content_hash: 8de661ac7d78b862f4ba40879a67b0e6d7618afc408ad919b7218c190b47574c
fetched_at: '2026-06-28T22:47:02.384281+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Erro no cadastro de cargos
type: support-article
updated_at: '2025-03-06T19:35:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007203832-RH-RM-FOP-Erro-no-cadastro-de-cargos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:40 min  
  
Ocorrência**No módulo **Folha de pagamento**, ao tentar realizar o **Cadastro de cargos** através da aba Administração de pessoal | Cargos é apresentada a mensagem **Você não está autorizado a utilizar esta funcionalidade do sistema!**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10590917329175)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Causa**Esse incidente ocorre, pois é necessário que o usuário tenha algumas permissões no módulo **Gestão de Pessoas** que estão desabilitadas, o que gera a mensagem de erro.   
  
**Solução**Para solucionar esta ocorrência, realize os seguintes passos:  
  
1. Acessar o módulo **Serviços Globais;**2. Dentro do módulo, acessar **Segurança | Perfis;**3. Ao selecionar a opção **Perfis**, ajustar a opção **Sistema**para o módulo **Gestão de pessoas**conforme abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10590914440727)  
  
4. Localize o perfil vinculado ao usuário neste módulo e verifique se a permissão **[01.05] Controle de Lotação**está habilitada para o perfil:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10590911856023)  
  
**Importante**É necessário verificar em qual perfil o usuário está vinculado no módulo Gestão de Pessoas, já que é possível que ele esteja vinculado a perfis diferentes nos diferentes módulo do sistema. A verificação pode ser realizada através de **Segurança | Usuários.**
