---
content_hash: e7916f3fb57844b8a164269d7ec7f4e11d14274c885c916e8b9584d4fccc3307
fetched_at: '2026-06-29T00:10:03.287737+00:00'
page_id: '452719089'
product: rm
source: tdn-rm
title: Calcular Movimentação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719089
version: 8
---

**Calcular Movimentação**

Neste módulo de Recálculo da Movimentação consiste em recalcular de forma global a movimentação dos funcionários de acordo com os parâmetros pré-estabelecidos no módulo de Recálculo.

ATENÇÃO: O processo de cálculo não deve ser executado simultaneamente à compensação do banco de horas, mesmo que o parâmetro **Calcula funcionários com alterações manuais** esteja desmarcado, pois o contexto do recálculo será carregado antes da compensação conseguir bloquear o movimento do funcionário, e por consequência, o recálculo irá desfazer a compensação/lançamento de banco de horas.

Pelo módulo é possível controlar:

**Parâmetros:**

**Calcula Funcionários sem pendências de Cálculo -** Efetua o recálculo dos funcionários que não tiveram dados alterados.

**Calcula Funcionários com alterações Manuais -** Efetua o recálculo para os funcionários que possuem alterações manuais.

**Observação -**Remove as alterações manuais e desabilita o botão "Valores alterados manualmente".

**Atualiza informações das ocorrências -** Quando **desmarcado** , será considerada a(s) ocorrência(s) já calculada(s) e gravada(s) na tabela AJUSTFUN. Quando **marcado** , será desconsiderada a(s) ocorrência(s) já gravada(s) na AJUSTFUN e irá realizar o cálculo com base na configuração atual do produto.

**Observação:**

Quando no sindicato estiver configurado nas etapas **- 3-Faixas de extras e 13-Banco de horas”** os parâmetros **"Considera faixas de distribuição de horas extras por intervalo e "Considera atitude do evento"**. Se ao realizar o recálculo a opção **“Atualiza informações das ocorrências”**, estiver desmarcado,  o sistema sempre irá considerar a atitude do evento  respeitando se existem alterações da Atitude da ocorrências coletadas .

**Atualiza ocorrências criticadas do período -** Quando **marcado**, atualizará o cálculo de todas as ocorrências, inclusive das ocorrências criticadas no período. Quando **desmarcado**, e houver ocorrências criticadas no período, nenhuma ocorrência será atualizada.

**Calcula eventos por fórmula no movimento -** Efetua o cálculo de eventos calculados por fórmula.

**Calcula eventos por fórmula no banco de horas -** Efetua o cálculo de fórmulas do banco de horas do evento.

**Gera arquivo de LOG técnico -** Gera o arquivo "RMCHRONUS\_CALCULO\_LOG" depois da execução do cálculo. Provavelmente na pasta C:\CorporeRM\RM.Net\ RMCHRONUS\_CALCULO\_LOG.txt

**Gera memória de cálculo -** Gera memória de cálculo para cada jornada calculada do funcionário. Para visualizar a memória de cálculo deverá acessar Movimento/Cálculo/Jornada Calculada.

**Observação**

A memória de cálculo é gerada somente para uma seleção de no máximo 10 funcionários, acima disso não é gerado memória de cálculo devido ao comprometimento de desempenho do recálculo.
