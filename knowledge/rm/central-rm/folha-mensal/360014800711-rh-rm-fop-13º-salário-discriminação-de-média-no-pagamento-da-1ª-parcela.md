---
article_id: 360014800711
category: Folha Mensal
content_hash: a43ccb427c9583c27268f3b0cab19be14f0bead40b1aaff01f70f7631d7d7ba4
fetched_at: '2026-06-28T22:47:00.277370+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: Discriminação de média no pagamento da 1ª parcela'
type: support-article
updated_at: '2024-06-14T14:56:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014800711-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-Discrimina%C3%A7%C3%A3o-de-m%C3%A9dia-no-pagamento-da-1%C2%AA-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24182681539095)Tempo aproximado para leitura: **00:01:31 min****Dúvida**Como realizar a discriminação das médias no pagamento da **1ª Parcela** do **13º Salário**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Por padrão, o sistema **não** discrimina as médias de **13º Salário** na **1ª parcela**. Esta discriminação somente acontece no pagamento da segunda parcela. Porém, o processo pode ser realizado através de fórmulas de cálculo. Para verificar a parametrização, segue instruções:  
  
1. Acesse: **Administração de Pessoal | Fórmulas** e cadastre a fórmula abaixo:  
  
Código: A0020  
Título: Média 13º na 1ª Parcela  
Texto: CALCMED(2) / 2  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009856512)**2. Acesse: **Administração de Pessoal | Eventos** e cadastre o evento:  
  
Código: A0020 ou conforme padrão da empresa.  
Título: Média 1ª Parcela do 13º Salário  
  
Parametrização:

* Provento;
* Valor;
* Código de Cálculo 9;
* Fórmula A0020, conforme passo 1;
* Incide FGTS 13º Salário;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009856812)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009872511)  
  
3. Acesse: **Administração de Pessoal | Sindicatos | 13º Salário** e desmarque o parâmetro **Paga média na 1ª Parcela.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412982716567)**  
  
4. Execute o pagamento da primeira parcela através do módulo **Folha Mensal | Cálculo 13º**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009874071)  
  
5. Acesse: **Folha Mensal | Lançamentos | Grupo de Eventos** e crie um grupo de eventos informando o evento A0020, conforme passo 2, para lançamento do evento das médias.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009875091)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009875131)  
  
6. Ainda no grupo de eventos, realize o lançamento para que o sistema lance o evento no envelope do funcionário.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009877791)
