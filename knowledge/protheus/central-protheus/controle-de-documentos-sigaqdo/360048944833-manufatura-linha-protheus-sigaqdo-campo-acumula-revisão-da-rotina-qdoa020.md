---
article_id: 360048944833
category: Controle de Documentos (SIGAQDO)
content_hash: c7b7fb8814cc24411418121ec130c29233e7073120448ff3ba1073a268ab8dfc
fetched_at: '2026-06-28T22:42:28.961245+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Campo Acumula Revisão da rotina QDOA020
type: support-article
updated_at: '2022-03-18T14:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048944833-Manufatura-Linha-Protheus-SIGAQDO-Campo-Acumula-Revis%C3%A3o-da-rotina-QDOA020
---

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Qual a utilização do campo **Acum. Revisão** da opção **Outas Ações/Respons** da rotina **QDOA020 - Cadastro do Tipo de Documento**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**O campo **Acum. Revisão** é validado no momento de gerar uma nova revisão na rotina **QDOA050 - Cadastro de Documentos** pela opção **Outras Ações/Gera Revisão**.   
Quando este campo estiver preenchido com **Sim**, caso seja admitido ou transferido um usuário que se enquadra nos responsáveis no tipo de documento para o mesmo departamento, ao gerar revisão, o Sistema verifica o campo e consulta novamente os usuários que estão na condição de responsáveis para o departamento. Desta forma, usuários que não possuíam a permissão para gerar revisão na revisão anterior, serão acrescentados para a nova revisão, e também serão acrescentados como responsáveis na nova revisão gerada.  
Caso o campo esteja como **Não**, serão mantidos os mesmos usuários responsáveis já definidos no documento no qual está gerando uma nova revisão.
