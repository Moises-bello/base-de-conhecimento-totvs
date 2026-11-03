---
content_hash: c8891e1e06c5bc69b04a333cefc9ee40700419d4d1a01fa13863adc9a3ed0f94
fetched_at: '2026-06-29T00:05:48.172782+00:00'
page_id: '1023307097'
product: rm
source: tdn-rm
title: Reforma Tributária - Parâmetros Tributários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1023307097
version: 4
---

## **Parâmetros Tributários**

Para viabilizar a correta parametrização e aplicação do IVA conforme a Reforma Tributária, o sistema passa a disponibilizar uma **tela específica para manutenção dos parâmetros do IVA**, com interface dedicada para configuração e controle dessas informações.

### Funcionalidade

Será criada uma **tela de parametrização** para definição dos parâmetros utilizados no tratamento do IVA, garantindo padronização e consistência no cálculo tributário dos movimentos do sistema.

### Informações parametrizadas

Na configuração dos parâmetros do IVA, deverão ser informados os seguintes dados:

* **Parâmetros do Movimento**

  + O tipo de movimento será **default**
  + Somente será permitido o **tipo de movimento 2.1.x**
* **TOTVS Fiscal**

  + ID da Regra Tributária Fiscal

    ## Regra Tributária Fiscal

    ### Objetivo

    Este documento tem como objetivo explicar as **Regras Tributárias Fiscais** aplicadas no TOTVS Construção Gestão de Imóveis, considerando as exigências da **Reforma Tributária**, garantindo conformidade legal, correta apuração dos tributos e segurança fiscal nos processos do negócio.

    ### Conceito de Regra Tributária Fiscal

    A Regra Tributária Fiscal define como o sistema deve:

    - Determinar a **base de cálculo dos tributos**;
    - Aplicar **alíquotas, redutores, isenções ou benefícios fiscais**;
    - Considerar o **tipo de operação e contrato**;
    - Atender às exigências legais vigentes no momento da emissão do documento fiscal.

    Essas regras são fundamentais para assegurar que o cálculo dos impostos esteja alinhado à legislação federal, estadual e municipal.

    ### Abrangência

    As regras tributárias fiscais podem ser aplicadas aos seguintes contextos:

    - **Contratos de Venda**
    - **Contratos de Aluguel**
    - **Condomínio / Empreendimento**
    - Movimentos financeiros e fiscais associados aos contratos

    ### Principais Elementos da Regra Fiscal

    Uma regra tributária fiscal pode considerar, entre outros, os seguintes parâmetros:

    - Tipo de contrato
    - Tipo de operação
    - Regime tributário
    - Base de cálculo do imposto
    - Alíquota aplicável
    - Redutores da base de cálculo (ex.: IVA)
    - Índices de atualização
    - Datas de vigência e competência

    ### Integração com a Reforma Tributária

    Com a Reforma Tributária, as regras fiscais passam a considerar novos conceitos, como:

    - **IVA (Imposto sobre Valor Agregado)**;
    - Regras de **transição tributária**;
    - Aplicação de **redutores legais** conforme o setor imobiliário;
    - Adequação automática dos cálculos conforme a legislação vigente.

    O correto cadastro das regras tributárias é essencial para garantir a conformidade fiscal e evitar inconsistências na apuração dos tributos.

    ### Aplicação no Sistema

    As regras tributárias fiscais são utilizadas pelo sistema para:

    - Calcular automaticamente os tributos nos documentos;
    - Garantir padronização nos cálculos fiscais;
    - Reduzir riscos de erro humano;
    - Atender às obrigações legais e fiscais.

    ### Controle e Auditoria

    Todas as alterações realizadas nas regras tributárias fiscais são registradas em **log de auditoria**, permitindo:

    - Rastreabilidade das mudanças;
    - Identificação do usuário responsável;
    - Histórico de vigência das regras;
    - Atendimento a fiscalizações e auditorias.

    ### Boas Práticas

    - Mantenha as regras fiscais sempre atualizadas;
    - Revise as regras após atualizações de versão;
    - Alinhe o cadastro com a legislação vigente;
    - Teste as regras em ambiente controlado antes da utilização em produção.

    ### Disponibilidade

    As regras tributárias fiscais estão disponíveis conforme a versão do produto e as adequações legais aplicáveis ao TOTVS Construção Gestão de Imóveis.

    > **Importante**  
    > O correto entendimento e configuração das regras tributárias fiscais impactam diretamente a conformidade legal e a segurança tributária da empresa.

    ## Estrutura da Regra Tributária Fiscal no Sistema

    A Regra Tributária Fiscal é composta por **campos de identificação** e por abas específicas que determinam **como e quando** a regra será aplicada nos cálculos fiscais.

    ### Aba: Identificação

    Nesta aba são definidos os dados principais da regra tributária.

    - **Coligada**  
      Indica a empresa/coligada à qual a regra tributária pertence.
    - **Código**  
      Identificador único da regra tributária no sistema.
    - **Descrição**  
      Descrição objetiva da finalidade da regra.  
      *Exemplo:* Situações tributadas integralmente pelo IBS e CBS.
    - **Fórmula de Base de Cálculo Fiscal**  
      Define a fórmula utilizada para apuração da base de    cálculo do tributo, quando aplicável. Caso não informada, o sistema utiliza a base padrão definida para o tributo.
    - **Situação Tributária**  
      Código que identifica o enquadramento tributário da operação conforme a legislação.
    - **Classificação Tributária**  
      Código utilizado para classificar a operação fiscalmente, servindo de base para aplicação das regras de cálculo e apuração dos tributos.
    - **Regra Tributária Regular**  
      Permite vincular a regra a uma regra padrão, quando necessário, para reaproveitamento de configurações fiscais.
    - **Início da Vigência**  
      Data a partir da qual a regra tributária passa a ser válida.
    - **Final da Vigência**  
      Data limite de validade da regra. Quando não informada, a regra permanece vigente por tempo indeterminado.
    - **Ativo**  
      Indica se a regra está disponível para uso no sistema.

    ### Aba: Detalhes dos Tributos

    Nesta aba são definidos os tributos que compõem a regra fiscal e como eles serão calculados.

    - Definição dos tributos aplicáveis à operação (ex.: **IBS**, **CBS**);
    - Configuração das alíquotas;
    - Indicação se o tributo é devido integralmente, parcialmente ou com redução;
    - Parametrização de bases de cálculo específicas, quando aplicável;
    - Integração com redutores da base de cálculo do IVA.

    Essas informações garantem que o cálculo dos tributos seja realizado corretamente conforme a legislação vigente.

    ### Aba: Regras de Seleção

    A aba **Regras de Seleção** define os critérios que o sistema utilizará para **selecionar automaticamente** a Regra Tributária Fiscal no momento do cálculo dos tributos.

    Esses critérios funcionam como filtros, garantindo que a regra seja aplicada somente quando as condições configuradas forem atendidas.

    #### Regra de Tributação

    Neste campo é definido o **tipo de dependência** utilizado como base para a seleção da regra tributária. As opções disponíveis são:

    - **Nenhuma Dependência**  
      A regra será aplicada de forma geral, sem considerar dependência específica. Indicada para regras padrão, amplas ou genéricas.
    - **Cliente / Fornecedor**  
      A regra será aplicada conforme o cadastro do cliente ou fornecedor envolvido na operação.
    - **Empresa**  
      Permite aplicar a regra de acordo com a empresa (coligada), quando há tratamentos fiscais distintos entre empresas do grupo.
    - **Estado**  
      A regra será selecionada conforme a Unidade Federativa (UF), considerando regras fiscais estaduais.
    - **Município**  
      Utilizada quando a tributação depende do município da operação.
    - **Produto**  
      A regra será aplicada conforme o produto ou serviço envolvido na operação.
    - **Classificação Fiscal de Bens e Serviços**  
      Utilizada para seleção da regra com base na classificação fiscal (ex.: enquadramentos fiscais específicos).
    - **Tipo de Operação**  
      Define a aplicação da regra conforme o tipo de operação fiscal realizada.

    #### Definição das Regras

    Após selecionar o tipo de dependência, devem ser cadastradas as **regras** informando:

    - O critério selecionado (ex.: Estado, Produto, Tipo de Operação);
    - O conteúdo correspondente (ex.: código do estado, produto ou operação);
    - A prioridade de aplicação, quando houver múltiplas regras.

    O sistema avalia essas regras em conjunto com a vigência para determinar automaticamente qual regra tributária será aplicada.

    ### Considerações Importantes

    - Evite configurar múltiplas regras com critérios conflitantes;
    - Priorize critérios mais específicos quando necessário;
    - Sempre valide a aplicação da regra em ambiente de testes antes de utilizar em produção.
    > **Atenção**  
    > A correta configuração da aba **Regras de Seleção** é essencial para garantir que a Regra Tributária Fiscal seja aplicada corretamente, evitando erros na apuração do IBS e da CBS.
