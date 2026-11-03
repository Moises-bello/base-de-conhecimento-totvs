---
content_hash: 7895a667cfed54a5fd8fb39682be8cd2d946c8a1fc3ef45af6a042f44cc9f1bb
fetched_at: '2026-06-29T00:09:15.548920+00:00'
page_id: '421385410'
product: rm
source: tdn-rm
title: Lançamentos no RM Fluxus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385410
version: 5
---

---

Podem-se gerar lançamentos no RM Fluxus, a partir do Cronograma Previsto.

Para isto:

Selecione a tarefa para o qual deseja gerar lançamentos. Essa tarefa deve ser uma Obra (Subdivisão do Projeto).

Clique no ícone "Gerar / Visualizar Lançamento no RM Fluxus para a Obra selecionada" e será aberta a visão de lançamentos já gerados para o RM Fluxus. Clique no ícone "Gerar Lançamentos no RM Fluxus referente à obra selecionada" e preencha os campos necessários.

Os campos dos lançamentos são preenchidos da seguinte maneira:

Histórico: "Previsão gerada pelo RM Solum - Projeto xxxx - Obra xxx - Período x"

Tipo Contábil: "Não Contábil"

Filial, Departamento e Centro de Custo: mesma informação existente no Projeto

Número do Documento: mesmo número de referência (identificador do lançamento)

Valor: soma das previsões de todas as tarefas da Obra selecionada, sendo que será gerado um lançamento para cada período. Será considerado o Cronograma previsto financeiro, não considera BDI do projeto (independente da forma de aplicação).

Moeda: R$

Data de emissão: data em que o lançamento foi gerado pelo RM Solum

Data de vencimento e de previsão de baixa: data de início do período do lançamento.

**Atenção:**

Para que o lançamento seja gerado é necessário que o parâmetro 'Gerar Número de Documento Seqüencialmente' ou o parâmetro 'Copiar Ref. Para Nº do Documento' do RM Fluxus esteja selecionado. Isso deve ser feito no Menu Opções | Parâmetros | RM Fluxus, pasta Lançamentos.

**Observação:**

Caso deseje que a data de vencimento ou data de previsão de baixa seja alterada para o próximo dia útil em caso de final de semana ou feriado é necessário alterar os parâmetros 'Aceita Vencimento a Pagar em finais de semana e feriados' e 'Aceita Previsão de Baixa a Pagar em finais de semana e feriados' para Primeiro Dia Útil Posterior

---
