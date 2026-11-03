---
article_id: 360006840032
category: Folha Mensal
content_hash: f1cfa5b403b087e70c6603001ea4fa3fdb9575078d7fafa4d8d2ef1b1cd34e5d
fetched_at: '2026-06-28T22:47:00.323427+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Salário Família: base de cálculo'
type: support-article
updated_at: '2026-03-27T18:30:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006840032-RH-RM-FOP-Sal%C3%A1rio-Fam%C3%ADlia-base-de-c%C3%A1lculo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27287232538007)Tempo aproximado para leitura: **00:00:50 min**  
  
**Dúvida**  
Como parametrizar a base para o cálculo do salário família corretamente para lançamento de folha de pagamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para o cálculo do salário família o sistema considera o salário nominal + eventos que incidem em salário família. Desta forma, existem apenas duas parametrizações para configurar o processo:  
  
1. Acesse: **Configurações |** **Parametrizador | Folha Normal | Salário Família**. Nesta tela você verificará a flag **Usa salário nominal**. Feito isso, marque o parâmetro caso queira que o salário nominal do funcionário seja considerado para o cálculo da base de Salário Família.  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27287232540695)  
  
2. Para parametrizar os eventos para incidir em salário família, acesse: **Administração de Pessoal | Eventos | Eventos**. Logo, edite o cadastro do evento que você desejar parametrizar e no **cadastro do evento | aba Inc. Proventos** você encontrará o parâmetro **Salário Família**. Este parâmetro define se o evento terá ou não incidência no cálculo da base do salário família.  
  
![EVENTO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007847651)  
  
**Observação**

* Quando em **Configurações |** **Parametrizador | Folha Normal | Salário Família** a flag **"Usa Salário Nominal"** está marcada, os eventos de código de cálculo 1 e 2  não devem ter a incidência salário família marcada em **Inc. Proventos**.
* O evento de código de cálculo 5 - salário família deve possuir prioridade maior do que os eventos que possuem incidência em salário família marcadas.  
    
  **Importante**  
  Para admitidos no mês e demitidos no mês, o sistema sempre irá considerar o salário base, salário do cadastro, para a base de salário família pois, de acordo com a Portaria MPS Nº 348, DE 08 DE ABRIL DE 2003, artigo 8º§§ 1º e 2º, o funcionário não terá direito ao recebimento do salário família de maneira proporcional ao dias trabalhados, pois, a base de calculo nesses casos, conforme §1º da Lei, é devida sobre a remuneração independentemente se ele trabalhou ou não todos os dias do mês. Ou seja, nos meses de admissão e demissão a base para salário família não é o valor recebido em função dos dias/horas trabalhadas e sim sobre o valor que seria devido caso trabalhasse o mês todo.   
    
  Caso queria pagar o salário família nestes casos, poderá lançar o valor para os funcionários através do [Código de Cálculo 65 - Diferença Salário Família.](https://tdn.totvs.com/pages/releaseview.action?pageId=452718611)  
    
  Apenas o valor da cota de salário família, valor do pagamento do salário família, será proporcionalizado em função dos dias trabalhados.​
