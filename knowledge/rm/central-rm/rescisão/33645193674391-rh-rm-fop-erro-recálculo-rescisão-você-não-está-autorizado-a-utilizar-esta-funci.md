---
article_id: 33645193674391
category: Rescisão
content_hash: f968fdbffdd70e9e7086f6a4303abad9562e17959900ecd894c32371fbb1b5f7
fetched_at: '2026-06-28T22:46:54.164124+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Erro: Recálculo Rescisão - Você não está autorizado a utilizar
  esta funcionalidade do sistema'
type: support-article
updated_at: '2025-10-15T20:23:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33645193674391-RH-RM-FOP-Erro-Rec%C3%A1lculo-Rescis%C3%A3o-Voc%C3%AA-n%C3%A3o-est%C3%A1-autorizado-a-utilizar-esta-funcionalidade-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33645193640599) Tempo aproximado para leitura: **00:01:19 min**  
  
**Ocorrência**  
  
No módulo Folha de Pagamento, ao tentar recalcular o envelope de pagamento de um colaborador que possui a situação funcional **D- demitido**, o sistema exibe a seguinte mensagem de erro: **Você não está autorizado a utilizar esta funcionalidade do sistema.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33656887206295)  
  
**Ambiente**  
  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
  
Essa mensagem de erro ocorre devido o usuário não estar com a permissão necessária para ações relacionadas a colaboradores demitidos, como o recálculo do envelope.  
  
**Solução**  
  
Para corrigir o problema, siga os passos abaixo:   
  
1. Acesse o menu: **Serviços Globais | Segurança | Perfis | Sistema: Folha de Pagamento.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33645162707095)**  
  
2. Localize o perfil do usuário desejado e clique em **Editar**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33645193646231)  
  
3. Vá até a aba **Acesso a Menus**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33645193646871)  
  
4. Localize a opção: **Rescisão (Ctrl + R): Visualizar**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33645162713495)  
  
5. Marque a opção **Permitir Acesso** e salve.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33645162714391)  
  
Após essa alteração, o usuário poderá recalcular envelopes de colaboradores com situação **“D”**.  
  
**Saiba Mais**  
  
[RH - RM - FOP - Liberação e restrição de permissões de acesso a campos e menus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414666224023-RH-RM-FOP-Libera%C3%A7%C3%A3o-e-restri%C3%A7%C3%A3o-de-permiss%C3%B5es-de-acesso-a-campos-e-menus#:~:text=Como%20liberar%20ou%20restringir%20permiss%C3%B5es,do%20m%C3%B3dulo%20Folha%20de%20Pagamento%3F&text=Para%20liberar%20ou%20restringir%20o,%7C%20Sistema%3A%20Folha%20de%20Pagamento.)
