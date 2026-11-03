---
article_id: 360038126774
category: Originação de Grãos (OG)
content_hash: 0f82757784634719c43607591f6076dffbfb66ddb93a70aca5865d4f026c5289
fetched_at: '2026-06-28T22:45:41.306869+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro MV_AGRORI
type: support-article
updated_at: '2025-06-13T15:21:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038126774-Agro-Linha-Protheus-AGR-Par%C3%A2metro-MV-AGRORI
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20494215175703)***Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Para que serve o parâmetro **MV\_AGRORI - Utiliza o Processo Originação do Módulo SIGAAGR**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O parâmetro **MV\_AGRORI** é do tipo **Lógico** e está localizado na rotina de funções padrão para **Exibição e Gravação automática das Mensagens de Inconsistências Ocorridas nos Modelos do Módulo de Originação** - **OGX007**.   
  
Possui duas opções:

* Se **.T. - True**, indica que o módulo **Originação** do **SIGAAGR** está em utilização, e tem integrações com os demais módulos.
* Se **.F. - False**, não utiliza o módulo **SIGAAGR – Originação**.
