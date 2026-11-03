---
article_id: 360024691031
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 99cd020f206a2963f8d376e239149ba66acef2e12ab97c70807650cc8a957e7c
fetched_at: '2026-06-28T22:37:21.524510+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como identificar os
  títulos gerados pelo módulo de Gestão de Contratos ?
type: support-article
updated_at: '2025-12-01T16:39:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024691031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-identificar-os-t%C3%ADtulos-gerados-pelo-m%C3%B3dulo-de-Gest%C3%A3o-de-Contratos
---

**Dúvida**Como identificar os títulos gerados pelo módulo de Gestão de Contratos ?

**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80  
  
  
**Solução**

Os títulos gerados nas medições pelo SIGAGCT, possuem o prefixo MED, sendo que para títulos a pagar e natureza é definida pelo parâmetro **MV\_CNNAT**, e para títulos a receber e natureza definida pelo parâmetro **MV\_CNNATCL**.  
Para ambos os títulos, o número utilizado é o Sequencial ou da Medição conforme a configuração do parâmetro **MV\_NMEDTIT** e o tipo DP (duplicata) com as parcelas definidas sequenciais, conforme condição de pagamento.

Caso tenha gerado título provisório e ainda não tenha ocorrido a substituição, é possível identificar através dos campos relacionados ao contrato:

'Num. Contrat' (***E1\_MDCONTR***),

'Num. Medição' (***E1\_MEDNUME***),

'Num. Parcela' (***E1\_MDPARCE***),

'Revisão' (***E1\_MDREVIS***).

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)

[MP - SIGAGCT - Parâmetro MV\_NMEDTIT - Numeração Título gerado na Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048576874-MP-SIGAGCT-Par%C3%A2metro-MV-NMEDTIT-Numera%C3%A7%C3%A3o-T%C3%ADtulo-gerado-na-Medi%C3%A7%C3%A3o)
