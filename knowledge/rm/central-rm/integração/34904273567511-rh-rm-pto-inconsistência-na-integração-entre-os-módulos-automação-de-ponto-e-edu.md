---
article_id: 34904273567511
category: Integração
content_hash: f31eb8e458dd46e0adb49db95f18c0a85a03ce9f9eb090c268bf709dee701897
fetched_at: '2026-06-28T22:46:34.639780+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO -  Inconsistência na integração entre os módulos  Automação de
  Ponto e Educacional
type: support-article
updated_at: '2025-10-08T18:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34904273567511-RH-RM-PTO-Inconsist%C3%AAncia-na-integra%C3%A7%C3%A3o-entre-os-m%C3%B3dulos-Automa%C3%A7%C3%A3o-de-Ponto-e-Educacional
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34904273553943) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O que deve ser validado quando ocorrer um erro na integração entre o módulo de Automação de Ponto e o Educacional?  
Erros comuns “o funcionário X da coligada 1 é professor e não tem horário definido no RM Classis”.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1-Professor usa horário do Automação de Ponto:**Caso o professor utilize o horário cadastrado no Ponto, Siga as orientações do link abaixo até o passo 4, avance as etapas até concluir e logo após tente importar as batidas:

[RH - RM - PTO - Considerar o horário do Automação de Ponto para professores](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028201852-RH-RM-PTO-Considerar-o-hor%C3%A1rio-do-Automa%C3%A7%C3%A3o-de-Ponto-para-professores)

**2- Professor usa horário do Educacional (com base no plano de aulas):**Caso utilize o plano de aula do Educacional, faça a validação apontada abaixo:

**2.1-** Acesse no módulo de educacional cadastre o Horário na Turma/Disciplina conforme documentação abaixo:

[TOTVS Educacional - Educacional - EDU - Cadastrar Horário na Turma/Disciplina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003030812-TOTVS-Educacional-Educacional-EDU-Cadastrar-Hor%C3%A1rio-na-Turma-Disciplina)

**2.2-** Logo após confira se o professor está associado aos horários, segue documentação:

[TOTVS Educacional - Educacional - EDU - Professor do Horário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003033872-TOTVS-Educacional-Educacional-EDU-Professor-do-Hor%C3%A1rio)

**2.3-** Realizado os passos acima gere o plano de aula e faça a importação novamente:

[TOTVS Educacional - Educacional - EDU - Gerar Plano de Aula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003035552-TOTVS-Educacional-Educacional-EDU-Gerar-Plano-de-Aula)

**3-** Para facilitar, segue abaixo uma captura de tela dos menus que devem ser verificados no módulo do Educacional:

**3.1-** Período letivo. Acesse o caminho: **Currículo Oferta | Períodos letivos**, em seguida, valide se o período letivo desejado já está cadastrado no sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34954606108311)

**3.2-** Data, início e fim da turma. Acesse o caminho: **Currículo e Oferta | Turmas** e verifique se as datas de início e término da turma estão configuradas conforme o desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34958837837335)

**3.3-** Data, fim e início da turma disciplina. Acesse o caminho **Currículo e Oferta | Turmas/Disciplinas** e verifique se as datas de início e término da turma/disciplina estão configuradas conforme o desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34958868275607)

**3.4-** Data, inicio e fim de associação do professor na turma disciplina. Acesse o caminho: **Currículo e Oferta | Turmas/Disciplinas**, filtre pelo período letivo, vai apresentar a turma/disciplina, vai **Anexos|Professores**, vai apresentar os professores que estão associados, edite o registro e verifique a data, início e fim que está associada ao professor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34959240442263)

**3.5** Aí seguir acesse pelo caminho: **Currículo e Oferta | Turmas/Disciplinas**, filtre pelo período letivo desejado, selecione este período e vá **Anexos | Plano de aula,** e verifique se possui as aulas geradas para o período desejado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34959807348887)

**Importante:**  
As datas do plano de aula cadastradas no módulo Educacional devem estar conforme as datas do período do módulo de Automação de ponto.

**Saiba mais**  
Para mais informações referente a integração dos módulos Educacional x Automação de ponto acesse as documentações:

[Importação Horário Professor](https://tdn.totvs.com/pages/releaseview.action?pageId=452719003)  
[Integração Ponto x Educacional](https://tdn.totvs.com/pages/releaseview.action?pageId=86474759)  
[RH - RM - PTO - Importar horário do professor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000249547-RH-RM-PTO-Importar-hor%C3%A1rio-do-professor)
