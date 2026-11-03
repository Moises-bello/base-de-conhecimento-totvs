---
article_id: 32319832741527
category: Folha Mensal
content_hash: ffbeea14eb81d9da78c884640e38c98ff958918725c71f3887115289927971b8
fetched_at: '2026-06-28T22:46:58.074502+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador -  Provisionamento de Férias
type: support-article
updated_at: '2026-03-23T19:05:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32319832741527-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Provisionamento-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32319804102935) Tempo aproximado para leitura: **00:04:15 min**  
  
**Dúvida**  
Como é feito o provisionamento de férias para empréstimos do tipo Crédito do Trabalhador conforme a nova modalidade?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches: 12.1.2406.287; 12.1.2410.258; 12.1.2502.160; 12.1.2506.105 e superiores  
  
**Solução**

Para realizar corretamente o provisionamento de férias empréstimos do Crédito do Trabalhador, verifique os passos abaixo:

**1.** Para que a provisão seja calculada, no menu **Configurações | Parametrizador | Férias | Empréstimo**, o parâmetro **Lança Provisionamento do Empréstimo do Crédito Trabalhador nas férias** deve estar marcado. Demais informações dessa tela não são utilizadas para a modalidade Crédito do Trabalhador, portando, **não precisam ser preenchidas**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449147352983)

**2.** Também é necessário cadastrar previamente verbas com os [códigos de cálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719279) (CC) abaixo, que serão utilizados no processo:  
     **480** - Desconto Empréstimo Crédito do Trabalhador (DESCONTO - Será utilizado no envelope de pagamento)  
     **485** - Provisão Crédito Do Trabalhador Férias 1º Mês (DESCONTO - Será utilizado no recibo de férias)  
     **486** - Provisão Crédito Do Trabalhador Férias 2º Mês (DESCONTO - Será utilizado no recibo de férias)  
     **487** - Provisão Crédito Trab. Férias 1º Mês Envelope (PROVENTO - Será utilizado no envelope de pagamento)  
     **488** - Provisão Crédito Trab. Férias 2º Mês Envelope (PROVENTO - Será utilizado no envelope de pagamento)  
     **489** - Adiantamento Provisão Emprést.Crédito (DESCONTO - Será utilizado no envelope de pagamento)  
  
**3.** O cadastro do empréstimo deve possuir a modalidade **Crédito do Trabalhador eSocial** e ter um evento de **código de cálculo 480** associado. Observe também se o início do desconto e o valor da parcela estão corretamente informados;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449147353239)

**4.** No recibo de férias, o sistema irá lançar os códigos de cálculo **485 - Provisão Crédito Do Trabalhador Férias 1º Mês** e **486 - Provisão Crédito Do Trabalhador Férias 2º Mês** em caso de férias partidas ou somente o CC 485 caso as férias sejam integrais dentro do mês;  
  
**4.1.** No exemplo abaixo geramos uma férias partidas tendo 19 dias em um mês e 1 dia no próximo mês. Assim, o sistema lançou os **CC 485** e **486** proporcionalizando o valor do empréstimo correspondente a cada mês;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449116298135)

**4.2.** O log de cálculo irá apresentar o valor do detalhamento da proporcionalização;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449147353495)

**5.** Ao realizar o lançamento das férias para o envelope, o sistema irá gerar os códigos de cálculo **489 - Adiantamento Provisão Emprést.Crédito** substituindo no envelope os eventos de desconto presentes no recibo de férias, e também o **487 - Provisão Crédito Trab. Férias 1º Mês Envelope** como provento devolvendo o valor da provisão correspondente ao mês atual. O CC **488 - Provisão Crédito Trab. Férias 2º Mês Envelope** será lançado no mês seguinte ao realizar a liberação das férias.  
  
**5.1.** Continuando com o exemplo de férias cadastrado, o sistema efetuou o lançamento dos **CC 487** e **489** no **mês atual**, e o **CC 488** no **próximo mês** quando as férias foram finalizadas. Esse processo visa garantir que no mês seguinte o funcionário possua valor suficiente de proventos para o cálculo do desconto do empréstimo, evitando a geração de insuficiência de saldo para tal;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449116298647)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449116300311)

**6.** Na competência de lançamento do início das férias, ainda que não exista valor de horas/dias trabalhados  para cálculo, deverá ocorrer o lançamento do grupo de eventos . Isso permitirá ao sistema o lançamento do código de cálculo **480 - Desconto Empréstimo Crédito do Trabalhador** com o efetivo valor do empréstimo. O **lançamento desse CC é primordial** para que o Governo considere corretamente o valor relacionado ao empréstimo descontado do funcionário;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449147355927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33449116302359)

**7.** Somente após o lançamento do CC 480 o sistema irá atualizar a aba **Descontos de Empréstimos** no cadastro do empréstimo do funcionário (anexo **Folha de Pagamento | Empréstimos**).

![image-2025-6-18_10-34-52.png](https://tdn.totvs.com/download/attachments/963024323/image-2025-6-18_10-34-52.png?version=1&modificationDate=1751642407387&api=v2)

OBSERVAÇÕES:

* Somente será lançado o evento de provisionamento nas férias caso **não** exista o evento de provisionamento ou empréstimo lançado em algum período da competência;
* O provisionamento será lançado **proporcionalizando** de acordo com dias de férias calculadas em cada mês. No caso de férias partidas, por exemplo, se no 1º mês tiver 10 dias de férias e do 2º  mês tiver 20 dias, será lançado o provisionamento de 10 dias da parcela do empréstimo no 1º mês e 20 dias da parcela do empréstimo no 2º mês;
* **Independente da quantidade de dias pagos no mês** será proporcionalizado. Por exemplo, em um caso que haja 1 dia de férias em um dos meses, será feito o cálculo proporcional a esse dia;
* Dias de abono pecuniário **não** entram nesse cálculo de proporcionalização, serão considerados somente dias pagos como férias;
* O provisionamento somente será lançado para a modalidade de empréstimo **Crédito do Trabalhador eSocial**;
* Não será feita nenhuma tratativa para lançar o provisionamento dentro da margem consignável, mesmo se estiver parametrizado;
  + Se não tiver líquido suficiente para desconto, deve lançar até o líquido disponível, **não gerando evento de arredondamento/insuficiência de saldo;**
* O cadastro de empréstimo não será atualizado quando lançar o provisionamento nas férias, somente será atualizado após lançar o grupo de eventos.

IMPORTANTE:

Em versões/patches mais recentes, foi criado o parâmetro **"Período para lançar o provisionamento do empréstimo crédito do trabalhador nas férias"**, permitindo que os eventos de provisão (CC 487 e 488) sejam lançados em período distinto do gozo de férias. Caso o campo não seja preenchido, o comportamento permanece como na versão anterior, realizando o lançamento no mesmo envelope das férias. Para mais detalhes, consulte o material: [RH - RM - FOP - Crédito do Trabalhador - Período de lançamento do Provisionamento de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/39239569152407-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Per%C3%ADodo-de-lan%C3%A7amento-do-Provisionamento-de-F%C3%A9rias)

**SAIBA MAIS**

* [Cálculo de Férias - Provisionamento nas Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=963024323)
* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
