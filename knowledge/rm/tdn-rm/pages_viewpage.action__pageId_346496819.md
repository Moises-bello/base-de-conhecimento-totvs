---
content_hash: 011d74810d2d8d546922457dca5eabe3d2be429a90b99e79ba56c38e94961a86
fetched_at: '2026-06-29T00:08:54.809991+00:00'
page_id: '346496819'
product: rm
source: tdn-rm
title: Actions - Funcionalidade Carregar Automaticamente e Actions Obrigatórias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346496819
version: 14
---

# Objetivo:

---

     Este documento tem por objetivo especificar a os tipos de actions e a funcionalidade Carregar Automaticamente e as Actions Obrigatórias.

# Tipos de Action:

---

     As actions podem ser de dois tipos:

**Actions de Desenvolvedores:** são actions fixadas em código, ou seja, actions desenvolvidas, para uma tela ou um conjunto de telas em especifico.  
- Essas actions não podem ser relacionadas à outras telas por intervenção do usuário.  
- Essas actions não podem ser desativadas.  
- Actions do subtipo Detalhe poderão ser configuradas como obrigatórias ou ser carregadas automaticamente.  
- Por outro lado, actions do Tipo Extensão (Extender), não poderão ser nem obrigatórias e nem carregadas automaticamente.

Percebam na imagem acima que os botões de **adicionar** e **remover relacionamento** estão **desabilitados**, porém as opções **Carregar automaticamente** e **Obrigatório** estão **habilitadas**, o que configura uma action do tipo **Desenvolvedor/Fixo** e do subtipo **Detalhe**.

Percebam na imagem acima que tanto os botões de **adicionar** e**remover relacionamento** quanto as opções **Carregar automaticamente** e **Obrigatório** estão **desabilitadas**, o que configura uma action do tipo **Desenvolvedor/Fixo** e do subtipo **Extender**.

Importante

Ao tentar remover uma **Action de Desenvolvedor**, será exibida uma mensagem similar a esta: "Você não pode remover uma Action do produto!".

Caso seja realmente necessário remover este anexo, por não fazer mais parte do produto é possível realizar esta ação no cadastro **Actions Anexas**.

Obs: Caso a action excluída ainda fizer parte do produto, ou seja estiver fixada em código, mesmo que seja excluída ela irá aparecer novamente.

* **Actions Configuradas pelo Usuário:** são actions que podem ser adicionadas pelo Usuário e devidamente configuradas pelo mesmo.  
  - Essas actions podem ser relacionadas à outras telas por intervenção do usuário.  
  - Essas actions podem ser desativadas.  
  - Actions do subtipo Detalhe poderão ser configuradas como obrigatórias ou ser carregadas.

Adicionar Action como Anexo

Para adicionar uma action anexa à uma tela Mestre, clique em **Action;**

Escolha a Action que será anexada.

Agora só falta configurar o relacionamento entre a action Pai e a action Filha.

Percebam na imagem acima que tanto os botões de **adicionar** e **remover relacionamento** quanto as opções **Carregar automaticamente** e **Obrigatório**estão**habilitadas**, o que configura uma action do tipo **Configurada pelo Usuário** e do subtipo **Detalhe**.

Actions Extender

As actions extender são sempre do tipo Desenvolvedor/Fixo, elas são apenas apresentadas na lista de actions, porém não podem ser alteradas pelo usuário.

# Subtipos de Action:

---

     As actions podem ser de dois subtipos:

* **Detalhe:** São Actions completas, ou seja, possuem uma tela de visão composta por uma grid (tabela) que apresenta todos os registros de um determinado dataserver, e uma tela de edição onde registros podem ser editados por ali.

**Tela de Visão da Action.**

**Tela de Edição da Visão.**

* **Extender:**São actions, que como o nome diz, são extensões da action mestre/pai, elas não tem uma tela de visão, elas possuem apenas uma tela de edição.

**Tela de Edição da Action**

Actions Extender

Devido à peculiaridade estrutural da action Extender ,elas não podem ser colocadas em anexo, por não possuirem uma estrutura de relacionamento de dados (bindingSource), assim como a action mestre/pai, inviabilizando assim sua ligação.

# Funcionalidade Carregar Automaticamente:

---

     A funcionalidade **Carregar automaticamente** permite que actions **Detalhe** possam ser carregadas sempre que a action mestre/pai for executada.

Escolha a Action desejada, clique na opção **Carregar automaticamente.**

A tela à seguir, deverá ser apresentada tanto no momento da configuração, quanto ao executar a action mestre/pai.

Atenção

Cuidado ao relacionar à action pai à action filha, os tipos das colunas têm que ser compativeis, pois se não a exceção abaixo poderá ser levantada.

# Actions Obrigatórias:

---

     A funcionalidade **Actions obrigatórias** permite que a action configurada se torne parte da action pai, participando não só fisicamente na estrutura da action (como aba na tela de edição), mas também das suas validações.

A tela à seguir, deverá ser apresentada tanto no momento da configuração e como parte da edição da action pai.

Atenção

Cuidado ao relacionar à action pai à action filha, os tipos das colunas têm que ser compativeis, pois se não a exceção abaixo poderá ser levantada.
