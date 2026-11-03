---
article_id: 32152995698071
category: Folha Mensal
content_hash: 3d52f8172992ce7debd1b8b2533c847e4d02a76b05a694fc603e668a0cf5ecc6
fetched_at: '2026-06-28T22:46:58.093460+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Cálculo 35% da Margem Consignável
  e Remuneração Disponível
type: support-article
updated_at: '2025-08-01T11:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32152995698071-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-C%C3%A1lculo-35-da-Margem-Consign%C3%A1vel-e-Remunera%C3%A7%C3%A3o-Dispon%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32152995661335) Tempo aproximado para leitura: **00:05:13 min****Dúvida**Como irá funcionar o cálculo dos 35% da margem consignável?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches: 12.1.2406.290, 12.1.2410.261, 12.1.2502.164, 12.1.2506.108 e superiores  
 **Solução**Antes das versões citadas na área **Ambiente**, o sistema considerava para o cálculo da margem consignável apenas o líquido do envelope. A partir de tais versões, o sistema passou a considerar como padrão para o cálculo a **base de contribuição previdenciária**, assim como sugere o [Manual Operacional do Empregador do Crédito do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf).  
  
O manual também apresenta os seguintes conceitos:

**Remuneração Disponível** - Valor da remuneração do trabalhador obtido após a dedução de descontos obrigatórios (INSS e IRRF) e demais descontos com incidência em INSS, bem como descontos compulsórios. 

**Margem Consignável** - Representa o limite máximo de desconto mensal permitido, correspondente a 35% da remuneração disponível. 

**•  CÁLCULO DA REMUNERAÇÃO DISPONÍVEL**  
No sistema, o cálculo da **remuneração disponível** é feita considerando a seguinte parametrização: 

* Menu **Configurações | Parametrizador | Folha Normal**, etapa [**Crédito Trabalhador**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=937259572), parâmetro **Eventos do Crédito Trabalhador devem ser adicionados na base de Contribuição Previdenciária**;
* Menu **Configurações | Parametrizador | Folha Normal**, etapa **[Eventos do Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=938311837)**;
* Cadastro do funcionário, anexo **Folha de Pagamento | [Eventos Remuneração Crédito Trabalhador](https://tdn.totvs.com/pages/viewpage.action?pageId=938311818)**.

O cálculo da remuneração irá considerar a marcação ou não do parâmetro, bem como a existência ou não de eventos informados no parametrizador e/ou no anexo do funcionário

* **PARÂMETRO MARCADO** ou **DESMARCADO** + **SEM EVENTOS INFORMADO** = Cálculo irá considerar a Base de INSS
* **PARÂMETRO MARCADO** + **EVENTOS INFORMADOS** = Cálculo irá considerar a Base de INSS e também os eventos informados no parametrizador e/ou anexo
* **PARÂMETRO DESMARCADO** + **EVENTOS INFORMADOS** = Cálculo irá considerar somente os eventos informados

#### ⚠️ O valor da **remuneração disponível** encontrado será lançado no sistema através do Código de Cálculo (CC) **482 - Remuneração Base Empréstimo Crédito do Trabalhador**.

**• CÁLCULO DOS 35% DA MARGEM CONSIGNÁVEL**

Para o cálculo da margem consignável, o sistema irá aplicar o percentual dos 35% sobre o valor da remuneração disponível encontrada.

#### ⚠️ Após encontrar o valor dos 35% da **margem consignável**, o sistema irá lançar o desconto da parcela do empréstimo através do Código de Cálculo (CC) **480 - Desconto Empréstimo Crédito do Trabalhador**, se limitando ao valor da margem.

O código de cálculo 480 irá representar o efetivo desconto do Crédito do Trabalhador. No caso de **múltiplos empréstimos**, é necessário cadastrar um código de cálculo 480 para cada empréstimo vinculado ao mesmo funcionário. Isso porque, no Leiaute do eSocial, ao gerar a verba do desconto do empréstimo no XML é necessário informar também os dados do empréstimo vinculado a tal pagamento.

**• EXEMPLO DE CÁLCULO**

1. No menu **Configurações | Parametrizador | Folha Normal | Crédito Trabalhador**, o parâmetro **Eventos do Crédito Trabalhador devem ser adicionados na base da Contribuição Previdenciária** está marcado;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871476150551)

1.1. Como não foi informado nenhum evento na etapa **Eventos do Crédito Trabalhador** desse mesmo parametrizador, nem no anexo **Eventos Remuneração Crédito Trabalhador** do cadastro do funcionário, o sistema irá considerar para o cálculo da remuneração **somente a base de INSS**;

2. O funcionário de chapa 00019 possui dois empréstimos do Crédito do Trabalhador cadastrados;

2.1. O empréstimo de código **EMPT0000001** está com o campo **Valor da Parcela** preenchido com o valor **R$ 200,00**. Também possui preenchido o percentual da margem com o valor 35%. Verba vinculada para desconto, código **0480**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871481669399)

2.2. O empréstimo de código **EMPT0000007** está com o campo **Valor da Parcela** preenchido com o valor **R$ 300,00**. Também possui preenchido o percentual da margem com o valor 35%. Verba vinculada para desconto, código **0148**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871476153239)

3. No menu **Folha Mensal | Lançamentos | Grupos de Eventos**, foi realizado o lançamento do empréstimo selecionando o parâmetro **Lançar Empréstimos** e indicando o empréstimo do **Crédito do Trabalhador** no campo **Tipo do Empréstimo**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871476154391)

4. No envelope do funcionário, a única verba com incidência em INSS é a 0002 - DIAS TRABALHADOS no valor de R$ 2323,20. Sobre esse valor, é necessário descontar a verba 0003 - INSS, no valor de R$ 187,90. O cálculo da **remuneração disponível** será a base de contribuição previdenciária - INSS - IRRF, ou seja, R$ 2323,20 - R$ 187,90 = **R$ 2135,30;** Esse valor será lançado no **CC 482;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871476155031)

4.1. Já o cálculo da **margem será 35%** sobre o valor da remuneração, ou seja, **35%** de **R$ 2135,30.** Esse valor da margem será exibido no **Log de Cálculo** do **CC 480**. O sistema irá então lançar o desconto da parcela nesse CC se limitando ao valor da margem;

4.2. Na verba **0480**, vinculada ao empréstimo **EMPT0000001**, o sistema considerou as verbas que compõem a remuneração e aplicou os 35% sobre esse valor, chegando em R$ 747,36. Esse é o limite máximo de desconto. Como a parcela do empréstimo **EMPT0000001**é de R$ 200,00, foi descontado esse valor na verba 0480;

4.3. Já na verba **1480**, vinculada ao empréstimo **EMPT0000007**, o sistema faz a mesma validação porém, **deduz** do limite da margem o valor **já descontado anteriormente** na verba **0480**, ou seja, retira R$ 200 dos R$ 747,36, chegando em R$ 547,36. Esse é o valor máximo que poderá ser descontado na verba 01480. Como o valor da parcela do empréstimo **EMPT0000007** é R$ 300, menor que o limite, foi descontada parcela integralmente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871476155159)

5. Abaixo, segue print do envelope apresentando o **CC 482** com o valor da remuneração disponível **R$ 2135,30**, e os **CC 480** representando os dois descontos do empréstimo, no valor de **R$ 200** e **R$ 300**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33871481673623)

**Importante**  
Caso o valor das parcelas dos empréstimos fossem maiores que o limite da margem consignável, o valor excedente à margem será lançado no **CC 483 - Insuficiência Saldo Empréstimo Crédito Trabalhador**, conforme exemplo a seguir: [Cálculo da Folha - Insuficiência de saldo](https://tdn.totvs.com/pages/viewpage.action?pageId=963023701).

**Saiba mais**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
