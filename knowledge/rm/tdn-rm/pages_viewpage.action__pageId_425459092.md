---
content_hash: e0a1e33bf6fd8e74870c08d40f14eb56ef7d71f6e911a7d90317318e6b70f85e
fetched_at: '2026-06-29T00:09:33.953199+00:00'
page_id: '425459092'
product: rm
source: tdn-rm
title: Requerimento.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459092
version: 25
---

Nesta tela possibilita criar novos requimentos do aluno.

Para mais informações  [Como realizar a integração TOTVS Educacional x TOTVS Aprovações e Atendimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037558413-RM-EDU-Como-realizar-a-integra%C3%A7%C3%A3o-Totvs-Educacional-x-Totvs-Gest%C3%A3o-de-Relacionamento-com-o-Cliente).

Configurações necessárias

É necessário realizar as parametrizações dos campos de "Atendente para abertura de atendimentos" e "Categoria geral" em: **Ambiente | Parâmetros Globais | Integração | Atendimento**

Perfil de acesso

Para acessar a funcionalidade, o perfil deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional | Atividades acadêmicas| Requerimentos | Requerimentos**

Fórmula associada ao tipo de atendimento

Quando o **tipo de atendimento** informado possuir uma fórmula a mesma será executada **automaticamente**. Caso a fórmula retorne **qualquer valor diferente do esperado**, o processo não será executado.

A fórmula deverá retornar:

1. O atendimento será criado normalmente, obedecendo os parâmetros de geração de serviço / verificação de inadimplência para **criar parcela/lançamento**;
2. O atendimento será criado, mas **não será criada parcela ou inserido lançamento**;
3. O atendimento **não será criado**;

Matrícula no período letivo

O contexto da fórmula será a matrícula no período letivo, baseado na matriz aplicada do curso do aluno ou do contrato. **Caso não encontrado**, será considerado a **criação normal do atendimento**.

ProcessoPasso 1

Neste passo o grupo de atendimento e tipo de atendimento deverão ser informados.

Passo 2

Neste passo o período letivo, aluno e contrato no período letivo deverão ser informados, a matrícula no período letivo **não é obrigatório**.

Tipo de atendimento com fórmula preenchida

Quando o **tipo de atendimento** informado possuir uma fórmula, mas a matrícula no período letivo **não foi encontrada**, sendo ela baseada na **matriz aplicada do curso do aluno** ou do **contrato selecionado**, a **fórmula não será considerada para validação de geração de lançamento**. O sistema irá emitir uma mensagem de alerta para o usuário, mas **não irá impedir** o andamento do processo.

Passo 3

Neste passo os dados do atendimento obrigatórios deverão ser informados.

Configurar os parâmetros de consulta SQL

O sistema permite que seja possível configurar os parâmetros de consulta SQL

Parâmetros de Contexto do Educacional

O sistema permite uso de campos adicionais, que são os [parâmetros de tipos de atendimento](https://tdn.totvs.com/x/Zf1bGQ). Caso seja utilizado parâmetros baseados em sentença SQL, é suportado pelo TOTVS Educacional o uso de parâmetros de contexto nas sentenças SQL.

São eles: CODCOLIGADA, IDHABILITACAOFILIAL, IDPERLET ou RA, conforme sentença SQL no exemplo abaixo. 

 

Parâmetros Dependentes

O sistema permite o uso na sentença SQL, de parâmetros que dependem do valor de algum parâmetro de atendimento. Para tanto, o parâmetro de atendimento a ser referenciado precisa estar no padrão "PARAMETRO\_CODIGODOPARAMETRO", conforme exemplo abaixo:

 

Parâmetros de atendimento dependentes

Até o presente momento, o recurso de parâmetros de atendimento dependentes (baseados em consulta SQL) somente está disponível no TOTVS Educacional e no novo portal do aluno, através da criação de [requerimentos](https://tdn.totvs.com/x/Yu36E). 

Parâmentros de Variáveis Dinâmicas

O sistema permite utilizar os parâmentros de variáveis dinâmicas definida. Essas variáveis trazem dados de datas atuais ou dados sobre o contexto do sistema. Para mais informações [Variáveis dinâmicas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003987132-RM-Frame-Vari%C3%A1veis-din%C3%A2micas-).

São elas: $CODCOLIGADA, $CODTIPOCURSO, $CODFILIAL, conforme sentença SQL no exemplo abaixo.

Variáveis Dinâmica de Data

As variáveis dinâmicas de data não estão disponíveis neste contexto

Passo 4

Neste passo os dados da parcela a ser gerada para o contrato do aluno deverão ser informados.

Exibir este passo

Este passo será **exibido** se o serviço do educacional informado no tipo de atendimento selecionado.

Data de vencimento

A data de vencimento, pode ser definida de três formas:

* Vencimento definido para o Período Letivo, para atendimentos solicitados até a data cadastrada. Pode-se definir também a parcela que será gerada com o serviço extra para o aluno solicitante.
* Vencimento calculado automaticamente a partir da data de solicitação, com o número de dias indicados pelo usuário: o parâmetro 'Calcular automaticamente a data de vencimento da parcela' deve ser selecionado, e o número de dias deve ser preenchido abaixo.
* Para contratos de Vencimento Fixo, tal data pode ser preservada independente da definição escolhida – que continua a valer para os demais contratos: basta marcar o parâmetro 'Utilizar a data de vencimento de contratos com dia fixo'
Confirmar o processo

Ao confirmar o processo de solicitação do atendimento serão realizadas as seguintes validações:

* Será verificado o prazo do tipo de atendimento
* Será verificado se o parâmetro "Substituir todos os valores atuais pelos do modelo do tipo de atendimento" está selecionado dentro do tipo de atendimento, caso ele esteja selecionado será emitida uma mensagem de alerta informando que o mesmo está desmarcado e se caso prosseguir com o processo o local de entrega selecionado será utilizado na abertura da solicitação. Caso exista um modelo de atendimento associado a mensagem não será exibida e seguirá com as informações pertinentes ao modelo associado.
* Será verificado se o aluno está inadimplente, caso o parâmetro configuração do tipo de atendimento e o parâmetro do serviço estiver marcado.
* Validação feita pela fórmula se informada na configuração do tipo de atendimento.

Matrícula no período letivo

O contexto da fórmula será a matrícula no período letivo, baseado na matriz aplicada do curso do aluno ou do contrato. **Caso não encontrado**, será considerado a **criação normal do atendimento**.

Após todas essas validações feitas são chamadas as seguintes rotinas

* Criação de atendimento do RM Agilis.
* Inclusão de parcela – somente se o aluno possui algum contrato cadastrado
* Função de avançar o atendimento aberto para a primeira etapa
