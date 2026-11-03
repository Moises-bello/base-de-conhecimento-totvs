---
article_id: 4409526965911
category: SIGAACD - Automação e Coleta de Dados
content_hash: 8fbda332d207ab5f92b715b9b327473e4cb5527669543bf9445bf613b76db94c
fetched_at: '2026-06-28T22:39:11.176839+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA030 - Parâmetro
  MV_VLDTINV e MV_INVAUT conceito e funcionalidade e comportamento campo BE_DTINV
type: support-article
updated_at: '2021-09-27T17:18:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409526965911-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA030-Par%C3%A2metro-MV-VLDTINV-e-MV-INVAUT-conceito-e-funcionalidade-e-comportamento-campo-BE-DTINV
---

**Dúvida**O campo BE\_DTINV fica preenchido mesmo após processar o inventário pelo ACAD030, qual o conceito e funcionalidade desse campo com o parâmetro MV\_VLDTINV?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - Todas as versões  
  
**Solução**O campo **BE\_DTINV** é preenchido com  a data do inventário no momento em que inicia uma contagem de inventário através da rotina MESTRE DE INVENTÁRIO (ACDA030).

O campo BE\_DTINV trabalha junto com o parâmetro  MV\_VLDTINV com isso deve seguir a definição do parâmetro.  
  
Definição  
Bloqueio o inventário por data.  
  
***Quando o parâmetro MV\_VLDTINV igual 0 - Não:***

O sistema bloqueia o produto ou endereço no momento que iniciar a contagem física e será desbloqueado automaticamente a ser feito o acerto de inventario e o ***parâmetro MV\_INVAUT deverá estar obrigatoriamente com 1-sim***  
  
***Quando o parâmetro MV\_VLDTINV igual 1 - SIM:***

O sistema bloqueia o produto ou endereço no momento que iniciar a contagem física o mesmo será desbloqueado somente com a virada do dia. Obs.: O campo BE\_DTINV mantém a data que foi processado o inventário e impede que sejam efetuadas movimentações nesse endereço na data indicada. 

**Saiba mais**:

*[Principais parâmetros SIGAACD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235302467-MP-SIGAACD-Par%C3%A2metros-SX6-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-)*

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados (ACD)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
