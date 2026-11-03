---
content_hash: 865ac7335b4bd8a5a8c934dc60cd60c75e15a00cebfab381e26aae4858d758e9
fetched_at: '2026-06-29T00:09:53.688743+00:00'
page_id: '440857942'
product: rm
source: tdn-rm
title: DT Cálculo Licença Maternidade 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440857942
version: 26
---

Tempo aproximado para leitura:**00 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Plataforma RH |
| Módulo: | Folha de Pagamento |
| Função: | Cálculo Licença Maternidade 13º Salário |
| Ticket: | 424322; 449641; 495565; 1113984 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FOPCALCULO01-4758 |
| Versões Afetadas | 12.1.22.137 ou superior  12.1.21.170 ou superior  12.1.20.421 ou superior  12.1.19.425 ou superior |

**02. SITUAÇÃO/REQUISITO**

Conforme orientação prevista na legislação, a empresa deve pagar o 13º integral para as funcionárias afastadas por licença maternidade. O valor de 13º salário proporcional aos dias de licença maternidade pagos no ano será deduzidos da GPS e/ou DCTFWeb de 13º salário do respectivo ano para que a Previdência Social possa reembolsar a empresa.

## **03. SOLUÇÃO**

Para atender a situação acima, foi criados os códigos de cálculos abaixo:

371 -  SEGUNDA PARCELA 13º LICENÇA MATERNIDADE PROVENTO

372 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE PROVENTO

373 - 13º RESCISÃO LICENÇA MATERNIDADE PROVENTO

374 - DIFERENÇA 13º RESCISÃO LIC. MATERNIDADE PROVENTO

390 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE JANEIRO

391 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE DISSÍDIO

414 - ADIANTAMENTO DE 13º LICENÇA MATERNIDADE

03.01 - CC 371 -  SEGUNDA PARCELA 13º LICENÇA MATERNIDADE PROVENTO

Este evento é do tipo provento  e valor, devendo ter as mesmas incidências do CC 102.

O sistema buscará o valor calculado pelo 13º Salário (CC 102) e dividirá pelo número de meses trabalhados no ano, em seguida dividirá por 30 e por fim multiplicará pela quantidade de dias de afastamento por Licença Maternidade no ano.

Após ser feito este cálculo, será recalculado o evento com o CC 102, reduzindo o valor original pelo valor encontrado neste evento.

No caso de médias, as mesmas serão rateadas conforme os dias de afastamentos, lançando as médias referente ao afastamento de licença maternidade juntamente com o evento de CC 371 e o restante conforme parametrizado no sindicato.

*Exemplo*:

Funcionário com Licença Maternidade retornando no dia 28 de Janeiro.

Dias de Licença Maternidade no Ano  = 28 dias

Salário 1000,00

* Calculo do 13º Salário sem média

CC 102 =  R$ 1000,00

**CC 371 = 1000,00 / 12 / 30 x 28 =  R$ 77,78**

**CC 102 = 1000,00 - 77,78 = R$ 922,22**

Cálculo do  13º Salário com média

CC 102 (evento de média) = 154,33

Valor referente ao período de afastamento = 154,33 / 12 / 30 x 28 = R$ 12,00

Valor pago juntamente com o evento de CC 102 = 154,33 - 12,00 = R$ 142,33

**Valor pago de 13º Salário de Licença Maternidade (CC371)  = 77,78 + 12,00 = R$ 89,78**

**Valor pago de 13º Salário (CC 102) = 922,22 + 142,33 = R$1064,55**

03.02 - CC 372 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE PROVENTO

Este é evento é do tipo provento e valor, devendo ter as mesmas incidências do CC 66, que é informado na aba '13º Salário | Eventos para pagamento de média 13º Salário na segunda Parcela' no cadastro de sindicatos.

O sistema utilizará este código de cálculo para lançar a diferença relativa ao 13º salário de Licença Maternidade (CC 371), somente no mês de Dezembro quando houver diferença com dissídio não marcado.

03.03 - CC 373 - 13º RESCISÃO LICENÇA MATERNIDADE PROVENTO

Evento provento do tipo valor, devendo ter as mesmas incidências do evento de CC 48.

O sistema buscará o valor calculado do 13º Salário Rescisão (CC 48), dividirá pelo número de meses trabalhados no ano, em seguida dividirá por 30 e por fim multiplicará pelo número de dias de afastamento por Licença Maternidade no ano.

Após feito esse cálculo, será calculado novamente o evento de CC 48, reduzindo o valor original pelo valor calculado no CC 373.

O cálculo é feito da mesma forma que o exemplo acima com o CC 102, porém será considerado o valor evento de CC 48 para encontrar o valor do evento de CC 373.

03.04 - CC 374 - DIFERENÇA 13º RESCISÃO LIC. MATERNIDADE PROVENTO

Este é evento é do tipo provento e valor, devendo ter as mesmas incidências do CC 97.

O sistema utilizará este código de cálculo para lançar a diferença relativa ao 13º salário de Licença Maternidade (CC 373).

03.05 - CC 390 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE JANEIRO

Este evento é do tipo provento, valor, devendo ter as mesmas incidência que o código de cálculo 66, calculado em Janeiro, ou seja, não devendo incidir em INSS 13º Salário.

O sistema utilizará este código de cálculo para lançar a diferença relativa ao 13º salário de Licença Maternidade (CC 371), somente no mês de Janeiro quando houver diferença com dissídio não marcado.

03.06 - CC 391 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE DISSÍDIO

Este evento é do tipo provento, valor, devendo ter as mesmas incidência que o código de cálculo 180.

O sistema utilizará este código de cálculo para lançar a diferença relativa ao 13º salário de Licença Maternidade (CC 371), somente quando houver diferença com dissídio sim marcado.

03.07-CC 414 - ADIANTAMENTO DE 13º LICENÇA MATERNIDADE

Evento tipo Desconto,valor. 

Este evento será calculado em Dezembro quando uma rescisão for calculada posterior ao lançamento da segunda parcela de 13º salário, para funcionários com afastamento por licença maternidade.  

Este código de cálculo conterá somente o valor que foi pago no evento com código de cálculo 371 (Segunda parcela de 13º Licença Maternidade Provento  ) separando do restante do 13º.

**Exemplo:**

 Dezembro:

Período 1: Pagamento da segunda Parcela de 13º .

**CC 371 ( Segunda parcela 13º Licença Maternidade Provento ) =544,00**

**CC102 ( 2º Parcela de 13º Salario)=1088,00**

Período 2: Rescisão

**CC51(Adiantamento 2º parcela 13º Salario )=1088,00**

**CC414(Adiantamento de 13º Licença Maternidade)=544,00**

## **04. DEMAIS INFORMAÇÕES**

Após estas mudanças, os eventos de CC 322 e CC 324, assim como seus respectivos eventos de diferença (CC 323 e CC 325) não serão mais lançados de forma automática no cálculo de 13º salário para funcionário que teve dias de afastamento no ano corrente. Porém ainda é possível fazer o lançamento dos mesmos de forma manual e os mesmos continuam sendo considerados nos encargos, como INSS, SEFIP, Folha Analítica, etc.

Caso já tenha feito o cálculo do 13º salário na competência atual e o sistema ainda esteja lançado os eventos de base, é recomendado fortemente que sejam cancelados os eventos de base do movimento e feito o lançamento do 13º Salário novamente após a atualização do sistema. Desta forma os novos eventos serão lançados, evitando inconsistências no envio das informações para o eSocial.

Para cálculos de diferença que tenha sido lançados os eventos de base de 13º Salário de Licença Maternidade nos envelopes originais, o sistema irá calcular considerando os novos códigos de cálculo.

13 Salário Maternidade x DCTFWeb

Importante ressaltar que, se os proventos de 13º Salário Maternidade não forem lançados no movimento de 13º Salário, poderá gerar inconsistência no valor pago na DCTFWeb, pois os mesmos não serão deduzidos na parte paga pela empresa devida do INSS.

**É necessário que seja criado um evento com os códigos de cálculo acima e Rubrica do eSocial relacionados a esta verba, sendo também necessário enviar o evento S-1010 referente a esta rubrica caso ainda não tenha enviado. IMPORTANTE!**
