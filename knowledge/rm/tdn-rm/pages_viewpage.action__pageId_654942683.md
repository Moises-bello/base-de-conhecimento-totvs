---
content_hash: fb36f6eec291177d33d9b86e33f570933d76a38e6d6d5d28b82df8a6074ba87c
fetched_at: '2026-06-29T00:11:12.559009+00:00'
page_id: '654942683'
product: rm
source: tdn-rm
title: Quando ocorrer uma rescisão após o pagamento da 2ª parcela e o valor do 13º
  Salário lançado em rescisão é menor do que o pago em 2ª parcela, gerando uma restituição
  de inss 13º,  como proceder?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654942683
version: 12
---

Esta situação ocorre quando já houve o cálculo da 2ª parcela de 13º salário e transmissão para para o esocial ou pagamento do funcionário e o mesmo é demitido no dia 10/12, gerando um valor de 13o salário menor na rescisão, já que não completou o avo de dezembro.Exemplo: demissão no dia 10/12, ao calcular a rescisão será gerado um valor de restituição no período, já que descontou mais inss na folha de 2a parcela devido ao pagamento de 12/12 avos.

falseAtenção

O eSocial não permite lançamento de restituição de INSS em período (Demonstrativo de Pagamento) que não há o desconto de INSS, a orientação do governo é retificar a própria folha que gerou o desconto de inss a maior.  Veja a resposta do “Fale Conosco”  do governo no fim deste documento.

IMPORTANTE

É recomendado o cálculo gerando a retificação, veja como processar esse cálculo no TDN do parâmetro [Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912&draft=true).

Quando ocorre esta situação no RM, é exibido  a mensagem abaixo :

*“O sistema identificou restituição de INSS para o funcionário de chapa 00004. Porém, para o eSocial não é permitido ter restituição de INSS em período onde não consta o desconto com valor igual ou superior ao valor da restituição.*

Para que a restituição não seja paga na rescisão e consequentemente não exibir  a mensagem acima, criamos o passo a passo abaixo para solucionar. Para isto, será necessário retificar no esocial a 2a parcela de 13º salário acertando o desconto de inss 13 através do pagamento da restituição na própria folha de 13o salário.(orientação do governo)

Abaixo será ilustrado um exemplo, de um pagamento de 2ª parcela com previsão de pagamento no dia 20/12 e com uma demissão no dia 10/12.

*Envelope de pagamento da  2ª parcela 13º salário.*

*Período 1*

*Data do Pagamento 20/12/2021*

*Rescisão de Contrato com data de demissão no dia 10/12/2021, ao calcular é exibido a mensagem abaixo:*

O eSocial não valida o evento S-1299 quando ocorre uma restituição (evento provento) sem um evento de desconto de INSS 13º . É exibido uma mensagem de inconsistência no eSocial.

Caso NÃO tenha transmitido ao eSocial, poderá cancelar o período referente a 2ª parcela de 13º e calcular os valores em rescisão, desta forma não ocorrerá restituição na rct.

Caso tenha transmitido o 13º salário ao eSocial, deverá ser tratado como retificação.

***Como retificar a folha de 13º Salário***

Para não exibir a mensagem acima,  seguir os procedimentos abaixo:

1. Abrir o log de cálculo da rescisão  e recuperar os valores:

* *Restituição INSS 13º salário = 11,00*
* *Avo de 13º salário pago a maior = 122,23*

*Abaixo o log com os valores.*

2. Voltar o período “Local” para o cálculo da 2ª parcela de 13º salário

3. Incluir as verbas abaixo manualmente com os valores que foram extraídos do log de cálculo da rescisão.

* Restituição de INSS 13º : 11,00 - CC 153 - verba do tipo provento
* 2ª parcela 13º salário pago a maior em RCT: 122,23 - Verba do tipo desconto - com incidência de inss 13º salário. Natureza da rubrica mesma da 2ª parcela. Incidências mesma da da 2ª parcela.
* Líquido Retificação (Provento)  CC 383: 111,23 - verba do tipo provento

4. Clicar no botão “Recalcular Bases”.

O valor do líquido permanece (679.05), não sendo necessário gerar nova Remessa Bancária.

4. Retificar no esocial o envio do evento de 13º salário.

4.1 - Reabrir a folha de 13o salário através do evento S-1298

4.2 - Reenviar o através do evento S-1200  (Retificação dos valores da 2ª parcela 13º salário)

4.3 - Fechar a competência através do evento S-1299

A restituição de inss 13º foi gerada na própria folha de 2ª parcela, conforme orientação do governo. 

***Como não gerar  a restituição de INSS 13º na rescisão***

Procedimentos: 

1. Criar a fórmula abaixo e informar no campo “Fórmula valor”  no evento CC 51. Esta fórmula de desconto no CC51 só será calculada para os funcionários com demissão menor que 15/12/2021. Caso o funcionario seja demitido após o dia 15/12, terá que alterar esta data conforme necessidade do cliente.

Fórmula - CC 51

2. Voltar para o período da Folha (neste exemplo, período 3)

3. Calcular a rescisão, lançando um desconto “Líquido Retificação” descontando o valor 111.23 da verba 0377 (no envelope do 13º salário este líquido foi lançado como provento, agora será necessário lançar como desconto em rescisão):

* Líquido Retificação (Desconto) CC 383:  111,23 (sem incidências).

**Conclusão**

Foi pago no CC48 = 1.344.53  e descontado no CC 51 1344.53. Sendo assim, a folha de 13º salário foi regularizada e retificada no eSocial, possibilitando o correto recolhimento de INSS parte patronal e segurado.

E na  rescisão calculou corretamente o valor de 13º salário devido ao funcionário. (11/12 avos, já que a demissão foi em 10/12), não tendo o direito do avo de 12/2021.

***Pergunta TOTVS ao Órgão Governamental no “Fale Conosco”***

***Resposta***

Um de nossos clientes entrou em contato com o Fale Conosco do Governo, e obteve a resposta abaixo:
