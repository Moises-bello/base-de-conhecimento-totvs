---
content_hash: e844cab6eef15efa3924e2bc7f5e4361e7f26971eab15a602fa7b4a30eec043a
fetched_at: '2026-06-29T00:06:16.417243+00:00'
page_id: '212897635'
product: rm
source: tdn-rm
title: TIN005_8_Valida se existem Vendas sem Integração com Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212897635
version: 23
---

| Descrição | Observação |
| --- | --- |
| VENDA EM PREPARAÇÃO COM PLANO DE FINANCIAMENTO GERADO E SEM LANÇAMENTO FINANCEIRO | Este processo valida se existem vendas:   * com parcelas quitadas ou canceladas sem lançamento financeiro baixado ou cancelado correspondente; * em preparação com plano de financiamento gerado; * efetivadas com plano de financiamento não integrado; * efetivadas com parcelas quitadas e não integradas;    Versão 12.1.15 A partir da versão 12.1.15 está disponível o processo que corrige a falta de integridade de dados gerados pela importação de dados de sistemas terceiros (legados). Esta importação geralmente ocorre durante o processo de implantação do sistema.  Toda parcela TIN deve ter um lançamento financeiro correspondente, nos casos onde a importação criou parcelas apenas no TIN sem um lançamento financeiro correspondente, será necessário o ajuste.  A ferramenta fará a geração de lançamentos financeiros correspondentes as parcelas quitadas ou canceladas no TIN , que não possuam lançamentos financeiros baixados ou cancelados correspondentes no TOTVS Gestão Financeira. Este processo a partir da versão 12.1.15 faz parte dos Pré-requisitos para a versão de revitalização do TOTVS Incorporação.    Obs.: Este processo pode ser acessado também pelo novo menu Utilitário => Conversor de parcelas importadas de outros sistemas. Versão 12.1.9 O projeto de revitalização tem como um dos seus focos eliminar a redundância de dados, isso quer dizer que a estrutura onde são criadas as parcelas no módulo imobiliário e que depois são integradas ao módulo financeiro deixarão de existir, passaremos a guardar os valores apenas na estrutura de lançamentos do módulo financeiro. Assim evitaremos a possibilidade de exibir dados dessincronizados entre os dois módulos para os usuários, por isso vendas em preparação com plano de financiamento gerado são impeditivas para a revitalização e precisarão de uma tomada de decisão por parte do usuário do que deve ser feito com elas antes da conversão. Para saber exatamente quais são as vendas nessa situação a ferramenta de conversão consulta a base de dados e verifica as vendas nesta situação através do SELECT abaixo.   sqltrue *Este select não precisa ser executado pelo usuário, pois é apenas ilustrativo.* As vendas nas condições acima listadas serão apresentadas ao usuário    Através da visão apresentada, o usuário deverá selecionar cada venda e executar o processo que mais se adeque: "Gerar Lançamentos Financeiros” ou “Excluir o Plano de financiamento”. A visão apresentada é da venda permitindo os ajustes manuais dentro da ferramenta de conversão.  Depois de ajustar venda a venda, o usuário deve fechar a tela.    A ferramenta automaticamente passará para a próxima opção. |
|  |  |
