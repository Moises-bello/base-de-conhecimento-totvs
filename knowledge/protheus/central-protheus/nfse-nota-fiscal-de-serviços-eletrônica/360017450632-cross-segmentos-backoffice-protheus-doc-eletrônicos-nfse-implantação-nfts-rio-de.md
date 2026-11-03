---
article_id: 360017450632
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 58363d0af623222923cf88e79a3f9d33169be151ba7cb573d22a04e74aed8c6c
fetched_at: '2026-06-28T22:39:56.196080+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Implantação
  NFTS Rio de Janeiro
type: support-article
updated_at: '2025-07-18T14:42:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017450632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Implanta%C3%A7%C3%A3o-NFTS-Rio-de-Janeiro
---

**Dúvida**Como implantar NFTS Rio de Janeiro  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**1. A NFTS desse município trabalha na modalidade de Upload de arquivos (TXT);  
  
2. A geração do arquivo deve ser feita pela rotina **FISA022**;  
  
3. O documento de entrada deve ser gerado com especie NFS.  
  
4. Certifique-se de que a emissão do documento gerou as tabelas CD2, SF3 e SFT.  
  
5. Utilize o rdmake **NFSEXMLENV** (MV\_NFSEMOD = .T.) e TSS atualizado, download disponível no portal do cliente.  
  
6. Segue abaixo um informativo para a Implantação de NFTS do Rio de Janeiro:  
  
A emissão da Nota Fiscal do Tomador/Intermediário - NFTS (emissão em lote) está integrada ao Sistema da Nota Fiscal de Serviços Eletrônica – NFS-e, permitindo que sejam transferidas informações dos contribuintes para a Prefeitura em arquivos no formato texto. Tais arquivos devem atender a um layout pré-definido.  
  
A Nota Fiscal Eletrônica do Tomador/Intermediário de Serviços – NFTS foi instituída pela Lei Nº 15.406, de 8 de julho de 2011, e se destina à declaração dos serviços tomados ou intermediados pelas pessoas jurídicas e pelos condomínios edilícios residenciais ou comerciais por ocasião da contratação de serviços. Os serviços tomados antes informados na Declaração Eletrônica de Serviços - DES agora são passíveis da emissão da Nota Fiscal do Tomador/Intermediário de Serviços – NFTS.  
  
Deverão emitir a Nota Fiscal Eletrônica do Tomador/Intermediário de Serviços – NFTS todas as pessoas jurídicas e os condomínios edilícios residenciais ou comerciais por ocasião da contratação de serviços, nas seguintes hipóteses:  
  
I – quando os serviços tiverem sido tomados ou intermediados de prestador estabelecido fora do Município de Rio de Janeiro, ainda que não haja obrigatoriedade de retenção na fonte do Imposto Sobre Serviços de Qualquer Natureza – ISS;  
  
II – quando responsáveis tributários nos termos do § 1º do art. 7º da Lei 13.701/2003, no caso dos serviços terem sido tomados ou intermediados de pessoa jurídica estabelecida no Município de Rio de Janeiro que não emitir NFS-e, Cupom Fiscal Eletrônico ou outro documento fiscal cuja obrigatoriedade esteja prevista na legislação.  
  
**Recibos na geração do arquivo:**  
  
Na geração do arquivo TXT da NFTS devem ser considerados os recibos lançados diretamente no financeiro. Eles são de prestadores de serviços que não fornecem o documento fiscal ao tomador por não terem esta obrigatoriedade ou, então, mesmo que obrigados não o faz. Desta forma, são gerados registros no arquivo TXT com os seguintes tipos de documento:  
  
01 - Dispensado de emissão de documento fiscal.  
  
03 - Sem emissão de documento fiscal embora obrigado.  
  
O tipo 02 - Com emissão de documento fiscal autorizado pelo município - é o tratamento já realizado pelo sistema e que são considerados os documentos de entrada de serviço.  
  
**Importante:**A geração do arquivo TXT, considerando os recibos lançados diretamente no financeiro, ocorre somente com a utilização de Múltiplos Vínculos de ISS.  
  
Informações sobre TSS no link abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=128681294>
