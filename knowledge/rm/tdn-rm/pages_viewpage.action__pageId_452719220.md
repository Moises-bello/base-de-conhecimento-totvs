---
content_hash: aa5c80fed68c2ac2cedabbffc34be3fd9d52cb930981fe9f1f72c2013d040215
fetched_at: '2026-06-29T00:10:04.571204+00:00'
page_id: '452719220'
product: rm
source: tdn-rm
title: Procedimento de Geração dos Arquivos MANAD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719220
version: 3
---

**Procedimento de Geração dos Arquivos MANAD**   
 Aqui se encontram as etapas pelas quais o usuário do RM Labore irá passar para a correta geração dos arquivos do MANAD. O objetivo desse material é auxiliar o cliente na verificação dos dados presentes na base de dados para a confecção de um arquivo com informações mais consistentes.  
    
 Antes de executar o procedimento aqui descrito, recomendamos a leitura do manual explicativo do MANAD, presente no site da Receita Federal, bem como o download, instalação e a leitura do manual do aplicativo SVA (também disponível no site da Receita). Tenha certeza de que entendeu bem todas as informações disponibilizadas nesses manuais.  
    
 Abaixo segue um breve resumo dos principais blocos que contém as informações mais relevantes para o entendimento daquilo que está sendo levado para o arquivo gerado.  
    
 Os blocos que começam com 0 indicam o cabeçalho do arquivo. Os demais blocos começam com a letra K, com exceção do Bloco I050 que é o cadastro de Plano de Contas Contábeis.  
    
 **Bloco 0000**

Leva os dados das filiais ou das seções (De acordo com o parâmetro na geração do relatório).

**Bloco 0050**

Dados do contabilista informados na geração do arquivo.

**Bloco 0100**

Dados do responsável pela geração do arquivo, informado na geração do relatório.  
 **Bloco I050**

Plano de contas contábeis.

**Bloco K050**

Cadastro dos funcionários.  
    
 **Bloco K100**

Cadastro de lotações, as seções do sistema.

**Bloco K150**

Cadastro de Rubricas, eventos do sistema.

**Bloco K200**

Contabilização. Eventos, seções e suas contas. O Labore não gera a contabilização por centro de custo por ocorrer um erro de validação por problema do próprio programa do fiscal.

**Bloco K250**

Mestre da folha de pagamento. Leva uma linha para cada funcionário, para cada mês com a base de INSS e IRRF total do mês.

**Bloco K300**

Itens da folha de pagamento. Leva os eventos da ficha financeira e sua incidência em INSS e IRRF. O total desses eventos deve corresponder à base informada no Bloco K250.  
 Seguem abaixo os passos de verificação, geração e validação do arquivo do MANAD.

**PASSO 01:**

Verificar a parametrização da contabilidade.  
 A execução desse passo dependerá diretamente do requerimento do Auditor Fiscal ou do órgão que solicitou o arquivo do MANAD. Na solicitação, geralmente é explícita a necessidade de geração do bloco K200 (Dados Contábeis). Quando não há nenhuma citação sobre esse tipo de geração, recomendamos o envio do arquivo contendo os dados contábeis da folha de pagamento (com o bloco K200).  
 Caso a contabilização não tenha sido parametrizada, ou caso ache importante fazer uma revisão dos processos hoje inseridos no RM Labore, é necessária a leitura e execução dos procedimentos presentes no Roteiro de Contabilização.  
 Além da parametrização citada acima, existe um dado que não era utilizado pelo RM Labore em nenhum processo contábil e que, por isso, não é citado em nenhum outro documento de parametrização da parte contábil: Natureza da conta para a emissão do SPED. No registro I050 (Plano de Contas) essa informação é utilizada para o preenchimento do campo Indicador da Natureza, onde são informadas se as contas são patrimoniais ou de resultado. Portanto, é de extrema importância que essa informação seja preenchida em todas as contas do plano de contas contábeis.  
 Para fazer uma verificação mais rápida das contas que necessitam ser atualizadas é possível executar uma query no banco.

**Exemplo de query:**

SELECT CODCONTA,NATSPED

FROM CCONTA

WHERE NATSPED IS NULL

Caso essa query não discrimine nenhuma conta é porque as todas elas estão preenchidas corretamente.

**PASSO 02:**

Verificar cadastro de funcionários.

Como são utilizados dados de funcionários na confecção de vários blocos, é extremamente importante que os dados cadastrais do mesmo estejam corretos e completos.  
    
 Para a geração do MANAD uma das informações mais importantes é o Histórico de Seção do funcionário. Através do histórico de seção que o sistema gera registros de transferência, de movimentação em filiais diferenciadas, etc.  
 Porém, existe uma obrigatoriedade quanto ao histórico de seção do funcionário: nesse histórico deve haver o registro com a seção na qual o funcionário foi lotado no momento de sua admissão, ou seja, deve haver um registro cuja data de mudança é igual à data de admissão do funcionário. Geralmente, empresas que possuem grandes números de transferências ou que tiveram as informações importadas de outros sistemas podem encontrar mais problemas quanto a esse tipo de informação.  
 Para facilitar a verificação das informações citadas acima é possível executar uma query (consulta SQL) que indica quais as chapas estão com o histórico de seção sem o registro da admissão.

**Exemplo de query:**

SELECT B.CHAPA

FROM PFUNC B

WHERE

B.CODCOLIGADA=1 AND

B.CHAPA NOT IN(

SELECT A.CHAPA

FROM PFHSTSEC A,PFUNC B

         WHERE

A.CODCOLIGADA=B.CODCOLIGADA AND

A.CHAPA=B.CHAPA AND

A.CODCOLIGADA=1 AND

A.DTMUDANCA=B.DATAADMISSAO

)

ORDER BY B.CHAPA

Infelizmente não há uma rotina que acerte esses cadastros. Portanto, para ajustar essas informações será necessário acessar o cadastro de cada uma das chapas citadas na query acima, corrigindo o histórico de seção do funcionário.

Caso os autônomos que prestam serviços para a empresa sejam cadastrados no RM Fluxus e não no RM Labore, veja o Roteiro para informar autônomos do RM Fluxus no MANAD.

**PASSO 03:**

Verificar se existe movimentação na Ficha Financeira ou Ficha Financeira Complementar no o período solicitado.  
 Em Opções | Parâmetros | RM Labore | Outros Parâmetros é possível definir por quanto tempo a movimentação será mantida na ficha financeira do funcionário e se a mesma será excluída da base de dados ou mantida na ficha financeira complementar. Antes que iniciar a geração do MANAD é muito importante fazer essa verificação, pois, caso a movimentação tenha sido excluída da base de dados, a geração do arquivo deverá ser feita através de um ambiente de teste com a restauração de um backup que contenha essas informações.  
 Caso a movimentação exista ou na ficha financeira ou na ficha financeira complementar, a geração do arquivo poderá ocorrer com sucesso. A única verificação que deve ser feita, nesse caso, é apurar se essa informação está aparecendo, em duplicidade, tanto na ficha financeira normal quanto na complementar. Se isso ocorrer a movimentação da ficha financeira complementar deverá ser apagada.

**Observação:**

Não é necessária a execução da rotina de Restauração da Ficha Financeira Complementar.

**PASSO 04:** Verificar cadastro de eventos.

Esse passo consiste unicamente em verificar as incidências dos eventos. É comum o Auditor Fiscal solicitar a movimentação de um período cujos eventos não são mais utilizados nas movimentações atuais.  Portanto, uma verificação criteriosa das incidências pode garantir informações mais consistentes.

**PASSO 05:** Gerar arquivo do MANAD.

Após realizar todas as verificações recomendadas, o arquivo do MANAD está pronto para ser gerado. Para esse passo é recomendada a leitura do help do Assistente de Geração de arquivo para o MANAD.

**PASSO 06:** Importar o arquivo gerado no aplicativo SVA.

O aplicativo SVA é um programa disponibilizado pela Receita Federal para garantir que as empresas entreguem o Arquivo Digital dentro do padrão de leiaute pré-estabelecido. No momento da importação o programa verifica, bloco a bloco, se as informações estão inseridas corretamente nos campos definidos e, feito isso, verifica se as informações dos blocos superiores estão de acordo com os blocos inferiores.

Abaixo, segue um pequeno procedimento que irá auxiliar o usuário na importação do arquivo no aplicativo da receita.  
 Ao acessar o aplicativo pela primeira vez, será aberta uma tela onde deverão ser inseridos os dados da empresa, do responsável pela mesma (proprietários, diretores, etc.) e do responsável pela geração de importação do arquivo (usuário). É obrigatório o preenchimento de todos os campos dessa tela.

Após o preenchimento dos dados, acessar a aba Arquivo(s) Selecionado(s), clicar em Selecionar Arquivo (s) e selecionar o arquivo gerado. Feito isso, clicar em Validação (MANAD) e, em seguida, em Empresas em Geral.

Após a validação do arquivo, o SVA irá demonstrar na tela o Resumo da Validação, contendo o número de registros importados, erros e avisos por bloco. Para verificar com detalhes o que ocorreu, clique em Mensagens da validação e Relatório Analítico de Mensagens da Validação.  
    
 Os dados relevantes para a análise desse relatório são:

**Tp Reg**

É o bloco onde ocorreu o erro.

**Nº linha**

Se refere a linha no arquivo importado que pode ser localizada pelo bloco de notas com o comando CTRL + G .

**Tp Msg**

Pode ser Erro ou Aviso. Lembrando que mesmos os avisos devem ser acertados, a não ser que tenham justificativas.

**Mensagem**

É a mensagem detalhada do erro.

**Observação**

Mais um detalhe do erro, pode ser o número da chapa, o número da conta, depende a que se refere.

Após a apuração e correção de todos os erros, os passos 05 e 06 deverão ser executados novamente até que não seja apresentado nenhum erro no Resumo da Validação do SVA.
