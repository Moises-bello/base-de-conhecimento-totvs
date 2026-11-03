---
article_id: 29285713676823
category: SIGAACD - Automação e Coleta de Dados
content_hash: 319cfc55f28f8c71f30cbb530421a5e0db8521eb2fff99a167a1e28af627aa2b
fetched_at: '2026-06-28T22:39:13.821387+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Sincronização Meu
  Coletor de Dados Http failure response for 0 Unknown Error
type: support-article
updated_at: '2025-01-16T19:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29285713676823-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Sincroniza%C3%A7%C3%A3o-Meu-Coletor-de-Dados-Http-failure-response-for-0-Unknown-Error
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29285713661207) Tempo aproximado para leitura: **00:01:00 min****Dúvida**O que fazer para corrigir a mensagem de erro na sincronização do Meu coletor de dados

**"Http failure response for 0 Unknown Error".** Como corrigir este erro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.   
  
**Solução**

Essa mensagem ocorre, porque o serviço criado para o aplicativo meu coletor de dados, informa que não tem licença disponível para o uso do aplicativo.

Avaliar as seguintes informações no ambiente, a respeito da mensagem apresentada:

1) Verificar no seu **AppServer.ini** do Rest na sessão **HTTPURI** na Tag **URL**, se consta mais de dois serviços configurado separadamente. Na Tag **URL** aonde informamos o **EndPoint** que ultimamente utilizamos como **REST**, pode constar outro serviço de **EndPoint**.

2) Analisar no serviço de licença se consta a licença **TOTVS I**, caso o cliente for Cloud acessar o ambiente TCLOUD informando sua empresa, clicando na opção Informações do ambiente e acessar o link do **Monitor do Licenser Server**.

3) Caso tiver a Tag Module=46, configurado no ambiente e ter a licença TOTVS I, configurado em serviços do EndPoint diferente, ira sincronizar corretamente.

4) Caso não tiver a licença TOTVS I, e tiver a Tag Module=46 configurada no AppServer.ini do Rest, é necessário contatar o seu ESN(Gerente de Contas) para obter a licença no Protheus.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
