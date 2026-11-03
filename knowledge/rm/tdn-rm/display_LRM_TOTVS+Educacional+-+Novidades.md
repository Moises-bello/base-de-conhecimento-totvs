---
content_hash: 82da1613a9cb131a891122d4ab5765c238be6fbe19469c6ddab04644568afee9
fetched_at: '2026-06-29T00:09:37.325019+00:00'
page_id: '425459585'
product: rm
source: tdn-rm
title: TOTVS Educacional - Novidades
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Educacional+-+Novidades
version: 12
---

---

****12.1.23**[Simulação de parcelas de contratos utilizando plano de pagamento via webservice](http://tdn.totvs.com/pages/viewpage.action?pageId=439359754) ***********Novo!!!*************

Disponibilizado via webservice a possibilidade de simular valores de parcelas de contratos de alunos através da configuração de parcelas de planos de pagamentos e concessão de bolsas futuras.

****12.1.23 - [Detalhamento do Cálculo da Parcela por](http://tdn.totvs.com/pages/viewpage.action?pageId=412886824) [Disciplina](http://tdn.totvs.com/pages/viewpage.action?pageId=412886824) *******Novo!!!***********No processo de geração do lançamento o TOTVS Educacional gravará o detalhamento do cálculo da parcela conforme as disciplinas matriculadas, levando em consideração a parametrização que define como os crédito serão processados.

****12.1.23 - [Detalhamento dos valores da parcela do contrato via Webservice](http://tdn.totvs.com/display/LRM/Detalhamento+dos+valores+da+parcela+do+contrato) ***********Novo!!!***************Disponibilizado via webservice o retorna do detalhamento dos valores da parcelas de contrato com lançamentos financeiros gerados baseados em turmas disciplinas, bolsas condicionais, bolsa incondicionais, desconto por antecipação ou conta corrente.

****12.1.23 -**[Composição dos valores da parcela](http://tdn.totvs.com/pages/viewpage.action?pageId=420547412) ***************Novo!!!*****************Disponibilizado na parcela a opção "Detalhamento do cálculo" que retorna de forma detalhada informações relacionadas aos valores que compõem o cálculo da parcela, tais como cálculo por crédito das disciplinas, descontos de parcelas, descontos por antecipação, aproveitamento de conta corrente, detalhamento das bolsas condicionais e incondicionais entre outros.

****12.1.21 - **[Validação da complexidade da Senha](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458897)*****Novo!!!*******Disponibilizado a opção nós parâmetros para validar a complexidade da senha do usuário, para essa validação deverá ser configurando os itens: Tamanho mínimo, conter caracteres maiúsculos, caracteres minúsculos, símbolos e números

****12.1.20**[Simulação de parcelas de contratos via webservice](http://tdn.totvs.com/pages/viewpage.action?pageId=392496907) ***********Novo!!!*************Disponibilizado via webservice a possibilidade do usuário simular os valores a serem pagos pelo aluno antes de efetuarem a matrícula nas disciplinas de determinadas turmas, ou seja, não é necessário ter matrícula nas disciplinas para que o cálculo das parcelas seja feito.

****12.1.20 - [Geração de lançamento de bolsa de crédito com tipo contábil e evento](http://tdn.totvs.com.br/pages/editpage.action?pageId=425459541)*******Novo!!!***********Disponibilizado parâmetros para informar o tipo contábil da bolsa de crédito e setar o evento contábil na inclusão do lançamento de bolsa de crédito.

**12.1.20 - Somatório do percentual de bolsas maior que 100% no contrato do aluno** ***Novo!!!***Diante alguma necessidade especifica da instituição de ensino houve uma evolução no sistema para que seja permitido adicionar bolsas no contrato do aluno cujo o somatório do percentual ultrapasse 100%. Para isso é preciso que a bolsa vinculada ao contrato do aluno tenha alguma fórmula vinculada, pois neste caso a regra estará na própria fórmula.

**12.1.20 -****[**Afeta Base de Cálculo**](http://tdn.totvs.com/pages/releaseview.action?pageId=325847718)** ***Novo!!!***A fim de informar se uma bolsa afeta a base de cálculo de outras bolsas (Somar Bolsas ou Aplicar Somente a Maior Bolsa) ou do desconto por antecipação, foi criado um campo no cadastro de bolsas, cadastro de bolsas de contratos e concessão de bolsas futuras. Esse campo estará disponível apenas quando o Tipo de Bolsas for por Contrato e após rodar script CN.2018.04\_12 e outros scripts para desconto por antecipação. Recurso disponível ao rodar script específico na 12.1.20 e nativamente na versão 12.1.21.   
Mais detalhes em [desconto por antecipação no TDN](http://tdn.totvs.com/pages/viewpage.action?pageId=325847718)

**12.1.20 -**[**Ordem de Aplicação do Desconto por Antecipação**](http://tdn.totvs.com/pages/releaseview.action?pageId=325847718) ***Novo!!!***   
A fim de possibilitar que um desconto por antecipação seja aplicado após o cálculo de uma determinada bolsa, foi criado o campo "Aplicar desconto por antecipação" no cadastro de bolsas, no cadastro de bolsas de contratos dos alunos e no cadastro de concessão de bolsas futuras. Recurso disponível ao rodar script específico na 12.1.20 e nativamente na versão 12.1.21.

**12.1.20 -** ****Alterar Vencimento do Desconto por Antecipação do Lançamento**** ***Novo!!!***Implementado processo para alterar vencimento do desconto por antecipação do lançamento, permitindo as instituições que seja possível alterar data de vencimentos do desconto caso os lançamentos já tenham sido processados.

**12.1.20 -** **Geração de movimento por competência em nome do responsável pelo contrato do aluno**   
Otimização realizada na geração de movimento por competência que passa a possibilitar a geração de movimentos em nome do responsável pelo contrato do aluno. Para isto foi incluída uma opção no cadastro do responsável financeiro do contrato do aluno para identificá-lo como responsável pelo movimento. Assim, ao gerar o movimento por regime de competência, basta selecionar para qual tipo de responsável o movimento será gerado: Responsável do aluno ou Responsável do contrato.

**12.1.20 -** **Prévia dos Valores do Lançamento**   
Implementado o processo de geração de Prévia dos Valores do Lançamento facilitando assim a conferência antes da geração oficial dos lançamentos financeiros. A Prévia gerada dos valores dos lançamentos é um espelho financeiro, pois utiliza as mesmas regras aplicadas na geração de lançamentos.

**12.1.20 -** **Melhoria no Censo Escolar**   
As rotinas do Censo (Básico e Superior) foram alteradas para buscar consultas internas do sistema, quando não houver configuração de consulta nos parâmetros do Censo. Além da alteração do local dos Menus de censo. Agora dentro da aba atividades acadêmicas contém o menu Censo.

**12.1.20 -**[**Alteração de senha no Novo Portal do aluno**](http://tdn.totvs.com/display/LRM/Alterar+Senha) ***Novo!!!***   
Disponibilizado a opção para permitir que o Aluno/Responsável altere a senha no Novo portal do aluno.

**12.1.20 -** **[Geração de lançamentos - Seleção de alunos por arquivo](http://tdn.totvs.com/pages/viewpage.action?pageId=334348063)*****Novo!!!***   
Disponibilizado no processo de geração de lançamentos a possiblidade de selecionar alunos a partir de um arquivo de texto ou planilhas do excel.

**12.1.20 -** **Função de fórmula QtdCoEmCurso** ***Novo!!!***   
Foi criada a fórmula QtdCoEmCurso, para retornar á quantidade de disciplinas, de crédito ou carga horária em curso, de um determinado período letivo ou até um período determinado.

**12.1.20 -**[**Novo portal do aluno - Login de acesso para a funcionalidade específica**](http://tdn.totvs.com/display/LRM/Login+-+Redirecionamento+para+funcionalidade)***Novo!!!***   
Otimizado o processo para permitir que o login do usuário seja redirecionado para funcionalidade do portal após login.

**12.1.20 -** [**Novo Portal do Aluno - Notas/Faltas Unificadas**](http://tdn.totvs.com/pages/viewpage.action?pageId=333779270)***Novo!!!***   
Otimizado o processo para unificar a visualização das notas e faltas das etapas de todas as disciplinas em que o aluno está matriculado no período letivo.

**12.1.19 -** [**Totvs eduCONNECT - Atividade de fórmula visual para enviar mensagens ao eduCONNECT**](http://tdn.totvs.com/pages/viewpage.action?pageId=329038161) Otimizar o processo para permitir que os usuários do TOTVS Educacional envie mensagens para seus usuários do TOTVS eduCONNECT.

**12.1.19 -** [**Totvs eduCONNECT - Possibilidade de visualizar/acessar links no corpo do texto das mensagens**](http://tdn.totvs.com/pages/viewpage.action?pageId=287075314) Otimizar o processo para acessar links no corpo do texto das mensagens no eduCONNECT.

**12.1.19 -** [**Totvs eduCONNECT - Permissionamento do eduCONNECT**](http://tdn.totvs.com/pages/viewpage.action?pageId=287075301) Otimizar o processo para permitir realizar a autenticação e acesso através do aplicativo.

**12.1.19 -**[**Totvs eduCONNECT - Parametrização da URL do Educa Mobile**](http://tdn.totvs.com/display/LRM/DT+Parametrizar+URL+do+Educa+Mobile)   
Otimizar o processo para permitir a alteração da URL do Educa Mobile.

**12.1.19 -** [**Totvs eduCONNECT - Opção para adicionar lembrete no calendário do dispositivo**](http://tdn.totvs.com/display/LRM/DT+Adicionar+mensagem+como+compromisso+do+eduCONNECT) Otimizar a opção de adicionar evento na edição da mensagem, que possibilita a criação de um compromisso no calendário do dispositivo Android ou iOS.

**12.1.19 -** **[Novo Portal do Processo Seletivo - Parametrização do conteúdo do corpo da página de informações, inscrições e resultado em formato HTML](http://tdn.totvs.com/pages/viewpage.action?pageId=312148088)**Otimizado o processo para transformar o Texto Formatado em código HTML nas páginas: Informações, Inscrição e Resultados.

**12.1.19 -** [**Novo Portal do Aluno - Rematrícula Ensino Básico**](http://tdn.totvs.com/pages/viewpage.action?pageId=315906285)  
Disponível no Novo portal do aluno, o processo de Rematrícula para o contexto Ensino Básico.

**12.1.19 -** **Usar campo dedução para informar valor de desconto no item de movimento**   
Preenchimento de campos de valores de Dedução de ISS para valores de bolsas incondicionais e descontos.

**12.1.19 -** **Personalização do Plano de Pagamento**   
Otimização realizada na personalização do plano de pagamento apresentando uma melhor usabilidade, facilitando e flexibilizando a forma de personalização.

**12.1.19 -** **Evolução do cadastro de Parametrização por curso**  
 Ao realizar o cadastro da parametrização por curso é possível configurar a sugestão de disciplina. Assim, durante o processo de matricula o usuário conseguirá visualizar no campo sugestões de disciplina, disciplinas de outro curso, de outro turno ou outra filial, conforme o informado no cadastro da parametrização.

**12.1.19 -** **Atualização do valor de crédito das disciplinas por percentual**   
Otimização realizada no processo de Atualizar número e valor de créditos das disciplinas, permitindo reajustar valores do crédito das disciplinas por percentual.

**12.1.19 -** **Exclusão de contratos cancelados**   
Otimização realizada na exclusão de contratos aplicada em contratos *'Cancelados'* permitindo que estes sejam excluídos mesmo que possuam parcelas. Para estes casos, o sistema excluirá automaticamente todas as parcelas, desde que estas parcelas não tenham lançamentos financeiros gerados, e em seguida excluirá o contrato.

********12.1.18 - [Usar número de crédito da matriz ou total de crédito financeiro da matriz em caso de equivalência múltipla](http://tdn.totvs.com.br/display/LRM/Financeiro+-+EDU+-+Duplicado+3) *******Novo!!!***************Disponibilizado novo parâmetro que faz com que o sistema use número de crédito da matriz e o parâmetro para usar o total de créditos financeiro da disciplina da matriz curricular do aluno em caso de equivalência múltipla.

******12.1.18 - **[Local de prestação do serviço é diferente do endereço do tomador](http://tdn.totvs.com.br/display/LRM/NF-e) *******Novo!!!***************Disponibilizado a opção de criar os campos complementares para a situação em que o município de prestação do serviço é diferente do tomador.  
Durante a geração de movimento o sistema verifica se o município do cliente é diferente do município da Filial, e o Educacional cópia automaticamente as informações do endereço da Filial para os respectivos campos complementares parametrizados.

**12.1.18 -** **[**Alteração no processo seletivo terceirizado**](http://tdn.totvs.com.br/display/LRM/Processo+Seletivo+Terceirizado+-+EDU)** ***Novo!!!***Foram inclusos os campos Tipo de rua, Tipo de bairro, País, Cor/Raça, Grau/Escolaridade, Situação ocupacional e Data de emissão da identidade no layout de importação de arquivo e no cadastro do processo seletivo.

**12.1.18.127 -**[**Digitação de Frequência diária por Turma**](http://tdn.totvs.com/pages/viewpage.action?pageId=318610173)   
 Otimizado o processo para permitir que o professor registre a falta para um aluno ou mais alunos, e ela será registrada para todas as turmas/disciplinas daquele professor no dia informado

**12.1.18 -** **[Parametrização dos serviços que podem ser pagos com cartão](http://tdn.totvs.com/pages/viewpage.action?pageId=311626407)**No cadastro dos serviços financeiros do TOTVS Educacional, foram criadas duas novas opções para cada serviço onde o usuário poderá marcar quais serviços sejam pagos com cartão de crédito e quais poderão ser pagos com cartão de débito.

**12.1.18 -** **Inadimplência**  
 Com as mudanças realizadas pelo TOTVS Gestão Financeira em função de boleto registrado, ao realizar um *Acordo* financeiro o boleto já remetido ao banco não é mais 'Cancelado' permanecendo 'Em aberto', com isso foi necessário evoluir o serviço de validação de inadimplência que passa a *não* validar como inadimplentes lançamentos que estiverem com status 'Baixado por Acordo'.

**12.1.18 -** **Regeração de Lançamentos**Evolução realizada nos procedimentos de regeração de lançamentos financeiros realizada diretamente no TOTVS Educacional para lançamentos que tenham boletos com status igual a "Remetido" ou "Registrado". Para auxiliar na regeração destes lançamentos foi criado o parâmetro *'Cancelar Remessa automaticamente ao regerar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado'**.*

*-* Na regeração de lançamentos, realizada diretamente no TOTVS Educacional, se os lançamentos não tiverem boletos ou os seus boletos estiverem todos cancelados, o sistema incluirá automaticamente novos boletos para os lançamentos que estiverem sendo regerados, porém, na regeração de lançamentos as regras de agrupamento de lançamentos não serão aplicadas, sendo incluído um boleto para cada lançamento. Se desejar que as regras de agrupamento de lançamentos sejam aplicadas, os lançamentos envolvidos deverão ser cancelados e incluídos novamente.

**12.1.18 -****Eventos Contábeis – Contabilização por competência**  
 Evolução realizada no cadastro de eventos contábeis dos processos de *Aumento* e de *Cancelamento* utilizados na contabilização por competência ampliando a possibilidade de buscas de *Centro de Custo* em sua parametrização além da possibilidade de ordenação e priorização desta busca, igualando-se assim, à forma de parametrização dos eventos utilizados pelos processos de contabilização de Contrato e Parcelas.

**12.1.18 - Inadimplência**Com o objetivo de padronizar as regras de validação de inadimplência dos alunos, a validação realizada pelo sistema (MDI) foi evoluída passando a considerar a data de vencimento do *boleto* e não mais a data de vencimento do lançamento. Este comportamento já era aplicado nas validações realizadas pelo Portal. Agora, sistema e Portal, utilizam as mesmas regras de validação de inadimplência.

**12.1.18 -****Cancelamento de lançamentos provenientes do TOTVS Educacional - Bolsa de crédito**  
 Melhoria na validação do cancelamento de lançamentos provenientes do TOTVS Educacional, para que não seja possível cancelar um lançamento originado de uma bolsa de crédito. Caso o lançamento selecionado para o cancelamento possua lançamentos oriundos de bolsa crédito vinculado, será executado o cancelamento tanto dos lançamentos de bolsa de crédito quanto do lançamentos selecionado no processo.

**12.1.18 -****Impressão de boletos provenientes de convênios de cobrança registrada**  
 Criado o parâmetro 'Permite a impressão de boletos não registrados' para controlar a impressão de boletos realizada diretamente no Educacional. Ele será usado para permitir ou não a impressão de boletos provenientes de convênios de cobrança registrada mas que ainda não tenham sido registrados nos bancos.  
 Este novo parâmetro está disponível em Ambiente | Parâmetros | Educacional | Tesouraria | Relatórios.

**12.1.18 -****Ajustes no processo de Transferência Interna que passa a atualizar a matriz aplicada dos registros da conta corrente**  
 Ao realizar o processo de Transferência Interna para alunos que possuírem débitos ou créditos na conta corrente e que optarem por cancelar o contrato antigo (original) e gerar um novo contrato, o sistema atualizará automaticamente a matriz aplicada dos registros da conta corrente dos alunos com a informação da matriz aplicada utilizada como destino neste processo, assim os registros da conta corrente do aluno estarão sempre vinculados a contratos ativos.  
 Na visão da **conta corrente** do aluno também foi disponibilizada a opção de edição, permitindo ao usuário alterar manualmente a matriz aplicada do registro da conta corrente, sendo possível selecionar entre as matrizes do aluno que estiverem vinculadas a contratos ativos, ou seja, contratos que não estiverem cancelados. A permissão para edição da matriz aplicada pela visão da conta corrente é atribuída no Perfil do usuário (Serviços Globais | Segurança | Perfis | Educacional | Educacional >> 01.01.01.12.01 - Editar matriz aplicada no registro da conta corrente).

**12.1.18 -****Importador TOTVS Educacional**  
 Melhoria realizada no Importador do Educacional que passa a contemplar também a tabela SLOGHABILITACAOALUNO, além da revisão na importação da tabela STURNO, que passa a suportar acentos em sua descrição.

**12.1.18 -****Bolsa Retroativa**   
O processo para Inclusão ou Exclusão de Bolsa retroativa foi otimizado, permitindo que possa se incluir ou excluir uma bolsa mediante parametrização , mesmo que os boletos em abertos estejam remetidos ou registrados.

**12.1.18 -****Concessão de Bolsas Futuras**   
O processo de concessão de bolsas futuras foi otimizado, permitindo que a mesma bolsa possa ser concedida para o mesmo aluno em períodos distintos.

**12.1.18 -****NF-e - Geração de movimento por competência**   
Das versões 12.1.15 até a versão atual, foi realizado um ajuste no processo de geração de movimentação em regime de competência, permitindo ao sistema gerar movimentação em regime de caixa para boletos oriundos de parcelas do tipo extra, mesmo quando o sistema estiver parametrizado para gerar movimento em regime de competência.

**12.1.18 -****Melhoria realizada no LOG do processo de Incluir/Excluir Bolsas Retroativas**  
 O LOG passa a apresentar informações das bolsas concedidas ou excluídas, além de detalhar de forma mais organizada e objetiva os contratos, RA, parcelas e lançamentos que foram atualizados. Os erros apresentados durante a execução do processo ficam separados ao final do LOG demonstrando informações dos contratos e lançamentos que não foram atualizados.

**12.1.17 -****Geração de Usuário personalizada**   
Otimização do processo de geração de usuário para um novo tipo de personalização chamado "nome + sobrenome + sequencial". Pra toda geração de usuário, seja ele aluno, professor, responsável acadêmico, pai ou mãe, coordenador ou funcionário, quando existir uma pessoa de mesmo nome e sobrenome no sistema e a geração de usuário estiver definida com essa personalização, o sistema irá adicionar um auto incremento. Ex: "MARIA"+"CLARA" o próximo usuário seria "MARIA" + "CLARA"+1.

**12.1.17 -****LMS – Parâmetro da Integração INT\_EDU\_LMS\_ATIVA\_INT\_DISC**   
Caso o parâmetro de integração "INT\_EDU\_LMS\_ATIVA\_INT\_DISC" esteja selecionado, somente os registros que se relacionam as disciplinas integradas ao LMS serão enviados na integração. No cadastro de disciplinas é possível informar se a disciplina deve ser integrada ao LMS.

**12.1.17 -****Cadastro de Pessoas Integração Protheus**   
Se a integração estiver ativa, todo aluno, Pesquisador, Participante de Banca de Estágio e TCC cadastrados no Educacional terá o seu correspondente no cadastro de pessoas do Protheus. Ao alterar ou excluir qualquer um dos cadastros, as alterações serão refletidas no Protheus.

**12.1.17 -****Formatação de casas decimais do campo Percentual/Valor nos processos correlatos à Bolsa**Evolução realizada nos processos que utilizam Bolsa, com relação à quantidade de casas decimais utilizadas na digitação dos seus valores, passando a respeitar a parametrização definida no TOTVS Gestão Financeira da seguinte forma: Se o tipo de desconto for indicado por *Percentual*, a quantidade de casas decimais utilizadas na digitação irá respeitar a quantidade de casas decimais definida no parâmetro do sistema financeiro "Nº Decimais Percentual". Se o tipo de desconto for indicado por *Valor*, a quantidade de casas decimais utilizadas na digitação irá respeitar a quantidade de casas decimais definida no parâmetro do sistema financeiro "Nº Casas Decimais".

**12.1.17 -****Arquivos anexos da reserva de** **Recurso e de Instalação**   
Otimização realizada através da criação de *tags* no Perfil de usuário para incluir, editar e/ou excluir arquivos às Reservas de Recurso e de Instalação permitindo assim maior controle na manipulação destes arquivos.

**12.1.17 -****Atualiza parcelas do contrato**   
Otimização realizada no processo de atualização das parcelas do contrato para que sempre que o usuário selecionar o campo "Valor do desconto" automaticamente o sistema selecione o campo "Tipo de desconto" ou vice versa, garantindo assim que as duas informações fiquem atualizadas nas parcelas dos contratos dos alunos.

**12.1.16 -****Repasse de Bolsa**   
Melhoria realizada no Repasse de Bolsa quando o valor do repasse for *menor* que o valor financeiro devido: Nestes casos, o valor da baixa atribuído ao lançamento financeiro referente à bolsa de crédito será o valor cadastrado no repasse, e o restante a receber, encontrado entre a diferença do valor total do lançamento e o valor do repasse, será lançado no campo 'Valor de integração' do respectivo item de baixa, completando assim o valor total do lançamento.

**12.1.16 -****Contabilização por competência**   
Otimização realizada no processo de contabilização por competência para quem utiliza o *segundo* para modelo de contabilização, permitindo definir quais Bolsas deverão ser consideradas e computadas pelo processo. Para isto foi criada a opção 'Compõe contabilização por competência' dentro do cadastro de Bolsas. Se marcada, a bolsa com seus respectivos valores será considerada na contabilização do contrato e na apropriação mensal conforme o evento contábil utilizado, se desmarcada, a bolsa com seus respectivos valores não será contabilizada pelo regime de competência.

**12.1.16 -****Matrículas equivalentes vinculadas ao TCC**   
Alterado o comportamento do sistema para permitir que disciplinas equivalentes possam ser listadas e associadas no anexo "Matrículas vinculadas ao TCC" no TCC do aluno.

**12.1.15 -****Projeto de Pesquisa**  
 Agora é possível alterar a situação de todos os projetos de pesquisa para arquivado ou em execução desde que a situação de origem seja "Recomendado".

**12.1.15 -****Conta corrente**  
 O aproveitamento de valores da conta corrente, para alunos com crédito, não mais utilizará o campo opcional de desconto, parametrizado na integração financeira. Sendo assim, os lançamentos financeiros não serão mais gerados com valor original em dobro.

**12.1.15 -****Integração Urânia**  
 O Urânia é um software de elaboração de horários para as turmas bem como para os professores. Ao final do seu processamento, o Urânia irá oferecer o dia da semana em que a turma/disciplina deve ser ofertada, o seu horário, e qual é o professor deste horário

**12.1.15 -****Projeto de Pesquisa & Extensão**  
 Mudanças no processo para submeter um projeto de Pesquisa/Extensão, é possível submeter com bolsista responsável pela atividade ( sem o vínculo do pesquisador/extensionista que será o responsável pela atividade) para avaliação e submeter o cadastro de bolsista realizando a vinculação do pesquisador/extensionista da equipe.

**12.1.15 -****Solicitação de estágio no portal**  
 Melhoria no processo de solicitação de estágio, agora o aluno consegue cadastrar mais de um funcionário para a empresa mediante permissão.

**12.1.15 -****Cadastro de Aluno Egresso**  
 Esta funcionalidade tem como objetivo permitir que alunos egressos que não estão na base RM possam solicitar seu cadastro através de uma página pública e que esse cadastro seja aprovado/reprovado através do fluxo: Cadastro de Aluno (fluig).

**12.1.15 -****Projeto Inovação**  
 Melhorias no projeto de inovação: Foram criados dois novos campos: Campo Aplicação e Acesso Tecnológico; estes campos são utilizados no preenchimento do formulário (fluig) dos eventos: Desenho industrial, Programa de computador, Obra literária e Cultivar/Biológico.

**12.1.15 -** **Geração de movimento - Regime de caixa**   
Com objetivo de flexibilizar a parametrização de composição do valor do item de movimento gerado por regime de caixa foi realizada uma evolução na parametrização deste recurso permitindo ao cliente parametrizar fórmulas que contemplem regras específicas da empresa e que serão responsáveis por calcular o valor líquido (baseado no lançamento financeiro) que irá compor o valor do item do movimento. Neste caso, a criação das fórmulas serão de responsabilidade do cliente. O novo parâmetro '*Valor líquido (calculado por fórmula)*' encontra-se em Ambiente | Parâmetros | Educacional | Integração | Fiscal.

**12.1.15 -** **Geração de movimento por competência**  
 Otimização realizada para que ao gerar movimento por competência, utilizando 'Valor líquido' para cálculo do valor do item de movimento, caso o valor de desconto supere o valor original do item, o movimento seja gerado atribuindo zero ao valor líquido do item de movimento.

**12.1.14 -****Data de Contabilização e de Estorno na contabilização por competência**   
Melhoria realizada no processo de contabilização por competência de forma a permitir que na execução do processo possa ser informada a data de contabilização para os lançamentos contábeis. A informação da data de contabilização não é obrigatória e caso não seja preenchida, as atuais regras continuarão sendo respeitadas. O sistema não permitirá a contabilização, caso a data informada na tela do processo seja maior que a data atual do sistema.

**12.1.14 -****Contabilização por competência - Novo Modelo**   
Otimização realizada para permitir a configuração de itens de evento de bolsa e de descontos nos eventos de cancelamento/aumento de contrato e nos eventos de cancelamento/aumento mensais. Com isto, os aumentos e cancelamentos de bolsas e de descontos e seus diferimentos mensais passarão a utilizar os eventos configurados para aumentos e cancelamentos. Desta forma, o complemento do histórico em caso de cancelamento/aumento de bolsas e de descontos, obedecerá a parametrização dos respectivos eventos de cancelamento/aumento.

**12.1.14 - Pagamento de boleto com cartão de crédito no Portal**   
Otimizada a operação de pagamento de boleto com cartão de crédito, onde os dados enviados para a operadora de cartão de crédito serão os dados do responsável financeiro do boleto (dados do cliente pagador – CPF / CNPJ, etc.).  
  
**12.1.14 - Impressão de boletos no Portal**   
Implementado o parâmetro '*Apresentar boleto de cobrança registrada ainda não registrado no Portal*' para permitir que os boletos originados de cobrança registrada que ainda não estiverem registrados nos bancos possam ser impressos no Portal do aluno. Este parâmetro está disponível em Ambiente | Parâmetros | Educacional | RM Portal Gerais | Portal Geral 8/11.  
  
**12.1.13 -****Central de Estágio**  
 Melhoria realizada no processo de gerenciamento de estágio, termo de compromisso que contém obrigatoriedade de defesa, só pode ser encerrado se conter pelo menos um participante cadastrado na banca e com a informação sobre a nota do aluno. Além de associar qualquer servidor como participante da banca de estágio, desde que esteja cadastrado com uma pessoa no sistema.  
  
**12.1.13 -****Inclusão de tags no complemento de histórico dos itens de evento contábil**  
 Melhoria realizada na parametrização do campo 'Complemento Histórico' dos eventos contábeis que passou a permitir a inclusão de Tags para serem utilizadas exclusivamente na geração de lançamentos com origem no TOTVS Educacional.

**12.1.13 -****Exibir disciplinas optativas/eletivas pendentes na análise curricular**  
 Disponibilizado o parâmetro exibir disciplinas optativas/eletivas pendentes na análise curricular. Com este parâmetro desmarcado, o sistema exibe somente as disciplinas optativas/eletivas que o aluno está cursando ou já concluiu.

**12.1.13 -****Concessão de Bolsa Futura**  
 Na inclusão de concessão da bolsa futura, quando o aluno possuir matrícula em mais de uma matriz curricular que esteja ativa ou quando a matriz curricular possuir mais de um turno associado, o usuário deverá selecionar a opção desejada para a inclusão da bolsa futura.

**12.1.13 -****Listagem de Bolsistas - SISCEBAS**   
Otimização realizada na geração do arquivo para o SISCEBAS. Na listagem estarão presentes alunos que tiverem Bolsas associadas em seu contrato, sendo apresentados os valores totais dos serviços, que passam a ser calculados através da 'Simulação de valores' e também os valores de débito contabilizados para as Bolsas.

**12.1.12 -****Otimização realizada no cálculo de Bolsas Condicionais**   
Criado o parâmetro 'Manter fórmula default para valor opcional de bolsas condicionais', disponível em Ambientes | Parâmetros | Educacional | Integração | Financeiro, para manter a fórmula utilizada no cálculo de bolsas condicionais associada ao valor opcional de bolsas condicionais na geração de lançamentos sendo que no momento da baixa a fórmula será processada para apresentar o valor da bolsa condicional. Com este parâmetro desmarcado, a geração de lançamentos calculará e atribuirá o valor das bolsas condicionais ao valor opcional parametrizado para bolsas condicionais do lançamento, desconsiderando a fórmula vinculada a esse campo. Ao cadastrar uma Bolsa no sistema com o campo "Bolsas incondicionais" DESMARCADO, é habilitado o campo "Ordem de perda" que indicará a ordem em que as bolsas perderão valor na baixa. A ordem de baixa das bolsas será o inverso da ordem de perda, ou seja, o menor número de Ordem de perda terá a menor prioridade de baixa.

**12.1.12 - Bolsa retroativa**   
Foi realizada otimização do processo de bolsa retroativa, de forma que o sistema mantenha a data de emissão dos lançamentos regerados por este processo.

**12.1.12 -****Verificar inadimplência na transferência interna e por coligadas**   
Esta implementação possibilita a instituição de ensino validar a inadimplência do aluno durante o processo de transferência interna, seja esta transferência dentro da mesma filial, entre filiais ou entre coligadas.

**12.1.12 -****Alterar Dados da Empresa**e **Alterar e incluir Funcionários**  
Permitir que as empresas possam através do portal, alterar seus dados cadastrais e de seus funcionários.

**12.1.12 -****Alterar Dados da Empresa**e **Alterar e incluir Funcionários**  
 Permitir que as empresas possam através do portal, alterar seus dados cadastrais e de seus funcionários.

**12.1.12 -****Permitir que os Funcionários das Empresas Parceiras Possam responder Avaliação Institucional no Portal**  
 Possibilitar que os funcionários da Empresas Parceiras possam responder avaliações Institucionais

**12.1.12 -****Empresa - Administração de Candidatos ás Vagas**  
 Possibilita que a empresa consiga consultar os candidatos que se inscreveram para as vagas que estão sendo ofertadas por ela.

**12.1.11 -****Empresa - Consultar Grades Curriculares**  
 Disponibilizar para as empresas as informações a respeito das matrizes curriculares da instituição de ensino.

**12.1.11 -****Consulta Pública - Projetos de Pesquisa, Extensão e Grupos de Estudo de Pesquisa**  
 Possibilita mecanismo para consulta pública das informações de projetos de pesquisa, projetos de extensão e aos grupos de pesquisa.

**12.1.11-****Páginas Públicas -  Cadastro de Empresa Parceira e Responsável**  
 Permitir que empresas interessadas em ser parceiras da IE, possam solicitar se cadastro através de uma página pública disponibilizada no Portal RM e que esse cadastro seja aprovado/reprovado através da plataforma Fluig.

**12.1.11-****Identificar faltas em aulas práticas, teóricas, estágio e laboratório**  
 Melhoria no plano de aula, agora é possível informar o tipo de aula, com o intuito de detalhar a frequência do aluno de acordo com seu tipo. Implementação disponível somente para o ensino superior.

**12.1.11- Otimização realizada na geração de lançamentos**   
Quando o sistema estiver parametrizado para buscar a conta caixa do responsável financeiro e a parcela possuir bolsa de crédito com outro sacado, o lançamento do outro sacado será gerado com a conta caixa cadastrada no cliente/fornecedor correspondente à bolsa de crédito e o lançamento do aluno será gerado com a conta caixa cadastrada no cliente/fornecedor do responsável financeiro.

**12.1.11- Data de contabilização da baixa na inclusão de bolsa retroativa.**   
Criado o parâmetro "Data de contabilização de baixa igual ao Padrão RM Fluxus, ao reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa", para permitir escolher qual data de contabilização de baixa será considerada quando o sistema estiver parametrizado para reconciliar extrato no processo de inclusão/exclusão de bolsa retroativa. Ao incluir uma bolsa retroativa e utilizar a reconciliação de extrato, caso este novo parâmetro esteja marcado, a data de contabilização da baixa obedecerá à parametrização definida no TOTVS Gestão Financeira (RM Fluxus | Parâmetros | Contas a Receber | Contab. Baixa Receber). Caso este novo parâmetro esteja desmarcado, o processo continua como antes, onde a data de contabilização da baixa será igual à data atual do sistema. Este parâmetro está disponível em Ambiente | Parâmetros | Educacional | Integração | Financeiro.

**12.1.10 -****Não permitir matricular em Lista de espera quando existir Correquisito**  
 Otimizado o processo para bloquear a matrícula de alunos em Lista de Espera caso a disciplina possua correquisito.

**12.1.10 -****Gerar contabilização para parcelas do tipo 'Parcela Extra' e 'Parcela Adicional'**  
 Melhoria realizada na geração da contabilização por competência para permitir contabilizar parcelas do tipo 'Parcela Extra' e do tipo 'Parcela Adicional' através da criação dos parâmetros "Contabiliza parcela do tipo Extra" e "Contabiliza parcela do tipo Adicional", disponíveis no menu Ambiente | Parâmetros | Educacional | Integração | Contabilidade.

**12.1.10 -****Permitir a Candidatura dos alunos egressos em vagas de emprego**  
 Permitir que os alunos egressos, possam fazer inscrição em vagas de empregos disponíveis para o seu Curso/Habilitação.

**12.1.10 -****Copiar Endereço da Empresa para o Funcionário**  
 No momento em que o usuário estiver cadastrando um funcionário para uma empresa na central de estágios, passou a ter a opção de atribuir ao endereço do funcionário que está sendo cadastrado o mesmo endereço da empresa à qual ele pertence. Essa regra vale tanto para a tela de cadastro de funcionário da empresa no Sistema quanto para a tela Web disponível no Fluig.

**12.1.9 -****Projeto de Inovação, Pesquisa & Extensão*****Novo!!!***  
 O Projeto de Inovação, Pesquisa e Extensão, tem como objetivo permitir aos clientes do TOTVS Educacional registrar, aprovar, acompanhar e manter dados referentes aos projetos submetidos para aprovação/verificação através de workflow na plataforma Fluig.

**12.1.9 -****Gestão de Visitas Técnicas e Grupo de estudos**  
 Afim de facilitar ao usuário gerenciar seus processos referentes a visitas técnicas, solicitação de participação em eventos e grupos/núcleos de estudos foi criado o processo de aprovação através do Worflow do Totvs fluig.

**12.1.9 -****Alteração do cadastro de aluno**  
 Para atender o conceito de multiparentalidade em que uma pessoa pode ter mais de um pai ou mãe no seu registro, foi alterado o cadastro de aluno com a inclusão de Pai e Mãe na aba de Responsáveis e o anexo de filiação.

**12.1.9 -****Análise curricular – apresentação do valor mínimo e concluído de cada Componente curricular**  
 Otimizada a visualização dos Componentes curriculares presentes na Análise curricular que passa a apresentar o valor mínimo exigido e valor concluído para cada Componente curricular.

**12.1.9 -****Estágio****| Cadastros da gestão de estágio na nova FW HTML**  
 Permitir que os cadastros básicos da rotina de estágio (cadastro de empresas, cadastro de funcionários da empresa, cadastro de vagas de estágio oferecidas pela empresa), possam ser utilizadas de dentro do Fluig, com as novas interfaces criadas com base no TOTVS HTML Framework.

**12.1.9 -****Exibir valores opcionais no Extrato Financeiro do Portal**  
 Otimizado a tela de Extrato Financeiro do Portal poderá ser desenhada dinamicamente respeitando as opções de visualizações de campos definidos nos parâmetros do sistema.

**12.1.9 -****Coordenador fazer Upload Materiais**  
 Com objetivo em aumentar a agilidade no processo de Upload de Materiais, o Coordenador poderá associar os materiais a um Curso, Série/Habilitação, Turma e Turmas/Disciplinas.

**12.1.9 -****Central de notificação II**  
 Melhoria na central de notificação, agora para cada mensagem de notificação é possível determinar o tipo de meio que será encaminhada, que pode ser através de e-mail e/ou uma notificação no fluig.

**12.1.9 -****Passagem de login externo no mobile**  
 Implementado a funcionalidade de passagem de login externo de aluno e professor no TOTVS Educa Mobile.

**12.1.9 -****Permitir Gerar Lançamentos para Período Letivo Encerrado**  
 Otimizado o processo, para que seja possível gerar lançamentos para Período Letivo Encerrado.

**12.1.9 -****Importador TOTVS Educaional**  
 Implementado na ferramenta Totvs Educacional - Importador, a opção de importar registros relacionados aos requisitos das disciplinas (Tabela = SREQUISITO).

**12.1.9 -****Informações da turma disciplina na Mudança de Turma**  
 Melhoria na etapa de "Seleção de disciplinas" do processo de mudança de turma/turno, o  para o contexto de Ensino Superior. Onde o sistema irá disponibilizar novos dados referente as disciplinas, turmas disciplinas, e subturmas visando agilizar o processo de escolha.

**12.1.8 -****Data dos lançamentos de estorno no Cancelamento de contrato**  
 Para permitir que a data dos estornos contábeis gerados pelo processo de Cancelamento de Contrato seja igual à data informada para o cancelamento do contrato, foi criado um novo parâmetro no sistema em Parâmetros | Integração | Contábil: "Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato". Com este novo parâmetro habilitado os estornos da contabilização receberão a mesma data informada no processo de "Cancelar contrato". Com o parâmetro desabilitado, o processo continuará como antes, ou seja, a data dos lançamentos de estorno continuará igual à data de execução do processo.

**12.1.8 -****Geração de movimento**  
 Criada a opção 'Data atual do sistema' na Geração de Movimentos por Boleto, assim, os movimentos gerados com esta opção marcada terão a data de geração igual à data atual do sistema.

**12.1.8 -****Cadastro de Filiação de Aluno**  
 Mudança no cadastro de filiação do aluno, para adequação do sistema ao conceito de multiparentalidade e parentalidade socioafetiva.

**12.1.8 -****Projeto de Inovação**  
 Permitir gerenciar os processos referentes a um Projeto de Inovação 'Atividades Tecnológicas - Registros de patentes' através do *workflow* do Fluig.

**12.1.8 -****Gestão de Alunos Egressos**  
 O sistema permite que alunos que já concluíram seu curso na instituição possam acessar o portal para alterar seus dados profissionais, responder a avaliação institucional ou consultar vagas de emprego.

**12.1.7 -****Recuperação de dados no dia "D" do Censo do ensino básico**   
 Implementado assistente que permite ao usuário obter uma "fotografia" dos dados pertinentes ao Censo escolar do ensino básico e arquiva-los, em distintas linhas do tempo para futuro envio ao Educacenso.

**12.1.7 -****Academia Social**  
 É um conceito do sistema que permite integrar o Totvs Educacional com o Fluig, para criar e alterar o status das comunidades, incluir e realizar a manutenção de participantes, além de um log com informações sobre o processo. Essas comunidades são geradas para as seguintes entidades: Curso, Habilitação, Turma,Turma/Disciplina, Turma Disciplina gerencial e gerenciada, Subturma e Atividade Ofertada.

**12.1.7 -****Central de notificação**Criado o cadastro de Mensagens de notificação que permitiu tirar de dentro dos parâmetros as templates dos envios de e-mails além de poder configurar o template no formato HTML.

**12.1.7 -****Disponibilizar informações de notas e faltas do aluno na Central do Aluno**  
 Na opção Matrícula da Central do aluno, é possível consultar as etapas de notas e faltas do aluno, bem como a visualização detalhada das notas em avaliações e detalhes das etapas de faltas.

**12.1.6 -****Melhoria na Central de Estágio**  
 Permite acesso ao portal educacional para o usuário da empresa, além de permissão as empresas para cadastro e divulgação de vagas.

**12.1.6 -****Parametrização por curso em lote**  
 Implementado processo que permite gerar de uma única vez (em lote) toda as parametrização por curso de um período letivo.

**12.1.6 -****Novo relatório do Book**  
 Disponibilizado novo relatório do book EDUREL007 - Diário de classe - Nota (preenchido) que gera  o diário de classe com a listagem dos alunos dos professores para cada disciplina e exibindo a nota das avaliações de uma etapa**.**

**12.1.6 -****Melhorias na geração de usuários**   
Melhoria no processo de geração de usuários para que seja possível: a. Personalizar a geração do código de usuário dos responsáveis, assim como já é feito atualmente para geração de usuários para alunos, professores e coordenadores; b. Escolher se será gerado usuário apenas para o aluno, apenas para os responsáveis ou para ambos; c. Possibilitar que o campo CPF, seja utilizado como opção de código do usuário; d. Possibilitar que o campo CPF seja utilizado como senha do usuário.

**12.1.6 - Exibição em árvore da Estrutura Curricular e da Estrutura de Oferta**  
 Para facilitar o acesso às funcionalidades referentes a Estrutura Curricular  e Estrutura de Oferta, foi implementado a visão em árvore com as opções de inclusão, exclusão, alteração e execução de processos das rotinas relacionadas. É possível a utilização de filtros de pesquisa e ordenação para tornar a visão mais otimizada.

**12.1.6 -****Melhoria na cópia do responsável do aluno como responsável financeiro**  
 Permitir o usuário aproveitar os clientes/fornecedores já existentes, ao definir o pai, a mãe, responsável acadêmico ou até mesmo o próprio aluno como responsável financeiro. Evitando a criação desnecessária de um novo cliente/fornecedor.

**12.1.6 -****Alterar matriz aplicada na cópia de turma entre períodos letivos**   
Melhoria no processo de cópia de turmas entre período letivo para que seja possível alterar a matriz aplicada e disciplinas na cópia da turma.

**12.1.6 -****Importação de Gabaritos e Associação de disciplinas**Implementado dois novos processos relacionados ao gabarito, visando facilitar o cadastro das respostas e a associação delas com a disciplina**.**

**12.1.6 -****Alterar data de matrícula no Período Letivo**  
 Evoluído o processo de cópia de turma entre períodos letivos para alterar a Matriz Aplicada, e as Disciplinas que serão replicadas para o novo período letivo.

**12.1.5 -****Mala direta**  
 Permitir o usuário gerar arquivos de mala direta para registros de uma determinada consulta SQL, com base em um template pré-definido, existindo também a possibilidade do conteúdo do arquivo ser enviado no corpo do  e-mail.

**12.1.5 - Botão: Remover Modelos de Etapas no processo: Atualizar Etapas de Turma/Disciplinas**  
 Este parâmetro tem como objetivo, oferecer mais praticidade ao usuário para excluir os modelos de etapas desnecessárias para atualização nas turmas/Disciplinas. Esse assistente pode ser executado nos processos das visões: Períodos Letivos e Parametrização por Curso.

**12.1.5 -****Alteração no processo de Cópia de Matriz Curricular**  
 Para tornar o processo de cópia de matriz curricular mais flexível, foi implementado a opção de incluir ou excluir as disciplinas, além de definir o status da nova matriz curricular, antes de realizar o processo de cópia.

**12.1.5 -****Visualizar os dados das Avaliações no Portal**  
 Permitir o professor/coordenador tenha acesso as demais informações pertinentes à avaliação no ato de sua escolha na digitação de notas.

**12.1.5 -****Parametrização de casas decimais para carga horária, créditos acadêmicos e créditos financeiros**  
 Criado parâmetro que permite ao usuário configurar o sistema para exibir as informações de carga horária, créditos acadêmicos e créditos financeiros com o número de casas decimais que lhe for mais conveniente.

**12.1.5 -****Troca de turno na matrícula do período letivo**  
 Implementado no processo  de Mudar turma a opção de trocar o turno da matrícula no período letivo dos alunos que ainda não foram enturmados, e permitir ao usuário aproveitar o contrato para os alunos do Ensino Básico.

**12.1.4 - Créditos Financeiros no processo da matrícula online**  
 Para dar mais flexibilidade ao usuário do RM Portal, um novo parâmetro foi criado. Ele permite a exibição de "Créditos Financeiros" durante o processo de matrícula.

**12.1.4 -****Lançamento de ocorrências do aluno, filtros livres**  
 A funcionalidade assistente de ocorrências de alunos está com uma maior flexibilidade, agora a informação sobre a matriz aplicada não possui obrigatoriedade com premissa para o próximo passo no avanço do assistente.

**12.1.4 - Exibição de turma e período do aluno no Portal Corpore.Net**  
 Foram criados dois novos parâmetros no TOTVS Educacional para controlar a exibição das informações de período base do aluno e turma do aluno. Esses dois novos parâmetros funcionarão tanto para o Ensino Básico quanto para o Ensino Superior, ficando a cargo do usuário administrador definir quais informações terão relevância no Contexto Educacional, exibido no RM Portal e no Educa Mobile.

**12.1.4 - Integração nos itens de****Contrato do Nucleus**  
 O objetivo dessa integração é permitir o cliente cadastrar no Educacional somente contratos do tipo serviço, para os alunos que possuírem integração nos itens de contrato do Nucleus. Para atender as necessidades dos clientes, foi implementado no cadastro de contratos do aluno, a permissão de cadastrar contratos do tipo Serviço , para os alunos que possuírem integração nos itens de contrato do Nucleus, e os  contratos do tipo Plano, ainda continuam sendo barrados.

**12.1.4 -****Turmas/Disciplinas**  
 Um novo campo foi criado no cadastro de Etapas "Permite digitação diretamente na etapa". Caso o usuário queira bloquear os campos de Nota e/ou Falta para digitação, deverá desmarcar o parámetro. O  campo estará disponível tanto para a etapa de notas quanto para a etapa de faltas

**12.1.4 -****Download MateriaisTotvs Educa Mobile**  
 Permitir que os Alunos, Responsáveis pelos alunos e Professores, visualizem e baixem os arquivos no Totvs Educa Mobile.

**12.1.4 - Inclusão de Novas Tags no Comprovante de Matrícula e Contrato Financeiro**  
 Para complementar os textos exibidos no demonstrativo de matrícula e contrato financeiro, durante a realização da matrícula online pelo aluno através do RM portal. Foi adicionado duas tags (Turma e Período) ao comprovante.

**12.1.3 -****Visualização de Ocorrências no Totvs Educa Mobile**  
 Implementado a funcionalidade para que seja possível os alunos ou responsáveis, visualize as ocorrências no Totvs Educa   
 Mobile.

**12.1.3 -****Melhoria na Matrícula Online**  
 Foram feitas melhorias para proporcionar aos usuários da rotina de matrícula on-line do Portal Corpore.Net uma experiência mais agradável no que diz respeito à usabilidade, bem como maior facilidade de acesso às diveras informações de cada fase do processo. Esta implementação consiste basicamente na alteração dos layouts das telas do processo de matrícula on-line do Portal Corpore.Net.

**12.1.3 -****Informar campus na matrícula do processo seletivo RM e processo seletivo terceirizado**  
 Incluído o campo Campus na matrícula do processo seletivo RM e processo seletivo terceirizado, para que durante a matrícula de candidatos oriundos do TOTVS processo seletivo RM ou Processo seletivo terceirizado, consiga informar qual o campus da habilitação do aluno.

**12.1.3 -****Forma de inscrição x Tipo de ingresso**  
 Criado o processo de relacionamento "de-para" da Forma de Inscrição do Processo Seletivo e a forma de Ingresso do ClassisNet.

**12.1.3 -****Parametrizar tipos de arquivos na entrega de trabalho**  
 Este funcionalidade determina quais extensões são permitidas para a entrega de avaliações(trabalhos) pelo aluno no portal além de delimitar o tamanho do arquivo.

**12.1.3 -****Bloquear bolsas de crédito no portal**  
 Agora é possível parametrizar o sistema para que o aluno não visualize o boleto correspondente a bolsa de crédito.

**12.1.3**-******Aproveitar documentos entregues no processo Seletivo no Processo de Matrícula RM**  
 Implementado a funcionalidade de aproveitar os documentos entregues no Processo Seletivo, no Processo de Matrícula RM.

**12.1.1 -****Geração de movimentos para emissão de NFe**  
  Na geração de movimentos, o sistema passou a permitir a 'Alteração' somente para última competência gerada e cujo período de apuração de tributos esteja em aberto.   
 Os valores calculados para o movimento em questão são feitos da seguinte forma: total dos valores do contrato menos valores já gerados para os movimentos anteriores, dividido pelo número de competências ainda não geradas.

**12.1.1 -****Matricular alunos em disciplinas incluídas na Matriz Curricular**  
 Este processo permite ao usuário efetuar a matrícula de um ou vários alunos em uma disciplina incluída posteriormente na Matriz Curricular para os alunos do contexto Ensino Básico.

**12.1.1 -****EntryPoints Matrícula - Fórmulas Visuais:**  
 Criado um recurso dentro da parametrização da Matrícula um novo recurso para associação da fórmula visual nos principais processos do sistema.

**12.1.1 -****Exibir o Tipo da Turma/Disciplina no SDD:**  
 No processo de Matrícula no Portal e no RM.Exe, o sistema irá diferenciar o tipo da Turma/disciplinas, se a mesma é: Presencial, Virtual ou Semi-Presencial.

**12.1.1 -****Quadro de Horários Dinâmico na Matrícula Presencial**  
 Conforme o usuário seleciona as turmas/disciplinas, o quadro de horários deve ser atualizado com os horários e marcado em vermelho caso existam choques de horário.

**12.1.1 -****Desabilitar Disciplinas sem vagas no SDD**  
 O Usuário da IE / Aluno não poderá selecionar a Turma/disciplina caso as vagas estejam esgotadas. A Turma/Disciplina ficará disponível apenas para visualização.

**12.1.1 -****Permissão de Acesso ao Botão: Adicionar Disciplinas:**  
 Criado o perfil de acesso ao Botão: Adicionar Disciplinas no processo de Matrícula em turmas/disciplinas no RM.Exe.

**12.1.1 -****Calendário Acadêmico**  
 Na tela de cadastro de calendário, foi incluído um anexo que é apresentado apenas quando o usuário está dentro do TOTVS Educacional, que possibilita o cadastro de eventos acadêmicos. Nas telas de geração de plano de aula e reserva de recursos e instalação o usuário pode selecionar quais os tipos de eventos acadêmicos deverão ser considerados no momento da geração, assim como ocorre com os feriados atualmente.

**12.1.1 -****Nome Social**  
 Conforme Portaria n. 1612/2011 do Ministério da Educação entende-se por nome social aquele pelo qual as pessoas se identificam e são identificadas pela sociedade.

**12.1.1 -****TOTVS Educa Mobile**  
Disponibilizado o TOTVS Educa Mobile; mais que uma aplicação móvel, uma solução inovadora que permite os professores, alunos e responsáveis por alunos, acessarem funcionalidades acadêmicas do dia a dia, através de dispositivos móveis.

**12.1.1 -****Relatórios SISTEC**  
O SISTEC é o Sistema Nacional de Informações da Educação Profissional e Tecnológica, que disponibiliza mensalmente informações sobre os cursos técnicos de nível médio, suas respectivas escolas e alunos matriculados.

**12.1.1 -****Gestão de TCC**  
Permite a Instituição de Ensino gerenciar todo o processo de Trabalho de conclusão de curso. Desde o seu cadastro inicial, passando pelas interações entre professores/orientadores e os alunos até a sua conclusão com ou sem a banca de avaliadores.

**12.1.1 -****Copiar turma entre períodos letivos**Implementação trata-se da alteração do processo  "Copiar turmas entre períodos letivos", localizado no menu Currículo e Oferta | Turma | Processo "Copiar turmas entre períodos letivos", para que o mesmo possa permitir a cópia de turmas e turmas/disciplinas em lote*.*

**12.1.1 -****Campos complementares Recurso/Instalação**Permite a Instituição incluir campos complementares à tela de cadastro de: Prédio, bloco, sala e recurso.

**12.1.1 -****Fórmula Visual para concessão de bolsa**  
Com as atividades da bolsa do aluno e de concessão de bolsa futura, o cliente irá conseguir personalizar o sistema com regras de negocio de acordo com sua necessidade, ele poderá criar uma fórmula visual para incluir, excluir, alterar, cancelar uma bolsa do aluno e/ou incluir, excluir, alterar uma bolsa futura.

**12.1.1 -** **Criar turma e Turma/disciplina em lote**Esta implementação trata-se da alteração do assistente "Cadastro de Turma e Turma/Disciplina", localizado no menu Atividades Acadêmicas ->Assistentes, para que o mesmo possa permitir a criação de turmas e turmas/disciplinas em lote. Também foi  implementado a geração de horários  e a associação dos professores nestas novas turmas/disciplinas.

**12.1.1 -****Exportar dados do Curso, Turma e Turma/Disciplina para arquivo XML**  
O sistema permite exportar as informações de curso, turma e turma/disciplina no formato XML.

**12.1.1 -****Associação de Matrículas no Período Letivo a Itens de Contrato**O TOTVS Educacional, agora, permite o vínculo de matrículas realizadas em um período letivo com um item de contrato do TOTVS Gestão de Estoque, Compras e Faturamento. Dessa forma, todo o financeiro é gerenciado pelo TOTVS Gestão de Estoque, Compras e Faturamento associado às regras de um contrato no módulo de Contratos. Esse tipo de vínculo permite o gerenciamento financeiro, através de um contrato, de turmas fechadas ou de um grupo de matrículas.

**12.1.1 -****Negociação Online**  
Implementado no portal do Educacional a Negociação Online, cujo objetivo é permitir que o usuário realize simulações de negociações e que possa visualizar as novas parcelas, seus valores e respectivos vencimentos.   
Serão exibidos, para seleção, os Lançamentos cujo Cliente/Fornecedor esteja vinculado ao usuário no Educacional, podendo ser o próprio aluno ou o responsável financeiro. A simulação poderá ser impressa e, avançando as etapas do  processo, o acordo será gerado a partir dos dados informados.

**12.1.1 -** **Central de Estágio**  
A central de estágio possibilita explorar meios que proporcionam ao aluno formação profissional de qualidade, no âmbito dos estágios curriculares e na relação com o mercado de trabalho. Esta relação se desenvolve no contato direto com as empresas privadas, públicas, organizações sem fins lucrativos e órgão de classes.  
 Em âmbito institucional assume a função acadêmico-administrativa de orientar e articular as ações propostas pelas Coordenações de Curso e/ou de Estágios, tendo em vista assegurar a qualidade do estágio dos estudantes, respeitando as particularidades de cada curso**.**

**12.1.1 -** **Justificativa de Falta**A funcionalidade permite ao professor cadastrar uma justificativa ao lançar falta para um aluno.

**12.1.1 -****Campos complementares Recurso/Instalação**Criação de novos campos complementares que podem ser configurados por nível de ensino.

**12.1.1 -****Máscara da Turma**  
Implementada a possibilidade do usuário alterar a máscara da turma para incluir o código do período da disciplina (coringa "p").

**12.1.1 -** **Período Contábil por Contrato**  
Visando flexibilizar a contabilização por competência nas instituições de ensino superior que possuem um período de contratação menor que a competência (cursos de curta duração) ou maior que a competência (cenários de pós graduação), foi criado a possibilidade de definição deste período contábil por contrato.

**12.1.1 -** **Agenda do Aluno - Portal**O aluno terá acesso no portal a um quando de horários onde estarão discriminadas todas as atividades, período de matricula, datas para entregas de trabalho. Todas as datas que interferem diretamente no dia a dia do aluno na instituição.

**12.1.1 -****Lição de Casa**Dentre as atividades desempenhadas por um professor no RM Portal Educacional está a de planejamento e execução de um plano de aula. No plano de aula é possível informar a data da aula, o horário, o conteúdo previsto e o conteúdo realizado para uma aula realizada. Surgiu a necessidade de informação também da lição de casa, para que o professor possa controlar as tarefas passada aos seus alunos no seu plano de aula.
