---
article_id: 360034008973
category: Originação de Grãos (OG)
content_hash: 681faa784e7b4108cb2fc6b9c5f275c952f33704468b66f5ce573dacade776a4
fetched_at: '2026-06-28T22:45:40.949340+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Linha Protheus - Parâmetro MV_OGLIBPV Avaliação
  e liberação crédito pedido romaneio AgroComercial
type: support-article
updated_at: '2025-01-03T19:40:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034008973-Agro-Linha-Protheus-AGR-Linha-Protheus-Par%C3%A2metro-MV-OGLIBPV-Avalia%C3%A7%C3%A3o-e-libera%C3%A7%C3%A3o-cr%C3%A9dito-pedido-romaneio-AgroComercial
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20412937885719)***Tempo aproximado para leitura: **00:00:35 min**  
**Dúvida**Para que serve o parâmetro **MV\_OGLIBPV - Gera docto fiscal do originação**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_OGLIBPV** é do tipo caractere e é utilizado para determinar a geração do documento fiscal no módulo de Originação de Grãos*.* Se o parâmetro não existir é considerada a opção 2.

* **Opção 1 ->** Não realiza nenhuma ação, o usuário deve analisar o porquê do bloqueio e se for o caso utilizar a rotina do faturamento **MATA440** - **Liberação Manual do Faturamento** para liberar o documento;
* **Opção 2 ->** Força liberar o crédito ou outros Bloqueios, e se for o caso, é necessário utilizar a rotina **MATA440**;
* **Opção 3 ->** Força liberar o crédito e chama em tela a rotina **MATA440**, caso ele ainda esteja bloqueado.
