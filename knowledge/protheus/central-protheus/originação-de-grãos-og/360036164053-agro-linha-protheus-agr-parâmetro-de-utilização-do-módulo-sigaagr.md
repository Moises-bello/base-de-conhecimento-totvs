---
article_id: 360036164053
category: Originação de Grãos (OG)
content_hash: e1e5548067040acd0aa20652e683091633ef96555809179a50e05a32d0b8d9a4
fetched_at: '2026-06-28T22:45:41.184498+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Parâmetro de utilização do módulo SIGAAGR
type: support-article
updated_at: '2025-06-24T19:17:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164053-Agro-Linha-Protheus-AGR-Par%C3%A2metro-de-utiliza%C3%A7%C3%A3o-do-m%C3%B3dulo-SIGAAGR
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20475593795863)***Tempo aproximado para leitura: **00:00:25 min**   
  
**Dúvida**Para que serve o parâmetro **MV\_SIGAAGR**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
O parâmetro **MV\_SIGAAGR - Utiliza módulo de Gestão Agroindústria** é do tipo lógico e está localizado na rotina **OGX007 - Funções Padrões do SIGAAGR** para a exibição e gravação automática das mensagens de inconsistências ocorridas nos modelos do módulo de originação. Possui duas opções:

* Se **.T.** indica que o módulo **SIGAAGR** está em utilização e tem integrações com os demais módulos;
* Se **.F.** não utiliza o módulo **SIGAAGR**.
