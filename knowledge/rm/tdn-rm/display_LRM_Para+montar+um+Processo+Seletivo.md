---
content_hash: 04c7a2eba84ae6e6b89ae9ccf9fd1c7510d137bab97ab50e50b10d452b6048d0
fetched_at: '2026-06-29T00:09:36.088910+00:00'
page_id: '425459466'
product: rm
source: tdn-rm
title: Para montar um Processo Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Para+montar+um+Processo+Seletivo
version: 12
---

O cadastro de processo seletivo terá seis guias que agrupam informações necessárias de um processo seletivo, o qual a instituição irá divulgar. As guias são:

**1 - Identificação**

Nesta guia será definida algumas parametrizações possíveis de um processo seletivo

Ativo: indica se um processo seletivo está ou não ativo

Código/Nome: O código é número sequencial que identifica unicamente um processo seletivo e será gerado automaticamente pelo sistema e o nome é para identificação do Processo Seletivo.

Instituição: se o processo seletivo estiver sendo realizado para [terceiros](https://tdn.totvs.com/display/LRM/16+-+Processo+Seletivo+Terceirizado+no+Novo+Portal), deverá ser preenchido com uma instituição existente na tabela auxiliar do Totvs Educacional- Instituição de Ensino.

Arquivo do edital: deverá ser escolhido para este campo o arquivo de edital em formato PDF. Quando for informado o arquivo, na área pública do Portal em detalhes do processo seletivo será disponibilizado um link para que os candidatos possam visualizá-lo.

Categoria do processo seletivo: Vincula o processo seletivo a uma Categoria selecionada. Para que posteriormente o processo seletivo possa ser filtrado por ela.

Valor da inscrição: define um valor de inscrição padrão para o processo seletivo. Ao se incluir uma “Área de Interesse Ofertada”, automaticamente ela irá assumir esse valor como taxa de inscrição. Porém, será possível definir taxas específicas para cada uma das áreas de interesse do processo seletivo.

Max. Inscrições por Candidato: especifica o número de vezes que uma mesma pessoa poderá se inscrever no processo seletivo. Poderão existir processos seletivos nos quais uma mesma pessoa concorrerá em uma ou mais vagas.

Aceita Treineiro: treineiros são candidatos que participarão do processo seletivo a título de experiência. Se for definido que o processo seletivo aceitará treineiros, será possível explicitar tal intenção dos candidatos no ato da inscrição. Conseqüentemente, as rotinas referentes à classificação e chamada irão desconsiderar os candidatos que tenham se declarado como treineiros ao se inscrever.

Visível para todas as filiais? Este parâmetro permite a visão do processo seletivo ou NÃO para todas as filiais. Se este parâmetro for marcado, este processo seletivo será visualizado e controlado por todas as filiais da coligada. O campo [Visível para todas as filiais] será editável somente quando a filial do contexto for a que criou o processo seletivo, para as demais ficará somente leitura.

Utiliza necessidades Especiais? Através deste campo será possível configurar a utilização dos campos de necessidades especiais na inscrição do Portal, ou seja, será possível definir se estes campos estarão ou não visíveis para o candidato no momento de se inscrever em um processo seletivo.  
  
Gerar log de alteração de status? Com este parâmetro habilitado, todas as alterações de status de opções de candidatos serão registradas.

**2 -** **Informações Complementares**

Abrange algumas configurações adicionais para caracterização e parametrização do processo seletivo

Utiliza controle de vagas?: este recurso poderá ser utilizado quando houver a necessidade de realizar um processo seletivo com controle de vagas. Quando esta opção for utilizada o usuário deverá escolher também o tipo do controle de vagas.

Tipo do controle de vagas: Existem duas opções: “Não permitir novas inscrições” e quando atingir o limite de vagas a inscrição será interrompida ou “Permitir novas inscrições" e ao atingir o limite de vagas os candidatos ficarão como excedentes.”

* **Importante**

Quando o processo seletivo utilizar controle de vagas as áreas ofertadas oferecidas pelo mesmo não poderão ter áreas opcionais. Essa regra existe porque a classificação de processos seletivos com controle de vagas é feita somente por ordem de inscrição. Sendo assim, a classificação em uma área opcional iria afetar a ordem de candidatos classificados pelo número de inscrição.  
Utiliza alocação automática?: quando essa opção for marcada, logo que uma inscrição for incluída o sistema tentará vincular o candidato a um local de prova. Se não houver local disponível para a alocação do candidato a inscrição será concluída normalmente. Quando a alocação automática falhar, para alocar o candidato, será necessário disponibilizar novos locais e executar o processo Alocar Candidatos em Locais de Prova ou incluí-lo por meio do anexo Local de prova do candidato. É obrigatório informar um e-mail para o qual serão enviadas mensagens de alerta. Sempre que não for possível alocar automaticamente o candidato, será enviado um e-mail para esse endereço, alertando o responsável sobre a impossibilidade de alocação automática.

Boleto de pagamento de inscrição: deverá ser selecionado para este campo um relatório de boleto que exista no book de relatórios financeiros da instituição. O relatório selecionado será usado como base para geração dos boletos de inscrição no Portal e também por meio do serviço “Inscrição de Candidato”.

Comprovante de inscrição: deverá ser selecionado para este campo um relatório do book de relatórios preparado especificamente para ser o comprovante de Inscrição. O relatório selecionado será utilizado para emissão do comprovante via Portal.

Questionário: deverá ser selecionada para este campo uma prova do tipo “pesquisa de opinião” que tenha sido criada no módulo “RM Testis”. Quando preenchido, os candidatos que fizerem a inscrição pelo Portal deverão responder o questionário sócio-econômico no momento da inscrição. Essa opção deverá ser utilizada, por exemplo, em vestibulares nos quais é necessário que um candidato preencha um questionário sócio-econômico ao se inscrever.

Nome do questionário: através deste campo será possível personalizar o nome do questionário a ser respondido na inscrição do Portal. Se não for configurado nenhum nome o padrão será “Questionário sócio-econômico”. Esta configuração só será utilizada se for definido algum questionário para o processo seletivo.

Utiliza envio de arquivos?: esta opção possibilita que no portal do processo seletivo (somente portal antigo) sejam habilitados campos para envio de arquivos sendo limitado a quantidade informada bem como o tamanho de limite dos arquivos.

**3 - Calendário**

Nessa guia serão definidos os três períodos pelos quais passa um processo seletivo: período de inscrições, período de seleção e período de divulgação de resultados. Para cada um dos três períodos deverá ser definida uma data de início e outra de término. O calendário poderá ser configurado para permitir períodos sobrepostos. Dessa forma, a inscrição, seleção e divulgação de resultado poderão ocorrer de forma paralela.

Importante

As definições de calendário serão fundamentais no decorrer dos processos seletivos, pois afetam diversos serviços. O Portal, por exemplo, irá se basear no calendário para exibir corretamente os processos seletivos e fornecer informações certas aos visitantes e candidatos. Com base no calendário o sistema irá permitir que sejam feitas inscrições somente no período de inscrições. Diversos processos só poderão ser executados em períodos específicos do calendário, exemplificando: não será possível executar o processo “Gerar Inscrições Anônimas” fora do período de inscrição.

**4 - Portaria**

Essa guia possui um único campo que deverá ser preenchido com o texto da portaria que autorizou a realização do processo seletivo. Esse conteúdo, quando preenchido, será exibido no detalhamento do processo seletivo no portal.

**5 - Informações Financeiras**

Nessa guia serão configuradas diversas informações que serão utilizadas na integração com o módulo “RM Fluxus” e “RM Labore”. Os serviços do RM Fluxus se fazem necessários para inclusão de lançamentos financeiros que servirão de base para emissão e baixa de boletos de inscrição. Lançamentos financeiros também são feitos para pagamento de Fornecedores que tenham trabalhado em um processo seletivo. A integração com RM Labore se relaciona ao pagamento de Funcionários que tenham trabalhado em um processo seletivo.

Informações Financeiras Inscrições: Aqui deverão ser definidos os parâmetros para geração dos lançamentos e boletos de inscrição por meio da integração com o RM Fluxus.

Cliente/Fornecedor: deverá ser selecionado um registro de cliente a partir do cadastro de clientes/ fornecedores. Esse registro irá compor o lançamento financeiro de cada uma das inscrições, evitando a necessidade de se criar uma entrada no cadastro de clientes/fornecedores para cada um dos candidatos.

Conta/Caixa: identifica a conta corrente que será utilizada no processo de recebimento dos boletos. Ex: “Santander - C/C - 13-001384-6”.

Tipo de Documento: deverá ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Uma das funções de um registro de “Tipo de Lançamento” é parametrizar o lançamento a ser feito, informando se ele é um lançamento “A pagar” ou “A Receber”. Logicamente, para os lançamentos de inscrição deverão ser usados tipos de registro a “A Receber”. Ex: “Recebimento de Taxas”.

Moeda: moeda corrente que será utilizada na geração dos boletos. Ex: “Real”.

Centro de custo: identifica qual centro de custo é o responsável pela receita gerada com as inscrições. Ex: “1.2.1.0.4 - Direção Acadêmica”.

Histórico: informação textual que irá compor o campo histórico dos lançamentos. Ex: “Inscrição Processo Seletivo 2008 - 1º Semestre”.

Testar geração de lançamento: através deste recurso será possível simular uma geração de lançamento para a inscrição, verificando se os parâmetros financeiros configurados são válidos segundo as regras do RM Fluxus. Após a simulação do lançamento, será exibida uma mensagem para o usuário informando se a configuração é válida ou se houve algum erro. Se houver algum erro a mensagem irá informá-lo.

Filial do lançamento: filial responsável pelos lançamentos. Ex: “Instituição X”.

Tipo Contábil: define qual será o status contábil do lançamento que será criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”.

Departamento do lançamento: departamento da filial responsável pelos lançamentos. Ex: “Diretoria acadêmica”.

Tabelas opcionais: permitem que sejam informados valores para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no RM Fluxus. Serão disponibilizadas 5 combobox referentes a cada uma das 5 tabelas opcionais possíveis de serem parametrizadas no RM Fluxus para serem utilizadas. O combobox só estará habilitado para seleção de algum valor se:  
**1 -** A tabela opcional correspondente foi parametrizada no RM Fluxus para ser utilizada  
**2 -** Na tabela opcional foi inserido um ou mais registros e ao menos um deles está Ativo.

Campos alfa: permitem que sejam informados valores para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no RM Fluxus. Serão disponibilizadas 3 caixas de textos correspondentes a cada um dos três campos alfa opcionais possíveis de serem parametrizados para utilização no RM Fluxus. A caixa de texto só estará habilitada se:  
**1 -** O campo alfa opcional foi parametrizado para ser utilizado no RM Fluxus.

Evento Contábil de inclusão: identifica o registro contábil que deverá será gerado em decorrência do lançamento de inscrição: Ex: “Despesas com Fornecedor”.

OBS: se o tipo contábil for "Contábil", o serviço do Fluxus tentará fazer a contabilização do lançamento. Se a tentativa de contabilizar não for bem sucedida, o lançamento não será feito e, consequentemente, a inscrição também não será. Ou seja, se for para contabilizar, além do evento contábil ter sido definido, é necessário que esse evento esteja com as definições corretas para que se obtenha sucesso na geração do lançamento.

Informações Financeiras Pagamento de Profissionais - Aqui deverão ser definidos os parâmetros para pagamentos dos profissionais através de geração dos lançamentos integrado ao RM Fluxus e pagamentos em folha do funcionário integrado ao RM Labore.

Cliente/Fornecedor: Aqui deverão ser definidos os parâmetros para geração dos lançamentos “A pagar” que deverão ser efetuados para pagamento dos fornecedores durante a execução do processo “Gerar Pagamento de Profissionais”.

Pessoa Física/Pessoa Jurídica: Tipo de Documento: aqui vale o mesmo que foi descrito para o campo “Tipo de Documento” no item “Informações Financeiras - Inscrições”. A diferença é que para este campo deverá ser escolhido um tipo de documento A Pagar. Esse tipo de documento irá compor os lançamentos de pagamento dos fornecedores. A parametrização deste campo é diferenciada de acordo com o tipo de fornecedor: pessoa física ou jurídica. Ex: “NF RPA - RPA”.

Código de Receita: esse campo também se diferencia conforme o tipo de pessoa do fornecedor. Esse campo deve ser preenchido se o respectivo “Tipo de Documento” possui, no RM Fluxus, as classificações “Gerar IRRF” ou “Gerar IRRF e INSS”. Ex: “0561 - Rend. Trabalho Assalariado”.

* **Importante**

Se o código de receita não for preenchido e o tipo de documento é um tipo parametrizado para reter imposto de renda sobre o lançamento, o serviço de integração não fará o lançamento de pagamento. Será gerado um erro.  
Natureza orçamentária financeira: permite que seja definidada o código da natureza financeira dos lançamentos que serão gerados através do serviço de integração com o RM Fluxus. A definição de um valor para este campo é opcional. Porém, se no RM Fluxus estiver parametrizado que é obrigatório informar o código de natureza, esse campo deverá ser preenchido para que seja repassado ao serviço de inclusão. Veja a seguir as possibilidades de utilização desse parâmetro de acordo com o que pode ser configurado no Fluxus:

Natureza Financeira Obrigatória no Fluxus: uma natureza financeira deverá ser parametrizada e sempre será passada para o Fluxus durante a geração de lançamentos. Quando não informado no Processo Seletivo, o Fluxus retornará uma exceção na inclusão do lançamento.  
Natureza Financeira Não Obrigatória: não é necessário definir uma natureza financeira. Se tiver sido definido um valor para o campo, ele será passado e registrado pelo Fluxus durante a geração de lançamentos. Porém, se não tiver sido definido um valor o lançamento será realizado normalmente.  
Não Utilizar Natureza Financeira: a natureza financeira não será registrada pelo Fluxus mesmo que o campo tenha sido preenchido no Processo Seletivo.  
Informações Financeiras - Pagamento de Profissionais - Funcionários.

Evento: deve ser configurado com o código do evento que irá compor o código fixo que será cadastrado para os funcionários pelo serviço de pagamento de profissionais. Ex: “200- Serviços prestados no Vestibular”.

Tipo de Código Fixo: o valor deste campo também irá compor o registro de código fixo que será cadastrado para os funcionários. No cadastro do RM Labore, este campo tem a função de permitir agrupar Códigos fixos para efeito de lançamento na movimentação.

Teste de geração de lançamento: para testar as configurações financeiras para pagamento de profissionais.

Disponibilizar pagamento de cartão de crédito no portal: Este parâmetro tem como objetivo, permitir que os candidatos do processo seletivo possam efetuar o pagamento da inscrição através do portal utilizando cartão de crédito. O pagamento ficará disponível nos serviços de Impressão após a inscrição do candidato e em 2ª via de boleto e será exibido um ícone, possibilitando ao usuário clicar na tela para informação dos dados de cartão de crédito, caso o processo seletivo esteja configurado. Caso contrário, será exibido somente o código IPTE do boleto e a opção de impressão do boleto.

Importante: Para realizar o pagamento da inscrição via cartão de crédito é preciso que seja parametrizado no RM Fluxus as configurações do cartão de crédito.

**6 - E-mails**

Nessa guia será parametrizado o envio de e-mail de confirmação de inscrição de candidato no portal por processo seletivo.

Enviar e-mail de confirmação de inscrição: Determina se será enviado o e-mail de confirmação de inscrição do candidato, após a inscrição sistema envia um e-mail de confirmação da inscrição.

Utilizar texto de e-mail personalizado (Confirmação de inscrição): Se a opção de e-mail correspondente for utilizada esse parâmetro ficará ativo e irá determinar o conteúdo do e-mail. Se ficar desmarcado será usado o texto de e-mail interno e fixo do sistema, determinado em parâmetros do sistema.

Texto do e-mail (Confirmação de inscrição): permite definir um texto personalizado caso a opção de utilizar texto de e-mail personalizado seja marcada poderão ser utilizadas tags no corpo do texto, quando enviadas serão substituídas pelos dados do candidato.

* Para utilização do envio de e-mail para confirmação de inscrição do candidato deve-se:

Estar habilitado como visível e obrigatório o campo e-mail na configuração de “campos de candidato” em parâmetros do sistema (Portal/ Pessoa/ Dados básicos). Uma vez que o campo E-mail não foi habilitado no cadastro de candidato não terá como o sistema enviar e-mails para o mesmo.  
Caso estiver habilitado o parâmetro "Utilizar responsável por candidato na inscrição" ao invés de "campos de candidato", deve-se validar os "campos de responsáveis".  
O campo E-mail de remetente do processo seletivo também deverá ser preenchido.

**7 - Forma de Inscrição**

Nessa guia poderá ser configurada uma ou mais formas de inscrição para o processo seletivo. A possibilidade de definir várias formas de inscrição em um processo seletivo agrega uma enorme flexibilidade para a instituição realizadora. Citando alguns exemplos, será possível:

* Configurar descontos diferenciados para determinados tipos de candidatos
* Configurar descontos para inscrições feitas somente em determinados períodos
* Especificar prazos de vencimentos diferentes para os boletos de inscrição
* Oferecer condições específicas para inscrições feitas pela Internet
* Limitar as datas em que será possível fazer inscrições pela Internet
* Configurar “tipos de indicações” para determinados tipos de candidatos
* Configurar a faixa etária (idade máxima e mínima) dos candidatos que poderão se cadastrar usando determinada forma de inscrição.
* Configurar a forma de inscrição para ser do tipo ENEM, ou seja, se a forma de inscrição selecionada for tipo ENEM e a Área ofertada utilizar ENEM, será obrigatório o preenchimento no ato da inscrição os campos Número da Inscrição ENEM e Ano de referência. Se a forma de inscrição selecionada exigir o preenchimento e a área ofertada NÂO utilizar ENEM, o usuário deverá alterar a forma de inscrição para conseguir finalizar sua inscrição.

Para cada uma das formas de inscrições cadastradas em um processo seletivo será necessário detalhar uma série de informações:

Data do início/Data do término: define o período no qual o sistema permitirá que sejam feitas inscrições desse tipo. Quando o período definido expirar, o sistema irá parar de exibir essa forma inscrição tanto do formulário de inscrição Web como WinForms. Ou seja, após o término do período não será possível incluir novas inscrições daquele tipo.

Número de dias para venc.: permite que seja especificado dentro de quantos dias o boleto de inscrição irá vencer a partir da sua emissão.

Data limite de vencimento: esse parâmetro limita o parâmetro “Número de dias para venc.”, fixando uma data máxima para o vencimento. Isso possibilita que seja dado um prazo para que o candidato efetue o pagamento do boleto desde que esse prazo não extrapole determinada data. Por exemplo, pode ser definido que o boleto sempre vencerá dentro de quatro dias após a emissão, porém a sua data de vencimento não poderá extrapolar o término do período de inscrições.

% Desconto: permite que seja configurado um valor de desconto para inscrições feitas dentro da forma que está sendo criada. Quando for feita uma inscrição desse tipo, será dado o desconto aplicando-se este percentual sobre o valor da taxa de inscrição da área de interesse escolhida. Por exemplo, se for informado para este campo um valor de 50% e o candidato se inscrever em uma área cuja taxa de inscrição seja de R$60,00, o boleto será gerado para ele com o valor de R$30,00.

Indicação de Aluno, Funcionário e Cliente/Fornecedor: Marcando estas opções no ato de uma inscrição via Web ou WinForms será identificado o número de registro do aluno,Funcionário e Cliente/Fornecedor que indicou o processo seletivo para o candidato.

Disponível na Internet: se essa opção estiver marcada os candidatos poderão optar por ele ao se inscrever pelo portal. Obs.: todas as formas de inscrição estarão disponíveis via WinForms independentemente dessa opção estar ou não marcada.

Idade mínima e Idade máxima: definem uma faixa etária para limitar a idade dos candidatos que podem se inscrever usando tal forma de inscrição. A idade máxima sempre terá que ser maior que a idade mínima.

Opcionalmente, o usuário poderá criar campos complementares para compor o cadastro. Nesse caso, além das guias citadas anteriormente, estará presente também a guia “Campos complementares”, ela será disponibilizada no sistema pelo Menu Cadastro| Campos complementares| Processo seletivo. No caso do Totvs Educacional, para que os campos complementares apareçam é preciso que sejam habilitados para a filial através do processo "Habilitar/Desabilitar campos complementares na filial".   
Identificador de Recursos
