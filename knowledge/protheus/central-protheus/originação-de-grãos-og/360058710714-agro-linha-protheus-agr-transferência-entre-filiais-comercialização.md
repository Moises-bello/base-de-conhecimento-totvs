---
article_id: 360058710714
category: Originação de Grãos (OG)
content_hash: 2f992099934e264f0f9f7919bcfce3136fba0213aa7d13e24af4bd6cc238ab3e
fetched_at: '2026-06-28T22:45:45.197514+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Transferência entre Filiais Comercialização
type: support-article
updated_at: '2025-06-23T15:53:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058710714-Agro-Linha-Protheus-AGR-Transfer%C3%AAncia-entre-Filiais-Comercializa%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20855219529879)**Tempo aproximado para leitura:**00:01:30 min**  
**Dúvida**Como efetuar a transferência entre **Filiais** na **Comercialização**?   
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - A partir da versão 12  
  
**Solução**Para solucionar está dúvida, há duas formas de proceder com esta operação no módulo **SIGAAGR - Originação de Grãos**:  
Através do **Romaneio com Pesagem - OGA250** e **Romaneio sem Pesagem - OGA251**, e para utilizar essas rotinas é necessário:

**1.** Registrar um **Contrato de Vendas - OGA290** na **Filial de origem**, sendo que a entidade **cliente do contrato será a entidade correspondente a filial de destino**.  
No contrato de **Vendas**, informar **Tipo de Entrada e Saída - TES** de saída **transferência entre filiais**, e demais configurações fiscais necessárias para a operação.

**2.** Registrar um **Contrato de Compras - OGA280** na **Filial de destino**, sendo que a **entidade fornecedor do contrato será a entidade correspondente a filial de origem**. No **Contrato de Compra**s, informar **TES** de entrada **transferência entre filiais**, e demais configurações fiscais necessárias para a operação.

Para a saída, na **Filial de origem**, criar romaneio no **OGA250** ou **OGA251**, informando o tipo **4 - Saída por Venda**, informar **contrato de vendas**, **pesagem** e **classificação**. **Atualizar** e **confirmar** para gerar a nota fiscal da transferência.   
Para a entrada, na **Filial de destino** criar romaneio no **OGA250** ou **OGA251**, informando o tipo **5 - Entrada por Compra**, informar **contrato de compras**, **pesagem** e **classificação**, **bem como as informações da nota fiscal recebida**. Atualizar e confirmar para efetuar o recebimento da nota fiscal no destino.  
  
**Saiba mais**Para mais informações acesse os *links* abaixo:[MP – AGR – O que é transferência entre Filiais na Comercialização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000236042)  
[MP – AGR – Romaneios tipos B Saída por Transferência e A Entrada por Transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060585453)
