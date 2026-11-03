---
content_hash: b02083f648d78e512fbd70414e2737eb51659fb988cb5fcbbf34bc276d08920d
fetched_at: '2026-06-29T00:09:12.777703+00:00'
page_id: '417700491'
product: rm
source: tdn-rm
title: Importador / Internação e Alta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700491
version: 2
---

**Importador / Internação e Alta**   
Foi implementado ao sistema de CIH o Menu Utilitários – Importador   
Para automatizar a aquisição de dados, reduzindo o retrabalho e promovendo uma integração mais transparente com o sistema de gestão de saúde da instituição.  
Os profissionais do controle de infecção podem se concentrar em agregar valores as informações exibidas pelo sistema ao invés de dedicar tempo e esforço a re-digitação de dados.   
A versão oferece dois tipos de importação: Utilizando arquivos TXT, formatados de acordo com o layout fornecido, gerados pelo sistema de gestão de saúde da instituição ou através de VIEWS, empregando um acesso direto ao banco de dados do sistema de saúde.   
Ao importar por view na tela do importador exibira as opções:  
Provedor  
Campo usado para definição do tipo de conexão que será usada. São pertencentes a esse conjunto:  
ODBC Data Provider e OLE Data Provider - Utilizados para conexão com outros bancos, que não MS SQL Server ou ORACLE, de acordo com a disponibilidade de drivers.  
Oracle Client Data Provider - Usado para conexões que o banco de dados utilizado é oracle  
SQLClient Data Provider - Usado para conexões que o banco de dados utilizado é SQL  
String de Conexão  
Campo onde será informada a configuração da máquina onde está localizada a base de origem, onde será feita a importação dos dados. É de suma importância o preenchimento dos campos.  
Para conexão Oracle Client Data Provider é necessário preencher:  
Data Source: Indica o nome do banco de dados ao qual conectar.  
Persist Security Info: Quando for falso, informações de senhas não serão gravadas na string de conexão, sendo assim para que o processo de importação funcione como desejado a o preenchimento deste campo devera ser True.   
Password - Usado para acesso ao banco de dados.   
User ID - Usado para identificar o nome de usuário que fará acesso ao banco de dados.   
Após criar a string de conexão, realizar teste de conexão. Salvar e escolher o período a ser importado.  
Para conexão SQLClient Data Provider:  
Data Source – Indica o nome da máquina na rede ao qual conectar.  
Initial Catalog – O nome do bando de dados ao qual conectar.  
Persist Security Info: Quando for falso, informações de senhas não serão gravadas na string de conexão, sendo assim para que o processo de importação funcione como desejado a o preenchimento deste campo devera ser True.   
Password - Usado para acesso ao banco de dados.   
User ID - Usado para identificar o nome de usuário que fará acesso ao banco de dados.   
Após criar a string de conexão, realizar teste de conexão. Salvar e escolher o período a ser importado.  
Para os tipos ODBC Data Provider e OLE Data Provider não foram realizados testes internos.  
Após clicar no botão Importar Agora será gerado a tela de log com as devidas mensagens:  
O log gera:  
Cabeçalho - Contendo informação do período importado, data da importação e hora da importação realizada por view. Já a importação realizada por TXT informa o caminho do arquivo importado.   
Corpo da mensagem – Informando mensagem de ERRO ou AVISO informando sobre eventos importantes ocorridos durante o processo.  
E por fim Rodapé – Informando um sumário de registros importados, além de outras informações específicas de cada tipo de importação.  
Exemplo  
Cabeçalho importação realizado por TXT  
Importação do arquivo C:\Documents and Settings\Desktop\NomedoArquivo.txt  
Cabeçalho importação realizado por View  
Importação do período de dd/mm/aaaa à dd/mm/aaaa, realizada em dd/mm/aaaa, às hh:mm  
Corpo  
Aviso - Provável problema de paciente duplicado:  
 Apresentará o numero do prontuário - Apresentará o nome do paciente    
 Apresentará o numero do prontuário - Apresentará o nome do paciente    
Erro - Internação ou paciente não encontrados:  
 Apresentará o numero do prontuário - Apresentará o nome do paciente    
Rodapé  
Processo concluído com avisos.  
Informações especificas a importação   
Processo concluído com erros.  
Informações especificas a importação   
Observação  
As mensagens de erro são geradas quando o importador recebe dados que comprometem a integridade da base, dados para os quais não se pode determinar um registro único de gravação ou dados que violem alguma consistência que já exista na base de CIH.  
Já as mensagens de aviso dizem respeito a dados que, por mais que estejam incompletos, são passíveis de serem ajustados, quer manualmente, quer pela reimportarão dos dados após uma correção na base de origem.   
Para evitar mensagem de aviso no que diz respeito a códigos inválidos na base destino, utilize o campo CODCLIENTE para informar o código na base origem.  
Exemplo  
Existe na base origem uma especialidade de código AB, na base destino a mesma especialidade possui o código CD. Antes de importar o registro, na tela de cadastro especialidade da base destino preencha o campo Codcliente com o código AB.   
O sistema de CIH oferece importação dos seguintes itens:  
Paciente Internação e Alta  
Observação   
Para as consistências

* Caso no arquivo importado, informe um tipo de alta que não seja um tipo de alta válido no sistema de CIH.
* Caso no arquivo a ser importado, não informe a data de alta, mas informe a tipo de alta.
* Caso no arquivo a ser importado, não informe o motivo da alta ,mas exista data de alta.  
  Exibirá log com mensagem de aviso, será importado para a base destino o paciente e sua internação, mas se o arquivo possuir algumas das três inconsistências não será importado data de alta e motivo de alta.  
     
  Para as consistências:
* Validação de unidade clínica - A unidade clínica deve ser válida.  
  -Validação de especialidade - A especialidade deve ser válida.   
  -Validação de convênio – O convênio deve ser válido.   
  Será gerado log com mensagem de AVISO e o campo onde estiver nulo (desde que não seja obrigatório) ou que não tenham valores validos para a base de CIH, após importação o campo ficara em branco. O restante do registro será importado normalmente.  
  Para a consistência:  
  Quando o primeiro nome do paciente é igual ao primeiro nome de algum outro paciente, a data de nascimento de ambos é a mesma e o prontuário é diferente.   
  Será gerado log com mensagem de aviso.  
  Esta consistência não é feita para recém-nascidos.  
  Para as consistências:
* Internações sobrepostas (período de uma internação dentro do período de outra internação).
* Internações com mesma data de alta e data de internação diferente ou mesma data de internação e data de alta diferente para o mesmo paciente. São tidas como internações inconsistentes.
* Numero de prontuários iguais e nomes diferentes. (Esta consistência não é feita para recém-nascidos).  
  Será gerado log com mensagem de erro.  
     
  As consistências abaixo servem para alertar ao usuário que sua base de CIH está errada, É um problema de lançamento de dados que é verificado no momento da importação.   
  -Quando o paciente for recém-nascido  
  Se existir, na base de destino, mais de um paciente com o mesmo prontuário, verifica-se se existe um paciente com mesmo nome e data de nascimento, porém prontuários diferentes.
* Quando o paciente não for recém-nascido  
  Se existir mais de um paciente com mesmo prontuário na base de destino.
