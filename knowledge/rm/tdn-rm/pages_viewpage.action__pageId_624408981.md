---
content_hash: a87e037084f2983642e565eca30b4fb663b9a085d21ce50bb3c6e7fd1eaeda09
fetched_at: '2026-06-29T00:11:03.564238+00:00'
page_id: '624408981'
product: rm
source: tdn-rm
title: Demonstrações Contábeis | Gerar Estrutura de Demonstrações Contábeis a partir
  do Plano de Contas Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=624408981
version: 19
---

Gerado através do menu de Processos | Gerar Estrutura de Demonstrações Contábeis a partir do Plano de Contas Contábil, possibilita a criação da Estrutura de Demonstrações Contábeis a partir de um Plano de Contas Contábil.

Nesse processo é necessário informar:

* **Coligada** de onde se quer utilizar o Plano de Contas Contábil para geração dos Fatos Contábeis
* **Código** e **Descrição**para nova Estrutura de Demonstrações que será criada
* **Grupos de Contas** que serão utilizados no processo. Para cada grupo de conta é possível definir a Origem do Valor da demonstração, mas vale ressaltar que o processo considera apenas as Contas Contábeis dos grupos com Origem de Valor diferente de "Não se Aplica".

**Importante:** Quando a **Coligada** do Plano de Contas Contábil selecionada **for a do contexto**, o processo irá associar os fatos criados as contas da coligada de forma automática.

540332

**Opções:**

* **Grau das Contas Contábeis**, marcando essa opção, as contas que serão utilizadas para gerar a estrutura serão apenas aquelas que estão de acordo com o nível selecionado. Caso selecione um nível que só tenha contas sintéticas, a última conta será exibida como analítica/fato contábil e assim permitirá associar outras contas.
* Ao marcar a opção **Estrutura Consolidada**, o processo criará uma Coluna para cada empresa participante do Grupo Empresarial escolhido além da sua Holding e, também, as colunas de Total Combinado, Eliminações a Débito, Eliminações a Crédito e Saldo Consolidado.
* Caso marque a opção **Associar Contas Contábeis em todas as Coligadas através do Código da Conta**, o processo também associará as contas que existirem com o mesmo Código nas colunas das empresas participantes do Grupo Empresarial de forma automática (independente se o plano de contas contábil selecionado for o da **coligada do contexto** ou não).

Após a execução do processo será gerada uma nova estrutura de demonstrações que está pronta para ser configurada e utilizada para geração do relatório de Demonstrações Contábeis.

Atenção

No campo **Grupo Empresarial** estarão disponíveis para seleção apenas os Grupos Empresariais cuja Coligada do Contexto seja a Holding ou seja Investidora de alguma outra Coligada dentro do grupo.
