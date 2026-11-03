---
article_id: 360017554792
category: RH - Férias
content_hash: 93e628cd4ac972dca743d886394a74e15d7b92984f02ef5bab812d514b7863bd
fetched_at: '2026-06-28T22:43:57.944386+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular férias, Sistema traz período aquisitivo
  ou dias de férias incorreto
type: support-article
updated_at: '2025-08-28T18:32:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017554792-RH-Linha-Protheus-GPE-Ao-calcular-f%C3%A9rias-Sistema-traz-per%C3%ADodo-aquisitivo-ou-dias-de-f%C3%A9rias-incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31438274992535) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**No módulo **Gestão de Pessoal**, ao tentar realizar **Cálculo de Férias,** Sistema traz período aquisitivo ou dias de férias incorreto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esse incidente pode ocorrer quando a **Situação** de um período aquisitivo já **quitado** na rotina de Controle de Dias de Direito consta como **Ativo.**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse rotina de **Controle Dias de Direito** através do Menu **Atualizações > Funcionários > Controle Dias de Direito**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10765642563607)  
  
2. Selecione funcionário em questão e clique em **Manutenção**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10780646923287)

3. Selecione campo **Situação** e ajuste conteúdo para 3-**Pago**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10780740198807)​

**Importante!**  
Esta alteração **só poderá ser realizada quando o período de fato já tenha sido calculado**, **pago e com histórico na tabela de Acumulados Anuais** (SRD).  
  
A alteração da **Situação** do período aquisitivo é feita somente após o **Fechamento** **da Competência (GPEM120)** em que as férias foram calculadas e somente quando os 30 dias de direito já tenham sido calculados.  
  
**Exemplo:**  
Funcionário possui **30 dias de férias vencidas em aberto** e serão **calculados somente 20 dias,** neste cenário a **Situação** do período aquisitivo constará como **Ativo**, pois haverá ainda 10 dias de direito a serem calculados. Somente **após o calculo dos 10 dias** em aberto **e fechamento** da competência de cálculo destes, a **Situação** será alterada para **Pago.**

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como calcular férias na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015658231-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-na-vers%C3%A3o-12?source=search)  
[RH - Linha Protheus - GPE - Como calcular férias programadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004091821-RH-Linha-Protheus-GPE-Como-calcular-f%C3%A9rias-programadas?source=search)  
[RH - Linha Protheus - GPE - Recalculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420404618903-RH-Linha-Protheus-GPE-Recalculo-de-F%C3%A9rias-?source=search)
