---
article_id: 6443501620247
category: Escrita Fiscal - Impostos - ICMS
content_hash: f0a1ed02b63420d32d3adc8c4d38b5cfc5af6c4cb18c03d1d43a0d3f4140dafc
fetched_at: '2026-06-28T22:39:24.044584+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  Credito Outorgado em SP?
type: support-article
updated_at: '2023-11-03T11:46:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6443501620247-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-Credito-Outorgado-em-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18786966201751) Tempo aproximado para leitura: 0:02**:00 min** **Dúvida**Como configurar Credito Outorgado em SP ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

Parâmetro

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6443284870423)

Informar o(s) quatro (4) primeiro(s) dígito(s) do(s) código(s) de NCM que contempla o Decreto 56.018 de 16.07.2010, o Decreto Nº 56.855 de 18 .03.2011  e o Decreto 56.874 de 23.03.2011 separados pelo símbolo **/**.

Caso não for preenchido esse parâmetro, o Sistema não mostra o valor do crédito outorgado na rotina de **Apuração de ICMS (MATA953)** automaticamente através da rotina **P9autotex.sp.**

2.     No Cadastro de TES (Tipos de Entrada):

a.        Acessar o Cadastro de TES e atribuir o percentual do crédito outorgado F4\_CROUTSP que deve ser aplicado ao item da nota fiscal conforme rege a legislação.

b.        Após essas configurações, gere as movimentações de entrada e saída para que o campo de **Crédito Outorgado**, no Livro Fiscal, seja alimentado automaticamente, de acordo com a aplicação do percentual configurado.

Apuração de ICMS

1.     Acesse a rotina de **Apuração do ICMS (MATA953)** e preencha as respectivas perguntas.

2.     Após o processamento da rotina, é exibido, o valor do Crédito Outorgado e será apresentado no folder de:

·         **Apuração de ICMS**, linha 006 / Código 007.32 – Crédito Outorgado – Artigo 31 do Anexo III do RICMS, e no folder **Informações Complementares**, linha 045, o valor do Crédito Outorgado.

·         **Apuração de ICMS**, linha 006 / Código 007.33– Crédito Outorgado - Art. 32 do Anexo III do RICMS, e no folder **Informações Complementares**, linha 045, o valor do Crédito Outorgado.

·         **Apuração de ICMS**, linha 006 / Código 007.34 – Crédito Outorgado - Art. 33 do Anexo III do RICMS, e no folder **Informações Complementares**, linha 045, o valor do Crédito Outorgado.

·         **Apuração de ICMS**, linha 006 / Código 007.35 – Crédito Outorgado - Art. 34 do Anexo III do RICMS, e no folder **Informações Complementares**, linha 045, o valor do Crédito Outorgado.

Para que seja exibida essa configuração de acordo com o P9autotext.SP precisa estar configurados os parâmetros abaixo:

MV\_USASPED = .T.

MV\_P9SPED = .T.

MV\_P9AUTO = .T.

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=699818173>
