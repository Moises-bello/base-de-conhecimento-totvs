---
content_hash: 4730a1ffc637c91895a920d4415915426e240a08a1f2538e7941ce43c306b09c
fetched_at: '2026-06-29T00:10:46.838198+00:00'
page_id: '556379167'
product: rm
source: tdn-rm
title: Formulários Dinâmicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556379167
version: 38
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré-requisitos**
3. **Pré-requisitos Formulário MultiProfissional**
4. **Compatibilidade de funcionalidades**
5. **Regras padrão**
6. **Exemplo de utilização**
7. **Informações de criação dos metadados no RM**
8. **Impressão**
9. **Rodapé e Assinatura Digital na Impressão**
10. **Utilização de Rótulos no Pep RM**

Formulários dinâmicosVisão Geral

## **01. VISÃO GERAL**

Possibilita ao usuário criar seus próprios formulários customizados dentro do prontuário do paciente utilizando a [funcionalidade de Metadados](https://tdn.totvs.com/pages/viewpage.action?pageId=556378814) do RM. A montagem do formulário é baseada nas [APIs de Metadados](https://tdn.totvs.com/display/LRM/API+Metadados), utilizando componentes do [PO-UI](https://po-ui.io/documentation/po-dynamic-form).

Pré-requisitos

## **02. PRÉ-REQUISITOS**

Para que um formulário possa ser utilizado dentro do prontuário do paciente, o mesmo deve possuir as seguintes colunas em sua tabela principal:

* CODCOLIGADA (INTEIRO)
* CODPROFISSIONAL (INTEIRO)
* STATUS (INTEIRO)
* CODPACIENTE (INTEIRO)
* CODATENDIMENTO (INTEIRO)
* CODIGOPROCESSO (INTEIRO) - **Usado em caso de assinatura digital**
* STATUSPROCESSO (STRING - TAMANHO 1) - **Usado em caso de assinatura digital**
Pré-requisitos Formulário MultiProfissional

## **03. PRÉ-REQUISITOS - FORMULÁRIO MULTIPROFISSIONAL**

Formulário multiprofissional é o tipo de formulário onde mais de um profissional tem a permissão para alterar ou cancelar o mesmo.

Para que um formulário seja caracterizado como multiprofissional ele deve possuir as seguintes colunas em sua tabela principal:

* MULTIPROFISSIONAL (INTEIRO)
* CODPROFISSIONALMULTI (INTEIRO)
* DATAMULTIPROFISSIONAL (DATETIME)

Coluna ID

Além das colunas informadas, existe um nome de coluna reservado para a chave primária: **ID (deverá ser do tipo INTEIRO e com numeração automática) ,** esta só deve ser utilizado para essa finalidade.   
**OBS:** A chave primária da tabela deve ser composta por **(CODCOLIGADA, ID).   
NÃO DEVE** ser utilizado de maneira alguma os campos **CODPACIENTE, CODATENDIMENTO**como chave composta, visto que a API de Metadados criará a coluna como uma concatenação da chave composta, gerando falhas nas funcionalidades relacionadas a formulário dinâmico.

Além disso, caso o usuário adicione a coluna **NOMEPROFISSIONAL**, que não é obrigatória, o sistema irá preencher automaticamente com o nome do profissional responsável pelo registro e exibirá o nome na listagem.

Caso o formulário não apresente as colunas obrigatórias, será exibida a seguinte mensagem de erro:

Compatibilidade de funcionalidades

## **04. COMPATIBILIDADE DE FUNCIONALIDADES**

Conforme informado na [documentação da funcionalidade](https://tdn.totvs.com/pages/viewpage.action?pageId=556378814), as seguintes funcionalidades estão indisponíveis no momento para formulários dinâmicos do PEP RM:

* Anexos e processos associados
* Campos do tipo "caixa de pesquisa"
* Rótulo
* Agrupador

Além disso, todos os tipos de controle com lista de opções (caixa de combinação, caixa de listagem e caixa de opção) seguiram a regra de acordo com o parâmetro "Utiliza caixa de opção em forma de lista?":

1. Parâmetro desabiitado:
2. Parâmetro habilitado:

Agrupador

Um formulário que contenha agrupador na sua construção do layout, quando utilizado nas versões atuais do PEPRM, será exibido de forma desconfigurada, sendo assim, é recomendado que os agrupadores customizados sejam removidos para evitar falhas na exibição do layout.

Caso seja um layout já existente, a orientação é que seja reiniciada a construção, voltando a configuração do layout para configuração padrão e refaça a construção do layout sem os agrupadores.

Evento OnValidate

As fórmulas visuais associadas aos eventos informados nos campos nos Metadados () estão disponíveis e funcionais no PEP RM a partir da versão 12.1.32.

Regras padrão 

## **05. REGRAS PADRÃO**

Os formulários criados dentro do prontuário do paciente seguirão as regras pré-definidas nos cadastros padrão e também conterão as mesmas funcionalidades.

São elas:

1. Apenas registros com o status de rascunho serão editáveis, **exceto para os formulários caracterizados como multiprofissional onde o registro finalizado pode ser alterado por um outro profissional.**
2. A edição apenas deve ocorrer pelo profissional que criou o registro, **exceto para os formulários caracterizados como multiprofissional onde o registro finalizado pode ser alterado por um outro profissional.**
3. Registros ainda em rascunho não são visíveis pelos usuários, exceto o responsável pelo registro.
4. Após ser finalizado, um registro não pode ser alterado, **exceto para os formulários caracterizados como multiprofissional onde o registro finalizado pode ser alterado por um outro profissional..**
5. Os rascunhos são salvos automaticamente na edição dos campos
6. É possível criar e gerenciar modelos de preenchimento formulários dinâmicos
7. São exibidos para o usuário apenas os formulários que ele possui permissão de acesso.
Exemplo de utilização

## **06. EXEMPLO DE UTILIZAÇÃO**

Seguem abaixo imagens com exemplos de um formulário customizado dentro do prontuário do paciente.

Seguem abaixo imagens com exemplos de um formulário customizado dentro do prontuário do paciente

**Formulários multiprofissional** possuem histórico das alterações. É possível consultar o histórico expandindo o item desejado conforme visualização abaixo.

É possível escolher quais colunas serão visíveis na tabela. Para isso a coluna tem que estar marcada como visível no momento da criação da tabela do formulário dinâmico.

Uma vez que a coluna já está exibida na visão da tabela pode-se escolher quais serão visualizadas clicando no botão

Colunas selecionadas ficaram visíveis para a visão de tabela.

## **6.1 Visualização do item do formulário dinâmico.**

Caso o formulário esteja configurado para ser **multiprofissional** será possível finalizar ou cancelar o mesmo por mais de um profissional.

Criação do formulário

A criação do formulário segue da mesma forma, conforme a [documentação](https://tdn.totvs.com/display/LRM/Metadados). Serão considerados formulários dinâmicos do PEP RM os formulários do [tipo API/PO-UI](https://tdn.totvs.com/pages/viewpage.action?pageId=556378814) criados dentro da estrutura de menus do PEP RM.

Informações de criação dos metadados no RM

## **07.** **INFORMAÇÕES DE CRIAÇÃO DOS METADADOS NO RM**

Conforme já mencionado, a documentação para criação dos metadados no RM está disponível [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=556378814). Abaixo seguem algumas informações adicionais para o cadastro para os Formulários Dinâmicos do PEP RM.

Exemplo de Utilização1º Passo:

Quando uma apresentação utilizar um modelo do tipo Web API/PO-UI, não será possível anexar Actions e Processos ao mesmo.

2º Passo:

Os campos adicionados no projeto (seja pela apresentação ou pelo modelo) não terão seus eventos de validação (OnValidate) considerados no uso do formulário pelo PEP RM.

3º Passo:

Ao utilizar projetos para Web API / PO-UI serão exibidos para seleção apenas os menus do tipo correspondente, sendo os menus de MDI Desktop indisponíveis para seleção.

4º Passo:

Atualmente o tipo de controle "Caixa de Pesquisa" não é suportado para Formulários Dinâmicos.

5º Passo:

      

É possível encontrar qualquer projeto gerado na barra de ferramentas "Executar" através tanto do código quanto do nome do formulário.

Impressão

## **08. IMPRESSÃO**

Para configurar um modelo de impressão para o formulário criado, basta criá-lo através do [RM Reports](https://tdn.totvs.com/display/LRM/RM+Reports) e [adicioná-lo ao formulário](https://tdn.totvs.com/pages/releaseview.action?pageId=450153593#:~:text=Para%20anexar%20o%20relat%C3%B3rio%20a,do%20relat%C3%B3rio%20a%20ser%20anexado.) como um anexo. O sistema identificará automaticamente o último relatório anexado ao formulário e executará a impressão. No entanto, para que tudo ocorra normalmente, o relatório deve receber parâmetros correspondentes em nome e tipo à chave primária da tabela do formulário. Caso exista assinatura digital configurada e parametrizada, será possível assinar os impressos gerados de formulários dinâmicos, para o correto funcionamento os campos **CODIGOPROCESSO** e **STATUSPROCESSO** devem existir obrigatoriamente.

Rodapé Assinatura Digital na Impressão

## **09**. **RODAPÉ E ASSINATURA DIGITAL NA IMPRESSÃO**

Para configurar o rodapé da impressão de registros assinados é preciso realizar as seguintes configurações no reports que foi anexado ao formulário dinâmico.

No relatório utilizado no formulário dinâmico criar uma expressão no rodapé do formulário.

Adicionar o parâmetro EXIBERODAPE para o funcionamento da assinatura

O rodapé da assinatura digital é composto pelos dados do NOMEPROFISSIONAL, CPF e a coluna RECMODIFIEDON da tabela criada para o formulário dinâmico.

Essas informações deverão ser incluídas na query para serem visualizadas corretamente no rodapé.

Após a criação das colunas necessárias editar a expressão criada no primeiro passo utilizando a instrução de exemplo abaixo.

Editar o SAUREL008101 pela query que está sendo utilizada no formulário em questão.

If(Relatório.EXIBERODAPE = 'T',  
Join(' ',   
Join(' ', 'Documento assinado digitalmente de acordo com a ICP-Brasil, MP 2.200-2/2001, Resolução CFM1821/2007, no sistema TOTVS PEP RM, por', Base.SAUREL008101.NOMEMEDICO),   
Join(' ', 'CPF',   
Join('', Base.SAUREL008101.CPF,   
Join(' ', ', às', Join('', Base.SAUREL008101.RECMODIFIEDON,'. Estado da assinatura: Válida.'))))), '')

O rodapé da assinatura digital será exibido mesmo na finalização de registros que não possuam rascunho prévio, desde que a unidade esteja com a assinatura digital ativa.

Utilização de Rótulos Pep RM 2502

## **10. UTILIZAÇÃO DE RÓTULOS PEP RM**

Essa funcionalidade permite a adição de **rótulos personalizados** em **formulários customizados** dentro do **Prontuário Eletrônico do Paciente (PEP)** no RM, por meio da interface de personalização do **DevExpress**.

**1.** No menu lateral de execução de actions, **digite o ID do projeto** que deseja configurar.

**2.** Após o carregamento do projeto, insira um **novo registro** ou **edite** um registro existente.

**3.** Na janela que será aberta, clique no primeiro ícone da barra de ferramentas, chamado Layout, para abrir a tela de **personalização**.

**4.** Na tela de **personalização**, alterne para a aba **Árvore de Organização**.

**5.** Na **Árvore de Organização**, selecione o componente que deseja rotular.

**6.** No painel de Propriedades, localize o campo **ControlText** e informe o rótulo que deve ser exibido no PEP RM.

**7.** Após salvar a configuração, abra o PEP RM, selecione um paciente, vá até o menu Formulários e selecione o formulário customizado editado. O rótulo será exibido acima do componente em que a configuração foi realizada.
