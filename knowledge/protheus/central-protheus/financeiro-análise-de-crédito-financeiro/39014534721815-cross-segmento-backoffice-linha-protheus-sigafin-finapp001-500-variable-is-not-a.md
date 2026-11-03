---
article_id: 39014534721815
category: Financeiro - Análise de Crédito Financeiro
content_hash: be9b6d9dcdab830d40395564e5744875d8e587e122dd3ae822d85fe395194f5d
fetched_at: '2026-06-28T22:37:25.510963+00:00'
product: protheus
section_id: 36607745462423
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINAPP001 - 500  variable
  is not an object
type: support-article
updated_at: '2026-03-23T21:26:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39014534721815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINAPP001-500-variable-is-not-an-object
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39014578028183) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao tentar acessar a rotina de Análise de Crédito Financeiro FINAPP001, o sistema apresenta a mensagem de erro: "500 - variable is not an object", impedindo o carregamento dos dados do cliente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39244066484759)  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O incidente ocorre devido à desatualização de componentes essenciais do sistema, especificamente a Biblioteca de Funções LIB e SMARTLINKLIB , ou devido a arquivos corrompidos na estrutura de pastas (HTTP-ROOT).

Para solucionar o problema, siga os passos abaixo:

Realize a atualização da [**LIB**](https://suporte.totvs.com/portal/p/10098/download#company/.)para a versão mais recente disponível no Portal do Cliente;

Aplique o [**pacote acumulado do Backoffice**](https://tdn.totvs.com/pages/releaseview.action?pageId=531017758)
