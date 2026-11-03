---
content_hash: 12ad2adcb425cd8225300fb64c9da17efd0b26a5db940dfb7b5ac4bfe4679b1d
fetched_at: '2026-06-29T00:11:45.093806+00:00'
page_id: '819495690'
product: rm
source: tdn-rm
title: Geração Automática de OS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819495690
version: 2
---

Permite a geração automática de OS com base nos Planos de manutenção ou/e Índices de acompanhamento:

**Geração a partir dos Planos de Manutenção:**  
Os planos utilizados na execução do processo para geração automática, serão os que tiverem a data de vencimento menor que a data atual somando os dias com o parâmetro "Número de dias de antecedência para geração de OS".

Para assegurar o correto funcionamento da geração automática de Ordem de Serviço (OS), é necessário que o procedimento de inicialização do plano de manutenção tenha sido executado previamente. Para obter informações mais detalhadas sobre esse procedimento, recomendamos a consulta às linhas anteriores deste mesmo documento, referente ao Plano de manutenção.

**Geração a partir de Índices de Acompanhamento:**

* Serão selecionados os índices de Objetos que tenham os valores menores que o valor mínimo e maior que o valor máximo definidos no cadastro de índices;
* O tipo de movimento selecionado, será o que estiver parametrizado no índice;
* Campos utilizados para a geração da OS:
  + Coligada
  + Tipo de Movimento
  + Objeto de Manutenção
  + Filial
  + Local de Estoque
  + Cliente/Fornecedor
  + Funcionário Responsável
  + Histórico de Indicador
  + Centro de Custo
* Após a criação da OS o identificador do movimento poderá ser consultado nos índices de acompanhamento dos respectivos objetos;
* Esse processo poderá ser agendado.
