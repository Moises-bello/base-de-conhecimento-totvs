---
content_hash: d63b5f963e05dfb033050d3c55b089f6545f0a814fc97838c787345e70b20d3b
fetched_at: '2026-06-29T00:08:34.295369+00:00'
page_id: '274659288'
product: rm
source: tdn-rm
title: FFF0001_Produto_Nao_E_Apresentado_Na_Ficha_Fisica_Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/FFF0001_Produto_Nao_E_Apresentado_Na_Ficha_Fisica_Financeira
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e superiores |
| **Ocorrência:** | Produto não apresentado na impressão da Ficha Física Financeira |
| **Ambiente:** | Ficha Física Financeira |
| **Passo a passo:** | Objetivo Este documento tem por finalidade auxiliar a identificar as possíveis causas de uma movimentação de produto não ter sido apresentada na Ficha Física Financeira. Causa 1 - O produto está cadastrado com o tipo “Serviço” e o sistema não esta parametrizado para consistir saldo de serviço;  2 - O tipo de movimento utilizado para este produto não esta parametrizado para afetar estoque;  3 - A filial da movimentação esta definido no cadastro do produto para ser “Não Estocável”;  4 - O Campo TITMMOV.CODFILIAL e TITMMOV.CODLOC não estão preenchidos no movimento do produto;  5 - A data do movimento utilizado por este produto está fora do período utilizado na Ficha Física Financeira;  6 - A data do movimento utilizado por este produto esta anterior a data de fechamento de estoque e a regeração de saldos e custos não considerou este movimento;  7 - O movimento esta com status faturado/recebido e o parâmetro “Afetar Estoque após faturado/recebido” esta desmarcado.   Solução 1- Definir qual deve ser o tipo do produto, se produto, ou serviço. Se for o segundo caso deverá ser marcado o parâmetro consiste saldo de serviço, na etapa de Custo dos parâmetros de Gestão de Estoque.  2- Parametrizar o tipo de movimento para afetar estoque se for necessário.  3- Acessar o cadastro de produto e definir como “Estocável” na aba Informações por Filial se necessário.  4- Se os campos TITMMOV.CODFILIAL e TITMMOV.CODLOC não estiverem preenchidos, regrave o movimento para que os campos sejam preenchidos.  5- Verifique se a data do movimento (TMOV.DATAMOVIMENTO) esta dentro do intervalo da Ficha Física Financeira.  6- Altera a data de fechamento estoque para ser anterior a data do movimento, regera saldos e custos marcando a opção “Forçar Regeração Total” e tire a Ficha Física Financeira novamente.  7- Se realmente o movimento estiver com status faturado/recebido ele não irá aparecer na Ficha Física Financeira ao menos que o parâmetro “Afetar Estoque após faturado/recebido” estiver marcado.     * **Informações Adicionais**   No caso de alterar a data de fechamento estoque para posterior regeração de saldos e custo vale lembrar que a regeração com a opção “Forçar Regeração Total” marcada irá refazer todas as movimentações e calcular o custo unitário dos movimentos de entrada, e custo médio para os movimentos de saída baseado na parametrização em que a regeração esta sendo feita, ou seja, caso alguma parametrização tenha sido incluída/ alterada o sistema poderá apresentar saldos e custos divergentes da última regeração, pois ele irá refazer os cálculos com a parametrização atual. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
