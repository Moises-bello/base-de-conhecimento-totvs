---
content_hash: 8aedae63549c52982aedd8f448ca0ee378c158458d7adc2902473124df59c242
fetched_at: '2026-06-29T00:08:15.773008+00:00'
page_id: '244924243'
product: rm
source: tdn-rm
title: RMPAT00006_Moedas_e_Índices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244924243
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.17 ou superior |
| **Ocorrência:** | Moedas e índices |
| **Ambiente:** |  |
| **Passo a passo:** | Em um significado básico, “moeda” é o meio através do qual são efetuadas as transações monetárias, ou seja,  é a unidade representativa de valor, controlada pelo governo do país, que é o único que pode fixar e controlar seu valor.    **Disponível em: Cadastros | Moedas e Índices.** Neste módulo você pode cadastrar a moeda corrente do seu país e as de outros países.        **Identificação - Cadastro de Moedas e Índices:** Nesta pasta são apresentadas informações que identificam a moeda ou o índice. Informações sobre alguns campos:  **Defasagem em Meses:** Preencha o campo com o número de meses cuja moeda/índice está defasada. Neste caso 0.  **Exemplo:** São cadastradas as seguintes Cotações: 1/10/2008 Valor = 7,000 30/09/2008 Valor = 6,000 29/09/2008 Valor = 5,000 01/09/2008 Valor = 4,000 28/08/2008 Valor = 3,000 27/08/2008 Valor = 2,000 25/07/2008 Valor = 1,000    No campo Defasagem é informado 0 (zero): Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/10, pois considera que a moeda não está defasada.    No campo Defasagem é informado 1 (um): Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/09. Ou seja, o sistema busca a cotação de 30 dias anteriores a data informada.    No campo Defasagem é informado 2 (dois): Ao baixar um lançamento com a data de 01/10/2008 o sistema busca a cotação do dia 01/07. Em todos as situações, caso não exista cotação da data procurada pelo sistema, será verificada a data anterior.    **Parte Inteira e Parte Fracionária:** Informe os nomes para a parte inteira e para a parte fracionária da moeda ou índice.  **Exemplo:** Exemplo de um cadastro de moeda: Símbolo = R$ Tipo = moeda Descrição = Real Casas Decimais = 4 Parte Inteira Singular = real Parte Inteira Plural = reais Parte Fracionária Singular = centavo Parte Fracionária Plural = centavos    No cadastro do Lançamento Financeiro, deve-se observar o respectivo campo para inserir a moeda e/ou o índice, pois o comportamento do sistema será diferente dependendo desses dados.  Se o objetivo for cadastrar um lançamento em moeda estrangeira, deve-se inserir um código no campo Moeda que esteja cadastrado com o tipo Moeda. E caso seja incluir um lançamento financeiro em real, mas com algum indexador para ajuste de valor, deve-se cadastrar no campo Moeda a moeda Real e no campo Indexador um código cadastrado como Índice. |
| **Observações:** | As cotações devem ser cadastras sempre com 4 casas decimais. |
