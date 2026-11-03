---
content_hash: 386cfe341bf583d5eb60d5fabc460baa4abb8bcd27818caeea4342b4d0498a96
fetched_at: '2026-06-29T00:11:32.343750+00:00'
page_id: '746505358'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Relatórios - Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=746505358
version: 7
---

O relatório de Faturamento está disponível a partir da versão **12.1.2306,**utilizando a nova estrutura do **Smart View.**Para saber mais sobre o Smart View e como instalá-lo**, [clique aqui!](https://tdn.totvs.com.br/pages/viewpage.action?pageId=626926739)**

---

O faturamento de um shopping é um indicador crítico do desempenho financeiro de um empreendimento comercial. Ele representa a receita gerada pelas vendas de produtos e serviços nos estabelecimentos do shopping. A análise cuidadosa desses dados permite que os proprietários e gerentes de shopping possam avaliar a eficácia das estratégias de marketing e vendas, bem como identificar tendências e oportunidades de crescimento.

Este relatório irá exibir para cada mês o valor do faturamento de todas as lojas de cada shopping. Ele possui os seguintes filtros:

* Data início: a partir de qual competência será exibido os dados
* Data fim: até qual competência será exibido os dados
* Shoppings: lista com os shoppings que serão retornados na análise (caso não esteja vinculado a visão de Empreendimentos)

Para os shoppings terem os seus faturamentos analisados, o módulo de condomínio deverá estar integrado ao módulo de aluguel. O sistema irá percorrer todas as subunidades (lojas) do empreendimento (shopping) e analisar a sua integração com os imóveis (aluguel).

Para cada loja, o relatório irá somar o valor registrado no Faturamento 1 e Faturamento 2 da medição do Aluguel Complementar. O sistema irá utilizar a competência da medição para determinar em qual mês aquele faturamento estará situado na planilha.

Para as LUCs que não tiveram o registro de faturamento cadastrado, o relatório irá exibi-las com a situação "Não Apurado".

Segue um exemplo das informações que o relatório irá exibir:

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
