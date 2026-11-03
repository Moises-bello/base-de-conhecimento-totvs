---
article_id: 360044238394
category: RH - Rescisão
content_hash: 5e3ee37d62b059cf64ce8d519480b8dd29dddbe276495d2943e660cd74d17233
fetched_at: '2026-06-28T22:43:49.586644+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar o cálculo de múltiplas rescisões
  de processos diferentes
type: support-article
updated_at: '2025-05-07T21:16:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044238394-RH-Linha-Protheus-GPE-Como-realizar-o-c%C3%A1lculo-de-m%C3%BAltiplas-rescis%C3%B5es-de-processos-diferentes
---

**Dúvida**Como realizar o cálculo de múltiplas rescisões de processos diferentes?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.23.  
  
**Solução**A rotina de **múltiplas rescisões** permite o cálculo rescisões de mais de um funcionários com processos diferentes simultaneamente. Para isso, antes de chamar o cálculo efetivamente, a rotina irá analisar se existe mais de um processo selecionado, e caso exista, irá exibir a tela para preenchimento dos parâmetros de cálculo para cada um dos processos, antes da execução do cálculo, de modo a não existir interrupções no meio do processo.

A rotina **GPEM040B** já esta disponível, mas caso ainda não esteja disponível no menu do SIGAGPE, deverá incluí-la como segue:

No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu do ***SIGAGPE***, conforme instruções a seguir:

|  |  |
| --- | --- |
| **Menu** | Miscelânea |
| **Submenu** | Cálculos |
| **Nome da Rotina** | Múltiplas Rescisões |
| **Programa** | GPEM040B |
| **Módulo** | 07 - SIGAGPE |
| **Tipo** | 1 - Função Protheus |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428902190999)

Após incluir no menu, ao entrar na rotina, será possível selecionar diversos funcionários para o cálculo da rescisão na tela abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428885431447)  
  
Ao clicar em Calcular, caso os funcionários selecionados estejam cadastrados em processos diferentes, sistema mostrará a tela abaixo, clique em SIM para prosseguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428902206615)  
  
Preencha a tela abaixo de acordo coma  sua necessidade de cálculo, essa tela será apresentada para cada processo diferente entre os funcionários selecionados:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428902216087)

Após preenchimento, clique em Salvar, sistema calculará as rescisões dos funcionários selecionados.
