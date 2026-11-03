---
article_id: 360059089413
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 6763d655c7a1e16e107bde395627a2c7630841f6cd783c49fd4ac6d419f8c4d5
fetched_at: '2026-06-28T22:42:42.089526+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Conceito do Campo Estrutura Similar
  na inclusão de Pré-Estrutura
type: support-article
updated_at: '2023-02-10T18:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059089413-Manufatura-Linha-Protheus-SIGAPCP-Conceito-do-Campo-Estrutura-Similar-na-inclus%C3%A3o-de-Pr%C3%A9-Estrutura
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:25 min**  
**Dúvida**Como funciona a carga para uma pré-estrutura através do preenchimento do **Estrutura Similar** no **MATA202 - Pré-Estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo **Estrutura Similar** tem por objetivo ser um facilitador no processo de inclusão de uma **pré-estrutura**, através dele podemos informar um produto que já tenha uma **estrutura** ou **pré-estrutura** e essa **estrutura** ou **pré-estrutura** ser copiada para o novo produto.  
Para tanto veja na lista de parâmetros do **MATA202** como está preenchido o parâmetro **Informação Similar**, se está preenchido com **Estrutura**, ao informar um código de produto no campo **Estrutura Similar** o Sistema procura pela estrutura desse item cadastrada no **MATA200 - Cadastro de Estrutura** e carrega esses dados em tela, se estiver preenchido com **Pré-Estrutura**, o Sistema procura pela **pré-****estrutura** desse item cadastrada no **MATA202**.

**Exemplo**Se desejarmos incluir uma estrutura para o produto AB, porém a composição desse item é similar ao do produto AA, que já tem uma pré-estrutura ou estrutura cadastrada, podemos através do campo estrutura similar, indicar que desejamos fazer a carga dessa estrutura ou pré-estrutura previamente cadastrada e assim realizar somente os ajustes pertinentes à produção do produto AB.
