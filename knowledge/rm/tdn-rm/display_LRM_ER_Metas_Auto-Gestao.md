---
content_hash: 5dbad6c367c284c9d2d4e5d1f25d6f69515930bd318c87dd0c6170269a524621
fetched_at: '2026-06-29T00:06:22.346175+00:00'
page_id: '223914980'
product: rm
source: tdn-rm
title: ER_Metas_Auto-Gestao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Metas_Auto-Gestao
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

 Permitir que sejam geradas metas pelos próprios avaliadores e avaliados a partir do Portal do RH.

## Definição da Regra de Negócio

**Req.1 - Configuração de metas agrupadoras**

Como analista de RH

Eu preciso definir dentro de uma metra agrupadora se será permitido cadastrar metas do tipo valor pelo portal através do avaliado ou avaliador. Posso também optar por definir uma meta agrupadora como "Meta Corporativa". Uma meta corporativa será visualizada por todos usuários da coligada.

Essas funcionalidades darão uma maior liberdade para a criação de metas pelos interessados através do portal.

Regras de negócio:

* Ao criar uma meta agrupadora, devem estar disponíveis as seguintes configurações:
  + Definir a meta como sendo corporativa.
    - Uma meta corporativa não terá Atribuições.
  + Deve exigir que seja definida a forma de avaliação (esta informação será aplicada para cada meta valor criada no Portal a partir da agrupadora).
  + Deve exigir informar as opções da meta idêntico ao que temos na aba de configurações de meta valor (estas informações serão aplicadas para cada meta valor criada no Portal a partir da agrupadora).
  + Avaliador poderá cadastrar metas valor para seus Subordinados/Avaliados.
  + Opções quanto ao avaliado:
    - Avaliado cadastra metas valor para ele mesmo
    - Caso a opção do avaliado cadastrar metas valor para si próprio esteja marcado, o item “Avaliado visualiza meta” deve sempre estar marcado.
    - Metas necessitam de aprovação do avaliador

**Req.2 - Cadastramento de metas no portal pelo avaliado**

Como avaliado / subordinado

Eu preciso cadastrar minhas metas individuais a partir de agrupadoras que permitam ao avaliado lançar metas valor pelo portal.

Para conseguir registrar quais são meus objetivos dentro da empresa.

Regras de negócio:

* Caso o cadastramento de meta valor seja chamado do botão superior no painel de meta, o usuário deverá informar uma meta agrupadora para a meta valor a ser cadastrada, caso seja chamado do botão localizado ao lado do registro de meta agrupadora no painel, não será necessário informar a meta agrupadora.
* Deve exigir informar o “tipo de valor” se é por valor de referência ou por faixa de valores.
* Sendo por faixa de valores, deve permitir inserir as faixas de valores.
* Deve permitir informar um valor de referência.
* A meta a ser criada deve sempre ser gerada com o status “Em aberto”.
* As metas valor deverão ter um FLAG de aprovação (pendente, sim ou não) que devem seguir a parametrização da meta agrupadora.
* A meta valor poderá ser excluída pelo próprio usuário desde que não esteja aprovada.
* O período da meta valor criada deve estar compreendido dentro do período da meta agrupadora.
* Deverá ser possível informar o % que a meta representa da agrupadora, e nunca deve ultrapassar 100% por avaliado.
* Ao ser criada, a meta valor deve estar atribuída ao usuário logado e sob responsabilidade:
  + Do superior imediato quando a agrupadora estiver configurada como "Meta Corporativa".
  + Do avaliador da atribuição da agrupadora nos demais casos.
* Metas pendentes de aprovação ou reprovadas não deverão permitir lançamentos ou outras movimentações;

**Req.3 – Cadastramento de metas no portal pelo avaliador**

Como avaliador

Eu preciso cadastrar metas para avaliados de minha atribuição/subordinados.

Para conseguir registrar quais são os objetivos de cada avaliado/subordinado.

Regras de negócio:

Este requisito depende do requisito 2. Com as restrições / diferenças abaixo:

* Caso o cadastramento de meta valor seja chamado do botão superior no painel de meta, o usuário deverá informar uma meta agrupadora para a meta valor a ser cadastrada, caso seja chamado do botão localizado ao lado do registro de meta agrupadora no painel, não será necessário informar a meta agrupadora.
* Deve gerar a meta valor já aprovada.
* As metas valor poderão ser excluídas somente pelo avaliador, desde que elas não tenham sido cadastradas no WINFORMS.
* Metas cadastradas diretamente pelo avaliador, podem requerer o aceite do avaliado conforme parametrização da meta agrupadora.
* Ao cadastrar uma meta para um avaliado, o usuário logado deverá ser o avaliador (responsável) pela meta.
* Caso configurado como “Meta Corporativa”:
  + O usuário deverá escolher um de seus subordinados como avaliado.
  + Para os demais casos, deverá ser escolhido um dos avaliados das atribuições da meta agrupadora.

**Req.4 – Aprovação de metas**

Como avaliador

Eu preciso visualizar as metas valor criadas dentro de agrupadoras que sou responsável e que estejam pendentes, para em seguida optar por aprová-las ou reprová-las.

Para conseguir alinhar junto a minha equipe quais objetivos devem ser estabelecidos.

Regras de negócio:

* Uma coluna de Status de Aprovação será acrescentada ao grid de metas do portal e exibirá os possíveis status das metas, podendo ser aprovadas, reprovadas ou pendentes.
* Deve exibir na grid, um botão para aprovar/reprovar metas com status pendente.
* Deve permitir aprovar/reprovar registros em lote.
* Ao selecionar metas para aprovação e acionar a ação, deve ser exibido um modal pop-up para que o usuário escolha se deseja aprovar ou reprovar.
* Deve permitir informar um motivo de reprovação.

**Req.5 – Reavaliação de metas**

Como usuário do portal

Eu preciso visualizar as metas reprovadas pelo meu gestor.

Para que eu a reavalie e a submeta novamente para aprovação ou para que eu a exclua.

Regras de negócio:

* Deve permitir visualizar todas as metas reprovadas e os motivos.
* Deve permitir excluir metas reprovadas ou pendentes.
* Deve permitir editar meta reprovada e submete-la novamente para aprovação do gestor.

**Req.6 – Avaliados no Painel de metas no Portal**

Como avaliador

Eu preciso visualizar o nome/descrição do avaliado no painel de metas quando houver apenas uma atribuição e caso existam múltiplas, devo ter uma opção na mesma coluna que me liste todas elas.

Para conseguir ter uma visualização rápida de quem é o avaliado.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
