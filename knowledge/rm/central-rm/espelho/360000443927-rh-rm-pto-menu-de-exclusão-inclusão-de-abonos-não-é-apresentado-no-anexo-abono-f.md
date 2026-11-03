---
article_id: 360000443927
category: Espelho
content_hash: 84bc44a46d6af423dda769eceb9c2dd1da1820302d25168e17afd675a69b4a0b
fetched_at: '2026-06-28T22:46:31.319307+00:00'
product: rm
section_id: 6045459696023
source: central-rm
title: RH - RM - PTO - Menu de exclusão / inclusão de abonos não é apresentado no
  anexo Abono Funcionário
type: support-article
updated_at: '2025-01-28T14:16:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000443927-RH-RM-PTO-Menu-de-exclus%C3%A3o-inclus%C3%A3o-de-abonos-n%C3%A3o-%C3%A9-apresentado-no-anexo-Abono-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16783347047831) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**  
No módulo **Automação de Ponto**, o menu de exclusão / inclusão de abonos não é apresentado na aba de anexo **Abono Funcionário**.

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80

**Causa**Esse incidente ocorre devido à falta de permissão no perfil associado ao usuário que está realizando o acesso ao sistema.

**Solução**Para habilitar as permissões de inclusão\exclusão de abonos, siga os seguintes passos.

1. Acesse no modulo de Serviços Globais o menu, Segurança > Usuários, selecione o sistema Automação de Ponto. Selecione e edite o seu usuário e clique na aba segurança e confira quais são os perfis associados ao usuário.  
   ![RvwkvJjGA9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29556988737175)
2. Acesse no modulo de Serviços Globais o menu Segurança > Perfis, selecione o sistema Automação de Ponto. Selecione e edite o perfil vinculado ao usuário e clique na aba acesso a menus dê a permissão ao itens de abono funcionário.

   ![RvwkvJjGA9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29556988737175)

   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/29557011126423)**
3. Salve as alterações e realize um logout\login no sistema.
