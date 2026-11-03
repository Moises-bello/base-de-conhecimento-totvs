---
article_id: 4409312876823
category: RH - Cálculo PLR
content_hash: bb0c376c3b07a4fef64b3e06da2efef5c8dc19c3000cfc9478b2b985b166be17
fetched_at: '2026-06-28T22:43:12.889331+00:00'
product: protheus
section_id: 360010855894
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar a base de IR do PLR quando houve
  mais de um pagamento dentro do mesmo ano de cálculo com verbas diferentes
type: support-article
updated_at: '2024-07-18T20:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409312876823-RH-Linha-Protheus-GPE-Como-parametrizar-a-base-de-IR-do-PLR-quando-houve-mais-de-um-pagamento-dentro-do-mesmo-ano-de-c%C3%A1lculo-com-verbas-diferentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24992359407895) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao efetuar o cálculo de PLR, foi apresentado a base de IR menor do que o valor pago ao funcionário durante o ano de cálculo.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**No cálculo do PLR o sistema não considera para compor a base de IR um pagamento realizado dentro do mesmo ano de cálculo em uma verba sem ID.  
  
**Solução**Para que o sistema considere todas os pagamentos com verbas diferentes dentro do mesmo ano de cálculo, será necessário informar as verbas no Mnemônico **P\_PDBIRPLR em Atualizações > Definições Cálculos > Mnemônicos (GPEA300)**.**Importante:** O mnemônico deve ser preenchido com as verbas que possuem incidência para IR de PLR mas não possuem identificador de cálculo, para que em um segundo cálculo com pagamento no mesmo ano, elas possam ser somadas na base de IR.

Caso exista mais de uma verba, o preenchimento deve seguir este exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409311997719)

**Saiba mais:**

[Mnemônico P\_PDBIRPLR](https://tdn.totvs.com/pages/viewpage.action?pageId=632830141)

[RH - Cálculo PLR](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855894-RH-C%C3%A1lculo-PLR)
