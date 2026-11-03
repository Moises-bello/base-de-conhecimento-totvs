---
content_hash: 24388694d47a8335bb2772c3eb3de4a2773417405e7b7d605796967594b30322
fetched_at: '2026-06-29T00:10:18.483636+00:00'
page_id: '4812466'
product: rm
source: tdn-rm
title: Diferença de 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812466
version: 36
---

BLOCK

Diferença de 13º Salário

FAQ: **Diferença de 13º Salário**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: |  |
| Versão: | 12.1 |

### Avaliação

Este documento visa demonstrar o cálculo e lançamento da diferença de 13º salário.

### Causa

Existem três formas de efetuar este lançamento:

* Em Dezembro;
* Em Janeiro;
* Nos meses de Fevereiro a Novembro.

### 

### Solução

**Procedimento a ser realizado no mês de Dezembro:**

Pelo fato do 13º salário ser pago antes da movimentação de folha do mês de Dezembro ter sido fechada, podem ocorrer lançamentos de eventos com incidência em média de 13º salário após este pagamento. Neste caso, o valor da média de 13º salário lançado para o funcionário, ficará menor que o correto. Portanto será necessário efetuar o pagamento de diferença de 13º salário para este funcionário.

**Segue abaixo um exemplo deste caso:**

Em Novembro foi lançado o evento ‘0083 – HORA EXTRA 100%’.

Cálculo efetuado: 227,27 / 12 = 18,18.

Este valor se deve ao evento ‘0083 – HORA EXTRA 100%’, com incidência em média de 13º salário e valor de

R$227,27 lançado no mês de novembro.

**OBS:** O evento '0083 – HORA EXTRA 100%’, é apenas um exemplo. Podem ser utilizados outros eventos que incidam em médias, como: 'HORA EXTRA 50%'.

Ainda em Novembro foi lançada a primeira parcela de 13°.

No mês de Dezembro, no período 1, foi lançada a 2ª parcela do 13º para o funcionário.

Ainda no mês de Dezembro, foi lançado o evento ‘0133 – MEDIA HORA EXTRA 2ª PARC 13º’, que foi lançado com o valor de R$18,94.

**DEZEMBRO**

Após o pagamento da 2ª parcela do 13º, foi efetuado o lançamento dos eventos de folha do funcionário, no período 3.

O evento ‘0083 – HORA EXTRA 100%’, foi lançado neste envelope, com o valor R$227,27. Como o evento foi lançado no mês de dezembro e tem incidência em média de 13º, o valor do mesmo deve ser considerado para o cálculo da média de 13º deste ano.

**JANEIRO**

Será necessário efetuar o seguinte procedimento:

* Alterar o período local para um período posterior ao período de lançamento dos eventos de folha;
* Acessar o módulo ' Folha de Pagamento → Folha Mensal → 13° Salario → Diferença 13°;
* Preencher a seleção de funcionários corretamente e informar a chapa do funcionário;
* Marcar o parâmetro ‘Dissídio: NÃO’;

Ao pagar a diferença de 13º salário no mês de Dezembro, o sistema assumirá o evento com Código de Cálculo '66' cadastrado no sindicato do funcionário, no Grupo 0, no campo ‘Evento de Diferença’, localizado na aba “Diferença de 13º salário”.

Caso o evento não esteja cadastrado no sindicato, o sistema assumirá o 1º evento cadastrado com CC (66) no cadastro de eventos.

Após processar a diferença de 13º, o envelope de pagamento ficará da seguinte forma:

Calculado efetuado: 227,27 / 12 = 18,94.

Referente a: 37,88 (valor total da média) – 18,94 (valor já pago para o funcionário no mês anterior) = R$18,94.

O IRRF também foi recalculado e a diferença do mesmo foi lançada no evento ‘0049 – I.R.R.F 13º Salário’.

O valor de INSS já havia sido descontado de forma integral no lançamento da 2ª parcela.

A diferença de 13º salário também poderá ser calculada quando o funcionário tiver um reajuste salarial no mês de dezembro e já tiver recebido o 13º com o valor do salário anterior. O salário do funcionário deverá ser alterado no cadastro do mesmo, e, após isso, efetuar o mesmo procedimento informado no exemplo anterior.

**Procedimento a ser realizado no mês de Janeiro:**

Para calcular a diferença de 13º salário no mês de Janeiro, será necessário cadastrar um novo evento.

Este evento terá o código de cálculo 66 - Dif. 13º Salário e deverá ser do tipo Provento e Valor, conforme demonstra a imagem abaixo:

Deverão ser marcadas as incidências em FGTS e INSS de folha;

O evento terá incidência em IRRF 13º.

Deve-se marcar as incidências da imagem acima pois, o provento pago em Janeiro participa do cálculo de INSS de Folha e utiliza a tabela de cálculo de INSS de Janeiro, ou seja, o recolhimento de INSS será feito juntamente com a folha de Janeiro (conforme legislação vigente).

A diferença de 13º salário calculada no mês de Janeiro, pode ocorrer pelo fato do salário do funcionário ter sido alterado de forma retroativa, após o fechamento da folha de pagamento do mês de Dezembro.

Segue abaixo um exemplo deste caso:

O cálculo do 13º salário do funcionário, foi efetuado com o salário no valor de R$4.000,00.

**Envelope do lançamento da 1ª parcela do funcionário:**

**Envelope do lançamento da 2ª parcela do funcionário:**

No mês de Janeiro, o salário do funcionário foi alterado para R$5.000,00, com data retroativa à 20/12/2011.

**Será necessário efetuar o seguinte procedimento:**

Alterar o período local para um período posterior ao período de lançamento dos eventos de folha;

* Acessar o módulo Folha de Pagamento → Folha Mensal→ 13° Salário → Diferença 13°;
* Preencher a seleção de funcionários corretamente e informar a chapa do funcionário;
* Marcar o parâmetro ‘Dissídio: NÃO’;
* Selecionar o evento de diferença de 13º, com código de cálculo 66 e incidência em INSS de folha.

**OBS:** ao calcular a diferença de 13º salário em Janeiro, todos os valores referentes à diferença serão lançados no evento de código de cálculo 66 informado no momento de processar o cálculo da diferença.

**Após processar a diferença de 13º, o envelope de pagamento ficará da seguinte forma:**

No evento ‘0066 – DIFERENÇA 13º SALARIO’, o sistema lançou o valor de R$ 1.000,00, sendo R$45,45 referentes à diferença do evento ‘0129 – 2ª PARCELA 13º SALARIO’ e R$3,79 referentes à diferença do evento ‘0133 – MEDIA HORA EXTRA 2ª PARC 13º’.

O valor do IRRF de 13º, foi recalculado considerando a base de IRRF do mês de Dezembro, foi lançado o valor de diferença.

**OBS:** É possível notar que o INSS foi calculado como evento de INSS de folha e o valor foi calculado sobre o evento da diferença lançado no envelope.

**Procedimento a ser realizado nos meses de Fevereiro a Novembro:**

Para calcular a diferença de 13º salário nos meses de Fevereiro a Novembro, será necessário cadastrar um novo evento.

Este evento terá o código de cálculo '180 - DIFERENÇA DE 13º SALÁRIO POR DISSÍDIO', deve ser do tipo Provento e Valor.

* O evento terá incidência de acordo com o TDN do [código de cálculo 180 - Diferença de 13º Salário por Dissidio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718369)

Em 'Administração Pessoal → Sindicatos' , editar na aba “13º Salário”, sub-aba “Eventos p/ Pag. de Média de 13º na 2ª Parcela”. Editar o grupo 0 (zero) e informar o evento no campo ‘Evento para diferença por dissídio’. Este evento deverá ser informado no cadastro de todos os sindicatos.

**OBS:** Poderão ser criados eventos de diferença de 13º salário por dissídio, para discriminar as médias.

Os eventos terão a mesma parametrização do evento ‘0311 - DIFERENÇA DE 13º SALÁRIO POR DISSÍDIO’ e deverão ser informados nos outros grupos criados no sindicato, na aba “13º Salário”, sub-aba “Eventos p/ Pag. de Média de 13º na 2ª Parcela”.

Assim como no mês de Janeiro, a diferença de 13º salário calculada nos meses de Fevereiro a Novembro, poderá ocorrer pelo fato do salário do funcionário ter sido alterado de forma retroativa após o fechamento da folha de pagamento do mês de Dezembro.

Vamos usar o mesmo exemplo do caso anterior, onde o cálculo do 13º salário do funcionário foi efetuado com o salário no valor de R$4.000,00.

**Envelope do lançamento da 1ª parcela do funcionário:**

**Envelope do lançamento da 2ª parcela do funcionário:**

No mês de Janeiro, o salário do funcionário foi alterado para R$5.000,00, com data retroativa a 20/12/2011.

Será necessário efetuar o seguinte procedimento:

* Alterar o período local para um período posterior ao período de lançamento dos eventos de folha;
* Acessar o módulo 'Folha de Pagamento→ Folha Mensal → Diferença 13°';
* Preencher a seleção de funcionários corretamente e informar a chapa do funcionário;
* O campo ‘Dissídio’ estará desabilitado nos meses de Fevereiro a Novembro, pois, nestes meses a diferença de 13° só poderá ser paga por dissídio;
* Será apresentada uma caixa com a opção de selecionar o ‘Ano de referência’;
* Informar o ano para o qual a diferença será calculada, conforme demonstra a imagem abaixo.

**Após processar a diferença de 13º, o envelope de pagamento ficará da seguinte forma:**

No evento ‘0311 – DIFERENÇA DE 13º SALARIO POR DISSÍDIO’, o sistema lançou o valor de R$1.000,00, referentes à diferença do evento ‘0129 – 2ª PARCELA 13º SALARIO’.

No evento ‘0401 – DIFERENÇA MÉDIA HORAS EXTRAS 2ª PARC 13º, o sistema lançou o valor de R$3,79 referentes à diferença do evento ‘0133 – MEDIA HORA EXTRA 2ª PARC 13º’.

O valor do IRRF de 13º, foi recalculado considerando a base de IRRF do mês de Dezembro. Foi lançado o valor de diferença.

**Observações**

Como o cálculo da diferença foi efetuado por dissídio, deve ser considerada a base de INSS do mês onde foi paga a segunda parcela do 13º salário. No caso deste funcionário, foi descontado o teto do INSS de 13º salário no mês de Dezembro, portanto, não haverá diferença de INSS de 13º salário para o mesmo.
