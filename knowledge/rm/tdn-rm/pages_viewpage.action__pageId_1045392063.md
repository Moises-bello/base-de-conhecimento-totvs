---
content_hash: cb2770ec002f4211be2ec1825ada06333d8c19447d26ab5a0359313d2c92f4a4
fetched_at: '2026-06-29T00:05:50.923305+00:00'
page_id: '1045392063'
product: rm
source: tdn-rm
title: Novidades 12.1.2606 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1045392063
version: 6
---

### Venda

---

* **Reajuste de Vendas Revitalizado:** 

  A documentação da funcionalidade **Reajuste de Vendas Revitalizado (TCGI CORE)** já está disponível.

  Consulte o material para conhecer as novidades, requisitos, parametrizações e o passo a passo de utilização.. [Clique Aqui para saber mais.](https://tdn.totvs.com/display/public/LRM/Reajuste+de+Vendas+-+Revitalizado)
* **Reforma Tributária – TCGI CORE Incorporadora:** 

  A documentação da **Reforma Tributária** para o **TCGI CORE Incorporadora** já está disponível.

  Neste material você encontrará as principais alterações implementadas, impactos nos processos da incorporadora, novas regras de negócio, parametrizações e orientações para utilização das funcionalidades relacionadas à adequação ao novo modelo tributário.

  **Acesse a documentação completa:** . [Clique Aqui para saber mais](https://tdn.totvs.com/pages/viewpage.action?pageId=1025239488)[.](https://tdn.totvs.com/display/public/LRM/Reajuste+de+Vendas+-+Revitalizado)
* **Integração com o RD Station Marketing:** 

  Agora o **RM TCGI Vendas** conta com integração com o **RD Station Marketing**, permitindo o envio automático de dados de clientes e contratos para a plataforma. Com essa integração, é possível potencializar campanhas de marketing, automatizar a nutrição de leads e acompanhar a evolução do funil de vendas de forma mais eficiente.

  A configuração é realizada por meio de um assistente no próprio RM, tornando a implantação simples e padronizada. Além disso, a integração é orientada a eventos, garantindo que as informações sejam enviadas automaticamente sempre que ocorrerem alterações relevantes, mantendo o RD Station sempre sincronizado com o status mais atualizado dos clientes e contratos.

  **Acesse a documentação completa:** **.**

### Aluguel

---

**REFORMA TRIBUTÁRIA. Para saber mais sobre os tópicos listados abaixo, consulte nossa documentação:**

**Movimentação e Gestão de Contratos de Locação**

* **Geração e Visão:** Desenvolvimento de rotinas para a geração de movimentos em contratos de locação e implementação de uma visão/tela para acompanhar esses movimentos gerados.
* **Cancelamento e Consistência:** Implementação da funcionalidade de cancelamento de movimento de locação de imóveis e criação de uma regra de consistência para o cancelamento de baixa quando houver um movimento de locação já gerado.

**Tributação (CBS e IBS) no Lançamento Financeiro**

* **Tipos de Aluguel:** Aplicação e validação da tributação de CBS e IBS em diferentes cenários de lançamento financeiro, abrangendo o aluguel complementar e o aluguel em dobro

**Regras de Negócio e Bloqueios**

* **Controle de Duplicidade:** Implementação de uma trava de segurança para o bloqueio de regra redutora social duplicada para aluguel

### Shopping

---

**CONFISSÃO DE DÍVIDA. Para saber mais sobre os tópicos listados abaixo, consulte nossa documentação:**

**Automação e Integração de Baixas**

* **Integração de Movimentações:** Implementação da rotina de integração automática tanto para a baixa de valores na Confissão de Dívida quanto para o cancelamento dessa baixa.

**Gestão de Valores, Descontos e Acréscimos**

* **Flexibilidade em Descontos:** Criação de uma opção específica para permitir descontar juros e/ou multas de forma separada no processo de Confissão de Dívida.
* **Segregação de Saldos:** Desenvolvimento da separação física e contábil do acréscimo e do desconto em relação ao valor original do contrato.
* **Desmembramento de Encargos:** Implementação da rotina para separar os juros e a multa de maneira individualizada no módulo de Confissão de Dívida.

**Parametrização do Sistema**

* **Configuração de Origem:** Criação de parâmetros para a integração financeira segmentados por origem, abrangendo tanto a estrutura de cadastros quanto a execução de processos.

**NEGOCIAÇÃO DE BOLETOS. Para saber mais sobre os tópicos listados abaixo, consulte nossa documentação:**

**Configuração e Parametrização**

* **Regras de Negócio:** Definição da estrutura e dos parâmetros necessários para a configuração geral da negociação de boletos.
* **Valores de Integração:** Definição dos parâmetros que controlam os valores financeiros que serão enviados e integrados entre os lançamentos dos boletos no Financeiro.

**Execução e Ciclo de Vida da Negociação**

* **Abertura e Criação:** Desenvolvimento do processo inicial para criar a negociação de boletos.
* **Efetivação:** Implementação da rotina para efetivar a negociação, consolidando os novos termos acordados.
* **Conclusão:** Criação da etapa de encerramento positivo, marcando o processo como concluído.
* **Cancelamento e Revisão:** Desenvolvimento das rotinas para cancelar uma negociação em andamento ou renegociar o saldo restante de um acordo pré-existente.

**Movimentações Financeiras (Baixas)**

* **Liquidação:** Implementação do processo de baixa do lançamento financeiro atrelado ao boleto negociado.
* **Estorno:** Criação da rotina de segurança para o cancelamento de baixa do lançamento, permitindo reverter a liquidação caso necessário.

### Portal de Imóveis

---

• **Mapa de Disponibilidade Revitalizado:** A documentação da nova visão do Mapa de Disponibilidade Revitalizado já está disponível. A funcionalidade foi reformulada para combinar um painel de cards interativos com o mapeamento visual do empreendimento, maior agilidade nas simulações de vendas. Acesse a documentação completa: [Clique Aqui para saber mais.](https://tdn.totvs.com/display/LRM/Empreendimentos+-+Mapa+de+disponibilidade+revitalizado)

• **Assinatura do TAE em Proposta e Impressão Padrão:** Desenvolvimento de melhoria para possibilitar a execução do fluxo de assinatura digital por meio do TOTVS Assinatura Eletrônica (TAE) diretamente a partir da visão de propostas, além de disponibilizar a opção para a emissão da minuta padrão do sistema. Acesse a documentação: [Clique Aqui para saber mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=572197716)

• **Inclusão Automática de Documentos da Unidade no Envelope do TAE:** Implementada a funcionalidade que permite incluir de forma automática no envelope do TOTVS Assinatura Eletrônica (TAE) os documentos que foram previamente vinculados à unidade. Essa automação otimiza a jornada do corretor e elimina falhas operacionais humanas, mitigando o risco de download ou anexo incorreto de arquivos durante a formalização do contrato. Acesse a documentação completa: [Clique Aqui para saber mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=563947962)

• **Download Unificado no menu Documentos da Pessoa:** Promovida a evolução de igualdade de recursos entre as visões do sistema. Agora, o menu de Documentos da Pessoa passa a contar com a opção de baixar todos os arquivos anexados de uma única vez (Download em lote), fornecendo a mesma flexibilidade e agilidade que já eram disponibilizadas nativamente no menu de Documentos da Proposta. Acesse a documentação completa: [Clique Aqui para saber mais.](https://tdn.totvs.com/display/LRM/Propostas+-+Documentos+da+Pessoa)
