---
content_hash: d7efcb87634ad55249c585a195abffa92d31ac7880863546dbf1116b80e6f466
fetched_at: '2026-06-29T00:10:57.923184+00:00'
page_id: '600805697'
product: rm
source: tdn-rm
title: Prescrição de Enfermagem PEP RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600805697
version: 35
---

1. **Visão Geral**
2. **Criar nova prescrição**
3. **Adicionar Diagnóstico**
4. **Liberar prescrição**
5. **Status da prescrição**
6. **Automatização com Diagnóstico de Enfermagem**

falsepaineltrueVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que permite aos usuários a possibilidade de prescrever itens da SAE para os pacientes.

Criar nova prescrição

## **02. CRIAR NOVA PRESCRIÇÃO**

Para criar uma nova prescrição, deve-se utilizar o botão "Criar Prescrição", localizado na página acessada a partir da Prescrição de Enfermagem.

Após o processamento, é exibida uma mensagem sinalizando a criação da nova prescrição com sucesso.

A partir de uma prescrição com status **Vencida**, é possível criar uma nova prescrição por meio de uma cópia.  
Para realizar essa ação, basta clicar no botão “Copiar Prescrição” na tela.  
Dessa forma, todos os itens da prescrição original serão copiados para uma nova prescrição, que será criada com o status **Rascunho**.

A vigência da prescrição irá depender da quantidade de dias que a mesma ficará valida, a ser definido no parâmetro geral, conforme imagem abaixo.

Porém pode ser configurado por unidade via RM Saúde. Caso configurado por unidade substituirá o parâmetro geral.

Adicionar diagnóstico

## **03. ADICIONAR DIAGNÓSTICO**

Para criar um novo item de prescrição, basta o usuário realizar a busca pelo diagnóstico desejado pelo campo de busca ou clicar no botão "Adicionar item". 

Ao efetuar a busca, a tela para adicionar o item já será aberta com o padrão de diagnóstico selecionado. Basta o usuário buscar o diagnóstico que faz parte do padrão selecionado e posteriormente o cuidado. 

Ao buscar os cuidados, o usuário poderá adicionar até quatro itens por vez. Os itens marcados de cor branca, significa que os campos obrigatórios já foram preenchidos. Os campos de cor cinza, significa que ainda estão pendentes o preenchimento dos campos obrigatórios.

É possível remover os itens da pré-lista, basta clicar no ícone "x" ao final de cada tag.

Após o preenchimento de cada item é necessário clicar no botão de salvar alterações, individualmente. Após isso, o item ficará em conformidade para ser inserido na prescrição.

Após clicar no botão para incluir os itens à prescrição, os itens serão listados na tela principal, onde cada submenu corresponderá a um padrão de diagnóstico. A quantidade de cuidados serão totalizados ao lado de cada titulo do submenu.

É possível realizar o pré-aprazamento do item adicionado. Basta selecionar o checbox e serão habilitados os horários. Os horários aqui definidos, serão os horários que serão refletidos na parte de aprazamento do PLT, para o usuário apenas liberar o mesmo.

Essa opção pode vir selecionada como default ao inserir os cuidados. Deve ser parametrizada no cadastro de [Unidade de Atendimento](https://tdn.totvs.com/display/LRM/Unidade+de+Atendimento).

## **Edição de item de prescrição de enfermagem**

Para editar um item basta clicar em um dos itens adicionados

Em seguida o seguinte modal será mostrado:

Caso o usuário clique em Excluir um modal de confirmação é mostrado

Além disso o usuário pode cancelar a ação de atualizar. Sendo assim, o mesmo voltará para a página anterior.

Ao clicar no botão atualizar o usuário confirma a atualização

LiberarLiberar prescrição de enfermagem

## **04. LIBERAR**

A rotina de liberar consiste em validar as informações cadastradas e consolidar alterando os itens para o status de "Liberado".

Para liberar a prescrição é necessário haver pelo menos 1(um) item cadastrado.

E o item é liberado com sucesso.

Após liberar, a prescrição é atualizada e a informação da validade é adicionada.

Ao liberar a prescrição, é gerada a impressão.

Ao liberar a prescrição, deverão ser enviadas as solicitações de materiais para a farmácia.

Status da prescrição

## **05. STATUS DA PRESCRIÇÃO**

O cabeçalho da prescrição de enfermagem exibirá o status da prescrição, sendo eles:

**RASCUNHO**: a prescrição está pendente de liberação.  
**VIGENTE**: a data atual está entre a data de início e término da prescrição.  
**VÁLIDA**: a data atual ainda não ultrapassou a data de término da prescrição.  
**VENCIDA**: a data atual é posterior a data de término da prescrição.

Além da tag de identificação do status da prescrição, também é exibido a vigência da prescrição.

Automatização com Diagnóstico de Enfermagem

## **06. PREENCHIMENTO AUTOMÁTICO DO PADRÃO DE DIAGNÓSTICO DE ENFERMAGEM**

##### **Funcionalidade disponível a partir da versão 12.1.2510.**

A partir desta atualização, o sistema passa a contar com um novo modelo automatizado que permite o preenchimento automático da Prescrição de Enfermagem com base nos padrões de diagnóstico finalizados na rotina de Diagnóstico de Enfermagem.

O objetivo é agilizar o processo de prescrição, reduzir o retrabalho e garantir maior padronização entre o diagnóstico e os cuidados prescritos.

A automação é opcional e depende da configuração do parâmetro:

**Caminho:**  
`Ambiente → Parâmetros → Gestão Hospitalar → Prontuário Eletrônico`

**Parâmetro:**  
`Utilizar modelo automatizado de diagnóstico de enfermagem na prescrição`

**Opções disponíveis:**

* **Sim** → Ativa o modelo automatizado.  
  Ao finalizar um padrão de diagnóstico, as **intervenções (cuidados)** associadas serão carregadas automaticamente na prescrição.
* **Não** → Mantém o funcionamento atual, com **preenchimento manual** da prescrição.
* O parâmetro deve ser configurado apenas por perfis autorizados e a mudança afeta apenas novas prescrições criadas após a alteração.

Quando o parâmetro estiver habilitado e o enfermeiro finalizar um padrão de diagnóstico na rotina de Diagnóstico de Enfermagem:

* A Prescrição de Enfermagem será automaticamente preenchida com os diagnósticos finalizados e suas intervenções associadas.
* Apenas diagnósticos vinculados a padrões (como os padrões NANDA) serão considerados, pois diagnósticos avulsos não possuem intervenções cadastradas e não são carregados automaticamente.
* O profissional pode editar, adicionar ou remover intervenções livremente, sem alterar o diagnóstico original.
* A automação não ocorre se o diagnóstico estiver em andamento ou não finalizado.

Pontos de Atenção

* A automação só ocorre para padrões de diagnóstico finalizados e com intervenções cadastradas.
* Diagnósticos criados de forma avulsa ou sem padrão cadastrado não participam do preenchimento automático.
* A funcionalidade é compatível apenas com o padrão NANDA.
* Clientes que ainda utilizam o modelo legado continuam com o funcionamento atual, sem impacto nos dados anteriores.
* O rastreamento entre diagnóstico e prescrição é mantido para auditoria e controle de conformidade.
