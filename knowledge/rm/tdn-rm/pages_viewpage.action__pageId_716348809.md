---
content_hash: bb7db6c51ab4ae80b918b3522463c48f093ca3ed6f0c997ce3496d87649d4383
fetched_at: '2026-06-29T00:11:26.341900+00:00'
page_id: '716348809'
product: rm
source: tdn-rm
title: Ordem de Aplicação do Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716348809
version: 7
---

---

O campo “Aplicar desconto por antecipação” define se o desconto por antecipação será aplicado “Antes do cálculo da bolsa” ou “Depois do cálculo da bolsa”. Uma vez aplicado (calculado) o desconto por antecipação, o mesmo não será calculado novamente, isto é, não será permitida a inserção de uma bolsa com o valor setado para “Depois do cálculo da bolsa” cuja ordem de aplicação dessa bolsa seja maior do que uma outra bolsa com o valor “Antes do cálculo da bolsa” pois o desconto já foi processado ao se calcular o valor da primeira bolsa.

CadastroBolsasCadastro de BolsasCadastro de Bolsas

Acréscimo do campo "Aplicar desconto por antecipação" que conterá o valor default "Antes do cálculo da bolsa". O preenchimento do campo "Aplicar desconto por antecipação" conterá o valor default para o cadastro de bolsas nos contratos, ou seja, a cada vez que uma bolsa for inserida no contrato do aluno, a mesma será inserida com o valor informado no cadastro da bolsa.

Tela do cadastro de bolsas com o novo campo:

  

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação

de bolsa setado com o valor "Contrato"

BolsasContratoBolsas de ContratosBolsa do Contrato

Acréscimo do campo "Aplicar desconto por antecipação" que buscará o valor default do valor informado para o respectivo campo do cadastro de bolsas. Esse campo também só ficará visível para o usuário se o parâmetro de aplicação de bolsa estiver setado com o valor "Contrato" conforme citado no tópico anterior.

Tela do cadastro de bolsas com o novo campo:

Validação de inclusão ou alteração de bolsas de contratos: O sistema validará o preenchimento do campo conforme o campo "Tipo da Bolsa" na edição do contrato e conforme registros de bolsas de contratos previamente cadastrados.

1. Tipo de Bolsa = "Aplicar bolsas em cascata": Quando o contrato estiver setado com esse tipo de bolsa, não será permitido se ter uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" com ordem menor ou igual à uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa". A mensagem será alterada dependendo da bolsa que estão sendo inserida / alterada.   
     
   Se estivermos inserindo uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa" e já tivermos uma bolsa no contrato com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" com ordem menor ou igual à bolsa que está sendo inserida ou alterada, o sistema exibirá a mensagem abaixo:  
     

   Se estivermos inserindo uma bolsa com o campo "Aplicar desconto por antecipação" setado para "Antes do cálculo da bolsa" e já tivermos uma bolsa no contrato com o campo "Aplicar desconto por antecipação" setado para "Depois do cálculo da bolsa" com ordem maior ou igual à bolsa que está sendo inserida ou alterada, o sistema exibirá a mensagem abaixo:
2. Tipo de Bolsa = "Somar Bolsas" ou "Aplicar somente a maior bolsa": Quando o contrato estiver setado com esse tipo de bolsa, não será permitido se ter uma bolsa com o campo "Aplicar desconto por antecipação" com valor diferente de alguma bolsa de contrato previamente cadastrada pelo usuário, ou seja, para esse tipo bolsa, todas as bolsas deverão ter o mesmo valor informado no campo "Aplicar desconto por antecipação". Caso seja informada uma bolsa inconsistente, será exibida a seguinte mensagem para o usuário:

ConcessaoBolsasFuturasConcessão de Bolsas FuturasConcessão de Bolsas Futuras

No cadastro de concessão de bolsas futuras teve a criação do campo “Aplicar desconto por antecipação”. Esse campo tem o objetivo de informar se o valor do desconto por antecipação será calculado antes ou depois do cálculo do valor da bolsa inserida no contrato via a concessão de bolsas futuras.

No assistente de concessão de bolsas futuras também teve a criação do campo “Aplicar desconto por antecipação”.

O campo “Aplicar desconto por antecipação” nas telas de cadastro de concessão de bolsas futuras e no assistente de concessão de bolsas futuras terá o preenchimento padrão por “Antes do cálculo da bolsa”. Esse valor poderá ser alterado pelo usuário conforme desejado. E também será alterado automaticamente pelo mesmo valor presente no campo “Aplicar desconto por antecipação” no cadastro de bolsa quando a bolsa for informada em ambas as telas.

Na inclusão de parcela para o contrato do aluno, caso o aluno tenha uma concessão de bolsas futuras que contempla nos dados informados na parcela. A bolsa será incluída no contrato do aluno onde o campo “Aplicar desconto por antecipação” da bolsa do aluno terá o mesmo valor do campo “Aplicar desconto por antecipação” presente na concessão de bolsas futuras.

GeracaoSimulacaoGeração de lançamentos / Simulação de valores de parcelasGeração de lançamentos / Simulação de valores de parcelas

**Geração de lançamentos / Simulação de valores de parcelas**

Para Bolsas com comportamentos “Somar Bolsas” e “Aplicar bolsas em cascata”. Se o contrato tiver esse comportamento (tipo de bolsas), poderemos ter bolsas com comportamentos distintos em relação ao desconto por antecipação, ou seja, com o desconto calculado “Depois do cálculo da bolsa” e bolsas com o desconto calculado “Antes do cálculo da bolsa” desde que não tenhamos uma bolsa B de ordem maior que uma bolsa A com o desconto por antecipação para a B sendo calculado como “Depois do cálculo da bolsa” e o desconto por antecipação para a bolsa A setado para “Antes do cálculo da bolsa”

Se duas bolsas no contrato possuem comportamentos distintos na aplicação do desconto por antecipação, a geração de lançamentos ou simulação de valores de parcelas, considerará, primeiramente, as bolsas cujo desconto seja calculado “Depois do cálculo da bolsa”.

**Exemplos**:

Somar Bolsas

Exemplo 1:

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 300,00  
- Valor líquido: R$ 200,00

Os valores de bolsas e de desconto por antecipação não foram influenciados porque o campo “Afeta base de cálculo” não está marcado.

Aplicar bolsas em cascata

Exemplo 1:

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Bolsa A: R$ 100,00  
- Valor do desconto por antecipação: 450,00  
- Bolsa B: R$ 90,00  
- Total de Bolsas aplicado: R$ 190,00  
- Valor líquido: R$ 360,00

Os valores de bolsas e de desconto por antecipação foram influenciados pela ordem de cálculo visto que, para o comportamento “Aplicar bolsas em cascata”, a base de cálculo das bolsas ou do cálculo do valor do desconto por antecipação sempre é influenciado pela ordem de cálculo dos itens (bolsas ou descontos). O campo “Afeta base de cálculo” não aparece no cadastro de bolsas em cascata porque, para esse tipo de comportamento, a base de cálculo dos itens sempre é afetada.

Para Bolsas com comportamento “Aplicar bolsas em cascata” e com dois ou mais itens de desconto por antecipação o educacional vai considerar o maior desconto por antecipação independente da data que for efetuada o pagamento ao calcular o valor da bolsa de todos os vencimentos.

Exemplos:

(Exemplo 1 – Descontos por antecipação antes do cálculo da bolsa)

- Parcela 1: R$ 1000,00  
- Bolsa (Cascada): 50%  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Desconto por antecipação no 1º vencimento (até dia 10): 10% (maior desconto)  
- Desconto por antecipação no 2º vencimento (até dia 15): 5%

=> Após geração da parcela 1, teremos os seguintes valores:  
- Desconto por antecipação (10%) = R$ 100,00  
- Bolsa (Cascata) (50%) = R$ 450,00  
- Valor líquido a pagar = R$ 450,00

- Desconto por antecipação (5%) = R$ 50,00  
- Bolsa (Cascata) (50%) = R$ 450,00  
- Valor líquido a pagar = R$ 500,00

**Como no cálculo dos valores do tipo cascata o educacional considera o maior desconto por antecipação independente da data que for efetuada o pagamento****. Neste caso, o valor da bolsa do segundo desconto por antecipação está considerando o maior desconto por antecipação que corresponde aos 10% do primeiro desconto.**

(Exemplo 2 – Descontos por antecipação depois do cálculo da bolsa)

- Parcela 1: R$ 1000,00  
- Bolsa (Cascada): 50%  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Desconto por antecipação no 1º vencimento (até dia 10): 10%   
- Desconto por antecipação no 2º vencimento (até dia 15): 5%

=> Após geração da parcela 1, teremos os seguintes valores:  
- Desconto por antecipação (10%) = R$ 50,00  
- Bolsa (Cascata) (50%) = R$ 500,00  
- Valor líquido a pagar = R$ 450,00

- Desconto por antecipação (5%) = R$ 25,00  
- Bolsa (Cascata) (50%) = R$ 500,00  
- Valor líquido a pagar = R$ 475,00

Aplicar somente a maior bolsa

Para Bolsas com comportamento “Aplicar Somente a Maior Bolsa”, todas as bolsas do contrato deverão ter o campo “Aplicar desconto por antecipação” com o mesmo valor, ou seja, ou todas as bolsas com o valor “Antes do cálculo da bolsa” ou todas as bolsas com o valor “Depois do cálculo da bolsa”

Exemplo 1:

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: Desmarcado

=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 200,00  
- Valor líquido: R$ 300,00

Os valores de bolsas e de desconto por antecipação não foram influenciados porque o campo “Afeta base de cálculo” não está marcado.

**O calculo de bolsa retroativa com desconto por antecipação terá o mesmo comportamento quando é incluído uma bolsa corrente no contrato**
