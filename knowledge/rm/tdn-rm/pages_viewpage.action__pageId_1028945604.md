---
content_hash: cee5a07690c0c9d72a41610832a09ce1beef18cc11924c08affa7031cec421ee
fetched_at: '2026-06-29T00:05:48.775901+00:00'
page_id: '1028945604'
product: rm
source: tdn-rm
title: Reforma Tributária - IBS por Localidade RM Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1028945604
version: 4
---

# **CONTEÚDO**

## 1CONTEÚDO

Pré-requisito Obrigatório!

O correto funcionamento da Reforma Tributária no RM Saúde depende da configuração prévia dos cadastros no módulo Fiscal.

Os cadastros relacionados à **Classificação Fiscal de Bens e Serviços**, **Regras Tributárias** e demais parametrizações fiscais **não são responsabilidade do módulo Saúde** e devem ser realizados conforme orientações da equipe de Gestão Fiscal.

Antes de utilizar o processo de Solicitação de Nota Fiscal, certifique-se de que:  
- A Classificação Fiscal de Bens e Serviços está cadastrada  
- As Regras Tributárias foram configuradas corretamente  
- Os parâmetros fiscais necessários foram definidos

Para orientações sobre esses cadastros, consulte a documentação oficial:

# **01. Visão Geral**

A Lei Complementar 214/2025 (Reforma Tributária) altera fundamentalmente a apuração do IBS (Imposto sobre Bens e Serviços), estabelecendo que o cálculo deve considerar o **município de efetiva prestação do serviço**. Esta mudança impacta diretamente o módulo Saúde do TOTVS Gestão Hospitalar, exigindo adequações nos fluxos de Solicitação de Nota Fiscal e na integração com o Backoffice.

# **02. Principais Mudanças**

**Modelo Anterior:**

* + Cálculo de impostos não considerava o município de prestação do serviço.
  + Menos controle sobre os dados do paciente.
  + Município não era considerado no cálculo.

**Modelo Atual (LC 214/2025):**

* + **Atendimento Presencial:** IBS calculado com base no município do hospital/clínica.
  + **Teleconsulta:** IBS calculado com base no município onde o paciente mora.
  + **Código Indicador de Operação:** Preenchido automaticamente para identificar o local de incidência do IBS e CBS no Backoffice.
  + Validação rigorosa dos dados cadastrais do consumidor do serviço, usando paciente e responsável quando aplicável.
  + Regra tributária obrigatória em todas as notas para pacientes particulares.
  + As informações enviadas ficam registradas na Solicitação de Nota Fiscal para consulta e auditoria.

### Impactos Operacionais

1. 1. **Dados de Localidade**: Novos campos criados para armazenar município/UF de operação
   2. **Regra Tributária**: Parametrização obrigatória para definir comportamento fiscal
   3. **Consumidor do Serviço:** Validação rigorosa dos dados cadastrais e bloqueio da integração quando houver informação obrigatória ausente
   4. **Consumidor do Serviço**: Validação rigorosa de dados cadastrais (paciente/responsável)
   5. **Integração Backoffice**: Layout atualizado conforme estrutura do Destinatário NFSe

# **03. Prazo de Adequação**

**Período de Transição 2026:** Durante o primeiro ano de vigência (2026), o IBS será aplicado com alíquota de teste de 1%, permitindo que hospitais e clínicas se adaptem gradualmente às novas regras antes da aplicação das alíquotas definitivas.

**Recomendações:**

* + Atualize o sistema antes de 01/01/2026
  + Revise os cadastros de pacientes e responsáveis financeiros
  + Configure a Regra Tributária Padrão nos parâmetros
  + Faça testes antes de usar em produção

Atenção!

A implementação da Reforma Tributária requer a release mínima 2502 no último patch disponível do sistema.

# **04. Configuração Inicial**

Antes de começar a usar o novo processo, é necessário configurar qual Regra Tributária será utilizada por padrão.

**Caminho:** Parâmetros do Saúde → Backoffice → Geral

**Campo:** Regra Tributária Padrão

Esta configuração define automaticamente a regra fiscal que será aplicada em todas as notas. Você ainda poderá alterá-la manualmente durante o processo de geração da nota, mas o campo sempre precisará estar preenchido.

# **05. Processo de Solicitação de Nota Fiscal**

O processo de Solicitação de Nota Fiscal foi reformulado para atender às exigências da LC 214/2025, garantindo que todos os dados necessários sejam coletados, validados e transmitidos corretamente ao Backoffice.

O fluxo completo de Solicitação de Nota Fiscal permanece o mesmo conforme documentado no manual oficial

As alterações da Reforma Tributária concentram-se exclusivamente na etapa Informações para o Backoffice.

Nesta etapa, o sistema passa a registrar automaticamente os seguintes dados:

| Informação | Descrição | Como é preenchido | Obrigatório |
| --- | --- | --- | --- |
| **Município da Operação** | Município considerado para o cálculo do IBS | Automático: hospital/clínica (presencial) ou paciente (teleconsulta) | Sim |
| **Estado da Operação** | Estado considerado para o cálculo do IBS | Automático: hospital/clínica (presencial) ou paciente (teleconsulta) | Sim |
| **Tipo de Atendimento** | Se foi presencial ou teleconsulta | Automático: identifica pelo tipo de atendimento registrado | Sim |
| **Regra Tributária** | Regra fiscal aplicada na operação | Automático: usa valor dos parâmetros (editável manualmente) | Sim |

Atenção!

Solicitações de Nota Fiscal criadas antes da adequação à Reforma Tributária não terão essas informações preenchidas automaticamente. Nesses casos, o preenchimento deverá ser realizado diretamente no Backoffice.

**Definição do Município e Estado da Operação:**

O sistema identifica automaticamente qual localidade será considerada no cálculo do IBS conforme o tipo de atendimento:

| Tipo de Atendimento | Operação Presencial | Local Operação IBS | Origem |
| --- | --- | --- | --- |
| Atendimento Presencial | 1 | Município/UF do prestador | Unidade de Faturamento → Prestador Principal |
| Teleconsulta | 3 | Município/UF do contratante | Responsável Financeiro do Paciente |

Além da definição do município e estado da operação, o sistema também preenche automaticamente o **Código Indicador de Operação**, utilizado pelo Backoffice para identificar o local de incidência do IBS e da CBS.

O valor enviado depende do tipo de atendimento.

* + **Atendimento Presencial:** O sistema envia o código 030101, indicando que o serviço foi prestado no estabelecimento do fornecedor.
  + **Teleconsulta:** O sistema envia o código 030102, indicando que o serviço foi prestado no endereço do paciente.

Essa definição segue a mesma lógica aplicada ao campo Operação Presencial e é única por Solicitação de Nota Fiscal.

Antes de permitir a conclusão da **Solicitação de Nota Fiscal**, o sistema valida automaticamente os dados cadastrais do paciente e do responsável financeiro. Caso existam informações obrigatórias ausentes, o processo é bloqueado. Para mais detalhes sobre essas validações, consulte o tópico 06. Validação dos Dados do Paciente.

# **06. Validação dos Dados do Paciente**

Para emitir a nota fiscal, o sistema agora precisa de informações completas tanto do **paciente que recebeu o serviço** quanto do **responsável financeiro**. Esta é uma mudança importante trazida pela Reforma Tributária, anteriormente apenas os dados do responsável financeiro eram exigidos.

**Informações Obrigatórias:**

* + Nome completo
  + CPF ou CNPJ
  + Endereço completo (rua, número, bairro)
  + Município e Estado
  + País
  + Telefone
  + E-mail

**Como o Sistema Verifica os Dados:**

**Situação 1: Dados do Paciente Completos**

* + O sistema usa os dados cadastrados do paciente
  + O processo segue normalmente

**Situação 2: Dados do Paciente Incompletos**

* + O sistema busca as informações faltantes no cadastro do Responsável Financeiro
  + Se encontrar tudo que precisa, o processo continua

**Situação 3: Dados Incompletos em Ambos**

* + O sistema **bloqueia** a geração da nota
  + Aparece uma mensagem mostrando exatamente quais informações estão faltando
  + Exemplo: "Não é possível gerar a nota fiscal. Dados obrigatórios não preenchidos: E-mail, Telefone"

**Importante:** Mantenha sempre os cadastros de pacientes e responsáveis atualizados para evitar bloqueios no processo. A exigência dos dados completos do paciente é uma novidade da LC 214/2025.

# **07. Estrutura de Dados**

Todos os dados utilizados na geração da Nota Fiscal são armazenados na tabela **SZPEDIDOATEND**, permitindo:

* + Auditoria completa do processo
  + Verificação de qual fonte de dados foi utilizada (paciente ou responsável)
  + Histórico de alterações da Regra Tributária

#### Novos Campos na Tabela SZPEDIDOATEND

| Campo | Tipo | Descrição | Obrigatório |
| --- | --- | --- | --- |
| **Local Operação IBS - Município** | String | Município utilizado no cálculo do IBS | Sim |
| **Local Operação IBS - UF** | String | Estado utilizado no cálculo do IBS | Sim |
| **Operação Presencial** | Int | Tipo de operação (1=Presencial, 3=Não Presencial) | Sim |
| **Regra Tributária** | Int | ID da regra tributária aplicada | Sim |

ObservaçãoRegistros legados não serão preenchidos retroativamente. Para esses casos, será necessário o preenchimento diretamente na rotina do Backoffice.

# **08. Dúvidas Frequentes**

**1. As notas antigas serão atualizadas automaticamente?**

- Não. Apenas as novas solicitações criadas após a atualização seguirão as novas regras.

**2. Posso mudar a Regra Tributária depois de configurar o padrão?**

- Sim. Durante a geração da nota você pode alterar manualmente, mas o campo não pode ficar vazio.

**3. O que acontece se o cadastro do paciente estiver incompleto?**

- O sistema tentará usar os dados do responsável financeiro. Se ainda assim faltar informação, você não conseguirá gerar a nota até completar o cadastro.

**4. Como sei se o atendimento foi presencial ou teleconsulta?**

- O sistema identifica automaticamente pelo tipo de atendimento registrado. Você não precisa informar manualmente.
