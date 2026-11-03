---
content_hash: 1c7426449601f3dafabd6b41d3bf2314401f7e4617d343fc4bc2fc6f83670842
fetched_at: '2026-06-29T00:11:17.045332+00:00'
page_id: '676047552'
product: rm
source: tdn-rm
title: Condições Contratuais - Eletrônico III
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676047552
version: 51
---

## **CONTEÚDO**

CONTEÚDO

# **01. Visão Geral**

Nesse documento estão descritos os parâmetros que mudam o comportamento da geração do XML no padrão TISS definido pela ANS.

# **02. Parâmetros Geral I - Regras I**

| Parâmetro | Descrição |
| --- | --- |
| **Versão dos arquivos XML** | Define qual versão **TISS** será gerado XML que será enviado a operadora de saúde. No caso de não se informar qual versão será usada, o Sistema assumirá automaticamente a versão 2.01.02 como base para geração do XML. |
| **Informações Especificas** | Atenção! Esse parâmetro foi descontinuado a partir da versão TISS 4.00.00  Agrupador de customizações especificadas para determinadas operadoras. Essa opção está descontinuada e só deve ser utilizada por clientes que ainda utilizam essa opção.TODO |
| **Código para Agrupamento** | Com essa opção configurada será gerado um único código de agrupamento para os **grupos de gastos** **Materiais**, **Medicamentos**, **Órteses** e **Próteses**. O agrupamento ocorre com a inclusão no XML de uma única linha com a descrição do AGRUPADOR.  Exemplo: Se configurado o código 19 no campo **Código para Agrupamento** em **Materiais** e na conta do paciente houver 30 itens de materiais, o sistema irá criar uma única linha com o código 19 e descrição MATERIAL, somando o valor desses 30 itens.  Também há possibilidade de identificação de quatro outros tipos de insumos localizados na aba **Eletrônico II**, sendo eles **Medicamento de consumo não brasíndice (41)** , **Medicamento de consumo não brasíndice/simpro (31),** **Medicamento** **manipulados** **(42)**, **Medicamento com autorização previa não brasíndice (43).**  Caso nenhum agrupador seja informado, a geração irá ocorrer conforme o padrão TISS, que é levar a informação de forma individualizada de cada um dos itens no XML. |
| **Tratar pacote como procedimento para Atendimento Interno** | Por padrão o pacote é enviado no XML na lista de Outras Despesas. Se habilitado, o mesmo será enviado na lista de Procedimentos para atendimento Internos.   * Quando marcado, os pacotes vinculados a um procedimento executado serão enviados no XML TISS como Procedimentos Executados, permitindo o envio da equipe médica com base no procedimento vinculado. Caso não seja vinculado nenhum procedimento ao pacote na aba de Taxas e serviços, a tag de equipe não será enviada * Quando desmarcado, os pacotes continuarão sendo tratados como Outras Despesas no XML, sem envio de equipe médica associada ao pacote para procedimentos internos. |
| **Tratar pacote como procedimento para Atendimento Externo** | Por padrão o pacote é enviado no XML na lista de Outras Despesas. Se habilitado, o mesmo será enviado na lista de Procedimentos para atendimento Externo.   * Quando marcado, os pacotes vinculados a um procedimento executado serão enviados no XML TISS como Procedimentos Executados, permitindo o envio da equipe médica com base no procedimento vinculado. Caso não seja vinculado nenhum procedimento ao pacote na aba de Taxas e serviços, a tag de equipe não será enviada * Quando desmarcado, os pacotes continuarão sendo tratados como Outras Despesas no XML, sem envio de equipe médica associada ao pacote para procedimentos externos. |
| **Enviar no XML a data de encerramento da parcial como data de saída** | Ao marcar este parâmetro,o sistema imprime a data de encerramento da parcial no campo "26-Data e hora da saída da internação" da Guia de Resumo de Internação. Quando o mesmo estiver desmarcado, é exibida a data de alta do atendimento. |
| **Incluir Lançamentos Fora da Conta** | Atenção! Esse parâmetro só se aplica para a geração do XML do Hospital (arquivo que se inicia com o zero).  Esse parâmetro indica se os itens **FORA DA CONTA** serão informados ou não no **XML** ou nos relatórios das **Guias**. O parâmetro **Valor Zerado** fica condicionado a se um desses parâmetros estiver ativo, indicando se o valor do item será zerado ou não.  É possível ter configurações distintas por tipos de atendimentos **Internos** ou **Externos** |
| **Valida Guias já utilizadas em outros atendimentos.** | Quando esse parâmetro habilitado, durante a inclusão de uma nova guia, será verificado se o número informado nas guias de Consulta, SADT, Resumo de Internação e Honorário Individual já foi utilizado em outras Parciais, seja para o mesmo paciente ou para outros pacientes. |
| **Regras para ordenação no xml** | Atenção! Esse parâmetro só se aplica a partir da versão TISS 4.00.00 e da BibliotecaRM 12.1.2410   * **Ordem das guias**:   + Número Guia Prestador   + Data da Parcial   + Data da Parcial e Nome do Paciente   + Data da Autorização   + Data da Autorização e Nome do Paciente   + Prontuário   + Unidade de Atendimento e Prontuário * **Ordem dos itens:**   + Sequencial do Lançamento   + Data do Lançamento   + Código do Item (Importante, caso a codificação do item esteja utilizando código TUSS ou código específico, o mesmo não será diferenciado na ordenação) |
| **Enviar Equipe com Prestadores com Honorário Zerado** | Quando ativado, este parâmetro permite que os dados da equipe estejam enviados mesmo quando o campo de valor honorário estiver preenchido com R$ 0,00. |

# **03. Parâmetros Geral I - Regras II**

# **04. Parâmetros Geral I - Regras XML Terceiros (Arquivos 2 e 5)**

# **05. Parâmetros Geral I - Tags Opcionais que não serão geradas no XML**

# **06. Geral II**

| Parâmetro | Descrição |
| --- | --- |
| **Guia Operadora e Guia Prestador** | Atenção! Atenção! Os parâmetros da Guia Operadora e Guia Prestador são distintos!  Essa configuração reflete no preenchimento do campo **Núm.** **Guia / Comprovante** informado na tela de **Guia / Autorização** e também para os campos **Guia Operadora** e **Guia Prestador** da tela **Informações para TISS**.  **Se nenhuma opção estiver habilitada**, ousuário fica responsável no preenchimento dessas informações.  Para que o sistema gere o número automaticamente, deverá ser configurada uma das seguintes opções:  **Automático**   * Quando habilitado o sistema irá preencher o campo **Num. Guia / Comprovante** da tela **Guia / Autorização.**O preenchimento do campo ocorre no momento de salvar a guia.   **Sequencial Único**   * Quando desmarcado: Um novo sequencial será controlada para cada **Convênio + Tipo de Guia + Guia**, desta forma o sequencial da **Guia de Consulta**, será diferente para a **Guia de SP/SADT** e assim para os demais tipos. * Quando marcado: Um novo sequencial será controlado para cada **Convênio** + **Guia**, desta forma o sequencial da **Guia de Consulta**, será sequenciado com a **Guia de SP/SADT** e assim para os demais tipos.   **Permite Alterar**   * Com essa opção habilitada, o sistema irá permitir que o usuário altere o número da guia operadora e prestador após a sua inclusão, essa opção só tem efeito quando o número foi gerado através da opção **Automático** estiver habilitada.   **Tipo de Atendimento**   * Controle se o número será gerado para ambos os tipos de atendimento ou somente para interno ou externo,.   **Máscara**   * Para automatizar o número da guia da operadora e o número da guia do prestador no padrão TISS é necessário que seja seja definida uma máscara. |
| **Copiar número da Guia/Comprovante para o campo Senha/Autorização** | Para utilizar o número da guia como senha devemos marcar o parâmetro **Copiar número da Guia/Comprovante para o campo Senha/Autorização**. |
| **Numero de lote baseado na remessa (alfanúmerico) ou fatura (numérico)** | Conforme o padrão TISS o número da remessa é alfanumérico. Se o portal da operadora não aceitar esse formato e o parâmetro for marcado, o sistema gera uma numeração alternativa composta apenas por dígitos. **Importante!** Os módulos de Faturamento continuam operando internamente com o número alfanumérico. |
| **Valida Guias já utilizadas em outros atendimentos** | Caso o parâmetro estiver marcado, o sistema deverá validar se a guia digitada já foi utilizada anteriormente em outro atendimento desse ou de outro paciente para o mesmo convênio (convênio do registro do atendimento em questão). |

**07. Geral III**

| Parâmetro | Descrição |
| --- | --- |
| **Incluir Tipo de Nota junto a identificação do Prestador conforme local do Atendimento Externo ou Interno** | Se marcado, será enviado junto a tag **identificacacaoPrestador**, **001** para atendimentos **Externos** ou **002** para atendimentos **Internos**. Exemplo: O código do prestador na operadora é **12345** e ao gerar uma remessa de atendimentos **Externos**, o número será gerado como **12345001**, se a remessa fosse para atendimentos internos, o número seria **12345002.** |

# **08. Web Service**

# **09. WS Config**

| Parâmetro | Descrição |
| --- | --- |
| **Identificação do Prestador** | Para os Web Services da ANS **Solicitação de Procedimento**, **Verifica Elegibilidade**, **Solicita Status Autorização** e **Cancela Guia**, pode-se configurar qual informação de credenciamento será utilizada no momento da geração do XML de comunicação, sobrescrevendo o que estiver definido no **Credenciamento do Prestador**. Os opções possíveis são: **CNPJ**, **CPF**, **Código Operador** e **Não Utiliza**. |
| **Configurações de Envio** | Ao marcar a opção **Realiza a integração por web service da Orizon** será definido para o sistema que irá utilizar WS da Orizon para efetuar troca de mensagens para os serviços, **Solicitação de Procedimento**, **Solicita Status Autorização** e **Cancela Guia**. O serviço de **Verifica Elegibilidade não está disponível para ser utilizado pela Orizon.**  Em **Prefixo para envio do XML**, definir qual o prefixo utilizado nas tags do XML de acordo com o esquema da operadora. |

Estas configurações são utilizadas como uma sobreposição de uma outra configuração similar, efetuada no cadastro do prestador, localizada em Cadastros > Prestador > anexo Credenciamento > campos “Tipo Credencial” e “Credencial”

**Atenção**: Estes campos existem novamente na aba “Histórico do Credenciamento”, e estes valores do histórico que são utilizados!

De acordo com a opção selecionada no campo Tipo credencial, o campo Credencial é preenchido com valores da aba “Identificação” do prestador, como “CPF”, “CNPJ” e “Número” em “Identidade Profissional”.

Para o campo “Tipo credential” temos as opções CPF/CNPJ, Identidade Profissional e Código Próprio.

**Utilização destas configurações**

As configurações citadas acima são utilizadas na geração dos arquivos XML para **Solicitação de Procedimento**, **Verifica Elegibilidade**, **Solicita Status Autorização** e **Cancela Guia**, no Registro de Atendimento > Guia / Autorização > Processos

Estas configurações são aplicadas em algumas tags dos arquivos XMLs, onde para os quatro tipos de arquivo XML, é gerado um cabeçalho igual, na tag cabecalho > origem > identificacaoPrestador.

E também em mais algumas, de acrodo com o tipo de XML:

1. cabecalho > origem > identificacaoPrestador
2. prestadorParaOperadora > solicitacaoProcedimento > solicitacaoSP-SADT > dadosSolicitante > contratadoSolicitante
3. prestadorParaOperadora > solicitacaoProcedimento > solicitacaoInternacao > identificacaoSolicitante > dadosDoContratado
4. prestadorParaOperadora > verificaElegibilidade > dadosPrestador
5. prestadorParaOperadora > solicitaStatusAutorizacao > dadosContratado
6. prestadorParaOperadora > cancelaGuia > dadosPrestador

Para todas estas, existe uma tag para identificação do prestador, onde esta pode ser como no exemplo um CNPJ, ou um CPF ou o código na operadora, e a regra para definir o tipo e o valor desta é:

Se a Identificação do Prestador na Condição Contratual (respeitando o tipo do XML / WS)...

1. CNPJ  
   Se o campo de CNPJ do cadastro do prestador estiver informado com 14 dígitos  
   Tipo CNPJ com o valor do campo CNPJ.
2. CPF  
   Se o campo de CPF do cadastro do prestador estiver informado com 11 dígitos  
   Tipo CPF com o valor do campo CPF.
3. Código Operadora  
   Tipo codigoPrestadorNaOperadora com o valor do campo Credencial.
4. Não Utiliza  
   Se o campo Tipo credencial no cadastro do prestador for...
   1. CPF/CNPJ
      1. Se o campo de CNPJ do cadastro do prestador estiver informado com 14 dígitos  
         Tipo CNPJ com o valor do campo CNPJ.
      2. Se o campo de CPF do cadastro do prestador estiver informado com 11 dígitos  
         Tipo CPF com o valor do campo CPF.
   2. Identidade Profissional  
      Tipo codigoPrestadorNaOperadora com o valor do campo Identidade Profissional.

Se seguindo esta lógica, não for definido o tipo e/ou valor, complementará com a regra...

1. Se o campo de CNPJ do cadastro do prestador estiver informado com 14 dígitos  
   Tipo CNPJ com o valor do campo CNPJ.
2. Se o campo de CPF do cadastro do prestador estiver informado com 11 dígitos  
   Tipo CPF com o valor do campo CPF.
3. Se o campo Identidade Profissional estiver informado.  
   Tipo codigoPrestadorNaOperadora com o valor do campo Identidade Profissional.
4. Senão  
   Tipo codigoPrestadorNaOperadora com o valor do campo Credencial.

# **10. Regras para geração XML**

1. **Ordem Guias**- Criar um combo de opções
   1. Número Guia Prestador
   2. Data da Parcial
   3. Data da Parcial e Nome do Paciente
   4. Data da Autorização
   5. Data da Autorização e Nome do Paciente
   6. Prontuário
   7. Unidade de Atendimento e Prontuário
2. **Ordem dos Itens**- Criar um combo de opções
   1. Sequencial do Lançamento
   2. Data do Lançamento
   3. Código do Item (Importante, caso a codificação do item esteja utilizando código TUSS ou código específico, o mesmo não será diferenciado na ordenação)
   4. Nenhum -  incluir no enum no topo da lista  = 0

**Observação :**

Esses parâmetros ficam ativos somente na versões TISS 4.00.00 e acimas
