---
article_id: 41454117600279
category: SIGAEST - CUSTOS
content_hash: fa68011cd3f85ae528aa4a237b5a01d295ee5ecf285e01940aa4dd5e0451d3b4
fetched_at: '2026-06-28T22:39:00.802765+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como validar o custo
  calculado vs a contabilizacao do mesmo?
type: support-article
updated_at: '2026-06-24T13:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41454117600279-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-validar-o-custo-calculado-vs-a-contabilizacao-do-mesmo
---

A conciliação do custo do movimento no estoque no ERP Protheus é feita registrando todas as movimentações, configurando lançamentos padrão, executando recálculo com contabilização, e comparando os relatórios de Razão Contábil e Kardex para assegurar a integridade financeira. É possível usar o Conciliador Contábil para vincular manualmente as tabelas e validar os valores.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41454122952215) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como eu posso saber, se o custo do movimento, foi levado corretamente para minha contabilizacao de estoque?  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A conciliação entre os valores de estoque e os registros contábeis é fundamental para garantir a integridade das demonstrações financeiras e a precisão na valorização dos ativos. No ERP Protheus, este processo é realizado por meio de rotinas de recálculo que corrigem eventuais distorções e automatizam a integração de dados.

Primeiro, entenda como contabilizar, para depois entender como avaliar:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações no Estoque Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos)

Este processo segue uma sequência lógica para assegurar que cada movimentação física possua um reflexo financeiro equivalente e auditável:

1. **Registrar Movimentações de Estoque:** Lance todos os eventos do período, incluindo notas fiscais de entrada (compras), notas de saída (vendas), requisições internas para produção e apontamentos de produção.
2. **Configurar Lançamentos Padrão (LPs):** Configure os LPs específicos para o recálculo do custo médio (normalmente na série 600, como 666 e 668). Defina as contas contábeis de Débito (estoque/ativo) e Crédito (custo ou fornecedores) para cada tipo de transação.

   [*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)
3. **Executar Recálculo e Contabilização:** Execute a rotina de Recálculo do Custo Médio com a contabilização habilitada, ou processe a jornada de fechamento. Ao final, o sistema disparará a contabilização automática dos valores, integrando-os ao módulo contábil.
4. **Extrair o Razão Contábil:** Gere o relatório de Razão para as contas de estoque definidas, filtrando pelo período e pelas filiais correspondentes para obter o saldo final e a movimentação contábil.
5. **Extrair o Kardex de Movimentações:** Gere o relatório de Kardex (ou Extrato de Movimentações) para os produtos do período. Este relatório detalha a quantidade e o valor de cada entrada e saída física.

   [*Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como parametrizar o relatório Kardex por Período MATR900*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-parametrizar-o-relat%C3%B3rio-Kardex-por-Per%C3%ADodo-MATR900)
6. **Comparar Valores:** Realize o cruzamento do saldo final e dos totais de débitos/créditos do Razão Contábil com os saldos e totais de entradas/saídas do Kardex. Analise eventuais divergências causadas por falhas na parametrização de LPs ou movimentos não contabilizados.

Abaixo, apresentamos um cenário de produção e venda utilizando o Custo Médio, com os respectivos lançamentos padrão configurados:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Etapa** | **Ação** | **Tabela** | **LP** | **Qtd** | **Valor Unitário** | **Valor Total** |
| 1 | Compra MP01 | SD1 | 681 | 100 | 10 | 1000 |
| 2 | Compra MP02 | SD1 | 681 | 100 | 20 | 2000 |
| 3 | Compra MP03 | SD1 | 681 | 100 | 30 | 3000 |
| 4 | Requisição MP01 | SD3 | 666 | 10 | 10 | 100 |
| 5 | Requisição MP02 | SD3 | 666 | 10 | 20 | 200 |
| 6 | Requisição MP03 | SD3 | 666 | 10 | 30 | 300 |
| 7 | Apontamento PA01 | SD3 | 668 | 10 | 60 | 600 |
| 8 | Venda | SD2 | 678 | 1 | 60 | 60 |

* **Para gerar o Kardex:** Acesse a rotina MATR900 ou utilize a opção de Acompanhamento de Custos.

![](https://tdn.totvs.com/download/attachments/1079774662/image-2026-6-22_11-35-3.png?version=1&modificationDate=1782139348660&api=v2)

![](https://tdn.totvs.com/download/attachments/1079774662/image-2026-6-22_11-36-16.png?version=1&modificationDate=1782139348593&api=v2)

* **Para gerar o Razão Contábil:** Acesse a rotina CTBR400

![](https://tdn.totvs.com/download/attachments/1079774662/image-2026-6-22_11-38-11.png?version=1&modificationDate=1782139348527&api=v2)

Observe, que o valor levado ao Razão, é exatamente o valor do custo da movimentação, ou seja, voce comparou Custo vs Contabil.

É possível realizar a conciliação utilizando o Conciliador Contábil, vinculando manualmente as tabelas SD1, SD2 e SD3. Para orientações detalhadas, consulte a [Conciliador Backoffice (SIGACTB)](https://tdn.totvs.com/pages/viewpage.action?pageId=587636759).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
