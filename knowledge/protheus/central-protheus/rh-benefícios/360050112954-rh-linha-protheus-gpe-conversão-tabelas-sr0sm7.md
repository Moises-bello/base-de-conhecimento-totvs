---
article_id: 360050112954
category: RH - Benefícios
content_hash: 287f646752b3917cd16f378610bbe0a56ec10b56cd80e32f0b1482d01d2c55c4
fetched_at: '2026-06-28T22:44:03.887264+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Conversão tabelas SR0/SM7
type: support-article
updated_at: '2024-10-04T12:48:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050112954-RH-Linha-Protheus-GPE-Convers%C3%A3o-tabelas-SR0-SM7
---

**Dúvida**Como é realizado a conversão das tabelas SR0/SM7?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**

Devida à reestruturação do cálculo de vales (VA/VR/VT), será necessário criar uma rotina para conversão das tabelas **SR0** e geração da **SM7****.**

Assim que o a rotina de Atualização (**GPEA131**) for acessada, será verificada a existência da tabela **SM7** (desde que o conteúdo do parâmetro**MV\_CALCBEN**seja .T.). Caso não exista, será sugerida a execução do **UPDDISTR** para sua criação e também a atualização das outras tabelas efetuadas pelo presente requisito.

Ao confirmar a execução da conversão, será gerado uma cópia da tabela SR0 e no final emitida uma mensagem indicando o caminho onde a mesma se encontra. Se houver inconsistências, elas serão apontadas em um relatório,e todos os dados estiverem corretos, a conversão seguirá as etapas abaixo:

1) Para que o processamento do cálculo continue, os dados abaixo serão copiados da tabela **SR0** para a **SM7**:

* Filial
* Matrícula
* Tipo de Vale (Alimentação, Refeição, Transporte)
* Código
* Descrição
* Dias proporcionais informados
* Qtde vales dias úteis
* Qtde vales dias não úteis
* Tipo de cálculo

2) Os novos campos da tabela **SR0**serão alimentados da seguinte forma:

-   Se o benefício já estiver calculado, além de gravar o **SM7**, os novos campos do **SR0**, listados abaixo, serão preenchidos e o registro mantido:

* Período
* Número do pagamento
* Roteiro
* Tipo de benefício (de acordo com a tabela S011)
* Mês/Ano
* Número do pedido (sequencial)
* Indicador de compra (para indicar se a compra do vale está aberta ou fechada)
* Data de referência inicial
* Data de referência final
* Qtde de falta descontada da falta total
* Qtde de vales utilizados no domingo (zerado)
* Qtde de vales utilizados na segunda-feira (zerado)
* Qtde de vales utilizados na terça-feira (zerado)
* Qtde de vales utilizados na quarta-feira (zerado)
* Qtde de vales utilizados na quinta-feira (zerado)
* Qtde de vales utilizados na sexta-feira (zerado)
* Qtde de vales utilizados no sábado (zerado)
* Qtde dias fixos (zerado)

Se o benefício ainda não tiver sido calculado, depois de copiar os dados para **SM7**, o registro de **SR0** será excluído.
