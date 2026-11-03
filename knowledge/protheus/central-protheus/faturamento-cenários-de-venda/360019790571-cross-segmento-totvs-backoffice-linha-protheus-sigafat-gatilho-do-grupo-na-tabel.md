---
article_id: 360019790571
category: Faturamento - Cenários de Venda
content_hash: eda61bab019a4c20bd90c270e0a999db5df7f99fa72624d4572579ddb0bb20c3
fetched_at: '2026-06-28T22:38:33.939843+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Gatilho do Grupo
  na tabela de preço
type: support-article
updated_at: '2023-01-31T13:08:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019790571-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Gatilho-do-Grupo-na-tabela-de-pre%C3%A7o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Configurar o gatilho para trazer a descrição na Tabela de Preços no módulo Faturamento.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - a partir da versão 11.  
  
**Solução**Para solucionar, siga os passo abaixo:

1. Acessar o Configurador “SIGACFG” >> Base de Dados >> Dicionário >> Bases de Dados;
2. Ir em Gatilho;
3. Localizar o campo “**DA1\_GRUPO**”;
4. Editar a sequência “002”;
5. No campo regra, informar o conteúdo “**SBM**->**BM\_DESC**”;
6. Em tabela de preço, valide que a alteração foi realizada.

**Para visualização das telas de configuração, acesse a FAQ:** [FAT0270\_Gatilho do Grupo na tabela de preço](http://tdn.totvs.com/pages/viewpage.action?pageId=394215078)
