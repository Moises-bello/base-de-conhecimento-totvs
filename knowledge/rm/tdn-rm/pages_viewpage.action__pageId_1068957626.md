---
content_hash: 5ed67a0681396d7c7d5af8c59828a5bad6cb9a9d3708bf8cbb5358c74da9f0c7
fetched_at: '2026-06-29T00:05:53.306964+00:00'
page_id: '1068957626'
product: rm
source: tdn-rm
title: Sumário de Alta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068957626
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Permissão de Acesso**
3. **Exemplos de Utilização**

Formulários dinâmicosVisão Geral

## **01. VISÃO GERAL**

Centralizada para gerenciar os sumários de alta do paciente, para documentar desfechos clínicos, acompanhar o status de transmissão e consultar o histórico de internações de forma segura e organizada.

Permissões de acesso

## **02. PERMISSÕES DE ACESSO**

O Administrador do sistema, pode configurar permissões de acesso à tela de "Sumário de Alta" vinculadas ao perfil de usuário. Para que apenas profissionais assistenciais autorizados possam visualizar ou interagir com os desfechos clínicos, garantindo a privacidade e a segurança dos dados do paciente.

**REGRA DE NEGÓCIO**

---

* O controle de acesso é aplicado ao *Perfil* do usuário
* Se o perfil do usuário logado não possuir permissão de acesso ao "Sumário de Alta", o item correspondente não será exibido no menu lateral do prontuário.
* A permissão pode ser fragmentada em níveis:
  + Visualizar;
  + Inserir;
  + Suspender;
  + Imprimir;

As permissões podem ser acessadas em: **Serviços Globais > Segurança > Perfis > Acesso à Menus > Hospitais e Clínicas > Prontário Eletrônico > Prontuário do Paciente > Sumário de Alta**:

Ao desabilitar a permissão de acesso de **Inserir**, o botão **Novo** será será desabilitado, impedindo o usuário de criar novo registro;

Ao desabilitar a permissão de acesso de **Imprimir**, o botão **Imprimir** será desabilitado, impedindo o usuário de imprimir o registro;

Ao desabilitar a permissão de acesso de **Suspender**, o botão **Suspender** será desabilitado, impedindo o usuário de imprimir o registro;

A permissão de **Visualizar**, é responsável por disponibilizar a tela de sumário de alta via menu lateral, permitindo ao usuário ver os registros na tabela;

A permissão de **Editar**, é responsável por habilitar/desabilitar a função de salvar o rascunho do usuário na tela de cadastro de sumário de alta:

Exemplo de utilização

## **03. LISTAGEM DOS DADOS**

A tela apresenta uma tabela única, onde cada linha representa um registro de Sumário de Alta.  
A listagem contempla os sumários de alta de todos os atendimentos do paciente.

Filtros

Ao clicar em "Filtrar" os campos para filtro são exibidos na lateral direito da tela.   
É possível aplicar filtros por Status, Período de Alta (início e fim), código do atendimento, CID, desfecho e profissional.

Colunas

* Data Alta (data da alta do paciente)
* Atendimento (código do atendimento em que o registro foi preenchido)
* CID Principal (descrição da CID principal)
* Defecho (desfecho)
* Responsável (responsável pelo preenchimento do registro)
* Visualização (permite uma visualização rápida do registro)
* Mais ações
  + Editar (redireciona para o formulário carregando um registro para edição)
  + Imprimir (gera um impresso do registro)
  + Suspender (suspende um registro finalizado)
  + Excluir (exclui um registro em rascunho)
  + Assinar (redireciona para o formulário carregando um registro finalizado com falha de assinatura para ser assinado)

## **03.1 DADOS DE EPISODIO**

## **03.2 DIAGNÓSTICO**

## **03.3 RESUMO CLÍNICO**

Essa seção contém campos obrigatórios referentes ao resumo clínico do paciente:

* Campo "Motivo de internação / queixa principal:.
* Campo **"**Evolução clínica e condição na alta":

Marcando a opção "Importar dados da anamnese", o sistema preenche os dados de Motivo de internação com o campo Resumo primeira anamnese finalizada, e preenche os dados de Evolução Clínica com o campo Exame Físico da ultima anamnese finalizada.
