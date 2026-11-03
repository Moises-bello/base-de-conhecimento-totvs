---
article_id: 360033051413
category: RH - Folha de Pagamento
content_hash: bec36780a98e65cd1b25138f5d69ec51854f6b0bbaf0bd0aeaef00d33eefb4a5
fetched_at: '2026-06-28T22:44:14.712055+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como ratear verbas informadas e geradas na folha
  de pagamento
type: support-article
updated_at: '2024-09-09T19:56:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033051413-RH-Linha-Protheus-GPE-Como-ratear-verbas-informadas-e-geradas-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26251924277143) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como configurar o sistema para ratear verbas informadas e/ou geradas na folha de pagamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Criado o mnemônico P\_LRATINFO para informar se a verba informada (origem I) ou quando gerada (origem G) será ou não rateada de acordo com a programação de rateio.

**Mnemônico:****P\_LRATINFO** - RATEIA VERBAS INFORMADAS CONFORME PROGRAMAÇÃO DE RATEIO  
**Conteúdo padrão:** .F. -→ Não rateia a verba de acordo com a programação de rateio.

**Observações:**1. Para que seja usada a implementação é necessário trocar o conteúdo do mnemônico para .T.;  
2. Se o mnemônico P\_LRATINFO estiver como .T., **não importarão os Centros de Custos informados no lançamento** para o sistema, pois será respeitada apenas a configuração de rateio do funcionário;  
3. Se o mnemônico P\_LRATINFO estiver como .F., o sistema funcionará como era anteriormente, ou seja, **não rateará a verba e respeitará exatamente o que foi informado**.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
