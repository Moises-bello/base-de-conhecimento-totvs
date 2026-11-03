---
article_id: 360025659773
category: RH - Provisão
content_hash: 8e0188da349926d82fe89238ab2445fef4e11e829c5b43736fac31ac82e74907
fetched_at: '2026-06-28T22:43:55.603009+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Adicionais de Provisão de Férias e 13º Salário
type: support-article
updated_at: '2025-06-17T20:33:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025659773-RH-Linha-Protheus-GPE-Adicionais-de-Provis%C3%A3o-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32881466603159)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como conferir os Adicionais de ATS (Anuênio, Biênio, Triênio, Quadriênio ou Quinquênio), Periculosidade, Insalubridade, Cargo de Confiança ou Adicional de Transferência, nos Cálculos de Provisão de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Os Adicionais (ATS, Periculosidade, Insalubridade, Cargo Confiança e Adicional de Transferência), mesmo quando estão Incorporando ao Salário do Funcionário, serão demonstrados em verbas especificas e na coluna "Adicionais" do relatório de provisão, e não somados aos valores de férias e 13º.   
Sendo assim as baixas também serão dadas como Adicionais.  
  
Para cálculo correto dos Adicionais, além dos Identificadores de Cálculo de Adicionais na Folha, são consideradas os cadastros abaixo:

1 - O Cadastro do Funcionário, na Aba Funcionários, deve estar vinculado ao cadastro de Sindicato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17624667239703)  
  
2 - No cadastro do Funcionário, na aba Adicionais, o Adicional que o funcionário tem direito deve estar preenchido.  
Neste exemplo, o funcionário possui Adicional de Periculosidade e Anuênio:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17624737179287)

3 - No Cadastro de Sindicato, os campos de cálculo de ATS, Periculosidade ou Insalubridade deverão estar preenchidos, de acordo com a convenção coletiva da categoria:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17624878247063)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17624847396759)  
  
4 - Ao Processar a Folha de Pagamento, os adicionais serão processados para o funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17625130064535)  
  
5 - Ao processar as provisões de Férias e 13º Salário, os adicionais serão calculados nas verbas abaixo:  
0254 - Adicional de Provisão de Férias Vencidas e Proporcionais;  
0267 - Adicional de Provisão de 13º Salário;  
0278 - Adicional de Provisão de 14º Salário.  
  
6 - Emita o relatório de Provisão para conferência dos valores de Adicionais:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17625367712663)

Para **Férias Vencidas**, como o funcionário tem direito à 30 dias, será somado o valor do Adicional de Periculosidade e Anuênio, para compor o valor de Adicional de Provisão de Férias.  
Anuênio + Periculosidade = Adicional de Prov. Férias Vencidas  
400 + 1200 = **1600**.  
  
Para **Férias Proporcionais**, como o funcionário ainda não tem o período de férias completo, o valor do Adicional de Periculosidade e Anuênio será proporcional aos dias de direito de Férias.  
Anuênio + Periculosidade / 30 x Dias de Direito = Adicional de Prov. Férias Proporcionais.  
400 + 1200 / 30 x 14 =  **746,67**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17625862050711)  
Para **13º Salário**, será somado o valor do Adicional de Periculosidade e Anuênio e proporcionalizado pelos Avos de Direito para compor o valor de Adicional de 13º Salário.  
Anuênio + Periculosidade / 12 x 8 = Adicional de 13º Salário  
400 + 1200 / 12 x 8 = **1066,67**.  
  
Para **14º Salário**, será aplicado o percentual de 14º informado nas perguntas para cálculo das provisões, sobre o valor de adicionais de 13º salário.  
Neste exemplo, ao processar a provisão, foi informado que o 14º salário deverá ser calculado aplicando o percentual de 50% sobre o 13º salário.  
Adicional de 13º Salário x % de 14º Salário = Adicional de 14º Salário.  
1066,67 x 50% =  **533,34**.

**Saiba Mais:**  
[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
