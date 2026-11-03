---
article_id: 360057943453
category: RH - Definições de Cálculo
content_hash: a091d08c49a897cddf3b46b915f89a1a012bc50b01a69ca6d720c1c9826bafee
fetched_at: '2026-06-28T22:43:22.579944+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: 'RH - Linha Protheus - GPE - O que analisar quando ocorre a mensagem: Já existe
  um período selecionado'
type: support-article
updated_at: '2021-12-27T12:42:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057943453-RH-Linha-Protheus-GPE-O-que-analisar-quando-ocorre-a-mensagem-J%C3%A1-existe-um-per%C3%ADodo-selecionado
---

**Ocorrência**O que analisar no módulo **Gestão de Pessoal**, na rotina de **Períodos** quando ocorre a mensagem: Já existe um período selecionado. Favor efetuar o fechamento antes de selecionar outro período.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097718353/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre quando geralmente o roteiro de cálculo da competência atual ainda consta em aberto, e por alguma razão existe a necessidade de realizar um cálculo para a próxima competência (benefícios). No entanto, é importante validar que o fechamento deve ocorrer de forma automática pela rotina de **Fechamento Mensal**, mas quando necessário executar um cálculo de benefício já para a próxima competência, existe uma prática em alterar a ativação dos períodos, ainda que não recomendado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097718493/mceclip1.png)

**Solução**Para solucionar essa ocorrência, realize o fechamento da competência atual de forma automática **(Miscelanea - Fechamento - Por Roteiros)**, para que o roteiro de Benefício que precisa validar possa ser liberado como aberto.  
  
**OBS:** Orientamos que o processo de fechamento dos roteiros/períodos, seja sempre realizado de forma automática, evitando possíveis inconsistências de cálculos, integrações ou ainda cadastros.
