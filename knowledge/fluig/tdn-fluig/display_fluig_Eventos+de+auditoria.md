---
content_hash: eafcb6e8bffc2d027b50ce47371ee00406e7511e79191c4ce12d45ddbde4b045
fetched_at: '2026-06-28T21:35:25.828238+00:00'
page_id: '312154706'
product: fluig
source: tdn-fluig
title: Eventos de auditoria
type: documentation
url: https://tdn.totvs.com/display/fluig/Eventos+de+auditoria
version: 40
---

Atenção!

Esse recurso está disponível a partir da **atualização 1.6.4 - Waterdrop**. Leia abaixo como obtê-lo.

trueÍndicenone

# Objetivo

Esse guia tem o objetivo de apresentar uma visão geral do recurso Eventos de auditoria no TOTVS Fluig Plataforma. Será abordado como obtê-lo, como utilizá-lo e como funciona.

# Visão geral

O recurso **Eventos de Auditoria** permite registrar alterações realizadas na plataforma em recursos específicos como Papel, Usuários, Grupos, Processos, Documentos, entre outros.

# Como obter

Para obter as licenças para uso do recurso **Eventos de Auditoria**é necessário entrar em contato com o time comercial solicitando uma proposta, através do e-mail [fluig.prime@fluig.com](mailto:fluig.prime@fluig.com). Com isso, o time comercial irá passar as instruções sobre a ativação da licença no .

# Como ativar os eventos de auditoria

A ativação de registro dos eventos de auditoria é realizada para cada empresa *(tenant)* individualmente, acessando a plataforma com o usuário wcmadmin. Consulte a documentação de  para saber os passos detalhados sobre como configurar a gravação dos eventos de auditoria.

# Como consultar os eventos e exportar os resultados

O recurso de Eventos de auditoria permite ao administrador da plataforma consultar os dados registrados, filtrando por usuário, recurso e período da atividade.

Com o objetivo de oferecer uma análise mais detalhada, é possível exportar os dados de auditoria no formato CSV (compatível com softwares de planilha eletrônica como o Microsoft₢ Excel).

Os passos detalhados para consultar os eventos registrados e gerar o relatório podem ser consultados na documentação de .

# Como saber os eventos que geram log

Todos os eventos em Papéis, Usuários, Grupos, Processos, Documentos geram log na plataforma. O registro dos eventos foi dividido em dois tipos específicos: **eventos gerais para auditoria** e **eventos de dados pessoais**. A estrutura dos dois tipos é semelhante, mas o objetivo é bem diferente. 

A diferença básica entre eles é que nos eventos gerais de auditoria foram previamente definidos os pontos de monitoramento. No caso dos dados pessoais, foram elencados os pontos que podem ter dados pessoais, monitorados a partir do mapeamento desses campos ([veja aqui](https://tdn.totvs.com/x/OfheI)).

## Eventos gerais que registram log para auditoria

Nos eventos gerais, o foco de realizar uma auditoria é saber quem criou ou editou um registro. Por isso, são auditadas as ações relacionadas abaixo:

Plataforma

- criação, edição, remoção, alteração em código-fonte, cache mobile, sincronização.

 - criação, edição, recuperação de senha pessoal.

- inclusão, edição e remoção de grupo; inclusão e remoção de usuário no grupo.

- inclusão, edição e remoção de papel; inclusão e remoção de usuário no papel; inclusão e remoção de papel no grupo.

Processos

- criação, edição e remoção; criação, edição e remoção no processo.

- criação, liberação, edição, remoção de versão de processo.

- criação, edição, remoção de processo.

- criação, edição, conversão, remoção, transferência de atividade, assumir atividade.

- criação, edição, remoção.

- criação, edição, remoção de anexo do processo.

Documentos

 - criação, edição, nova revisão, nova versão, restaurar revisão, restaurar versão, exclusão de documento da navegação, espelhar documento, marcar e desmarcar como favorito, *download*, mover de pasta, copiar.

- criação, edição de pasta, mover, copiar.

- criação, edição de aplicativo.

- criação, edição de formulário.

- criação, edição de registro de formulário.

- criação, edição de arquivo físico, remoção, mover.

- criação, edição de artigo.

- criação, edição de documento externo, mover, copiar.

- criação, edição de relatório, mover, copiar.

- limpeza da lixeira, exclusão de item da lixeira, restaurar item da lixeira, inclusão de tarefa de agendamento de limpeza da lixeira.

## Eventos de dados pessoais que registram log para auditoria

Nos eventos de dados pessoais, o foco é facilitar o atendimento à [LGPD](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789), informando ao usuário quem teve acesso às informações dele. Por isso, a visualização de registros que contenham dados pessoais é controlada, o que envolve os recursos abaixo:

 - criação, edição, visualização de usuário (ação realizada por outro usuário).

Registro de formulários - criação, edição, visualização (via tela ou webservice).

Lembrando que, no caso dos dados de formulário, podem ser incluídos como dados pessoais :

* Formulários criados com o Forms,
* Formulários avançados, criados no fluig Studio,
* Formulários de processos e
* Formulários de comunidades.
