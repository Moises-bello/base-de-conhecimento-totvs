---
article_id: 1500011639322
category: Férias
content_hash: 71ba038fdc4a35412e642dcadf9744f721da19aecb7a0a339f9c7e86cc12862d
fetched_at: '2026-06-28T22:46:56.392929+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Configuração para não pagamento de 1/3 do abono pecuniário
  conforme MP 1.046/2021
type: support-article
updated_at: '2025-03-12T20:11:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011639322-RH-RM-FOP-Configura%C3%A7%C3%A3o-para-n%C3%A3o-pagamento-de-1-3-do-abono-pecuni%C3%A1rio-conforme-MP-1-046-2021
---

**Ocorrência**

Não realizar o pagamento de 1/3 do abono pecuniário conforme MP 1.046 para que o pagamento do mesmo ocorra até 20/12.

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir das versões:

* 12.1.29.250
* 12.1.31.154
* 12.1.32.101 e superiores.

**Causa**

Conforme a MP1046 Art. 8º, A conversão de 1/3 do período de férias  de que trata o caput em abono pecuniário dependerá do empregador, hipótese em que o pagamento poderá ser efetuado até a data de que tratar o art. 7º: O adicional de um terço relativo às férias concedidas durante o período a que se refere o art. 1º poderá ser pago após a sua concessão, a critério do empregador, até a data em que é devida a gratificação natalina prevista no [art. 1º da Lei nº 4.749, de 12 de agosto de 1965](http://www.planalto.gov.br/ccivil_03/leis/l4749.htm).

Para atender a determinação do Art 8º, o Módulo TOTVS Folha de Pagamento disponibiliza o recurso de fórmulas que pode ser configurado pelo usuário para que não calculo 1/3 de abono pecuniário caso seja opção do empregador.  
  
**Solução**

### *Cálculo de férias*

**1)** Criar a fórmula conforme o exemplo abaixo e vincular no evento de código de cálculo 39 e 56:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018800242/mceclip0.png)

**Fórmula - Cálculo 1/3 de Abono Pecuniário**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018800282/mceclip1.png)  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-4-34.png?version=1&modificationDate=1620918274530&api=v2)   
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-6-25.png?version=1&modificationDate=1620918385557&api=v2)  
  
Cadastro do evento código de cálculo 39 e 56:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-5-17.png?version=1&modificationDate=1620918317130&api=v2)   
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-7-23.png?version=1&modificationDate=1620918443340&api=v2)  
  
**2)** Criar a Fórmula para incluir em um evento de base para armazenar o valor devido de Abono pecuniário e 1/3 de abono, que será pago posteriormente.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018800322/mceclip2.png)  
  
Incluir um evento do tipo Base de Cálculo com a fórmula acima para ser lançado no recibo de férias. O mesmo pode ser informado como evento adicional:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-10-39.png?version=1&modificationDate=1620918639583&api=v2)   
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-12-26.png?version=1&modificationDate=1620918746493&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-14-37.png?version=1&modificationDate=1620918877650&api=v2)  
  
**3)** Cadastrar/Calcular as Férias. Recibo de Férias após o cálculo das Férias lançou os eventos de base e não lançou os eventos de provento referente ao pagamento de abono:  
  
![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-27-5.png?version=1&modificationDate=1620919625820&api=v2)

![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-23-20.png?version=1&modificationDate=1620919400830&api=v2)  
  
**4)** Lançar Férias. Os eventos de base também será lançado no envelope do funcionário:

![](https://tdn.totvs.com/download/attachments/615606796/image2021-5-13_12-26-37.png?version=1&modificationDate=1620919598000&api=v2)
