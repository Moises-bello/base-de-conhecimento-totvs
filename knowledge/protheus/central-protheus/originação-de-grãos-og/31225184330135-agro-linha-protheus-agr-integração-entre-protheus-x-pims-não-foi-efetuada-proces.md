---
article_id: 31225184330135
category: Originação de Grãos (OG)
content_hash: 296eb4490b4bc667208926040813d781f5d0ee87c1f08cb2c0b1f1ffdbfc2433
fetched_at: '2026-06-28T22:45:40.926385+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Integração entre Protheus X PIMS não foi efetuada.
  Processado pelo ERP, aguardando valoração
type: support-article
updated_at: '2025-10-02T13:33:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31225184330135-Agro-Linha-Protheus-AGR-Integra%C3%A7%C3%A3o-entre-Protheus-X-PIMS-n%C3%A3o-foi-efetuada-Processado-pelo-ERP-aguardando-valora%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31225184310167) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**  
No módulo Faturamento, ao gerar um romaneio com pesagem do tipo **1-Entrada** por produção, algumas horas depois ou no dia seguinte este romaneio é reaberto para ajuste é apresentada a mensagem **Integração entre Protheus X PIMS não foi efetuada. Processado pelo ERP, aguardando valoração**.  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Causa**  
Esse incidente ocorre, ao gerar um romaneio com pesagem do tipo **1-Entrada** por produção, algumas horas depois ou no dia seguinte este romaneio é reaberto para ajuste, surge a mensagem de aviso "**aguardando valoração**".  
  
**Solução**A mensagem de "**aguardando valoração**", é uma validação do **PIMS**, o qual foi integrado com o estoque gerando movimentação e impede que o boletim de pesagem será modificado.   
No **Protheus** realizado ajuste no reabrir e cancelar do romaneio para integrar com o **PIMS**, validando se o romaneio pode ser reaberto ou cancelado.  
Na integração ao reabrir ou cancelar o romaneio no **Protheus**, caso o **PIMS** retorne permitindo a integração, o boletim de pesagem do **PIMS** será excluído e o romaneio do **Protheus** será reaberto ou cancelado. Ao confirmar novamente o romaneio do **Protheus** o boletim de pesagem será novamente incluído. Caso o **PIMS** não permita integrar ao reabrir ou cancelar o romaneio com status **Confirmado**, o romaneio permanecerá confirmado.  
Se na integração a mensagem **"Processado pelo ERP, aguardando valoração."** for apresentada, é necessário uma ação lá no **PIMS** para o boletim de pesagem, para estornar a movimentação e assim permitir novamente a integração.
