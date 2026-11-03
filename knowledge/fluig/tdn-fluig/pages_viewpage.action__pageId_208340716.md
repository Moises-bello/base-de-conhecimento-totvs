---
content_hash: 1a77ebc46f6edaccbe93581b8ff71d09ed14c4602433159ea2f1258c8739207f
fetched_at: '2026-06-28T21:35:19.494103+00:00'
page_id: '208340716'
product: fluig
source: tdn-fluig
title: BPM 013 - Qual a diferença da consulta com usuário comum e com usuário administrador?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208340716
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:**Todas as versões

# Ocorrência

Consulta de Solicitações não está achando solicitações para usuários comuns quando marcada "Todas as Solicitações Públicas".

# Causa

Há uma diferença no caso da Consulta de Solicitações para usuário administrador e comum. Para usuário administrador, há a flag "Todas as Solicitações", que faz a pesquisa procurar dentre todas as solicitações da plataforma para aquela empresa. Já para usuários comuns, a flag torna-se "Todas as Solicitações Públicas", que busca todas solicitações cujos processos são marcados como "Público" nas configurações do mesmo.

**Observação:** O comportamento acima só muda para o usuário comum, caso ele tenha selecionado a flag "Todas as Solicitações Públicas" e tenha selecionado algum processo na listagem de processos. Neste caso o se o usuário possuir algum processo igual ao selecionado a plataforma irá retorná-lo, mesmo este processo não sendo publico.

# Solução

É um comportamento da plataforma, não um problema real, sendo possível marcar os processos como públicos caso seja realmente necessário que usuários comuns busquem solicitações que os mesmos não tem acesso.
