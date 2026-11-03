---
article_id: 360036015514
category: Originação de Grãos (OG)
content_hash: 7b2523ec881ce10b1e927e7971264cd886b1296908a1ca400c96c0f8adaea07e
fetched_at: '2026-06-28T22:45:41.058388+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Movimentações de transferência no gestor da entidade
type: support-article
updated_at: '2025-06-24T11:35:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036015514-Agro-Linha-Protheus-AGR-Movimenta%C3%A7%C3%B5es-de-transfer%C3%AAncia-no-gestor-da-entidade
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20447960314647)***Tempo aproximado para leitura:**00:01:30 min**  
**Dúvida**Quais são as movimentações de transferência permitidas pelo sistema na rotina **OGA450 - Gestor da Entidade**?  
  
 **Ambiente**  
TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**As movimentações de transferência que podem ser efetuadas na rotina **OGA450** são as seguintes: Contratos

* **Transferência entre contratos de compra:** são gerados romaneios sem pesagem automaticamente para efetivar a movimentação.  
   Para o contrato de origem é gerado um romaneio com operação de saída do tipo **Devolução de Compra**. Para o contrato de destino é gerado um romaneio com operação de entrada do tipo **Entrada por Compra**;
* **Transferência entre contratos de armazenagem de terceiros:** a movimentação fiscal é gerada automaticamente.   
  Para o contrato de origem é gerado um romaneio sem pesagem com operação de saída do tipo **Devolução de Depósito**. Para o contrato de destino é gerado um romaneio sem pesagem com operação de entrada do tipo **Entrada para Depósito**;
* **Transferência de contrato de armazenagem de terceiros para contrato de compra:** Para o contrato origem é gerado automaticamente um romaneio sem pesagem com operação de saída do tipo **Devolução de Depósito**. Para o contrato de destino é gerado automaticamente um romaneio com operação de entrada do tipo **Entrada por Compra**;
* **Transferências de contrato de compra** **para** **contrato de armazenagem:**É gerado automaticamente um romaneio sem pesagem com operação de saída do tipo **Devolução de Compra** para o contrato origem. Para o contrato de destino é gerado automaticamente um romaneio sem pesagem com operação de entrada do tipo **Entrada para Depósito**.
