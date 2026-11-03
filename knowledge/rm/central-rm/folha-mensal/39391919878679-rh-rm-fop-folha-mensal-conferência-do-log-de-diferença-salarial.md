---
article_id: 39391919878679
category: Folha Mensal
content_hash: 03061829feb08e2f07bf0a9103f854c8b02e74d44e75df56978a83f873ae8e92
fetched_at: '2026-06-28T22:46:57.953540+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Conferência do Log de Diferença Salarial'
type: support-article
updated_at: '2026-03-30T19:28:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39391919878679-RH-RM-FOP-Folha-Mensal-Confer%C3%AAncia-do-Log-de-Diferen%C3%A7a-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39391919861527) Tempo aproximado para leitura: **00:06:38 min**  
  
**Dúvida**  
Como interpretar o log de cálculo de diferença salarial (dissídio) e identificar a origem dos valores gerados no envelope de pagamento?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Quando ocorre um aumento salarial retroativo (por exemplo, concedido na competência 09 com efeito na competência 08), o sistema realiza um recálculo da folha anterior para identificar valores que deveriam ter sido pagos com base no novo salário.  
  
O log de diferença compara o que foi pago originalmente com o que deveria ter sido pago com o novo salário.

Ele é dividido em quatro partes principais por período analisado:

* Envelope Original: O que já foi calculado e fechado no mês anterior;
* Envelope Recalculado: O cálculo simulado com o novo valor do salário;
* Diferenças do Período: O resultado da subtração (Recalculado - Original);
* Envelope de Diferença Acumulada: Onde o sistema consolida os valores para pagamento no período atual.

1.Ao acessar o log de cálculo do envelope é demonstrado as informações do Envelope original:

O envelope original representa o cálculo da folha na competência em que foi efetivamente processada e fechada. No nosso exemplo, a folha é da competência 08 (Agosto).

Características:

* O envelope original considera o salário vigente na época (antes do reajuste);
* Contém os valores já pagos ao funcionário;
* Serve como base para comparação.

Veja o exemplo abaixo onde é demonstrado o Envelope Original do mês 08/2011: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39396754628759)

Na imagem apresentada, os eventos são informados com os seus respectivos valores originais. O evento 0001 (horas normais) por exemplo, é apresentado com o valor de **2.699,37** pois é o valor que foi pago ao funcionário dentro do mês 08.   
  
Todos esses valores representam o pagamento original realizado ao colaborador.

2. Em seguida, logo abaixo do Envelope Original, são demonstrados os valores recalculados. Esses valores são, basicamente,  o processamento da mesma folha, considerando o novo salário com efeito retroativo.

Características:

* Mantém as mesmas quantidades de eventos (horas, faltas, etc.);
* Aplica o novo valor de salário;
* Recalcula todos os eventos dependentes do salário.

Objetivo:  
  
Demonstrar quanto deveria ter sido pago caso o salário atualizado já estivesse vigente na competência original.

Veja abaixo um exemplo com o Envelope Recalculado: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39396879265687)

Conforme demonstrado na imagem acima, os valores são alterados após o recálculo, esses novos valores são processados considerando o novo valor do salário. Por exemplo: O evento original tinha o valor de R$ 2.699,37 no envelope original (antes do recálculo). Após o recálculo, o valor passou a ser  R$ 2.969,30.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39398886417047)

O mesmo ocorreu com os outros eventos, como por exemplo a verba de Hora extra 50%, que no envelope original estava com o valor de 1.464,70 e após recálculo o valor ficou como 1.611,17.   
  
  
3.  Apuração das diferenças:

Após o recálculo, o sistema apura a diferença entre os valores recalculados e os valores originais.  
  
Fórmula aplicada:  
  
**Diferença = Valor Recalculado – Valor Original.**  
  
O resultado representa os valores complementares que devem ser pagos ou descontados do funcionário.

Veja no exemplo abaixo um exemplo do log de cálculo com os valores de diferença aplicados: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39396879267351)

A imagem acima demonstra as diferenças por evento. Por exemplo:   
  
O evento de Horas Normais possui uma diferença de R$ 269,93, pois se fizermos o cálculo: **2.969,30 - 2.699,37 = R$ 269,93**. Esse valor corresponde exatamente a diferença entre valor original e o valor recalculado.

**Saiba Mais**

[RH - RM - FOP - Diferença salarial por dissídio retroativa à competência atual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414433322519-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-retroativa-%C3%A0-compet%C3%AAncia-atual)
