---
article_id: 360025545214
category: RH - Folha de Pagamento
content_hash: 682fdb3ba7ccd0624b0b842108606004b4b3808391149a63dd972956cf05b1e7
fetched_at: '2026-06-28T22:44:13.297592+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o calculo de adicional para Cargo
  de Confiança
type: support-article
updated_at: '2024-09-06T20:41:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025545214-RH-Linha-Protheus-GPE-Como-configurar-o-calculo-de-adicional-para-Cargo-de-Confian%C3%A7a
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26195268989207) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como configurar  o calculo de Adicional para cargo de Confiança?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema possui o campo **% Adc.Conf. (RA\_ADCCONF)** e o Identificador de Cálculo **984 - Adicional para Cargo de Confiança**, com a finalidade de efetuar o Cálculo de adicional para cargo de confiança, de acordo com o artigo descrito abaixo:  
  
A CLT (Art.62) determina uma remuneração, no mínimo, superior em 40% à remuneração do cargo efetivo para os empregados que exercem cargo de confiança (Gestão), substitui o próprio empregador, isto é, embora não sendo o dono da empresa ou do negócio, detém poderes de tal modo que o diferencia dos demais trabalhadores, pois age como se fosse empregador (contrata, disciplina, assalaria, etc).  
O simples pagamento do acréscimo mencionado, não configura o cargo como sendo de confiança. De tal modo, que no sistema não foi implementado nenhum controle, sobre quem tem direito ou não ao adicional, a perda ou a incorporação do adicional, nem tampouco a quem está submetido ao controle de jornada de trabalho, por exemplo.  
  
Cadastre uma verba e configure os campos:  
  
**Tipo Cod**. (RV\_TIPOCOD): 1 - Provento.  
**Tipo Verba.** (RV\_TIPO): V (Valor).  
**Percentual.** (RV\_PERC): Informe 100.  
**Id.p/Cálculo.** (RV\_CODFOL): Informe o código 984 - Adicional para Cargo de Confiança.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039688674)  
  
Cadastro do funcionário, aba Adicionais, informe o percentual do adicional.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039688754)  
  
Para o calculo de férias deve criar as verbas de Identificadores de calculo abaixo:  
**1308 – Ad. Cargo Confiança Férias mês.****1309 – Ad. Cargo Confiança Férias mês seguinte.**

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
