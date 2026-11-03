---
article_id: 23057454463511
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: ff4ae0a9887733daba54471a7bb4502874473049d80e9fa8df944c15e9b14eb1
fetched_at: '2026-06-28T22:38:44.173587+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Restringir ação/botão/permissão
  por rotina no faturamento
type: support-article
updated_at: '2026-03-26T12:56:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23057454463511-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Restringir-a%C3%A7%C3%A3o-bot%C3%A3o-permiss%C3%A3o-por-rotina-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23057469165591) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como restringir ação/botão/permissão por rotina no módulo faturamento?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**  
É possível deixar certos usuários impossibilitados de realizar certas ações de acordo com a regra de negócio da empresa. Para isso, siga os passos a seguir, no exemplo, será retirado do usuário a ação "excluir nota fiscal de saída":

1 - Entre na rotina que deseja retirar a permissão do usuário. Aperte as teclas "Shift" + "F6" e visualize o nome da rotina, a figura 1 é quando a central diagnóstica não está habilitada:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057469172247)![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057454437911)

2 - Entre no configurador (SIGACFG), no caminho: "Usuário" > "Senhas" > "Usuários" > Selecione o usuário que quer tirar o acesso de algo e vá no botão "Alterar".

* Dúvida nesse passo, contate a Equipe Framework.

3 - Vá na aba superior "Restrições de Acesso" > Depois na aba inferior "Ambientes" > Selecione o módulo onde a rotina está (SIGAFAT) > botão superior "Outras Ações" > "Restrição de rotina do menu":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057454441239)

4 - Na janela, procure pelo mesmo nome da rotina visto no passo 1, selecione-a e clique em "Acessos":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057454443543)

5 - Agora, basta tirar a seleção das ações da rotina em que deseja que o usuário não tenha acesso para realizar > apertar "Ok" > Salvar todas as telas abertas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057718825111)

Quando o usuário tentar excluir na rotina no botão bloqueado, ocorrerá essa mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23057695376151)
