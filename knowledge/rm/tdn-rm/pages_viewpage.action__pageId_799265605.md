---
content_hash: 12d878af918349c5a381581a5c910f375fe0cd24f28dde73fdc391bce75dbba4
fetched_at: '2026-06-29T00:11:42.819739+00:00'
page_id: '799265605'
product: rm
source: tdn-rm
title: 02 - Modelos de Ficha Médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799265605
version: 39
---

# Sumário

---

Sumário

# Objetivo

---

A ficha médica flexível permite que o cliente crie modelos totalmente flexíveis conforme sua necessidade, portanto aqui deverá ser construído o modelo da ficha médica que será utilizado pela instituição.

Nesta tela será possível realizar a gestão dos modelos cadastrados podendo executar as seguintes operações: **criar**, **excluir** e **editar** um Modelo de Ficha médica.

# Pré-requisitos

---

Para que o menu do **Modelo da Ficha Médica** seja apresentado em **TOTVS Educacional** | **Educacional** | **Configurações**, conforme a imagem de criação de novo modelo, será necessária a realização da [parametrização](https://tdn.totvs.com/pages/viewpage.action?pageId=790645086) e também configuração das devidas permissões no perfil.

Em  [parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=790645086) o usuário poderá alterar o nome do modelo. Caso o usuário não informe um nome em parâmetros e o campo "nome para apresentação no sistema" fique sem preenchimento, automaticamente o nome do modelo será **Ficha Médica**.

* **Permissão**

Por questão de segurança e rastreabilidade, as requisições serão permitidas somente para um usuário cadastrado no RM, portanto é necessário conceder as devidas permissões para o perfil do usuário que irá executar as requisições.

# Criação de novo modelo

---

Para criar um novo modelo, clicar em "**Criar nova ficha médica +"**. Sendo obrigatório informar um Nome e opcionalmente a Descrição para o modelo.

Após o modelo ter sido criado, poderá **Editar** a ficha a qualquer momento, editando o nome e/ou a descrição.

**Excluir o modelo**: Na edição do modelo da ficha médica, o modelo poderá ser excluído, exceto se já tiver campo associado preenchido por aluno ou candidato.

Ao excluir um modelo de ficha médica que não possua campos associados preenchidos, toda a sua estrutura, agrupadores, seções e campos, serão definitivamente excluídos, não sendo possível recuperá-los.

No modelo da ficha criada, está disponívela opção de **Ativar** ou **Inativar** um modelo.

É permitido somente um modelo ativo por contexto, não sendo possível ativar outros modelos para o mesmo contexto.

O modelo que estiver ativo será o modelo disponibilizado em todos os locais do RM, tais como, anexo do cadastro do aluno, portal do aluno, matricula via portal, PGE.

## Fazer uma cópia para outro contexto

---

Cópia 

Na opção **Fazer uma cópia para outro contexto** (Coligada | Filial | Nível de Ensino), ao ser copiada, o modelo poderá ser modificado somente no novo contexto.   
Podendo realizar a cópia para mais de uma Coligada | Filial | Nível de Ensino

O modelo que for realizado a cópia, ficará com a palavra Cópia em frente ao nome do modelo.

Para seguir com a estruturação do modelo e criar os itens de Agrupador, Seção e/ou Campo, clicar em **[Acessar ficha médica](https://tdn.totvs.com/pages/viewpage.action?pageId=801997666)**.
