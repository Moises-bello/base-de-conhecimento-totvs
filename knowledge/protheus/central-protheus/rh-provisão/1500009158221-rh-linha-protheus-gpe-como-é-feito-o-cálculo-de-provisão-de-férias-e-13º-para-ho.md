---
article_id: 1500009158221
category: RH - Provisão
content_hash: 67c32ccc2ae00c0b33d273f4df2c09258c440d7de8c81dd3ea7934a43ecd2b26
fetched_at: '2026-06-28T22:43:56.892082+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como é feito o cálculo de provisão de férias e
  13º para horistas
type: support-article
updated_at: '2024-05-31T19:03:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009158221-RH-Linha-Protheus-GPE-Como-%C3%A9-feito-o-c%C3%A1lculo-de-provis%C3%A3o-de-f%C3%A9rias-e-13%C2%BA-para-horistas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23869578402583) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como é feito o cálculo de provisão de férias e 13º para horistas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – Todas as Versões

**Solução**

Para os funcionários Horistas, a montagem do Salário Base nos cálculos de Provisão de Férias e 13º Salário será de acordo com o Salário Hora x Carga Horaria Mensal do cadastro do funcionário.  
  
1. Acesse: Atualizações / Funcionários / Funcionários (GPEA010) e verifique na Aba Funcionais o Salário hora e Carga Horaria: **![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869578416919)**Considerando este exemplo, o Salário Base para cálculo das provisões será:  
35,00 x 200 = **R$7.000,00**

2. Acesse: Miscelânea / Provisões / Provisão de Férias e 13ºSalário (GPEA070), e veja que o campo Valor do Salário apresenta o valor de R$7.000,00 para compor os cálculos das provisões:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869578438423)

3. Para emitir o Relatório de Provisão acesse: Relatórios / Provisões / Provisões de Férias (GPER070) ou Provisões de 13º Salário (GPER090), e preencha os parâmetros para impressão:  
  
**Cálculo da Provisão de Férias:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869627254807)  
  
**- Valor** = Salário / 30 x Dias de Direito = 7.000,00 / 30 x 5 = **1.166,67**

**- Adicionais** = Nesta coluna serão considerados os Adicionais calculados em Folha de Pagamento + Valor das Médias. **155,58**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869578462999)  
Mais informações sobre como conferir as Médias e Adicionais na provisão, acesse: [RH - Linha Protheus - GPE - Relatório de Médias pela Rotina de Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13972932615063-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-M%C3%A9dias-pela-Rotina-de-Provis%C3%A3o?source=search)

**- 1/3 Constit.**= Valor + Adicionais / 3 = 1.166,67 + 155,58 / 3 = **440,75**

**Cálculo da Provisão de 13º Salário:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869627274903)**

**- Valor** = Salário / 12 x Avos de Direito = 7.000,00 / 12 x 1 = **1.166,67**

**- Adicionais** = Nesta coluna serão considerados os Adicionais calculados em Folha de Pagamento + Valor das Médias. **155,58  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23869578504087)**

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
