---
article_id: 17737986260503
category: PMS - Projetos
content_hash: beb37037b35341257b7f4274d8f486d2a6c3ccf186ae7acf97f1b791b4d8294e
fetched_at: '2026-06-28T22:37:15.995064+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Usuário sem
  permissão no módulo PMS
type: support-article
updated_at: '2023-09-22T15:24:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17737986260503-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Usu%C3%A1rio-sem-permiss%C3%A3o-no-m%C3%B3dulo-PMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17737954636439) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Ao tentar realizar algumas ações no módulo PMS, aparece a mensagem: "Usuário sem permissão", como resolver?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as versões  
  
**Solução**Dentro do módulo do PMS, é possível restringir certas ações, tanto restringir alguma ação em projetos por conta da fase em que o projeto (PMSA070)/orçamento (PMSA060) se encontram ou por conta de permissões de usuário (PMSA200 > Usuários).

![RESTRICOES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17738001576855)

É importante salientar, que o controle de permissão do PMS (esquerda) é diferente do controle do configurador (Privilégios - SIGACFG) (direita).

O controle do configurador (Privilégios - SIGACFG) tem mais prioridade que o do módulo PMS.

Solução para retirar o bloqueio de usuário:

1 - Selecionar um usuário com permissão ou o usuário criador do projeto e entrar no sistema Protheus.

2 - Ir no caminho: Gerenciamento de Projetos (PMSA200) > Outras Ações > Usuários > Expandir no "mais" as árvores:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17737780786327)

3 - Ver o PROJETO/EDT/TAREFA e visualizar qual usuário dentro dela está sem a permissão/com a mensagem ocorrendo, no exemplo acima, podemos ver o usuário "VINI" posicionado sobre a tarefa "01.03".

4.1 - Opção 1 (caso queira remover a validação):  Selecionar o usuário com problema > Outras Ações > Usuários > Excluir

4.2 - Opção 2: Selecionar o usuário com problema > Outras Ações > Usuários > Alterar propriedades

5 - Procurar o campo com a opção que o usuário está tentando realizar e não consegue. No exemplo, o pré-apontamento estava bloqueado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17737886125463)

6 - Alterar para "Controle total" ou "Alterar" e Salvar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17737921606551)

7 - Sair e entrar na rotina com o usuário que não estava conseguindo realizar a alteração.

**Saiba mais:**  
**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Hierarquia na consideração de regras em projetos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16831093650711)**
