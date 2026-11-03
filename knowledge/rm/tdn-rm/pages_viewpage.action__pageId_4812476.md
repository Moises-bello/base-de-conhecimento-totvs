---
content_hash: 6d90b1f8e83eb15218f469bd8ddb19fc2a2d2027e5a8fe1b16ac865098f34909
fetched_at: '2026-06-29T00:10:18.510763+00:00'
page_id: '4812476'
product: rm
source: tdn-rm
title: Cálculo e Lançamento do 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812476
version: 13
---

BLOCK

Cálculo e Lançamento do 13º Salário

FAQ: **Cálculo e Lançamento do 13º Salário**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.0 |

Avaliação

Este documento visa demonstrar o cálculo e lançamento do 13º salário.

Solução

### Parametrização - 13º Salário - Com Média

**PREPARAÇÃO DO SISTEMA**

Cadastro de Eventos:

**1º Passo:** Módulo "Cadastro | Eventos"

- Deverá existir na base de dados eventos cadastrados com os seguintes códigos de cálculo:

CC09 - Evento 1ª Parcela de 13º Salário

CC35 - Adiantamento 13º Salário

CC49 - IRRF 13º Salário

CC58 - Dedutível IRRF 13º Salário

CC66 - Diferença de 13º Salário

CC83 - Base de INSS 13º Salário Outro Emprego

CC101 - 13º Salário Pago pela Previdência

CC102 - 2ª Parcela de 13º Salário

CC103 - INSS 2ª parcela 13º Salário

CC106 - IRRF 13º Calculado pelo Usuário

CC144 - INSS 13º Outro Emprego

CC171 - Valor do INSS Descontado pela Previdência

CC172 - Valor do IRRF Descontado pela Previdência

Cadastro/Sindicatos:

Deverá ser definida neste cadastro a forma de cálculo para férias, 13º salário e aviso prévio, que poderá ser sem média, com média por valor ou por hora. Deveremos também informar os eventos dos grupos para que as médias sejam discriminadas no envelope dos demais eventos de 13º Salário e definir o período de cálculo das médias.

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3CkJvZfI/AAAAAAAAEHc/OFE8-iGmSZ4/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3BQYBUWI/AAAAAAAAEHY/mD6aco5i_j4/s1600-h/clip_image002%5B4%5D.jpg)

**1º Passo:** Devemos cadastrar os eventos para cálculo das médias, que deverão ter o mesmo código de cálculo do grupo 0 de 13º Salário (provento, Valor e C.C. 102).

**Exemplo:**

Eventos a serem cadastrados para cadastro na pasta 13º Salário/ Subpasta "Eventos para pagamento de 2ª parcela de 13º Sal." do Sindicato.

**Grupo 0:**

Pagamento: CC 102 - 2ª parcela de 13º salário

Diferença: CC 66 - Dif. 2ª parcela de 13º salário

Evento para diferença por dissídio: CC 180 Dif. 13º Salário por dissídio

**Grupo 1:**

Pagamento: CC 102 - Média de H. Extra 13º salário 2ª parcela

Diferença: CC 66 - Dif. média de H. Extra 13º salário 2ª parcela

Evento para diferença por dissídio: CC 180 Dif. média H.Extra 13º Salário p/ dissídio

**Grupo 2:**

Pagamento: CC102 - Média de Comissão 13º salário 2ª parcela

Diferença: CC 66 - Dif. média de Comissão 13º salário 2ª parcela

Evento para diferença por dissídio: CC 180 Dif. média Comissão 13º Salário p/ dissídio

[![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3EVx8osI/AAAAAAAAEHk/AWwAd3Opgl8/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3DT7pM6I/AAAAAAAAEHg/MDibwlxiChA/s1600-h/clip_image004%5B4%5D.jpg)

**Obs.:** A parametrização acima é fictícia e deverá consultar o sindicato dos empregados para validação da mesma. Deverão estar obrigatoriamente informados:

No **GRUPO 0 (zero) de 13º Salário**, o evento com código de cálculo **102**.

No **GRUPO 0 (zero) de Aviso Prévio**, o evento com código de cálculo **62**.

No **GRUPO 0 (zero) de Férias**, o evento com código de cálculo **38**.

No **GRUPO 0 (zero) de 13º Rescisão**, o evento com código de cálculo **48**.

### Parâmetros de 13º Salário

**Opções/Parâmetros/RM Labore/Pasta Parâmetros 13º Salário:**

Determinaremos neste módulo os parâmetros para cálculo do 13º salário.

Códigos Fixos no 13º Salário: Esta pasta serve para lançar Códigos fixos no 13º salário do funcionário. É preciso marcar quais os Tipos de Códigos Fixos que deverão ser lançados, estes códigos fixos devem ser cadastrados previamente na Tabela Dinâmica INT42. Para efetuar esta operação é preciso marcar o código fixo nesta pasta e também cadastrar o evento marcando o código fixo em CADASTROS | FUNCIONÁRIOS | PASTA BASE DE CÁLCULO | CÓDIGOS FIXOS.

[![clip_image006](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3FnTgpyI/AAAAAAAAEHs/UDXObmD8D5M/clip_image006_thumb%5B1%5D.jpg?imgmax=800 "clip_image006")](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3EzX2K0I/AAAAAAAAEHo/x00lIAH0ZXc/s1600-h/clip_image006%5B4%5D.jpg)

Fórmulas adicionais p/a base 13º: Informa a referência das fórmulas cujo resultado será adicionado a base de cálculo do 13º na segunda parcela.

[![clip_image008](http://lh3.ggpht.com/_G7KXZLoZDsY/TO_3Hq9NukI/AAAAAAAAEH0/g6IMDsrjAlQ/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3GR2tKOI/AAAAAAAAEHw/t0gXPquxUSs/s1600-h/clip_image008%5B4%5D.jpg)

Eventos Adicionais Globais**:** Poderão ser informados os eventos adicionais globais para 13º Salário que serão lançados juntamente com o cálculo do mesmo.

[![clip_image010](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3JqTHWDI/AAAAAAAAEH8/9c1qR5XP6oA/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh4.ggpht.com/_G7KXZLoZDsY/TO_3I0N9plI/AAAAAAAAEH4/Td9fHgTHfsM/s1600-h/clip_image010%5B4%5D.jpg)

### Processamento - 1ª Parcela de 13º Salário (Automático)

**Movimento/Folha de Pagamento/Lançamento Automático/13º Salário**

Tipo de Lançamento:

- **Primeira parcela:** Se a empresa está processando é a primeira parcela

- **Ajustar primeira parcela:** Este campo serve para quem já recebeu a primeira parcela antecipada. Se o salário do funcionário teve um reajuste após adiantamento da 1ª parcela, caso a empresa desejar pagar a diferença desta deverá confirmar este campo.

Este campo ficará marcado como padrão, caso a primeira parcela esteja sendo lançada.

### 1ª Parcela com Média discriminada

**1º Passo:** Cadastrar a seguinte fórmula em "Cadastro | Fórmulas"

**Código A0020**

**Título :** Média 13º na 1ª Parcela

**Texto:** CALCMED(2) / 2

**2º Passo:** Cadastrar o seguinte evento em "Cadastro | Eventos"

Código:

Provento, Valor, com Código de Cálculo 9, incide FGTS, informar a fórmula criada no passo 1.

[![clip_image012](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3LYCQlWI/AAAAAAAAEIE/eRD8xNB97ws/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh4.ggpht.com/_G7KXZLoZDsY/TO_3K1olkUI/AAAAAAAAEIA/dgqJbeqi78A/s1600-h/clip_image012%5B4%5D.jpg)

[![clip_image014](http://lh4.ggpht.com/_G7KXZLoZDsY/TO_3Nk7KDAI/AAAAAAAAEIM/yh1VdaHAbwg/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3MUVdscI/AAAAAAAAEII/QLGbu5woOFY/s1600-h/clip_image014%5B4%5D.jpg)

**3º Passo:** Acesse o módulo "Cadastro | Sindicatos", pasta "13º Salário". Desmarque a opção "Paga média na 1ª Parcela".

[![clip_image016](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3Pb4YQYI/AAAAAAAAEIU/9iH8GBJkhxo/clip_image016_thumb%5B1%5D.jpg?imgmax=800 "clip_image016")](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3OVhcrnI/AAAAAAAAEIQ/sVkaGwQJHos/s1600-h/clip_image016%5B4%5D.jpg)

**4º Passo:** Execute o pagamento da primeira parcela através do módulo "Movimento | Folha de Pagamento | Lançamentos Automáticos | Décimo Terceiro Salário".

**5º Passo:** Acessar o módulo "Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos" e criar um grupo de eventos informando o evento criado no passo 2.

[![clip_image018](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3QmBjf5I/AAAAAAAAEIc/dlTKvxgzmeo/clip_image018_thumb%5B1%5D.jpg?imgmax=800 "clip_image018")](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3P4DqB6I/AAAAAAAAEIY/dBVIy_-neGk/s1600-h/clip_image018%5B4%5D.jpg)

[![clip_image020](http://lh3.ggpht.com/_G7KXZLoZDsY/TO_3RuWFYRI/AAAAAAAAEIk/zUVYd4oEpOI/clip_image020_thumb%5B1%5D.jpg?imgmax=800 "clip_image020")](http://lh4.ggpht.com/_G7KXZLoZDsY/TO_3RNZs7AI/AAAAAAAAEIg/pZ5UeAmadKA/s1600-h/clip_image020%5B4%5D.jpg)

**6º Passo:** Lance o Grupo de Eventos.

### Pagamento de 13º Salário integralmente em meses anteriores a Dezembro (Com discriminação da média)

Para o pagamento da 2ª parcela antecipadamente, deve-se observar que os encargos de INSS e IRRF serão recolhidos para os órgãos competentes **apenas no mês de Dezembro** (mês da quitação). Isso se deve ao fato de que o pagamento ocorrido em novembro ou em outros meses anteriores ao mês de dezembro são antecipações (adiantamento). VEJA NOTA PRESENTE NO FINAL DO ROTEIRO.

**PREPARAÇÃO DO SISTEMA**

**Obs.:** Para esse lançamento a Preparação do Sistema especificada nas páginas 2,3,4 e 5 devem ser as mesmas.

Cadastrar as fórmulas Básicas para o cálculo:

**Código:** CHAPA

**Título:** Chapa

**Texto:** Chapa

**Código:** ANO

**Título:** Ano

**Texto:** Ano

**Código:** MES

**Título:** Mês de Competência

**Texto:** MES

**Código:** COLIGADA

**Título:** Coligada

**Texto:** Coligadacorrente

**Código:** PERIODO

**Título:** Período atual

**Texto:** Periodo

**1º Passo:** Acessar o módulo "Utilitários | Consultas SQL" e cadastrar as consultas SQL abaixo:

**Código: 13SALARIO**

**Título:** 13º salário pago durante o ano

**Texto:**

**SELECT SUM**(VALOR) VALOR **FROM PFFINANC** (**NOLOCK**), **PEVENTO** (**NOLOCK**), **PPARAM** (**NOLOCK**)

**WHERE** PFFINANC.CODCOLIGADA=PEVENTO.CODCOLIGADA

**AND** PPARAM.CODCOLIGADA=PFFINANC.CODCOLIGADA

**AND** PEVENTO.CODIGO=PFFINANC.CODEVENTO

**AND** PFFINANC.CHAPA=:FRM\_CHAPA

**AND** PEVENTO.CODIGOCALCULO='9'

**AND** (PFFINANC.MESCOMP<>PPARAM.MESCOMP **OR** PFFINANC.NROPERIODO<> :FRM\_PERIODO)

**AND** PFFINANC.ANOCOMP=PPARAM.ANOCOMP

**AND** PFFINANC.CODCOLIGADA=:FRM\_COLIGADA

**Código: INICIOVIGENCIAIR**

**Título:** INICIO DE VIGENCIA DA ULTIMA TABELA DE IRRF

**Texto:**

**SELECT MAX**(INICIOVIGENCIA) AS DATAINICIO **FROM PTABCALC**

**WHERE** FINALIDADE = 2

**AND** CODCOLIGADA = :FRM\_COLIGADA

**2º Passo:** Cadastrar as seguintes fórmulas através do módulo "Cadastro | Fórmulas".

**OBSERVAÇÃO:** As fórmulas não consideram o meses de admissão caso o número de dias trabalhados sejam inferiores a 15 dias.

**Código da 1ª fórmula: A0011**

**Título:** AVOS 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

NROAVOS13+ABS(MES-12)

SENAO

NROAVOS13

FIMSE

**Código da 2ª fórmula: A0012**

**Título:** 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

(RC/12)\*(NROAVOS13+ABS(MES-12))-resultsql('13SALARIO','valor')

SENAO

(RC/12)\*(NROAVOS13)-resultsql('13SALARIO','valor')

FIMSE

**-----**

**OBSERVAÇÃO:** Caso queira que as fórmulas adicionais de 13º informadas em **Opções/Parâmetros/RMLabore/Parâmetros de 13º** sejam consideradas deverá alterar a fórmula anterior (A0012) da seguinte forma:

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

((RC + FOR("XXXX") + FOR("YYYY"))/12)\*(NROAVOS13+ABS(MES-12))

SENAO

((RC + FOR("XXXX") + FOR("YYYY"))/12)\*(NROAVOS13)

FIMSE

\*Onde houver XXXX ou YYYY deverá ser alterado para as fórmulas adicionais existentes.

**-----**

**Código da 3ª fórmula: A0016**

**Título:** MEDIA DE 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO

**Texto:**

execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

(CALCMED(2)/12)\*(NROAVOS13+ABS(MES-12))

SENAO

(CALCMED(2)/12)\*(NROAVOS13)

FIMSE

**3º Passo:** Criar as fórmulas abaixo através do módulo "Cadastro | Fórmulas".

**Código: A0013**

**Título:** INSS DE ANTECIPAÇÃO DE 13º SALARIO

**Texto:**

execsql('13SALARIO');

TI(FOR('A0012')+FOR('A0016')+ resultsql('13SALARIO','valor'))

**Código: PENS13PR**

**Título:** Pensão sobre líquido de 13º salário antecipado (liquido)

**Texto:**

DECL PERC, CONT, X;

SETVAR (CONT,1);

SE TABDEP ('DTNASCIMENTO' ,'V' ,CONT) <> DATANULA ENTAO

REPITA

  SE TABDEP ('DTNASCIMENTO','V',CONT) <> DATANULA E TABDEP ('INCPENSAO','S',CONT) ='1'    ENTAO

           SETVAR (PERC, TABDEP ('PERCENTUAL' , 'V', CONT) / 100);

           SETVAR (X,1)

   SENAO ""

  FIMSE;

  SETVAR (CONT,CONT+1)

ATE X=1 OU TABDEP ('DTNASCIMENTO' ,'V' ,CONT) = DATANULA

FIMSE;

SE X>0 ENTAO

     DECL LIQUIDO, VLRBASEIRRF, VLRINSS, VLRINSS2, VLR,CONTADOR;

     SETVAR (LIQUIDO, C('8001') + C('8005')); /\*Se quiser deduzir o valor adiantado basta diminuir o valor do evento cc 35\*/

      SETVAR (VLRINSS, TI (LIQUIDO));

      SETVAR (VLRINSS2, TI2(LIQUIDO));

      SETVAR (VLRBASEIRRF, LIQUIDO);

      REPITA

              SETVAR (VLR, ((LIQUIDO-VLRINSS- TR (VLRBASEIRRF-VLRINSS2-VLR)) \* PERC));

              SETVAR (CONTADOR, CONTADOR+1)

      ATE CONTADOR= 7;

VLR

SENAO

      0

FIMSE

**Obs.:** A fórmula acima somente deverá ser criada caso queira descontar a pensão sobre o pagamento do 13º salário integral. Neste, o usuário também deverá cadastrar um evento do tipo desconto/valor sem incidências e associar a fórmula PENS13PR.

**Código: A0014**

**Título:** IRRF DE ANTECIPAÇÃO DE 13º SALÁRIO

**Texto:**

EXECSQL('13SALARIO');

EXECSQL('INICIOVIGENCIAIR');

DECL BCALC, VALDEPIR, DT;

SETVAR (DT, RESULTSQL('INICIOVIGENCIAIR','DATAINICIO'));

SETVAR(BCALC,FOR('A0012')+FOR('A0013')+RESULTSQL('13SALARIO','VALOR'));

SETVAR (VALDEPIR, NDEPIR ( HOJE) \* F ('DDEP'));

SE BCALC <= TABCALCULO ('LIMITESUPERIOR' ,'IRRF' ,DT ,1 )

ENTAO 0 SENAO

SE BCALC <= TABCALCULO ('LIMITESUPERIOR' ,'IRRF' ,DT ,2 )

ENTAO ((BCALC - VALDEPIR - TI(BCALC) - FOR('PENS13PR')) \* 0.075) - TABCALCULO ('VALDEDUZIR' , 'IRRF' , DT , 2) SENAO

SE BCALC <= TABCALCULO ('LIMITESUPERIOR' ,'IRRF' ,DT ,3 )

ENTAO ((BCALC - VALDEPIR - TI(BCALC) - FOR('PENS13PR')) \* 0.15) - TABCALCULO ('VALDEDUZIR' , 'IRRF' , DT , 3) SENAO

SE BCALC <= TABCALCULO ('LIMITESUPERIOR' ,'IRRF' ,DT ,4 )

ENTAO ((BCALC - VALDEPIR - TI(BCALC) - FOR('PENS13PR')) \* 0.225) - TABCALCULO ('VALDEDUZIR' , 'IRRF' , DT , 4) SENAO

((BCALC - VALDEPIR - TI(BCALC) - FOR('PENS13PR')) \* 0.275) - TABCALCULO ('VALDEDUZIR' , 'IRRF' , DT , 5)

FIMSE

FIMSE

FIMSE

FIMSE

**Código: A0015**

**Título:** DESCONTO DE INSS E IRRF ANTECIPADO

**Texto:**MV(15,ANO,'8003')+MV(15,ANO,'8002')

**Obs.:** Em caso do desconto do evento de pensão, incluir na fórmula acima +MV(15,ANO,'XXXX'), onde XXXX deve ser substituído pelo código do evento de pensão criado conforme descrito na observação da fórmula PENS13PR.

**4º Passo: Cadastrar os seguintes eventos em "Cadastro | Eventos".**

**Código do 1º evento: 8001**

**Descrição:** Adiantamento de 13º Salário

Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS

No campo "Fórmula valor" informar a fórmula de código A0012.

No campo "Fórmula Referência" informar a fórmula de código A0011.

[![clip_image022](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3TRiADEI/AAAAAAAAEIs/wNeMOZaYmYc/clip_image022_thumb%5B1%5D.jpg?imgmax=800 "clip_image022")](http://lh6.ggpht.com/_G7KXZLoZDsY/TO_3SoHY-wI/AAAAAAAAEIo/deBp7-VIYEY/s1600-h/clip_image022%5B4%5D.jpg)

[![clip_image024](http://lh5.ggpht.com/_G7KXZLoZDsY/TO_3UiEDHTI/AAAAAAAAEI0/mHZ3XT0FJnM/clip_image024_thumb%5B1%5D.jpg?imgmax=800 "clip_image024")](http://lh4.ggpht.com/_G7KXZLoZDsY/TO_3T7nB_sI/AAAAAAAAEIw/OBRD0zzc3yM/s1600-h/clip_image024%5B4%5D.jpg)

**Código do 2º evento: 8005**

**Descrição:** Média de adiantamento de 13º Salário

Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS

No campo "Fórmula valor" informar a fórmula de código A0016.

No campo "Fórmula Referência" informar a fórmula de código A0011.

**Código do 3º evento: 8002**

**Descrição:** INSS 13º Salário (antecipado)

Desconto/Valor, sem Código de Cálculo.

No campo "Fórmula valor" informar a fórmula de código A0013.

**Código do 4º evento: 8003**

**Descrição:** IRRF 13º Salário (antecipado)

Desconto/Valor, sem Código de Cálculo.

No campo "Fórmula valor" informar a fórmula de código A0014.

**Código do 5º evento: 8004**

**Descrição:** Desconto de INSS13º e IRRF13º (antecipado)

Provento/Valor, sem Código de Cálculo.

No campo "Fórmula valor" informar a fórmula de código A0015.

**5º Passo:** Para realizar o lançamento você deverá lançar os eventos 8001, 8002, 8003 e 8005 através do módulo "Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos".

### PROCEDIMENTO A SER REALIZADO NA COMPETÊNCIA DEZEMBRO

### (Somente para quem efetuou o pagamento integral antecipado)

**6º Passo:** Lançar, através do módulo "Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos" o evento 8004 (criado no passo 2).

**7º Passo:** Na competência Dezembro deverá efetuar o processamento de 13º Salário normalmente através do módulo "Movimento | Folha de Pagamento | Lançamentos Automáticos | Décimo Terceiro Salário".

**8º Passo:** Efetuar a geração do SEFIP e de todas as guias.

**- - - - - - - - - - - - - - - /// NOTA IMPORTANTE \\\ - - - - - - - - - - - - - - -**

O recolhimento do INSS de 13º salário e IRRF de 13º salário deve ocorrer em dezembro, pois a legislação de IRRF (texto abaixo) informa que o IRRF deve ser calculado no ato da quitação e na verdade a quitação só ocorre em dezembro, pois podem ocorrer diferenças salariais, diferenças de médias e até mesmo de tabelas de cálculo o que acarretaria problemas no cálculo da diferença de INSS e IRRF.

O INSS só é aceito no SEFIP da competência 13 (veja manual do SEFIP). Se recolhido anteriormente não será possível a geração deste SEFIP automaticamente na competência de dezembro.

**Obs.:** **Lembramos que, ao emitir a DIRF, o IRRF e o INSS do funcionário irá aparecer na competência Dezembro.**

### Processamento – 2ª Parcela de 13º Salário (Mês de Dezembro)

###### Módulo: “Movimento/Folha de Pagamento/Lançamento Automático/13º Salário”

Tipo de Lançamento:

- **Segunda parcela:** Lançamento da segunda parcela do 13º salário.

Situações a observar:

- Funcionário comissionista, será efetuado o cálculo da média ou considerado o mínimo garantido do sindicato.

- Quando o funcionário tiver afastado por acidente de trabalho:

|  |  |
| --- | --- |
| 1 – | Deverá ser lançado um evento de Salário Pago na Previdência, (Desconto, Valor, com CC101), onde deverá ser informado o valor que o funcionário recebeu no período que esteve afastado (Lembrando que este valor do 13º Salário pago pela previdência, deverá ser apurado junto ao funcionário). |

- A empresa não poderá estar trabalhando com as médias discriminadas apenas no 13º Salário ou apenas no 13º Rescisão, pois afeta o cálculo de INSS de ambas as partes.

- Lançamento de pensão alimentícia poderá ser feito através dos códigos fixos, lembrando que o evento deverá ter CC120.

- Quando o funcionário possuir outro emprego:

Empresas que fazem o cálculo paralelo

|  |  |
| --- | --- |
| 1 - | Criar o Evento INSS 13º Outro Emprego (Base de Cálculo, Valor, Com CC144), informar o valor caso já tenha sido descontado na outra empresa o INSS, caso contrário deverá ser lançado o evento com CC83, onde o sistema efetuará a proporcionalização. |
| 2 – | Criar o Evento Base de INSS 13º outro emprego (Base de Cálculo, com CC83), informar o valor da Base de incidência de INSS do outro emprego para que seja proporcionalizado. |

Empresas que não fazem cálculo paralelo (proporcional nas duas empresas)

|  |  |
| --- | --- |
| 1 - | Criar o Evento INSS 13º Outro Emprego (Base de Cálculo, Valor, Com CC182), informar o valor da base da INSS de 13º na outra empresa.  O código de ca´culo 83 será calculado automaticamente. |

**ATENÇÃO:**

- No dia 20/12 deverá ser gerado SEFIP de 13º (módulo “Relatórios | SEFIP”), marcando o campo “SEFIP 13”, Informe o percentual de INSS recolhido pela empresa. Este SEFIP não gera recolhimento de FGTS, pois ele é utilizado apenas para declaração do valor de INSS de 13º salário que foi pago pela empresa na guia de GPS 13 no dia 20/12.

### Cálculo para funcionários que eram mensalistas e passaram a ser comissionistas

Nesse caso o sistema calcula 13° somente a partir do mês que se tornou comissionista, por isso é necessário utilizar o roteiro.

**Cadastrar a consulta SQL :**

**/\* Verifica qual o último mês que o funcionário recebeu dias trabalhados ou horas normais, ou seja, último mês como mensalista/horista \*/**

**Código: ULTIMOMES**

**Título:** Ultimo mês que o funcionário recebeu dias trabalhados ou horas normais

**Texto:**

**SELECT MAX**(PFFINANC.MESCOMP) **AS** ULTIMOMES

**FROM** PFFINANC, PEVENTO, PPARAM

**WHERE** PFFINANC.CODCOLIGADA=PEVENTO.CODCOLIGADA

**AND** PPARAM.CODCOLIGADA=PFFINANC.CODCOLIGADA

**AND** PEVENTO.CODIGO=PFFINANC.CODEVENTO

**AND** PFFINANC.CHAPA=:FRM\_CHAPA

**AND** (PEVENTO.CODIGOCALCULO='2' **OR** PEVENTO.CODIGOCALCULO='1')

**AND** PFFINANC.ANOCOMP=PPARAM.ANOCOMP

**AND** PFFINANC.CODCOLIGADA=:FRM\_COLIGADA

**AND** (**SELECT** PFFINANC.VALOR **WHERE** PEVENTO.CODIGOCALCULO='2')>0

Fórmula para pagar 13° sobre os meses que o funcionário era mensalista :

oBS : Esta fórmula foi criada considerando como média o ano todo. Se o cliente deseja pagar média sobre 6 meses, por exemplo, a fórmula deve ser adaptada.

**Fórmula 1ª parcela:**

**Código: 1parcela**

**Título:** 1ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E EXECSQL('ULTIMOMES')>0 E MES=11

ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES'));

(RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13+1)-(12-MENSAL))/2

SENAO

0 FIMSE

**Fórmula para o evento com C.C 102 :**

**Código: 2parcela**

**Título:** 2ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E EXECSQL('ULTIMOMES')>0 E MES=12

ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES'));

(RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13)-(12-MENSAL))/2

SENAO

0 FIMSE

A cliente deverá lançar o 13° normalmente pelo módulo automático, o sistema irá pagar para todos os funcionários, e também para o comissionista, incluindo as médias do ano todo.

Criar outro evento com código de cálculo 9 e outro com código de cálculo 102, com a respectiva fórmula acima, para pagamento do valor referente aos meses que o funcionário era mensalista.

Efetuar o lançamento do 13° pelo módulo automático primeiro e depois o lançamento pelo grupo de eventos o evento criado. Isso evita a substituição de valores.

Informar a fórmula no evento com C.C 102 somente após o pagamento da primeira parcela, pois interfere no cálculo.

**Fórmula considerando os últimos 6 meses para o cálculo de 13° :**

**Código: 1parcela**

**Título:** 1ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E RESULTSQL('ULTIMOMES','ULTIMOMES')>=5 E MES=11

ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES'));

(RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13+1)-(12-(MENSAL-1)))/2

SENAO

0 FIMSE

**2ª parcela :**

**Código: 2parcela**

**Título:** 2ª parcela

**Texto:**

EXECSQL('ULTIMOMES');

DECL(MENSAL);

SE TFUNC='O' E RESULTSQL('ULTIMOMES','ULTIMOMES')>=5 E MES=12

ENTAO

SETVAR(MENSAL,RESULTSQL('ULTIMOMES','ULTIMOMES'));

(RANT(MTDATA(1,MENSAL,ANO))/12)\*((NROAVOS13)-(12-MENSAL+2))/2

SENAO

0 FIMSE

Exemplo da fórmula considerando 6 últimos meses: Funcionário recebia 500,00 até o mês 9, deixou de ser mensalista e passou a ser comissionista.

O cálculo será na competência 11, considerando do mês 6 ao mês 11:

(500/6) \* 4 = 333,33 1ª parcela : 166,66

Competência 12, considerando do mês 7 ao mês 12 :

(500/6) \* 3 = 250,00 2ª parcela : 125,00

O valor de 1ª e 2ª parcela sobre a comissão será pago no evento normal.

### Como é feito o Cálculo de Médias

As médias são utilizadas nos cálculos de 13º salário, férias, aviso prévio e licença maternidade. Para que o sistema faça o cálculo de médias é preciso que a parametrização esteja feita de forma correta.

Média  
(Estatística) - É o número obtido somando-se os valores medidos e dividindo-se a soma obtida pelo número de medições. É usada como síntese, valor representativo do conjunto de dados. É particularmente útil em distribuições simétricas. É a região da distribuição de freqüências onde se concentra a maioria das observações.

**Exemplo de cálculo de média:**

Salário R$ 1257,14

Jornada Mensal 220:00

Salário Hora: Salário/Jornada => 1257,14 / 220 = 5,7142

Hora Extra 75% = 5,7142 + 75% => 5,7142\*1,75 = R$ 10,00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Mês e ano** | **Evento** | **Nome** | **Horas** | **Valor** |
| 02/2010 | 0157 | Horas extras 75% | 10:00 | R$ 100,00 |
| 03/2010 | 0157 | Horas extras 75% | 10:00 | R$ 100,00 |
| 05/2010 | 0157 | Horas extras 75% | 20:00 | R$ 200,00 |
| 07/2010 | 0157 | Horas extras 75% | 10:00 | R$ 100,00 |
| 10/2010 | 0157 | Horas extras 75% | 10:00 | R$ 100,00 |

Numero de meses com horas extras = 5

Soma de horas 60:00

Soma do dos valores R$ 600,00

**Média do período de 01/01/2010 a 31/12/2010**

Número de mês do período acima: 12 meses

Salário atual R$ 2200,00

Jornada Mensal 220:00

Salário Hora: Salário/Jornada => 2200,00 / 220 = R$ 10,00

Hora Extra 75% = 10,00 + 75% => 10,00\*1,75 = R$ 17,50

**Tipos de média**

Cálculo da média por valor:

Soma dos valores encontrados no período / número de meses analisados

R$ 600,00 / 12 = 50,00

**Cálculo da média por horas**

Soma das horas encontradas no período / número de meses analisados

60:00h / 12 = 5:00h

Médias das horas multiplicado pelo valor das horas com seu percentual, atualmente

5:00h \* R$ 17,50 = R$ 87,50

Veja que a média por horas considera o salário atual.

### Observações para admitidos em Janeiro e para afastados durante o ano

- **1)** Para funcionários admitidos até 17 de janeiro (inclusive), o Sistema calculará metade (50%) do salário contratual percebido no "Mês Anterior" ao do pagamento.

- **2)** Para funcionários admitidos após 17 de janeiro, o Sistema calculará o número de avos a que o funcionário tem direito (da admissão até o mês anterior ao pagamento) e pagará a metade do total encontrado.

- **3)** Para funcionários afastados por acidente de trabalho, o 13º será pago integralmente. Para descontar o 13º pago pela previdência, deverá ser lançado na movimentação do mês de dezembro, o evento de desconto com CC 101, com o valor de 13º pago pela previdência.

O evento com CC 101 é um evento de Desconto tipo Valor. O valor informado neste código de calculo será deduzido também da base de calculo do 13º salário para o cálculo do IRRF e INSS.

- **4)** Para funcionários afastados pela previdência, o 13º será pago somente sobre os avos aos quais o funcionário terá direito. As incidências do FGTS, INSS, IRRF serão somente sobre o valor pago pelo sistema ao funcionário.

- **5)** Para funcionárias que tiveram dias de afastamento por licença maternidade durante o ano o sistema irá calcular o valor normalmente (como é calculado para os demais funcionários), porém na guia de INSS e no SEFIP os valores referente ao valor do 13º salário pago pela previdência serão calculados da seguinte forma:

Soma dos eventos de CC 102 (ou CC48 caso venha a ser rescisão) / nº de avos que estão sendo pagos / 30 \* Número de dias de afastamento dentro do ano.

Estes valores sobre os dias de afastamento por licença maternidade não aparecerão na movimentação e nem na folha analítica, para que seja impresso na folha analítica deverá ser criada uma fórmula.

### Informações Legais:

13º Salário (Gratificação Natalina)

[**DECRETO Nº 57.155, DE 3 DE NOVEMBRO DE 1965.**](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/DEC%2057.155-1965?OpenDocument)

*http://www.planalto.gov.br/CCIVIL/decreto/1950-1969/D57155.htm*

[**LEI No 4.090, DE 13 DE JULHO DE 1962.**](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/lei%204.090-1962?OpenDocument)

<http://www.planalto.gov.br/ccivil/leis/L4090.htm>

[**LEI No 4.749, DE 12 DE AGOSTO DE 1965.**](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/lei%204.749-1965?OpenDocument)

<http://www.planalto.gov.br/ccivil/Leis/L4749.htm>

[**LEI Nº 7.855, DE 24 DE OUTUBRO DE 1989.**](http://legislacao.planalto.gov.br/legislacao.nsf/Viw_Identificacao/lei%207.855-1989?OpenDocument)

<http://www.planalto.gov.br/ccivil/Leis/L7855.htm#art3>

**LEI DELEGADA Nº 13, DE 27 DE AGOSTO DE 1992.**

**<http://www.planalto.gov.br/ccivil/Leis/LDL/Ldl13.htm>**

**IMPOSTO DE RENDA SOBRE O 13º SALÁRIO.**

[http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.htm](http://www.receita.fazenda.gov.br/PessoaJuridica/DIRF/Mafon2003/escladicionais.htm#Gratifica%E7%E3o%20de%20Natal%20%2813%BA%20SAL%C1RIO%29)
