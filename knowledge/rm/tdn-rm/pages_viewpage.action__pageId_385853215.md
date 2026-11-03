---
content_hash: e19316c5932ab1aa75d9f1c19696eac46b3f76acb3d463882b6cdfb9c8985b26
fetched_at: '2026-06-29T00:09:07.871193+00:00'
page_id: '385853215'
product: rm
source: tdn-rm
title: 3443793 FOPROTINAS01-5262 DT - Filtro Incorreto na Visualização de Subordinados
  de um Supervisor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385853215
version: 1
---

# EXIBIR APENAS OS FUNCIONÁRIOS PERTENCENTES À EQUIPE DO SUPERVISOR NA TELA DE SUBORDINADOS DO RM PORTAL - PORTAL RH

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Recursos Humanos |
| **Módulo:** | RM Portal - Portal RH |
| **Função:** | Subordinados |
| **Situação/Requisito:** | Quando o parâmetro "Estende o código de equipes para supervisores relacionados a este grupo de acesso" (no parametrizador do RM Portal, na etapa "Supervisores") está marcado, ao acessar o RM Portal com o usuário de um supervisor e clicar em Portal RH >> Equipe >> Subordinados, são exibidos incorretamente todos os funcionários da coligada em que ele é supervisor. Isso ocorre apenas quando o funcionário é supervisor em mais de uma seção. Entretanto, é emitido erro quando o supervisor tenta editar um funcionário que não pertence à sua equipe. Se o parâmetro estivesse desmarcado, seriam exibidos todos os funcionários das seções em que ele é supervisor, até mesmo aqueles que não pertencem à sua equipe. |
| **Solução/Implementação:** | Foi ajustado o filtro utilizado para recuperar corretamente apenas os funcionários pertencentes à equipe do supervisor quando ele acessar a tela de Subordinados do Portal RH. |
| **Tickets relacionados:** | 3443793 |
