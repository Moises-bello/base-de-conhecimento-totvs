---
article_id: 4407577509399
category: Manutenção de Ativos (SIGAMNT)
content_hash: b0b932d247b91bed0b918d04731bedb6ff5604cadfac29e6d10dc21a84c36452
fetched_at: '2026-06-28T22:42:34.045626+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Geração de Ordem de Serviço Automática
  via Schedule
type: support-article
updated_at: '2021-12-15T13:05:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407577509399-Manufatura-Linha-Protheus-MNT-Gera%C3%A7%C3%A3o-de-Ordem-de-Servi%C3%A7o-Autom%C3%A1tica-via-Schedule
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Qual é o processo para criação de **O.S - Ordem de Serviço** automática via *Schedule*?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Segue abaixo o procedimento de utilização:

1. Acesse o **Configurador - SIGACFG**.
2. Acesse **Ambiente - Schedule - Schedule**, em **Schedule - Agent - Cadastro**. O Sistema apresenta a janela de agentes cadastrados.
3. Incluir um agente com **IP = localhost**, porta conforme a porta do **[TCP]** no arquivo **.ini**, empresa.
4. Confira os dados e confirme.
5. Acesse **Schedule - Agendamento - Cadastro**. O Sistema apresenta a janela de agendamentos cadastrados.
6. Incluir um agendamento no qual a rotina seja **MNTGOSAUTO()**, data atual, **Empresa/Filial** com todas utilizadas e **Módulo = 19**.
7. Confira os dados e confirme.
8. Acesse **Schedule - Agent - Monitor**. O Sistema apresenta a janela de monitor de agentes.
9. Selecionar **Iniciar Serviço** e em **Schedule - Agendamento - Monitor**.
10. O Sistema apresenta a janela de monitor de agendamentos.
11. Selecionar **Executar Agora**.
12. Confira os dados e confirme.
13. Verificar que é gerada **Ordem de Serviço** automática via *Schedule*.
