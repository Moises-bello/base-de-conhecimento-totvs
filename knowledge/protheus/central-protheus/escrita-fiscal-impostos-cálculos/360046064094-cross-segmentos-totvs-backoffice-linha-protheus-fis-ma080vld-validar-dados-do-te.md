---
article_id: 360046064094
category: Escrita Fiscal - Impostos - Cálculos
content_hash: f2fb26e45738eae7df9936d3425b789c00c2b3e645bc3ddfa2b48ed95164085b
fetched_at: '2026-06-28T22:39:30.600582+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - MA080VLD - Validar
  dados do TES
type: support-article
updated_at: '2021-07-29T13:29:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046064094-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-MA080VLD-Validar-dados-do-TES
---

**Dúvida**  
MA080VLD - Validar dados do TES  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Ponto-de-Entrada: MA080VLD - Validar dados do TES  
  
Descrição:

Este ponto de entrada pertence à rotina de cadastro de tipos de entrada e saída, MATA080(). Ele permite ao usuário validar os dados do TES antes que sejam gravados.

Programa Fonte  
.PRW  
Sintaxe  
MA080VLD - Validar dados do TES ( [ nOpcao ] ) --> lRet

Parâmetros  
  
Nome: nOpcao  
Tipo: Numérico  
Descrição: Indica a operação: 3 - inclusão / 4 - Alteração  
Default:  
Obrigatório:   
Referência:  
  
Retorno

**lRet**

(logico)* .T. permite a gravação  
  .F. não permite a gravação.

Abaixo link contendo fonte das informações:  
  
<https://tdn.totvs.com/display/public/PROT/MA080VLD+-+Validar+dados+do+TES>
