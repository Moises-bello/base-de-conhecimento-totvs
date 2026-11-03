---
content_hash: d0256baa7a49e30c83c56caa9170a0f8d980e59ab9202818ade851cc282a30a6
fetched_at: '2026-06-29T00:08:37.620424+00:00'
page_id: '284880233'
product: rm
source: tdn-rm
title: Requerimentos solicitados
type: documentation
url: https://tdn.totvs.com/display/LRM/Requerimentos+solicitados
version: 29
---

Nessa página o aluno/responsável terá uma visão geral das solicitações. Através desse menu, o mesmo tem a opção acompanhar e interagir com as movimentações das solicitações.

Para acessar o processo de integração entre o TOTVS Educacional e o TOTVS Aprovações e Atendimento. **Para saber mais acesse** [Integração TOTVS Educacional x TOTVS Aprovações e Atendimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037558413-RM-EDU-Como-realizar-a-integra%C3%A7%C3%A3o-Totvs-Educacional-x-Totvs-Gest%C3%A3o-de-Relacionamento-com-o-Cliente).

Permissão de acesso

Para acessar a funcionalidade, o perfil do usuário deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Acadêmico | Solicitações**

Filtros

O sistema disponibiliza as seguintes opções como filtro:

* Grupo de atendimento;
* Número de protocolo;
* Lista de todos os dependentes

Lista de todos os dependentes

Esse filtro lista a relação de todos os requerimentos solicitados de todos os seus dependentes (inclusive a do próprio usuário logado, caso o mesmo seja aluno e responsável e tenha requerimentos criados com o seu usuário) do responsável financeiro ou responsável acadêmico ou mãe ou pai, independente do aluno selecionado, caso o usuário logado seja o próprio aluno, este filtro não será exibido.

**Exemplo:** No portal fiz o login com o usuário da mãe, essa mãe é vinculada a dois alunos diferentes, então clicando nesse filtro deve aparecer os requerimentos dos dois alunos. 

Dados da solicitação

A solicitações possui as seguintes informações:

* Data e Hora de abertura: A data que foi criada a solicitação;
* Protocolo: Número do protocolo gerado pelo sistema;
* Status: Status da solicitação, podendo ser: **Em andamento**, **Concluído**, **Cancelado**;
* Etapa atual: A etapa atual em que a solicitação se encontra dentro do fluxo de aprovação;
* Solicitação: A descrição da solicitação de atendimento informado no ato da abertura.
* Discussão: Mantém todo o histórico de discussão referente caso o aluno/responsável interaja na solicitação.
* Arquivos: Lista da relação de arquivos adicionados no requerimento.
Anexo da solicitação

A solicitação tem a possibilidade de o usuário adicionar arquivo de anexo.

Parametrização de armazenamento

Para o funcionamento, será necessário realizar informar do parametrização do armazenamento de arquivos em: **TOTVS Aprovações e Atendimento |** **Configurações | Parâmetros | Arquivos anexos ao atendimento. Saiba mais em**

Upload de arquivos grandes

Caso a instituição permita uploads no portal com tamanho superior ao tamanho padrão **30mb** do **IIS(Internet Information Services)**será necessário realizar algumas configurações adicionais. Saiba mais em

Incluir anexo

Para incluir arquivo, o usuário deverá possui a permissão e selecionar a opção de "Enviar arquivos"

Permissão

A opção "Enviar arquivos" só estará disponível mediante a permissão no CRM em: **TOTVS Aprovações e Atendimento | Meus Atendimentos | Atendimentos | Atendimentos | Arquivos anexos do atendimento**

Baixar aquivo

Para baixar arquivo, o usuário deve selecionar a opção de "Download".

Discussão da solicitação

A solicitação tem a possibilidade do usuário adicionar uma nova discussão.

Permissão

A opção "Adicionar discussão" só estará disponível mediante a permissão no Educacional em: **Educacional | Educacional | Educacional (Portal) | Acadêmico | Solicitações | Permitir inclusão de discussão no atendimento**

Cancelamento da solicitação A opção "**Cancelar Requerimento**" só estará disponível mediante a permissão em: **TOTVS Aprovações e Atendimento | Meus Atendimentos | Atendimentos | Atendimentos | Cancelar Atendimentos**Responsável atual da solicitação

O requerimento poderá ser cancelado corretamente, mesmo que o **responsável pela abertura** seja diferente do **responsável atual da solicitação**. Esta regra é **exclusiva do portal do aluno**, **não contempla no RM.EXE**.

Cancelamento da solicitação com lançamento já gerado

O requerimento **não poderá ser cancelado** caso tenha um lançamento já gerado associado a ele.

Legenda

A tela conta com uma legenda onde é possível identificar de forma clara e objetiva as solicitações apresentadas.
