---
content_hash: c90a241800d40f03c8259fc876f87648caf76c7a7ec6f547cb3e3346623b60a8
fetched_at: '2026-06-29T00:11:33.269819+00:00'
page_id: '754954317'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Relatórios - Cobrança de Fundo
  Promocional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754954317
version: 8
---

Este relatório foi desenvolvido exclusivamente para uso no Smart View e estará disponível a partir da versão 12.1.2306! Para saber mais sobre o Smart View e como instalá-lo**, [clique aqui!](https://tdn.totvs.com.br/pages/viewpage.action?pageId=626926739)**

---

## **Introdução**

---

Este relatório tem como objetivo analisar a eficácia (ROI) do fundo promocional no aumento das vendas do shopping center durante um período de referencia.

A sigla ROI significa "Return on Investment", em português "Retorno sobre Investimento".

É uma métrica utilizada para medir a eficiência de um investimento, mostrando o quanto de lucro ou prejuízo foi gerado em relação ao valor investido. O cálculo do ROI é feito dividindo-se o lucro obtido pelo investimento pelo valor investido. Esse resultado é então expresso em porcentagem ou valor decimal, indicando o retorno em relação ao investimento realizado. O ROI é uma ferramenta importante para avaliar o desempenho financeiro de um projeto, campanha de marketing ou investimento empresarial. Ao comparar o ROI de diferentes projetos ou investimentos, é possível identificar quais são mais rentáveis e, assim, tomar decisões mais estratégicas em relação ao uso dos recursos financeiros da empresa.

##### Cálculo do ROI

---

Exemplo do cálculo ROI

Período de Referência:

* Fundo Promocional total no período de R$ 50.000,00
* Faturamento total no período de R$ 250.000,00.

Período de Análise:

* Fundo Promocional total no período de R$ 80.000,00
* Faturamento total no período de R$ 220.000,00.

Referência (Fundo/Faturamento) = (50.000,00/250.000,00) = 0,2   
Análise (Fundo/Faturamento) = (80.000,00/220.000,00.) = 0,36

0,2 / 0,36 = 0,55

ROI = 0,55-1 = -0,45%

## **Procedimentos para utilização**

---

Ao carregar o relatório, devemos primeiramente definir um filtro para geração do mesmo. Este filtro é composto dos seguintes campos, explicados abaixo:

Parâmetros de Visualização: O relatório conta com os seguintes parâmetros de visualização, auto explicativos, sendo imprescindível preencher as informações do período de referência e do período de análise.

* Período Inicial Referência
* Período Final Referência
* Período Inicial Comparativo
* Período Final Comparativo

Empreendimento: Permite seleciona um ou mais empreendimentos (caso não esteja vinculado a visão de Empreendimentos). Facilitando a visão do relatório filtrando apenas os dados relevantes ao empreendimento ou empreendimentos selecionados.

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
