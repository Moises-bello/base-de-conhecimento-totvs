---
article_id: 360033628574
category: RH - Rescisão
content_hash: 2b9b1cabb55d88cfe5576d856ca95094f1fe0474ba85bee3df88465bf347beab
fetched_at: '2026-06-28T22:43:48.392173+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  No cálculo da rescisão, o sistema verifica a quantidade
  de faltas da rotina de Controle de Dias de Direito
type: support-article
updated_at: '2025-04-16T18:56:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033628574-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-da-rescis%C3%A3o-o-sistema-verifica-a-quantidade-de-faltas-da-rotina-de-Controle-de-Dias-de-Direito
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26561123397271)***Tempo aproximado para leitura: **00:01:00 min****Dúvida**No cálculo da rescisão, o sistema verifica a quantidade de faltas da rotina de Controle de Dias de Direito?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Se somente informado a quantidade de dias de faltas na rotina de Controle de Dias de Direito, o sistema não considerará a quantidade de dias informadas nesta rotina para o abatimento de avos de férias, uma vez que verifica a verba (geralmente o id 0054 com S para Média Férias) que está nos acumulados do período aquisitivo.  
  
Para que seja considerado a quantidade de faltas para abatimento dos avos de período aquisitivo na rescisão, execute o lançamento da verba de faltas na rotina de Lançamentos por Funcionário ou na própria rescisão por meio da opção Outras Ações **(Lembramos que esta ação fará com que a verba de faltas lançada seja  descontada na rescisão, além da perda de avos)**.

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
