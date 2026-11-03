---
article_id: 360025641673
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: d6ac265fc896c18c3f41b71a4c9cee7709eb5e1788e1efb7731b87fe6056fce7
fetched_at: '2026-06-28T22:42:41.017021+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campos D3_LOTECTL, D3_VALID e D3_POTENCI
  não são visíveis no MATA250
type: support-article
updated_at: '2021-07-15T18:11:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025641673-Manufatura-Linha-Protheus-SIGAPCP-Campos-D3-LOTECTL-D3-VALID-e-D3-POTENCI-n%C3%A3o-s%C3%A3o-vis%C3%ADveis-no-MATA250
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:57 min**  
**Dúvida**Como proceder quando ao realizar um apontamento através da rotina **MATA250 - Apontamento Simples**, os campos  **D3\_LOTECTL - Lote**, **D3\_VALID - Validade do Lote Informado** e **D3\_POTENCI - Potencia do Lote** não são apresentados em tela?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Além das configurações de permissão dos campos no **SIGACFG - Configurador**, veja também o conteúdo do parâmetro **MV\_PRODAUT - Gera lançamentos automáticos de produção das ordens de produções vinculadas com a ordem de produção pai**, quando o conteúdo desse parâmetro é **T** esses campos não são apresentados na tela de inclusão, sendo apresentados somente ao confirmar o registro de apontamento.
