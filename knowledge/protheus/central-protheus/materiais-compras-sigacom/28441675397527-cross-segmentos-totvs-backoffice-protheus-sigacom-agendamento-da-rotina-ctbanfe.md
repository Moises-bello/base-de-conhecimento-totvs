---
article_id: 28441675397527
category: Materiais - Compras (SIGACOM)
content_hash: 3d6ac8f908cec905d943f9cfc041bb2e486384090bc62b8245d295a384067417
fetched_at: '2026-06-28T22:41:13.085506+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Agendamento da rotina
  CTBANFE via Schedule
type: support-article
updated_at: '2024-12-11T13:38:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28441675397527-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Agendamento-da-rotina-CTBANFE-via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28441702653463) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como efetuar o agendamento da rotina CTABANFE - Rotina de Contabilização off-line das Notas Fiscais de Entrada via Schedule?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão 12

**Solução**

A rotina **CTBANFE** está preparada para ser executada via Schedule.  
Basta seguir os mesmos procedimentos para agendamento das demais rotinas do sistema, os quais estão descritos no seguinte link:  
[Schedule - Como agendar a execução de rotinas](Como%20agendar%20a%20execu%C3%A7%C3%A3o%20de%20rotinas)

Ao informar a rotina **CTBANFE** no campo "Rotina" em **Schedule** > Agendamentos > Cadastro, será aberta a tela de parâmetros da rotina (caso não seja aberta, clique no botão "Parâmetros").  
Os parâmetros são os mesmos que são apresentados ao acessar a rotina **CTBANFE** via menu no módulo de Compras em Miscelanea / Ajuste / Lc.ctb.doc.entrada.  
Adicionalmente, na configuração via schedule a tela de parâmetros apresenta a aba "Fórmulas". Nesta aba podem ser definidas fórmulas, que devem ser cadastradas, para que sejam retornados os valores dos parâmetros conforme desejado.  
Caso deseje utilizar fórmulas, deixe os parâmetros da aba "Parâmetro" em branco e utilize apenas as fórmulas.  
A rotina será executada conforme configurado no **Schedule** para efetuar a contabilização das notas fiscais de entrada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
