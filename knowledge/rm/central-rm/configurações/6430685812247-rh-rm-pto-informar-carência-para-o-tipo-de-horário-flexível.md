---
article_id: 6430685812247
category: Configurações
content_hash: d2eebac2a286763f2cba83b4aa77532aa1c3154f8188a75b654ce50a84954fc4
fetched_at: '2026-06-28T22:46:29.883400+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Informar carência para o tipo de Horário flexível
type: support-article
updated_at: '2025-09-12T18:08:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6430685812247-RH-RM-PTO-Informar-car%C3%AAncia-para-o-tipo-de-Hor%C3%A1rio-flex%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980467410839) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Onde informar carência (tolerância) para o tipo de Horário flexível?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**

No novo cálculo de ponto, o sistema possibilita a aplicação de tolerância por batida, seja em relação ao Sindicato ou ao horário. No entanto, essa abordagem pode não ser a mais adequada, pois, para que a tolerância seja efetivamente aplicada, o funcionário deve registrar suas batidas próximas ao horário previsto, o que não é comum para trabalhadores com horários flexíveis. Assim, o ideal seria estabelecer a tolerância diretamente na jornada.

Para realizar a parametrização de atrasos, acesse a visão do espelho de ponto do funcionário e selecione a opção **Processos | Parametrizar Funcionário**. Em seguida, avance até a etapa de **atrasos** e localize a seção **Carência após a compensação**. No campo **Carência de atraso**, insira o valor que será tolerado para a jornada de trabalho.

Para indicar o limite das horas extras , avance até a etapa de Extras, e localize a seção **Carência após a compensação**. No campo **Carência de extra**, preencha com o valor que será tolerado em relação à jornada de trabalho:

Após a alteração, avance até concluir e realize o recálculo do espelho de ponto e valide as ocorrências geradas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34900741272087)

**Importante**Caso o atraso ou extra ultrapasse a **carência** será considerado integralmente.

**Saiba mais:**Para realizar a alteração global dos parâmetros dos funcionários, acesse o link :

[RH - RM - PTO - Alteração global de parâmetros dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945111-TOTVS-RH-Linha-RM-PTO-Como-fazer-a-altera%C3%A7%C3%A3o-global-de-par%C3%A2metros-dos-funcion%C3%A1rios)

[Atrasos](https://tdn.totvs.com/display/public/LRM/Atrasos)

[Extras](https://tdn.totvs.com/display/public/LRM/Extras)
