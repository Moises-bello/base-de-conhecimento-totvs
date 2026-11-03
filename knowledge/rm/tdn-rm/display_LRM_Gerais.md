---
content_hash: ac6dd0a5637c428064aa03d0e69f917ed3a2619f6cb45c37f78c0136e6086eee
fetched_at: '2026-06-29T00:10:04.100096+00:00'
page_id: '452719197'
product: rm
source: tdn-rm
title: Gerais
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerais
version: 4
---

**Gerais**

**Preferências**

**Calendário Oficial**  - Campo para definição do calendário a ser utilizado pelo sistema.

**Moeda para o reajuste do depósito recursal** - Campo para definição da moeda a ser aplicada como índice em reajustes de depósito de processos trabalhistas.

**Descrições para os campos de Telefone no cadastro de Pessoas** - Campo para configuração da descrição dos campos Telefone I, Telefone II e Telefone III do cadastro de pessoas.

**Perfil de Triagem** - Considerar apenas currículos com áreas de interesse especificadas  = Marcando este parâmetro, no menu Recrutamento | Seleção por Função, o sistema na etapa da seleção terá que considerar apenas os currículos com áreas de interesse especificadas no Perfil de Triagem.

**Parâmetros RM Labore**  - Campo para visualização do mês competência, ano competência, mês caixa, ano caixa, período e dia de pagamento, como dados de critério de pagamento da empresa, todos parametrizados **apenas pelo RM Labore**. Este campo ficará disponível para preenchimento caso não exista licença do TOTVS Folha de Pagamento (RM Labore).  
   
**Arquivo Anexo** -  Campo para definir o tamanho máximo, em megabyte, dos arquivos que podem ser anexados no RM e no Portal.  
   
**Tipo de Gestão Hierárquica**  - Campo para definição do tipo de gestão hierárquica utilizada pela empresa: Por Seção ou Por Posição.

**Observação:**

**-** Só é possível escolher o tipo de gestão hierárquica "Por Posição" se tiver uma gestão ativa cadastrada na Coligada atual (Gestão Organizacional| Gestões de Hierarquia).  
**-** O tipo de gestão hierárquica (Por Seção/Por Posição) define a visualização de Subordinados em todas as funcionalidades:

Por Seção: os subordinados serão considerados de acordo com a estrutura de Chefes/Supervisores;  
Por Posição: os subordinados serão considerados de acordo com a Gestão de Hierarquia ativa na Coligada atual.

**-** É importante que todas as coligadas da empresa tenham a mesma parametrização do Tipo de Gestão Hierárquica. Caso as coligadas possuam parametrizações distintas o sistema não dará suporte a líder/chefe para coligadas que sejam diferentes da que a pessoa esteja lotada.   
   
**Validações**

Pessoa - Validar unicidade de Pessoa por

**- Nome, Dt. Nascimento, CPF, Estado Natal e Cidade Natal**  Marcando este parâmetro, a validação da unicidade de Pessoas no sistema compara os campos Nome, Dt. Nascimento, CPF, Estado Natal e Cidade Natal com as pessoas já cadastradas no sistema.

**- CPF**  Marcando este parâmetro, a validação da unicidade de Pessoas no sistema compara somente o campo CPF.  Quando este campo for marcado o sistema solicita confirmação do usuário, informando a mensagem que o parâmetro 'CPF Não obrigatório' será desmarcado para todas as coligadas. E se o usuário confirmar a alteração, serão desabilitados os parâmetros 'CPF Não obrigatório' e 'Permitir CPFs duplicados'.  
   
**Observação:**

Quando este parâmetro estiver marcado o campo Dt. Nascimento no cadastro de Pessoas não é obrigatório.  
 As próximas opções 'CPF obrigatório' e 'Permitir CPFs duplicados' ficam desabilitadas para alteração com a validação de unicidade por CPF   
CPF obrigatório  Marcando este parâmetro, no cadastro de Pessoas o sistema obriga o preenchimento do campo CPF.

Se a pessoa cadastrada for estrangeira (nacionalidade diferente de Brasileira), o sistema permite o cadastro sem informar o CPF Permitir CPFs duplicados  Marcando este parâmetro, o sistema permite o cadastro de Pessoas diferentes com CPFs iguais.

**Localizar Pessoa**

 Os parâmetros 'Exibir Dados Básicos', 'Exibir Documentos' e 'Exibir Ambos' permitem escolher quais são as formas disponíveis para localizar pessoa no pré-cadastro de um funcionário.  
   
**Anotações Pessoais**

**- Somente chefes podem aprovar Anotações Pessoais**  - Marcando este parâmetro, ao incluir uma anotação pessoal, deve mostrar no campo 'código do solicitante' somente as pessoas que estiverem cadastradas como chefes no cadastro de chefes/supervisores e que forem chefes do funcionário selecionado.

**Observação:**

Caso a pessoa seja candidato serão exibidos todos os chefes da empresa. Se o funcionário estiver com a situação de demitido e este parâmetro marcado, não vai ser exibido nenhuma pessoa no lookup de 'Campo do solicitante', pois, como o funcionário está como demitido, o mesmo não possui nenhum chefe. Para que seja exibido alguma pessoa neste campo, é necessário desmarcar este parâmetro.  
   
**Atenção:**

 Se o parâmetro 'Tipo de Gestão Hierárquica' (Configurações | Parametrizador | Preferências) estiver definido 'Por Posição', no campo 'código do solicitante' deve mostrar os líderes ativos da Gestão de Hierarquia.

**- Obrigatório Filtro por Perfil para Anotações Pessoais**  - Marcando este parâmetro, deverá existir no perfil do usuário um filtro para validar quais os tipos de anotação serão disponibilizados ao solicitante na inclusão da anotação pessoal. Se o parâmetro for marcado e não tiver filtro no perfil, não será visualizado nenhum tipo de anotação.

**OBS.:**

* Filtro na tabela PANOTAC: Define quais anotações pessoais serão visualizadas na visão do cadastro.
* Filtro na tabela PTPANOTACAO: Define quais anotações pessoais serão visualizadas no lookup "Tipo de anotação", na inclusão/edição do cadastro. Remuneração

**- Considerar os salários das tabelas salariais**  - Marcando este parâmetro, no cadastro de Funcionários o sistema ficará definido para utilização das tabelas salariais. Todos os campos relacionados aos salários dos funcionários serão encontrados através dos cruzamentos de informações de faixas e níveis salariais.

**Observação:**

A vinculação das tabelas salariais pode ser realizada nas Seções, Funções e Quadro de Lotação.

**- Permitir alteração manual do salário**  Marcando este parâmetro, será permitida a alteração manual dos campos relacionados aos salários, na edição do cadastro de Funcionários.

**Observação:**

Este campo somente será habilitado se o campo 'Considerar os salários das tabelas salariais' estiver marcado.

**-** **Usar Seção e/ou Lotação na organização das Tabelas Salariais**

 Marcando este parâmetro, é permitida a vinculação das tabelas salariais somente à Lotação (Seção x Função) e/ou Seção. Caso contrário, é permitida a vinculação somente à Função. Número de meses a verificar participação em Processos Seletivos  Campo para definição do número de meses que a pessoa pode participar de outro processo seletivo no cadastro de Seleção por Função.

**Exemplo:**

Número de meses a verificar participação em Processos Seletivos = 6 meses Ao executar o processo de seleção, a pessoa que participar de um processo de seleção hoje só poderá participar de novo daqui a 6 meses. Utilizar Notação de Órgão Federal  Marcando este parâmetro, há alteração na descrição de alguns cadastros. Cargo será apresentado com denominação de Grupos de Cargos. Função será apresentada com denominação de Cargos. Tarefas serão apresentadas com denominação de Função.  
  
**Acompanhamento do Funcionário**  
   
 Habilitar o Acompanhamento do Funcionário  
 Essa funcionalidade é utilizada apenas para usuário que possui subordinados, o mesmo pode utilizá-la no Portal, em Equipe | Subordinados, selecione um funcionário e vá em Anexos.  
   
**- Descrição para o Anexo "Acompanhamento do Funcionário"**  
 Esse campo é para a escolha da nomenclatura da funcionalidade no anexo.  
   
**- Relatório de Acompanhamento do Funcionário**  
 Esse campo é para a escolha de um relatório que será aberto e gerado de acordo com o funcionário selecionado, trazendo as informações consultadas pelo relatório.  
   
**Redes Sociais**  
   
 Contas para a publicação em redes sociais  
 Essa funcionalidade é para o cadastro de contas das redes sociais FaceBook, Twitter e Linkedin que serão utilizadas para a publicação de vagas pelo RM.
