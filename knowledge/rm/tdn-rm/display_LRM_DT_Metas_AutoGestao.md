---
content_hash: 100c83eda77604d2becc525c20eb517854f1567910485aab597c43b4b0a49238
fetched_at: '2026-06-29T00:06:24.262931+00:00'
page_id: '224115090'
product: rm
source: tdn-rm
title: DT_Metas_AutoGestao
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Metas_AutoGestao
version: 1
---

# METAS AUTO GESTÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Portal | Metas | |
| **Versões/Release:** | 12.1.9 |

## Descrição

O TOTVS Gestão de Pessoas permite que sejam geradas metas pelos próprios avaliadores e avaliados a partir do Portal do RH.

## Procedimento para Utilização

METAS AGRUPADORAS

Dentro de uma metra agrupadora é permitido cadastrar metas do tipo valor pelo portal através do avaliado ou avaliador. O usuário pode também, optar por definir uma meta agrupadora como "Meta Corporativa". Uma meta corporativa é visualizada por todos usuários da coligada.

O usuário pode definir a meta como sendo corporativa, mas ela não terá Atribuições.  
O Portal exige que seja definida a forma de avaliação e que o usuário informe as opções da meta idêntico ao que temos na aba de configurações de meta valor.  
O Avaliador pode cadastrar metas valor para seus Subordinados/Avaliados.

Opções quanto ao avaliado: Avaliado cadastra metas valor para ele mesmo; Caso a opção do avaliado cadastrar metas valor para si próprio esteja marcado, o item “Avaliado visualiza meta” deve sempre estar marcado; Metas necessitam de aprovação do avaliador.

CADASTRAMENTO DE METAS NO PORTAL PELO AVALIADO

Para o avaliado lançar metas valor pelo porta, o usuário do portal precisa cadastrar suas metas individuais a partir de agrupadoras para que o avaliado consiga registrar quais são seus objetivos dentro da empresa.

Caso o cadastramento de meta valor seja chamado do botão superior no painel de meta, o usuário deve informar uma meta agrupadora para a meta valor a ser cadastrada, caso seja chamado do botão localizado ao lado do registro de meta agrupadora no painel, não é necessário informar a meta agrupadora.  
O usuário deve informar o “tipo de valor” se é por valor de referência ou por faixa de valores.  
Sendo por faixa de valores, o portal permite inserir as faixas de valores e informar um valor de referência.  
A meta a ser criada tem que ser gerada sempre com o status “Em aberto”.  
As metas valor tem um FLAG de aprovação (pendente, sim ou não) que seguem a parametrização da meta agrupadora.  
A meta valor pode ser excluída pelo próprio usuário desde que não esteja aprovada.  
O período da meta valor criada deve estar compreendido dentro do período da meta agrupadora.  
É possível informar o % que a meta representa da agrupadora, e nunca deve ultrapassar 100% por avaliado.  
Ao ser criada, a meta valor deve estar atribuída ao usuário logado e sob responsabilidade: Do superior imediato quando a agrupadora estiver configurada como "Meta Corporativa"; Do avaliador da atribuição da agrupadora nos demais casos.  
Metas pendentes de aprovação ou reprovadas não permitem lançamentos ou outras movimentações.

 

CADASTRAMENTO DE METAS NO PORTAL PELO AVALIADOR

O Avaliador precisa cadastrar metas para avaliados de sua atribuição/subordinados para conseguir registrar quais são os objetivos de cada avaliado/subordinado.

Este requisito depende do requisito de CADASTRAMENTO DE METAS NO PORTAL PELO AVALIADO. Com as restrições / diferenças abaixo:

Caso o cadastramento de meta valor seja chamado do botão superior no painel de meta, o usuário deve informar uma meta agrupadora para a meta valor a ser cadastrada, caso seja chamado do botão localizado ao lado do registro de meta agrupadora no painel, não é necessário informar a meta agrupadora.  
Deve gerar a meta valor já aprovada.  
As metas valor podem ser excluídas somente pelo avaliador, desde que elas não tenham sido cadastradas no WINFORMS.  
Metas cadastradas diretamente pelo avaliador podem requerer o aceite do avaliado conforme parametrização da meta agrupadora.  
Ao cadastrar uma meta para um avaliado, o usuário logado será o avaliador (responsável) pela meta.  
Caso configurado como “Meta Corporativa”: O usuário escolherá um de seus subordinados como avaliado; Para os demais casos, deve ser escolhido um dos avaliados das atribuições da meta agrupadora.

APROVAÇÃO DE METAS

O Avaliador precisa visualizar as metas valor criadas dentro de agrupadoras que é responsável e que estejam pendentes para em seguida opte por aprová-las ou reprová-las para conseguir alinhar junto a sua equipe quais objetivos devem ser estabelecidos.

Uma coluna de Status de Aprovação no grid de metas do portal  exibe os possíveis status das metas, podendo ser aprovadas, reprovadas ou pendentes. Te, também um botão para aprovar/reprovar metas com status pendente.  
É permitido aprovar/reprovar registros em lote.  
Ao selecionar metas para aprovação e acionar a ação, será exibido um modal pop-up para que o usuário escolha se deseja aprovar ou reprovar.  
É permitido informar o motivo da reprovação.

REAVALIAÇÃO DE METAS

O usuário do portal pode visualizar as metas reprovadas pelo seu gestor para que ele a reavalie e a submeta novamente para aprovação ou para exclusão.

O portal permite a visualização de todas as metas reprovadas e os motivos, como também excluir metas reprovadas ou pendentes e editar a meta reprovada e submete-la novamente para aprovação do gestor.

AVALIADOS NO PAINEL DE METAS NO PORTAL  

 Para conseguir ter uma visualização rápida de quem é o avaliado, o avaliador pode visualizar o nome/descrição do avaliado no painel de metas quando houver apenas uma atribuição, caso existam múltiplas, tem uma opção na mesma coluna em que lista todas elas.
