---
article_id: 6217068180631
category: RH - Provisão
content_hash: 4956c0db44103e5451f638f1240914aadea1392d928be94c13604b50f7405da0
fetched_at: '2026-06-28T22:43:55.676314+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de provisão com Tipo de ausência Perda
  após 180 dias e Congela após 6 meses (por período)
type: support-article
updated_at: '2025-10-24T12:36:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6217068180631-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-provis%C3%A3o-com-Tipo-de-aus%C3%AAncia-Perda-ap%C3%B3s-180-dias-e-Congela-ap%C3%B3s-6-meses-por-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998250640791) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Cálculo de provisão com Tipo de ausência Perda após 180 dias e Congela após 6 meses.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Neste documento vamos verificar o comportamento do sistema no cálculo de provisão conforme configuração do tipo de ausência.

Funcionário ativo na competência 12/2021, possui 30 dias de férias vencidas e 2,5 dias de férias proporcionais:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6218113619223)

Relatório da competência 12/2021:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6218042726295)

Na etapa seguinte vamos configurar o cálculo da provisão em Atualizações/Definições de Cálculo/Tipos de Ausências:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6217944817303)

Na competência 01/2022 vamos incluir um afastamento para o funcionário e analisar mês a mês até o seu retorno como o cálculo da provisão se comportará:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6217872660503)

O cálculo da provisão de férias ocorrerá conforme configurado no tipo de ausência, calculando normalmente até 6 meses (Congelar após 6 meses).

No print abaixo, vemos os 5 primeiros meses  calculados de acordo com cada avo adquirido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6220539826839)

Dando sequência nos cálculo em competências posteriores, vemos que ao alcançar o 6º mês de cálculo, a provisão congela o cálculo e só retorna a provisionar valores devido ao retorno do colaborador na competência 10/2022:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6221261892375)

Retorno do funcionário:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6221388506775)

Vamos verificar também como ficou gravado o controle de dias de direito (tabela SRF) após o retorno do funcionário:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6222604845207)

**Período aquisitivo:**  
01/12/2020 a 30/11/2021 = Ativo - uma vez que o período foi adquirido e não quitado.

01/12/2021 a 30/11/2021 = Prescrito - uma vez que o colaborador esteve afastado por mais de 180 dias.

11/10/2022 a 10/10/2021 = Ativo - de acordo com a data de retorno (10/10/2022), o sistema criará um novo período e a partir da competência provisionar os avos a cada mês.

Relatório de provisão na competência de retorno do colaborador (10/2022):   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6268752884759)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
