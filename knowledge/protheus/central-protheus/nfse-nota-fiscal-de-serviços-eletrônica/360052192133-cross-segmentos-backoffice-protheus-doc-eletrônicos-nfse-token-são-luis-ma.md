---
article_id: 360052192133
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 1e816057a78b9e6029d2b323d2f8b7808110c5718f3d48c8daeb3c77071feeeb
fetched_at: '2026-06-28T22:39:58.539239+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - TOKEN SÃO
  LUIS-MA
type: support-article
updated_at: '2025-06-10T19:00:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052192133-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-TOKEN-S%C3%83O-LUIS-MA
---

**Dúvida**Como solucionar a mensagem abaixo ao transmitir uma nota de São Luis-MA?  
  
*<ERRO>ERRO DE VALIDAÇÃO DO XSD: CVC-MINLENGTH-VALID: VALUE '' WITH LENGTH = '0' IS NOT FACET-VALID WITH RESPECT TO MINLENGTH '32' FOR TYPE 'TPTOKENENVIORPS'.</ERRO>*  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.

**Solução**A prefeitura de São Luis, possui a nota técnica abaixo e no último parâmetro faz a seguinte orientação:  
  
*"A partir de 01/07/2016, todos os arquivos XML do serviço de RPS, deverão ser enviados informando-se a tag <TokenEnvio> no cabeçalho. **O conteúdo dessa tag pode ser obtido acessando-se o menu de Nota Fiscal Eletrônica - Contribuinte - Minha Empresa - Configuração de Empresa do Sistema da SEMFAZ (STM)**. A partir do dia 01/06/2016, o ambiente de homologação estará funcionando com essa nova regra, para que os contribuintes possam testar o envio de seus arquivos e verificar se os mesmos já atendem à nova especificação;"*

**[Nota Técnica](https://www.semfaz.saoluis.ma.gov.br/conteudo?/28/0/NOTA_T%C3%89CNICA_SOBRE_ENVIO_DE_RPS)**

O Token deve ser preenchido no wizard.config da rotina FISA022, campo AUTORIZACAO AEDF-e.  
Em seguida retransmita e monitore a nota**.**
