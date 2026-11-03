---
content_hash: 211766a5a3b988afd35cc0b78f9a3184ef464f168c9236f6148eb03eab37237f
fetched_at: '2026-06-29T00:10:06.577819+00:00'
page_id: '452719317'
product: rm
source: tdn-rm
title: Assistente de Geração de arquivo para o MANAD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719317
version: 4
---

Através da execução desse assistente é gerado o arquivo do MANAD, para a entrega ao Auditor Fiscal ou outro órgão solicitante. Para conhecer mais sobre o MANAD recomendamos o acesso ao site da Receita Federal.  
Esse assistente é composto de 7 etapas pelas quais o responsável pela a geração dos arquivos passará, definindo a composição dos mesmos, de acordo com o layout e de acordo as solicitações do requisitante (Auditor Fiscal, etc.). São essas etapas:  
**ETAPA1 - Perfil de Parâmetros e Descrição do Processo**

Essa é a tela de abertura do assistente. Como o arquivo do MANAD possui uma composição de dados bastante complexa, esse módulo foi preparado para que pudessem ser gerados arquivos para cada uma das coligadas em apenas uma ou poucas execuções. O número de vezes que o assistente será executado dependerá, exclusivamente, das solicitações feitas pelo Auditor Fiscal ou outro requisitante, para cada uma das coligadas.  
Para otimizar essas execuções foi possibilitada a criação de perfis, que irão guardar a parametrização utilizada em cada uma dessas gerações. Além disso, é possível nomear o processo que está sendo executado caso o usuário queira agendar a criação do arquivo para outro momento. É nessa tela que se inicia esse processo de criação de perfis e de nomeação de processos agendados relativos ao MANAD.

**Caixa "Perfil de Parâmetros"**

Essa caixa é composta de três itens:

**Nome do Perfil**

Esse é o local onde são criados novos perfis ou selecionados perfis criados anteriormente. Na primeira execução do assistente é obrigatório a criação de um perfil.

**Excluir**

Esse botão tem a finalidade de excluir um perfil que não é mais utilizado.

**Salvar perfil ao concluir**

Esse CheckBox tem a finalidade de indicar que o perfil que está sendo utilizado será modificado durante a execução do assistente e que tais modificações deverão ser gravadas. Ao utilizar um perfil sem a marcação desse parâmetro, caso o mesmo seja modificado durante o processo, essas alterações não serão gravadas. Na criação de um novo perfil esse parâmetro deverá estar marcado.

**Caixa "Descrição do Processo"**

Nesse campo poderá ser nomeado um processo caso a execução do assistente seja feita com o intuito de agendar a geração do arquivo para outro momento. Para entender melhor esse processo, leia o help da 7ª etapa do assistente (Agendamento do Processo).

**E****TAPA 2 - Parâmetros Globais**

Nessa tela são definidos os parâmetros que serão utilizados para todas as coligadas selecionadas na 6ª etapa do assistente (Seleção de Coligadas).

**I****ntervalo de datas para a movimentação.**

Aqui será definido o período das informações solicitadas pelo Auditor Fiscal ou outro requisitante. É obrigatório informar as duas datas, e a Data Fim não poderá ser anterior à Data Início.

**Seleção de Funcionários**

Aqui será definido qual o grupo de funcionários será informado no arquivo do MANAD.

**Observação**

Essa seleção verifica a Situação, Tipo e Código de Recebimento atuais dos funcionários. Para validar funcionários de acordo com as suas informações cadastrais na época da movimentação definida no campo anterior, deverá ser criada uma fórmula de seleção.

**Folha de Pagamento em Relação ao Período**

Os blocos K250 e K300 do MANAD possuem uma subdivisão quanto ao tipo de folha. Os indicadores do tipo de folha são: 1 - Folha Normal 2 - Folha de 13º Salário 3 - Folha de Férias Marcando a 1º Opção, as movimentações serão levadas para o MANAD de acordo com essa divisão. Caso seja marcada a 2ª Opção, as movimentações de Folha Normal e de Férias serão unificadas e serão ambas informadas com o indicador 1, enquanto o 13º Salário permanece sendo informado no arquivo com o indicador 2.

**Gerar Contabilização**  
O Auditor Fiscal (ou outro órgão solicitante) poderá exigir as informações da folha de pagamento com ou sem informações contábeis. Marcando a 1ª Opção essas informações irão compor o arquivo do MANAD, enquanto a 2ª Opção, ao ser marcada, fará com que o sistema não considere essas informações na composição do arquivo.

**Localização do(s) arquivo(s)**

Aqui é informado onde o arquivo será gerado.  
   
**Desconsidera data de pagamento**   
Quando marcado o parâmetro o sistema não vai considerar data de pagamento da ficha financeira para o período informado de processo se o tipo de folha for diferente de 3.  
   
**Utiliza mais de um vínculo nas transferências**  
Quando marcado esse parâmetro e o tipo de transferência for (T ou E, essa informação fica na aba registro no cadastro do funcionário quando o tipo de transferência pelo módulo de rescisão for 5 ou 6 ) assume-se a data de transferência para admissão do funcionário.    
   
**ignora incidência de IRRF de férias no registro K250**  
Quando o parâmetro é marcado os eventos que possuem incidências em IRRF de férias não são computados para a base de IRRF.  
   
**Considerar os CC 37, 66, 96, 97 no dissídio de INSS**  
Quando marcamos os eventos de código de cálculo 37, 66, 96, 97 passam a somar para compor o valor do campo 14 VL\_BASE\_PS Base de Cálculo Para a Previdência Social do K250.  
   
**Considera como 1 os índices de base 9 no registro K300**  
   
O tipo 9 é se: Os eventos em que há incidências em IRRF de férias ou estorno de IRRF de férias ou o código de cálculo for 126, 86 e 87.  
   
**Observação 1**

Caso seja adotada instalação do sistema em 3 camadas, esse local deve indicar uma pasta compartilhada na rede, com acesso total.

**Observação 2**

Caso seja adotada instalação do sistema em 3 camadas, se o sistema encontrar problemas de permissão de gravação de arquivo durante a geração do mesmo, a gravação ocorrerá em uma pasta temporária no servidor de aplicação e esse fato será informado no log de execução do processo.

**Observação 3**

O nome do arquivo gerado tem o seguinte formato: MANAD\_Código da Coligada\_Data Início (AAAAMMDD)\_Data Fim (AAAAMMDD).txt

**ETAPA 3 - Opções de Exportação**

Nessa tela são definidos os dados que serão utilizados na composição dos blocos de abertura do arquivo do MANAD, bem como serão exportados alguns dados de movimentação Esses parâmetros serão utilizados para todas as coligadas selecionadas na 6ª etapa do assistente (Seleção de Coligadas).

**Composição do Registro 0000 (Dados da Empresa)**

Aqui o sistema verifica as seções que tiveram funcionários lotados no período informado e, para a composição do registro de abertura (0000) o sistema faz os seguintes tratamentos: Marcando a Gerar Por Filial, irá verificar quais as filiais foram vinculadas às seções encontradas no levantamento citado acima e irá agrupar as informações de todas as seções nos códigos de filiais encontrados. Cada filial encontrada dará origem a um registro (uma linha) no bloco de abertura. Marcando a Gerar Por Seção, irá gerar um registro para cada seção encontrada no levantamento citado anteriormente.

**Eventos tipo base (Indicação de Provento/Desconto)**

Nesse parâmetro o sistema verifica quais foram os eventos de base de cálculo que foram lançados na movimentação dos funcionários no período informado e os levará para o bloco K300 (itens de folha de pagamento). Nesse bloco existe o campo Indicador de Provento ou Desconto, que pode ser preenchido com: D - Desconto P - Provento O - Outros Marcando a 'Exportar como Outros', os eventos serão levados para o bloco k300 com o indicador O. Marcando a 'Exportar como Provento/Desconto', os eventos serão levados para o bloco k300 com os indicadores D ou P (de acordo com as incidências e / ou código de cálculo.

**Indicador de Tipo de Entrada de Dados**

No bloco de abertura do arquivo do MANAD (bloco 0000), existe o campo Indicador de Tipo de Entrada de Dados, cujo preenchimento é feito a partir dos códigos acima. Esse preenchimento será feito de acordo com instruções dadas pelo Auditor Fiscal ou outro órgão solicitante.

**Finalidade do Arquivo**

Código que será levado para o arquivo, de acordo com informação dada pelo fiscal.

**ETAPA 4 - Visão do Contabilista**

Nessa tela é (são) cadastrado(s) o(s) contabilista(s) responsável(is) pela veracidade das informações enviadas para o relatório do MANAD.  
Na inclusão de um novo contabilista aparecerá uma tela de cadastro onde constarão os seguintes campos:

**Nome do Contador ou Empresa Terceirizada**

Nome do profissional de contabilidade ou da empresa responsável pela contabilidade da empresa - É obrigatório.

**CNPJ**

CNPJ do responsável - quando pessoa física com vinculo empregatício com a empresa deve ser informado o CNPJ da própria empresa - É obrigatório.

**CPF**

CPF do profissional de contabilidade - É obrigatório.

**Inscrição CRC**

Número de inscrição do profissional no Conselho Regional de Contabilidade - É obrigatório.

**CEP**

CEP do profissional de contabilidade ou da empresa responsável pela contabilidade da empresa - quando pessoa física com vinculo empregatício com a empresa deve ser informado o CEP da própria empresa - É obrigatório.

**Data de Início**

Data inicial da prestação dos serviços de contabilidade - É obrigatório.

**Data de Término**

Data final da prestação dos serviços de contabilidade - Não é obrigatório.

**Caixa Postal**

Caixa Postal do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**CEP Caixa Postal**

CEP da Caixa Postal do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Endereço**

Endereço do escritório do profissional ou empresa responsável pelas informações contábeis - É obrigatório.

**UF**

Unidade Federativa do escritório do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Número**

Número do escritório do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Complemento**

Complemento do escritório do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Bairro**

Bairro do escritório do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Telefone**

Telefone do escritório do profissional ou empresa responsável pelas informações contábeis - Não é obrigatório.

**Fax**

Fax do escritório do profissional ou empresa responsável pelas informações contábeis- Não é obrigatório.

**E-Mail**

E-mail do profissional ou empresa responsável pelas informações contábeis - É obrigatório.

**ETAPA 5 - Visão do Responsável**

Nessa tela é (são) cadastrado(s) o(s) responsável(is) pela veracidade das informações enviadas para o relatório do MANAD.  
Na inclusão de um novo responsável aparecerá uma tela de cadastro onde constarão os seguintes dados:

**Caixa 'Responsável pela geração do Arquivo'**

**Campo Cód. do Funcionário**  
Aqui é informada a chapa do funcionário que executou o processo de geração do arquivo do MANAD. Esse campo é de preenchimento obrigatório.

**Caixa 'Informa Dados Responsável'**

Marcando este parâmetro será possível o cadastro dos dados do responsável a executar o processo de geração do arquivo do MANAD manualmente.

Preencha os campos abaixo:

**Nome:** Nome da empresa/técnico responsável pela geração do arquivo

**CPF:**Número do CPF do técnico responsável pela geração do arquivo.

**CNPJ:**Número do CNPJ da empresa responsável pela geração do arquivo.

**Cargo:** Cargo do responsável na empresa

**Email:** Endereço do correio eletrônico

**Telefone:**Número do telefone

**Atenção:** ao marca o parâmetro **Informa Dados Responsável** o sistema irá desabilitar a Caixa **'Responsável pela geração do Arquivo'.**

**Caixa 'Prestação dos Serviços de Informática'**

**Data Início**

Aqui é informada a data em que o responsável iniciou a prestação de serviços de informativa (preenchimento de dados no sistema). Esse campo é de preenchimento obrigatório.

**Data Fim**

Aqui é informada a data em que o responsável finalizou a prestação de serviços de informativa (preenchimento de dados no sistema).

**ETAPA 6 - Seleção de Coligadas**

Nessa tela é(são) selecionada(s) a(s) coligada(s) para a(s) qual(is) será(ao) gerado(s) o(s) arquivo(s) do MANAD. Lembrando que NÂO será gerado um arquivo consolidado com os dados de todas as coligadas e sim um arquivo para cada uma das coligadas selecionadas.

**Coligada possui parâmetros específicos.**

Essa legenda mostra que, toda vez que uma coligada possuir, nessa tela, o símbolo demonstrado na mesma, ao lado esquerdo de seu código, ela terá parâmetros específicos definidos para a mesma.  
Na inclusão de Parâmetros Específicos para uma coligada, aparecerá uma janela contendo os seguintes dados:

**Usar parâmetros específicos**

Marcando esse parâmetro será possível definir uma seleção de funcionários específica ou qual a Origem da Movimentação do funcionário.

**Seleção de Funcionários**

Aqui será definido qual o grupo de funcionários será informado no arquivo do MANAD. Essa seleção será definida somente para a coligada escolhida na inclusão de parâmetros específicos.

**Origem da Movimentação do Funcionário**

Aqui é definido se o sistema irá considerar a movimentação da ficha financeira ou da distribuição por tomadores de serviço para a composição dos blocos k250 e k300.

**Observação 1**

Essa caixa só será visível se, em Opções | Parâmetros | RM Labore | Param. Cálculo, o parâmetro Utiliza Tomadores de Serviço estiver marcado.

**Observação 2**  
Para a marcação do segundo parâmetro recomenda-se a verificação do parâmetro Meses de distribuição guardados, para a geração de Sefip em atraso, presente em Opções | Parâmetros | RM Labore | Param. Cálculo, pois, caso o período das informações seja anterior ao número de meses definido nesse parâmetro, o sistema não terá mais tais informações, sendo necessária a restauração de backup em ambiente de teste para a recuperação das mesmas.

**ETAPA 7 - Agendamento do Processo**

Nessa tela é possível definir se a geração dos arquivos MANAD irá ocorrer logo após o término da execução do assistente ou conforme agendamento.  
Marcando a Agora, os arquivos MANAD serão gerados logo após o término da execução do assistente.  
Marcando a Executar Em, os arquivos MANAD serão gerados em um momento futuro, de acordo com data e hora pré-determinadas. Esse processo gera, após o término da execução do assistente, um registro de agendamento de processo que é possível ser visualizado em Sistema | Server | Gerenciamento de Jobs. Esse processo será nomeado nesse gerenciador da seguinte forma: Intrução Normativa 100 (MANAD) [Descrição do Processo]. Lembrando que a descrição do processo é definido na 1ª etapa do assistente de geração dos arquivos MANAD (Perfil de Parâmetros e Descrição do Processo).  
Marcando a Sob Demanda, os arquivos MANAD não serão gerados. Geralmente essa opção é utilizada para que seja possível a finalização do assistente, gravando um novo perfil, mas sem a geração do arquivo.  
Marcando a opção 'Executar em' são habilitados os parâmetros abaixo caso o usuário deseje repetir o processo de geração dos arquivos MANAD e ainda definir a periodicidade dessas repetições, de acordo com os parâmetros abaixo:

**Não Repetir**

O sistema irá gerar os arquivos MANAD uma única vez, na data e hora pré-determinadas.

**Todas as semanas, no mesmo horário, no(s) dia(s)**

O sistema irá gera os arquivos MANAD todas as semanas, na data e hora pré-determinadas, nos dias selecionados.

**Todos os meses, no mesmo horário, no dia**

O sistema irá gera os arquivos MANAD todos os meses, na hora pré-determinada, no dia determinado. Ex: todo dia 5 de cada mês.

**Diariamente, a cada intervalor (em horas) de**

O sistema irá gera os arquivos MANAD todos os dias em um intervalo de horas pré-determinado.  
Para a geração correta do arquivo do MANAD, garantindo assim a integridade dos dados que serão entregues ao requisitante, recomenda-se, após o entendimento completo dos parâmetros aqui apresentados, a leitura do Processamento do MANAD. O procedimento detalhado nesse material irá auxiliar o responsável pela geração dos arquivos na preparação da base de dados, bem como na validação dos dados no aplicativo SVA, também disponível no site da Receita Federal.

|  |  |
| --- | --- |
|  | Como Fazer |

---

Procedimento de Geração dos Arquivos MANAD  
   
Roteiro para informar autônomos do TOTVS Gestão Financeira no MANAD

|  |  |
| --- | --- |
|  | Veja Também |

---

Dicas Para Correção de Erros no MANAD
