---
article_id: 360024575574
category: RH - Pensão
content_hash: 5942d04db33be6ad2f2be8c4c313c7809255cb0fa6606299905b7d91026c70af
fetched_at: '2026-06-28T22:43:35.192002+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Pensão Alimentícia - Como conferir pensão alimentícia
  com mais de um beneficiário
type: support-article
updated_at: '2026-06-01T20:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024575574-RH-Linha-Protheus-GPE-Pens%C3%A3o-Aliment%C3%ADcia-Como-conferir-pens%C3%A3o-aliment%C3%ADcia-com-mais-de-um-benefici%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36985474303767) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como funciona o cálculo de pensão com o novo mnemônico P\_PENSPROP?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Para o cálculo da pensão alimentícia, principalmente quando é sobre o líquido, existe a configuração do parâmetro **MV\_PENSOUT**.

Caso esse parâmetro esteja configurado com **S**, o valor das pensões calculadas anteriormente será considerado para o cálculo do IR das pensões seguinte:

Caso esteja com **N**, não será considerado o cálculo da primeira pensão para abater das demais.

**Se a pensão é sobre o líquido** (informação do campo RQ\_CALSLIQ - Cal.Sobr.Liq no cadastro de beneficiário), caso os beneficiários possuam percentuais iguais de pensão, o primeiro beneficiário cadastrado receberá um valor maior de pensão do que o segundo beneficiário cadastrado quando o parâmetro estiver com **S**.

**Para que isso não ocorra**, ou seja, percentuais iguais de pensão terem valores diferentes de pensão, foi criada a proporcionalização da pensão entre os percentuais.  
  
Exemplo:

Supondo que a pensão total seja de 1000,00, com a proporcionalização, ambos os beneficiários receberão 500,00.

Ocorre que, quando os percentuais são DIFERENTES, a proporcionalização passa a ser questionável e, pensando nisso, foi criado esse mnemônico.

Com o novo mnemônico criado, será possível definir se os valores de pensão serão proporcionalizados ou não.

Esse mnemônico pode ser configurado de 3 formas quando o parâmetro **MV\_PENSOUT esta com S:**

1 - Sempre proporcionaliza a pensão.

2 - Não proporcionaliza a pensão.

3 - Proporcionaliza somente se os percentuais e as verbas de base de cálculo forem iguais.  
  
O mnemônico pode ser configurado somente de 1 forma quando o parâmetro **MV\_PENSOUT esta com N**:

4 - Agrupa beneficiários com o mesmo percentual, somando-os e fazendo o calculo com a mesma base, e no final dividindo o valor pelos beneficiários.  
  
**Abaixo alguns exemplos de cálculo, com o parâmetro com S:**

**Cenário 1:**

1 - Cad. De Beneficiário com SIM para Calcula sobre Líquido, sem verbas base de cálculo selecionadas

2 - Verbas de pensão sem id de cálculo.

3 - MV\_PENSOUT = S

4 - Beneficiários Cadastrados - um com 20% e outro com 30% e outro com 20%, exatamente nessa sequência de cadastro.

5 - Mnemônico **P\_PENSPROP** configurado com **1** (Caractere).  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082888414)

- Para o cálculo do IR, sistema considerou o valor descontado da pensão anterior:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082888454)

-Para o cálculo do IR, sistema considerou o valor descontado da pensão 1 e 2:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360082888474)

**Cenário 2:**

1 - Cad. De Beneficiário com SIM para Calcula sobre Líquido, sem verbas base de cálculo selecionadas

2 - Verbas de pensão sem id de cálculo.

3 - MV\_PENSOUT = S

4 - Beneficiários Cadastrados - um com 20% e outro com 30% e outro com 20%, exatamente nessa sequência de cadastro.

5 - Mnemônico P\_PENSPROP configurado com **2** (Caracter).

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36985439224471)**

- Para o cálculo do IR, sistema considerou o valor descontado da pensão anterior:  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36985439227543)**  
  
-Para o cálculo do IR, sistema considerou o valor descontado da pensão 1 e 2:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084057193)

**NÃO PROPORCIONALIZA. VALORES APURADOS SÃO GERADOS NO CÁLCULO**  
  
**Cenário 3:**

1 - Cad. De Beneficiário com SIM para Calcula sobre Líquido, sem verbas base de cálculo selecionadas

2 - Verbas de pensão sem id de cálculo.

3 - MV\_PENSOUT = S

4 - Beneficiários Cadastrados - um com 20% e outro com 30% e outro com 20%, exatamente nessa sequência de cadastro.

5 - Mnemônico P\_PENSPROP configurado com **3** (Caracter).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36985474308247)

- Para o cálculo do IR, sistema considerou o valor descontado da pensão anterior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36985439231767)  
  
-Para o cálculo do IR, sistema considerou o valor descontado da pensão 1 e 2:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084057233)  
  
**Abaixo segue exemplo de cálculo com o parâmetro com N:**

1 - Cad. De Beneficiário com SIM para Calcula sobre Líquido, sem verbas base de cálculo selecionadas.

2 - Verbas de pensão sem id de cálculo.

3 - MV\_PENSOUT = N.

4 - Beneficiários Cadastrados - funcionário com 2 beneficiários com percentual de 15% cada.

5 - Mnemônico P\_PENSPROP configurado com **4** (Caracter).   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5923566549655)

**Observação:** O conteúdo padrão do mnemônico é "1".

**Saber Mais:**

[RH - Linha Protheus - GPE - Como conferir o cálculo de pensão alimentícia sobre o líquido quando há incidência de IRRF no adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044532413-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-pens%C3%A3o-aliment%C3%ADcia-sobre-o-l%C3%ADquido-quando-h%C3%A1-incid%C3%AAncia-de-IRRF-no-adiantamento?source=search)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016145152-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Cálculo de pensão alimentícia por quantidade de salário mínimo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4779950764567-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-pens%C3%A3o-aliment%C3%ADcia-por-quantidade-de-sal%C3%A1rio-m%C3%ADnimo?source=search)

[RH - Linha Protheus - GPE - Onde ficam as informações de Pensão no Validador da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004776841-RH-Linha-Protheus-GPE-Onde-ficam-as-informa%C3%A7%C3%B5es-de-Pens%C3%A3o-no-Validador-da-DIRF?source=search)

[RH - Linha Protheus - GPE - O que verificar quando o Sistema não gera a verba de pensão 13º salário na DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023797612-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-Sistema-n%C3%A3o-gera-a-verba-de-pens%C3%A3o-13%C2%BA-sal%C3%A1rio-na-DIRF?source=search)

[RH - Linha Protheus - GPE - É possível calcular pensão em rescisão com base no salário mínimo e verbas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012456261-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-calcular-pens%C3%A3o-em-rescis%C3%A3o-com-base-no-sal%C3%A1rio-m%C3%ADnimo-e-verbas-?source=search)

[RH - Linha Protheus - GPE - Como fazer filtro das verbas com SIM para pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059137174-RH-Linha-Protheus-GPE-Como-fazer-filtro-das-verbas-com-SIM-para-pens%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 2º Parcela, quando já ocorreu desconto na 1° Parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10784734204951-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-2%C2%BA-Parcela-quando-j%C3%A1-ocorreu-desconto-na-1-Parcela?source=search)

[RH - Linha Protheus - GPE - Como calcular IR pensão somente sobre verbas que fazem base para pensão (MV\_PENSIR)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8033388008983-RH-Linha-Protheus-GPE-Como-calcular-IR-pens%C3%A3o-somente-sobre-verbas-que-fazem-base-para-pens%C3%A3o-MV-PENSIR-?source=search)

[RH - Linha Protheus - GPE - Desconto de pensão alimentícia na 1º Parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10771368342551-RH-Linha-Protheus-GPE-Desconto-de-pens%C3%A3o-aliment%C3%ADcia-na-1%C2%BA-Parcela-do-13%C2%BA-Sal%C3%A1rio?source=search)
