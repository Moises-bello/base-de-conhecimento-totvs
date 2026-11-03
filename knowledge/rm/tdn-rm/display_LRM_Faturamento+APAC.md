---
content_hash: e3a950a8b51d2b683202243c4d6362e1e1b7c28b894711c9e5a49d9a1c532977
fetched_at: '2026-06-29T00:11:06.271152+00:00'
page_id: '633056175'
product: rm
source: tdn-rm
title: Faturamento APAC
type: documentation
url: https://tdn.totvs.com/display/LRM/Faturamento+APAC
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Faturamento APAC**
4. **Refaturamento APAC**
5. **Reprocessamento APAC**
6. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Esse documento tem como objetivo explicar qual o fluxo de funcionamento do Faturamento SUS dos atendimentos APAC (Autorização de Procedimentos de Alta Complexidade).

Unificação de CNS/CPF

A partir de outubro de 2025, com a unificação CNS/CPF, o CPF passa a ser o identificador prioritário do cidadão nos atendimentos do SUS, enquanto o Cadastro Nacional de Saúde (CNS) permanece como identificador secundário.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Uma vez selecionada a opção de APAC, o sistema fará a busca das contas de pacientes externos de acordo com os filtros informado.

Para a geração da fatura de APAC, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa
Faturamento APAC

## **03. FATURAMENTO APAC**

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento APAC. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta definida no parâmetero Diretório de Armazenamento do Arquivo.

Refaturamento APAC

## **04. REFATURAMENTO APAC**

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento APAC já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo é gerado na pasta definida no parâmetero Diretório de Armazenamento do Arquivo.

Reprocessamento APAC

## **05. REPROCESSAMENTO  APAC**

Para selecionar a opção de reprocessamento com APAC, devemos acessar os seguintes passos:

Acessar Faturamento -> Fatura SUS

Selecionar uma conta e acessar o menu: Processos → Faturamento AIH, BPA, APAC.

Escolher a opção “Reprocessamento” e “APAC”

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Nesse processo será recalculado o valor total da fatura e a quantidade de contas que a mesma possui.

**Observação:** Caso a remessa só possua uma conta ao remover essa conta da fatura, a mesma deve ser cancelada caso exista uma outra remessa em aberta. Caso não tenha nenhuma remessa em aberta, a remessa que teve a conta removida deve ter seu status modificado para em aberto e a quantidade de contas e valor total de ser zerado.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Faturamento)

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo as contas foram liberadas, neste processo não deve remover as contas da remessa e o valor da remessa deve manter o mesmo.

Tabelas Utilizadas

## **06.****TABELAS UTILIZADAS**

* SZSUSAPAC
* SZAPACPROC
* SZAPACMED
* SZAPACNEFRO
* SZAPACNEFROFISTULA
* SZAPACNEFROACOMPDRC
* SZAPACRADIO
* SZAPACQUIMIO
* SZAPACQUIMIO
* SZAPACPOSBARI
* SZAPACPREBARI
* SZAPACBARI
* SZAPACLAUDO
