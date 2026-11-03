---
content_hash: 84985dd2d0fb96ae558e2f9f740872bd4846270ab4cf4a33a1f5bdefcd74440f
fetched_at: '2026-06-29T00:09:09.068383+00:00'
page_id: '391545741'
product: rm
source: tdn-rm
title: RMCTB00001_Fechamento de Exercício
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=391545741
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS - Gestão Contábil |
| **Versões:** | 12.1.20 |
| **Ocorrência:** | Fechar Exercício Contábil |
| **Ambiente:** | Novo Modelo BackOffice |
| **Passo a passo:** | **Definição do processo:**  Este processo é responsável por fechar o exercício contábil.  O fechamento de exercício será **anual e somente poderá ser liberado um exercício (ano) por vez**.  A execução deste processo move os dados de contabilização para tabelas de histórico deixando as tabelas de contabilização mais enxuta.  **Regras Gerais:**  Para execução deste processo, o sistema faz algumas validações, sempre considerando o ano definido para liberação do exercício nos parâmetros do processo:  • Valida se existe lançamentos em Lotes não integrados; • Valida se existe lançamentos com diferença; • Valida se existe inconsistências nos lançamentos; • Valida se existe tarefas pendentes;  **Exemplo:**  O sistema está parametrizado com o período contábil 01/01/2010 até 01/01/2020 e começou sua operação no dia 01/01/2010. Se o usuário executar fechamento de período do ano 2010 o sistema fará as seguintes alterações: • Fechará o exercício contábil, que corresponderá ao período de 01/01/2010 a 31/12/2010; • Calcula os saldos das contas de acordo com os parâmetros preenchidos para o exercício que esta sendo Fechado. Para calcular o saldo das contas, o sistema considerará o saldo do último exercício fechado.  O cálculo de saldo das contas segue o seguinte agrupamento:  - Coligada - Conta contábil - Filial - Departamento - Conta gerencial - Centro de custo - Código da Filial    O Cálculo dos saldos é a soma do Exercício anterior com o saldo do exercício fechado, ele ainda: • Move os dados das contabilizações no período selecionado para histórico; • Atualiza a tabela de saldo por exercício; • Atualiza as datas período contábil e data de fechamento.    Abaixo segue a tela que corresponde o processo acima: |
| **Observações:** | Caso o usuário identifique que seja necessário a Reabertura deste período, o mesmo poderá ser feito através do menu: Reabrir Exercício Contábil. |
