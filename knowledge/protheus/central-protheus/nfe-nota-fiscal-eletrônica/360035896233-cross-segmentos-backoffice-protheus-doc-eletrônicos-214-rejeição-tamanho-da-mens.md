---
article_id: 360035896233
category: NFe - Nota Fiscal Eletrônica
content_hash: ca2b7fbaecc41ca6be98d64967377451cf77c7ed99defe716745edf6364b5347
fetched_at: '2026-06-28T22:40:00.461706+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 214 Rejeição :
  Tamanho da mensagem excedeu o limite estabelecido'
type: support-article
updated_at: '2023-03-06T13:32:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035896233--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-214-Rejei%C3%A7%C3%A3o-Tamanho-da-mensagem-excedeu-o-limite-estabelecido
---

**Ocorrência**Rejeição 214: Tamanho da mensagem excedeu o limite estabelecido  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Causa**Segundo o Manual de Orientação ao Contribuinte, a mensagem enviada aos WebServices para autorização não deve ultrapassar o tamanho de 500 KB. Caso seja encaminhado a Sefaz uma NF-e ou Lote de NF-e que possua um tamanho superior a 500 KB, a mensagem será descartado e retornado a rejeição "214 - Tamanho da mensagem excedeu o limite estabelecido".  
  
**Solução**

Separar a nota em 2 ou mais notas, pois não a SEFAZ não aceita XML maior que 500 kb.

Por padrão o ERP limita o tamanho do XML em 400k para ter uma margem de de segurança e a nota não for rejeitada.

Porém existe o parâmetro  MV\_XMLSIZE e o mesmo faz um tratamento pra diminuir ou aumentar o tamanho do XML para aqueles casos que estão maior  ou menor que 500k.

Este parâmetro deve ser preenchido com numero em milhar

Ex: 500000.

Caso o XML seja maior que 500kb é preciso refazer a nota com uma quantidade menor. Lembrando que isso não é uma limitação do ERP e sim da sefaz.

Só é possível verificar o tamanho do XML no momento da transmissão da nota.

Obs: O parâmetro deve ser criado manualmente  
  
Nome: MV\_XMLSIZE  
Tipo: numérico  
Descrição: Define o tamanho máximo do XML aceito pelo sistema.
