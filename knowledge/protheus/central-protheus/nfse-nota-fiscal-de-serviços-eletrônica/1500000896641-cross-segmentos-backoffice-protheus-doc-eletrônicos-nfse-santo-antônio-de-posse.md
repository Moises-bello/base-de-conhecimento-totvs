---
article_id: 1500000896641
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d2c1fbc6b4b3d69db3dca6aadaf46a9f8cc15500f9d35adf0279f15712d9b00c
fetched_at: '2026-06-28T22:39:58.495468+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Santo Antônio
  de Posse (Particularidades Homologação)
type: support-article
updated_at: '2025-06-20T12:06:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000896641-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Santo-Ant%C3%B4nio-de-Posse-Particularidades-Homologa%C3%A7%C3%A3o
---

**Dúvida**  
Como realizar a transmissão de um RPS em ambiente de testes da prefeitura de Santo Antônio de Posse/SP?   
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A prefeitura em questão exige que algumas informações na nota sejam enviadas de uma maneira padrão no ambiente de homologação, sendo elas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099943834/mceclip0.png)  
  
Uma das particularidades a ser observada é o Código do Município, onde na verdade se trata do município do cliente utilizado na nota, que deverá ser 3504800 (Bálsamo/SP).  
Note que além de dados cadastrais como Código de Serviço, Alíquota, entre outros, se faz necessário utilizar o CNPJ e IM citados, ou seja, dentro do Protheus **será necessário criar uma nova filial com esses dados.**  
  
Detalhes: Manual de Integração disponível no próprio portal da prefeitura: [clique aqui.](http://fi1.fiorilli.com.br:5663/issweb/paginas/login)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001044022/mceclip1.png)  
  
*Obs.: Caso o status da nota esteja = 2 - Aguardando Transmissão do Lote, verificar documentação a seguir: [link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000480641-MP-NFSE-Santo-Ant%C3%B4nio-da-Posse-SP-Fault-occurred-while-processing-Homologa%C3%A7%C3%A3o-).*
