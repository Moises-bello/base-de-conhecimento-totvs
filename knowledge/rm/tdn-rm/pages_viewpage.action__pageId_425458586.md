---
content_hash: 1edcf26e0617d51c9bd0b9c1d406a56532cc8866155988426efba4063cf200f8
fetched_at: '2026-06-29T00:09:31.265687+00:00'
page_id: '425458586'
product: rm
source: tdn-rm
title: Cancelar área ofertada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458586
version: 5
---

Este processo poderá ser executado a partir da visão de "processos seletivos". O objetivo dele será permitir que uma área ofertada em um processo seletivo seja cancelada. Cancelar uma área de interesse ofertada significa que a instituição não irá prosseguir com a seleção para a mesma. Diversos motivos podem levar uma instituição a querer cancelar uma área, por exemplo: determinada área de interesse não ter atingido um número de inscrições considerado mínimo.

O assistente permitirá que apenas uma área seja cancelada por vez. Ao cancelar uma área ofertada, o status dela será alterado para "Inativo", impedindo assim que novas inscrições sejam feitas para ela. Ao término do processo, a área ofertada não irá apresentar nenhuma inscrição ativa.

Com relação às inscrições já feitas para a área em questão, a instituição poderá tomar uma das três possíveis providências permitidas pelo processo:

**1-**Transforme a 2ª opção dos candidatos em 1ª opção : Se for escolhida essa alternativa, o processo irá "converter" a 2º opção dos candidatos em 1ª opção. A área que está sendo cancelada será removida da lista de opções do candidato. O que antes era a sua 2ª opção passará a ser 1ª opção. O processo prevê situações em que o candidato não tenha definido uma 2ª opção. A instituição poderá optar por fixar uma área ofertada alternativa para candidatos que recaírem sobre essa situação. Somente áreas ofertadas ativas poderão ser escolhidas como área alternativa. A instituição poderá também optar por cancelar as inscrições que não possuírem uma 2º opção para substituir a que esteja sendo cancelada.

**2-** Transfira todas as inscrições da área de interesse que será cancelada para:  Com essa alternativa, todas as inscrições pertencentes à área que estiver sendo cancelada serão movidas para outra especificada. Mesmo que a área de interesse que esteja sendo cancelada não seja a 1ª opção do candidato, ela será substituída pela nova opção escolhida. Se a opção de substituição já estiver presente na lista de opções do candidato, antes ela será removida da posição em que se encontra inicialmente.

**3-**Apenas cancele todas as inscrições: Neste caso todos os candidatos que possuírem a área cancelada como sua 1ª opção terão a inscrição cancelada.

Observações

Á partir da versão 12.1.27, caso as inscrições da área de interesse ofertada que estiver sendo cancelada possuírem termo de aceite, gerado através de inscrições pelo portal do processo seletivo (somente novo portal), ao cancelar a área o sistema irá verificar se a área possui inscrições com termo de aceite, caso exista, será exibido uma lista com os candidatos que possuem o termo de aceite bem como duas ações possíveis nos termos de aceite existentes da área a ser cancelada.

Caso no processo seja escolhido a opção de "Apenas cancele todas as inscrições", não serão exibidos os candidatos com termos de aceite, pois suas inscrições serão canceladas e não transferidas para outra área ofertada.

**As ações possíveis são:**

* **Excluir o termo de aceite atual:** excluir os termos de aceite dos candidatos que possuírem.
* **Copiar o termo de aceite da nova área de interesse caso a área possua termos de aceite preenchido:** para os candidatos que possuem termo de aceite na área que está sendo cancelada e a nova área possuir um termo de aceite, o termo atual será substituído pelo da nova área de interesse, mas somente para os candidatos que possuírem termo de aceite.

Caso a nova área de interesse não possua termo de aceite, os termos existentes da área antiga serão excluídos.

**Pré-requisitos do processo:**  
a) Uma área ofertada só poderá ser cancelada se ainda não tiver ocorrido alocação de candidatos  
b) O processo de cancelar área ofertada será executado de acordo com o valor Y de dias definido antes do início do período de seleção. Esse número de dias a ser considerado é parametrizado pelo campo "Limite canc. Áreas (em dias)" na guia Identificação do cadastro do Processo Seletivo.

Até a versão 11.00 quando uma inscrição era cancelada pelo processo "Cancelar área ofertada" ocorria apenas a alteração do status da inscrição para "Inscrição Cancelada". Agora, as mesmas regras do processo "Cancelar ou excluir inscrição" serão aplicadas no Cancelar área ofertada quando a opção for para cancelar as inscrições. Ou seja, além da mudança de status,  o lançamento de financeiro será cancelado.
