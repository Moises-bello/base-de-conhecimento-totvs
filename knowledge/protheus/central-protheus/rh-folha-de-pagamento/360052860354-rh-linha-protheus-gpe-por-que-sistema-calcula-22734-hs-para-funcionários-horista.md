---
article_id: 360052860354
category: RH - Folha de Pagamento
content_hash: e03b3543617ccf81491ff8d1f59c1aa894e2f0ef4257e9a9ca676d3da99e38a3
fetched_at: '2026-06-28T22:44:16.173267+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Por que sistema calcula 227,34 hs para funcionários
  horistas no mês de 31 dias com 26 dias de horas normais e 5 dias de DSR
type: support-article
updated_at: '2024-09-12T11:34:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052860354-RH-Linha-Protheus-GPE-Por-que-sistema-calcula-227-34-hs-para-funcion%C3%A1rios-horistas-no-m%C3%AAs-de-31-dias-com-26-dias-de-horas-normais-e-5-dias-de-DSR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26319666342039) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Por que sistema calcula 227,34 hs para funcionários horistas no mês de 31 dias com 26 dias de horas normais e 5 dias de DSR?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O sistema efetua o cálculo das horas normais e DSR separadamente, multiplicando a quantidade de dias (determinada no cadastro do período) pela quantidade de horas diárias do cadastro de funcionários (RA\_HRSDIA), sendo assim ficaria:  
  
No primeiro caso:  
26 \* 7,3333 = 190,6658 = 190,67 (Normal)  
5 \* 7,3333 = 36,6665 = 36,67(DSR)  
Total = 227,34  
  
No segundo caso:  
25 \* 7,3333 = 183,3325 = 183,33 (Normal)  
6 \* 7,3333 = 43,9998 = 44,00(DSR)  
Total = 227,33  
  
Importante observar que não trata-se de erro no sistema, e sim de arredondamento.  
Se truncar o valor, ao invés de utilizar o arredondamento, o valor ainda seria diferente, exemplo:  
  
26 \* 7,3333 = 190,6658 => 190,66  
5 \* 7,3333 = 36,6665 => 36,66  
A soma seria  227,32

**Saiba Mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=394225103>

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
