---
content_hash: 65b77701e7ce4abcd63afabc9f3acea59e6d5e27b81f7183eb03b94fc806af1f
fetched_at: '2026-06-28T21:35:28.623166+00:00'
page_id: '662892312'
product: fluig
source: tdn-fluig
title: FormController - a varíavel "form"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=662892312
version: 5
---

# Índice

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é descrever os métodos do FormController para ajuda-lo a entender melhor o desenvolvimento de eventos de formulário.

# Pré-requisitos

---

Antes de iniciar, é importante que leia a documentação sobre  e que tenha começado com os .

# FormController

---

O **formController** é o objeto que realiza a comunicação entre o formulário e a customização dos eventos. Esse objeto está disponível em cada um dos **eventos de customização** de formulários através da variável ***form***recebida via parâmetro do evento.

Este objeto permite alterar os valores dos campos de um registro de formulário e também obter o estado de edição deles, por exemplo: se o usuário está visualizando ou editando o registro de formulário.

Veja a seguir os métodos disponíveis para a variável ***form***:

| Método | Descrição |
| --- | --- |
| long getCompanyId() | Retorna o ID da empresa |
| int getDocumentId() | Retorna o ID do documento (registro de formulário) |
| int getVersion() | Retorna a versão do documento (registro de formulário) |
| int getCardIndex() | Retorna o ID do formulário |
| String getValue(String fieldName) | Obtém o valor de um campo do formulário  O campo fieldName é *case insensitive*, ou seja, você pode usar "codigo", "Codigo", "CoDiGo", "CODIGO" |
| void setValue(String fieldName, String fieldValue) | Define o valor de um campo do formulário  O campo fieldName é *case insensitive*, ou seja, você pode usar "codigo", "Codigo", "CoDiGo", "CODIGO" |
| boolean getEnabled(String fieldName) | Verifica se um campo está habilitado |
| void setEnabled(String fieldName, boolean enabled) | Define se um campo deve estar habilitado ou não |
| void setEnabled(String fieldName, boolean enabled, boolean protect) | Define se um campo deve estar habilitado ou não, e se o campo desabilitado deve ser protegido ou não.  Quando definido o valor *true* para o parâmetro protect, o campo desabilitado não terá seu valor salvo no registro de formulário.  A função de proteção dos dados do formulário só é válida no contexto de uma movimentação workflow. |
| void setEnhancedSecurityHiddenInputs(boolean protect) | Quando definido com o valor *true*, todos os campos desabilitados pelo método setEnabled após a ativação deste método serão protegidos\* e não terão seus valores salvos no registro de formulário.  Esta função deve ser chamada antes do setEnabled.  A função de proteção dos dados do formulário só é válida no contexto de uma movimentação workflow. |
| String getFormMode() | Obtém o modo de edição do formulário, podendo retornar os seguintes valores: ADD: Criação do formulário  MOD: Formulário em edição  VIEW: Visualização do formulário  NONE: Não há comunicação com o formulário, por exemplo, ocorre no momento da validação dos campos do formulário onde este não está sendo apresentado. |
| void setHidePrintLink(boolean hide) | Quando definido com o valor *true*, oculta o botão de imprimir do formulário. |
| boolean isHidePrintLink() | Verifica se o botão de imprimir está ocultado. |
| void setHideDeleteButton(boolean hide) | Quando definido com o valor *true*, oculta o botão de excluir os registros filhos de todas as tabelas de pai-filho de um formulário. |
| void setHideDeleteButton(String tableName, boolean hide) | Quando definido com o valor *true*, oculta o botão de excluir registros filhos em um formulário com pai-filho. É necessário informar o ID do pai-filho. |
| boolean isHideDeleteButton() | Verifica se o botão de exclusão de registros filhos está ocultado. |
| boolean isHideDeleteButton(String tableName) | Verifica se o botão de exclusão de registros filhos está ocultado. É necessário informar o ID do pai-filho. |
| void setHideAddButton(boolean hide) | Quando definido com o valor *true*, oculta o botão de adicionar os registros filhos de todas as tabelas de pai-filho de um formulário. |
| void setHideAddButton(String tableName, boolean hide) | Quando definido com o valor *true*, oculta o botão de adicionar registros filhos em um formulário com pai-filho. É necessário informar o ID do pai-filho. |
| boolean isHideAddButton(String tableName) | Verifica se o botão de adicionar de registros filhos está ocultado. É necessário informar o ID do pai-filho. |
| boolean isHideAddButton() | Verifica se o botão de adicionar de registros filhos está ocultado. |
| boolean getMobile() | Verifica se o registro de formulário está sendo acessado através de um dispositivo *mobile*. |
| boolean isVisible(String fieldName) | Verifica se um campo está marcado para ser visível pelo nome do campo |
| void setVisible(String fieldName, boolean visible) | Define se um campo deve estar visível ou não pelo nome do campo |
| boolean isVisibleById(String id) | Verifica se um item do html está marcado para ser visível |
| void setVisibleById(String id, boolean enabled) | Define se um item do html deve estar visível ou não |
| Map<String, String> getChildrenFromTable(String tableName) | Retorna um mapa contendo os nomes e valores dos campos filhos de uma tabela pai. |
| Integer[] getChildrenIndexes(String tableName) | Retorna um array contendo os índices que contenham campos filhos na tabela pai |

# Exemplos de utilização

---

jsQuando não for uma inclusão, bloqueia o campo codigotruejsAo adicionar um registro, torna o campo código invisíveltruejsCom validar campos, conferir e atribuir valorestrue

 

jsExemplo de como listar todos os registros de uma tabela pai x filho e usar para validaçãotruejsExemplo de como manipular os campos de uma tabela pai x filhotrue
