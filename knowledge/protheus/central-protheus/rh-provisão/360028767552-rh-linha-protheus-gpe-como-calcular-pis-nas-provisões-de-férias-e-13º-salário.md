---
article_id: 360028767552
category: RH - Provisão
content_hash: 0ac06c1ca460e8829eabbc08ffe2e71b57be8ac5894242a5dd82c69c18d5b46a
fetched_at: '2026-06-28T22:43:55.715657+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como Calcular PIS nas Provisões de Férias e 13º
  Salário
type: support-article
updated_at: '2022-09-15T10:20:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028767552-RH-Linha-Protheus-GPE-Como-Calcular-PIS-nas-Provis%C3%B5es-de-F%C3%A9rias-e-13%C2%BA-Sal%C3%A1rio
---

**Dúvida**Como calcular o PIS nas Provisões de Férias e 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O PIS sobre a folha de pagamento é uma obrigação tributária de 1%, principalmente devida por entidades sem fins lucrativos, que é calculado sobre a folha de pagamento.

Para calcular o Encargo de PIS sobre as provisões de Férias e 13º Salário, realize os seguintes passos:1. É necessário ter os Identificadores de Cálculo abaixo vinculados à uma verba. Para cadastrar ou localizar as verbas, Acesse: Atualizações / Definições de Cálculo / Verbas / Procure os Identificadores abaixo, e se não localizar, será necessário cadastrá-los:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030016952/mceclip1.png)

2. Verifique se a verba com Identificador de Cálculo 0229 está com o campo "Percentual" (RV\_PERC) está preenchido com 1,000:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078693733/mceclip1.png)

3. Prossiga com o Cálculo das provisões de Férias e 13º Salário normalmente;  
  
4. Ao emitir o Relatório de Provisão, o sistema apresenta uma nova coluna, com o cálculo de 1% de PIS:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077548014/mceclip2.png)

Para mais informações, acesse: <https://tdn.totvs.com/pages/viewpage.action?pageId=286022031>
