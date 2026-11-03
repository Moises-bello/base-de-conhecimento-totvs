---
article_id: 360020084511
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 409cd83ed26e9805d8c88c9209f8aad3c12b2c57811758a26ff5c911e6ba9fa6
fetched_at: '2026-06-28T22:40:48.719674+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - X320 - UNIDADE
  DE MEDIDA '
type: support-article
updated_at: '2022-06-06T21:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020084511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-X320-UNIDADE-DE-MEDIDA
---

**Dúvida**

Não esta sendo gerado no registro X320 a unidade de medida para o arquivo TXT   
  
**Ambiente**   
Protheus – Contabilidade gerencial – A partir da versão P12

**Solução**

Para que seja gerada a Unidade de Medida ECF no arquivo texto, deverá ser realizada a amarração dos campos CFV\_UNIDAD x C1J\_UMECF através da rotina TAFA335.

Para isto, basta selecionar o campo Unid. Medida (CFV\_UNIDAD), clicar em Incluir ou Editar a informação previamente cadastrada, selecionar a Unidade de Medida desejada no campo UM ECF  (C1J\_UMECF). Neste campo estão os registros provenientes da Tabela Auto-Contida CHJ, sendo que é esta informação que é levada na geração dos blocos da ECF.

Veja mais

[MP - SIGACTB - ECF - Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
