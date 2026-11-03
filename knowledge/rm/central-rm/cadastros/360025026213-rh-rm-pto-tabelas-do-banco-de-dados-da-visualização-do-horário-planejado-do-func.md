---
article_id: 360025026213
category: Cadastros
content_hash: 3e3ac529fa56d06c53bf81c3cd1e08f22069f388571df3f6a1c45c5e4fd6f64a
fetched_at: '2026-06-28T22:46:28.486823+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Tabelas do banco de dados da visualização do horário planejado
  do funcionário
type: support-article
updated_at: '2026-02-13T22:46:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025026213-RH-RM-PTO-Tabelas-do-banco-de-dados-da-visualiza%C3%A7%C3%A3o-do-hor%C3%A1rio-planejado-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17200705028247) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Quais as tabelas do banco de dados que guardam a informação da jornada planejada do funcionário?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**  
O horário planejado do funcionário é gerado no sistema, em vez de estar em uma tabela específica, ele é composto por um conjunto de informações que consideram diversos fatores, como histórico de horários, afastamentos, férias, descansos, feriados, entre outros.

Para montar a visualização do horário do funcionário, o sistema utiliza o código-fonte e a função dataserver PtoDataViewHorarioFuncionario, que se baseia nas informações das tabelas de horário e outras tabelas associadas. Abaixo estão algumas tabelas que podem ajudá-lo a obter as informações desejadas:   
AHORARIO - Horários por intervalo  
AINDHOR - Letras Associadas aos Índices  
AJORHOR - Jornadas dos Horários  
ABATHOR - Batidas dos Horários  
PFUNC - Funcionários  
PFHSTHOR - Histórico de Horários  
AHORARIOJORNADA - Horário por Jornada  
AINDICEJORNADA - Indíce do Horário por Jornada  
AJORNADAFUN - Histórico de Horário por Jornada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29219626745879)
