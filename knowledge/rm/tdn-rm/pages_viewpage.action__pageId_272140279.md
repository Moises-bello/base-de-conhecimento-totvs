---
content_hash: fb1fac0e4610b45fb8c746a272cfe83c58425389b8575f79c47ae412f8a51e18
fetched_at: '2026-06-29T00:08:29.018598+00:00'
page_id: '272140279'
product: rm
source: tdn-rm
title: MEDU-2822 DT Validações e alertas de relatórios de boleto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272140279
version: 116
---

# VALIDAÇÕES E ALERTAS DE RELATÓRIOS DE BOLETO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Validação de relatórios* | **Validação de relatórios** |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | ***Mensagem inicial do sistema*** | ***Mensagem inicial do sistema*** | | ***Geração de lançamentos*** | ***Geração de lançamentos*** | | *Parâmetros de relatório de boleto* | ***Parâmetros de relatório de boleto*** | | **Impressão de Boleto** | ****Impressão de Boleto**** | |
| **Cadastros Iniciais:** | *Relatórios feitos no gerador antigo (delphi) ou novo (RM Reports) Boletos gerados para os responsáveis financeiros dos alunos.* |
| **Parâmetro(s):** | *Em Configurações | Parâmetros | Tesouraria| Relatórios:*   * *Escolher o tipo de relatório de Contrato / Boleto**:*   + *Gerador de Relatórios (Antigo): Utilizará os relatórios criados no gerador de relatórios em delphi*   + *RM Reports: Utilizará os relatórios criados no RM Reports.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows 7 ou superior* |

## Descrição

A partir da versão 12.1.14, os RELATÓRIOS DE BOLETOS deverão ter a TABELA DE BOLETOS como tabela principal e NÃO mais a tabela de lançamentos.

Essa alteração foi necessária devido às adaptações no sistema para atender a nova plataforma de cobrança da Febraban, utilizando sempre boletos registrados. Para isso, o sistema foi evoluído, permitindo mais de um boleto associado ao mesmo lançamento.

## Procedimento para Implantação

A validação estará contida nas versões mais recentes do Educacional a partir da 12.1.14.

## Procedimento para Utilização

1. **Mensagem inicial de sistema**: Ao logar no módulo do Educacional ou alterar o contexto na MDI para o contexto do Educacional, o sistema exibirá o alerta abaixo:
2. **Geração de lançamentos**: Mensagem de alerta para o usuário conforme (figura 1) quanto à tabela master do relatório com opção de não aparecer mais ao selecionar o checkbox “Não exibir novamente” (semelhante às mensagens iniciais do sistema) na geração de lançamentos (visão de parcelas e wizard de geração).
3. **Parametrização do relatório de boleto**: *(Configurações | Parâmetros | Tesouraria| Relatórios*)

##### (**Utilizando o Reports [DotNet]**)

Quando o usuário for imprimir um boleto, o sistema verificará a tabela master do relatório. Caso não consiga detectar que a tabela master é a FBOLETO, será exibida uma mensagem de alerta para o usuário que poderá ignorar a mensagem e parametrizar o relatório escolhido.

(**Utilizando o Gerador [Delphi]**)

Quando o usuário for imprimir um boleto, o sistema verificará os filtros de relatório em Delphi. Caso o filtro não esteja sendo feito utilizando FLAN.IDBOLETO, será exibida uma mensagem de alerta para o usuário que poderá ignorar a mensagem e parametrizar o relatório escolhido.

4. **Impressão de boletos**:

 (**Utilizando o Reports [DotNet]**)

Quando o usuário for imprimir um boleto, o sistema verificará a tabela master do relatório. Caso não consiga detectar que a tabela master é a FBOLETO, será exibida uma mensagem de alerta para o usuário que poderá ignorar a mensagem e parametrizar o relatório escolhido.Essa mensagem terá a opção de não aparecer mais ao selecionar o checkbox “Não exibir novamente” (semelhante às mensagens iniciais do sistema)

Importante

O identificador da mensagem será montado considerando o Id. do relatório selecionado, isto é, se o usuário selecionar a opção "Não exibir novamente" para um relatório "A" e selecioná-lo para impressão posteriormente, a mensagem de alerta não será exibida mas, se o usuário selecionar um outro relatório "B" para impressão, a mensagem de alerta será exibida novamente.

(**Utilizando o Gerador [Delphi]**)

Quando o usuário for imprimir um boleto, o sistema verificará os filtros de relatório em Delphi. Caso o filtro não esteja sendo feito utilizando FLAN.IDBOLETO, será exibida uma mensagem de alerta para o usuário que poderá ignorar a mensagem e parametrizar o relatório escolhido. Essa mensagem terá a opção de não aparecer mais ao selecionar o checkbox “Não exibir novamente” (semelhante às mensagens iniciais do sistema)

Importante

O identificador da mensagem será montado considerando o Id. do relatório selecionado, isto é, se o usuário selecionar a opção "Não exibir novamente" para um relatório "A" e selecioná-lo para impressão posteriormente, a mensagem de alerta não será exibida mas, se o usuário selecionar um outro relatório "B" para impressão, a mensagem de alerta será exibida novamente.

A impressão de relatórios em Delphi continua validando os campos FBOLETO.CODCOLIGADA e FBOLETO.IDBOLETO antes da exibição da mensagem de alerta. Se o relatório de boleto não possuir esses campos, será exibida a mensagem abaixo ao invés da mensagem de alerta citada anteriormente.

divs
