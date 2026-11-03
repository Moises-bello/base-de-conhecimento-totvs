---
article_id: 360051550453
category: RH - Cálculos
content_hash: 4804a0bf24f1207f5b5d9482997e9cc1f6bdf1e33426f7be15dfe4522b5b2cc0
fetched_at: '2026-06-28T22:44:51.604014+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON -  Como fazer e qual a finalidade do Cálculo Mensal
type: support-article
updated_at: '2025-10-17T20:26:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550453-RH-Linha-Protheus-PON-Como-fazer-e-qual-a-finalidade-do-C%C3%A1lculo-Mensal
---

**Dúvida**Como fazer e qual a finalidade do Cálculo Mensal?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Esta rotina tem como objetivo **apurar os eventos gerados durante o período** de apontamento, e de acordo com a parametrização destes eventos, **determina** o que deve ser computado no **Banco de Horas** ou gera **Verba** nos **Resultados** do funcionário.   
O **Cálculo Mensal** não gera **Log de Ocorrências**, apenas se ocorrer algum **problema** no processo.  
**Importante ressaltar** que esta rotina só pode ser utilizada para **períodos em aberto**, e que é de **extrema importância** que se tenha **atenção à data base**, que deve estar no **último dia do período de apontamento**.  
  
A rotina pode ser encontrada no **SIGAPON** em **Miscelanea - Cálculos - Cálculo Mensal.**

São calculados os eventos como o desconto de DSR, atrasos, a saídas antecipadas, horas extras quando a apuração (definido na regra de apontamento) é diferente de “diário”, os eventos que irão para banco de horas e totalizar (levar para os resultados) as refeições.  
Serão identificados durante o processo, os eventos que irão para o Banco de Horas e os que serão enviados a Folha de Pagamento (Resultados).  
  
Entram para o cálculo mensal eventos apontados, ou seja, registros existentes em atualizações > lançamentos > apontamentos, por este motivo o cálculo mensal só deve ser executado depois de ter sido realizado apontamento das marcações.  
  
Outro objetivo do cálculo mensal é o desconto de DSR é descontar as horas referentes aos dias de DSR e feriados para funcionários que não cumpriram integralmente a carga horária estabelecida para o período de apuração. No cadastro de eventos devem ser indicados os eventos que compõem a base de cálculo do desconto. Os eventos que serão considerados devem ter o campo “Desc. DSR” (P9\_DESCDSR) com “Sim”.

Na regra de apontamento (atualizações > cadastro ponto > regra de apontamento) define-se o período de apuração do desconto conforme o campo “Apur.Des.DSR.” (PA\_PERDDSR).  
Serão considerados DSR todos os dias classificados com o tipo “DSR” na tabela de horário padrão e também os dias considerados feriados (atualizações > cadastro ponto > feriados).  
  
Os eventos utilizados para o desconto de DSR são os que tiverem vinculados aos identificadores de cálculo 017N ou 018A, se será autorizado, 018A, ou não autorizado, 017N, vai depender de como estiver configurado o campo “Desc. DSR” da regra de apontamento do cadastro de funcionário (RA\_REGRA) do funcionário que está sendo processado, campo PA\_DESCDSR, para que o evento seja levado para a folha de pagamento, como desconto, no cadastro de evento o identificador deve estar vinculado a um “Código para a folha” (verba), no campo P9\_CODFOL.

Os **parâmetros** disponíveis na rotina, são:  
- Filial De/Até?  
- Centro de Custo De/Ate?  
- Turno De/Até?  
- Matrícula De/Até?  
- Regra de Apontamento De/Até?  
- Nome De/Até?  
- Situações a Gerar?  
- Categorias a Gerar?  
- Gerar Horas/DSR? (existem as opções: **Horas da Tabela** = que leva em consideração **apenas** o cadastro da **Tabela de Horário Padrão** OU **Horas Apontadas** = que leva em consideração os **apontamentos do período**)  
- Data Inicial/Final?  
- Tipo Refeição De/Até?  
- Agrupar Eventos? (se **SIM** = as verbas **já calculadas** são **somadas** de acordo com **cada cálculo** que for feito; se **NÃO** = a cada novo cálculo as **verbas são sobrescritas**. Documentação com maiores detalhes: [RH - Linha Protheus - PON - Funcionalidade da pergunta Agrupa Eventos no Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007974992-RH-Linha-Protheus-PON-Funcionalidade-da-pergunta-Agrupa-Eventos-no-C%C3%A1lculo-Mensal?source=search))  
- Qual Tipo Contrato? (se o **cálculo** for feito apenas para **funcionários mensalistas**, **independente do tipo de contrato ser determinado ou não**, você pode selecionar a opção **TODOS**. É necessário **atenção** apenas quando se tratar de funcionários de contrato **Intermitente**, pois nestes casos, o **cálculo** deve ser feito para **as datas exatas da convocação**, e nesta pergunta, deve ser selecionada a opção **Intermitente**).  
  
Após confirmar os parâmetros para cálculo, o sistema demostrará a mensagem **informativa** abaixo, para os casos de funcionários de contrato **Intermitente** (Documentação com maiores detalhes: [RH - Linha Protheus - PON - Mensagem de Eventos sobrepostos no Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403897652119-RH-Linha-Protheus-PON-Mensagem-de-Eventos-sobrepostos-no-C%C3%A1lculo-Mensal?source=search)):

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405310883607)

**Saiba Mais:**[Cálculo Mensal(PONM070)](https://tdn.totvs.com/pages/releaseview.action?pageId=635988738)  
[RH - Linha Protheus - PON - Como cadastrar os eventos para Folha de Pagamento ou Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013459532-MP-PON-Como-cadastrar-os-eventos-para-Folha-de-Pagamento-ou-Banco-de-Horas?source=search)  
[RH - Linha Protheus - PON - Quais os Pontos de Entrada disponíveis na rotina PONM070 - Cálculo Mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037898653)  
  
**Informações complementares**  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
