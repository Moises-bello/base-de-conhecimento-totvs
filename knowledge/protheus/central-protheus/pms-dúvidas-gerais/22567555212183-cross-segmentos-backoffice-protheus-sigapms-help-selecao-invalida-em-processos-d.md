---
article_id: 22567555212183
category: PMS - Dúvidas Gerais
content_hash: dbfe54af4ce1472b653955fad75938689f604f4ee1959934c7d3061a4e52140e
fetched_at: '2026-06-28T22:37:17.668131+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Help "Selecao Invalida."
  em processos de projetos (SIGAPMS)
type: support-article
updated_at: '2025-01-10T19:56:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22567555212183-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-Selecao-Invalida-em-processos-de-projetos-SIGAPMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22567570172183) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como resolver o Help "Selecao Invalida." em processos de projetos (SIGAPMS)?

![](https://atendimento.totvs.com/attachments/token/7W9n8daC98UTzo4GncLe6Ha8w/?name=image004.png)

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Solução**Esse erro ocorre por conta das permissões de usuários (tabela AFX):

Solução:

1 - Selecionar um usuário com permissão ou o usuário criador do projeto e entrar no sistema Protheus.

2 - Ir no caminho: Gerenciamento de Projetos (PMSA200) > Projeto que está envolvido no processo > Outras Ações > Usuários > Expandir no "mais" as árvores:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22567555187863)

3 - Ver o PROJETO/EDT/TAREFA e visualizar qual usuário está com erro, localizá-lo (ou não) dentre o projeto, EDT e Tarefa acima e acrescentar o usuário caso não exista ou alterar a propriedade dele, acrescentando permissões.

4 - Procurar o campo com a opção que o usuário está tentando realizar e não consegue (caso ele exista no projeto/tarefa/EDT que causa o Help.

No exemplo, o pré-apontamento estava bloqueado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22567570175383)

**OBS:** Para entender sobre permissões/privilégios e hierarquia de permissões no módulo de projetos (SIGAPMS), verifique os links do saiba mais.

**Saiba mais:**

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Usuário sem permissão no módulo PMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17737986260503-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Usu%C3%A1rio-sem-permiss%C3%A3o-no-m%C3%B3dulo-PMS)

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Hierarquia na consideração de regras em projetos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16831093650711)
