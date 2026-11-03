---
article_id: 360018471912
category: Call Center - Telecobrança
content_hash: 432a78402f8fcd395ce3c8cc032a6b707c49adc5e5a2a9a04c3278b07564ce1a
fetched_at: '2026-06-28T22:41:28.695877+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-JOB Baixa Cobrança
  Autormatica TMKA290 - Parametros
type: support-article
updated_at: '2022-06-22T17:38:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018471912-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-JOB-Baixa-Cobran%C3%A7a-Autormatica-TMKA290-Parametros
---

**Dúvida**

Mesmo criando Schedule e job no server sistema não executa a baixa automaticamente.  
  
**A****mbiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-a partir da versão 11.  
  
**Solução**

Verificar os parâmetros abaixo se estão preenchidos corretamente:

**MV\_TMKENC** - Define o código de encerramento padrão utilizado  no encerramento de atendimentos do telecobrança de forma automática

Ex: 000001

**MV\_TMKMEMO** - Define o o texto padrão de encerramento utilizado no encerramento de atendimentos do telecobrança de forma automática.

Ex: "Encerramento automático via Job/Schedule."

Obs:

O fonte **TMKA290** está preparado para execução de rotinas automáticas, mais não há nenhum schedule(JOB) pronto para executar pois é o fonte do schedule(JOB) que deve ser cadastrado na tabela **SXD**.

Nesse caso, o usuário poderá customizar um JOB para chamar a função **TMKA290ATU**() auxilio no link abaixo, onde é necessário estar com as configurações dos parâmetros MV\_TMKENC,MV\_TMKMEMO. corretas.

**[TMK0016\_Como\_Configurar\_Schedule\_na\_Baixa\_de\_Cobranca](http://tdn.totvs.com/display/PROT/TMK0016_Como_Configurar_Schedule_na_Baixa_de_Cobranca)**
