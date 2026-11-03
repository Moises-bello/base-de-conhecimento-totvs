---
article_id: 5318614050839
category: Rescisão
content_hash: 4e323f9e85b1753549a1f1281daf0a19dc55f6719614a964495113881fcad4b4
fetched_at: '2026-06-28T22:46:54.386184+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Indenização Adicional devida na Dispensa antes da Data Base
type: support-article
updated_at: '2024-09-24T14:12:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5318614050839-RH-RM-FOP-Indeniza%C3%A7%C3%A3o-Adicional-devida-na-Dispensa-antes-da-Data-Base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26587793795991) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como lançar indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base na rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O empregado dispensado, sem justa causa, no período de 30, trinta, dias que antecede a data de sua correção salarial, terá direito à indenização adicional equivalente a 1, um, salário mensal, seja ele optante ou não pelo [Fundo de Garantia por Tempo de Serviço - FGTS.](http://www.guiatrabalhista.com.br/guia/fgts.htm)  
  
Para solucionar essa dúvida, realize o passo a passo abaixo:  
  
1. Primeiramente, é necessário realizar a criação dos eventos abaixo:

* [Código de Cálculo 344 - Indenização Adicional na Dispensa Antes Data Base](https://tdn.totvs.com/pages/releaseview.action?pageId=452718308)
* [Código de Cálculo 345 - Diferença Indeniz. Adic. na Dispensa Antes Data Base](https://tdn.totvs.com/pages/releaseview.action?pageId=452718634)

2. O evento de código de cálculo 344 deverá ter uma fórmula cadastrada, para retorno do valor de cada sindicato. No exemplo abaixo, a fórmula retorna o salário do funcionário.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5318682480151)  
  
3. Feito isso, acesse: **Administração de Pessoal | Sindicatos** e edite o sindicato do funcionário. Logo, marque o parâmetro **Lança indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base** e informe o dia e mês da data base.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26587793809047)  
  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5318768168727)  
  
Ao calcular uma rescisão que está dentro do prazo de 30 dias que antecede o dia e mês da data base cadastrado no sindicato será lançado o evento de código de cálculo 344.  
  
Quando houver cálculo de rescisão complementar cujo valor da fórmula do código de cálculo 344 seja influenciado, será lançado o evento de código de cálculo 345.  
  
**Importante**- Estes códigos de cálculo somente serão lançados se o parâmetro estiver marcado e a data informada, caso não satisfaça uma das condições o evento não será lançado.  
- A data informada no sindicato entra no cálculo de dias, portanto, se o aviso for 03/03 terminando dia 01/04 será pago o evento, caso seja 04/03 terminando em 02/04 não será pago o evento.  
- A fórmula para ser vinculada ao evento CC344 deverá ser criada pela empresa.  
  
**Saiba mais**[RH - RM - FOP - Fórmulas e Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061764374-RH-RM-FOP-F%C3%B3rmulas-e-Fun%C3%A7%C3%B5es)  
[RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)
