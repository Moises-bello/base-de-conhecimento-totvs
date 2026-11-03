---
content_hash: 32c90bbc27dc3cb9f69fa4d5536f2205675ba05fa365b623f0c813a81af3d5b5
fetched_at: '2026-06-29T00:11:42.703243+00:00'
page_id: '795106302'
product: rm
source: tdn-rm
title: Aditivo - Renegociação de Contrato - Valor Presente Price
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795106302
version: 3
---

A partir do Patch Específico 12.1.2310.102, ao acessar a tela de Identificação do *Aditivo de Renegociação*, o sistema apresenta a opção para calcular o **Valor Presente Price** das parcelas selecionadas nesta renegociação.

Para ter acesso à esta funcionalidade é preciso executar o *[RM Atualizador](https://tdn.totvs.com/display/public/LRM/RM+Atualizador)*, que executará um script ativá-la. Caso está ação não seja executado, o sistema exibirá uma exceção ao usuário solicitando esta execução.

*"Erro ao criar: ImbVendaAditivoViewAction.*

*Foi liberado um novo script, para o aditivo de renegociador, na versão específica de mercado, que necessita que execute o RMAtualizador.exe antes."*

Desta forma, caso entre estas parcelas selecionadas tenha alguma com a modalidade Price o sistema calculará o Valor Presente das mesmas para a *Data do Aditivo* definida para o mesmo. Caso não tenha nenhuma parcela com este modelo de cálculo na seleção, este valor refletirá o valor das parcelas selecionadas.

Assim, ao marcar esta opção, o sistema pode apresentar o *Valor Presente Total*, diferente do Valor de Parcelas Selecionadas, devido ao deságio aplicado em relação à *Data do Aditivo*.
