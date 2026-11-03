---
article_id: 17995686483095
category: SIGAEST - CUSTOS
content_hash: 7ccbfcdab3345670d373794a09ca06cfb17c737992cb9187ee9f89eee0a7851e
fetched_at: '2026-06-28T22:39:00.637694+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como avaliar o erro
  Data width error em rotinas de processamento?
type: support-article
updated_at: '2026-06-18T14:44:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17995686483095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-avaliar-o-erro-Data-width-error-em-rotinas-de-processamento
---

O erro "Data width error" ocorre quando o tamanho dos dados excede o limite configurado no campo do dicionário de dados (SX3) durante processamentos no Protheus, como recálculo de custo médio. Para corrigir, verifique se o valor é correto; se sim, aumente o tamanho do campo; se não, ajuste ou exclua o movimento incorreto. Após correções, refaça os saldos com MATA300. Avalie também quantidades e moedas envolvidas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17995669969687) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

Em rotinas de processamentos, como o Recálculo do Custo Médio (MATA330), ou até mesmo em rotinas que efetuam movimentações de estoque, pode ocorrer a geração de um `error.log` que informa a mensagem "Data Width error". Como avaliar e corrigir o erro de estouro de campo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O erro "**Data width error**" é uma mensagem que indica um problema relacionado ao **tamanho (largura) dos dados**. Isso significa que a quantidade de caracteres e decimais calculados durante o processamento de uma operação excede o limite configurado para o campo no dicionário de dados (SX3).

**Por exemplo:** O erro ocorre quando o sistema espera gravar o resultado de um cálculo em um campo de tamanho 14 com 2 casas decimais, porém, o dado recebido e gerado pelo cálculo possui um tamanho superior ao que o campo suporta atualmente.

Exemplo, supondo que o seu campo B2\_CM1 no configurador possui tamanho 16 / 4, essa mensagem abaixo sera apresentada como erro>

`Data width error - Field: B2_CM1 Value: 29191919199.111111`

**>Porque:** o tamanho total é 17 contando do 2 até o ultimo 1 e (tirando ponto). Bem como o decimal esta tentando gravar 6 posições 111111, mas o seu campo tem 4 posições.

**A primeira avaliação necessária é:** o valor que o sistema está tentando gravar é correto?

* **Se o valor for correto** e coerente com a operação, então logo deve-se efetuar o aumento no tamanho dos campos afetados no dicionário de dados para suportar o novo volume de dados que esta tentando ser gravado.
* **Se o valor não for correto** (um número exorbitante gerado por erro de digitação ou movimento indevido), ajustar o tamanho do campo não é a solução. É necessário rastrear a movimentação que gerou a anomalia e estornar ou excluir o documento causador do erro.

> **IMPORTANTE:** Caso o erro ocorra na rotina Acompanha Custos (MATA038) durante a etapa de Cálculo do Custo Médio, efetue o processamento diretamente pela rotina de Custo Médio (MATA330). Isso é necessário para que seja gerado o `error.log` completo, uma vez que a rotina MATA038 apresenta apenas o cabeçalho do erro, impossibilitando identificar qual produto causou o incidente.

**Passos**

1. Identifique o campo e o valor estourado dentro do log. Exemplo da mensagem de erro no processamento: `Data width error - Field: B2_CM1 Value: 29191919199.111111`
2. Conte a quantidade de dígitos apresentados no valor (no exemplo acima, são 17 dígitos desconsiderando o ponto). Em seguida, verifique no sistema se o campo em questão (exemplo: `B2_CM1` na tabela SX3) possui o tamanho configurado menor que 16 ou casas decimais menores que as geradas?

   [Tamanho máximo por tipo de campo](https://tdn.totvs.com/pages/releaseview.action?pageId=22479521) (16 / 8)
3. Avalie os detalhes do `error.log` (sugere-se o uso do Notepad++ ou bloco de notas). Sabendo que o erro ocorreu na tabela de saldos atuais (SB2), busque e filtre dentro do log pelo campo `B2_COD`.
4. A busca por `B2_COD` trará o código do produto que gerou o erro de cálculo. Também é possível buscar por palavras-chave como `_DOC`, que trazem a relação do documento em processamento, assim voce podera avaliar cada um desses movimentos pontualmente.
5. Com o código do produto identificado, acesse o módulo Estoque/Custos e gere o relatório Kardex por Período (MATR900 ou Smartview ESTSV023) focado apenas neste produto.
6. Analise o relatório para identificar possíveis inconsistências. Verifique se existe alguma movimentação indevida no período, saldos ou valores digitados incorretamente que não condizem com a realidade.
7. Se for identificado um movimento incorreto, efetue a tratativa necessária (estorno ou exclusão do documento) e refaça a operação que apresentou o erro.
8. Caso o Kardex tenha sido gerado corretamente, sem exibir campos com asteriscos (`**********`) e sem movimentos incorretos, avalie duas alternativas:

   * Efetuar um Acerto de Custo para o produto, de forma que o custo seja corrigido e o valor reduzido.
   * Efetuar o aumento do tamanho e decimais dos campos relacionados a custo (tamanho máximo permitido pelo padrão TOTVS é 16/8). Essa ação é válida se o valor for devido e o sistema não comportar o volume do cálculo atualmente.
9. Após a correção da causa (seja ajuste de movimento ou aumento de campo), efetue o processamento da rotina de Refaz Saldos (MATA300) para o produto identificado com erro no log e em seus respectivos armazéns. Isso garantirá a recomposição correta dos saldos atuais.
10. Toda a avaliação/correção de campos, aumento e ajustes, deve ser feita previamente em Homologação.

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA300 - Refaz Saldos - Conceito e Informações*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420659401751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA300-Refaz-Saldos-Conceito-e-Informa%C3%A7%C3%B5es)

[*Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Como parametrizar o relatório Kardex por Período MATR900*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-MP-SIGAEST-An%C3%A1lise-de-Custos-MATR900-Kardex-por-Per%C3%ADodo)

**Avaliações Adicionais:**

* **Estouro nos campos de quantidade:** O conceito é o mesmo aplicado aos campos de custo. Avalie no Kardex se a quantidade de alguma movimentação foi digitada errada. Caso o volume real transacionado esteja correto, realize o aumento do tamanho dos campos de quantidade.
* **Estouro em outras moedas (além da moeda 1):** Caso o parâmetro `MV_MOEDACM` esteja em branco, será preciso ativar o rastro da respectiva moeda para que o acerto seja feito na moeda que está gerando o erro (mesmo se o objetivo for apenas zerar o saldo por falta de uso). Apenas ignorar ou alterar o parâmetro de contabilização não corrige o erro no registro da moeda.
* **Erro em documento de devolução ou com múltiplos itens:** A avaliação não deve se limitar ao erro em si, mas deve envolver a conferência de todos os itens contidos no documento, bem como os dados registrados no documento de origem (nota fiscal de saída ou entrada original).
* **SEMPRE:** Após ajuste de tamanho de campos, efetuar pontualmente a reinstalação de todas as procedures de forma geral, visando a integridade de dados: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Saiba Mais**

* [*Clique aqui e veja artigos sobre Processamentos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033442-SIGAEST-PROCESSAMENTOS)
* [*Clique aqui e veja artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
