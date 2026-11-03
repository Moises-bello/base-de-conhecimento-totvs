---
content_hash: b62d4ea10eeda0f07cce3801d5582241221d4343da3730e15da88d7c3ab9870b
fetched_at: '2026-06-29T00:09:18.681850+00:00'
page_id: '421388747'
product: rm
source: tdn-rm
title: Alteração Global de Lançamentos 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388747
version: 19
---

O processo de Alteração Global consiste na alteração em múltiplos Lançamentos simultaneamente.

Ao realizar as alterações se for identificado algum impedimento será exibido ao final da execução do processo, um arquivo com o log explicativo.

Caso parametrizado, ao utilizar Orçamentos Excedidos (Liberar com Senha), Limite de crédito do Cli/For, Clientes em atraso e Clientes vencidos o sistema não solicitará a senha do usuário supervisor para que o processo seja realizado. Isso porque o processo é executado via job num servidor, inclusive com agendamento, onde não há interferência do usuário (tela para perguntar a ação). Caso o usuário não tenha permissão, o processo não será executado para os registros que estejam vinculados a alguma dessas restrições.

**Dicas**  
Lançamentos com "" não poderão ser alterados os campos relacionados a Valores gerais (original, juros, multa, capitalização, juros ao dia, multa ao dia, formulas dos campos e etc.), Data Vencimento, Data Emissão, Tipo contábil e Valores adicionais.  
   
 Filial  
Quando a alteração global for para o campo Filial, o sistema altera a Filial e limpa o campo Departamento. Para executar o processo de Alteração Global de Filial o campo Departamento não poderá ter rateio, se houver rateio o sistema não permitirá a alteração.

Departamento

Quando o departamento for alterado, a Filial será alterada para a Filial do Departamento selecionado. Se houver rateio no Departamento dos Lançamentos selecionados e o Departamento selecionado para alteração for da mesma Filial, o sistema fará a alteração.   
Se houver rateio no Departamento dos Lançamentos selecionados e o Departamento selecionado para alteração for de outra filial o sistema não permitirá a alteração, o rateio deverá ser excluído.

Centro de Custo

Quando o Centro de Custo for alterado, o sistema altera o Centro de Custo e mantem os rateios dos Lançamentos.

Evento Contábil

Ao alterar Lançamentos, se o campo escolhido for "Evento Contábil", o sistema vai regerar a contabilização automaticamente, mesmo que o novo evento contábil seja igual ao anterior.

Convênio

Caso esteja parametrizada a "Contabilização de Mútuo" disponível em Integração Contábil | Contabilização, poderá ser feita uma remessa para um convênio de outra coligada onde será feito o pagamento propriamente dito. Assim, na pesquisa desse campo, também serão exibidos convênios de outra coligada.

Valor Original

Ao alterar Lançamentos, se o campo escolhido for "Valor Original" o sistema vai regerar a contabilização automaticamente.

**Observação:**

* A opção de Alteração Global de Lançamentos  está disponível também para integração TOTVS Educacional x BackOffice Protheus quando ativa, a partir da versão 12.1.31.
