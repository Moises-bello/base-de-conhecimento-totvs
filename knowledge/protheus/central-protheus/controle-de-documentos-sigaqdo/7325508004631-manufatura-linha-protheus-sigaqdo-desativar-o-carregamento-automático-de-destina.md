---
article_id: 7325508004631
category: Controle de Documentos (SIGAQDO)
content_hash: 6e762c8a0e54376c4e9c78625a06718fb8541caf2fda89f303bf86af3a250f75
fetched_at: '2026-06-28T22:42:28.995187+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Desativar o carregamento automático
  de destinatário de revisão anterior
type: support-article
updated_at: '2022-12-14T17:20:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7325508004631-Manufatura-Linha-Protheus-SIGAQDO-Desativar-o-carregamento-autom%C3%A1tico-de-destinat%C3%A1rio-de-revis%C3%A3o-anterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:30 min** **Dúvida**Na rotina **QDOA050 - Cadastro de Documentos** como **desativar** o carregamento automático de **destinatário** de revisão anterior ao gerar **uma nova revisão** do documento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Na rotina **QDOA050** para **desativar** o carregamento automático de **destinatário** de revisão anterior ao gerar **uma nova revisão** do documento, o parâmetro **MV\_QDODEST - Carrega todos os Destinatários da Revisão Anterior (1 = SIM 2 = Não)** deverá ter o **conteúdo igual a 2**.  
Caso não seja incluído um novo destinatário na nova revisão do documento, ao tentar **Finalizar** a geração da mesma, será exibido o [Help QD050DBR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038539853-Manufatura-Linha-Protheus-SIGAQDO-Help-QD050DBR-%C3%89-obrigat%C3%B3rio-o-cadastramento-dos-destinos-do-documento) informando a obrigatoriedade do cadastramento de destinatário.
