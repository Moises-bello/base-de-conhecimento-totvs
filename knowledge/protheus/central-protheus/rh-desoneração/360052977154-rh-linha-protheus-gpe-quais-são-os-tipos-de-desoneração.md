---
article_id: 360052977154
category: RH - Desoneração
content_hash: 7b695361840e3f429101ef7c0e79a2a9a10a6a32a5b01dc603a950ec3d3621b3
fetched_at: '2026-06-28T22:43:42.305620+00:00'
product: protheus
section_id: 360003109152
source: central-protheus
title: RH - Linha Protheus - GPE - Quais são os tipos de Desoneração
type: support-article
updated_at: '2025-03-18T15:02:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052977154-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-tipos-de-Desonera%C3%A7%C3%A3o
---

**Dúvida**Quais são os tipos de Desoneração?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**

**Desoneração Pura** – Sistema calculará apenas o valor da alíquota sobre faturamento da empresa. Não será apresentado a verba de id 0148. Será apresentado apenas a verba de id 0973.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087460674)

**Desoneração Mista/Concomitante** – Sistema calculará o valor da alíquota sobre o faturamento desonerado e calculará uma alíquota reduzida sobre a folha de pagamento. Sendo assim, serão apresentadas na folha as verbas de id 0973 e 0148.  
 ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087461894)

**OBS:** Para o caso de empresas com desoneração mista, se o faturamento tiver a parte desonerada maior que 95% do total faturado, não será calculada a verba de id 0148.  Se a situação for contrária, sendo a parte não desonerada maior que 95%, o sistema não calculará a verba de id 0973. No caso de empresas concomitantes não existe a validação desta regra.
