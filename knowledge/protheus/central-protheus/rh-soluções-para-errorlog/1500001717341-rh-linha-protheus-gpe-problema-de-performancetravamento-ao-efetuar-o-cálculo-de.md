---
article_id: 1500001717341
category: RH - Soluções para error.log
content_hash: d3253006aef78e848394ea896de02c847d6bd5fb7c2aa0c2a2239275ab396ff8
fetched_at: '2026-06-28T22:44:09.125818+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Problema de performance/travamento ao efetuar o
  cálculo de férias
type: support-article
updated_at: '2022-11-01T13:42:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001717341-RH-Linha-Protheus-GPE-Problema-de-performance-travamento-ao-efetuar-o-c%C3%A1lculo-de-f%C3%A9rias
---

**Ocorrência**Ao tentar efetuar o **Cálculo de Férias**, através da rotina **GPEM030** gera **problema de performance/travamento (demora no cálculo)** no ambiente  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões

**Causa**O problema ocorre devido a rotina de Troca de Turnos possuir cadastrado apenas uma linha bastante antiga para o funcionário, onde o sistema acaba criando calendários anteriores até a data da última linha da Troca de Turno, gerando então a lentidão no cálculo  
  
**Solução**Para solucionar o problema verifique os pontos abaixo:  
**1.** Este funcionário possui cadastrado alguma Troca de Turno na rotina em Atualizações/Ponto Eletrônico/Trocas de Turno conforme demonstrado abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/YVCkJOhJmlDXOt5uBw3Cwka7a/?name=inline869625358.png)​  
  
**2.** Se o módulo de Ponto Eletrônico **não é utilizado**, a mesma rotina não precisa compreender com nenhum registro para o funcionário, devendo assim, deletar a informação  
  
**3.** Se o módulo de Ponto Eletrônico **é utilizado**, certifique-se de que o período do Ponto Eletrônico bata com o período da Folha e nesta rotina, conste linhas mês à mês de cada fechamento do Ponto.  
  
Observação: Outra possibilidade pode ser o Mnemônico P\_LMEMCALC (Memoria de calculo), quando o mesmo está ativado ele grava todo o processo efetuado em um arquivo fazendo com que o sistema apresente lentidão.   
  
**Saiba mais:**Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
