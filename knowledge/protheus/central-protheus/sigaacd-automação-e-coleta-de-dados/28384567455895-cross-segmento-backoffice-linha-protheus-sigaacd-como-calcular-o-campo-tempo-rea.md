---
article_id: 28384567455895
category: SIGAACD - Automação e Coleta de Dados
content_hash: fbcfa0eb3ea22abdb73e477de26cca8ffff322f1c18e478cacf5e2c5aa93de4c
fetched_at: '2026-06-28T22:39:12.531266+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como calcular o campo
  "Tempo Real" (H6_TEMPO) no ACD corretamente?
type: support-article
updated_at: '2025-01-09T13:23:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28384567455895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-calcular-o-campo-Tempo-Real-H6-TEMPO-no-ACD-corretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28384551708951) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como calcular o tempo usando a rotina monitoramento da produção (**ACDA080**), no campo "Tempo Real" (H6\_TEMPO)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

Ao usar a rotina "Monitoramento da Produção" (**ACDA080**), e o campo "Tempo Real" (**H6\_TEMPO**) está sendo calculado de forma incorreta, segue a parametrização para ajuste do calculo no campo:

* Usar o parâmetro **[MV\_CBCALPR](https://tdn.totvs.com/pages/releaseview.action?pageId=235596091) = .F.** (Quando o parâmetro está falso, usará o calculo padrão da rotina Modelo II de apontamento (**MATA681**), inclusive pode considerar o tempo de turnos diferentes);
* Usar também o parâmetro **[MV\_USACALE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027589692-Manufatura-Linha-Protheus-SIGAPCP-Par%C3%A2metro-MV-USACALE) = .F.** (Maiores detalhes clicar no parâmetro para obter informações sobre a documentação do mesmo).

Parametrizando dessa forma o campo "Tempo Real" (**H6\_TEMPO**) será calculado corretamente no SIGAACD, tanto na rotina **ACDV025** e na rotina **ACDA080**.

*Saiba Mais:*

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA080 - Pontos de Entrada disponíveis na rotina.*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13393323979927-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA080-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina)
