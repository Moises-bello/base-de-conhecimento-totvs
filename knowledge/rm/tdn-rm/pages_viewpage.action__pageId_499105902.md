---
content_hash: aaec459f8abb1e04c5210d712367dbb26b3b93de5f0b5bc087be61efc5980996
fetched_at: '2026-06-29T00:10:22.782589+00:00'
page_id: '499105902'
product: rm
source: tdn-rm
title: 'S-1200 e S-1210: Autônomos Cadastrados no Financeiro - Pagamento Parcelado'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499105902
version: 8
---

false

**A partir das Versões:**

* 12.1.23.000
* 12.1.24.000
* 12.1.25.000

# Objetivo:

---

O objetivo deste documento é trazer informações de como enviar os eventos S-1200 (Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social) e S-1210 (Pagamentos de Rendimentos do Trabalho) para transportador autônomo - Autônomos cadastrados no Financeiro quando é feito pagamento de forma parcelada.

---

Passos para o envio das informações para o eSocial:

 No cliente fornecedor preencher os campos:

**Observação: a partir da versão 12.1.25.00, será disponibilizado o anexo do eSocial, que irá substituir o item Integrações | eSocial**

No lançamento do cliente fornecedor deve existir uma baixa parcial para que no S-1210 a tag indPgtoTt e os demais campos do grupo infoPgtoParc sejam considerados no XML.

# Exemplo 1: Autônomos com categorias diferentes de 711 ou 712 cadastrados no Totvs Gestão Financeira

Existe um lançamento no valor total de 50.000,00. Para o mês corrente, existe apenas uma baixa no valor de 25.000,00.

Nesse mês será gerado um S-1200 com o valor total do lançamento:

O evento S-1210 será gerado com o valor da baixa realizada dentro do mês. 

Obs.: 

* O “Valor da baixa” será levado para a tag vrLiq
* O “Valor Original” será levado para o valor da rubrica informada como pagamento de autônomo no parametrizador do eSocial no Folha de Pagamento.
* O valor total dos devidos tributos(INSS, IRRF, ISS, SEST/SENAT) serão gerados no XML da primeira baixa.

Nesse exemplo, no mês seguinte ocorreu a baixa do valor restante do lançamento:

Nesse mês será gerado apenas o S-1210 com o valor da Baixa. Não serão informados os valores dos tributos, pois esses foram gerados apenas na primeira baixa:

# Exemplo 2: Autônomos com categorias iguais a 711 ou 712 cadastrados no Totvs Gestão Financeira

Para essas categorias, o eSocial pede que sejam enviadas as bases de IRRF e INSS separadamente do valor do frete.

Leia esse FAQ para mais detalhes: <http://tdn.totvs.com/pages/viewpage.action?pageId=463820907>

Dessa forma, no pagamento parcelado os valores lançados para os eventos informados no Parametrizador I eSocial I Configurações Gerais I Autônomos e Externos 2/2, serão proporcionalizados conforme o percentual informado para a base de INSS e IRRF.

Exemplo:

Parametrização:

Categoria do autônomo: 712 - Contribuinte individual - Transportador autônomo de carga

Lançamento:

Nesse lançamento, observe que a base para IRRF será de 10% do valor total do lançamento.

A base de INSS do Empregado será 20% do valor total do lançamento:

Nesse exemplo existe uma baixa no valor de 25.000,00 no mês do lançamento:

No S-1200 o valor do lançamento de 50.000,00 é dividido conforme o percentual das bases de INSS e IRRF.

Observações: 

* Uma vez informado que a base de IRRF é 10%, o sistema leva no XML 10% do valor do lançamento no evento de código de cálculo 400 -REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM IRRF informado no parametrizador. No exemplo abaixo, o valor é 5.000,00 no evento 0400.
* Sendo informado um percentual de 20% para a base de INSS, o sistema leva no XML 20% do valor do lançamento no evento de código de cálculo 401 - REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM INSS informado no parametrizador. No exemplo abaixo, o valor é 10.000,00 no evento 0401.
* A diferença entre o valor da baixa, e a base de INSS e IRRF é lançada no evento de código de cálculo 399 - REMUNERAÇÃO FRETE AUTÔNOMO.

No evento S-1210 o valor da tag “idPgtoTt” irá como “N”, e o “vrLiq” será o valor da baixa para a data de pagamento desse período de referência.

Para esse indicativo de pagamento, todos eventos relacionados no S-1200 devem ser informados no S-1210. Para esses tipos de autônomos(711 e 712), será feito uma proporcionalização em relação ao valor original da baixa e percentual das bases de INSS e IRRF.

Nesse exemplo foram consideradas as bases de 10% para IRRF e 20% de INSS.

Cálculo:

Valor original da baixa

Rubrica 0401 = 20% (Base de INSS) de 26.195,46 (Valor original da baixa)

Rubrica 0401 = 5.239,09

Rubrica 0400 = 10% (Base de IRRF) de 26.195,46 (Valor original da baixa)

Rubrica 0400 = 2.619,55

Rubrica 0399 = 26.195,46 (Valor original da baixa) - 5.239,09 (Valor da Rubrica 0401) - 2.619,55 (Valor da Rubrica 0400)

Rubrica 0399 = 18.336,82  

 

**Observação:** Os tributos calculados (INSS, IRRF, ISS, SEST/SENAT) sempre serão levados no XML correspondente à primeira baixa do lançamento.
