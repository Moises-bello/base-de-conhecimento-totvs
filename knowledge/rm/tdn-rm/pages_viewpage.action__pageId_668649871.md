---
content_hash: 24d44ba0ddf7dcde0e5a663730fcc77fc6f1caf2b574dc101a9e47c411112356
fetched_at: '2026-06-29T00:11:16.495904+00:00'
page_id: '668649871'
product: rm
source: tdn-rm
title: Permissão de Perfil do Usuário - Regras de validação do Evento da EFD-Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668649871
version: 11
---

# Conteúdo

Conteúdononenone

# 1. Visão Geral

Para facilitar a execução de testes em bases que já tenham dados de transmissão da EFD-Reinf, foi disponibilizada uma permissão no **perfil do usuário** para permitir apagar/editar os dados existente sem gerar reflexos no ambiente da Receita Federal do Brasil (RFB). 

# 2. Perfil do Usuário

A permissão está disponível através Perfil de usuário | acesso a menus | Gestão Fiscal | Obrigações Acessórias | SPED | SPED | EFD-Reinf | Eventos | **Sobrescrever Regras de Validação**

Imagem

# 3. Regras

Um vez que a permissão estiver concedida, o usuário poderá **sobrescrever as regras de validação do Evento da** **EFD-Reinf** sendo permitido editar e apagar os Eventos gerados sem qualquer validação do sistema, como status e TSS por exemplo. Estas alterações podem ser realizadas em qualquer Evento, seja ela Periódico ou Cadastral, sendo que:

No caso de Edição, é gravado um histórico indicando que ocorreu alteração manual e do nome do usuário que fez a alteração, além disso **as alterações não terão efeitos no ambiente da RFB.**

Edição

Com Status **Autorizado**

Com Status **Não Transmitido**

Após edição- **Histórico do Evento**

Ao excluir os Eventos, é informado ao usuário que a exclusão do registro na base **não terá nenhum efeito no** **ambiente da RFB** e **não poderá ser revertida.**

Exclusão

Ao Excluir Evento Periódico - Mensagem na Tela

Evento Periódico Excluído
