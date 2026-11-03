---
content_hash: 89ffa9d0c8712809bd18d3720612ce3782d147b609088b155dfb58cc48ff8676
fetched_at: '2026-06-29T00:09:32.421991+00:00'
page_id: '425458845'
product: rm
source: tdn-rm
title: Dados básicos do Candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458845
version: 4
---

**1- Identificação**  
Essa guia agrupa as informações fundamentais de uma inscrição e por meio dela é que será estabelecido o vínculo de uma pessoa com um processo seletivo. Seguem informações adicionais sobre os campos que não são auto-descritivos.

Número da inscrição: esse campo não poderá ser editado já que o próprio sistema controla a geração dos números das inscrições. O botão visualizado ao lado desse campo permite que seja selecionada uma inscrição anônima previamente gerada. Com isso, será possível recuperar uma inscrição anônima para que o restante do seu preenchimento seja feito manualmente e não por meio da utilização do processo "Importar Inscrições Anônimas".

Pessoa: esse campo representa a identificação do candidato que está realizando a inscrição. Caso o candidato já exista cadastrado na base de dados basta pesquisá-lo e selecioná-lo. Caso não exista o mesmo poderá ser cadastrado no momento da inscrição.

Forma de inscrição: estarão disponíveis para seleção todas as formas de inscrição possíveis, de acordo com o calendário, para uma inscrição no processo seletivo selecionado.

Local de realização da prova: permite que seja selecionada a cidade escolhida pelo candidato para realização das provas. As cidades disponíveis para escolha serão todas aquelas que possuem locais incluídos no processo seletivo em que esteja se inscrevendo.

Status da inscrição: permite que se visualize e altere a situação atual da inscrição. Os status possíveis são: Inscrito (pendente de confirmação de pagamento), Candidato (inscrição confirmada) e Inscrição cancelada.

 2ª via de comprovante: permite imprimir o comprovante de inscrição através de relatório criado no gerador de relatórios.

Enviar login ao candidato: envia um e-mail para o candidato informando sua senha de acesso ao Portal de Inscrições. O formato de e-mail deverá ser configurado na tela de parâmetros do sistema.

Questionário: permite responder o questionário sócio-econômico na inscrição do candidato. O questionário a ser respondido deverá ser definido no cadastro de processo seletivo. Todas as questões são de preenchimento obrigatório e caso o usuário tente salvar com questões em branco será emitida uma mensagem. Uma vez respondida, a prova não poderá ser editada nem visualizada pelo Processo Seletivo  
   
Caso o processo seletivo seja controlado por vagas e aceitar inscrições excedentes, esta informação com dados de excedente estará visível na identificação da inscrição do candidato. Haverá um painel informando a situação do candidato e sua posição de excedente.

**2- Informações Complementares**  
Nesta guia deverão ser configurados detalhes secundários relacionados à inscrição. Nela também poderão ser visualizadas informações sobre o lançamento financeiro gerado na integração com o módulo "RM Fluxus".

Canhoto: se for marcado, indica que o candidato é canhoto e seja pelo sistema ou manualmente, sua alocação será em sala com lugares para canhoto.

Treineiro: se for marcado em sua inscrição e o processo seletivo permitir treineiro, indica que o candidato irá participar apenas para efeito de experiência não podendo concorrer efetivamente a nenhuma das vagas. O sistema desconsidera a inscrição de "treineiros" no momento da classificação.

Dados do ENEM: quando marcado, indica o desejo do candidato de aproveitar o resultado obtido por ele no ENEM, Exame Nacional do Ensino Médio. Dessa forma, a rotina de classificação irá considerar o aproveitamento do candidato no referido exame. As informações relativas à avaliação e aproveitamento do candidato poderão ser visualizadas e preenchidas por meio dos campos "Número de inscrição", "Ano de referência", "Nota objetiva" e "Nota redação". O preenchimento e alteração desses campos, também poderão ser dados pela execução dos processos "Importar Notas do ENEM" e "Importar Notas Inconsistentes do ENEM".

Lançamento e Status do lançamento: visualização do código do lançamento e seu status no módulo "RM Fluxus".

Observação

À partir da versão 12.1.25 (patch 12.1.25.100), será possível clicar no lançamento e abrir a tela com os detalhes do lançamento no TOTVS Gestão Financeira, sendo que a tela só será aberta  para visualização e edição se o usuário possuir permissão nas funções de lançamentos do TOTVS Gestão Financeira.

Responsáveis pelo candidato: Para candidatos que necessitam de responsável Acadêmico, Financeiro, Dados do Pai e da Mãe, estes campos deverão ser preenchidos. Lembrando que para todo lançamento a ser gerado, pelo menos o campo de responsável financeiro deverá ser preenchido. Estes dados poderão ser utilizados no cadastro de Aluno do Classis Net. Através do processo de matrícula Processo seletivo, ao matricular os candidatos do processo seletivo como alunos e gerar contrato com lançamentos.

Opção pelo sistema de cotas: Se o processo seletivo no qual o candidato está se inscrevendo utilizar o sistema de cotas de acordo com a lei federal, será exibido um novo grupo de opções ao candidato. O candidato deverá responder Sim/Não para questões que forem apresentadas para se incluir no sistema de cotas, se definir como sendo de baixa renda e se autoclarar como preto, parto ou indígena. Os textos destas perguntas são definidos no executável através do anexo do processo seletivo chamado "Cotas de instituições federais".

**3- Necessidades Especiais**  
Nessa guia serão incluídas as informações sobre as deficiências alegadas e comprovadas pelo candidato. Quando houver alguma deficiência informada, ela será considerada pelo processo "Alocar Candidatos em Locais de Prova". Os candidatos portadores de deficiência serão alocados em salas com suporte a estas necessidades informadas.

* Importante: Se for informada a opção "Outra" para necessidades especiais, o candidato nunca será alocado pelo processo citado acima, Sendo sempre necessária a sua alocação manual por meio do serviço "Local da Prova do Candidato".

**4- Indicações**  
Se a forma de inscrição escolhida permitir indicações, será possível informar uma pessoa ligada à instituição que tenha indicado o processo seletivo para o candidato. Essa informação poderá ser utilizada para restringir a concessão de determinados descontos a candidatos ou para contabilizar indicações caso se queira premiar indivíduos (alunos, professores, funcionários, etc.) com maiores números de indicações para o processo seletivo.

**5- Áreas de Interesse**  
Nessa guia serão inseridas ou editadas as opções dos candidatos para uma ou mais áreas de interesse disponíveis no processo seletivo. Para as próximas fases, após classificar os candidatos, será possível visualizar nesta guia: Status na opção (inscrição cancelada, em chamada, compareceu a chamada, desclassificado, etc.) Classificação (posição da classificação) Pontuação do candidato (valor de pontuação na prova). Número da Chamada (Identificação da Chamada em que o candidato foi chamado) Ultima etapa realizada (Etapa na qual passou pela última classificação)  
No Portal, essas informações estarão visíveis na área privada do candidato no serviço Inscrições/Resultados.  As outras abas estão descritas no processo de escolha de área ofertada.
