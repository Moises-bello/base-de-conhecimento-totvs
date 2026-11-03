---
content_hash: 201f1f9a9f92e086f30e7a332f6bb4970d0222a532111c52e03c5ac27e38f42c
fetched_at: '2026-06-29T00:10:30.073566+00:00'
page_id: '519190471'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Código Fonte" (conSourceCodeActivity)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519190471
version: 20
---

# Índice:

---

* Objetivo:

* Especificação:

# Objetivo:

---

          Esse documento possui a finalidade de exemplificar a utilização da atividade de fórmula visual **Executar Código Fonte** para personalizar a execução de processos. Utilizaremos o processo de cópia de perfis neste exemplo.

         Para maiores detalhes da criação e acesso a fórmulas visuais, acesse a documentação

# Especificação:

---

     A atividade “Executar Código Fonte” é uma atividade que permite que um código (que varia de Levantar uma Exceção à

falseExemploFVExemploFVPasso 01

Crie uma nova fórmula visual e edite a mesma. A esquerda, clique na aba Atividades e arraste a atividade de Executar Código Fonte para o fluxo de trabalho da fórmula.

Depois de arrastar a atividade para o fluxo, clique com o botão direito do mouse e acesse a opção “Selecionar código fonte”.

ExemploFVPasso 02

Inclua um novo registro, preencha o campo Nome do código fonte e posteriormente clique no botão Editor C#

Na janela aberta é disponibilizado um NameSpace com uma classe pré criada para personalizarmos a execução do nosso processo. Nessa janela possuímos recursos para executar o Build do código fonte e adicionar referências necessárias para a nossa classe entre outros.

Como vamos personalizar um processo, utilizaremos o método CustomProcess

ExemploFVPasso 03

Para manipular a classe de parâmetros do processo de cópia de perfis, é necessário referenciar a dll que contém a definição da mesma, para isso, acessamos o Project Explorer (no canto direito da janela), selecionamos o item References, clicamos com o botão direito e selecionamos a opção Add Reference...

Na janela aberta, selecionamos a aba Browse, e clicamos no botão Browse

ExemploFVPasso 04

Para acessar as propriedades da classe de parâmetros do processo, é necessário realizar um CAST do objeto genérico processParams.ParamsProc para o tipo da classe de parâmetros do processo que escolhemos (RM.Glb.Processos.GlbParamsProcCopyPerfil). Observe que após realizar o cast, as propriedades da classe de parâmetros do nosso processo estarão disponíveis através do intelisense da atividade.

A partir daí, podemos manipular as informações da forma como desejarmos, e nesse exemplo utilizamos o recurso para:

* Forçar a criação de um novo perfil;
* Não permitir a substituição de registros existentes
* Verificar se todos os campos foram preenchidos e lançar exceções caso contrário
* Adicionar a string “\*\*Cópia\*\* ” na identificação do perfil resultante do processo de cópia

***Método ficou assim:***

c#EclipseExemploFVPasso 05

A todo momento podemos testar se o código digitado possui erros clicando no botão **Build**. Clique no botão OK na janela de edição de código fonte. Clique no botão OK na janela de Cadastro de códigos fontes. Clique novamente em OK com o código recém cadastrado selecionado.

Posteriormente, para editar o código fonte associado a atividade clique no botão da propriedade Id. Código fonte.

Salve a fórmula visual. Na visão de fórmulas visuais, selecione a fórmula recém-criada e clique sobre o botão editar da visão. Selecione a aba Gatilhos. Em processos, selecione a opção “Antes da Execução” e clique no botão de adicionar gatilhos. Na tela aberta pesquise por GlbProcCopyPerfil e clique sobre o processo de cópia de perfis. Clique em OK para salvar as alterações.

ExemploFVPasso 06

Para testar a fórmula visual, acesse a visão de Perfis, selecione um registro, clique em processos, Copiar Perfil.

Selecionamos as opções “Novo Perfil” e “Substituir Perfis” e preenchemos os dados solicitados. Observando que, o comportamento definido foi para que não seja substituído nenhum perfil, apenas a criação de um novo como uma cópia do registro selecionado na visão.

Depois de clicar em executar, uma das exceções definidas no código fonte foi lançada.

Se repetirmos a execução preenchendo os mesmos dados e desmarcando a opção de Substituir Perfis, o processo será executado com sucesso e na visão, podemos observar que o valor da coluna Identificação na grid foi alterado conforme definido no código fonte criado.

# Parâmetro da Atividade:

---

     Na atividade de "Executar Código Fonte (conSourceCodeActivity1)" existe a opção de criar parâmetros.

A utilização do parâmetro é utilizada quando é necessário a chamada de outra outra atividade dentro da fórmula visual.  
Como exemplo, acrescente a atividade de "**Exceção**" no fluxo sequencial e aponte o parâmetro criado na atividade "**Executar Código Fonte**" para a atividade de "**Exceção**", exemplo demonstrativo abaixo:

Verifique que quando executada a fórmula visual a exceção é levantada.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.24 ou Superior

false

**Processo:** Atividade "Executar Código Fonte" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:** 21/10/2019

false

**Autores:**

false
