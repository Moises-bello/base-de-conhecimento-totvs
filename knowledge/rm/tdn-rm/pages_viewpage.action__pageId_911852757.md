---
content_hash: f08ed3d05268b56b4a401bbfc3f0890abd8f13413a62e65222bf714c08aef35c
fetched_at: '2026-06-29T00:12:03.566772+00:00'
page_id: '911852757'
product: rm
source: tdn-rm
title: Fechamento do Condomínio Individualizado - Processo - Gerar Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911852757
version: 26
---

Geração de Lançamentos Financeiros – Fechamento de Condomínio

# 📘 Introdução

Este processo permite a geração de **Lançamentos Financeiros** a partir dos cálculos realizados em um
Fechamento de Condomínio Individualizado.

Ao gerar os lançamentos, a situação das despesas relacionadas à subunidade selecionada será alterada de
*Calculado* para *Integrado*.

É possível selecionar uma ou mais subunidades para a geração simultânea dos lançamentos.

# ⚙️ Pré-Condições

* Empreendimento com **Parâmetros de Integração Financeira** associados.
  + Caminho:
    *TOTVS Incorporação > Condomínio > Empreendimento > Fechamento > Parâmetros de Integração Financeira*
* Subunidade com **Status = Calculado**.
  + Para atingir esse status, é necessário executar ao menos um cálculo através do processo
    [Apurar Condomínio](https://tdn.totvs.com/pages/viewpage.action?pageId=852299397).
* As despesas calculadas devem possuir **Item de Cobrança** associado.
  [Veja a documentação](https://tdn.totvs.com/pages/viewpage.action?pageId=435105029).

# ▶️ Como Utilizar

1. Selecione o fechamento desejado;
2. No menu de processos, selecione **Gerar Lançamento Financeiro**;
3. Informe a **Data de Vencimento** e defina os agrupamentos desejados.
   A prioridade considera sempre o Cliente/Fornecedor.
4. Opções de agrupamento:
   * Cliente/Fornecedor
   * Cliente/Fornecedor e Cálculo
   * Cliente/Fornecedor e Subunidade
   * Cliente/Fornecedor e Item de Cobrança
   * Cliente/Fornecedor, Subunidade e Cálculo
   * Cliente/Fornecedor, Subunidade e Item de Cobrança
   * Cliente/Fornecedor, Subunidade, Cálculo e Item de Cobrança
5. Avance o processo;
6. Os lançamentos serão gerados conforme os cálculos do fechamento;
7. O fechamento terá o status alterado para **Integrado**;
8. As despesas relacionadas também terão o status atualizado para **Integrado**.

### ⚠️ Regra de Negócio: Comportamento das Opções de Agrupamento

Ao utilizar as opções **"Agrupar Cliente/Fornecedor"**,
**"Agrupar cliente/fornecedor e cálculo"** ou
**"Agrupar cliente/fornecedor e item de cobrança"**, o sistema aplicará as seguintes regras com base nos Contratos de Locação:

* **Registros COM Contrato de Locação:** Caso existam contratos de locação preenchidos e eles sejam diferentes entre si, **será gerado um lançamento financeiro exclusivo para cada contrato**. O sistema impede a unificação de contratos distintos no mesmo lançamento para preservar a individualidade das cobranças.
* **Registros SEM Contrato de Locação:** Se os registros de condomínio não possuírem nenhum contrato vinculado os valores serão gerados em um único lançamento financeiro de acordo com o agrupamento escolhido.

| Cenário | Critério de Agrupamento | Resultado Esperado |
| --- | --- | --- |
| Contratos de locação **diferentes** selecionados | Qualquer opção por Cliente/Fornecedor | Um lançamento financeiro para cada contrato (não agrupa). |
| Condomínios **sem contrato** vinculados | Qualquer opção por Cliente/Fornecedor | Um único lançamento financeiro consolidando os registros. |
