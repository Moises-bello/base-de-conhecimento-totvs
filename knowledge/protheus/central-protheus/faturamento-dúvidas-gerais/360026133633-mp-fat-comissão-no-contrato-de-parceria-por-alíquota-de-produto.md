---
article_id: 360026133633
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 23e74c64a1758c1002ae908a6dc0693ab67c619a95ee792d102526eccd70f8fb
fetched_at: '2026-06-28T22:38:31.174915+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Comissão no contrato de parceria por alíquota de produto
type: support-article
updated_at: '2021-04-28T15:54:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026133633-MP-FAT-Comiss%C3%A3o-no-contrato-de-parceria-por-al%C3%ADquota-de-produto
---

**Dúvida**

No contrato de parceria (**FATA400**), é possível que o sistema  trate a comissão do vendedor (**MATA040**), buscando a alíquota do cadastro de produto (**SB1**), sem o ter que digitar a alíquota no cabeçalho do contrato?

**Ambiente**Microsiga Protheus - todas as versões.  
  
**Solução**

Em avaliação a rotina FATA400, o tratamento de comissão é voltado apenas para o cabeçalho do contrato.

No tdn, na documentação de referência do Protheus que fala sobre a rotina, não há menção de outros campos para tratamento de comissão através do contrato de parceria, apenas menciona o preenchimento de comissão na tabela **ADA** , campo **ADA\_COMIS(1 a 5)**: - **<http://tdn.totvs.com/display/PROT/Parcerias+-+FATA400+-+Faturamento+-+P12>** - principais campos.
