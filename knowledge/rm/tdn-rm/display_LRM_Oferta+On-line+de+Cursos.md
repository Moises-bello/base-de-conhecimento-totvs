---
content_hash: 5a3f09afc639e05711d6f3de5bb07c769e4170fee1802ffa3870a0da3e794a01
fetched_at: '2026-06-29T00:10:14.595759+00:00'
page_id: '461909640'
product: rm
source: tdn-rm
title: Oferta On-line de Cursos
type: documentation
url: https://tdn.totvs.com/display/LRM/Oferta+On-line+de+Cursos
version: 56
---

Atenção

Esta funcionalidade está disponível a partir da versão 12.1.24

A partir dessa versão será possível matricular um candidato no curso da área ofertada, durante o processo de inscrição realizado no novo portal do Processo Seletivo e ao finalizar a matrícula selecionar a forma de pagamento a ser exibida. Para isso o sistema validará se a área ofertada faz o uso da oferta online e se não existe nenhuma restrição de envio de documentos obrigatórios.

**Parametrização:**

Para habilitar a oferta online e configurar as opções de pagamento o usuário do sistema deverá acessar o Processo Seletivo e marcar o campo “Oferta Online”.

 **TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Oferta Online de Cursos**

Em seguida, deverá ser configurada a aba "Oferta Online de Cursos", onde será indicado se haverá validação obrigatória de documentos no momento da matrícula. Caso este parâmetro seja ativado e a área do curso exija algum documento específico, a matrícula não será efetivada imediatamente, ficando limitada apenas à inscrição do candidato no processo seletivo. A validação dos documentos ocorrerá posteriormente, e, somente após essa verificação, a matrícula será formalizada no sistema.

Se a área ofertada não exigir nenhum documento obrigatório ou o parâmetro estiver desmarcado ao ser realizada a inscrição do candidato ele também será matriculado no curso. Isso não ocorrerá apenas se o candidato for alocado na lista de espera do processo seletivo.

Para maiores informações sobre como configurar os documentos que serão exibidos para o candidato enviar acesse: <https://tdn.totvs.com/x/EREMKg>

Para maiores informações de como configurar o envio de arquivo acesse: <http://tdn.totvs.com/pages/releaseview.action?pageId=450152315>

**Parâmetros da Área de Interesse Ofertada**

Na tela de edição da área ofertada estará disponível uma aba com nome “Oferta Online de Cursos”. Nesta deverão ser configuradas as informações que possibilitarão a realização da matrícula.

 **TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Oferta Online de Cursos| Anexo| Área de Interesse ofertada**

Ao utilizar a opção de geração de contrato o candidato ou seu responsável financeiro serão utilizados para geração do cliente/fornecedor, porém, antes é feito uma busca para validar a existência de um cliente/fornecedor com os mesmos dados, sendo assim o sistema irá filtrar somente cliente/fornecedores que estejam ativos no TOTVS Gestão Financeira. 

Atenção

Para mais informações das parametrizações a serem realizadas no sistema, consulte a documentação: [http://tdn.totvs.com/x/JcVGGg](https://tdn.totvs.com/x/-MGrKw)

Matrícula

Caso seja informada uma turma nas definições do venda online é possível parâmetrizar o sistema para que o seja ignorados disciplinas concluídas ou em curso, ou seja, caso o candidato já tenha sido aluno e está sendo matriculado em uma turma que possui disciplinas que já foram concluídas ou estão em curso no passado, o sistema poderá ignorar estas disciplinas e prosseguir com a matrícula sem impedimento.   
Para mais informações acesse: 

Obs: esta modificação estará disponível à partir da versão 12.1.2406 prevista para Junho de 2024.

Após realizado as devidas parametrizações no sistema, o processo seletivo parametrizado estará pronto para utilização no portal.

Quando o candidato acessar a tela de inscrição de um processo seletivo do tipo "oferta online", e a validação obrigatória de documentos no momento da matrícula estiver **desativada**, após preencher todos os dados e clicar em "Finalizar Inscrição", a matrícula será automaticamente realizada no TOTVS Educacional.

Na Central do Candidato, a informação de matrícula será exibida em verde, indicando que o aluno foi matriculado. O status também mostrará a situação específica da matrícula, de acordo com os parâmetros configurados.

Quando o candidato acessar a tela de inscrição de um processo seletivo do tipo "oferta online", e a validação obrigatória de documentos no momento da matrícula estiver **marcada**, após preencher todos os dados e clicar em "Finalizar Inscrição", a matrícula **não** será automaticamente realizada no TOTVS Educacional, ficará aguardando a validação de documentos para confirmação da Matricula.

Na Central do Candidato, a informação de matrícula não será exibida.

**Passando o identificador da Área de Interesse via url**

A partir dessa versão o usuário poderá informar o identificador da área de interesse no link a ser disponibilizado para o candidato, assim, caso exista mais de um Processo Seletivo e mais de uma Área de interesse ofertada o candidato será direcionado diretamente para a área de interesse que estiver indicada na url. Para isso na url deverá ser informada a chave “ai=222”, onde 222 corresponde ao id da área de interesse ofertada.

Exemplo:

Id. do Processo Seletivo: 10

Id. da Área de Interesse Ofertada: 4

http://www.totvs.com.br/web\_src/app/Edu/PortalProcessoSeletivo/?c=1&f=1&ps=10&ai=4#/es/inscricoeswizard/dados-basicos

**Matrícula com seleção de Plano de Pagamento**

Caso a oferta online utilize a geração de contrato e possibilite a alteração da forma de pagamento o usuário visualizará uma opção para selecionar o Plano de Pagamento e para visualizar os detalhes do plano selecionado.

É importante ressaltar que nos casos de cursos que os seus valores são calculados baseado no número / valor de crédito, e que a parcela do plano de pagamento esteja parametrizada para que o valor seja calculado automaticamente, o campo “Código da Turma” disponibilizado na aba “Acadêmico” deverá ser devidamente preenchido para que seja possível disponibilizar a simulação dos valores do Plano de Pagamento

Na tela de confirmação dos dados da inscrição será exibida a forma de pagamento selecionada.

Plano de pagamento e bolsa associado ao prospect

Para informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

É possível parametrizar o TOTVS Educacional para que ao criar as parcelas no contrato do aluno a partir do plano de pagamento, sejam consideradas do plano de pagamento somente as parcelas com vencimento a partir do mês da inclusão do plano de pagamento no contrato.

Para saber mais [clique aqui](https://tdn.totvs.com/display/LRM/Tesouraria) (recurso disponível a partir da versão 12.1.33).

Importante

Caso a parametrização citada anteriormente esteja habilitada, é importante que as parcelas que terão lançamentos gerados estejam de acordo com o plano de pagamento.

Em alguns casos podem estar parametrizado como **"Parcela inicial" = 1** e **"Parcela final" = 1**, e se a parcela de número 1 estiver vencida, a mesma será desprezada, e com isso não haverá parcelas com lançamentos gerados ocasionando a apresentação da mensagem abaixo ao realizar a matricula.

**Sobre a Flexibilização do Plano de Pagamento [Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=728646916) (disponível a partir da versão 12.1.2302).**

 **Ao finalizar a inscrição podem ocorrer as seguintes situações:**

**1 –** **A quantidade de vagas da área de interesse tiver sido atingida.**

Neste caso o aluno poderá ser incluído em uma lista de espera, o que implicará que sua matrícula no TOTVS Educacional não será realizada, devendo esta ser realizada posteriormente caso surja uma nova vaga.

Se o aluno for incluído na lista de espera ele será alertado sobre essa situação e poderá acompanhar se uma nova vaga surgiu através da central do candidato.

Situação da inscrição/matrícula apresentada na Central do Candidato:

**2 –** **A oferta online foi configurada para que seja gerado lançamento financeiro.**

Ao ser configurada uma oferta com geração do lançamento financeiro a matrícula do candidato será realizada no Totvs Educacional, porém ficará pendente de confirmação por pagamento.

Essa situação será informada ao usuário que deverá realizar o pagamento via Boleto ou Cartão (conforme parametrização).

Ao clicar nos botões de pagamento via boleto ou via cartão serão abertas as telas para impressão do boleto ou realização do pagamento.

O candidato poderá acompanhar o status da efetivação da matrícula através da central do aluno.

Avisos

* A opção de pagamento com cartão, utilizando a adquirente GetNet somente está disponível a partir da versão 12.1.25
* A parcela com a menor data de vencimento será exibida na central do candidato para o pagamento.

Na central do candidato, na situação atual da matrícula, será apresentado o texto de identificação cadastrado na situação de matrícula do Totvs Educacional.

O pagamento ficará com a informação que aguarda pagamento até o que lançamento financeiro relacionado esteja baixado no sistema financeiro.

**3 –** **Oferta Online com envio de documentos obrigatórios e parametrização de validação dos documentos**

Caso o processo seletivo esteja com o parâmetro “Validar documentos obrigatórios na matrícula da oferta online de cursos” e a área ofertada solicitar algum documento que esteja marcado como “Obrigatório”, a matrícula no educacional não será efetuada, sendo gerada apenas a inscrição do processo seletivo.

Na Central do Candidato, a informação de matrícula **não** será exibida.

O usuário responsável pelo processo seletivo deverá acessar o cadastro do candidato, validar os documentos enviados e marcar a opção de documento entregue caso esteja de acordo com o esperado.

Após a Validação do documento deverá ir para a tela de identificação do Candidato e selecionar a opção Matricular.

Na Central do Candidato, a informação de matrícula **não** será exibida.

**4 –** **Existência de vagas na área ofertada e ocorrência de erro no processamento da matrícula**

Pode ocorrer de que a configuração da área de interesse esteja correta, porém por algum motivo a matrícula não veja a ser realizada  no  TOTVS Educacional,  ocorrendo  erro  no processamento.

Caso  isso  ocorra  nem o  cadastro  do  candidato  do processo seletivo e no Totvs Educacional não serão efetuados e a mensagem de erro com a causa do erro será exibida ao usuário.

**Atualização de dados dos alunos a partir da ficha de inscrição do processo seletivo**

Agora é possível parametrizar a venda online de cursos, se o candidato, poderá atualizar automaticamente os dados do aluno ou responsável financeiro diretamente da ficha de inscrição do portal do processo seletivo, caso o aluno já esteja cadastrado na base de dados.

Para realizar a parametrização basta acessar o caminho abaixo:

 **TOTVS Processo Seletivo| Cadastros| Processo Seletivo/ Oferta Online de Cursos| Anexo| Área de Interesse ofertada**

* Sobrescrever informações do aluno:
  + **Endereço:** Será atualizado somente os dados da aba de endereço do aluno
  + **Dados pessoais:** Será atualizado todos os outros dados do aluno, que estejam parametrizados para exibição no portal do processo seletivo
* **Sobrescrever dados do Responsável Financeiro do aluno:** Será atualizado todos os dados possíveis de atualização do  responsável financeiro.

Caso os parâmetros acima estejam marcados, quando um candidato que já possui cadastro de aluno na base, entra para realizar a compra de um novo curso, o mesmo informará seus dados e dados de responsável financeiro, caso seja parametrizado para isso, e ao final da inscrição, os dados serão atualizados automaticamente na base.

**Observação: Apenas os dados referentes ao aluno serão sujeitos a sobrescrita em caso de aproveitamento de pessoa, os dados dos responsáveis não serão alterados.**

Esta funcionalidade está disponível a partir dos Patches: "**12.1.27.259**" e "**12.1.28.171**".

**OBS.**: *É necessária a execução do "**RM.Atualizador**" para que sejam atualizados os script na base de dados, para a liberação do acesso ao campo "**Endereço**", na aba "Venda online de cursos", no cadastro de Área ofertada do processo seletivo.*

Importante

A partir da versão **12.1.31.138** é importante informar que quando o candidato inscrito for um funcionário e possuir um cadastro como pessoa e uma chapa, o sistema não irá sobrescrever as informações do aluno com as do candidato.

Tanto o aluno quanto o funcionário são associados a mesma pessoa e compartilham as mesmas informações. Todas as alterações realizadas no cadastro de uma pessoa se refletem no funcionário e devem ser enviadas para o eSocial.

Dessa forma, o Processo Seletivo não realiza a atualização dos dados do aluno existente quando o mesmo é um funcionário. Essas informações devem ser alteradas diretamente no módulo do RH.

Campos passíveis de alteração por parâmetro:

**Sobrescrever endereço do aluno:** São os campos que tem mais probabilidade de serem alterados com maior frequência, e-mail e todos os campos dentro da aba "Endereço" .

**Sobrescrever dados pessoais do aluno:** São os campos que tem menos probabilidade de serem alterados com maior frequência, serão todos os campos da aba "Identificação" e "Documentos".

**Sobrescrever dados do Responsável Financeiro do aluno:**Somente os campos de endereço, e-mail e telefones, das abas "Principal", "Pagamento" e "Entrega"

Utilizando responsável financeiro ou acadêmico menor de idade

A partir da versão 12.1.2302 será possível matrícula os alunos com responsável financeiro ou acadêmico que seja menor de idade, para isso, será necessário marcar o parâmetro "Associar responsável financeiro/acadêmico menor de 18 anos ao aluno" disponível na área de interesse ofertada| Venda Online de cursos| Perfil do usuário.

Você sabia que é possível restringir ou alertar, sobre possíveis débitos financeiros vinculados ao CPF do responsavel financeiro.

Para maiores informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=727373766).
