---
content_hash: 9fe87e6a7e10486cd4393e03afa31903c70cbe8bb8497b9f55d7340ec8933520
fetched_at: '2026-06-29T00:05:49.169462+00:00'
page_id: '1039016360'
product: rm
source: tdn-rm
title: Alto Custo - Controle e Autorização de Itens
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1039016360
version: 8
---

Informações Importantes!

**Configuração Contratual:** A configuração de alto custo deve estar alinhada com o contrato vigente com a operadora. Alterações nos valores ou no tipo de controle devem ser precedidas de aprovação contratual para evitar glosas no faturamento.

* ✅ O sistema possui dois modos para identificar o alto custo, modo unificado (legado) e modo individual.
* ✅ As regras do Alto custo integram-se com as regras de restrições contratuais existentes, não gerando duplicidades na autorização.
* ✅ Os itens identificados como Alto Custo, serão enviados ao serviço padrão de Central de Autorizações

**Impacto nas Configurações** Todos os processos compartilham a mesma base de informações sobre alto custo e autorizações. Alterações nas configurações de alto custo afetam imediatamente todos os módulos integrados. É fundamental que a parametrização esteja correta antes de liberar prescrições.

**Regras Operacionais**

* Não há "pré-aprovação" de tratamentos: cada dia requer nova autorização
* Medicamentos contínuos exigem prescrição e autorização diárias
* A operadora pode autorizar no dia 1 e negar no dia 2 (mesmo item)
* Comunicação entre setores (Guias/Assistencial/Faturamento) é crítica
* Documentação das ações tomadas é obrigatória para auditoria

## **CONTEÚDO**

**2CONTEÚDO**

## **01.** **Visão Geral**

O controle de alto custo permite que hospitais e operadoras de saúde estabeleçam limites de valor para materiais, medicamentos, órteses e próteses que requerem autorização prévia. Esta funcionalidade garante que itens que ultrapassem valores pré-estabelecidos sejam automaticamente encaminhados para análise e autorização antes da sua utilização.

## **02. Tipo de Alto Custo**

Para efetuar a configuração do alto custo, deve-se acessar as condições contratuais, em Cadastros > Faturamento > Condições Contratuais.

Em seguida acessar Parâmetros 3 > MatMed > Alto Custo.

O sistema oferece duas modalidades de controle de alto custo:

### Unificado (Padrão)

Utiliza um único valor limite para todos os tipos de item (material, medicamento, órtese e prótese). Mantém o comportamento tradicional do sistema.

### Individual

Permite configurar valores distintos por tipo de item, possibilitando controle mais granular conforme negociações específicas com cada operadora.

**Importante:** Ao alterar o tipo de alto custo, os valores anteriormente configurados são automaticamente zerados.

## **03. Configurações de Valores**

Para configurar os valores de alto custo:

1. 1. Acesse **Cadastros > Faturamento > Condições Contratuais com Convênios**
   2. Selecione o contrato do convênio desejado
   3. Acesse a aba **Parâmetros 3 > aba MatMed**
   4. Localize a seção **Alto Custo**
   5. Selecione o **Tipo de Alto Custo** (Unificado ou Individual)
   6. Preencha os valores conforme o tipo selecionado

## **04. Modo Unificado**

Quando configurado como Unificado:

* + Um único campo de valor é apresentado
  + Todos os tipos de item (material, medicamento, órtese, prótese) são avaliados contra este valor único
  + Qualquer item que ultrapasse este valor é identificado como alto custo
  + Mantém compatibilidade com configurações legadas

**Exemplo:** Se o valor unificado for R$ 5.000,00, qualquer medicamento, material, órtese ou prótese acima deste valor será considerado alto custo.

## **05. Modo Individual**

Quando configurado como Individual:

* + Quatro campos de valor são apresentados:
    - Valor Alto Custo Material
    - Valor Alto Custo Medicamento
    - Valor Alto Custo Órtese
    - Valor Alto Custo Prótese
  + Cada tipo de item é avaliado contra seu valor específico
  + Permite controle diferenciado por categoria

**Exemplo:**

* + Material: R$ 3.000,00
  + Medicamento: R$ 8.000,00
  + Órtese: R$ 10.000,00
  + Prótese: R$ 15.000,00

## **06. Regras de Identificação**

A identificação de alto custo ocorre no momento da **liberação da prescrição pelo médico**.

Para isso, no prontuário eletrônico, acessar o prontuário do paciente > Prescrições > Médicas > + Novo (para incluir uma nova prescrição) > "+" em Medicamentos.

Em seguida, após informar o medicamento, será exibido um alerta, informando que o mesmo possui alto custo.

### Processo de Avaliação

1. 1. Médico libera a prescrição
   2. Sistema verifica a configuração de alto custo do convênio
   3. Para cada item prescrito:
      * Identifica o tipo do item (material, medicamento, órtese, prótese)
      * Busca o valor de alto custo correspondente
      * Compara o valor do item com o limite configurado
      * Se ultrapassar, marca o item como alto custo

### Critérios de Comparação

**Modo Unificado:**

* + Valor do item > Valor Alto Custo Unificado

**Modo Individual:**

* + Valor do material > Valor Alto Custo Material
  + Valor do medicamento > Valor Alto Custo Medicamento
  + Valor da órtese > Valor Alto Custo Órtese
  + Valor da prótese > Valor Alto Custo Prótese

## **07. Envio para Central de Autorizações**

### Características do Envio

* + **Por Item:** Cada item identificado é enviado individualmente
  + **Por Prescrição:** Considerando a validade de 24 horas
  + **Integrado:** Combina itens de alto custo com restrições contratuais
  + **Sem Duplicação:** Itens que se enquadram em ambas as regras são enviados apenas uma vez

### Processo

1. 1. Item identificado como alto custo ou com restrição contratual
   2. Sistema envia automaticamente para a Central de Autorizações
   3. Aguarda retorno da autorização
   4. Disponibiliza o item apenas após liberação

Para que o item de Alto Custo seja gerado na Central de Autorizações, é necessário estar marcada a configuração "**Incluir na Central de Autorizações**"

## **08. Restrições Contratuais**

A funcionalidade de alto custo trabalha em conjunto com as restrições contratuais já existentes.

### Restrições que Exigem Autorização

Localizadas em: **Cadastros > Faturamento > Condições Contratuais > Anexo > Restrições de Contrato**

* + Exige Liberação de Convênio
  + Exige Liberação de Responsáveis

### Integração

O sistema consolida:

* + Itens identificados por alto custo
  + Itens com restrição contratual que exigem autorização

Ambos são enviados para a Central de Autorizações através do mesmo fluxo, evitando envios duplicados.

## **09. Parâmetros Complementares**

Dois parâmetros adicionais controlam o comportamento da autorização:

**Necessita Justificativa**

* + Quando ativo, exige que o médico justifique a prescrição do item de alto custo
  + Justificativa é enviada junto com a solicitação de autorização

**Inclui na Central de Autorizações**

* + Controla se o item será enviado automaticamente para autorização
  + Permite configurar itens de alto custo que não necessitam autorização prévia

## **10. Processos Interligados**

O controle de alto custo opera de forma integrada com quatro processos essenciais do sistema, criando um fluxo contínuo desde a prescrição médica até o faturamento final. Esta integração garante que as regras de autorização sejam aplicadas consistentemente em todos os pontos do sistema, evitando divergências e garantindo conformidade contratual.

A **Central de Autorizações** atua como o hub central de comunicação com as operadoras, recebendo automaticamente as solicitações geradas pela prescrição médica e gerenciando todo o ciclo de vida das autorizações. A **Prescrição Médica** é o ponto de entrada do processo, onde a identificação de itens de alto custo ocorre no momento da liberação pelo médico. As **Condições Contratuais com Convênios** fornecem os parâmetros que determinam quais itens serão considerados alto custo e como serão tratados. Por fim, a **Elaboração de Contas** consolida todos os lançamentos e valida se os itens autorizados podem ser faturados, impedindo o fechamento de contas com pendências de autorização.

Esta arquitetura integrada elimina a necessidade de controles manuais paralelos e garante que todos os setores trabalhem com as mesmas informações em tempo real, desde o corpo clínico até o faturamento.

## **11. Central de Autorizações**

**Descrição:** Módulo responsável por gerenciar solicitações de autorização junto às operadoras de saúde.

**Documentação:** [Central de Autorizações](https://tdn.totvs.com/x/HDMjMg)

**Integração com Alto Custo:**

* + Recebe automaticamente itens identificados como alto custo
  + Consolida solicitações de itens com restrição contratual
  + Gerencia o ciclo de vida das autorizações (solicitado, autorizado, negado)
  + Controla prazos de validade das autorizações
  + Permite acompanhamento em tempo real do status das solicitações

**Fluxo:**

1. 1. Item de alto custo identificado na prescrição
   2. Enviado automaticamente para Central de Autorizações
   3. Operadora analisa e retorna aprovação/negação
   4. Sistema libera ou bloqueia o uso do item conforme retorno

## **12. Prescrição Médica e Validação**

**Descrição:** Módulo onde médicos registram prescrições de materiais, medicamentos, órteses e próteses para pacientes.

**Documentação:** [Prescrição Médica](https://tdn.totvs.com/x/xBYCMQ)

**Integração com Alto Custo:**

* + Ponto de identificação inicial dos itens de alto custo
  + Validação ocorre no momento da liberação da prescrição
  + Aplica regras de alto custo configuradas no convênio do paciente
  + Exibe alertas visuais para itens que necessitam autorização

**Comportamento:**

* + **Modo Unificado:** Avalia todos os itens contra valor único
  + **Modo Individual:** Avalia cada tipo de item contra seu valor específico
  + **Validade:** Prescrições têm validade de 24 horas
  + **Justificativa:** Se parametrizado, exige justificativa do médico para itens de alto custo

**Indicadores Visuais:**

* + Ícone de alerta para itens pendentes de autorização
  + Ícone de bloqueio para itens não autorizados
  + Ícone de confirmação para itens autorizados

### Validade e Renovação

* + Prescrições têm validade de **24 horas**
  + Cada prescrição liberada gera uma nova solicitação de autorização
  + **Não há conceito de plano terapêutico**: cada prescrição é tratada isoladamente
  + Para tratamentos que se estendem por múltiplos dias, novas prescrições devem ser liberadas diariamente

**Exemplo Prático:**

## **13. Elaboração de Contas**

**Descrição:** Módulo de faturamento onde são consolidados e gerenciados todos os lançamentos realizados na conta do paciente durante seu atendimento.

**Localização:** Faturamento > Elaboração de Contas

**Impacto do Alto Custo:**

* + Itens de alto custo são incluídos na Parcial no momento do lançamento, independentemente do status de autorização
  + O sistema identifica automaticamente itens que necessitam autorização, marcando a coluna "Exige Liberação" como "Sim"
  + Durante o processo de encerramento da Parcial, o sistema valida o status de autorização de todos os itens marcados
  + Se houver itens com "Exige Liberação = Sim" sem autorização concedida, uma mensagem impeditiva é exibida, bloqueando o encerramento até que todos os itens estejam devidamente autorizados
  + Itens autorizados apresentam o número da autorização vinculado ao lançamento, garantindo rastreabilidade no faturamento

**Campos Relacionados:**

* + Exige Liberação (Sim/Não)
  + Número da Autorização
  + Status da Autorização
  + Data de Autorização
  + Operador que Autorizou

**Validações no Encerramento:**

1. 1. Sistema verifica todos os itens da Parcial
   2. Identifica itens com "Exige Liberação = Sim"
   3. Valida se possuem autorização válida
   4. Bloqueia encerramento se houver pendências
   5. Exibe mensagem com lista de itens não autorizados

## **14. Fluxo de Autorização**

**Fluxo Completo**

### Observações Importantes

* + Não há autorização de tratamentos completos neste escopo
  + Cada prescrição é tratada individualmente
  + Itens da mesma prescrição podem ter autorizações diferentes
  + Sistema mantém histórico de autorizações por item e prescrição

### Tratamento de Não Autorizações

Quando um item de alto custo não é autorizado pela operadora, o seguinte fluxo deve ser executado:

**Responsabilidade do Setor de Guias**

**Opção 1 - Substituição do Item:**

1. 1. Setor de Guias notifica o setor assistencial
   2. Setor assistencial avalia itens similares disponíveis
   3. Médico prescreve medicamento/material alternativo
   4. Nova prescrição passa pelo fluxo de autorização

**Opção 2 - Cobrança Particular:**

1. 1. Setor de Guias notifica o responsável pelo paciente
   2. Informa sobre a não autorização do convênio
   3. Apresenta opção de pagamento particular
   4. Obtém concordância formal do responsável
   5. Setor de Guias comunica o setor de faturamento
   6. Faturamento transfere o item da cobrança do convênio para Gastos Particulares na Parcial

**Fluxo de Comunicação**

### Cenários Comuns

**Cenário 1: Medicamento Não Autorizado - Substituição**

**Cenário 2: Material Não Autorizado - Particular**

### Registro e Rastreabilidade

Cada ciclo de prescrição mantém registro independente:

* + Data/hora da prescrição
  + Data/hora do envio para autorização
  + Data/hora do retorno (aprovação/negação)
  + Ações tomadas em caso de negação
  + Responsável pelas ações

### Impacto no Faturamento

**Itens Autorizados:**

* + Lançados normalmente na conta do convênio
  + Número de autorização vinculado ao lançamento
  + Uma autorização por prescrição diária

**Itens Não Autorizados:**

* + **Se substituídos:** Item original não cobrado, alternativa faturada
  + **Se particulares:** Transferido para gastos particulares com autorização do responsável
