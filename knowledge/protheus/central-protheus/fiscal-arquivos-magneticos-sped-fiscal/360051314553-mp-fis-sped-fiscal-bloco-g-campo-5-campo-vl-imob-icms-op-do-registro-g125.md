---
article_id: 360051314553
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: fab5a8aed5a0fa4e62259671b30b5f9da5dca873258bfb1d251b701911b18749
fetched_at: '2026-06-28T22:42:03.844032+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - SPED FISCAL BLOCO G - CAMPO 5 (Campo VL_IMOB_ICMS _OP ) DO REGISTRO
  G125
type: support-article
updated_at: '2025-03-19T17:50:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051314553-MP-FIS-SPED-FISCAL-BLOCO-G-CAMPO-5-Campo-VL-IMOB-ICMS-OP-DO-REGISTRO-G125
---

**Dúvida**  
Campo 5 (Campo VL\_IMOB\_ICMS \_OP ) do registro G125 esta sendo gravado sem descontar o valor do ICMS Diferencial de Alíquota.   
  
Ao validar o arquivo é apresentado o erro de validação conforme abaixo:

O campo VL\_IMOB\_ICMS\_OP do registro superior G125 é maior que somatório do campo VL\_ICMS\_OP\_APLICADO de seus hierarquicamente inferiores G140.   
  
![](https://totvssuporte.zendesk.com/attachments/token/ZM520CEE8e70fW2RZeIjdhOoY/?name=inline-191593235.png)  
  
 **Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80]  
  
**Solução**  
Além de verificar se o cliente esta atualizado conforme portal do cliente, verificar na rotina MATA905 - Manutenção CIAP se o campo Tipo do Bem (F9\_TIPO - Classificação do Tipo de Bem, semelhante ao Ativo Fixo) esta preenchido.

Caso não esteja preenchido, será necessário efetuar o devido preenchimento conforme caraterista do bem.

O erro mencionado acima na validação do SPED FISCAL foi presentando para bens incluídos direto na rotina Manutenção CIAP.

Conforme boletim técnico do "CIAP – Crédito ICMS sobre Ativo Permanente" foi identificado a informação abaixo referente o campo Tipo do Bem (F9\_TIPO):

"Campo criado para informar o tipo de Ativo, a busca é realizada pela mesma Consulta Padrão utilizado no Ativo Fixo (G1) e para atender o SPED, na geração do bloco G, registro G125 e 0300.

Caso o bem estiver cadastrado como componente, ou seja, o campo F9\_TIPO com o conteúdo 03, não será  possível apropriá-lo e o sistema irá apresentar um alerta com as instruções para resolução da inconsistência."

Abaixo link do boletim técnico:

<https://tdn.totvs.com/pages/releaseview.action?pageId=187532625>
