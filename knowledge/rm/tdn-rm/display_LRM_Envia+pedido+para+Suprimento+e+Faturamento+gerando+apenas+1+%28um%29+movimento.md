---
content_hash: 17c40184e21304102869d907d16367677fcdcaff5349c8625a0232b5ffef0435
fetched_at: '2026-06-29T00:09:14.866871+00:00'
page_id: '421385286'
product: rm
source: tdn-rm
title: Envia pedido para Suprimento e Faturamento gerando apenas 1 (um) movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+apenas+1+%28um%29+movimento
version: 9
---

Selecionar o pedido na visão de requisição de materiais, após selecionar o pedido, clique no botão (Gerar apenas 1 Movimento) ou Processos Envio | Pedido para Suprimento/Faturamento Gerando apenas 1 Movimento.  
Através deste processo, a requisição se tornará em apenas um pedido do Gestão de Estoque Compras e Faturamento. Se as obras tiverem locais de estoque diferentes, será gerado um movimento para cada obra. A data de entrega do movimento será a data de início do primeiro período previsto.  
Após o processo, o sistema altera o status da requisição para "Enviada" alterando também a cor da linha da requisição.  
Se for gerar apenas um movimento para uma obra ou um conjunto de obras, podem ocorrer situações onde o insumo é utilizado em períodos diferentes e serão inclusos itens iguais no movimento. Para isso, acessar o menu Opções | Parâmetros | Gestão de Estoque Compras e Faturamento| Outras Movimentações | Grupo Item-Identificação 2/2 o parâmetro "Permitir item repetido" deve estar marcado.  
Geração de Movimentos para o Protheus com Controle de Status - Integração (EAI 2.0)  
Apesar de estar no mesmo processo, a geração do movimento foi separada internamente do processo de integração. Assim, caso haja erros de integração, os movimentos e consequentemente todos os cálculos efetuados continuam salvos na base e passíveis de serem reenviados para o sistema integrado.  
Para esse controle, foi acrescentado um novo status no fluxo dos pedidos para que o usuário final visualize os movimentos pendentes de integração. Ou seja, caso sejam gerados movimentos no RM e algum desses não seja integrado corretamente, o usuário final deverá somente ajustar a inconsistência e reenviar o movimento para integração.  
Enquanto esse movimento não for corrigido e reenviado pelo usuário, este ficará com o status: "Em Suprimento/Faturamento com Movimentos não Integrados".  
As exclusões dos movimentos continuam de forma transparente para o usuário, não importando se o movimento já está Integrado ou com status de "Em Suprimento/Faturamento com Movimentos não Integrados", basta executar o processo de "Excluir Movimentos" para que esse movimento seja excluído e o pedido possa sofrer alterações novamente.   
   
Caso a exclusão do movimento não ocorra por inconsistências de integração, seguirá o mesmo fluxo de status apresentado anteriormente.  
 

**Envio de Natureza Orçamentária**

Caso o movimento gerado no BackOffice Nucleus esteja parametrizado para não editar natureza orçamentária o TOTVS Construção Obras e Projetos não envia a natureza e o BackOffice Nucleus preenche com a natureza do produto.

Caso o parâmetro Orçamento>Editar Natureza Orçamentária/Financeira do Tipo de Movimento parametrizado no Nucleus tenha valor diferente de "Não edita":

Ao gerar movimento do pedido de material no Nucleus, o TOP deverá enviar a Natureza Orçamentária/Financeira seguindo a seguinte regra de prioridade:

1 - Buscar a natureza na tarefa. Se não houver,  
2 - Buscar a natureza no insumo. Se não houver,  
3 - Buscar a natureza no grupo de custo. Se não houver, não enviar.

**Observações**

* Caso o projeto esteja com a parametrização [Integração TOTVS Aprovação e Atendimentos](https://tdn.totvs.com/x/1tQdGQ) ativa, no momento do Envio do pedido para Suprimentos/Faturamento, gerando apenas um movimento ou gerando movimento por data, o sistema permite que seja gerado o movimento somente se existir um workflow com o status de aprovado. É necessário que o atendimento seja concluído como aprovado para seguir o fluxo normal da Requisição de Material. Caso o atendimento seja concluído como reprovado, identifique quais mudanças devem ser efetuadas. Os itens do pedido de material não poderão ser alterados, assim como o pedido excluído enquanto o workflow não for concluído.
* Quando o TOTVS Construção Obras e Projetos estiver utilizando integração com o BackOffice RM , será possível estornar movimentos.
* Outro comportamento  nessa integração é que caso seja necessária a utilização parcial deste movimento gerado ,basta somente editar o item do movimento salvando o mesmo e será visível no campo estorno do pedido o reflexo dessa mudança.
