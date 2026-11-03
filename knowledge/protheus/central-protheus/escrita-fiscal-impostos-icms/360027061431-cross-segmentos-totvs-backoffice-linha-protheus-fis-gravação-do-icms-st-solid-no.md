---
article_id: 360027061431
category: Escrita Fiscal - Impostos - ICMS
content_hash: 49e59398a826d38a769fcddb35223ca5429b3daeedf8882e7cb29c9011978695
fetched_at: '2026-06-28T22:39:23.999338+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Gravação do ICMS-ST
  (Solid) no campo observação no Livro Registro de Entrada'
type: support-article
updated_at: '2021-07-20T13:23:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027061431--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Grava%C3%A7%C3%A3o-do-ICMS-ST-Solid-no-campo-observa%C3%A7%C3%A3o-no-Livro-Registro-de-Entrada
---

**Dúvida**Como configurar o Protheus para que seja gravado o valor de ICMS-ST (Solid) no campo Observação no Livro de Registro de Entradas.  
  
**Ambiente**Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**  
Para que este valor sera escriturado no relatório campo OBSERVAÇÃO, o parâmetro MV\_P1ICMST deverá estar configurado com a opção .T. descrição:

Indica   que serão exibidos os valores referente ao ICMS-ST no Reg.Proc.Dados(P1/P1A) quando o campo Crd.ICMS ST (F4\_CREDST) do TES (SF4) for igual a 4=Subst.Trib.
