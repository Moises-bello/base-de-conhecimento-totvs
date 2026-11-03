---
article_id: 7503224755351
category: RH - Rescisão
content_hash: 307ff1451fe0b859efd7193c9ce02069c4c5b2008850db80ecc388369e7b5707
fetched_at: '2026-06-28T22:43:52.057161+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como é o cálculo da rescisão para funcionário horista
  com jornada variável
type: support-article
updated_at: '2025-06-16T18:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7503224755351-RH-Linha-Protheus-GPE-Como-%C3%A9-o-c%C3%A1lculo-da-rescis%C3%A3o-para-funcion%C3%A1rio-horista-com-jornada-vari%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como é o cálculo da rescisão para funcionário horista com jornada variável  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O campo de **Saldo de Salário** refere-se aos dias/horas trabalhadas no mês da **Rescisão**, atualmente para o cálculo do campo, consideramos o salário referência do funcionário, porém para a categoria de **horista com Jornada Variável**, passaremos a considerar a quantidade de horas trabalhadas, vindas da importação do ponto, por exemplo, tornando assim o processo mais simples para o usuário.

Desta forma, caso o usuário realize a importação de lançamentos do ponto, ou possua verbas lançadas no roteiro **FOL**, e que estão no **GRUPO 0, campo Grupo Verba (RV\_GRPVER = "0")**  rotina passa a verificar estas verbas.

O código da verba será alterado para o código da Verba de **Saldo de Salário (ID 048)**, sendo assim, será apresentada na tela de cálculo de Rescisão com a referência em horas e o valor calculado com base nessas horas (Salário Hora do Cadastro de Funcionário \* Somas das horas das verbas lançadas que **pertençam ao grupo 0**)

**Obs.** Como no caso de horistas o valor do **Salário** e do **DSR** são separados, mesmo que a verba de **ID 0033 DSR Horista** esteja no **grupo 0** as horas desta verba não serão somadas ao **Saldo de Salário**.  
  
**Impressão TRCT**Como sabemos, para a impressão do TRCT, a referência da Verba Saldo de Salário deve ser apresentada em DIAS.

Sendo assim, para este caso de funcionário **Horista Jornada Variável** (RA\_HOJORVA) cujo as horas são provenientes do PONTO, iremos no campo Quantidade de Dias, considerar a Data de Afastamento, descontando (se houver) as faltas.  
  
**Aviso Prévio**Para o cálculo do Aviso Prévio será considerada a média de Horas apuradas das verbas que estão no **GRUPO 0, campo Grupo Verba (RV\_GRPVER = "0")** dos 12 meses anteriores à data de rescisão, após encontrar a médias multiplica-se pelo valor do Salário Hora atual.
