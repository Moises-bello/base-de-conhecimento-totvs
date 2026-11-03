---
article_id: 37142643414679
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ac4c547abf4b1bb3d6d3c006f35afa34f3c32b4c7c31b8c81f457776948a95c8
fetched_at: '2026-06-28T22:42:45.605604+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ponto de entrada para validações customizadas
  no apontamento
type: support-article
updated_at: '2025-12-19T18:57:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37142643414679-Manufatura-Linha-Protheus-SIGAPCP-Ponto-de-entrada-para-valida%C3%A7%C3%B5es-customizadas-no-apontamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37142628521111) Tempo aproximado para leitura: **00:02:04 min**  
  
**Dúvida**  
Qual o ponto de entrada que pode ser utilizado para implementar uma validação customizada no apontamento da **OP - Ordem de produção**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Para apontamentos via **MATA250 - Produção Simples**, pode-se fazer uso do ponto de entrada **MT250TOK  - Valida Valor Digitado ou Tela Toda,** para apontamentos via **MATA680 - Producao Mod I** ou **MATA681 - Produção Mod II** há o ponto de entrada **MT680VAL - Inclusão das Produções**[**.**](https://tdn.totvs.com/pages/viewpage.action?pageId=287056482)  
Já para apontamentos via **App Minha Produção** a validação customizada deve ser realizada também através do ponto de entrada **MT250TOK** para os casos em que o apontamento se dá através do formulário **1 - Produção Simples** ou através do ponto de entrada **MT680VAL** para apontamentos realizados através do formulário **3 - Prod PCP Mod 2.**  
  
**Saiba mais**  
A documentação sobre o ponto de entrada MT250TOK encontra-se disponível no [link](https://tdn.totvs.com/display/PROT/MT250TOK+-+Valida+valor+digitado+ou+tela+toda), e a documentação sobre o potno de entrada MT680VAL encontra-se disponível no [link](https://tdn.totvs.com/pages/viewpage.action?pageId=287056482)
