---
article_id: 1500009004322
category: RH - Contabilização
content_hash: 3dcd096f897133b7927669bf8b004d9aaf8ad035bff90f3848209b9bf38b0dee
fetched_at: '2026-06-28T22:43:45.821639+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como contabilizar as verbas do cálculo de Participação
  nos Lucros e Resultados - PLR
type: support-article
updated_at: '2025-07-30T13:45:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009004322-RH-Linha-Protheus-GPE-Como-contabilizar-as-verbas-do-c%C3%A1lculo-de-Participa%C3%A7%C3%A3o-nos-Lucros-e-Resultados-PLR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33819151209495) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como contabilizar as verbas do cálculo de Participação nos Lucros e Resultados - PLR?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  GPE Gestão de Pessoal – Todas as Versões  
  
**Solução**  
Para contabilizar as verbas do cálculo de **Participação nos Lucros e Resultados - PLR**, realize os seguintes passos:  
  
1. Na rotina **Roteiro de Cálculo - GPEA160** , altere o conteúdo do campo **Contabiliza** para **Sim**Acesse **Atualizações** -> **Definições de cálculo** -> **Roteiros de Cálculo**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013917741)  
  
2. Será necessário atrelar um **Lançamento Padrão - CTBA080** as verbas que fazem parte do Cálculo do PLR, através do campo **Lcto. Padrão** localizado na aba **Contabilização** do cadastro de **Verbas - GPEA040**, efetue o relacionamento de acordo com seu plano de contas.  
Acesse **Atualizações** -> **Definições de cálculo** -> **Verbas**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013917921)  
  
Dessa forma os valores serão contabilizados através da rotina **Contabilização GPEM110**

**IMPORTANTE:**Embora os valores estejam em roteiros separados FOL e PLR, a contabilização apresentará os lançamentos contábeis no mesmo lote.   
  
PLR:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130688522775)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130725695895)

FOLHA:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130752395287)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130715452567)  
  
Contabilização através da rotina GPEM110 - Miscelânea / Fechamentos / Contabilização. No exemplo abaixo , usaremos a contabilização por Centro de custos:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130822598551)

Contabilização dos 2 roteiros (FOL e PLR) no mesmo lote contábil)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5130794404759)

No Suporte não orientamos criação de fórmulas para os lançamentos padrões ou customizações, e caso necessite de auxílio para isso, solicite a presença de um analista TOTVS em sua empresa para que lhe auxiliem a configurar as fórmulas ou avaliar se há necessidade de customização ou não.  
  
**Saiba Mais:**  
Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:  
[MP - GPE - Contabilização da provisão de PLR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058949193-MP-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-de-PLR)
