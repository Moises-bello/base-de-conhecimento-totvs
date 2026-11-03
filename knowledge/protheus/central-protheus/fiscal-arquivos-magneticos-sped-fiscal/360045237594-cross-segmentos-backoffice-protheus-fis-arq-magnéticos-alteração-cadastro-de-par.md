---
article_id: 360045237594
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: d14e98b3a049f2c653039ab426caebe71c39a31b8b3a4e4ffdf9394537362db9
fetched_at: '2026-06-28T22:42:00.890826+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - ALTERAÇÃO CADASTRO
  DE PARTICIPANTE REGISTRO 0175 SPED FISCAL
type: support-article
updated_at: '2024-06-20T18:32:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045237594-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-ALTERA%C3%87%C3%83O-CADASTRO-DE-PARTICIPANTE-REGISTRO-0175-SPED-FISCAL
---

**Dúvida**Como gerar o registro **0175**alteração da tabela de cadastro de participante no Sped Fiscal?

**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
   
**Solução**Para gerar o registro **0175** no Sped Fiscal realize os seguintes passos:

1. Verifique no **Configurador** o parâmetro;

**MV\_HISTTAB** = .T.;

2. Realizar alterações nos cadastros de **clientes**, **fornecedores**, **transportadoras** e **produtos**. irá gravar a alteração na tabela **AIF**;

3. Realizar um Documento Fiscal de entrada ou saída com o registro alterado;

4. Gerar o SPED FISCAL;

Mais informações no link do tdn abaixo;

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285>
