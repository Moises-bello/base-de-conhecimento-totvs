---
content_hash: 08a314d34f0f9d152517cc0ba68fb6dc209b2d20e1ebe2ff67e7060e44559d87
fetched_at: '2026-06-29T00:08:41.396369+00:00'
page_id: '286725187'
product: rm
source: tdn-rm
title: DT_MATESTCNTFTOF01-636_Consultar_Valores_Orçados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286725187
version: 108
---

# Consulta Valores de Orçamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Consulta Valores de Orçamento* | MovConsultaOrcamentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Consulta Valores de Orçamento* | MovConsultaOrcamentoForm | |  |  | |
| **Cadastros Iniciais:** | *Controle Orçamentário* |
| **Parâmetro(s):** | *Não se Aplica* |
| **Ponto de Entrada:** | *Não se Aplica* |
| **Tickets relacionados** | *Não se Aplica* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | [MATESTCNTFTOF01-636](http://jiraproducao.totvs.com.br/browse/MATESTCNTFTOF01-636) |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *TMOVORCAMENTO* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Por esta opção, será possível consultar os valores de orçamento de forma simplificada e ágil.

**Observações:**

- A nova consulta de valores orçados só deve estar disponível quando utilizado o novo orçamento através do menu Opções | Controle Orçamentário | Utiliza Nova Versão.

- Melhoria na usabilidade da tela.

- A consulta pode ser visualizada através do menu Orçamento | Consulta Valores de Orçamento ou pelo atalho **CTRL + O**.

- Para realizar um filtro, seleciona-se nas abas a faixa a ser filtrada de acordo com o Centro de Custo, Período, Natureza e Grupo Orçamentário. **A aba de Grupo Orçamentário será exibida apenas se nos parâmetros de Controle Orçamentário estiver definido para utilizar o mesmo**.

**Centro de Custo**

**Período**

**Natureza**

**Grupo Orçamentário**

- No resultado da pesquisa, marca-se quais efetivamente serão filtrados, e/ou qualquer combinação dos quatro. Por exemplo: somente Centro de Custo, Centro de Custo com Natureza.

- Na tela de consulta é possível realizar dois tipos de agrupamentos: Por Centro de Custo ou Natureza e Por Período.

- Somente devem ser permitidas consultas que filtrem dados que retornem menos de 2.000 registros.

- A consulta traz todos os valores disponíveis de orçamento e também calcula o saldo.

Qualquer movimentação que for realizada no orçamento sempre irá afetar a tabela de saldo do orçamento e também irá incluir um registro na tabela que guarda as movimentações do orçamento (TMOVORCAMENTO).

A tabela de Saldo do orçamento terá os seguintes campos de valores:

- Valor Orçado;

- Valor Opcional 1;

- Valor Opcional 2;

- Valor Excedente;

- Valor Realizado;

- Valor Recebido;

- Valor Cedido.

\* O Valor Orçado é alterado somente pela tela de manutenção do cadastro de orçamento.

\* Os valores Opcional 1 e Opcional 2, são valores intermediários que podem ser configurados no efeito do orçamento por tipo de movimentos.

**Exemplo**: o Valor Opcional 1 pode ser parametrizado para ser afetado na solicitação de compra, o Valor Opcional 2 pode ser parametrizado para afetado no pedido de compra, e o Valor Realizado, será afetado somente na Nota Fiscal. Com essa configuração o orçamento será afetado na solicitação de compra, e será acompanhado até a realização na inclusão da Nota fiscal.

\* O Valor Excedente é atualizado automaticamente, quando algum item do movimento excede o saldo do orçamento disponível no período, e o movimento fica com o status de bloqueado.

\* O valor Realizado, é a última etapa que deve ser configurada para o efeito dos valores do orçamento.

\* Os valores Recebido e Cedido, são utilizados automaticamente na utilização do assistente que faz a transferência de valores do orçamento, para desbloquear um movimento.

divs
