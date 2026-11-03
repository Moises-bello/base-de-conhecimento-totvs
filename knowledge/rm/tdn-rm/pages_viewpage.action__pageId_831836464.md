---
content_hash: c6e5d57523df5958b1813d7dd3fcfb86ea4742a9803628ef9f9e08b1d8975f69
fetched_at: '2026-06-29T00:11:49.371792+00:00'
page_id: '831836464'
product: rm
source: tdn-rm
title: Enviar / Reenviar Mensagem EAI por Filtro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=831836464
version: 1
---

Esse processo permite o envio/reenvio das mensagens EAI, baseado em um filtro determinado pelo usuário com a possibilidade de definir uma recorrência e fracionamento de jobs para uma melhor desempenho.

O processo está disponível no menu "Utilitários | Outros | Mensagem EAI | Enviar / Reenviar Mensagem EAI por filtro"

**Segurança de Fracionamento de Jobs**

Para que o processo seja executado é necessário definir a segurança de fracionamento de jobs no menu "Ambiente | Segurança de Jobs Fracionados" incluindo um novo registro:

Perfil: Perfil do usuário que irá executar o processo com fracionamento

Classe do Job: FinReenviaMsgEAIFiltroProcData

Min. Frações: Mínimo 2

Max. Frações: Defi

Marcar opção "Departamento Ativo" (Ativa o fracionamento do processo)

Marcar opção "Agendável" (Se marcado o parâmetro, o processo é passível de agendamento, caso esteja desabilitado o processo não poderá ser agendado)

Mais detalhes sobre a segurança de jobs fracionados [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=547231277)

**Definição do filtro para execução**

Antes de executar o processo é necessário definir um filtro. Esse filtro pode ser montado baseado na tela de filtro padrão do TOTVS RM utilizando todos os seus recursos para montar as condições.

**Agendamento**

Caso ambiente esteja configurado para executar em 3 camadas, será possível efetuar um agendamento para que o processo seja executado em determinado horário ou até mesmo uma recorrência.

Também é possível definir em quantos jobs o processo será definido conforme a quantidade de frações definidas na segurança de jobs fracionados.
