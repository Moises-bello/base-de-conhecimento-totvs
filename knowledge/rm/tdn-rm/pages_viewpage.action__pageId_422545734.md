---
content_hash: b194ee1e8e4aa7c335b321e45fdba464aa09f42e37372b368a905315e858eb3d
fetched_at: '2026-06-29T00:09:20.653617+00:00'
page_id: '422545734'
product: rm
source: tdn-rm
title: Geração do Registro F525 por Documentos Agrupados por Código da Situação Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545734
version: 4
---

**Cadastro de Parâmetro de Processos F500**

Implementação do campo Base de Cálculo do Registro 1900 nos tributos do Cadastro de Parâmetros de Processos dos registros F500.

**Processo "Cálculo das Contribuições Docs Não Escriturados"**

O processo foi evoluído para atender o serviço de Inclusão de tributos do Lançamento financeiro e suas Baixas com mais de um CST.  
No filtro de datas dos lançamentos financeiros sempre será considerado a Data de Emissão alem das datas de Baixa, compensação e etc.  
A tela do processo foi ajustada para que não seja possível editar o conteúdo do campo mês e o campo Ano será considerado apenas números.   
A base será preenchida com o valor calculado a partir do campo "Base de Cálculo do Registro 1900" do cadastro dos Parâmetros de Processos dos registros F500.       Pode ser usado o Valor Original ou Fórmula.

**Exemplo de fórmulas utilizadas**

***Importante!*** As fórmulas abaixo são apenas exemplos, as fórmulas devem ser criadas conforme a sua necessidade e entendimento a respeito da geração dos valores nos registros.

* Baixa = Formula Teste 1900 CST 01 = TABLAN('VALORORIGINAL','V') \* 0.60
* Compensação = Formula Teste 1900 CST 01 = TABLAN('VALORORIGINAL','V') \* 0.60
* Baixa = Formula Teste 1900 CST 06 = TABLAN('VALORORIGINAL','V') \* 0.40 - Compensação = Formula Teste 1900 CST 01 = TABLAN('VALORORIGINAL','V') \* 0.40
* Formula Teste F525 CST 01 - Baixa = TABLANBAIXA('VALORORIGINAL','V') \* 0.60
* Compensação = Formula Teste 1900 CST 01 = TABLAN('VALORORIGINAL','V') \* 0.60
* Formula Teste F525 CST 06 - Baixa = TABLANBAIXA('VALORORIGINAL','V') \* 0.40
* Compensação = Formula Teste 1900 CST 01 = TABLAN('VALORORIGINAL','V') \* 0.40

***Observação:*** Caso o parâmetro "Base de Cálculo do Registro 1900" não estiver selecionado nenhuma opção, no processo será considerado o valor presente no campo FLAN.VALORORIGINAL.

**Layout EFD Contribuições**

* Foi implementado o parâmetro "F525 - Indicador da composição da receita recebida no período" com este parâmetro marcado como "04-DocumentoFiscal" o registro F525 será gerado por documento.

***Observação:*** Com a opção default "01-Cliente" marcado o registro F525 será gerado conforme é gerado atualmente por Cliente Fornecedor.  
  
**Contexto EFD Contribuições**

* Implementação dos registros F500\F525\1900 agrupando mais de um CST.
* No registro 1900 o campo (07) VL\_TOT\_REC será gerado com base no campo FTRBLAN.BASECALCULOORIGINAL respeitando o agrupamento por CST.

**Dúvidas Frequentes:**

* E se for usada a o opção "Pela Compensação"?\*

Deve ser usada uma fórmula que busque o valor do Lançamento financeiro. Exemplo: TABLAN ('VALORORIGINAL','V')

* Lançamento Financeiro a pagar e a receber ?\*

Conforme guia prático Versão 1.22 de 31/07/2017 "Este registro tem por objetivo representar a escrituração e tratamento fiscal das receitas recebidas no período, segmentado por Código de Situação   
 Tributária - CST, do PIS/Pasep e da Cofins." Ou seja, vão ser considerados lançamentos financeiros "A Receber".

* No filtro de datas dos lançamentos financeiros sempre será considerado a Data de Emissão além das datas de Baixa, compensação e etc. ?

O registro 1900 é gerado pela data de emissão caso o lançamento não tenha sido baixado ou compensado.  
 É necessário gerar o processo de cálculo dos Docs não escriturados mesmo que o lançamento não esteja baixado, para que a tabela FTRBLAN seja povoada e o registro 1900 gerado.  
 As informações do registro 1900 são consolidadas por " CFOP, CST, Série/Subsérie, Situação, Informações complementares e conta contábil."
