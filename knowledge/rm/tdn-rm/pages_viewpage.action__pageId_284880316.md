---
content_hash: a2b159dfe782c7a6356fceea061a4ed412760349c3959f13ea9e24fc46b31711
fetched_at: '2026-06-29T00:08:37.659019+00:00'
page_id: '284880316'
product: rm
source: tdn-rm
title: Relatórios.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880316
version: 20
---

Nesta tela, o aluno pode visualizar e emitir os relatórios que estiverem disponíveis para seu perfil.

## **01. PERMISSÃO**

Para acessar a funcionalidade, o perfil do aluno deverá ter a permissão em:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Relatórios | Emitir relatórios.**

## **02. LISTA DE RELATÓRIOS DISPONÍVEIS**

O portal irá listar os relatórios disponíveis considerando a seguinte regra: Serão exibidos os relatórios marcados na parametrização "**Relatórios disponibilizados para alunos (Tipos: SECRETARIA, TESOURARIA, ALUNOS)**", disponível em: **Parâmetros | RM Portal | RM Portal - Gerais | Portal - Relatórios 1/2**.

Tipos de relatórios disponíveis

Os tipos de relatórios disponíveis para parametrização devem seguir os seguintes tipos: **Secretaria, Aluno e Tesouraria**.

Relatórios de Tesouraria

Para visualizar relatórios do tipo **Tesouraria**, o usuário logado no Portal do Aluno precisa ter a **permissão de acesso a dados financeiros**, configurada na tela **Contrato**, na aba **“Acesso dados Contrato”**.

Tabela master

Selecione os relatórios que possuam a **tabela master correta** de acordo com o tipo do relatório, pois é assim que o Portal do Aluno aplicará os filtros para a execução.

**Tabela master por tipo de relatório:**

* **Tipo Secretaria:** Campos-chave da tabela `SMATRICPL` → `CODCOLIGADA`, `IDPERLET`, `IDHABILITACAOFILIAL`, `RA`
* **Tipo Aluno:** Campos-chave da tabela `SALUNO` → `CODCOLIGADA`, `RA`
* **Tipo Tesouraria:** Campos-chave da tabela `SCONTRATO` → `CODCOLIGADA`, `RA`, `IDPERLET`, `CODCONTRATO`

## 

## **03. LISTA DE RELATÓRIOS DISPONÍVEIS PARA OUTRAS TELAS DO PORTAL**

O Portal listará os relatórios disponíveis seguindo a seguinte regra: Somente serão exibidos os relatórios cadastrados na parametrização **“Relatórios do aluno”**, acessível em:  
**Parâmetros | RM Portal | RM Portal - Gerais | Portal - Relatórios 2/2**.

O aluno poderá visualizar, no Portal, todos os relatórios parametrizados anteriormente, incluindo: **Quadro de Horário, Consulta de Ocorrências, Consulta de Notas, Consulta de Faltas, Grade Curricular, Financeiro** e **Calendário**, com a opção de **‘Imprimir’** disponível na tela.

Tela de solicitações/requerimentos

O relatório de **Solicitações/Requerimentos** é exibido no menu **Requerimentos**, na aba **Solicitados**. No combo de opções **“Outras Ações”**, está disponível a opção de **Download**.

Parâmetros para o relatório

Na execução dos relatórios, serão passados **parâmetros com informações do contexto selecionado pelo aluno**. Para que esses dados sejam utilizados corretamente, crie os seguintes parâmetros nos relatórios:

* **CODCOLIGADAPARAM:** Código da coligada
* **CODFILIALPARAM:** Código da filial
* **CODTIPOCURSOPARAM:** Código do nível de ensino
* **IDPERLETPARAM:** Identificador do período letivo selecionado
* **IDHABILITACAOFILIALPARAM:** Identificador da habilitação filial
* **RAPARAM:** Registro acadêmico do aluno

Tela de solicitações/requerimentos

O relatório **Solicitação/Requerimento** utiliza parâmetros específicos. São eles:

* **CODCOLIGADAPARAM:** Código da coligada
* **CODATENDIMENTOPARAM:** Código do atendimento
* **CODLOCALPARAM:** Código do local

**Exemplo na tela de “Quadro de Horário”:**

*(A seguir, seriam exibidos detalhes ou uma imagem ilustrativa mostrando como o quadro de horário aparece para o aluno, incluindo botões como “Imprimir”, filtros aplicáveis e informações de cada período/disciplinas.)*
