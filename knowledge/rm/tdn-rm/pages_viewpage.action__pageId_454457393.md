---
content_hash: d3085a8afdaa4f51c7c68ec9e92e6a95452e7730e794e76d905af5738ed7bde9
fetched_at: '2026-06-29T00:10:12.461293+00:00'
page_id: '454457393'
product: rm
source: tdn-rm
title: Conversão EAI 2.0 ( TOTVS INCORPORAÇÃO )
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454457393
version: 109
---

## **Processos para efetuar a conversão da base de Dados TOTVS INCORPORAÇÃO do EAI 1.0 para EAI 2.0.**

Análise de Compatibilidade

A versão miníma exigida do RM para a conversão ao EAI 2.0 é 12.1.28 e do Protheus 12.1.25 (Lobo Guará)A análise de compatibilidade do cliente com o EAI 2.0 deve ser realizada pelo consultor de implantação ou analista de suporte, que deve considerar as características:

1. Todos os pacotes de integração utilizados pelo cliente devem estar disponíveis no EAI 2.0
2. Caso haja planejamento de implantação de novos pacotes de integração, deve-se garantir que estes estejam disponíveis no EAI 2.0 até o prazo da implantação pois a conversão da base de dados é irreversível
3. Verificar se o cliente possui customizações em suas Transformações XSLT ou nos SourceCodes
   1. Todas as customizações de integração do EAI 1.0 deverão ser re-codificadas pois o modelo de customização do EAI 2.0 não é retro-compatível.

**Script de liberação**  
Caso após a análise acima seja constatado que o cliente é compatível com o EAI 2.0, deve-se solicitar ao suporte o script de liberação de acesso ao conversor.  
Sem a execução deste script o menu de acesso não é visível ao cliente.

**ATENÇÃO:**  
Sobre Compartilhamento Protheus Quando Integrado ao RM, tem que ser observado algumas restrições: [Clique aqui!](https://tdn.totvs.com/pages/viewpage.action?pageId=269080214)

PAI2. Config. EAI Protheus | Serviço Rest1. Config. EAI Protheus | Serviço Rest |2 .Config. EAI Protheus | Serviço Rest

Documento de configurar o **EAI** do Protheus:

Documento de Serviço **REST:**

3. Config. EAI RM - Host2. Config. EAI RM - Host |3. Config. EAI RM - Host

Configurando WebService/EAI do RM:

Caminho do serviço RM após ter sido configurado estará ao final da apresentação do mesmo no browser como descrito no link acima, a tag wsdl com o atributo name="RM\_IRMSServer" o valor do atributo location será o valor que deverá ser inserido no parâmetro MV\_EAIURL2 do Protheus.  
**<http://localhost:8051/EAIService/IConWSEAIService>**

6. Config para efetuar a conversão de EAI 1.0 para EAI 2.04. Config para efetuar a conversão de EAI 1.0 para EAI 2.0 |6. Config para efetuar a conversão de EAI 1.0 para EAI 2.0

**Configurações que devem ser realizadas antes da Conversão:**

# Desabilitando fórmulas visuais

Gestão | Fórmula Visual | Fórmula Visual

***Selecionar a Fórmulas***

* Mensagem Padrão - Lançamentos Financeiros 1.002
* Menssagem única - Obra / Etapa / Tarefa
* Mensagem única - Projeto
* Mensagem única - Contrato

 Inativar todas as Fórmulas

# PARAMETROS DA INTEGRAÇÃO.

Configurando Parâmetros Integração RM:

| Coligada | Parâmetro | Tipo | Valor | Descrição |
| --- | --- | --- | --- | --- |
| 0 | PRJ\_URLAPIRESTPROTHEUS | Texto | [http://CaminhoServidor:8013/rest](http://10.31.73.79:8013/rest) | Caminho configurado no appserver.ini do Protheus, utilizado pelo RM para alguns processos na conversão e nos processos diários de algumas rotinas |
| 0 | PRJ\_USRAPIRESTPROTHEUS | Texto | Usuário Administrador do Protheus | Usuário para login no Protheus ao ser acionado o serviço rest.  (admin) |
| 0 | PRJ\_PASSAPIRESTPROTHEUS | Texto | Senha  Administrador do Protheus (123) | Senha do Usuário Administrador informado no parâmetro PRJ\_USRAPIRESTPROTHEUS |
| 0 | AJUSTECAMPOPARCELATIN | Logico | Marcado (True) | Utilizado para ajustar tamanho dos campos relacionado as parcelas do TIN no Financeiro. |
| 0 | CODCLASSIFICPAIS | Texto | Depende da classificação que está ligada no País Brasil | Utilizado para encontrar o País no momento da gerar ou receber as mensagens de integração. |

**ADPTERS Que são criados após a conversão.**

Ambiente | Shedule | Adapter E.a.i

| Mensagem Unica | Rotina | Mensagem | Descrição | Envia | Recebe | Método | Operação | Canal Envio | Versão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sim | FINI070LST | LISTOFACCOUNTRECEIVABLESETTLEMENTS | Lista de Títulos a Receber para Baixa | Não | Sim | Síncrono | Todas | EAI | 1.000 |
| Sim | FINI035LST | LISTOFCOMPLEMENTARYVALUE | Cadastro Valores Acessórios | Não | Sim | Síncrono | Todas | EAI | 1.000 |

**Convertendo a base RM para EAI 2.0**

Para Habilitar o processo de conversão para **EAI 2.0** favor entrar em contato com a TOTVS!

Entrar no RM ( Módulo – Integração )

Verificar se o Contexto encontra-se todo preenchido.

* Coligada
* Filial

Integração | Mensagem Única | **Conversor EAI 2.0**

Na primeira etapa de conversão é necessário informar e Validar os serviços Web Service e REST do Protheus.

Na etapa referente ao Diagnostico será possível visualizar os Adapters utilizados na Integração ativa, e ao clicar na opção **Iniciar Validação** será possível visualizar se o nível de compartilhamento das tabelas está correto para que a integração funcione corretamente.

Diagnostico de Integração

Ao finalizar a conversão será possível executar o Diagnostico de Integrações separadamente para consultar os ajustes necessários.

Compartilhamento Indevido

Caso seja apresentado algum compartilhamento indevido para a integração, será apresentado a mensagem abaixo e não será possível avançar o conversor até que compartilhamento no Protheus seja ajustado.

**Para avançar no processo de conversor de integração, entre RM e Protheus será necessário verificar e ajustar as inconsistências apresentadas.**

Source Application

Caso o SourceApplication não seja recuperado automaticamente na etapa subsequente deverá ser utilizando a opção **Atualizar por Sistema Integrado.**

OBS : Este processo irá converter o RM do EAI 1.0 para 2.0 automaticamente

1- Converter os dados relacionados às estruturas pertinentes às integrações (a saber: cadastro de integrações, entidades, mensagens, de/para, ... etc) para uma nova estrutura de dados.  
  
2- Converter os dados relacionados à integração TOP + Protheus.  
  
3- Converter os dados relacionados à integração TIN + Protheus.

a. Os valores de integração dos lançamentos financeiros (RM) são convertidos em valores acessórios dos títulos (Protheus).

b. Todos os adapters relacionados à integração são cadastrados no RM nas versões necessárias para o correto funcionamento da integração.

c. É ligado o parâmetro de Reajuste Online.

4- Será enviado os parâmetros de De/Para para o Protheus.

5- Irá configurar os Adapters no Protheus.

Ao finalizar a conversão para o EAI 2.0 será necessário executar a conversão do TCGI. Caso a conversão seja abortada por algum motivo, ao inicia-la novamente o sistema irá continuar de onde parou. O Totvs Construção e Gestão de Imoveis ficara bloqueado até que a sua conversão seja finalizada.

**Abre automaticamente a tela – Processo de carga de dados de apropriação nos Pedidos de Compra integrada**

 Avançar

Marcar todas coligadas que deverão sofrer a conversão!

Executar o processo

Processado com sucesso ( Fechar em seguida )

**Configurando Parâmetros do Protheus**

SIGACFG

Base de Dados | Bases de Dados

Parâmetros | Pesquisar

MV\_RMTINVE = 2

**Observação**: Este parâmetro será automaticamente criado pelo conversor do TIN EAI2.0. Caso ele não exista ou esteja criado de forma diferente, a conversão irá recriá-lo.

MV\_EAIURL2 = WEB SERVIÇE DO RM

Ambiente | Shedule | Adapter E.a.i

ROTINA :FINI070LST

NOME : LISTOFACCOUNTRECEIVABLESETTLEMENTS

ROTINA : FINI035LST

NOME : LISTOFCOMPLEMENTARYVALUE

7. Cadastros Contábeis5. Cadastros Contábeis |7. Cadastros Contábeis

**Cadastros Contábeis ( TIN & PROTHEUS )**

Adpaters utilizados na Integração Contábil

Módulo - **SIGACTB**

Atualizações | Entidades | Plano de Contas

Plano de Contas inserido no Protheus

Mensagem enviada para o RM.

Plano de contas enviado para o RM.

Atualizações | Entidades | Centro de Custo

Centro de Custo cadastrado no Protheus

Mensagem enviada para o RM.

Centro de Custo enviado para o RM.

Importante

Para que as funcionalidades de Item Contábil e Classe de Valor sejam utilizados no Protheus, terá que efetuar a configuração abaixo.

Segue o Link com orientações de como criar os Adapters no TIN:

Configurações | Configurações Contábeis

Configurações de Custos

Editar - **Item Conta** e **Cod Cl Val**

**Contr Saldo?**

**1 = SIM**

**2 = NÃO**

**Editar para que fiquem = 1 e passarem a ser utilizados.**

**Item Conta = 1 - OK em seguida!**

**Cod Cl Val = 1 - OK em seguida!**

Atualizações | Entidades | Item Contábil

Cadastro de Item contábil no Protheus.

Mensagem envaida para o RM.

Item Contábil enviado para o RM.

Atualizações | Entidades | Classe de Valor

Cadastro da Classe de Valor no Protheus

Mensagem enviada para o RM

Classe de Valor enviada para o RM.

Incluindo um novo Lançamento contábil

Selecionar o Lançamento - ABA ( Dados Adicionais )

Tipo Contábil = Contábil ou Baixa Contábil.

Clicar em seguida = Inclusão

Inserido o Lançamento Contábil no RM.

Mensagem enviada do RM.

Atualizações | Movimentos | Lancam Contabeis

Lançamento Contábil enviado para o Protheus.

8. Melhorias no EAI 2.06. Melhorias no EAI 2.0 |8. Melhorias no EAI 2.0

### Ao migrar para o EAI 2 o sistema entregará um maior ganho de funcionalidades nas quais o controle de recebíveis por parte do TIN já possui, e estão sempre em evolução: [Valores Acessórios no Contas a Receber](http://tdn.totvs.com/pages/viewpage.action?pageId=311631483)

Com a migração dos Valores de Acréscimos/Decréscimos para Valores Acessórios no EAI 2.0, a funcionalidade dos Valores Acessórios permitirá maior flexibilização das regras de acréscimos e decréscimos nos títulos a receber.

Através desta funcionalidade será possível definir regras para que o sistema efetue o cálculo de acréscimos ou decréscimos em títulos a receber, de forma automática, com base nas regras pré-definidas, permitindo regras específicas para cada título a receber, de forma individual. Mais detalhes clique [Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=311631483).

O cadastro de 'Valores Acessórios' no Protheus será preenchido pelo conversor, a partir do cadastro de componentes do Imobiliário, respeitando as ações de acréscimo e decréscimo desse cadastro.

Serão migrados títulos a receber que estão em aberto ou com baixas parciais no Protheus. Os valores de acréscimos/decréscimos serão zerados e terão os valores acessórios preenchidos com base nos valores de integração do financeiro do RM, exceto os componentes que tenham a ação nada.  O campo ‘Valor Original’ do Protheus receberá o ‘Valor Original’ do lançamento do financeiro do RM.

Após a migração, os valores dos títulos serão os mesmos de antes e serão visualizados na subtela de Valores Acessórios dentro da visualização de Contas a Receber.

As baixas parciais dos Títulos a Receber serão migradas seguindo a mesma regra acima, onde os itens de baixas serão refeitos e discriminados por valores acessórios na baixa.

Antes

Depois

.

9. Contas a Receber RM7. Contas a Receber RM |9. Contas a Receber RM

### Ao migrar para o EAI 2, os recebíveis gerados pelo Totvs Construção Gestão de Imóveis serão gerenciados através do RM, e para isso é necessário que toda a parte de Contas a Receber do Totvs Gestão financeira, como por exemplo (Remessa, Retorno de Cobrança e Relatórios de Boletos) tenham sido parametrizados e testados previamente para que não pare a operação dos usuários do financeiro.

Ao executar o conversor para EAI 2, o cliente deverá dar o aceite que tenha sido parametrizado o Totvs Gestão Financeira

8. Mensagem de Envio de Status CNAB - UPDATECONTRACTSTATUSPARCEL |

## Configuração de Transação

## Configuração de Rota

# Processos envolvidos

No novo modelo de integração (EAI 2.0), a remessa de cobrança dos lançamentos financeiros do TIN será realizada pelo RM. Nesse caso, o status CNAB deve ser enviado pelo RM e tratado no Protheus.

Desta forma foi criado a partir da versão 12.1.23 do EAI 2.0 (Enterprise Application Integration) da integração TOTVS Incorporação e Protheus um novo “Adapter” chamado “UpdateContractStatusParcel” para alteração da situação de cobrança do título financeiro do Protheus pelo respectivo status CNAB do lançamento financeiro enviado pelo RM através dos processos financeiros de:

* Remessa de Cobrança Eletrônica
* Registro online de boletos
* Remessa de débito automático
* Cancelamento de remessa de boletos

Para que esta integração ou espelhamento de informações fosse possível foi necessário a criação de um parâmetro no Protheus para estabelecer a relação entre o status CNAB do Financeiro RM e a respectiva Situação de Cobrança do título no Financeiro Protheus

A relação de paridade entre as duas entidades é apresentada na tabela a seguir:

|  |  |
| --- | --- |
| Status CNAB (RM) | Situação de Cobrança (Protheus) |
| 0 = Não Remetido | 0 = Carteira |
| 1 = Remetido | X = Parâmetro MV\_RMTINCA |
| 2 = Registrado | X = Parâmetro MV\_RMTINCA |
| 3 = Recusado | X = Parâmetro MV\_RMTINCA |
| 4 = Baixado | X = Parâmetro MV\_RMTINCA |
| 5 = Cancelado | X = Parâmetro MV\_RMTINCA |

Os processos de remessa citados anteriormente disparam o gatilho de integração do adapter UpdateContractStatusParcel enviando a mensagem com o valor de status CNAB que deve ser tratado no Protheus para definição da Carteira ou situação de cobrança do titulo financeiro.

No lado Protheus o usuário precisa definir o valor do Parâmetro MV\_RMTINCA para que a situação de cobrança do respectivo título seja alterada.

Sobre Carteira Informada:

A carteira informada deverá conter a seguinte configuração:  
Carteira selecionada deve possuir banco e não permitir cobrança descontada

Ao integrar com o Protheus é possível verificar a situação de cobrança do título através do menu de Funções de Contas a Receber conforme imagem a seguir

# XSD (XML Schema Definition) do Adapter UpdateContractStatusParcel

**XSD (XML Schema Definition) do Adapter UpdateContractStatusParcel**

|  |
| --- |
| `<``xs:schema` `xmlns:xs``=``"http://www.w3.org/2001/XMLSchema"` `xmlns:xsi``=``"http://www.w3.org/2001/XMLSchema-instance"` `elementFormDefault``=``"qualified"` `xsi:noNamespaceSchemaLocation``=``"../totvsmsgdoc.xsd"``>` `<!--  ====================================  -->` `<!--  INCLUDES NECESSARIOS PARA A MENSAGEM  -->` `<!--  ====================================  -->` `<``xs:include` `schemaLocation``=``"../totvsmsg.xsd"``/>`   `<!--  ====================================  -->` `<!--  DOCUMENTAÇÃO DA MENSAGEM              -->` `<!--  ====================================  -->` `<``xs:annotation``>` `<``xs:appinfo``>` `<``MessageDocumentation``>` `<``Name``>UpdateContractStatusParcel</``Name``>` `<``Description``>Requisição de atualização da situação da parcela</``Description``>` `<``Segment``>Construção e Projetos</``Segment``>` `<``ProductInformation` `product``=``"RM"``>` `<``Contact``>Cristiano Silva Faria</``Contact``>` `<``Description``>GDP Sustentação Const. e Proj.</``Description``>` `<``Adapter``>UpdateContractStatusParcel</``Adapter``>` `<``Send``>` `<``Request``>sim</``Request``>` `<``Insert``>não</``Insert``>` `<``Update``>não</``Update``>` `<``Delete``>não</``Delete``>` `</``Send``>` `<``Receive``>` `<``Request``>não</``Request``>` `<``Insert``>não</``Insert``>` `<``Update``>não</``Update``>` `<``Delete``>não</``Delete``>` `</``Receive``>` `</``ProductInformation``>` `<``ProductInformation` `product``=``"PROTHEUS"``>` `<``Contact``/>` `<``Description``/>` `<``Adapter``/>` `<``Send``>` `<``Request``>sim</``Request``>` `<``Insert``/>` `<``Update``/>` `<``Delete``/>` `</``Send``>` `<``Receive``>` `<``Insert``/>` `<``Update``/>` `<``Delete``/>` `</``Receive``>` `</``ProductInformation``>` `</``MessageDocumentation``>` `</``xs:appinfo``>` `</``xs:annotation``>` `<!--  ====================================  -->` `<!--  CONTEÚDO DE NEGÓCIO DA MENSAGEM ====  -->` `<!--  ====================================  -->` `<``xs:complexType` `name``=``"RequestType"``>` `<``xs:sequence``>` `<``xs:element` `name``=``"CompanyInternalId"` `type``=``"xs:string"` `minOccurs``=``"1"``>` `<``xs:annotation``>` `<``xs:documentation``>InternalId da Empresa</``xs:documentation``>` `<``xs:appinfo``>` `<``FieldDocumentation` `product``=``"RM"``>` `<``Field``>FLAN.CODCOLIGADA|FLAN.CODFILIAL</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>integer|integer</``Type``>` `<``Length``/>` `<``Description``>Chave da empresa</``Description``>` `</``FieldDocumentation``>` `<``FieldDocumentation` `product``=``"PROTHEUS"``>` `<``Field``/>` `<``Required``>sim</``Required``>` `<``Type``/>` `<``Length``/>` `<``Description``/>` `</``FieldDocumentation``>` `</``xs:appinfo``>` `</``xs:annotation``>` `</``xs:element``>` `<``xs:element` `name``=``"BranchId"` `type``=``"xs:string"` `minOccurs``=``"0"` `maxOccurs``=``"1"``>` `<``xs:annotation``>` `<``xs:documentation``>Código da Filial</``xs:documentation``>` `<``xs:appinfo``>` `<``FieldDocumentation` `product``=``"PROTHEUS"``>` `<``Field``>FLAN.CODFILIAL</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>varchar</``Type``>` `<``Length``>2</``Length``>` `<``Description``>Pode ter tamanho entre 02 e 12 dependendo da configuração do Protheus</``Description``>` `</``FieldDocumentation``>` `</``xs:appinfo``>` `</``xs:annotation``>` `</``xs:element``>` `<``xs:element` `name``=``"AccountDocumentInternalId"` `type``=``"xs:string"` `minOccurs``=``"0"``>` `<``xs:annotation``>` `<``xs:documentation``>InternalId do Lançamento</``xs:documentation``>` `<``xs:appinfo``>` `<``FieldDocumentation` `product``=``"RM"``>` `<``Field``>FLAN.CODCOLIGADA|FLAN.IDLAN</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>int|int</``Type``>` `<``Length``/>` `<``Description``>Chave da tabela FLAN</``Description``>` `</``FieldDocumentation``>` `<``FieldDocumentation` `product``=``"PROTHEUS"``>` `<``Field``>CEMPANT|CFILANT|SE1XX0.E1_PREFIXO|SE1XX0.E1_NUM|SE1XX0.E1_PARCELA|SE1XX0.E1_TIPO</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>varchar</``Type``>` `<``Length``/>` `<``Description``/>` `</``FieldDocumentation``>` `</``xs:appinfo``>` `</``xs:annotation``>` `</``xs:element``>` `<``xs:element` `name``=``"RemittedBank"` `type``=``"xs:string"` `minOccurs``=``"0"``>` `<``xs:annotation``>` `<``xs:documentation``>Situação da parcela</``xs:documentation``>` `<``xs:appinfo``>` `<``FieldDocumentation` `product``=``"RM"``>` `<``Field``>FLAN.CNABSTATUS</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>int</``Type``>` `<``Length``/>` `<``Description``>Situação do Lançamento com relação ao banco</``Description``>` `</``FieldDocumentation``>` `<``FieldDocumentation` `product``=``"PROTHEUS"``>` `<``Field``>SE1XX0.E1_SITUACA</``Field``>` `<``Required``>sim</``Required``>` `<``Type``>varchar</``Type``>` `<``Length``/>` `<``Description``>0 = Carteira 1 = Cobrança Simples 2 = Cobrança Descontada 3 = Cobrança Caucionada 4 = Cobrança Vinculada 5 = Cobrança C/Advogado 6 = Cobrança Judicial 7 = Cob Caução desconto F = Carteira Protesto G = Carteira Acordo H = Cobrança Cartorio</``Description``>` `</``FieldDocumentation``>` `</``xs:appinfo``>` `</``xs:annotation``>` `</``xs:element``>` `</``xs:sequence``>` `</``xs:complexType``>` `<!--  ====================================  -->` `<!--  REFERÊNCIA AOS TIPOS                  -->` `<!--  ====================================  -->` `<``xs:complexType` `name``=``"ReturnContentType"``> </``xs:complexType``>` `<``xs:element` `name``=``"BusinessContent"` `type``=``"RequestType"` `substitutionGroup``=``"AbstractBusinessContent"``/>` `<``xs:element` `name``=``"ReturnContent"` `type``=``"ReturnContentType"` `substitutionGroup``=``"AbstractReturnContent"``/>` `</``xs:schema``>` |

# TOTVS Message UpdateContractStatusParcel

**TOTVS Message UpdateConstractStatusParcel**

|  |
| --- |
| `<``TOTVSMessage``>` `<``xs:schema` `id``=``"TOTVSMessage"` `xmlns``=``""` `xmlns:xs``=``"http://www.w3.org/2001/XMLSchema"` `xmlns:msdata``=``"urn:schemas-microsoft-com:xml-msdata"``>` `<``xs:element` `name``=``"TOTVSMessage"` `msdata:IsDataSet``=``"true"` `msdata:UseCurrentLocale``=``"true"``>` `<``xs:complexType``>` `<``xs:choice` `minOccurs``=``"0"` `maxOccurs``=``"unbounded"``>` `<``xs:element` `name``=``"FLAN"``>` `<``xs:complexType``>` `<``xs:sequence``>` `<``xs:element` `name``=``"CODCOLIGADA"` `type``=``"xs:short"` `minOccurs``=``"0"` `/>` `<``xs:element` `name``=``"CODFILIAL"` `type``=``"xs:int"` `minOccurs``=``"0"` `/>` `<``xs:element` `name``=``"IDLAN"` `type``=``"xs:int"` `minOccurs``=``"0"` `/>` `<``xs:element` `name``=``"CNABSTATUS"` `type``=``"xs:int"` `minOccurs``=``"0"` `/>` `</``xs:sequence``>` `</``xs:complexType``>` `</``xs:element``>` `</``xs:choice``>` `</``xs:complexType``>` `</``xs:element``>` `</``xs:schema``>` `<``FLAN``>` `<``CODCOLIGADA``>4</``CODCOLIGADA``>` `<``CODFILIAL``>1</``CODFILIAL``>` `<``IDLAN``>178206</``IDLAN``>` `<``CNABSTATUS``>0</``CNABSTATUS``>` `</``FLAN``>` `</``TOTVSMessage``>` |

# TOTVS Message UpdateContractStatusParcel Transformada

A TAG <RemmitedBank>0</RemmitedBank> recebe o código 1 para envio de remessa e recebe 0 para cancelamento de remessa

**TOTVS Message UpdateContractStatusParcel Transformada**

|  |
| --- |
| `<``TOTVSMessage``>` `<``MessageInformation` `version``=``"1.000"``>` `<``UUID``>d47d9c06-b087-482c-ae9e-98e27ccce520</``UUID``>` `<``Type``>BusinessMessage</``Type``>` `<``Transaction``>UPDATECONTRACTSTATUSPARCEL</``Transaction``>` `<``StandardVersion``>1.000</``StandardVersion``>` `<``SourceApplication``>RM</``SourceApplication``>` `<``CompanyId``>4</``CompanyId``>` `<``BranchId``>1</``BranchId``>` `<``Product` `name``=``"RM"` `version``=``"12.1.23.0"` `/>` `<``GeneratedOn``>2018-10-25T12:08:56</``GeneratedOn``>` `<``DeliveryType``>Sync</``DeliveryType``>` `</``MessageInformation``>` `<``BusinessMessage``>` `<``BusinessEvent``>` `<``Entity``>UPDATECONTRACTSTATUSPARCEL</``Entity``>` `<``Event``>Upsert</``Event``>` `</``BusinessEvent``>` `<``BusinessContent``>` `<``RMENTITYNAME``>FLAN</``RMENTITYNAME``>` `<``CompanyInternalId``>4|1</``CompanyInternalId``>` `<``BranchId``>1</``BranchId``>` `<``AccountDocumentInternalId``>4|178206</``AccountDocumentInternalId``>` `<``RemmitedBank``>0</``RemmitedBank``>` `</``BusinessContent``>` `</``BusinessMessage``>` `</``TOTVSMessage``>` |

# TOTVS Message UpdateContractStatusParcel de Resposta

A TAG <Status></Status> retorna como foi processada a mensagem pelo Protheus   
**TOTVS Message UpdateContractStatusParcel de Resposta**

|  |
| --- |
| `<``TOTVSMessage``>` `<``MessageInformation` `version``=``"1.000"``>` `<``UUID``>8a0c4aa8-f2fa-112c-6203-83c7e624f129</``UUID``>` `<``Type``>Response</``Type``>` `<``Transaction``>UPDATECONTRACTSTATUSPARCEL</``Transaction``>` `<``StandardVersion``>1.000</``StandardVersion``>` `<``SourceApplication``>HOMOLOG_WS04</``SourceApplication``>` `<``CompanyId``>04</``CompanyId``>` `<``BranchId``>040101</``BranchId``>` `<``Enterprise``>04</``Enterprise``>` `<``BusinessUnit``>01</``BusinessUnit``>` `<``Product` `name``=``"PROTHEUS"` `version``=``"12"``></``Product``>` `<``GeneratedOn``>2018-10-25T12:08:59Z</``GeneratedOn``>` `<``DeliveryType``>Sync</``DeliveryType``>` `</``MessageInformation``>` `<``ResponseMessage``>` `<``ReceivedMessage``>` `<``SentBy``>RM</``SentBy``>` `<``UUID``>d47d9c06-b087-482c-ae9e-98e27ccce520</``UUID``>` `<``Event``>Upsert</``Event``>` `<``MessageContent``>``<![CDATA[<?xml version="1.0" encoding="utf-8"?><TOTVSMessage><MessageInformation version="1.000">    <UUID>d47d9c06-b087-482c-ae9e-98e27ccce520</UUID>    <Type>BusinessMessage</Type>    <Transaction>UPDATECONTRACTSTATUSPARCEL</Transaction>    <StandardVersion>1.000</StandardVersion>    <SourceApplication>RM</SourceApplication>    <CompanyId>4</CompanyId>    <BranchId>1</BranchId>    <Product name="RM" version="12.1.23.0" />    <GeneratedOn>2018-10-25T12:08:56</GeneratedOn>    <DeliveryType>Sync</DeliveryType>  </MessageInformation><BusinessMessage><BusinessEvent><Entity>UPDATECONTRACTSTATUSPARCEL</Entity><Event>Upsert</Event></BusinessEvent><BusinessContent><RMENTITYNAME>FLAN</RMENTITYNAME><CompanyInternalId>4|1</CompanyInternalId><BranchId>1</BranchId><AccountDocumentInternalId>4|178206</AccountDocumentInternalId><RemmitedBank>0</RemmitedBank></BusinessContent></BusinessMessage></TOTVSMessage>]]>``</``MessageContent``>` `</``ReceivedMessage``>` `<``ProcessingInformation``>` `<``ProcessedOn``>2018-10-25T12:08:59Z</``ProcessedOn``>` `<``Status``>ok</``Status``>` `</``ProcessingInformation``>` `<``ReturnContent``>` `<``InternalId``>` `<``DestinationInternalId``>04|040101|1  |201806130|   |NF </``DestinationInternalId``>` `<``OriginInternalId``>4|178206</``OriginInternalId``>` `<``Status``>Titulo atualizado com sucesso. Carteira atual: 0</``Status``>` `</``InternalId``>` `</``ReturnContent``>` `</``ResponseMessage``>` `</``TOTVSMessage``>` |

Apresentação dos títulos Incorporação x Protheus |

Os títulos a receber passa a apresentar os valores acessórios preenchidos com base nos valores de integração do TCGI do RM, com exceção dos componentes que tenham a ação nada no TCGI.  O campo ‘Valor Original’ do Protheus receberá o ‘Valor Original’ do lançamento do TCGI do RM e os demais valores serão preenchidos em valores acessórios.

Importante:

**A Entidade utilizada para Inclusão/Alteração/Exclusão dos títulos no protheus é a FINANCING**

- **Momento 0**: Parcela criada no TCGI é representada corretamente no TCGI RM e no Backoffice Protheus, Mas Protheus não possui representação de Correção Monetária com valor zerado.

- **Momento 1**: Parcela após reajuste inflacionário no TCGI é representada corretamente no TCGI RM e no Backoffice Protheus.

**Situação:** Inflação aumenta o valor do componente “Correção Monetária” enviando ao Protheus o valor a ser acrescentado.

- **Momento 2**: Parcela após reajuste Deflacionário no TCGI é representada corretamente no TCGI RM e no Backoffice Protheus.

**Situação:** Deflação pode zerar ou negativar o valor do componente “Correção Monetária”

\*\* Obs: Valor da Correção Monetária passou a ser negativa.

Configurador - Correção das Inconsistências.|Configurador - Correção das Inconsistências.|Configurador - Correção das Inconsistências.|

# Corrigindo inconsistências ao executar o Conversor EAI e Configurador- Configurador de Integração

## **Compartilhamento de tabela Protheus**

Avaliando inconsistência de Compartilhamento.

Log Mostrando a TABELA e como encontra-se o compartilhamento no Protheus da Tabela. E a Solução.

**Sobre compartilhamento de Tabelas Protheus**  -   
Para entender um pouco mais sobre as validações de compartilhamentos - [Clique Aqui!](https://tdn.totvs.com/display/INT/Compartilhamento+Tabelas+%28Adapters%29+-+EAI2+RM+x+Protheus)

## **Versão de Adpter RM x Protheus**

Log mostrando a versão do Adpter no RM e no Protheus. A versão do Adpter tem que ser a mesma em ambos sistemas.

Neste Exemplo : RM versão 1.000

Protheus versão 1.001

Corrigido para 1.000

Correções Feitas , voltando a executar o conversor e Iniciar novamente validação.

Incosistências do Conversor - OK e neste momento pode seguir a conversão.
