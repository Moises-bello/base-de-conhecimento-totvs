---
article_id: 360011930291
category: SIGAEST - CUSTOS
content_hash: c519ea6e1dde254257e3311ae5145327ee27b322f7e346fbb71e6d65784454ba
fetched_at: '2026-06-28T22:39:00.483242+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como parametrizar
  o relatório Kardex por Período MATR900
type: support-article
updated_at: '2026-04-06T16:09:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Como-parametrizar-o-relat%C3%B3rio-Kardex-por-Per%C3%ADodo-MATR900
---

O relatório Kardex por Período (MATR900) no Protheus é usado para analisar movimentos e custos de estoque, requerendo pré-processamento do custo médio (MATA330). A parametrização correta inclui informar produto, período, armazém conforme MV\_CUSFIL, sequência de cálculo e impressão. Movimentos sem movimentação física não aparecem. Para inconsistências, é recomendada análise dos últimos três períodos e envio do PDF com parâmetros e análise ao suporte.

**Dúvida**

Como extrair corretamente (parametrizar) as perguntas do relatório Kardex por Período (MATR900) para análise de custos e movimentos do estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque e Custos - Todas as versões.

**Solução**

O relatório Kardex por Período (MATR900) é a ferramenta principal para analisar as movimentações de estoque e seus respectivos custos. Para garantir a precisão dos dados na listagem, é necessário que o sistema esteja corretamente parametrizado e atualizado.

**Pré-requisito:** É obrigatório já ter processado a rotina de Custo Médio (MATA330) para o período que será avaliado.

**Conceito importante:** Movimentos realizados com Notas de Entrada ou Saída em que o campo da TES de controle de estoque esteja configurado como não (F4\_ESTOQUE = NAO) **não constarão no relatório**, pois não realizam movimentação física.

**Modelo** [Smart View - Kardex](https://tdn.totvs.com/x/VyueLQ)

**Passos**

1. Acesse o módulo SIGAEST e siga o caminho: **Relatórios > Análises > Movimentações > Kardex > Por Período.**
2. **Na Pergunta 01 (Do Produto?)** e **Pergunta 02 (Até o Produto?)**, informe o código de apenas um produto para focar a análise.
3. **Na Pergunta 05 (Do Período?)** e **Pergunta 06 (Até o Período?)**, informe o período mensal exato a ser analisado (exemplo: 01/04 a 30/04).
4. **Na Pergunta 08 (Qual Armazém?)**, preencha rigorosamente de acordo com o conteúdo do parâmetro **MV\_CUSFIL**, que determina a aglutinação de custos na empresa:

* **Se MV\_CUSFIL = E** (Empresa): Preencha com **##**
* **Se MV\_CUSFIL = F** (Filial): Preencha com **\*\***
* **Se MV\_CUSFIL = A** (Armazém): Preencha com o código do armazém (exemplo: 0001, respeitando as casas decimais do campo). Não avalie custos com configurações divergentes da aglutinação oficial do sistema.

5. **Na Pergunta 09 (Doc/Sequência?)**, preencha com **S** para exibir e validar a sequência de cálculo gerada pelo custo médio.
6. **Na Pergunta 11 (Sequência de Impressão?)**, preencha com **CÁLCULO** para visualizar os movimentos na exata ordem em que foram recalculados pelo sistema.
7. **Na Pergunta 16 (Seleciona Filiais?)**, escolha Sim ou Não conforme a necessidade
8. Após confirmar, gere a impressão do relatório em formato PDF.

**Regras para análise e envio ao suporte:**

Caso identifique custos ou saldos físicos incorretos, emita o Kardex (MATR900) dos últimos três períodos para validar se o saldo final de um fechamento confere com o saldo inicial do mês seguinte.

Para abertura de chamados, envie sempre o PDF do relatório gerado com a Sequência de Impressão em "**Calculo**", o print da tela de parâmetros utilizada e um descritivo destacando qual linha de movimento está inconsistente junto com a sua respectiva analise e entendimento, do o porque esta errado.

* Emitir o Kardex por Período (MATR900) dos últimos três períodos.
* Verificar se os saldos iniciais batem com os saldos finais dos períodos anteriores.
* Analisar os fechamentos para identificar possíveis inconsistências.

Print ou anexo tambem dos ultimos 3 periodos, filtrado no arquivo **SB9 em formato Sqlite**, apenas do produto em questão.

**Curiosidades:**

* **Eu tenho custo aglutinado por Filial ou Empresa, eu posso avaliar o custo das minhas movimentações no Kardex, filtrando apenas o numero do Armazem?**

  *R: Não, isso vai te gerar uma duvida do custo "no armazem", e seu calculo não é por armazem, é aglutinado, então sempre validar custos, de acordo seu parametro MV\_CUSFIL, não se tratando de um erro, mas sim de um conceito aplicado a regra de aglutinação.*

**Saiba mais:**

[*MP - SIGAEST - Como fazer uma análise de Custos no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
