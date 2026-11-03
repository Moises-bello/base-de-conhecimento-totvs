---
content_hash: 64e03b9261a4abe817caed750eff43d09ca6fdfc877181dc44657ed36634f4a4
fetched_at: '2026-06-29T00:10:43.717869+00:00'
page_id: '550328851'
product: rm
source: tdn-rm
title: Digitação de histórico (ensino básico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550328851
version: 3
---

# Geral

Esta tela permite incluir históricos, bem como as disciplinas que compõe cada histórico.

Histórico do Ensino Básico por Nível de Ensino

Vale ressaltar que ao configurar a exclusividade do Curso do Histórico, Grupo de Séries, Disciplinas do Histórico e Partes do Histórico por Nível de Ensino. Através do caminho: Configurações > Parâmetros >15.01 - Secretaria > Geral 3/6 > Parâmetro: **Utilizar Histórico por nível de ensino,**todo cadastro relacionado ao histórico será vinculado ao nível de ensino e visualizado apenas pelo mesmo. Caso esteja desmarcado, a visualização e utilização do histórico será por coligada.

# Copiar disciplinas

Esta funcionalidade tem por objetivo copiar as disciplinas de um histórico já existe para outro. Exemplo, copiar disciplinas do histórico 2020 para 2021.

Ao selecionar um Histórico de Origem e executar a ação de Cópia, o sistema realiza a transferência de dados para o Histórico de Destino com as seguintes regras:

* **Cópia de Disciplinas**: somente as disciplinas que não existem previamente no Histórico de Destino são copiadas. Disciplinas duplicadas no destino não são sobrescritas ou alteradas.
* **Áreas do Conhecimento**: se uma disciplina copiada possuir associação com Áreas do Conhecimento, essa associação é mantida e copiada para o destino.
* **Dados Excluídos da Cópia**: as seguintes informações não são transferidas durante o processo de cópia: **notas** e **faltas**.
