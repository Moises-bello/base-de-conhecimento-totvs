---
article_id: 360058298973
category: Férias
content_hash: 4749edbdf11e36f30096e9199b6bbc1c09e6820e25545a6e1fe2bd941d36c402
fetched_at: '2026-06-28T22:46:56.442679+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RM - FOP - Período Aquisitivo estendido
type: support-article
updated_at: '2021-06-17T12:22:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058298973-RM-FOP-Per%C3%ADodo-Aquisitivo-estendido
---

**Dúvida**

Ao realizar a rotina de Acerta Período Aquisitivo, o produto estende a Data Fim do período conforme a quantidade de dias afastados. O que fazer para ajustar?

**Ambiente**

RM - Totvs Folha de Pagamento - Todas as versões

**Solução**

Para funcionários que possuem Afastamento por Contrato Suspenso, quando a rotina de Acerta Período Aquisitivo for executada, o produto criará um novo Período Aquisitivo futuro, que ficará fechado enquanto o anterior não for finalizado. Neste novo Período Aquisitivo, o produto somará na data fim, a **quantidade de dias de afastamento por suspensão**.

Por exemplo, para um funcionário que ficou 60 dias afastado nessas condições, ao executar o Acerta Período Aquisitivo, ficará da seguinte forma:

![](https://tdn.totvs.com/download/attachments/545621865/image2020-4-5_10-57-38.png?version=1&modificationDate=1586095059073&api=v2)  
  
Caso o Usuário desejar manter o período, existem duas propostas de solução para aplicar no produto.

**Proposta 1:**

Acessar o Período Aquisitivo que foi estendido e ajustar manualmente sua data fim.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098083113/mceclip0.png)  
  
Porém, este procedimento poderá retornar um erro. Em alguns casos, ocorre quando o usuário decide alterar essa data algum tempo depois do produto já ter estendido a data fim.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098079773/mceclip0.png)  
  
Deste modo, o erro acima ocorre quando, no Período Aquisitivo que foi estendido, já existe cadastro na aba Período de Gozo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095783474/mceclip1.png)  
  
Para que seja permitido realizar a alteração, deve-se seguir os seguintes passos:

1. Excluir o período de gozo cadastrado na aba informada;
2. Alterar a Data Fim para a data desejada;
3. Incluir novamente o período de gozo com as mesmas informações, ou seja, conforme exemplo anterior, deverá informar as mesmas datas já em situação "Finalizadas".

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098080133/mceclip2.png)  
  
**Proposta 2:**

O usuário que ainda não executou a rotina Acerta Período Aquisitivo, para que não ocorra este tipo de comportamento, deverá verificar se a versão do sistema é igual ou superior a:

* 12.1.27.241
* 12.1.28.150
* 12.1.26.259

Nas versões supracitadas ou superiores, foi adicionado um parâmetro para que o usuário decida se irá estender ou não a data fim do Período Aquisitivo.

Ao acessar Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento 2/2 é exibida a seguinte tela:  
  
![](https://tdn.totvs.com/download/attachments/545621865/image2020-7-30_19-5-39.png?version=1&modificationDate=1596146739647&api=v2)  
  
Marcando esses parâmetros e informando o motivo de afastamento que será utilizado no afastamento do funcionário, serão mantidos o cálculo do período aquisitivo de férias e os avos de direito ao 13º salário para o período afastado pelo motivo C – Contrato Suspensão.

**Exemplo:** 

Mês competência 05/2020 – Parâmetros marcados e motivo preenchido com 1 – Com perda de avos

Funcionário 1 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 1 – Com perda de avos

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Afastamento de 01/03/2020 a 29/04/2020 – 60 dias - Motivo de afastamento 2 – Sem perda de avos

Executando o acerto de período aquisitivo:

Funcionário 1 – Período aquisitivo de 02/01/2020 a 02/03/2021 – Período estendido porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – Período aquisitivo de 02/01/2020 a 01/01/2021 – Período não foi estendido porque o motivo de afastamento não era o mesmo do parametrizador.

Calculando 13º salário em dezembro/2020:

Funcionário 1 – 10 avos – Perda de 2 avos porque o motivo de afastamento era o mesmo do parametrizador.

Funcionário 2 – 12 avos – Avos completos porque o motivo de afastamento não era o mesmo do parametrizador.

**Obs: Para a rescisão contratual, deverá ser executado o acerto de período aquisitivo primeiro, pois assim, o período aquisitivo estará correto no momento do cálculo e o cálculo do 13º salário rescisão seguirá do mesmo jeito que o 13º salário normal.**
