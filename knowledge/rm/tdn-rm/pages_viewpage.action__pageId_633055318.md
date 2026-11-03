---
content_hash: 81d5c8e9aacc2133f82bbe5c97858bade8810bfedc32aa687dbda5778a6ef3f6
fetched_at: '2026-06-29T00:11:06.257091+00:00'
page_id: '633055318'
product: rm
source: tdn-rm
title: AIH (Autorização de Internação Hospitalar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=633055318
version: 12
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Faturamento AIH**
4. **Refaturamento AIH**
5. **Reprocessamento AIH**
6. **Tabelas utilizadas**

## **01. VISÃO GERAL**

AIH (Autorização de Internação Hospitalar) para paciente interno.

Unificação de CNS/CPF

A partir de outubro de 2025, com a unificação CNS/CPF, o CPF passa a ser o identificador prioritário do cidadão nos atendimentos do SUS, enquanto o Cadastro Nacional de Saúde (CNS) permanece como identificador secundário.

## **02. EXEMPLO DE UTILIZAÇÃO**

Uma vez selecionada a opção de AIH, o sistema fará a busca das contas de acordo com os filtros informado.

Para a geração da fatura de AIH, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa
* Se o percentual de cesáreas em relação aos partos normais, é menor ou igual ao parâmetro permitido (Parâmetros Sus | AIH | Gerais II | % Cesarianas)

## **03. FATURAMENTO AIH**

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento AIH. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta   c: temp  chamado SUS.TXT .

## **04. REFATURAMENTO AIH**

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento AIH já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo chamado SUS.TXT é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo.

## **05. REPROCESSAMENTO AIH**

Selecionar a opção reprocessamento AIH

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Observação: Caso a quantidade de cotas não seja maior que 1 a remessa então será cancelada.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Auditoria)
* Retornar Conta para Correção(Faturamento)

As duas opções acima para o SUS tem o mesmo comportamento.

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Auditoria)" ou "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo podemos verificar que as contas foram liberadas, vide imagem abaixo.

## **06. TABELAS UTILIZADAS**

* SZSUSAIHPROD
* SZSUSRECEMNATO
* SZSUSAIHCID
* SZSUSPROCREALIZADOS
