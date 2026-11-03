---
article_id: 1500000127341
category: RH - Contabilização
content_hash: 981955dd10d8d1ff0b7d65e28a55e4aeab6c3188479e7e735f965ba5e4ee2e63
fetched_at: '2026-06-28T22:43:46.059181+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não realiza contabilização do roteiro VEX
type: support-article
updated_at: '2025-07-24T14:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000127341-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-realiza-contabiliza%C3%A7%C3%A3o-do-roteiro-VEX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33687488251671)** Tempo aproximado para leitura: **00:01:30 min**

**Ocorrência**  
Sistema não realiza contabilização do roteiro VEX.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**  
Sistema não esta parametrizado para contabilização do Roteiro VEX.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
**1 -** É necessário possuir o sistema **devidamente atualizado**;  
**2 -** Para efetuar a contabilização dos valores extras você deve verificar se o **roteiro VEX** está parametrizado para contabilizar acessando a rotina **Roteiros de Cálculo - GPEA160**Acesse: **Atualizações** -> **Definições de Cálculo** -> **Roteiros de Cálculo**;  
**3 -** Altere o campo **Contabiliza? (RY\_CONTAB)** para "**SIM**";  
**4 -** Após realizar a parametrização do roteiro, acesse a rotina **Contabilização - GPEM110**,   
Acesse: **Miscelânea** -> **Fechamentos** -> **Contabilização**: preencha as perguntas para contabilização;  
**5 -** O Sistema irá processar os valores extras com o tipo (RZ\_TIPO) igual a FL.  
  
Para esta parametrização, o roteiro VEX não pode estar parametrizado para integrar no Roteiro FOL, portanto o campo integra (RY\_INTEGRA) deve estar com conteúdo "NÃO" na rotina Roteiros de Cálculo - GPEA160.

**Saiba Mais:**  
[Página Centralizadora da Contabilização Protheus RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
