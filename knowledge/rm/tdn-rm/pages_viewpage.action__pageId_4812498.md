---
content_hash: 4a3d7b0ee4b9b4fdc1246dedb2269fbfe432cd0e732bd1f0e506bc269d9f4757
fetched_at: '2026-06-29T00:10:18.539359+00:00'
page_id: '4812498'
product: rm
source: tdn-rm
title: Geração da GPS e SEFIP de  13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812498
version: 4
---

BLOCK

Geração da GPS e SEFIP de 13º Salário

FAQ: **Geração da GPS e SEFIP de 13º Salário**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.0 |

Avaliação

Este documento irá auxiliá-lo na geração das Guias de 13º Salário.

Causa

* Geração da Guia de INSS de 13º Salário (GPS)
* Geração do SEFIP de 13º Salário

Solução

### Guia de INSS Competência 13

Quando é processado o módulo de geração da Guia de INSS da competência 13 o sistema considera para a base de INSS dessa guia os eventos de 13º salário que foram pagos na competência de dezembro com código de cálculo 102, independentemente de sua situação. Para funcionários demitidos os valores de 13º pagos na rescisão aparecerão na guia normal.

##### Nesta Guia não são recolhidos os valores de autônomos nem valores da folha normal.

##### Cadastro do Funcionário e Ficha Financeira

O sistema verifica no cadastro do funcionário os afastamentos para contagem dos avos de 13º. Caso o funcionário não tenha 15 dias de trabalho no mês ele não terá direito ao avo (no caso de afastamento por acidente de trabalho e doença ocupacional ele não perde direito aos avos). Os 15 primeiros dias de afastamento são considerados como dias trabalhados, ou seja, o afastamento começa a ser considerado a partir do 16º dia.

O sistema verifica também na ficha financeira a existência de faltas (Evento com CC 8). Caso ele tenha mais de 15 faltas no mês ele perde direito ao avo de 13º salário referente aquele mês. Nos meses de admissão e demissão esse cálculo é proporcional.

**Contagem dos Avos**

Cada mês onde se tenha trabalhado 15 ou mais dias é considerado como 1 avo de 13º.

- Obs.: Para funcionárias que tiveram dias de afastamento por licença maternidade durante o ano o sistema irá calcular o valor normalmente (como é calculado para os demais funcionários), porém na guia de INSS e no SEFIP os valores referente ao valor do 13º salário pago pela previdência serão calculados da seguinte forma:

**Soma dos eventos de CC 102 (ou CC48 caso venha a ser rescisão) / nº de avos que estão sendo pagos / 30 \* Número de dias de afastamento dentro do ano.**

- Estes valores sobre os dias de afastamento por licença maternidade não aparecerão na

movimentação e nem na folha analítica, para que seja impresso na folha analítica deverá ser criado uma fórmula.

### Dedução de Salário Maternidade, sobre o 13º Salário, na Guia de INSS

Através da Lei 10.710 de 05/08/2003, Art. 2º, o valor de Licença Maternidade passou a ser pago pela empresa.

Deve-se observar que em alguns casos o sistema estará deduzindo um valor de salário maternidade na Guia de INSS em meses onde não existe nenhuma funcionária afastada por licença Maternidade, no mês de dezembro isso será comum. Este valor é devido no caso do pagamento de licença maternidade ou quando da demissão da funcionária, onde a empresa deve deduzir o valor do 13º salário rescisão proporcional aos dias de afastamento.

**Exemplo:**

A funcionária esteve de afastada por Licença Maternidade até o dia 20/01/2006. Desta maneira a empresa é responsável pelo pagamento de 13º salário referente aos dias de afastamento por motivo de Licença maternidade no ano corrente o que acarretaria o seguinte calculo:

(CC 102 + CC 48) / número de avos de direito /30 \* Número de dias de afastamento por Licença Maternidade no ano corrente.

Para que este valor apareça na folha analítica, deverá ser criada a fórmula abaixo e informá-la na Folha Analítica.

**Para o RM Labore**

Os eventos 0048, 0088, 0089 são eventos de 13º salário rescisão com CC 48 e 0129, 0133 e 0134 são eventos de CC 102.

DECL DIASAFASTADO, X;

SE SETVAR (DIASAFASTADO,DIASAFT (MTDATA (1,1,ANO), MTDATA (1,1,ANO+1)-1,'E')) >0 ENTAO

SE SFUNC='D' ENTAO

SE DIADT (DTD) <15 ENTAO SETVAR (X,1)

FIMSE

FIMSE;

(MV(MES,ANO,'0048') +

MV(MES,ANO,'0088') +

MV(MES,ANO,'0089') +

MV(MES,ANO,'0129') +

MV(MES,ANO,'0133') +

MV(MES,ANO,'0134')) / (NROAVOS13- X) /30 \* DIASAFASTADO

SENAO

0

FIMSE

Quando este valor de dedução não estiver sendo descontado na GPS/Guia de INSS acesse o módulo “Cadastro | Cálculos | Valores fixos”, localize o valor fixo com finalidade 10 (Limite para desconto de Salário Maternidade em GRPS) e informe neste o valor de 999999,00. Verifique também a sua vigência.

**Informações necessárias para a geração das Guias**

É necessário que exista a movimentação de 13º Salário no envelope do funcionário do evento com Código de Cálculo 102.

**Obs.: Os Valores abaixo são fictícios, sendo necessário que as tabelas de INSS e IRRF além dos valores fixos estejam devidamente atualizadas**.

[![clip_image002](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp15UZWXqI/AAAAAAAAC18/uiegoqlzMpY/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp140FcZWI/AAAAAAAAC14/eVAgx6Xs58Y/s1600-h/clip_image002%5B4%5D.jpg)

[![clip_image004](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp16bqI0UI/AAAAAAAAC2I/IBoG1H_vCc4/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp16HjvZ1I/AAAAAAAAC2A/rafANLDVgTo/s1600-h/clip_image004%5B4%5D.jpg)

**Guia de INSS de 13º Salário (GPS-13)**

**Acesse:** Relatórios | Guia de INSS

**1º -** Na tela de geração da Guia de INSS deve ser marcada a opção Guia 13°.

[![clip_image006](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp17ZDWKlI/AAAAAAAAC2Q/DrT4OL4aBxc/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp17GA2hPI/AAAAAAAAC2M/uwh6UHbc70w/s1600-h/clip_image006%5B4%5D.jpg)

Em seguida Clicar em **“Calcular Valores”**.

[![clip_image008](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp18vO7WxI/AAAAAAAAC2Y/U5RWlFbS9KA/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp18QcDyZI/AAAAAAAAC2U/tpgRgYD7M4U/s1600-h/clip_image008%5B4%5D.jpg)

[![clip_image010](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp1-DPr6wI/AAAAAAAAC2g/yeCWXSbBze8/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp19tSd_nI/AAAAAAAAC2c/hzM1LajwgT0/s1600-h/clip_image010%5B4%5D.jpg)

Uma opção que auxilia bastante a conferência dos valores apurados é a opção **“Gerar Memória da Guia”**:

[![clip_image012](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp1_KhJdsI/AAAAAAAAC2o/FvAL-N-KBls/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp1-3JhNCI/AAAAAAAAC2k/HjvX8oDfWjc/s1600-h/clip_image012%5B4%5D.jpg)

**2º -** Após marcar essa opção e tendo o cálculo dos valores já realizado podemos então fazer a geração.

[![clip_image014](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp1_3thWMI/AAAAAAAAC2w/8XppWQPrWRo/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp1_lJQK0I/AAAAAAAAC2s/_1cyCyEr32w/s1600-h/clip_image014%5B4%5D.jpg)

Finalizada a geração podemos voltar à tela emissão e clicar para visualizar a memória do cálculo.

[![clip_image016](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp2AsFSBYI/AAAAAAAAC24/zLkS5zzrPA0/clip_image016_thumb%5B2%5D.jpg?imgmax=800 "clip_image016")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp2ACN6sPI/AAAAAAAAC20/cytR5s2sjp8/s1600-h/clip_image016%5B5%5D.jpg)

Nela teremos as informações detalhadas:

[![clip_image018](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp2BhH2sqI/AAAAAAAAC3A/0hfnsbEVscI/clip_image018_thumb%5B2%5D.jpg?imgmax=800 "clip_image018")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2BGOjwbI/AAAAAAAAC28/5OkpZYQZyr8/s1600-h/clip_image018%5B5%5D.jpg)

Valor da Guia apurada: **R$ 1991,34**.

**Como o sistema chegou nesse valor:**

**1º** - A **base** obtida foi de **R$ 5609,51.**

**2º -** O valor de **Segurados** é referente ao desconto do INSS sobre o 13º Salário, no caso **R$ 375,81**.

**3º -** **A parte da empresa** é composta pelo Percentual de Autônomos, no caso 20%, e do Percentual de acidente de trabalho que fica cadastrado no cadastro da seção do funcionário:

**Base \* Autônomos % = Autônomos**

R$ 5609,51 \* 20% = **R$** **1121,90**

[![clip_image020](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp2CfqkvCI/AAAAAAAAC3I/rMUaz_FI2fY/clip_image020_thumb%5B2%5D.jpg?imgmax=800 "clip_image020")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2B4bMEPI/AAAAAAAAC3E/poH1mGwlCBA/s1600-h/clip_image020%5B5%5D.jpg)

**Base \* Acidente de Trabalho % = Acidente de Trabalho**

R$ 5609,51 \* 3% = **R$ 168,28**

**4º -** O **percentual de terceiros** também fica cadastrado dentro da seção do funcionário na aba Dados para INSS à direita do Percentual de Acidente de Trabalho.

[![clip_image022](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp2DBv07AI/AAAAAAAAC3Q/gF-WN4iKMls/clip_image022_thumb%5B6%5D.jpg?imgmax=800 "clip_image022")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2C9fED6I/AAAAAAAAC3M/OQMpPwyC8vA/s1600-h/clip_image022%5B9%5D.jpg)

**Base \* Terceiros % = Terceiros**

R$ 5609,51 \* 5,8% = **R$ 325,35**

**5º -** O **Liquido** apurado tem neste exemplo o mesmo valor final da guia, pois não tem correção, juros ou multa.

**Total da Guia:**

**(Segurados + Parte Empresa - Deduções) + Terceiros**

(R$ 375,81 + (R$ 1121,90 + R$ 168,28) – R$ 0,00) + R$ 325,35 = **R$ 1991,34**

É possível também no ato da geração da GPS-13 realizar o Lançamento Financeiro de INSS de 13º Salário.

[![clip_image024](http://lh3.ggpht.com/_G7KXZLoZDsY/TNp2EMcoIOI/AAAAAAAAC3Y/JKz6SDGRMHw/clip_image024_thumb%5B1%5D.jpg?imgmax=800 "clip_image024")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2DinBPAI/AAAAAAAAC3U/LwUQu-ARxCU/s1600-h/clip_image024%5B4%5D.jpg)

Na parametrização do Lançamento Financeiro **(Cadastro | Financeiro | Parametrização dos Lançamentos Financeiros)** o tipo definido deverá ser o **11 – INSS 13º a pagar**.

[![clip_image026](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2FR-SpSI/AAAAAAAAC3g/AQxdM0IMPco/clip_image026_thumb%5B2%5D.jpg?imgmax=800 "clip_image026")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2E9woyMI/AAAAAAAAC3c/102HRh84PUs/s1600-h/clip_image026%5B5%5D.jpg)

**SEFIP de 13º Salário (SEFIP-13)**

**Acesse:** Relatórios | Sefip | Sefip .Net

Na tela de geração do arquivo SEFIP deve ser observado:

**1º -** A competência tem que ser **12**, o parâmetro Sefip para 13º Salário deve estar **marcado**, a Modalidade deve ser **1-Declaração ao FGTS e a Previdência**, pois, a sefip de 13º é apenas declaratória e no campo Recolhimento do FGTS deve ser informado **0 – Em Branco**, pois o FGTS somente será recolhido na SEFIP emitida no final da competência, a SEFIP-13 é apenas para declarar as informações recolhidas na GPS-13.

[![clip_image028](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp2GtHXlxI/AAAAAAAAC3o/YOuOKUkKwUU/clip_image028_thumb%5B4%5D.jpg?imgmax=800 "clip_image028")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp2GC_mU_I/AAAAAAAAC3k/N_rXlHbS36Q/s1600-h/clip_image028%5B7%5D.jpg)

**2º -** Após geração do arquivo o mesmo deverá ser importado no programa da SEFIP.

[![clip_image030](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp2H2VzMXI/AAAAAAAAC3w/lrP7Veenbmk/clip_image030_thumb%5B1%5D.jpg?imgmax=800 "clip_image030")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp2HMEOlOI/AAAAAAAAC3s/S_QsSa_189g/s1600-h/clip_image030%5B4%5D.jpg)

Note que nas Remunerações, o campo 13º Salário sairá com valor R$ 0,00, pois conforme informado anteriormente a SEFIP-13 é declaratória, ou seja, apenas haverá valor informado no campo **“Referente à Competência do Movimento”**.

**3º -** Para realizar a geração do Lançamento Financeiro de FGTS 13º é necessário que a rotina seja executada através do menu **Rotinas | Geração de Lançamentos Financeiros**.

O tipo do lançamento é o **10 – FGTS 13º**.

[![clip_image032](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp2JzkWS3I/AAAAAAAAC34/WgOBVSStjwM/clip_image032_thumb%5B1%5D.jpg?imgmax=800 "clip_image032")](http://lh6.ggpht.com/_G7KXZLoZDsY/TNp2Jc3mJ3I/AAAAAAAAC30/Nb0KOrQvThs/s1600-h/clip_image032%5B4%5D.jpg)

Durante a validação no arquivo do SEFIP um erro muito comum em acontecer é o erro:

"**300548** - Base de cálculo 13º salário referente à competência do movimento deve ser informada para trabalhadores com movimentação definitiva."

**O que fazer nesse caso?**

**[![clip_image034](http://lh4.ggpht.com/_G7KXZLoZDsY/TNp2LeXYsdI/AAAAAAAAC4A/cDONz_lQRu0/clip_image034_thumb%5B1%5D.jpg?imgmax=800 "clip_image034")](http://lh5.ggpht.com/_G7KXZLoZDsY/TNp2KdVd5RI/AAAAAAAAC38/WfLGG78-LNE/s1600-h/clip_image034%5B4%5D.jpg)**

O campo **”Referente à Competência do movimento”** deve ser preenchido com valores reais (que realmente foram pagos aos funcionários) quando ocorrer diferença de 13º salário na competência 12 ou no caso de rescisões em qualquer competência. Nos casos de rescisões deve ser considerado que se na competência 12 (dezembro) foi pago a 2º parcela de 13º salário até o dia 20 e o INSS dessa verba já recolhida em GPS e após este pagamento houve a demissão do funcionário o campo deve vir em branco. No caso de ocorrer a demissão sem a ocorrência do pagamento da 2ª parcela no referido mês o campo deve vir preenchido com o valor da base de INSS de 13º na rescisão.

O campo **“Referente à GPS da competência 13”** deve ser preenchido com a base de INSS de 13º salário pago na segunda parcela quando ocorrer diferença de 13º salário na competência 12 ou quando o valor pago em rescisão for maior do que o valor pago na 2º Parcela.

**Exemplos**:

**EXEMPLO 1**

1º pagamento:

- 2ª Parcela 2000,00

-INSS  220,00

2º pagamento

- Diferença de 13º salário 200,00

-INSS 13º sobre a diferença 22,00

O campo **“Referente à Competência do movimento”** deve ser preenchido com: 200,00

O campo **“Referente à GPS da competência 13”** deve ser preenchido com: 2000,00

**EXEMPLO 2**

**1º pagamento:**

- 2ª Parcela 2000,00

-INSS  220,00

**2º pagamento:**

- 13º salário rescisão 2200,00

-INSS 13º sobre a diferença 22,00

- Desconto de 2º parcela já creditada 2000,00

O campo **“Referente à Competência do movimento”** deve ser preenchido com: 200,00

O campo **“Referente à GPS da competência 13”** deve ser preenchido com: 2000,00

**EXEMPLO 3**

**1º pagamento:**

- 2ª Parcela 2000,00

-INSS  220,00

**2º pagamento:**

- 13º salário rescisão 2000,00

- Desconto de 2º parcela já creditada 2000,00

O campo **“Referente à Competência do movimento”** deve ser preenchido com: 0,01 (um centavo)

O campo **“Referente à GPS da competência 13”** deve ser preenchido com: 0

**EXEMPLO 4**

**1º pagamento:**

- 13º salário rescisão 2200,00

-INSS 13º 242,00

O campo **“Referente à Competência do movimento”** deve ser preenchido com: 2200,00

O campo **“Referente à GPS da competência 13”** deve ser preenchido com: 0

**EXEMPLO 5**

**1º pagamento:**

- 2ª Parcela 2000,00

-INSS  220,00

**2º pagamento:**

- 13º salário rescisão 1900,00

- Restituição de INSS 13º 10,00

- Desconto de 2º parcela já creditada 2000,00

O campo **“Referente à Competência do movimento”** deve ser preenchido com: 0,01 (um centavo)

O campo **“Referente à GPS da competência 13”** deve ser preenchido com: 0

O valor pago a maior deve ser compensado.
