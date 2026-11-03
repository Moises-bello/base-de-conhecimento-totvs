---
article_id: 360022225372
category: Gestão de Transportes (TMS)
content_hash: e7d33053e20da532c92a8267212e7a36aec47eea3c7671daf2c623b39657b683
fetched_at: '2026-06-28T22:45:27.398277+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como cadastrar Tipo de Faturamento
type: support-article
updated_at: '2023-07-14T11:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022225372-Log%C3%ADstica-Linha-Protheus-TMS-Como-cadastrar-Tipo-de-Faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16022740360599)** Tempo aproximado para leitura:**00:01:00 min****Dúvida**Como cadastrar **Tipo de Faturamento**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Na rotina **Tipo de Faturamento** são informados os dados que serão utilizados na geração das faturas automáticas conforme perfil do cliente, permitindo configurar o tipo de faturamento, o intervalo de dias que serão considerados para a seleção dos títulos dos clientes - faixas de dias cadastrais -, a data para geração da fatura, entre outros.  
  
**Exemplos:****Faturamento Semanal**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019323591)**

Neste exemplo, as faturas serão geradas semanalmente, sempre às segundas-feiras, selecionando os títulos com emissão de segunda a sexta-feira da semana anterior.  
  
**Faturamento Decendial**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019323631)**

Neste exemplo, as faturas serão geradas por decêndio:

* No item 1, as faturas serão geradas no dia 11 do mês corrente, selecionado os títulos com emissão entre o dia 01 a 10 do mesmo mês.
* No item 2, as faturas serão geradas no dia 21 do mês corrente, selecionado os títulos com emissão entre o dia 11 a 20 do mesmo mês.
* No item 3, as faturas serão geradas no dia 1 do mês corrente, selecionado os títulos com emissão entre o dia 21 a 31 do mesmo anterior.

**Faturamento Quinzenal**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019454552)**

Neste exemplo, as faturas serão geradas por quinzena:

* No item 1, as faturas serão geradas no dia 11 do mês corrente, selecionado os títulos com emissão entre o dia 01 a 10 do mesmo mês.
* No item 2, as faturas serão geradas no dia 21 do mês corrente, selecionado os títulos com emissão entre o dia 01 a 10 do mesmo mês.

Se o campo **Tipo do Dia= Mês**, as faturas serão geradas mensalmente e as faixas de dias cadastrais devem somar 31 dias. Caso contrário, se esse campo for configurado como **Semana**, as faturas serão geradas semanalmente e as faixas de dias cadastrais devem somar 7 dias.  
  
**Procedimentos**Para informar o tipo de faturamento:

1. Em **Tipo de Faturamento**, selecione a opção **Incluir:**
2. Será apresenta a janela **Tipos de Faturamento - Incluir**, dividida em áreas:

   **Cabeçalho**  
   Nesta área, informe o tipo do faturamento, a descrição e tipo do dia (1-Mês ou 2-Semana).  
   **Itens**  
   Nesta área, informe o período a ser considerado e o dia para a geração da fatura.
3. Para inserir um novo item, pressione **seta para baixo**. Será apresentada uma nova linha para a digitação.
4. Confira os dados e **confirme**.
