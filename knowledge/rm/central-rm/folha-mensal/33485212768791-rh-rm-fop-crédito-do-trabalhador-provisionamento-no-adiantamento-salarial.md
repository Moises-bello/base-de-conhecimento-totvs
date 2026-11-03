---
article_id: 33485212768791
category: Folha Mensal
content_hash: 210054dd07641b8fcec094aaa0d1f0616436b5f6a3d8b8a96424fcbcac9cdc92
fetched_at: '2026-06-28T22:46:58.030377+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador -  Provisionamento no adiantamento salarial
type: support-article
updated_at: '2025-08-29T12:18:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33485212768791-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Provisionamento-no-adiantamento-salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33485212730903)  Tempo aproximado para leitura: **00:02:32min**  
  
**Dúvida**  
Como é feito o provisionamento de adiantamento salarial para empréstimos do tipo Crédito do Trabalhador conforme a nova modalidade?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches 12.1.2406.277, 12.1.2410.229, 12.1.2502.145, 12.1.2506 e superiores  
  
**Solução**

Veja abaixo o processo para o lançamento do provisionamento no adiantamento:

1. Conforme o manual do **Crédito do Trabalhador**, o empregador pode provisionar, no momento do adiantamento, o valor correspondente à parcela do empréstimo consignado, de forma **proporcional ao valor antecipado**. Sendo assim, o cálculo do provisionamento no adiantamento salarial, quando realizado, será realizado considerando o **percentual do adiantamento**. Não será feita nenhuma tratativa para lançar dentro da margem consignável, mesmo se estiver parametrizado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33485203721111)

2. É necessário que, no cadastro do Funcionário, exista informações do empréstimo registrado com modalidade **Crédito do Trabalhador eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33486062006551)

3. No menu **Folha Mensal | Lançamentos | Grupo de Eventos**, ao efetuar o lançamento do grupo, selecione o parâmetro **Lançar Provisionamento do Empréstimo do Crédito do Trabalhador eSocial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33486062010647)

4. No envelope do funcionário, será lançado o evento de **código de cálculo (CC) 481** como desconto da provisão. Importante reforçar que este evento de desconto **não pode** conter a natureza de rubrica **9253**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33486062015767)

5. Ao lançar a folha de pagamento do funcionário, o sistema irá lançar o **CC 484** devolvendo o valor da provisão. Também irá lançar o **CC 480** com o **efetivo desconto do empréstim**o, calculado considerando as margens da base do crédito. O **CC 480** deverá conter a natureza de rubrica **9253** para que seja corretamente levado ao eSocial;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33486035406231)

**Importante**  
Se não tiver líquido suficiente para desconto será lançado o desconto até o líquido disponível, não gerando evento de arredondamento/insuficiência de saldo;

Quando não houver valor no percentual de adiantamento no cadastro do funcionário será apresentada a mensagem no log.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33486035407895)

**Saiba mais**

* [RH - RM - FOP - Crédito do Trabalhador - Provisionamento de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32319832741527-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Provisionamento-de-F%C3%A9rias)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/releaseview.action?pageId=925361639)
