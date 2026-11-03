---
article_id: 360051273954
category: RH - Sindicais
content_hash: b682b1dc327c66bdde160972771893f7b4e40d846646f90f9fcccbd5f281f213
fetched_at: '2026-06-28T22:43:10.903006+00:00'
product: protheus
section_id: 360011997333
source: central-protheus
title: RH - Linha Protheus - GPE - Contribuição assistencial / confederativa / mensalidade
  sindical sobre o salário base informado no cadastro do funcionário
type: support-article
updated_at: '2025-04-15T15:15:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051273954-RH-Linha-Protheus-GPE-Contribui%C3%A7%C3%A3o-assistencial-confederativa-mensalidade-sindical-sobre-o-sal%C3%A1rio-base-informado-no-cadastro-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799423639) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**Contribuição assistencial / confederativa / mensalidade sindical sobre o salário base informado no cadastro do funcionário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recursos Humanos - A partir da versão 12  
  
**Solução**

Para que o sistema realize o calculo da contribuição assistencial / confederativa / mensalidade sindical com base no salário base informado no cadastro do funcionário (GPEA010), foi disponibilizada melhoria para que seja possível definir se as contribuições Assistencial e Confederativa serão calculadas para funcionários afastados. Essa opção está disponível através do campo “**Desc. Afast.**” (RCE\_DESAFA) no cadastro de Sindicatos.

Por meio desse campo será possível definir se o sistema irá calcular ou não as contribuições Assistencial, Confederativa e a Mensalidade Sindical. Além disso o mnemônico **P\_PROPCONT** precisa estar configurado com **.F.**. Para configurar e calcular conforme a necessidade siga os passos abaixo**:**

**1.** Acesse **Atualizações > Definições de Cálculos > Mnemônicos** e pesquise pelo mnemônico **P\_PROPCONT** - Proporcionaliza as contribuições Sindicais, clique em **Alterar** e configure com **.F.**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428838761367)

**2.** Acesse o cadastro do Sindicato em **Atualizações > Cadastros > Sindicatos (GPEA340),** selecione o sindicato conforme a necessidade clique em **Alterar** e na aba **Outras Informações** preencha o campo **Desc. Afast.**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799427351)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799430679)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799431831)

**3.** Acesse a rotina de Verbas e cadastre as verbas de id 0069, 0720 e 0175 em **Atualizações > Definições de Cálculo > Verbas (GPEA040)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799437207)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428838770199)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799440791)

**4.** Acesse o cadastro do Funcionário em **Atualizações > Funcionário > Funcionários (GPEA010)** na aba **Funcionais** informe **SIM** no campo referente ao tipo de Contribuição Sindical, nesse exemplo configuramos o campo **Contr. Assis**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799443607)

**5.** Configure a contribuição sindical no cadastro do Sindicato em **Atualizações > Cadastros > Sindicatos (GPEA340)** informe percentual a ser descontado, preencha o campo **Tipo Salario** configure com **1 - Base**. Nesse exemplo configuramos a **Contribuição Assistencial**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799445143)

**6.** Acesse o cadastro do **Tipo de Ausência** em **Atualizações > Definições de Cálculos > Tipos de Ausências (GPEA430)** a ser lançado e configure com o campo **Des. Con. Sind. com Sim**;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799446679)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799447831)**

**7.** Lance o afastamento em **Atualizações > lançamentos > Ausências (GPEA240)**;

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428838792087)**

**8.** Calcule a folha em **Miscelânea > Cálculos > Por Roteiros (GPEM020)**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428799452823)

![](https://i.imgur.com/Fy7yLJX.png)

**9.** Consulte o calculo em **Consultas > Cálculos > Por Funcionários (GPEA090)**:

Salário base \* % cadastrado no sindicato = Desconto Sindical

R$5000,00 \* 0,91%= R$45,50

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31428838804887)

**Saiba Mais**  
[Artigos sobre Sindicais](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011997333-RH-Sindicais)

[DT contribuições Assistencial, Confederativa e Mensalidade Sindical](https://tdn.totvs.com/display/PROT/417367+MRH-6040+DT+contribuicoes+Assistencial%2C+Confederativa+e+Mensalidade+Sindical)
