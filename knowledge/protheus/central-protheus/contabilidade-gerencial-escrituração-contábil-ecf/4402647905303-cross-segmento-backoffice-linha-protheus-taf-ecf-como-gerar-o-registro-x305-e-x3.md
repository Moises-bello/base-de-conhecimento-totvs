---
article_id: 4402647905303
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 6fdfd8f0aabb34308e0d217ca7066a885ef201c9464f1ec56ae152176d08a608
fetched_at: '2026-06-28T22:40:48.938778+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF- ECF, Como gerar o registro
  X305 e X325
type: support-article
updated_at: '2021-06-14T19:26:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402647905303-Cross-Segmento-Backoffice-Linha-Protheus-TAF-ECF-Como-gerar-o-registro-X305-e-X325
---

**Dúvida**

Como gerar o registro X305 e/ou X325?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]  
  
**Solução**

**Estes registros devem ser preenchidos quando houver "ajustes ao preço parâmetro", ou seja, na extração dos dados rotina CTBS001 (SIGACTB) + ECF + exporta DIPJ= SIM, informe:**

**Registro X300= “Sim (para exportação) e/ou Registro X320= Sim (para importação).**

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402655899543/mceclip6.png)**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402655920279/mceclip7.png)**

Registro X305, Rotina TAFA334 (Registro x300, Operação com exterior- Exportações)

**O registro deve ser preenchido de forma manual no TAF.**

O campo "Ajust. Param (CAY\_AJUPAR) deve ser preenchido= SIM para que a aba "Ajustes do Preço Parâmetro da Exportação" seja habilitado.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402660285975/mceclip4.png)

**Registro X325, Rotina**TAFA335 **(Registro x320, Operações com exterior- importações),**

**O registro deve ser preenchido de forma manual no TAF.**

**O campo "Aj. Preço Pa" (CFV\_AJUPAR) deve ser preenchido= SIM para que a aba "Ajustes do Preço Parâmetro da Importação" seja habilitado.**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402655804951/mceclip5.png)

**Saiba mais:**

[Como atualizar a ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-Pacote-de-atualiza%C3%A7%C3%A3o-e-como-realizar-a-atualiza%C3%A7%C3%A3o-da-ECF-2021-leiaute-7)

[Composição dos Blocos/Registros ECF](https://tdn.totvs.com/pages/releaseview.action?pageId=192094180#Blocos/Registros-blocox)

[Página centralizadora ECF](https://tdn.totvs.com/display/public/PROT/ECF)
