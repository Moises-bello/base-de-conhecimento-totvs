---
article_id: 360022588751
category: RH - Soluções para error.log
content_hash: 6d66a55ab91df61dd928c8ab48d4511848e6e2e634ceab58297daee4637a0f13
fetched_at: '2026-06-28T22:44:08.798285+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo da Folha gera o Error Log array out of
  bounds ( 0 of 0 ) on FCARMVTO(GPEXINI.PRX)
type: support-article
updated_at: '2025-07-30T16:16:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022588751-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-Folha-gera-o-Error-Log-array-out-of-bounds-0-of-0-on-FCARMVTO-GPEXINI-PRX
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33823896929303)**** Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**  
Ao realizar o cálculo da Folha para Funcionário em situação de Férias, caso exista uma verba na RGB proveniente das Férias, mas que não exista no Cadastro de Verbas ou que esteja Bloqueada para Lançamentos, é gerado o *Error Log* ***array out of bounds ( 0 of 0 ) on* FCARMVTO(GPEXINI.PRX).**  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**   
Esse incidente ocorre quando existe uma **verba de Férias** na tabela **RGB,** mas ela **não existe** no Cadastro de Verbas **ou** **está desabilitada.**  
  
**Solução**  
Para solucionar essa ocorrência, é necessário acessar **Atualizações > Definições de Cálculo > Verbas** e seguir os passos abaixo:  
**>** Cadastrar a verba existente na RGB   
**>** Habilitar a verba através da aba Bloqueio de Lançamentos, marcando todas as opções com SIM.  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como cadastrar Verbas no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783-RH-Linha-Protheus-GPE-Como-cadastrar-verbas-no-Protheus)
