---
article_id: 16841461768343
category: PMS - Projetos
content_hash: 8cc91f7ac24ea030da914ea9bc7a9d6fdcc73ad0c1dc174fb584f3092e80b2f4
fetched_at: '2026-06-28T22:37:15.990696+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Opções/funcionalidades
  do projeto bloqueadas
type: support-article
updated_at: '2023-08-17T17:53:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16841461768343-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Op%C3%A7%C3%B5es-funcionalidades-do-projeto-bloqueadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16841433982103) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como liberar certas funcionalidades/opções bloqueadas?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as versões  
  
  
**Solução**Nos projetos, é permitido colocar regras do que pode-se fazer ou não, dependendo do usuário inserido ou da fase em que está o projeto.

Por conta disso, algumas funcionalidades, podem estar na coloração "cinza". Ou por conta de regra de negócio do fluxograma de projeto ou, muitas vezes o que ocorre é, por estarem bloqueadas por regras de projeto ou usuário, por exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16840842492695)

Caminho da funcionalidade acima: "Rotina (PMSA410) > Outras Ações > Alterar Estrutura > Outras Ações > Progresso Físico do Projeto > Confirmações"

Quando isso ocorre, pode estar bloqueado de duas maneiras, regra de usuário e regras de fases de projetos. Para identificar, basta ver o nome do botão/caminho que está indisponível.

Exemplo: Acima podemos ter como pista "Confirmações" e "Progresso Físico do Projeto", basta procurarmos nas regras do projeto e regras de usuário, campo com essa definição.

**1 - Procurando na rotina "Fases do projeto (PMSA070)" na fase em que o projeto está:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16840946789783)

1.1 - Podemos ver que há uma aba chamada "Confirmações" do projeto, exatamente onde tem uma funcionalidade disponível, pode-se alterar as opções dessa aba para "Permitir", para que o botão seja utilizável:

Antes:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16840991791895)

Depois:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16840975923095)

Se ainda assim não liberar o campo, vamos para o passo 2.

**2 - Procurando nas regras do usuário "rotina (PMSA200) > Outras Ações > Usuários":**

2.1 - Expanda toda a árvore para que seja exibido todas as EDTs/Tarefas do projeto em que o usuário que não consegue usar a funcionalidade/botão está, mesmo se for o administrador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841123655575)

2.2 - Selecione sobre o usuário que não consegue consegue usar a funcionalidade/botão vá em "Outras Ações > Usuarios > Alterar propriedades" e verifique se há algo que remeta a "Confirmações" ou "Progresso Físico do Projeto":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841152273047)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841217736087)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841221645591)

2.3 - Podemos ver que há um campo específico para "Confirmações", vamos liberá-lo também:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841242894487)

2.4 - Resultado: Agora é possível usar a funcionalidade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16841333016215)

**OBSERVE:** Se o mesmo usuário estiver em mais de um espectro, ou seja, regras do mesmo usuário na tarefa, EDT e projeto, deve ser liberado em todos eles, para verificar a hierarquia da prioridade de regra, veja:

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Hierarquia na consideração de regras em projetos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16831093650711)**
