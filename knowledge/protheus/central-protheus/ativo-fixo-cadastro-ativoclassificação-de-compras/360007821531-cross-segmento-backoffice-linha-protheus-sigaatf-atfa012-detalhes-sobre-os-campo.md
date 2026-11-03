---
article_id: 360007821531
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 2e8339f23234dc0a5a7e03c3ecf5dc5d1250cf552e14d881c419047479d00ad6
fetched_at: '2026-06-28T22:41:48.374152+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 :Detalhes sobre
  os campos N3_VRDBAL1 e N3_VRDACM1
type: support-article
updated_at: '2022-09-28T13:47:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007821531-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Detalhes-sobre-os-campos-N3-VRDBAL1-e-N3-VRDACM1
---

**Dúvida**

* Como é gerado o calculo no campo N3\_VRDBAL1?
* Detalhes sobre os campos N3\_VRDBAL1 e N3\_VRDACM1
* Bens com Depreciação acumulada como deve ser informado ?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12

**Solução**

O valor gerado no campo N3\_VRDBAL1 refere-se ao último balanço do período da depreciação na moeda1,  o valor de depreciação é gerado a cada calculo com base na taxa de depreciação do bem, acumulando este valor no campo N3\_VRDBAL1.  
Este campo é zerado na execução da rotina de virada anual.

O campo N3\_VRDACM1 irá demonstrar o valor da depreciação acumulada. Cada calculo realizado  no mês é acumulado neste campo, até atingir o valor total do bem que indica o fim da depreciação do bem.

É utilizado também na inclusão de um bem que já possui um saldo de depreciação acumulado e este saldo deve ser informado neste campo.

Segue link de calculo de depreciação, que contém características do calculo e métodos de depreciação gerencial.

<http://tdn.totvs.com/pages/releaseview.action?pageId=6067612>

Links sobre virada Anual

<http://tdn.totvs.com/display/PROT/ATF0001+Rotina+Virada+Anual>

<http://tdn.totvs.com/pages/viewpage.action?pageId=43549203>
