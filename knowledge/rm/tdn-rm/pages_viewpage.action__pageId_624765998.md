---
content_hash: 54beaaf73d5e6a5488af5d8095db8f7dcc6644817a822ea39d28ab44d33cb5c7
fetched_at: '2026-06-29T00:11:03.677203+00:00'
page_id: '624765998'
product: rm
source: tdn-rm
title: Alteração do Período para Manutenção de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624765998
version: 4
---

Período para Manutenção de Lançamentos Contábeis é o período definido para o usuário em que ele terá acesso liberado para incluir, alterar ou excluir lançamentos contábeis.   
Qualquer tentativa de incluir, alterar ou excluir lançamentos contábeis fora do período definido será barrada pelo sistema.

Quando a data de um lançamento estiver fora do período de manutenção definido para um usuário, este lançamento não poderá ser excluído nem suas partidas alteradas por   
este usuário, a não ser que a data deste lançamento seja alterada para dentro do período permitido para o usuário, ficando o lançamento a partir daí, disponível para alterações e exclusão por este usuário.

Porém, quando a opção **'Barrar alteração da data do lançamento fora deste período para dentro do mesmo'** estiver *marcada*, não será permitido que o usuário altere a data de tais lançamentos,   
impossibilitando então que quaisquer alterações nos lançamentos que estiverem fora do período de manutenção definido para o usuário sejam feitas.

O processo para alteração deste período permite selecionar como filtro: Todos Usuários, Somente Supervisores, Exceto Supervisores e Definir Usuários.

Todos esses filtros são relacionados ao Módulo Gestão Contábil, então por exemplo:  
Filtro selecionado → Exceto Supervisores   
O processo irá alterar o período de todos os usuários, exceto aqueles com acesso de supervisor no contábil, independente do módulo selecionado.

**Observação**

O período para manutenção de lançamentos é definido por usuário, independente para quais sistemas o usuário tenha acesso.   
Todos os usuários que têm acesso ao sistema de Gestão Contábil devem ter o período definido.   
Somente usuário Supervisor terá acesso a esta tela de configuração diretamente pelo cadastro de usuários, disponível dentro das opções dos *Anexos.*

Fórmulas Visuais

Caso esteja utilizando fórmulas visuais para alterar o período, a fórmula deve obedecer a estas configurações em cada atividade para que funcione corretamente:

Obs: Apenas um dica, pode ou não funcionar para outros tipos de servers. Para mais detalhes, consulte a documentação oficial de fórmulas visuais.

*ReadRecord*

*AddTable*

*SaveRecord*
