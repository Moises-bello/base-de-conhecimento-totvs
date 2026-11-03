---
article_id: 360043778414
category: Originação de Grãos (OG)
content_hash: 281675ec0644f8df275aad166e9965843b6ed4b05b5ddd893e6e3f9e1bf69836
fetched_at: '2026-06-28T22:45:39.371818+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Entrada por Produção, está validando o campo
  D3_TM
type: support-article
updated_at: '2025-04-07T20:34:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043778414-Agro-Linha-Protheus-AGR-Entrada-por-Produ%C3%A7%C3%A3o-est%C3%A1-validando-o-campo-D3-TM
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20325938557079)*** Tempo aproximado para leitura: **00:00:45 min**  
 **Ocorrência**No módulo de **Originação**, ao tentar realizar o **OGA251 - Romaneio** tipo **1 - Entrada por produção** é apresentada a mensagem **AJUDA D3\_TM Código do tipo de movimento, sendo: Produção - Código menor que 500**

![tm01.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360059889993)

**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
 **Causa**Esse incidente ocorre, pois é necessário o uso do parâmetro **MV\_ARM251A - Tipo de movimentação de Estoque** parametrizado com uma **TM** - **Tipo de Movimento** do tipo **Devolução**, entrada simples.  
  
 **Solução**Parametrizar o parâmetro **MV\_ARM251A** com o tipo de movimento **001 - Devolução** cadastrado no **MATA230 - Tipo de Movimentações.**

**![tm02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360059001594)**
