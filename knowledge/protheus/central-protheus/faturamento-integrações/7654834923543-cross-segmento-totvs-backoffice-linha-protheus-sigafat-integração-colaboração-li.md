---
article_id: 7654834923543
category: Faturamento - Integrações
content_hash: 2e2933faeae37688be52302547bbd0f205a875468f741afa76f95347d4b2936d
fetched_at: '2026-06-28T22:38:26.595570+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: ' Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Integração
  Colaboração Licença para uso '
type: support-article
updated_at: '2022-07-22T18:42:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7654834923543--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-Colabora%C3%A7%C3%A3o-Licen%C3%A7a-para-uso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Para importar arquivos gerados pelo Neogrid via Totvs Colaboração é necessário uma licença específica ?  
  
**Ambiente**Microsiga Protheus -  a partir da versão 12.  
  
**Solução**

Sim, é necessário uma licença específica chamada **3100 (TOTVS\_COLAB\_ONDEMAND).**   
  
Caso não exista esta licença, o sistema movimenta o XML da pasta In para Lidos, grava a tabela CKOCOL com o campo CKO\_FLAG = 0 (que é o status de documento não importado) e não grava o Pedido de Vendas  
  
No Console.Log o sistema pode apresentar a mensagem abaixo:

**FWAlertError -> Ambiente não licenciado para o modelo TOTVS Colaboração**

**Links Auxiliares :**

[MP - FAT - Quais Pré requisitos para integração de cadastros do Totvs Colaboração com pedido de venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026580194-MP-FAT-Quais-Pr%C3%A9-requisitos-para-integra%C3%A7%C3%A3o-de-cadastros-do-Totvs-Colabora%C3%A7%C3%A3o-com-pedido-de-venda?source=search)  
  
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - COLABORAÇÃO - Legenda dos campos: DS\_STATUS, CKO\_STATUS, DS\_TIPO E CKO\_FLAG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037713954-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-COLABORA%C3%87%C3%83O-Legenda-dos-campos-DS-STATUS-CKO-STATUS-DS-TIPO-E-CKO-FLAG?source=search)
