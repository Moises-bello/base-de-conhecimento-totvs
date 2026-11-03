---
content_hash: ba977ecb312636d58ed3bc6832a9a1eb38108668bf3377e6b6bbdfd40f5af7d8
fetched_at: '2026-06-29T00:10:03.895464+00:00'
page_id: '452719170'
product: rm
source: tdn-rm
title: Geração do arquivo RAIS - Relação Anual de Informações Sociais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719170
version: 5
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Através desse módulo será gerada a Relação Anual de Informações Sociais - RAIS, criado pelo Governo Federal, através do Decreto nº 76.900, de 23.12.75  em que deverão constar informações relativas a empregados com quem a empresa tenha mantido relação de emprego durante qualquer período do ano-base.

Este importante instrumento de coleta de dados denominado de Relação Anual de Informações Sociais - RAIS tem por objetivo:   
·         O suprimento às necessidades de controle da atividade trabalhista no País;  
·         O provimento de dados para a elaboração de estatísticas do trabalho, a disponibilização de informações do mercado de trabalho às entidades governamentais;  
Os dados coletados pela RAIS constituem expressivos insumos para atendimento das necessidades:   
·          Da legislação da nacionalização do trabalho;  
·          De controle dos registros do FGTS;  
·          Dos Sistemas de Arrecadação e de Concessão e Benefícios Previdenciários;  
·          De estudos técnicos de natureza estatística e atuarial;  
·          De identificação do trabalhador com direito ao abono salarial PIS/PASEP.

Para saber mais sobre a RAIS, consulte o site www.rais.gov.br.

Empresas que possuem filiais, agências ou outras unidades correlatas devem emitir uma RAIS para cada CNPJ existente.

Esse assistente é composto de 07 (sete) etapas pelas quais o responsável pela geração dos arquivos passará, definindo a composição dos mesmos, de acordo com o layout. São essas etapas:

**ETAPA1 - Perfil de Parâmetros e Descrição do Processo**          
Essa é a tela de abertura do assistente. Como o arquivo da RAIS possui uma composição de dados bastante complexa, esse módulo foi preparado para que pudessem ser gerados arquivos para cada uma das coligadas em apenas uma ou poucas execuções. O número de vezes que o assistente será executado dependerá, exclusivamente, das solicitações feitas pelo usuário, para cada uma das coligadas.  
Para aperfeiçoar essas execuções foi possibilitada a criação de perfis, que irão guardar a parametrização utilizada em cada uma dessas gerações. Além disso, é possível nomear o processo que está sendo executado caso o usuário queira,  agendar a criação do arquivo para outro momento. É nessa tela que se  inicia esse processo de criação de perfis e de nomeação de processos agendados relativos ao RAIS.  
Caixa "Perfil de Parâmetros"  
Essa caixa é composta de três itens:  
   
Nome do Perfil   
Esse é o local onde são criados novos perfis ou selecionados perfis criados anteriormente. Na primeira execução do assistente é obrigatória a criação de um perfil.  
   
Excluir   
Esse botão tem a finalidade de excluir um perfil que não é mais utilizado.  
   
Salvar perfil ao concluir   
Esse CheckBox tem a finalidade de indicar que o perfil que está sendo utilizado será modificado durante a execução do assistente e que tais modificações deverão ser gravadas. Ao utilizar um perfil sem a marcação desse parâmetro, caso o mesmo seja modificado durante o processo, essas alterações não serão gravadas. Na criação de um novo perfil esse parâmetro deverá estar marcado.  
   
Caixa "Descrição do Processo"

Nesse campo poderá ser nomeado um processo caso a execução do assistente seja feita com o intuito de agendar a geração do arquivo para outro momento. Para entender melhor esse processo, leia o help da 7ª etapa do assistente (Agendamento do Processo).  
Geração da RAIS - Parâmetros

**ETAPA 2 - Parâmetros**  
Nessa tela, são definidas as opções para emissão da RAIS para todas as coligadas selecionadas na 6ª etapa do assistente (Seleção de Coligadas).

Quebra de Seção  
Informe o código de quebra para o qual será emitido o relatório ou aceite o valor default (padrão).  
   
Observação 1:  
Conforme explicação no manual de orientação da RAIS, o sistema não irá informar o estabelecimento inscrito no Cadastro Específico do INSS (CEI), que não possuiu empregados no ano-base selecionado.  
   
Observação 2:  
Para o estabelecimento inscrito no CNPJ e que não possuiu empregados no ano base, o sistema irá informar este estabelecimento no arquivo, porém  no campo "Tipo de RAIS" será informado "1 – estabelecimento sem empregados".   
Lembrando que em Cadastros | Seções| Pasta Identificação a opção "Desativada" não deverá está marcada, caso esteja marcada esta seção não será informada na geração da RAIS.  
Observação 3:  
Quando existirem caracteres não numéricos no número ou série da carteira de trabalho do cadastro do funcionário, estes caracteres não serão considerados devido o validador da RAIS permitir somente caracteres numéricos.  
   
Seleção de Funcionários  
Aqui será definido qual o grupo de funcionários será informado no arquivo da RAIS.  
   
Observação  
Essa seleção verifica a Situação, Tipo e Código de Recebimento atuais dos funcionários.  
   
Ano Base RAIS  
Selecione o ano-base para geração das informações do arquivo.  
   
RAIS em Arquivo  
Selecionando esta opção o sistema irá habilitar os campos abaixo para a geração da RAIS.  
   
Gera RAIS Genérica  
Marcando este parâmetro o arquivo será gerado conforme layout do programa GDRAIS Genérico que permite informar os anos-base 1976 a 2005. Para maiores informações, consulte o site www.rais.gov.br.  
   
RAIS Retificadora  
Quando houver necessidade de emitir RAIS retificando dados do funcionário marque este campo que será informado no arquivo, no devido campo, que se trata de uma retificação do arquivo anterior.  
   
Data da Retificação:  
Este campo será habilitado somente se o parâmetro acima estiver marcado e será preenchido pelo usuário com a data da retificação para ser informada no arquivo que será retificado.  
   
CREA a ser retificado:  
(Controle de Recepção/Expedição de Arquivos) Este campo só ficará habilitado quando o parâmetro RAIS Retificadora estiver marcado. Neste caso, o preenchimento deste campo será obrigatório.  
   
Arquivo:  
Neste campo virá informando o nome do arquivo que será gerado no Drive escolhido anteriormente.  
   
Observação:  
Na geração do arquivo texto o sistema automaticamente fará substituições de caracteres acentuados pelos caracteres simples, pois algumas validações de arquivos textos exigem que os arquivos não contenham caracteres especiais.  
   
Localização do(s) arquivo(s):  
Salvar o(s) arquivo(s) na pasta:  
Selecione o caminho onde o sistema irá gerar o arquivo da RAIS, poderá utilizar a caixa de listagem ao lado. O sistema trará como default o disco local da máquina. Exemplo: C:\.  
Gera Rais para Conferência  
Selecionando esta opção o sistema emitirá a RAIS para conferência, a fim de permitir a correção prévia de eventuais erros.  
Ordenação  
Possibilita a ordenação do relatório Por PIS ou Por Nome.  
Este campo somente ficará habilitado se a opção "RAIS para conferência" estiver marcada.  
   
Layout:  
Selecione o layout para geração do arquivo.  
   
Gera registro para alteração de CEI  
Marcando este parâmetro o sistema irá verificar em Cadastros | Funcionários | Registro | Pasta Hist. Seção as mudanças de seções identificadas por CEI ocorridas no ano base da RAIS.  
Sendo que a data de mudança no histórico de seção representará a data de demissão no CEI antigo e a de admissão no novo CEI.   
Para os casos de mudança de CEI, a demissão será tipo 4 (sem ônus) na seção antiga e a admissão do tipo 31 (sem ônus) na nova.  
Observação 1:  
Se o funcionário não possuir histórico de seção, este funcionário não sairá na RAIS.  
   
Observação 2:  
O sistema irá verificar os meses nos quais o funcionário trabalhou em cada quebra de CEI.   
Nos meses onde houve a mudança, a movimentação vai para o mês onde o funcionário trabalhou mais dias.   
Exemplo 1:  
Funcionário: 00001  
Histórico de seção  
**Dt. Transf             Cod. Sec          Prefixo             Motivo**  
05/05/2004                     01.01                      00                          Admissão  
15/08/2006                     01.02                      01                          Transferência mesma empresa  
   
Ao gerar a RAIS ano base 2006, o funcionário sairá na movimentação dos prefixos 00 e 01, sendo que no prefixo 00 serão preenchidos os meses de 1 a 7, e no prefixo 01 os meses de 08 a 12 e as verbas do 13º salário.  
   
Exemplo 2:  
Funcionário: 00002  
**Dt. Transf             Cod. Séc         Prefixo           Motivo**  
10/10/2005                    01.01                     00                       Admissão  
20/11/2006                    01.02                     01                       Transferência mesma empresa  
   
Neste caso, para a RAIS ano base 2006 as verbas dos meses de 1 a 11 e a 1ª parcela do 13º Salário sairão no prefixo 00, e o mês 12 mais a 2ª parcela do 13º sairão para o prefixo 01.  
   
Atenção:  
O critério utilizado no mês da transferência, ou seja, qual seção será considerada a movimentação do funcionário no mês de transferência, é o dia 15. Se o funcionário mudou de seção no dia 15, a movimentação deste mês sairá na nova seção.

Projeta Aviso Prévio Indenizado na Data de Desligamento:

Conforme manual da RAIS ano-base 2014, apresentou novidades quanto a data de desligamento do empregado: *"VI - A data de desligamento deve ser a data de saída constante na carteira de trabalho (CTPS), que deve corresponder a data do término do aviso prévio, ainda que indenizado."*

Em relação a data de desligamento, pairaram algumas dúvidas relativas ao preenchimento correto deste campo, face a interpretação advinda do Manual da RAIS, assim o Ministério do Trabalho e Emprego (MTE) foi acionado solicitamos-lhes orientações quanto ao correto tratamento envolvido à declaração constante como 'Data Desligamento'. A TOTVS recepcionou tais esclarecimentos do Ministério do Trabalho e Emprego (MTE) em 12/03/2015, conforme transcrevemos abaixo:

“A data de desligamento que deve ser informada na RAIS é a data constante na Instrução Normativa Secretário de Relações do Trabalho – SRT Nº 15 de 14/07/2010 – na página relativa ao contrato de trabalho, a do último dia da data projetada para o aviso prévio indenizado.”

Face à tal esclarecimento e novas interpretações, implementamos o parâmetro “*Projeta Aviso Prévio Indenizado na Data de Desligamento”*para atender a Instrução Normativa acima. Recomendamos aos nossos clientes a revisão desta interpretação conjuntamente com os responsáveis na Empresa pela declaração da RAIS perante ao MTE, é importante que seja analisado e definido qual opção à Empresa fará (data da demissão ou data projetada), a TOTVS implementou no sistema o novo entendimento sem a remoção do anteriormente praticado.

Marcando o parâmetro descrito acima, o processo irá fazer a projeção da data de desligamento somando os dias de aviso indenizado à data de demissão, e caso a soma ultrapasse o último dia do ano base, não serão preenchidos os campos referente a "Data de Desligamento", Código do tipo de desligamento e verbas rescisórias no arquivo da RAIS:

**Atenção I:**Os valores das verbas rescisórias não serão levados devido o validador GDRAIS acusar erro pela falta de data de desligamento quando as verbas são informadas.

**Atenção II:**Os valores que não corresponderem a verbas rescisórias mas estiverem no movimento da rescisão serão levados normalmente para remuneração. Exemplo: Dias trabalhados, horas extras, faltas, comissões, etc.

Caso o funcionário tenha sido demitido no ano anterior ao ano base, e a data projetada tenha finalizado no ano base da RAIS, esse funcionário será levado para o arquivo com a sua data de demissão projetada, os valores da rescisão e aviso prévio.

**ETAPA 3 – Configuração de Afastamentos**

Alguns afastamentos não são considerados na RAIS (tipos de afastamento: ‘I – Após. Invalidez’, ‘R – Licença Remunerada’, ‘U – Outros’, 'S - Mandado Sindical', ‘C – Contrato de Trabalho Suspenso).

Caso o usuário queira informar estes afastamentos na RAIS (responsabilidade do usuário), ele deve associar os mesmos a algum tipo de afastamento válido (ao clicar no botão reticências serão listados os afastamentos compreendidos pela RAIS).

**ETAPA 4 – Configuração de Demissão**

Nessa etapa é possível substituir os tipos de demissão que não são considerados na RAIS para tipos validos (tipo de Demissão: ‘B – Rescisão determinada pela justiça’).

Caso o usuário queira informar está demissão na RAIS (responsabilidade do usuário), ele deve associar o tipo da demissão e o motivo da demissão a algum tipo de demissão válido (ao clicar no botão reticências serão listados os tipos de demissão compreendidos pela RAIS).
