---
content_hash: f5da7a147806746c77f2e1c186a7ec70397bbf4b8c0c5ceec653d7719afe6a09
fetched_at: '2026-06-28T21:35:17.607631+00:00'
page_id: '107941778'
product: fluig
source: tdn-fluig
title: Dados para Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107941778
version: 27
---

# Índice

true.\*ndicenone

# Visão Geral

No *Analytics* apenas dados do TOTVS Fluig Plataforma são enviados para análise. Dentro dele são criados *Datasets* que se referem a conjuntos de dados enviados para geração de relatórios.

# Pré-requisitos

Conhecer como é feita a criação de um relatório no Analytics e como consultar os datasets, conforme apresentado . 

# BPM - Processos

Acompanhe a seguir as informações de Processo para geração dos relatórios.

## Dataset: solicitacao

**Objetivo:** possuir dados das solicitações já abertas.

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| solicitacaoId | Chave | Código da solicitação | 1001 4003 5851 |
| solicitacaoVersaoProcesso | Atributo | Versão do processo que está executando | 1 2 3 |
| solicitacaoIdProcesso | Atributo | Código do processo | vendas viagens |
| solicitacaoDescricaoProcesso | Atributo | Descrição completa do processo | Solicitação de Viagens  Pedido de Venda |
| solicitacaoIdSolicitante | Atributo | Código (matricula) do usuário que solicitou o processo | nome.sobrenome |
| solicitacaoNomeSolicitante | Atributo | Nome completo do solicitante | Nome Sobrnome |
| solicitacaoIdResponsavel | Atributo | Código do usuário (ou identificador do pool) que é o responsável atual da atividade | nome.sobrenome  papel |
| solicitacaoNomeResponsavel | Atributo | Nome completo do usuário ou descrição do papel/grupo | Nome Sobrnome  Grupo RH |
| solicitacaoStatus | Atributo | Situação da solicitação | Aberto  Fechado  Cancelado |
| solicitacaoIdAtividade | Atributo | Código da atividade | 3 6 8 |
| solicitacaoNomeAtividade | Atributo | Descrição completa da atividade | Aprovação de Pedido |
| solicitacaoCustom0 solicitacaoCustom1 solicitacaoCustom2   ...  solicitacaoCustom29 | Atributo | 30 campos customizado para ser preenchido via evento para servir como atributos | <qualquer valor pode ser colocado nesse campo> |
| solicitacaoFact0 solicitacaoFact1 solicitacaoFact2  ...  solicitacaoFact9 | Fato | 10 campos customizado para ser preenchido via evento para servir como fatos | 2.00 3.55 11.58 22.62 |
| createDate | Data | Data de criação da solicitação | 2013-10-10 |
| updateDate | Data | Data da ultima movimentação da solicitação | 2013-10-10 |

## Dataset: solicitacaoEmAtraso

**Objetivo:** possuir uma referência a solicitações com tarefas em atraso.

**Observação**:  Para que esse dataset seja populado é necessário cadastrar a notificação de Tarefas Atrasadas na tela Painel de Controle/Agendador de Tarefas.

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| solicitacaoId | Chave | Relaciona o dataset solicitacaoEmAtraso com o Dataset de solicitação | 1001 4003 5851 |
| solicitacaoEmAtrasoPrazo | Data | Data de expiração da tarefa | 10/10/2010 |
| solicitacaoEmAtrasoHora | Fato | Hora de expiração da tarefa. | 1  10  22 |

# ECM - Documentos

Acompanhe a seguir as informações de Documentos para geração dos relatórios.

## Dataset: documento

**Objetivo:** possuir dados de visualização de documentos

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| documentoId | Chave | Chave do documento composta pelo código e a versão | 8558\_1000  8558\_2000  82517\_1000 |
| documentoCodigo | Atributo | Código do documento | 8558  82517 |
| documentoVersao | Atributo | Versão do documento | 1000  2000 |
| documentoDescricao | Atributo | Descrição principal | Norma da Qualidade  Melhores práticas de projetos  Caso 229 - Cliente ACME |
| documentoIdPublicador | Atributo | Código do usuário (matricula) que publicou o documento | nome.sobrenome |
| documentoNomePublicador | Atributo | Nome completo do usuário que publicou o documento | Nome Sobrenome |
| documentoIdAutor | Atributo | Código do usuário que elaborou o documento | nome.sobrenome |
| documentoNomeAutor | Atributo | Nome completo do usuário que elaborou o documento | Nome Sobrenome |
| documentoTipo | Atributo | Descrição do tipo de documento | Documento  Pasta  Formulário |
| documentoAssunto | Atributo | Descrição do assunto | Padrão |
| documentoIdPai | Atributo | Código da pasta/Formulário | 8871 |
| documentoDescricaoPai | Atributo | Descrição da pasta/formulário |  |
| documentoExtensao | Atributo | Extensão do arquivo principal | PDF  DOCX |
| documentoDownload | Atributo | Informação se o download é permitido | true  false |
| documentoQtAcessos | Fato | Quantidade de acessos ao documento | 1  53 |
| documentoTamanho | Fato | Tamanho em bytes dos arquivos | 1024  6370187 |
| createDate | Data | Data de criação do documento | 2013-10-10 |
| updateDate | Data | Data da ultima alteração | 2013-10-10 |

Importante!

Documentos armazenados nas pastas particulares (Meus Documentos) **não são sincronizados** com o Analytics, pois estes diretórios são de uso e visualização exclusivas do usuário autenticado.

# WCM - Portais - Hit de página

Acompanhe a seguir as informações de Hit de página para geração dos relatórios.

## Dataset: pageHit

**Objetivo:** possuir informações sobre os acessos as páginas.

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| pageHitIdHit | Chave | Identificador único do hit | usuario\_87979879874212111 |
| pageHitCodPagina | Atributo | Código da página | home  cpaineladmin  comurh |
| pageHidDescPagina | Atributo | Descrição da página | Home  Painel administração  Comunidade RH |
| pageHitLoginHit | Atributo | Login do usuário | [nome.sobrnome@empresacom](mailto:nome.sobrnome@empresacom) |
| pageHitHora | Atributo | Hora do acesso | 17 |
| pageHitMinuto | Atributo | Minuto  do acesso | 30 |
| pageHitQtHit | Fato | Valor para fixo para calculo | sempre 1 |
| hitDate | Data | Data do acesso | 10/10/2013 |

# Social

Acompanhe a seguir as informações Sociais para geração dos relatórios.

## Dataset: Events

**Objetivo:** possuir eventos sociais que ocorram dentro da plataforma TOTVS Fluig. Atributo customizado que pode ser populado via API Pública.

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| eventId | Chave | Código único do evento no formato {eventType}{entityID} | POST5578 COMMENT158936 |
| eventType | Atributo | Tipo de evento social que ocorreu | LIKE POST COMMENT DENOUNCE  SHARE MENTION |
| eventSubType | Atributo | Sub tipo de evento social que ocorreu | DEFAULT <quando não há sub tipo> LIKE\_POST LIKE\_COMMENT SHARE\_POST MENTION\_SHARE MENTION\_POST MENTION\_COMMENT |
| referenceId | Atributo | Código do evento raiz  Ex: se é um comentário, esse código informa o Post que gerou o comentário | 331 21313 32772 |
| customAttr0 | Atributo | Atributo customizado que pode ser populado via API Publica |  |
| customAttr1 | Atributo | Atributo customizado que pode ser populado via API Publica |  |
| customAttr2 | Atributo | Atributo customizado que pode ser populado via API Publica |  |
| placeId | Atributo | Código da comunidade ou usuário onde foi feita a ação Juntamente com esse campo existe um rótulo "name" | 554 -> CIPA 1122 -> Ana maria |
| gdPost | Fato | Campo para soma | 1 <sempre será valor 1> |
| customFact0 | Fato | Fato customizado que pode ser populado via API Publica |  |
| customFact1 | Fato | Fato customizado que pode ser populado via API Publica |  |
| customFact2 | Fato | Fato customizado que pode ser populado via API Publica |  |
| createDate | Data | Data de criação do evento | 2013-10-10 |
| authorId | Chave | Código do autor que fez a ação Juntamente com esse campo existe um rótulo "name" | 1122 -> Ana Maria 3312 -> João Silva |
| placeId | Chave | Código da comunidade ou usuário onde foi feita a ação Juntamente com esse campo existe um rótulo "name" | 554 -> CIPA 1122 -> Ana maria |

## Dataset: Author

**Objetivo:** possuir dados dos autores de eventos sociais com informações de seu perfil na plataforma TOTVS Fluig

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| authorId | Chave | Código o autor que fez a ação Juntamente com esse campo existe um rótulo "name" | 1122 -> Ana Maria 3312 -> João Silva |
| removed | Atributo | Informa se o autor está desativado | 0 <ativo> 1 <desativado> |
| participations | Fato | Número de comunidades que o autor participa | 111 |
| followers | Fato | Número de seguidores do autor | 222 |
| followings | Fato | Número de usuários que o autor segue | 333 |
| likes | Fato | Campo não utilizado |  |
| posts | Fato | Campo não utilizado |  |
| moderations | Fato | Campo não utilizado |  |
| images | Fato | Campo não utilizado |  |
| videos | Fato | Campo não utilizado |  |

## Dataset: Place

**Objetivo:** possuir dados das comunidade onde foram feitas as ações sociais

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| placeId | Chave | Código da comunidade ou usuário onde foi feita a ação Juntamente com esse campo existe um rótulo "name" | 554 -> CIPA 1122 -> Ana maria |
| removed | Atributo | Informa se a comunidade está desativado | 0 <ativa> 1 <desativada> |
| placeType | Atributo | Informa se é uma comunidade ou é um usuário | COMMUNITY USER |
| hidden | Atributo |  | false true |
| privateContent | Atributo |  | false true |
| requireApproval | Atributo | Necessita aprovação | false true |
| members | Fato | Número de participantes na comunidade | 30 4454 9547 |
| images | Fato | Campo não utilizado |  |
| videos | Fato | Campo não utilizado |  |
| documents | Fato | Campo não utilizado |  |
| articles | Fato | Campo não utilizado |  |

## Dataset: WatchContent

**Objetivo:** Informações sobre os conteúdos observados pelos usuários

| Campo | Tipo | Descrição | Exemplos de valores |
| --- | --- | --- | --- |
| watchId | Chave | Código único do watch | 345 |
| wc\_contentType | Atributo | Identifica o tipo de objeto a ser observado | COMMUNITY  DOCUMENT  POST |
| wc\_contentId | Atributo | Id do comunidade, post ou do documento que esta sendo observado | 123 |
| wc\_version | Atributo | caso o objeto for um documento traz a versão do documento que esta sendo observada | 1000 |
| wc\_parentType | Atributo | Campo não utilizado |  |
| wc\_parentId | Atributo | caso o objeto for um documento  traz o id da pasta ou do formulário onde o documento esta publicado | 1 |
| wc\_removed | Atributo | Campo não utilizado |  |
| wc\_fact | Fato | Fixo 1 | 1 |
| placeId | Chave | Código da comunidade, post ou documento onde foi feita a ação Juntamente com esse campo existe um rótulo "name" | 554 -> CIPA 1122 -> Ana maria |
| authorId | Chave | Código do autor que fez a ação  Juntamente com esse campo existe um rótulo "name" | 1122 -> Ana Maria 3312 -> João Silva |
| createDate | Data | Data de criação | 2016-10-10 |
