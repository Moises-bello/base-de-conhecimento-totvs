---
content_hash: 1519cffc8c54c63b6890cf5c273a431529240821eb6843f73273d1cf769845c3
fetched_at: '2026-06-28T21:35:19.183432+00:00'
page_id: '198938892'
product: fluig
source: tdn-fluig
title: Personalização da tela inicial do My Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198938892
version: 10
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar o passo a passo necessário para personalizar a tela inicial do My Fluig.

# Configurando tela inicial do My Fluig

---

Para maior personalização do aplicativo Fluig, é possível configurar a tela inicial do aplicativo. Para realizar esta alteração realize os seguintes passos:

**01.** Efetue a autenticação no Fluig Plataforma utilizando o usuário **wcmadmin**, e então acesse **Painel de Controle  ► WCM ► Empresas**.

**02.** Selecione a empresa que deseja alterar a tela inicial do aplicativo e então clique em **Editar**.

**03.** A tela de edição de empresa será apresentada. Clique no botão **Cadastrar dados adicionais**.

**04.** A tela de dados adicionais da empresa será apresentada. No campo **Chave**informe o valor **startScreen**e no campo **Valor**informe:

* PROCESS:  Se você deseja que a tela inicial seja a inicialização de processos.
* SOCIAL: Se você deseja que a tela inicial  seja a timeline.
* DOCUMENT: Se você deseja que a tela inicial  seja a navegação de documentos.
* HOMEAPP: Define que a home do aplicativo será exibida como tela inicial.
* TASKS: Se você deseja que a tela inicial  seja a central de tarefas.
* COMMUNITY:ALIAS\_DA\_COMUNIDADE : Se você deseja que a tela inicial seja uma comunidade, o parâmetro ALIAS\_DA\_COMUNIDADE deve ser preenchido e válido para direcionar para comunidade correta.
* PAGE:IDENTIFICADOR\_UNICO : Se você deseja que a tela inicial seja uma página, o parâmetro IDENTIFICADOR\_UNICO deve ser preenchido e válido para direcionar para página correta.

**05.** Clique no botão **Salvar** para salvar os dados adicionais. O item **startScreen**será adicionado na listagem de dados adicionais da empresa

**06.** Clique no botão **Salvar** para salvar as alterações na empresa e efetivar a alteração da tela inicial do aplicativo.

Quando funciona?

A alteração terá efeito após a segunda utilização do aplicativo ou ao cadastrar a empresa novamente.

Quero voltar ao que era antes

1. A home padrão do aplicativo será definida nos casos onde o parâmetro starscreen não esteja configurado e a página home da plataforma Fluig não possua widgets com visualização suportada no mobile ativada.
2. Para que a home da plataforma seja definida como tela inicial, basta remover o parâmetro startScreen e adicionar a visualização no mobile em pelo menos uma widget que contém essa opção.
3. Caso deseje voltar a utilizar outras páginas como home no aplicativo, basta passar alguns dos parâmetros informados no **passo 04** do item **Configurar tela inicial do My Fluig**.
