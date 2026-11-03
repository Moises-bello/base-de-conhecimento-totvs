---
article_id: 360026398511
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b6d158841f5c7463812518b6f3041fd792575ece9f5528fb29d6ff830b3cd6ac
fetched_at: '2026-06-28T22:39:56.317725+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Belo Horizonte:
  Desconto Condicionado '
type: support-article
updated_at: '2025-07-18T14:38:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026398511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Belo-Horizonte-Desconto-Condicionado
---

**Dúvida**NFSE Belo Horizonte: Desconto Condicionado Conforme Lei número 9145, de 12 de Janeiro de 2006  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**O desconto condicionado normalmente é concedido em uma fatura, quando por exemplo o tomador vai antecipar algum pagamento, isso após a geração da nota, ou seja, na emissão da nota esse desconto ainda não existe.

Somente em algum caso muito especifico com embasamento legal, destacamos o desconto condicionado no XML da nota de serviços.

Belo Horizonte-MG: Lei número 9145, de 12 de Janeiro de 2006.

Art. 1º - Ficam isentos do Imposto Sobre Serviços de Qualquer Natureza - ISSQN - os serviços contratados pela Administração Pública Direta ou Indireta do Município, desde que seja descontado expressamente do valor do serviço constante do documento fiscal emitido o percentual referente à alíquota do imposto, que incidiria sobre a operação, se não fosse a isenção.

Existe uma exceção no rdmake NFSEXMLENV para atender essa legislação, para gerar a tag é necessário a configuração abaixo:

MV\_NFSEMOD=.T.  
A1\_TPESSOA= EP  
F4\_AGREG= D  
D2\_DESCICM = Valor do desconto  
O campo D2\_DESCICM será preenchido automaticamente com o valor do ISS, ao usar um TES com F4\_AGREG= D que calcula o ISS.  
  
https://cm-belo-horizonte.jusbrasil.com.br/legislacao/236159/lei-9145-06
