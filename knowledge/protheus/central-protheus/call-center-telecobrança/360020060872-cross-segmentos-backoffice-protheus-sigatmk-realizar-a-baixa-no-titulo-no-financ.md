---
article_id: 360020060872
category: Call Center - Telecobrança
content_hash: a83ae94290c5e5fcd77e377a8d81fed026c1dd33df3053e4644c7b48bd0ce604
fetched_at: '2026-06-28T22:41:28.609974+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Realizar a baixa no titulo
  no Financeiro e atualizar o Status (Encerrado) no atendimento de TeleCobrança
type: support-article
updated_at: '2024-04-25T12:41:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020060872-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Realizar-a-baixa-no-titulo-no-Financeiro-e-atualizar-o-Status-Encerrado-no-atendimento-de-TeleCobran%C3%A7a
---

**Dúvida**

Realizar a baixa do titulo no financeiro e atualizar o Status (Encerrado) no atendimento de Tele Cobrança.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Essa rotina é responsável por selecionar todos os títulos a receber vencidos e não recebidos até a data vigente do seu processamento. Os títulos selecionados pelo processamento dessa rotina, posteriormente, serão motivo de cobrança por parte dos operadores através de um processo de atendimento. Os títulos selecionados (da tabela SE1) serão levados também à tabela de títulos do Telecobrança (SK1).

 O acesso a rotina **tmka290** (Quitação de Cobrança)é restrito aos supervisores dos operadores do Telecobrança. A seleção de títulos deve ocorrer de forma isolada, ou seja, a rotina não poderá ser executada enquanto os operadores estiverem acessando os processos de atendimento do Telecobrança. Portanto, seu processo deverá ocorrer de forma “stand alone”. Esse processo dever ser executado pelo menos uma vez ao dia para que a base de títulos em cobrança seja atualizada, obedecendo às últimas configurações.

 Durante o processamento dessa rotina, os títulos importados serão direcionados aos grupos de atendimento de acordo com as suas regras de seleção ora estabelecidas.

 Posteriormente, o controle de referência com o cadastro de títulos a receber será efetuado nas rotinas:**Pré-Atendimento (tmka280), Cobrança Receptiva (tmka350) e na Agenda do Operador (tmka380).**

 Os títulos a receber que forem selecionados para compor a base de dados do Telecobrança, e que foram:

1 - **Prorrogados no módulo Financeiro** serão excluídos da tabela dos títulos do Telecobrança (SK1), e se esse título estiver compondo um processo de atendimento no Telecobrança, o status dele (dentro do referido processo de atendimento do Telecobrança) será atualizado para “prorrogado”);

2 -**Pagos no módulo Financeiro** serão excluídos da tabela dos títulos do Telecobrança (SK1), e se esse título estiver compondo um processo de atendimento no Telecobrança, o status dele (dentro do referido processo de atendimento do Telecobrança) será atualizado para “pago”);

3 - **Baixados parcialmente no Financeiro** não serão excluídos da tabela dos títulos do Telecobrança (SK1), porém o seu saldo será atualizado, e se esse título estiver compondo um processo de atendimento no Telecobrança, o status dele (dentro do referido processo de atendimento do Telecobrança) será atualizado para “Baixado”).

Para validação de exemplo de uso, acesse a **FAQ no TDN: [TMK0041\_Processo\_de\_TeleCobrança\_x\_Contas\_a\_Receber](http://tdn.totvs.com/pages/viewpage.action?pageId=284472091)**
