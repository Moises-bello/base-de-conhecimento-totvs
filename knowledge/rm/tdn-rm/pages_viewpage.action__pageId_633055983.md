---
content_hash: 54dd198d5391a7c896ebcc5befb12c8ea031219e1844de4c475b56ae4be9e111
fetched_at: '2026-06-29T00:11:06.263821+00:00'
page_id: '633055983'
product: rm
source: tdn-rm
title: BPA (Boletim de Procedimento Ambulatorial)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633055983
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Faturamento BPA**
4. **Refaturamento BPA**
5. **Reprocessamento BPA**
6. **Tabelas utilizadas**

## **01. VISÃO GERAL**

BPA (Boletim de Procedimento Ambulatorial) para paciente externo.

Unificação de CNS/CPF

A partir de outubro de 2025, com a unificação CNS/CPF, o CPF passa a ser o identificador prioritário do cidadão nos atendimentos do SUS, enquanto o Cadastro Nacional de Saúde (CNS) permanece como identificador secundário.

## **02. EXEMPLO DE UTILIZAÇÃO**

Uma vez selecionada a opção de BPA, o sistema fará a busca das contas de pacientes externos de acordo com os filtros informado.

Para a geração da fatura de BPA, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa

### **Parâmetro "Habilita BPA no Registro de Atendimento externo"**

O parâmetro se encontra em Registro e Controle, como é mostrado na imagem abaixo:

Caso este parâmetro esteja marcado, contas com atendimento, em que o tipo paciente é igual a Interno serão trazidos no grid, como é mostrado abaixo:

Caso contrário, não ser trago os pacientes Internos:

## **03. FATURAMENTO BPA**

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento BPA. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo. Um exemplo abaixo é mostrado:

## **04. REFATURAMENTO BPA**

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento BPA já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo.

## **05. REPROCESSAMENTO BPA**

Para selecionar a opção de reprocessamento com BPA, devemos acessar os seguintes passos:

Acessar Faturamento -> Fatura SUS

Selecionar uma conta e acessar o menu: Processos → Faturamento AIH, BPA, APAC.

Escolher a opção “Reprocessamento” e “BPA”

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Nesse processo será recalculado o valor total da fatura e a quantidade de contas que a mesma possui,

Observação: Caso a quantidade de contas não seja maior que 1 a remessa então será cancelada.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Auditoria)
* Retornar Conta para Correção(Faturamento)

As duas opções acima para o SUS (BPA) tem o mesmo comportamento.

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Auditoria)" ou "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo as contas foram liberadas.

## **06. TABELAS UTILIZADAS**

* SZSUSBPALANC
* SZSUSBPAPROD
* SZSUSBPAPRODHIST
