---
content_hash: fe3ffac09df15940f8fec70c9ce9804508a1495c687c6f62590e9b7ee2a3d77c
fetched_at: '2026-06-29T00:10:59.718734+00:00'
page_id: '615384329'
product: rm
source: tdn-rm
title: Evolução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615384329
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Complementos de Evolução**
4. **Histórico de evolução**
5. **Informações adicionais**
6. **Evolução por voz (V.2510)**
   1. **Visão Geral**
   2. **Acesso**
   3. **Observações**

EvoluçãoVisão Geral

## **01. VISÃO GERAL**

Recurso que possibilita ao usuário o registro de evoluções.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar o menu Evolução, será exibida a tela com o histórico de evoluções registradas para o paciente selecionado.

Na tela será possível visualizar, cadastrar e imprimir evoluções.

Para refinar a listagem, clique no botão Filtros, onde será possível filtrar as evoluções por período, grupo profissional e/ou prestador.

Além disso, é possível clicar em + Novo para registrar uma nova evolução e em Imprimir todos para imprimir as evoluções listadas.

Ao clicar no botão "novo", será aberta a tela para registro da evolução.

Neste momento é validado o conselho do profissional, onde é com essa informação que amarramos a evolução ao filtro na tela inicial do menu.

O usuário poderá realizar uma evolução a partir de um modelo já cadastrado, através da opção **“Mais ações > Usar modelo”**.

Ao clicar, o usuário poderá selecionar ou buscar um modelo específico, podendo ser **público** ou **privado**, onde:

* **Público**: modelos cadastrados pelo próprio usuário ou por outros usuários.
* **Privado**: modelos cadastrados apenas pelo próprio usuário.

Os modelos podem ser cadastrados na própria tela de registro de evolução. Após realizar a digitação da evolução, o usuário poderá acessar **“Mais ações > Salvar modelo”**.

Ao selecionar esta opção, será aberta uma janela para preenchimento das informações do modelo, onde o usuário deverá informar:

* **Nome do modelo**
* **Unidade de atendimento**

Além disso, o usuário poderá habilitar a opção **“Salvar modelo como público”**, tornando o modelo disponível para outros usuários.

Após preencher os dados, basta clicar em **“Salvar”** para concluir o cadastro ou em **“Cancelar”** para retornar à tela de evolução sem salvar o modelo.

O usuário terá a disposição funcionalidade de um editor de texto. Poderá também realizar a marcação de uma tag, informando a situação do paciente no momento da evolução.

Durante o preenchimento, o sistema realiza salvamento automático (auto save) da evolução. Caso o usuário não finalize o registro, a evolução ficará salva como rascunho no histórico do paciente.

Caso o usuário opte por não registrar a evolução, a exclusão poderá ser realizada apenas pela tela inicial do menu Evolução, através da listagem de evoluções do paciente.

Após preenchimento, basta clicar no botão de finalizar ou finalizar e imprimir. Caso a unidade utilize a certificação digital, neste momento a mesma será solicitada.

Complementos de Evolução 

## **03. COMPLEMENTOS DE EVOLUÇÃO**

Especialistas podem informar complementos na evolução de acordo com sua especialidade.

##### **Como criar um complemento de evolução**

Acesse o sistema RM e em Cadastros/Campos complementares, selecione a especialidade desejada.

Clique em novo e preencha as informações do novo complemento (NOME DA COLUNA, DESCRIÇÃO, TIPO DO CAMPO E ORDEM).

*Observação: cada especialidade possui sua tabela de complementos, e cada complemento corresponde a uma nova coluna nessa tabela.*

Já no sistema PEP, os campos complementares estarão disponíveis para preenchimento do profissional.

Histórico de evolução 

## **04. HISTÓRICOS DE EVOLUÇÃO**

Janela flutuante que dá, ao especialista, a opção de visualizar/copiar a descrição de uma evolução anterior.

Ao clicar em "Histórico de evoluções" é aberta uma janela flutuante.

Nela fica disposta uma caixa de seleção contento todas as evoluções finalizadas do paciente em questão. A janela permite ser redimensionada e arrastada para qualquer lugar dentro da tela.

Ao selecionar uma evolução, basta clicar no botão ao lado da caixa de seleção para copiar sua descrição e então colar na evolução sendo criada.

Informações adicionais

## **05. INFORMAÇÕES ADICIONAIS**

Foi criado um parâmetro, via banco de dados, para definir se a exibição da timeline da evolução e receita será por atendimento ou geral:

UPDATE SZPARAM SET TEXTO = 'F' WHERE IDPARAM = 976 AND CODCOLIGADA = NUMEROCOLIGADA .

Caso não possua o parâmetro na base do cliente, necessário criar através do insert: INSERT INTO SZPARAM VALUES (1, 976, 'F', NULL, NULL, NULL, NULL, NULL, NULL, NULL, null )

Evolução por voz (V.2510)

## **06. EVOLUÇÃO POR VOZ**

##### **Funcionalidade disponível a partir da versão 12.1.2510.**

## **a.****VISÃO GERAL**

O DTA permite preencher o formulário de evolução por comandos de voz, convertendo a fala em texto automaticamente.

## **b.****ACESSO**

* Abra o formulário de evolução.
* Clique em **Mais Ações → Carregar Evolução por Voz**.
* Fale as informações e confirme o preenchimento.

## **c.** **OBSERVAÇÕES**

* Ative o microfone e permita o uso no navegador para que o DTA possa monitorar a fala.
