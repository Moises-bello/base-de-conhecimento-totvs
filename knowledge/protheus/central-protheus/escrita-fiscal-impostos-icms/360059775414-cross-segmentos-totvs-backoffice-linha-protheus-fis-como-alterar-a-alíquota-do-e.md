---
article_id: 360059775414
category: Escrita Fiscal - Impostos - ICMS
content_hash: eda47cb1909b71bd83b1a22d03651924abd2f50731707a257105b71af3b6d298
fetched_at: '2026-06-28T22:39:24.378660+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como Alterar a Alíquota
  do Estado do Rio Grande do Sul Para 17,5%?
type: support-article
updated_at: '2022-06-07T19:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059775414-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Alterar-a-Al%C3%ADquota-do-Estado-do-Rio-Grande-do-Sul-Para-17-5
---

**Dúvida**Como alterar alíquota interna do estado do Rio Grande do Sul para 17,5%.?

**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**  
A alteração da alíquota pode ser realizada de três formas: 

1) exceção fiscal

<https://tdn.totvs.com/pages/releaseview.action?pageId=539703381>

2) Cadastro de produtos ( SB1 ) ou Indicador de produtos ( SBZ )

3) Parâmetros

MV\_ICMPAD = 17.5  ( Icms próprio )

MV\_ESTICM = 17.5  ( Icms St )

Sempre utilizando ponto, pois o sistema não reconhece virgula.

Após alteração, será necessário fechar o sistema e acessar novamente ou trocar de módulo e retornar para o módulo que esta efetuando os testes.
