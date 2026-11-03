---
content_hash: 264a3a313ab9f329aae3e8b84f2b6d7977d5f0a71b9d2336ce3ea71040d71fa8
fetched_at: '2026-06-29T00:09:46.596139+00:00'
page_id: '435104854'
product: rm
source: tdn-rm
title: Aditivo - Processo - Contabilizar Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivo+-+Processo+-+Contabilizar+Aditivo
version: 7
---

Ao executar esse processo, é exibido a tela de contabilização do Aditivo.   
Permitindo incluir lotes de Crédito e Débito, assim como inserir um Evento Contábil.

A partir da versão 12.1.26, será possível realizar a contabilização de forma assíncrona, assim como a recontabilização. A qualquer momento o aditivo pode ser contabilizado. O processo funcionará da mesma forma porém a qualquer momento.

 Importante: Caso o evento contábil associado ao aditivo seja calculado a partir de uma fórmula e esse valor durante o processo da contabilização for igual a zero, o sistema não irá contabilizar o aditivo. Será necessário ajustar a fórmula ou alterar o evento contábil.

* Para aditivos do tipo , existe o parâmetro **Contabilizar sempre o aditivo de renegociação** para que este aditivo seja contabilizado mesmo quando não tenha alteração de valor:   
  Os valores das parcelas selecionadas serão desfeitos na contabilização do evento deflacionário e refeitas com os valores das novas parcelas no evento inflacionário.  
  Como envolve dois eventos ao mesmo tempo na contabilização do aditivo, então não será exibida a tela de pré-visualização da contabilização.

* Para aditivos do tipo

Parâmetro **Evento Contábil Aditivo de Troca de Subunidade** - Informar qual evento contábil será usado para contabilizar este tipo de aditivo.

Valores de incidência **Valor Aditivo Subunidade Antes** e **Valor Aditivo Subunidade Após** - São utilizados para que na contabilização deste tipo de aditivo, seja possível indicar se o valor a ser considerado na contabilização é referente a subunidade que foi retirada ***(Subunidade Antes)*** ou a subunidade que foi incluída ***(Subunidade Após),*** quando estes forem diferentes

## Se na efetivação do aditivo tiver mais de um tipo a ser contabilizado, então a contabilização será feita da forma antiga.
