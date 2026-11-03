---
article_id: 360047618393
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: ea7288eef198e9ccabbc745a857cb7d9db52c219ec655cdf280ffd66e569d22e
fetched_at: '2026-06-28T22:38:43.911096+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Prazo para Exclusão
  Notas Serviço (MATA521A) para o Município (ISS)
type: support-article
updated_at: '2022-09-08T17:07:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047618393-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Prazo-para-Exclus%C3%A3o-Notas-Servi%C3%A7o-MATA521A-para-o-Munic%C3%ADpio-ISS
---

**Ocorrência**

Prazo para Exclusão Notas Serviço (MATA521A) para o Município (ISS).

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

Ao tentar excluir uma Nota Fiscal de Serviços o sistema apresenta uma tela indicando: **O prazo para exclusão de NF de serviço para o município de Xxxxxx - XX é de até o último dia do mês subsequente da sua emissão. Data Limite: XX/XX/XX:**

![Imagem1.jpg](https://tdn.totvs.com/download/attachments/267797581/Imagem1.jpg?version=1&modificationDate=1489079174000&api=v2)

O prazo para **exclusão** das **notas** que geraram **ISS** (**NF de serviços**) é determinado pelos parâmetros **MV\_EXCNFS**(**Limite de dias para exclusão de NF**) e **MV\_TIPOPRZ** (**Tipo de prazo para exclusão das notas fiscais de serviço**).  
  
**Solução**Necessário verificar a configuração dos parâmetros:   
**1.** MV\_TIPOPRZ = 1 e MV\_EXCNFS = 15 - Essa configuração indica que: Até o dia 15 do mês subsequente é possível excluir notas que geraram título de ISS;

2. MV\_TIPOPRZ = 2 e MV\_EXCNFS = 15 - Essa configuração indica que: Até 15 dias após emissão é possível excluir notas que geraram título de ISS.

Saiba Mais: **<https://tdn.totvs.com/pages/viewpage.action?pageId=267797581>**
