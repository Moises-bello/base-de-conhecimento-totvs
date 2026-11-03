---
content_hash: 5a76262b60705c319d4bf5e7cbe5ec8796e7386b0fddefc239edaf45915b7dac
fetched_at: '2026-06-29T00:09:29.091275+00:00'
page_id: '423938805'
product: rm
source: tdn-rm
title: Período para Manutenção de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938805
version: 4
---

Período para Manutenção de Lançamentos Contábeis é o período definido para o usuário em que ele terá acesso liberado para incluir, alterar ou excluir lançamentos contábeis. Qualquer tentativa de incluir, alterar ou excluir lançamentos contábeis fora do período definido será barrada pelo sistema.

Quando a data de um lançamento estiver fora do período de manutenção definido para um usuário, este lançamento não poderá ser excluído nem suas partidas alteradas por este usuário, a não ser que a data deste lançamento seja alterada para dentro do período permitido para o usuário, ficando o lançamento a partir daí, disponível para alterações e exclusão por este usuário.

Porém, quando a opção **'Barrar alteração da data do lançamento fora deste período para dentro do mesmo'** estiver *marcada*, não será permitido que o usuário altere a data de tais lançamentos, impossibilitando então que quaisquer alterações nos lançamentos que estiverem fora do período de manutenção definido para o usuário sejam feitas.

O processo para alteração deste período permite selecionar como filtro: Todos Usuários, Somente Supervisores, Exceto Supervisores e Definir Usuários.

Todos esses filtros são relacionados ao Módulo Gestão Contábil, então por exemplo:  
Filtro selecionado → Exceto Supervisores   
O processo irá alterar o período de todos os usuários, exceto aqueles com acesso de supervisor no contábil, independente do módulo selecionado.

**Observação**

O período para manutenção de lançamentos é definido por usuário, independente para quais sistemas o usuário tenha acesso. Todos os usuários que têm acesso ao sistema de Gestão Contábil devem ter o período definido. Somente usuário Supervisor terá acesso a esta tela de configuração diretamente pelo cadastro de usuários, disponível dentro das opções dos *Anexos.*
