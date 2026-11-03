---
content_hash: bbc103de20f2ed730c7db874cec839226736aa111f28407bd81efa9c94ee4472
fetched_at: '2026-06-29T00:10:47.947478+00:00'
page_id: '561070194'
product: rm
source: tdn-rm
title: Conversão EAI 2.0
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561070194
version: 30
---

## **01. Apresentação**

O conversor do EAI 1.0 para 2.0 tem por finalidade disponibilizar acesso às novas rotinas de integração, convergir os pacotes de integração para aplicativos integrados, migrar as informações presentes na base para o novo modelo de dados e realizar os ajustes de base de dados necessários para cada pacote de integração instalado no EAI.

Alterações Diretas

Qualquer alteração realizada diretamente na tabela GEAICONFIG irá automaticamente bloquear todo o uso das ferramentas de integração do RM. Assim sendo, sempre utilize o RM para realizar qualquer configuração referente ao EAI.

Compatibilidade

A versão mínima exigida do RM para a conversão ao EAI 2.0 é 12.1.29 e do Protheus 12.1.25 (Lobo Guará)A análise de compatibilidade do cliente com o EAI 2.0 deve ser realizada pelo consultor de implantação ou analista de suporte, que deve considerar as características:

1. Todos os pacotes de integração utilizados pelo cliente devem estar disponíveis no EAI 2.0
2. Caso haja planejamento de implantação de novos pacotes de integração, deve-se garantir que estes estejam disponíveis no EAI 2.0 até o prazo da implantação pois a conversão da base de dados é irreversível
3. Verificar se o cliente possui customizações em suas Transformações XSLT ou nos SourceCodes
   1. Todas as customizações de integração do EAI 1.0 deverão ser recodificadas pois o modelo de customização do EAI 2.0 não é retro-compatível.

Clientes Stored

Clientes que tem por origem Stored devem garantir a correta conversão a versão do EAI 1.0 antes de realizar a conversão para o EAI 2.0. Por exemplo o correto carregamento de De/Para na tabela HCINTEGRACAOID.

## **02. Desabilitando fórmulas visuais**

Gestão | Fórmula Visual | Fórmula Visual

***Selecionar a Fórmulas***

* Mensagem Padrão - Lançamentos Financeiros 1.002
* Mensagem única - Obra / Etapa / Tarefa
* Mensagem única - Projeto
* Mensagem única - Contrato

 Inativar todas as Fórmulas

## **02. Acesso ao conversor**

O acesso ao conversor de integrações é restrito a bases de dados que possuem o parâmetro de liberação, pois até o presente momento (fevereiro de 2019) ainda existem pacotes de integração não migrados para o EAI 2.0.

### 02.01. Análise de compatibilidade

A análise de compatibilidade do cliente com o EAI 2.0 deve ser realizada pelo consultor de implantação ou analista de suporte, que deve considerar as características:

1. 1. Todos os pacotes de integração utilizados pelo cliente devem estar disponíveis no EAI 2.0
   2. Caso haja planejamento de implantação de novos pacotes de integração, deve-se garantir que estes estejam disponíveis no EAI 2.0 até o prazo da implantação pois a conversão da base de dados é irreversível
   3. Verificar se o cliente possui customizações em suas Transformações XSLT ou nos SourceCodes
      1. Todas as customizações de integração do EAI 1.0 deverão ser recodificadas pois o modelo de customização do EAI 2.0 não é retro-compatível.

### 02.02. Script de liberação

Caso após a análise acima seja constatado que o cliente é compatível com o EAI 2.0, deve-se solicitar ao suporte o script de liberação de acesso ao conversor.

Script

Sem a execução deste script o menu de acesso não é visível no menu do RM.

### 02.03. Caminho do menu

O processo de conversão está disponível no contexto de integrações, na árvore de menus de Mensagem Única.

## **03. Processo de conversão**

O processo de conversão passa por 4 passos, melhor descritos nas sub-sessões a seguir.

### **03.01. Teste de comunicação dos serviços**

A primeira etapa, consiste nos teste de comunicação dos serviços do Ambiente do Protheus. Basta informar a URL do Web Services e do serviços REST para testar a comunicação. Esta URL pode ser obtida do arquivo appserver.ini, onde é definido a porta do WSDL e a porta do REST mais o endereço do servidor, conforme os exemplos na imagem abaixo.

### **03.02. Validação de compartilhamento das Entidades do Protheus**

Nesta etapa, ao clicar no botão iniciar validações é onde a Api Rest "**ShareModeRest**" entra em ação para obter os compartilhamento das tabelas no Protheus.   
Na imagem abaixo, segue exemplo de resultado de compartilhamentos das tabelas do Protheus.

IMPORTANTE!

* Na lateral temos o grupo de empresas do Protheus associados a empresa (coligada) do RM, será efetuado uma varredura de todas que aparecem nesta visão lateral associado, a todos os adapters no Protheus. Porque o Protheus pode ter compartilhamentos diferentes por tabela em cada empresa, e isso não será aceito pelo RM, assim como algumas tabelas vinculadas ao adapter não poderá conter alguns compartilhamentos incompatíveis com os cadastros no RM.
* Deve ser analisado junto do time de Produto qual deve ser o nível de equivalência adequado à ser utilizado.  
  Abaixo Json exemplo para consumo da api rest SHAREMODEREST do Protheus, como é feito no processo de busca dos dados para ser utilizado na validação.
* POST - JSON - solicitação dos compartilhamentos adapterstrue

### **03.03.** **Regra de negócio referente aos níveis de equivalência para a replicação**

Define a equivalência de conceitos entre o Protheus x RM, utilizando as propriedades <CompanySharingMode>, <BusinessUnitySharingMode>, <BranchSharingMode> do arquivo XML.

* **Grupo de Empresas: (**Determina que o compartilhamento da mensagem de integração Protheus x RM é Exclusivo por Coligada e Compartilhada por Filial**)**IsSharedColigada = false;  
  IsSharedFilial = true;   
  ReplicateToCompanyGroup = false;  
  Estas propriedades são definidas de forma fixa baseada na regra de negócio entre o conceito de Grupo de Empresas do Protheus X Coligadas do RM.  
  Dessa forma elas nãos serão configuráveis baseadas nas outras propriedades de equivalência do arquivo XML.
* **Empresas:**IsSharedColigada = CompanySharingMode == "C";  
  IsSharedFilial = ( CompanySharingMode == "E" And BusinessUnitySharingMode == "C" );  
  ReplicateToCompanyGroup = CompanySharingMode == "C";
* **Unidade de Negócio:**IsSharedColigada = BusinessUnitySharingMode == "C";  
  IsSharedFilial = ( BusinessUnitySharingMode == "E" And BranchSharingMode == "C" );  
  ReplicateToCompanyGroup = BusinessUnitySharingMode == "C";

**Legenda:**

IsSharedColigada = true or false, Define se será Compartilhado por Coligada e Filial.

IsSharedFilial = true or false, Define se será Exclusivo por Coligada e Compartilhada por Filial.

ReplicateToCompanyGroup = true or false, Define se deve ser filtrado pelo Grupo de Empresas.

IMPORTANTE!

Na concepção do serviço de Replicação do EAI 2.0 foi acordado entre todas as partes envolvidas que as regras de negócio e todo o código implementado relacionado a replicação é de responsabilidade do Produto e não do time de Framework.

### **03.04.** **Configuração do Código Externo(CODEXTERNO) para a replicação**

Para que a replicação ocorra e encontre uma referência entre o Protheus X RM, o campo Código Externo deve ser preenchido com o código referente ao Protheus, que é informado na Tag <CompanyId> do arquivo XML. O conteúdo padrão do Código Externo é vazio, portanto numa primeira ativação da integração, caso ele permanecer vazio a replicação não será realizada pois não sera encontrada uma referência.

### **03.05. Avisos e confirmação**

Nesta etapa do processo de conversão é declarar-se ciente dos riscos e procedimentos de segurança.

### **03.06. Parâmetros de execução**

Ao passar do segundo para o terceiro passo, o conversor tentará obter automaticamente (vide imagem abaixo) a informação do SourceApplication de cada pacote integrado a partir do envio de uma mensagem única WhoIs para o WebService parametrizado no pacote.

Em caso de falha ao tentar consultar o serviço Protheus será exibido o alerta abaixo, porém é possível prosseguir realizando o preenchimento manual da informação de SourceAplication

Logo após a consulta automática será apresentada a tela de parametrização da conversão, disponibilizando a lista de integrações a serem convertidas e a parametrização de mensagens a migrar para as novas tabelas.

Podemos observar que na imagem acima o pacote de integração não teve seu SourceApplication identificado automaticamente, devendo assim ser parametrizado de forma manual através do botão "Atualizar por Sistema Integrado".

O SourceApplication pode ser identificado a partir de uma Mensagem Única trafegada via EAI 1.0, copiando o conteúdo de uma Tag de mesmo nome. A informação do SourceAplicacion por padrão no Protheus é definida pelo nome do enviroment (P12) + grupo de empresa (01). Ou seja neste exemplo "P1201".

Também é possível a definição do parâmetro MV\_EAISRC no modulo de configuração Protheus (SIGACFG). Sendo a configuração recomendada, pois independente do nome do Enviroment do Protheus todas as mensagens utilizarão o mesmo SourceAplication.

A rotina de conversão não migrará mensagens com sucesso para a nova estrutura de tabelas, ficando a cargo do consultor no momento da conversão definir se deve-se ou não importar as mensagens de erro. É aconselhável que todas as análises do ambiente 1.0 sejam realizadas previamente, tornando assim a conversão das mensagens de erro desnecessárias.

### **03.07. Execução dos conversores por pacote de integração**

Após finalizar da conversão por parte do EAI (dados de integração) serão executados os processos de conversão específicos de cada pacote de integração.

A ocorrência de erro em um dos processos por pacote de integração não fará com que a conversão por parte do EAI seja desfeita, ficando a cargo do consultor responsável pela conversão realizar os ajustes necessários e executar novamente o processo em questão.

## **04. Dados convertidos**

O processo de conversão realiza a consolidação e migração de dados das tabelas do EAI 1.0 para o EAI 2.0.

Segue abaixo os dados trabalhados pelo conversor padrão do EAI:

1. 1. Conversão dos pacotes de integração
      1. Os pacotes de integração são convertidos em Aplicativos e Pacotes Instalados, conforme descrito no documento de [Entidades Relacionadas](https://tdn.totvs.com/display/framework/1.+Entidades+do+EAI).
   2. Conversão dos Mapas de integração para a tabela de Rotas.
   3. Cópia das informações de De-Para para a nova tabela.
   4. Cópia das informações de mensagens trafegadas para a nova estrutura de tabelas
      1. A cópia ou não destas informações depende da parametrização apresentada na sessão [03.02](https://tdn.totvs.com/pages/createpage.action?spaceKey=framework&title=ParametrosConversao&linkCreation=true&fromPageId=454830786).
   5. Conversão de parâmetros e execução de scripts de conversão por transação
      1. São realizados procedimentos necessários para compatibilização entre o comportamento de adapters do EAI 1.0 com os novos adpters do EAI 2.0.
      2. Exemplo: O adapter de Centro de Custo possuía três versões diferentes que utilizavam três parâmetros diferentes para definir se utiliza código auto-incremental. O adapter do EAI 2.0 padronizou estes três parâmetros em um só e o conversor é responsável por gerenciar esta unificação.

## **05. Inclusão de novos pacotes ou transações**

Durante os projetos de migração dos pacotes de integração do EAI 1.0 para o EAI 2.0 podem surgir necessidades específicas de adapters ou destes pacotes de integração. Estas necessidades devem ser analisadas e ter suas regras de negócio implementadas na respectiva sessão do conversor.

Os fontes do conversor estão disponíveis no projeto **RM.EAI.TotvsMessage.Conversor.Server** e as sub-sessões a seguir apresentam os pontos de desenvolvimento para cada necessidade.

### **05.01. Conversão de parâmetros de adapter**

Este ponto de desenvolvimento deve ser utilizado para implementação de ajustes de base de dados relacionados a um adapter específico.

O fonte com o conversor do adapter deve seguir as regras citadas abaixo:

1. Estar disponível no mesmo projeto, dentro da estrutura de pastas "./ConverteEAI2/AdapterConverter"
2. Possuir o atributo "AdapterConverterAttr", definindo neste o nome da transação convertida.
3. Herdar da classe "EaiAdapterConverterBase"
4. Implementar a conversão internamente ao método "ConvertAdapter", definido na interface "IEaiAdapterConverter".

## **Exemplo de código: Conversor CustomerVendor** Expandir origem

### **05.02. Conversão de scripts por Pacote de Integração**

Este ponto de desenvolvimento é reservado para ajustes específicos de um pacote de integração que devem ser executados na mesma transação dos scripts do EAI, como ajustes de roteamento e de parâmetros de integração.

Estes ajustes devem ser adicionados como uma sessão no método "ExecutarScriptsPacotes" da classe "EAIConverteEAI2", conforme exemplo de código abaixo.  
**Exemplo de código: Pacote TOP x Protheus** Expandir origem

### **05.03. Processos de conversão específicos por pacote de integração**

Após finalizar a execução do processo de conversão do EAI são executadas também todas as actions de processos parametrizadas para os pacotes de integração convertidos. Este fluxo de execução deve ser utilizado na conversão de informações que necessitem de iteração do usuário, para processamentos de longa duração ou que devam ser executados fora da transação do conversor padrão.

Atenção!

A execução dos processos de conversão específicos por pacote de integração é realizada pelo Client, estando assim fora da transação original e não realizando nenhum tipo de tratamento de erros.

Todo o tratamento de erro dos processos deve estar contidos na execução do próprio, como por exemplo o travamento da integração até a reexecução com sucesso do processo.

**Passos para desenvolvimento de um processo de conversão específico:**

1. Desenvolvimento do Processo
   1. Deve-se passar por todo o desenvolvimento padrão de um Processo da Framework RM, como o desenvolvimento do Form, ParamsProc, Process e a Action.
   2. Este processo deve conter todas as regras de negócio necessárias, bem como o tratamento de erros.
2. Adição da Action desenvolvida no retorno do método "GetProcessBeforeConvertEai2" do server "EAIConversorServer".
   1. Este é o método responsável por retornar a lista de Actions a serem executadas.

## **06. Assuntos Relacionados**

* Entidades Relacionadas ao EAI 2.0
  + [1. Entidades do EAI](https://tdn.totvs.com/display/framework/1.+Entidades+do+EAI)
* Documento técnico da criação do Conversor para EAI 2.0  
  + [DT\_ConversorEAI1\_EAI2](https://tdn.totvs.com/display/LRM/DT_ConversorEAI1_EAI2)
