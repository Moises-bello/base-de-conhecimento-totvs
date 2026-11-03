---
content_hash: 582a53d042ce9a2747b0d20257e8ff49498eb884e3b3b2d955a7f573067c2362
fetched_at: '2026-06-29T00:09:15.633413+00:00'
page_id: '421385430'
product: rm
source: tdn-rm
title: Integração TOTVS Aprovações e Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385430
version: 50
---

---

A utilização da Integração com o TOTVS Aprovações e Atendimento permite que sejam criados atendimentos para aprovação originados do TOTVS Obras e Projetos ou no .

Esses atendimentos poderão ser aprovados/reprovados no  ou no TOTVS Aprovações e Atendimento, quando realizadas as seguintes parametrizações:

**Configurações Gerais**

**Status para Aprovação**

Define qual o status do atendimento no TOTVS Aprovações e Atendimento TOTVS Aprovações e Atendimento TAA (Antigo Agilis) é considerado como ***Aprovado*** no TCOP. É a partir dessa parametrização, que o sistema permitirá a criação/alteração de contratos, a liberação dos períodos de medição de contratos, a geração de movimentos de pedidos e pedidos extra no backoffice, bem como a alteração de fase de projetos.

**Status para Reprovação**

Define o status do atendimento no TOTVS Aprovações e Atendimento TAA (Antigo Agilis)  que deverá ser considerado como ***Reprovado*** no TCOP, impedindo que se efetive ou possibilitando ajustes na criação/alteração de contratos, a liberação dos períodos de medição de contratos, a geração de movimentos de pedidos e pedidos extra no backoffice, bem como a alteração de fase de projetos.

**Coligada Centralizadora**

O preenchimento da Coligada Centralizadora, determina que todos os atendimentos gerados através da integração TCOP com o TAA serão criados na coligada informada, independente da coligada de origem do contrato, pedido, pedido extra ou projeto, assim todas as aprovações ficam centralizadas somente em uma coligada.

Caso o campo não esteja preenchido, os atendimentos serão gerados na coligada em que o usuário que solicitou a aprovação estiver logado.

As parametrizações acima refletem nos workflows de aprovação que serão gerados pelos processos que estiverem assinalados abaixo:

**Contrato**

**Contrato e****Aditivo**

Ativa a integração com TAA  TOTVS Aprovações e Atendimento (antigo RMAgilis)  para aprovar associação de itens ao contrato , associação de itens ao aditivo . [Aditivos Contratuais](https://tdn.totvs.com/x/udMdGQ),

Após a aprovação do workflow o contrato ou aditivo será avançado automaticamente para o status "Em andamento" consequentemente os itens poderão ser utilizados para medições ou em caso de aditivos de data a data de prorrogação do termino do contrato será aplicada ao contrato.

**Liberação de Períodos**

Ativa a integração com TAA na aprovação/reprovação da liberação de períodos do contrato.

Somente após a aprovação workflow é possível executar os processos de liberar no TOTVS Construção Obras e Projetos ou  [Gerar Integração com Suprimentos/Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=421385502)

**Adiantamento**

Ativa a integração TCOP com o TAA para aprovar a inclusão  de um adiantamento de contrato. [Adiantamento](https://tdn.totvs.com/display/LRM/Adiantamento+de+Contrato)

Somente após a aprovação do workflow é possível executar os processos: Liberação e cancelamento de liberação de adiantamentos de contrato.

**Faturamento Direto**

Ativa a integração TCOP com o TAA para aprovar a inclusão  de um pedido de  de contrato.

Somente após a aprovação do workflow é possível gerar o pedido para Suprimento/Faturamento.

Mais detalhes sobre o WorkFlow gerado para o período podem ser consultados no anexo: 

**Requisição de Material**

**Pedido de Material**

Ativa a integração TCOP com o TAA para aprovar a inclusão de um pedido de compra. [Geração de Pedidos](https://tdn.totvs.com/pages/viewpage.action?pageId=421385492)

Somente após a aprovação do workflow é possível executar os processos: [Envia pedido para Suprimento e Faturamento Gerando apenas 1 (um) Movimento](https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+apenas+1+%28um%29+movimento) , [Envia pedido para Suprimento e Faturamento Gerando 1 Movimento por Data de Entrega](https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+Movimento+por+Data). 

É importante salientar que a rotina de aprovação de Pedidos de Materiais integrada ao TOTVS Aprovações e Atendimento não se encontra disponível no Portal de Obras, ou seja, somente se aplica a Pedidos de Materiais gerados no TOTVS Construção Obras e Projetos. A implementação dessa funcionalidade no Portal de Obras será realizada em breve.

**Pedido Extra**

Ativa a integração TCOP com o TAA para aprovar a inclusão de um pedido de compra. [Geração de Pedido Extra](https://tdn.totvs.com/pages/viewpage.action?pageId=421385494&moved=true)

Somente após a aprovação do workflow é possível executar os processos: [Envia pedido para Suprimento e Faturamento Gerando apenas 1 (um) Movimento](https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+apenas+1+%28um%29+movimento) , [Envia pedido para Suprimento e Faturamento Gerando 1 Movimento por Data de Entrega](https://tdn.totvs.com/display/LRM/Envia+pedido+para+Suprimento+e+Faturamento+gerando+Movimento+por+Data). 

É importante salientar que a rotina de aprovação de Pedidos de Materiais integrada ao TOTVS Aprovações e Atendimento não se encontra disponível no Portal de Obras, ou seja, somente se aplica a Pedidos de Materiais gerados no TOTVS Construção Obras e Projetos. A implementação dessa funcionalidade no Portal de Obras será realizada em breve.

**Tipo de Atendimento**

Para cada funcionalidade selecionada acima, serão incluídos workflows no TAA, utilizando o **Tipo de Atendimento** informado.

A informação do tipo de atendimento é obrigatória, caso o processo relacionado esteja marcado.

O mesmo tipo de atendimento pode ser informado como tipo de atendimento de mais de uma  funcionalidade.

Para mais detalhes de tipo de atendimento veja em : [Tipo de atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459518)

Para geração do atendimento a partir do TOTVS Obras e Projetos, será necessário que o usuário esteja vinculado a um atendente do TOTVS Aprovações e Atendimento. Caso o envio para aprovação, seja realizado através do Portal de Medição de Contrato para Fornecedor, o atendimento será gerado a partir do atendente cadastrado para no

**Observação:**

Quando o projeto em execução estiver utilizando, integração com Fluig, [WorkFlow - Construção e Projetos](https://tdn.totvs.com/pages/viewpage.action?pageId=173083240) **,** não será possível utilizar  essa funcionalidade portanto os parâmetros estarão desabilitados .
