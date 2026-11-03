---
content_hash: 1d5108c075c961c9c43f662b72dc823b2d92300746a88b375f7dfbad4ca5ea07
fetched_at: '2026-06-29T00:11:13.102506+00:00'
page_id: '656317973'
product: rm
source: tdn-rm
title: Simulando uma proposta
type: documentation
url: https://tdn.totvs.com/display/LRM/Simulando+uma+proposta
version: 7
---

#FF9000Procedimentos para Utilização

Após a reserva da unidade é possível simular as condições de pagamento para efetivação do negócio. Clique nas mesmas opções da etapa de reserve e agora siga com o botão SIMULAR existente em todas as telas acima demonstradas. Neste momento será aberta a tela a seguir:

Para uma proposta os campos de CPF, nome e celular são obrigatórios.

Importante: Esta opção pode ser alterada de acordo com os campos obrigatórios parametrizados no Portal de Imóveis (vide capítulo sobre Pessoas)

Mais abaixo na mesma tela temos a solicitação de dados referente a mídia que trouxe o prospect até esta proposta, o motivo pelo qual ele está comprando e qualquer outra observação deste processo de venda.

Observação: Os cadastros de mídias e motivo da compra estão em backend > globais 

Seguindo na tela de simulação de propostas, temos agora as possíveis condições de pagamento ou modalidades de vendas para construção da proposta.

Se houver mais de uma modalidade de venda associada ao empreendimento no TCGI e estas modalidades estiverem com vigência ativa, então o Portal de Imóveis irá possibilitar a escolha, ao selecionar a condição de pagamento desejada sua composição será carregada para tela.

Nesta tela o corretor poderá negociar com o cliente a condição de pagamento mais apropriada e ao final do processo deverá clicar sobre o botão VALIDAR para que a proposta seja avaliada pelo Portal de Imóveis e sua real condição financeira seja analisada, resultando em uma proposta APROVADA ou REPROVADA . Uma proposta só poderá ser salva se for validada anteriormente.

Observação: Quando há divergências de valores relacionados ao percentual de VPL o sistema passa a exibir, a partir da versão 12.1.33 o informativo de log do VPL.

Este informativo visa mostrar o detalhe do cálculo e seus percentuais e como o Portal de Imóveis chegou ao resultado.

Ao clicar no Log de cálculo temos a informação do cálculo como demonstrada abaixo:

Ainda é possível incluir na proposta outros cadastros (ao clicar em Mostrar dados adicionais), **"Representante Legal" e "Fiador"**

Quando uma pessoa é utilizada para algum papel dentro de uma proposta ele é cadastrado de acordo com seu tipo, dando a sensação de duplicidade porém o Portal de Imóveis tem comportamentos para cada tipo de pessoa.  
Diante deste cenário o nome da pessoa será acrescido de seu tipo de acordo com os tipos abaixo:  
**5=Procurador 6=Procurador Cônjuge 7=Representante Legal 8=Fiador**

No rodapé da proposta também temos a possibilidade de demonstrar o painel de comissão. Este painel serve para selecionar quem paga a comissão e qual a forma de rateio desta, conforme mencionado no item 13 deste manual. Caso o empreendimento use somente um tipo de pagamento de comissão, podemos definir o comportamento padrão desta comissão e eliminar para o empreendimento desejado a visão deste painel onde o corretor deve escolher pela forma de pagamento da comissão.

Para deixar valores padrões e esconder o painel da comissão acesse backend > empreendimento, na primeira aba ao final da página estarão as opções para esta ação.

Após salvar a proposta a mesma aparecerá no menu PROPOSTAS possibilitando sua edição ou mudança desta para outra etapa.

#FF9000Editar uma proposta salva

Após a proposta salva, podemos acessar o menu propostas e lá estarão todas as propostas salvas. Aquelas que permitem edição terão o ícone do “lapis” habilitado e ao clicar sobre ele, será carregada a mesma tela da simulação da proposta.

Mais informações

---

* [Empreendimentos - Simular Proposta](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Simular+Proposta)
* [Empreendimentos - Tabela de Preços](https://tdn.totvs.com/pages/viewpage.action?pageId=652222231)
* [Propostas - Anexos da Proposta](https://tdn.totvs.com/display/LRM/Propostas+-+Anexos+da+Proposta)
