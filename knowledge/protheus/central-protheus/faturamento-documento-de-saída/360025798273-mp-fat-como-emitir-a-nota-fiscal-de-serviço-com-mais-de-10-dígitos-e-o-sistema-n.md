---
article_id: 360025798273
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: ca6b4cbd3e8a0e40400b3cdae335aabcc910c539c06410b36f12c3da34b2bcde
fetched_at: '2026-06-28T22:38:45.144894+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - Como emitir a nota fiscal de serviço com mais de 10 dígitos e o
  sistema não permite aumentar.
type: support-article
updated_at: '2022-01-14T18:02:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025798273-MP-FAT-Como-emitir-a-nota-fiscal-de-servi%C3%A7o-com-mais-de-10-d%C3%ADgitos-e-o-sistema-n%C3%A3o-permite-aumentar
---

**Ocorrência**

Como emitir a nota fiscal de serviço com mais de 10 dígitos e o sistema não permite aumentar.  
  
**Ambiente**

Microsiga Protheus –  A partir da versão 12.1.17.  
  
**Solução**

Para alguns estados a transmissão de nota fiscal de serviço precisa de 15 dígitos para transmissão de NFS-e, para isso devera ser adequado todos os campo. **NFELETR**do Protheus para tamanho '15'

* **SF1-> F1\_NFELETR**
* **SF2-> F2\_NFELETR**
* **SF3-> F3\_NFELETR**
* **SFT-> FT\_NFELETR**
* **SE1-> E1\_NFELETR**​

Foi criado um novo grupo de campos específico para o número da nota fiscal eletrônica gerado pela prefeitura (GRUPO 124 COM TAMANHO DE 20).  
![](https://totvssuporte.zendesk.com/attachments/token/byZnPOdWmWS0e05GNeedroV08/?name=inline-123658301.png)​  
Valide em ambiente de testes se os campos mencionados acima participam do grupo e estão com tamanho 20 para atender a solicitação.
