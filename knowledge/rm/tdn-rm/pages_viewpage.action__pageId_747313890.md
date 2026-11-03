---
content_hash: c14e27f38a3c7bbc804d5dcb612abc4036ed2c1347960b5cda3300e3186d9bc1
fetched_at: '2026-06-29T00:11:32.371092+00:00'
page_id: '747313890'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Relatórios - Despesas do Sócio
  Empreendedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=747313890
version: 16
---

Importante

Este relatório foi desenvolvido exclusivamente para uso no Smart View e estará disponível a partir da versão 12.1.2306! Para saber mais sobre o Smart View e como instalá-lo**, [clique aqui!](https://tdn.totvs.com.br/pages/viewpage.action?pageId=626926739)**

**O relatório está disponível apenas para fechamentos de condomínio do tipo Individualizado. Para entender como realizar o fechamento de condomínio dessa forma, [consulte a documentação aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=857578505)**

---

Em resumo, o relatório de despesas do sócio empreendedor apresenta informações relevantes como previsões de gastos, valores vencidos e recebidos, provenientes tanto de vacâncias quanto de outras fontes residuais. Trata-se de uma ferramenta valiosa para que o sócio empreendedor possa gerenciar suas finanças e tomar decisões estratégicas embasadas em informações precisas e atualizadas.

Este relatório irá exibir os dados por competência agrupados por Shopping e por Sócio empreendedor para cada mês/competência. Ele possui os seguintes filtros:

* Data de pagamento ou data base: Esta data irá considerar a data de baixa dos lançamentos para análise e retorno dos valores recebidos no intervalo de período informados.
* Data início: a partir de qual período será considerado para exibição os dados.
* Data fim: até qual período será considerado para exibição dos dados.
* Shoppings: lista com os shoppings (caso não esteja vinculado a visão de Empreendimentos) que serão retornados na análise.

Exemplo de como são exibidos os dados:

* O **valor previsto** de um determinado lançamento, equivale ao valor original do mesmo;
* O **valor vencido** equivale ao valor líquido na data de pagamento (Data Base) selecionada ao gerar o relatório;
* O **valor recebido** é a soma das baixas do lançamento até a data de pagamento (data base) selecionada ao gerar o relatório.

* Para saber mais sobre vacância [(Clique aqui)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680244548)
* Para saber mais sobre o cálculo residual [(Clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=435105013)

## **Como Acessar o Relatório**

---

Existem algumas formas de visualizar o relatório, dependendo de suas permissões e da configuração do sistema.

#### **Método 1: Acesso Direto (Requer Permissão)**

1. Navegue até o menu: `Shopping > Relatórios > SmartView`.
2. Selecione o relatório.

> **Nota:** O acesso a este menu é controlado por permissões. Caso a opção não esteja visível, por favor, contate o administrador do sistema para solicitar a liberação.

#### **Método 2: Acesso via Cadastro de Empreendimento**

1. Navegue até o menu: `Condomínio > Manutenção de Empreendimento > Empreendimento > Anexos > Relatórios`.
2. Selecione o relatório.

**O que fazer se o relatório não estiver listado?**

Caso o relatório não apareça nesta lista, você pode vinculá-lo manualmente seguindo os passos abaixo:

1. No Anexo Relatórios do empreendimento, clique no botão **"Inserir Relatório"**.
2. Siga as instruções do assistente de configuração (Wizard).
3. Na etapa **"Vínculo de Campos"**, configure o vínculo da seguinte forma:

   * **Nome do Campo:** `CODEMPREENDIMENTO`
   * **Valor:** `Empreendimento`
4. Conclua o assistente para salvar a configuração.
