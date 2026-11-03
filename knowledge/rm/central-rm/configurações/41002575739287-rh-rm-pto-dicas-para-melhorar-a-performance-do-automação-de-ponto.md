---
article_id: 41002575739287
category: Configurações
content_hash: eca4fe787dc93a13e99f1374d6255f13d2fb478ad9340617cb2e7eac32431d00
fetched_at: '2026-06-28T22:46:29.823627+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO- Dicas para melhorar a performance do Automação de Ponto
type: support-article
updated_at: '2026-06-15T18:16:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41002575739287-RH-RM-PTO-Dicas-para-melhorar-a-performance-do-Automa%C3%A7%C3%A3o-de-Ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41002575725719) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Caso no TOTVS Automação de Ponto o usuário tenha problemas de lentidão ao efetuar rotina de recálculo e/ou gerar o relatório do espelho do cartão, como identificar a **causa da baixa performance** e quais são as melhores práticas para **melhorar a performance**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2510  
  
**Causa**  
A lentidão no RM TOTVS Automação de Ponto pode ser causada por diversos fatores, incluindo configurações do ambiente, um grande número de acessos simultâneos,  locks em tabelas do banco, desempenho da infraestrutura atual, fórmulas de evento no movimento e fórmulas de evento no banco de horas, entre outros fatores.  
  
**Solução**  
Criamos a **documentação** abaixo, que detalha as principais **configurações** recomendadas para **melhorar a performance** de recálculo do ponto. Recomendamos que você leia **atentamente** toda a documentação preparada. Se, após seguir essas orientações, o problema persistir, **continue consultando o restante deste KCS** para mais informações e soluções adicionais.

[RH - RM - PTO - Fracionamento de JOBS ao recalcular](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027793151-RH-RM-PTO-Fracionamento-de-JOBS-ao-recalcular)

[Segurança de Jobs Fracionáveis](https://tdn.totvs.com/pages/releaseview.action?pageId=547231277)

No link de Segurança de Jobs Fracionáveis é possível fracionar o processo de geração do relatório do espelho do cartão de ponto. Basta seguir a documentação e adicionar a classe de job **PtoProcRelatEspelhoCartao** e seguir as orientações de acordo com seu cenário.

Se, mesmo seguindo **todas orientações acima**, continuar enfrentando problemas de desempenho na usabilidade dos processos, **verifique** os itens listados abaixo:

1. Se a lentidão estiver no processo de recálculo, verifique se desmarcar as opções de *'**Calcula eventos por fórmula no movimento'*** e *'**Calcula eventos por fórmula no banco de horas'***o processo será executado de forma mais rápida. Se o processo executar de forma rápida, fica confirmado que as fórmulas customizadas precisam ser otimizadas.  
     
   ![recalculo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41002589262359)  
      
   Se precisar de acompanhamento para análise da performance e otimização das fórmulas customizadas, temos nosso time de consultoria técnica que poderá apoiá-lo na análise. Se optar por este caminho basta retornar no ticket manifestando este interesse que direcionamos o atendimento para que o time lhe informe os procedimentos e valores.
2. Caso a lentidão ocorra em processos específicos, ou seja, somente no módulo de ponto, avalie se no gerenciamento de jobs, há jobs de recálculo, lançamento de batidas pelo horário planejado, ou mesmo importação de batidas em concorrência. Jobs de diferentes processos do módulo do ponto executando simultaneamente podem causar locks no banco, ou mesmo lentidão nos processos.  
     
   Agendamentos de jobs executando simultaneamente, também podem causar lentidão.  
     
   Para identificar jobs agendados, segue documentação:  
   [Framework - Linha RM - Frame - Identificar job agendado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014009212-Framework-Linha-RM-Frame-Identificar-job-agendado)  
     
   Se identificar vários jobs agendados, sem necessidade, podendo causar lentidão, segue documentação para desabilitá-los:  
   [Framework - Linha RM - Frame - Como desabilitar job agendado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003038712-Framework-Linha-RM-Frame-Como-desabilitar-job-agendado)
3. Se a lentidão estiver de forma generalizada, ou seja, em qualquer processo, qualquer módulo, sugerimos verificar a documentação abaixo:  
   [Framework - Framework RM - BD - Orientações Gerais para Otimização de Performance](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027943052-Framework-Framework-RM-BD-Orienta%C3%A7%C3%B5es-Gerais-para-Otimiza%C3%A7%C3%A3o-de-Performance)

**Importante**  
Se houver necessidade de investigação mais aprofundada em seu ambiente, temos nosso serviço TIS. O Infraestrutura de Sistemas é o serviço especializado de análise, sustentação e evolução da infraestrutura que suporta os sistemas de gestão da TOTVS.  
Para maiores detalhes, segue link [**TIS**](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-servico-infraestrutura-de-sistemas/)

**Saiba mais**  
Para avaliar locks no banco, segue documentação para base SQL:  
[Framework - Framework RM - BD - Como verificar Deadlock no SQL Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003068212-Framework-Framework-RM-BD-Como-verificar-Deadlock-no-SQL-Server)  
  
Como apoio, para auxiliar no monitoramento do ambiente, segue documentação sobre o Sentinela:  
[Framework - Framework RM - BD - Sentinela RM Ferramenta de Monitoramento de Ambientes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007212312--Framework-Framework-RM-BD-Sentinela-RM-Ferramenta-de-Monitoramento-de-Ambientes)  
  
Confira também, como melhorar o desempenho de outros Produtos do RH:  
[RH - RM - FOP- Dicas para melhorar a performance da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41083949075863-RH-RM-FOP-Dicas-para-melhorar-a-performance-da-Folha-de-Pagamento)  
[RH - RM - Meu RH- Dicas para melhorar a performance do Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441139391767-RH-RM-Meu-RH-Dicas-para-melhorar-a-performance-do-Meu-RH)
