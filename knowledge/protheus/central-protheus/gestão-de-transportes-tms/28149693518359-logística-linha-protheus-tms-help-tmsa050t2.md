---
article_id: 28149693518359
category: Gestão de Transportes (TMS)
content_hash: 5b488a4ad39f6150b7da7d0b7a1da8e00cb95f839faf3ed85b9de44fc0c54004
fetched_at: '2026-06-28T22:45:29.273624+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - HELP TMSA050T2
type: support-article
updated_at: '2024-11-29T13:36:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28149693518359-Log%C3%ADstica-Linha-Protheus-TMS-HELP-TMSA050T2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28149693505175) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**O que significa o help **TMSA050T2 - O Cliente/Loja remetente deve ser o mesmo Cliente/Loja da operação de transporte, da viagem vinculada ao lote** e como proceder?   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O help **TMSA050T2** é uma validação exclusiva do processo de apontamento de operação de chegada em cliente, o qual valida quando o lote criado está vinculado a uma viagem que está com status **Em trânsito** e existe um apontamento de **chegada em cliente,** que é a operação definida no parâmetro **MV\_ATVCHGC** sem que exista o apontamento de **saída de cliente,** que é a operação definida no parâmetro **MV\_ATVSAIC.** Neste cenário, o Sistema valida se o remetente do documento é o mesmo remetente da operação de **chegada em cliente,** campo **DTW\_CODCLI**, pois o processo de operação de chegada e saída de cliente deve ser utilizado somente para carregar documentos em que o remetente é o cliente que foi apontado a chegada.  
  
Com isso, se precisar carregar um documento que seja de outro cliente remetente, deve-se utilizar o processo de apontamento de operação de **chegada em ponto de apoio**.  
  
**Saiba mais**Documentação sobre processo de chegada em cliente: [DT MELHORIAS NA VIAGEM DE ENTREGA](https://tdn.totvs.com.br/display/public/PROT/DT+MELHORIAS+NA+VIAGEM+DE+ENTREGA)  
Conceito do processo de ponto de apoio: [Conceito - Ponto de Apoio na viagem](https://tdn.totvs.com.br/display/public/PROT/Conceito+-+Ponto+de+Apoio+na+viagem)  
Exemplo de uso do ponto de apoio: [Exemplos de Utilização - Carregamento em Ponto de Apoio Viagem Modelo 3 (TMSAF60 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=572962382)  
**How To** sobre o processo de ponto de apoio : [HOW TO SIAGATMS PONTO DE APOIO](https://www.youtube.com/playlist?list=PLc53uWgxEXo_-EAb5RhyIsKpWA0kFYMWk)
