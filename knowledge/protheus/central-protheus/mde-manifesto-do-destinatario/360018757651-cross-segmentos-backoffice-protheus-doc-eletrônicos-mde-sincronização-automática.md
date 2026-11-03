---
article_id: 360018757651
category: MDe - Manifesto do Destinatario
content_hash: fc36a3978365523b324033321ce178ae8879f3c4f31f322d0564aa14bb1ffda0
fetched_at: '2026-06-28T22:40:09.280214+00:00'
product: protheus
section_id: 1500001549162
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - MDE - Sincronização
  Automática da MDe via Schedule
type: support-article
updated_at: '2025-06-10T18:42:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018757651-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-MDE-Sincroniza%C3%A7%C3%A3o-Autom%C3%A1tica-da-MDe-via-Schedule
---

|  |
| --- |
| 1. Acesse o Configurador  2. Através do Configurador, acesse a rotina de **Schedule**  CaminhoSchedule.gif   3. Em “**Schedule**”, clique em “Iniciar todos os serviços” (caso os serviços ainda não tenham sido iniciados) e verifique se o ‘**STATUS**’ do seu **Schedule** ficará como ‘**Iniciado**’  4. No menu “**Agent**”, cadastre um novo ***Agent*** (caso não exista nenhum cadastrado)  agent.gif  5. Após cadastrar o ***Agent***, clique no **botão** “**Iniciar todos os serviços**” e verifique se o ‘**Status**’ do seu ***Agent*** ficará como ‘**Iniciado**’  iniciado.gif  6. Em seguida, será necessário efetuar o cadastro do agendamento para a rotina **JOBMANI**. No menu, clique em *Agendamentos* > *Cadastros*    *cadastro.gif*    7. Ainda no Cadastro do Agendamento, não se esqueça de configurar as recorrências para a execução da rotina **JOBMANI** – Manifesto do Destinatário  mceclip0.png    8. Confirme o cadastro e verifique se o semáforo de sua rotina **JOBMANI** está como verde no menu *Agendamentos*    9. Finalizada a etapa de **Cadastro** do **SCHEDULE** (Agent e Agendamento), ao reinicializar o serviço do Protheus a mensagem **“SINCRONIZACAO MD-E VIA SCHEDULE => Entidade:”** deverá ser exibida no console do servidor Protheus |
|  |
