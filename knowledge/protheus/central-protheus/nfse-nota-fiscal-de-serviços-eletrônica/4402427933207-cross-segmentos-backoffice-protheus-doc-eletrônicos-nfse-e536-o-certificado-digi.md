---
article_id: 4402427933207
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 49a358ab389663dd2bfd30424f8558d8d5780d945a82ced0585c5c1117951d20
fetched_at: '2026-06-28T22:39:57.382233+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E536 - O
  CERTIFICADO DIGITAL INFORMADO NÃO ESTÁ VINCULADO O USUÁRIO INFORMADO (Curitiba)
type: support-article
updated_at: '2025-06-25T13:30:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402427933207-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E536-O-CERTIFICADO-DIGITAL-INFORMADO-N%C3%83O-EST%C3%81-VINCULADO-O-USU%C3%81RIO-INFORMADO-Curitiba
---

**Ocorrência**Ao realizar a transmissão para a prefeitura de Curitiba, ocorre a rejeição: *"E536 - O CERTIFICADO DIGITAL INFORMADO NÃO ESTÁ VINCULADO O USUÁRIO INFORMADO".*  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Documentos Eletrônicos - Todas as versões.  
  
**Causa**A rejeição ocorre pelo fato do Certificado Digital utilizado não estar vinculado ao usuário no portal da prefeitura.  
  
**Solução**Para correção da rejeição, deverá vincular o Certificado Digital no portal da prefeitura com o usuário que realizou o acesso através do menu: '*Contribuinte':*

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402428396567/mceclip0.png)*Vale lembrar que esse certificado vinculado é o mesmo que foi importado no navegador da máquina.  
Em casos de alteração/atualização do certificado, é sempre recomendado excluir do navegador a configuração antiga e manter apenas a nova. Pois no momento da vinculação, caso possua dois (antigo e o novo), o navegador sempre irá considerar o antigo para acesso/vinculação no portal.  
  
Feito essa vinculação, dentro da rotina FISA022 precisará configurar o Wizard.cfg com o mesmo certificado utilizado, sendo assim possível realizar as transmissões ou retransmissões.  
  
**IMPORTANTE**Se mesmo com a vinculação a rejeição persistir, a prefeitura deverá ser acionada para verificarem internamente se há algum tipo de problema cadastral com o usuário utilizado.
