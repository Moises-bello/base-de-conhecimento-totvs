---
article_id: 360014600772
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: ff4b61f26bfc94bdc192f13b4345f3df87ad6746805cc38d4ea19b0e5f9bf66f
fetched_at: '2026-06-28T22:40:47.642435+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ECF O valor '02' informado na
  coluna 2 para o campo Registro ECF ( CEI_REGECF ) somado ao valor '111' informado
  na coluna 3 para o campo Código Lançamento ( CEI_CODIGO ) COMO CORRIGIR ?
type: support-article
updated_at: '2024-04-23T18:28:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014600772-Cross-Segmento-Backoffice-Linha-Protheus-ECF-O-valor-02-informado-na-coluna-2-para-o-campo-Registro-ECF-CEI-REGECF-somado-ao-valor-111-informado-na-coluna-3-para-o-campo-C%C3%B3digo-Lan%C3%A7amento-CEI-CODIGO-COMO-CORRIGIR
---

**Dúvida****Validação no TAF (integração ECF)**

Erro 1 - Linha: 3 - O valor '02' informado na coluna 2 para o campo Registro ECF ( CEI\_REGECF ) somado ao valor '111' informado na coluna 3 para o campo Código Lançamento ( CEI\_CODIGO ) não existe na base de dados:

*|T092AB|02|111|28526725.33|*

**Ambiente**Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Veja que com base no layout o deveria ter sido gerada um  Código, conforme tabela dinâmica do Sped, e  no lugar está gerando  “**111“**

Exemplo: |T092AB|02|111|28526725.33|

 Vide planilha deste Registro no arquivo <http://sped.rfb.gov.br/pasta/show/1644>

*abaixo layout da tabela tafst1*

* [Conheça o Layout de Integração](http://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009869571)

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados, conforme exigência da Receita.  

[Arquivos Modelos - Plano Referencial / Visões Gerenciais](http://tdn.totvs.com/pages/viewpage.action?pageId=189314312)

<http://tdn.totvs.com/display/public/PROT/ECF#Controladoria-6>

O registro T092AB  apresenta os dados para o Bloco P130, o qual deve ser usado pela visão gerencial conforme modelo. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009854352)

Veja: [MP - SIGACTB - ECF : P130,P200,P230,P300,P400,P500 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033706414-MP-SIGACTB-ECF-P130-P200-P230-P300-P400-P500-COMO-GERAR?source=search)
