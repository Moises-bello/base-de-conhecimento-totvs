---
article_id: 10699504348567
category: RH - Férias
content_hash: 1fa8b1ca306cae3ca02a44a59cf2d78844894e0a1c466ae6adf1e042d277e844
fetched_at: '2026-06-28T22:43:58.080971+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir a base de cálculo para médias conforme
  cadastro de verbas e sindicato
type: support-article
updated_at: '2025-09-02T17:23:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10699504348567-RH-Linha-Protheus-GPE-Como-conferir-a-base-de-c%C3%A1lculo-para-m%C3%A9dias-conforme-cadastro-de-verbas-e-sindicato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31494734532247) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como conferir a base de cálculo para médias definido no cadastro de verba e sindicato.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

A base para cálculo de médias é formada com de acordo com as informações do **cadastro de verbas** e **sindicatos**.  
  
**Exemplos de Utilização;**

O cadastro de verbas é a informação mais específica do cálculo e ponto de partida para a geração de médias, apenas verbas que tenham incidência para médias preenchida no cadastro de verbas serão utilizadas no cálculo. Existem três campos no cadastro de verbas utilizados para médias, são eles:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31494778638103)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10699344607767)

Os três campos podem ser preenchidos de 4 formas diferentes, são eles:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10699346225687)

Para exemplificar as possibilidades de cálculo, vamos pensar no seguinte cadastro de verbas fictício:   
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10699347598615)

E um funcionário com os seguintes lançamentos ao longo do ano;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10699380557463)

Com essas configurações, o cálculo de **média de férias** realizado em dezembro ocorrerá da seguinte forma:

**Verba 001**

Serão considerados 9 meses para a somatória das verbas, de acordo com o cadastro de sindicatos.  
Somatório da verba 001 considerada = R$900,00

**Verba 002**

Serão considerados 12 meses para a somatória das verbas, pois deverá utilizar a quantidade de meses do período aquisitivo.  
Somatório da verba 002 considerada = R$2400,00

**Verba 003**

Serão considerados 8 meses para a somatória das verbas, pois é a quantidade de meses definido no cadastro de verbas.  
Somatório da verba 003 considerada = R$1200,00

Base total de média de férias = R$4500,00

Para o cálculo de **média de 13º salário** serão considerados os seguintes valores:

**Verba 001**

Serão considerados 12 meses para a somatória das verbas, pois é a quantidade de meses definido no cadastro de verbas.  
Somatório da verba 001 considerada = R$1200,00

**Verba 002**

Serão considerados 9 meses para a somatória das verbas, de acordo com o cadastro de sindicatos.  
Somatório da verba 002 considerada = R$1800,00

**Verba 003**

Serão considerados 12 meses para a somatória das verbas, pois deverá utilizar a quantidade de meses do período aquisitivo.  
Somatório da verba 003 considerada = R$1800,00

Base total de média de 13º = R$4800,00

**Importante**

O cadastro de verbas e sindicatos influência no cálculo da base para médias, que é o valor total utilizado antes da divisão pelos meses de direito, essa última divisão, para encontrar o valor para pagamento de médias, é calculado com base no conteúdo do mnemônico [P\_MEDDIREN](https://tdn.totvs.com/pages/viewpage.action?pageId=224112471).

**Saiba Mais:**[RH - Linha Protheus - GPE - Como conferir o Relatório de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025175673-RH-Linha-Protheus-GPE-Como-conferir-o-Relat%C3%B3rio-de-M%C3%A9dias-?source=search)  
[RH - Linha Protheus - GPE - Cálculo de médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050726154-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-m%C3%A9dias?source=search)  
[RH - Linha Protheus - GPE - Parâmetros e Mnemônicos que o Sistema utiliza para o cálculo de médias em férias e 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7011337477015-RH-Linha-Protheus-GPE-Par%C3%A2metros-e-Mnem%C3%B4nicos-que-o-Sistema-utiliza-para-o-c%C3%A1lculo-de-m%C3%A9dias-em-f%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio?source=search)
