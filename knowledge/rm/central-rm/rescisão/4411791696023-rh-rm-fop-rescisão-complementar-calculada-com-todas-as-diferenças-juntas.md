---
article_id: 4411791696023
category: Rescisão
content_hash: 5fb73e07043ef4b5677e3ec824eeecfac8c4bcf9b33ced804b8826d68e15a2d5
fetched_at: '2026-06-28T22:46:54.484649+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Rescisão complementar calculada com todas as diferenças juntas
type: support-article
updated_at: '2025-01-21T18:32:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411791696023-RH-RM-FOP-Rescis%C3%A3o-complementar-calculada-com-todas-as-diferen%C3%A7as-juntas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como calcular a Rescisão Complementar com outras Diferenças no mesmo envelope?**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Quando a alteração salarial é referente a um mês anterior, ou a meses anteriores à rescisão, o usuário deverá calcular além da rescisão complementar, as diferenças de salário, férias e/ou 13º salário que existirem nesse intervalo entre a data do aumento retroativo e a data de desligamento do funcionário.  
  
Ao marcar o parâmetro **Calcular todas as diferenças juntas** haverá mais um passo para informar quais diferenças serão calculadas junto com a rescisão complementar, de acordo com a seleção do usuário.  
  
Para utilizar esse parâmetro, acesse a rotina: **Rescisão | Complementar**. Na rotina de **Rescisão Complementar** encontrará diversos campos parametrizáveis, ajuste-os conforme a sua necessidade e marque a flag **Calcular todas as diferenças juntas**, como demonstrado na imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4705142586007/mceclip0.png)  
  
Na tela **Parâmetros de Diferenças** deve-se selecionar o mês em que as diferenças deverão iniciar o cálculo e logo depois deverá ser selecionado o cálculo que será realizado.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4705178056599/mceclip1.png)  
  
Sobre os cálculos disponíveis para seleção:

* Diferença Salarial
* Diferença de Férias: Se a 1ª parcela do 13º salário foi paga junto com as férias, será necessário informar um evento com **código de cálculo 9- 1ª Parcela de 13º Salário,** para que a diferença da 1ª parcela seja lançada.
* Diferença de 13º Salário: Se a diferença for paga no mês de Janeiro será habilitado o combo apresentando os eventos com **código de cálculo 66** com incidência em **INSS folha** para o cálculo da diferença.

**Importante**Após o cálculo da rescisão complementar não será possível realizar alterações no envelope como, por exemplo, editar, inserir ou excluir eventos e recalcular o envelope  
  
**Saiba mais**  
Para mais informações, acesse o [TDN - Rescisão Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718921).
