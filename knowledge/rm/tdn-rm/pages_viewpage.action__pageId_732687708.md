---
content_hash: 963e165a1f82ed10c8d7a1b25c5eff8a66cdc71ca0e9db52540e0f6e8bc0bf10
fetched_at: '2026-06-29T00:11:28.644536+00:00'
page_id: '732687708'
product: rm
source: tdn-rm
title: Tributos (Movimento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=732687708
version: 14
---

**Visão Geral:**

A tela **Tributos do Movimento** apresenta os impostos incidentes sobre o movimento selecionado, permitindo a visualização, cálculo automático e eventual edição dos valores.

A tela é dividida em duas áreas principais:

1. **Grid de Tributos (parte superior):** lista os tributos aplicáveis ao movimento, mostrando:

   * **Código do Tributo**
   * **Base de Cálculo**
   * **Alíquota**
   * **Valor**
   * **Manter Valor**

Clique aqui para expandir

1. **Detalhamento do Tributo (parte inferior):** exibe informações complementares e campos específicos de acordo com o tributo selecionado na grid.  
   Essa área é **dinâmica** e se adapta ao tributo em destaque (por exemplo, CBS, IBS, ICMS).

Exemplo: O campo Beneficiário é visível apenas para o tributo COSIRF (Este campo está disponível a partir da versão 12.1.2602.XXX e fica disponível após atualização da base de dados).

Clique aqui para expandir

1. **Preenchimento de dados dos tributos IBS/CBS:**

Ao definir o produto os tributos são carregados de acordo com a parametrização do tipo de movimento.

Ao selecionar a "Regra tributária" os tributos IBS/CBS, caso existam como tributos do movimento, tem suas informações recuperadas e preenchidas preenchidas (CST/Situação tributária, Classificação tributária, Percentual de redução de alíquota, Código de crédito presumido, Percentual de crédito presumido e Percentual de diferimento) e os valores são calculados (Valor crédito presumido, Valor diferido e Alíquota). A Regra Tributária será selecionada da aba Fiscal do primeiro Item de Movimento. 

A atualização dos campos de percentuais destes tributos também acionam o recálculo dos respectivos valores destes percentuais. Tais valores são calculados conforme o valor da base de cálculo.

**Natureza de Rendimento:**

Disponível a partir da versão: 12.1.2205.

**Gestão Fiscal**

Cadastre as naturezas de rendimento em:  Cadastros - Mais - Natureza de rendimento.

**Gestão de Compras, Estoque e Faturamento**

**Movimento:**

Ao acessar o movimento - Aba Tributos e Valores - Menu: Tributos. Preencher o campo clicando na "seta" e selecione a natureza de rendimento.

**Parâmetros do tipo de movimento:**

É possível parametrizar um valor default para o campo nos parâmetros do tipo de movimento.  
  
Ao informar o item de movimento, o sistema irá considerar a seguinte ordem de prioridade para preenchimento da Natureza de Rendimento, do item:  
1 - Natureza de Rendimento informada no Anexo - Dados Fiscais do Produto;  
2 - Natureza de Rendimento informada no Anexo - Tributos Defaults de Cli/For;  
3 - Natureza de Rendimento informada no parâmetro do tipo de movimento.  
  
Obs: Esta regra é considerada para os tributos **PISRF**, **COFINSRF**, **COSIRF**, **CSLLRF**, **CSRF**e **IRRF Importação**.

Consumindo WebService

Natureza de Rendimento <IDNATRENDIMENTO></IDNATRENDIMENTO>

O campo possui relacionamento com a tabela DNATUREZARENDIMENTO. Desta forma, só podem ser informados valores de IDNATRENDIMENTO, que estejam na tabela DNATUREZARENDIMENTO.

**Importante:** Para utilização do campo é necessário que a base de dados esteja atualizada (RM Atualizador).

**Pauta por Produto (Alíquota AD REM ou Alíquota Fixa)**

É possível parametrizar a tributação do movimento para buscar a Alíquota AD REM. Para isso, acesse a parametrização do tipo de movimento desejado e vá para a etapa 64: "**Fis - Tributação - Item**".  
No campo "Procurar Alíquota Em", informe "**Pauta por Produto**".

A parametrização por pauta tem prioridade sobre as outras. Por exemplo, caso no cadastro do tributo seja informada a busca de alíquota por outra opção, e no tipo do movimento seja informada a busca pela pauta do produto, a alíquota informada no item do movimento será aquela cadastrada na pauta do produto.
