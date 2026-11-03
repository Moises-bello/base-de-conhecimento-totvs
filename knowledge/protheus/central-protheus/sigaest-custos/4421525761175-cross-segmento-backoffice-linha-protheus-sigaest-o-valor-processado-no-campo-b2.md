---
article_id: 4421525761175
category: SIGAEST - CUSTOS
content_hash: ba45a4d5d983b6c829edc7157af36497aaaa38b27a10597189ecf900aba64409
fetched_at: '2026-06-28T22:39:02.289789+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O valor processado
  no campo B2_CMFIM1 é repassado para o campo B2_CM1?
type: support-article
updated_at: '2025-03-12T12:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421525761175-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-valor-processado-no-campo-B2-CMFIM1-%C3%A9-repassado-para-o-campo-B2-CM1
---

**Dúvida**  
Como é feita a atualização do campo **"C Unitario" (B2\_CM1)** com **"C Unit 1a M" (B2\_CMFIM1)**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Por legado, ao final do processamento da rotina de **Custo Médio** (**MATA330**) o valor processado no campo **"C Unit 1a M" (B2\_CMFIM1)** é repassado para o campo **"C Unitario" (B2\_CM1)**, porém, caso não seja desejado este repasse, é possível realizar alteração por meio do parâmetro **MV\_330ATCM** =. F.

Caso não tenha o parâmetro no arquivo **SX6**, realize a atualização do dicionário de dados e execute o UPDDISTR (seguindo todos os procedimentos de segurança, como backups, teste em homologação, etc.).

**Parâmetro**: MV\_330ATCM  
**Tipo**: Lógico  
**Cont**. Por: .F.

**Saiba mais:**

* [O valor processado no campo B2\_CMFIM1 é repassado para o campo B2\_CM1](https://tdn.totvs.com/x/aN3yE)
* *[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
