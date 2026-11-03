---
content_hash: c47aab3e72f52ce81c1f242cf8aa66e3e5ce6e94b31cdcf7576e739381c887d0
fetched_at: '2026-06-29T00:10:56.137534+00:00'
page_id: '592067102'
product: rm
source: tdn-rm
title: Cópia de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592067102
version: 36
---

## **01. VISÃO GERAL**

Utilizando a funcionalidade de Cópia de Dados é possível copiar parâmetros e entidades entre Coligadas. Pode ser utilizado tanto para a primeira configuração de uma nova Coligada ou para replicar dados entre Coligadas existentes. 

É possível criar templates determinando quais entidades do sistema devem ser copiadas. 

Veja a seguir os cadastros utilizados pelo sistema para utilizar a Cópia de Dados. Menu disponível em: **Serviços Globais > Administração > Cópia de Dados**.

Obs.: Em versões anteriores, o menu de Cópia de Dados era apresentado como 'Cópia de Coligada.'

**02. CADASTRO DE ENTIDADE**

O cadastro de entidade representa os vários cadastros que o sistema tem e que pode ser copiado. As entidades são disponibilizadas pela Totvs RM.

## **03. CADASTRO DE TEMPLATE**

Alguns templates são disponibilizados pela Totvs RM. Também é permitido criar novos templates de acordo com a sua necessidade. Não é permitido alterar/excluir templates padrão do sistema, mas ele pode ser clonado e editado, conforme descrito no passo 04. Cópia de Template.

Para criar um novo Template, após clicar em **Novo**, os seguintes campos devem ser informados:

**Descrição do Template:** Informe um nome para identificação do template;

**Buscar dados na base aceleradora o externa:**

* **Base acelerado:** Os dados de origem serão buscado da base modelo (acelerador) que estará em cloud (Azure)**.**
* **Base externa:**Os dados de origem serão buscado da base externa cadastrada.

Importante

Existe um parâmetro no cadastro de base externa "**Habilitar para buscar os dados de origem**" que é responsável pela habilitação automática da utilização da base externa quando o usuário marcar o parâmetro "**Buscar dados na base aceleradora o externa**".

**Versão:** Campo para inserir a versão do objeto. Exemplo: Se a liberação se dará na versão 12.1.2209, deve se informar 12.1.

O campo "**Versão**" só pode ser modificado pela TOTVS.

IMPORTANTE

A partir da versão 12.1.2209

* Adicionado o cálculo de CRC.
* Adicionado no Atualizador do RM um script para gerar o CRC nos templates antigos.
* A partir do Patch 151, controle de segurança e edição passou a ser realizado pelo Perfil de Segurança.

**Selecione a entidade para associar ao template:** Selecione a entidade que será copiada entre uma Coligada e outra. Estarão disponíveis para cópia as entidades do tópico 'Cadastro de Entidade' deste documento. Neste exemplo vamos realizar a cópia das Fórmulas.

**Ordem Execução:**É possível configurar a ordem de execução de cada entidade adicionada ao template; Representa a ordem que cada entidade será copiada (primeira, segunda...). Por padrão todas são adicionas com Ordem de Execução = 1.

**Transação:**Se o ambiente estiver configurado para executar o job de Cópia de Dados de forma fracionada, leia mais em: , a transação pode ser informada para separar um conjunto de cópias dentro de uma transação. Para cada transação será gerada um job no job fracionado, por isso os conjuntos de cópias precisam ser independentes umas das outras.

Ex.: Entidade Cópia de Fórmulas com transação = 1 e entidade Relatórios com transação = 2 no mesmo template.

Ao executar a cópia com o fracionamento de jobs, a cópia de fórmulas será feita na primeira transação (job) do fracionamento e a cópia de relatórios na segunda.

Exemplo de log

Iniciando execução do job principal - com fracionamento  
Foram criados 2 jobs filhos  
Finalizada a execução dos 2 jobs filhos  
Fazendo Merge dos Logs de todos os jobs filhos  
Resumo de execução dos jobs filhos:  
Job 102830-1 Status: 'Executado com sucesso'.  
Job 102831-1 Status: 'Erro na execução'.

Onde o job 102830-1 foi a execução de cópia das fórmulas e o job 102831-1 foi a execução de cópia do relatório.

Cada template é representado por um job, quando um processo for executado com erro dentro de um template, todos os outros processos (pertencentes a esse mesmo template) que foram executados com sucesso, serão feitos rollback, ou seja, o template (Job) será mostrado como "Erro na execução" (como mostra o "Exemplo de log" no expandir acima).

Caso haja outros templates separados que não deram erros, o fluxo correto é que eles sejam executados normalmente (com sucesso).

Após a correção do erro detectado na execução do processo, o usuário poderá executar normalmente o processo, pois quando executado só será considerado a execução daquele template que ocorreu o erro, desconsiderando os que já foram executados com sucesso.

**Filtro para buscar os registros:**Podem ser criados filtros nos registros de cada uma entidade. O cadastro de filtro é similar ao cadastro das demais telas do sistema. Saiba mais em:  e . Se nenhum filtro for cadastrado, todos dados serão copiados.

**Cópia Obrigatória:**Quando esse campo está marcado no template de origem, ao criar uma cópia desse template outros usuários não poderão excluir essa entidade.

**Incluir Selecionada:** Inclui a nova entidade selecionada em 'Parâmetros do template' no template aberto.

**Incluir Todas:**Essa opção inclui todas as entidades cadastradas no sistema no template aberto.

Após incluir a entidade, é possível alterar algumas informações no próprio grid de listagem do template:

Depois de criar o template, use o processo Cópia de dados descrito neste documento, para execução da cópia das entidades.

### **03.01 Regra de permissão para edição**

A partir da versão 12.1.2209 Patch 151, houve uma alteração para adequar a permissão de edição de um template para seguir o mesmo padrão dos objetos gerenciais.  
O controle de segurança e edição passou a ser realizado pelo Perfil de Segurança.

* + Template versionado não pode ser editado.  
    Caso exista alguma informação no campo Versão o template será considerado como versionado e será impedido de ser alterado.
  + Cópia e importação de qualquer template, será editável.  
    Para qualquer template, de qualquer usuário que for Copiado ou Importado, este novo template passará a ser de propriedade do usuário logado e será permitido editar.
  + A permissão de segurança deve sobrepor as demais.  
    Caso o Perfil de Segurança esteja configurado com restrições de acesso, edição e etc, elas terão prioridade sobre as regras acima.

Caso seja usado o argumento #objetos\_gerenciais

* + Os templates versionados serão possíveis de editar e o campo de versão estará liberado.
  + A permissão de segurança deve sobrepor as demais, exatamente como descrito mais acima.

### **03.02 Regra de exclusão de template**

           Como dentro dessa funcionalidade existem regras específicas com relação aos templates, a sua exclusão deve ser feita sempre pelo processo **Exclusão de Template**, no menu processos.

## **04. CADASTRO BASE EXTERNA**

        É um cadastro onde é possível cadastrar uma base externa, para buscar dados de uma coligada diferente da base que está sendo utilizada.

Observação

Ao realizar a comunicação com a base externa, é necessário que o usuário que fará a conexão esteja vinculado a um código de acesso que tenha permissão na base de dados de origem.

               

        Na tela de cadastro de base interna, temos os seguintes campos:

* **Usuário para Conexão:** Usuário que realizara a conexão com a base externa
* **Alias da base externa:** Seleção do alias que será utilizado (deve estar cadastrado no gerenciamento de alias)
* **Habilitar para buscar os dados de origem:** Parâmetro utilizado para quando o usuário for buscar dados de origem dessa base externa, caso esteja desabilitado os dados serão buscados da base base local ou da base acelerado (depende de como o seu template está configurado).

       

        Quando marcado o a parâmetro "**Habilitar para buscar os dados de origem**" é possível visualizar em dois momentos que o mesmo está habilitado:

* A primeiro momento é na tela de cadastro de template, quando selecionado o parâmetro "**Buscar dados na base aceleradora o externa**" é possível visualizar na tela que a base externa está ativa.

       

* O segundo momento é na execução do processo de Cópia de dados, onde também existe uma mensagem informando: "**Origem de Dados: base externa ativa**".

       

Importante

Quando utilizada a base externa como origem dos dados, é mostrado um novo campo "**Coligada Origem**" no processo de Cópia de Dados, que consiste na escolha de qual coligada será buscado os dados para a cópia, a marcação dele é obrigatória. 

**05. CÓPIA DE TEMPLATE**

Para facilitar a criação de templates semelhantes, é possível duplicar um template existente. Para editar um template padrão é necessário criar uma cópia para customizá-la.

Basta selecionar o template desejado, menu Processos > Cópia de templates:

A ordem de execução, transação e cópias obrigatórias não podem ser alteradas em um template copiado por um usuário diferente de quem criou o template.

## **06. CÓPIA DE DADOS**

Para executar a cópia das entidades, selecione o template desejado, clique em Processos >> Cópia de Dados.

Depois, selecione a(s) Coligada(s) que receberão as cópias da Coligada corrente no contexto:

Marque a opção 'Substitui registros no destino se eles já existirem' se for desejado que os dados copiados prevaleçam sobre os dados já existentes na Coligada.

**Observação:** Algumas entidades não podem sobrescrever os dados de mesma chave, mesmo com o parâmetro habilitado, como por exemplo, na entidade de Relatórios. Caso isso ocorra, o processo pode retornar erro de índice existente.

Depois de executar o processo, veja o log da execução:

Aba Execução:

Após a execução, todas as Fórmulas da Coligada 1 foram copiadas para a Coligada 6. No Log de execução é possível identificar se o registro foi incluído, atualizado ou não alterado (se já existir na Coligada destino e não foi marcado para substituí-lo).

**Observação:** Esse job deve ter permissão de fracionamento de jobs em ambientes 3 camadas. Veja mais sobre .

## **07. ANEXO - LOGS DE EXECUÇÕES DO TEMPLATE**

Para visualizar o histórico de execução dos templates, acesse Anexos > Logs de execuções do template:

No anexo é possível consultar se a cópia foi realizada com sucesso ou falha. É possível reexecutar o processo pelo menu Processos > Reprocessamento de Cópia de Dados:

Após executar este processo, será retornado no log de execução o ID do job que fará o reprocessamento. Exemplo:

O status desse novo job pode ser consultado na própria tela de Anexo, ou na tela de Gerenciamento de Jobs ():

O reprocessamento de Cópia irá executar apenas a parte da Cópia que retornou erro e não executadas dentro de um conjunto de cópias , como uma nova tentativa de sucesso, caso algum ajuste na base tenha sido feito. Os conjuntos de cópias executados com sucesso na execução original não é reprocessado, pois os dados já foram salvos, visto que os conjuntos de cópias são independentes.

Exemplo ao tentar reprocessar um job de status de sucesso:

Exemplo ao tentar reprocessar uma cópia com 2 transações, onde a primeira foi executada com sucesso e a segunda com erro:

Apenas a cópia com erro foi reprocessada.

* Os parâmetros das cópias, ordem, conjunto de cópias (transações), filtros serão os mesmos da execução original.
* Origem dos dados (em Cloud) irá obedecer o que está atualmente informado no template.
