---
article_id: 360036560514
category: RH - Rescisão
content_hash: a589b14ba881421f242806693be5bbe9374d7571f44855575376809374737d51
fetched_at: '2026-06-28T22:43:48.593358+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular Múltiplas  Rescisões com vários processos
type: support-article
updated_at: '2025-09-10T17:17:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036560514-RH-Linha-Protheus-GPE-Como-calcular-M%C3%BAltiplas-Rescis%C3%B5es-com-v%C3%A1rios-processos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34843652138391) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como calcular Múltiplas  Rescisões com vários processos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Rotina de Cálculo Múltiplas rescisões: Para possibilitar o cálculo de múltiplas rescisões de processos diferentes, hoje a rotina **GPEM040B** permite o cálculo apenas de um processo por execução.

A melhoria está disponível na 12.1.25.

A rotina de múltiplas rescisões permitirá o cálculo de mais de um processo simultaneamente. Para isso, antes de chamar o cálculo efetivamente, a rotina irá analisar se existe mais de um processo selecionado, e caso exista, irá exibir a tela para preenchimento dos parâmetros de cálculo para cada um dos processos, antes da execução do cálculo, de modo a não existir interrupções no meio do processo.

**Entrar na rotina de Múltiplas Rescisões**

**Miscelânea > Calculo > Múltiplas Rescisões**,Selecionar as matriculas com processos diferentes, solicitar o calculo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048767474)

Ira gerar uma tela informando que mais de um processo foi selecionado, confirmar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049669373)

Em seguida irá abrir a tela para preenchimento do cabeçalho da rescisão, datas, tipo da rescisão e o primeiro Processo. Ao salvar ira aparecer o segundo processo onde devera preencher e salvar para que o sistema calcule as duas rescisões selecionadas.

**Primeiro Processo 00001**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048768054)

**Segundo Processo 00005**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048768274)**

Para visualização do cálculo dessas rescisões será necessário entrar na rotina de cálculo de rescisão GPEM040.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049670513)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049670633)  
  
**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
