---
content_hash: 6f647c4ed33564dba2e21b5cb9a6d59a22e7cb91f6993bc9f85f41d438a7e969
fetched_at: '2026-06-29T00:09:15.487509+00:00'
page_id: '421385391'
product: rm
source: tdn-rm
title: Backup e Restore de Projetos
type: documentation
url: https://tdn.totvs.com/display/LRM/Backup+e+Restore+de+Projetos
version: 89
---

---

Essa funcionalidade faz o backup de um projeto selecionado ou a restauração de um backup existente.

Para acessá-la vá em: TOP | Projeto | Utilitários | Backup e Restore.   
   
O Sistema automaticamente entenderá que se trata de:

* **Backup:** Se a funcionalidade for acessada dentro de um projeto aberto.
* **Restore:** Se a funcionalidade for acessada com a visão de projetos estiver aberta.

**Backup do Projeto**  
   
Para fazer backup do projeto:   
Informe o caminho onde o backup será salvo;  
Execute o processo.

Ao efetuar backup de projetos que utilizam a funcionalidade Mobilidade serão incluídas as tabelas relacionadas à Equipe.

As tabelas de mobilidade que serão restauradas possuem relação com a tabela PPESSOA que não são presentes no processo de Backup/Restore, portanto ao restaurar um backup que não foi gerado a partir da mesma base em que está sendo restaurado, é possível que alguns registros não sejam criados, por não conter os respectivos códigos relacionados ao cadastro de pessoas. No entanto, caso o registro seja inserido sem erros, mesmo que a base destino seja diferente da origem, é porque o código existe na base, porém pode não ser o correspondente exato, ou seja, o código pode ser o mesmo mas o membro cadastrado pode não ser o correto.   
Exemplo:     
Base Origem: EQUIPE 001: Responsável (Relação PPESSOA): 01 - João da Silva Base Destino: EQUIPE 001: Responsável (Relação PPESSOA): 01 - Maria de Souza

**BIM:** Estarão presentes nos arquivos de backup as seguintes tabelas:

* MTIPOTAREFA: Informações do tipo de tarefa relacionada ao modelo BIM;
* MTIPOTAREFAFORMULA: Fórmulas relacionadas ao tipo de tarefa, utilizadas no processo de extração de quantitativos do modelo 3D;
* MBIMMODELO: Associação do arquivo BIM ao projeto;
* MBIMMODELOTAREFA: Associação das tarefas aos objetos ao modelo 3D;
* MBIMAPARENCIA: Aparências relacionadas ao tipo de tarefa.

**Restore do Projeto**  
   
Para restaurar um backup siga os passos abaixo:  
**Caminho do backup/restore**   
Informe o caminho do diretório onde está armazenado o Backup do Projeto que será restaurado;

**Novo código do projeto**   
Informe o novo código do projeto. O código é um campo obrigatório e caso não seja informado, o backup não será restaurado;

Opções de checkbox:

**Importar dados backoffice:**  
Caso este campo esteja marcado, o processo irá importar a condição de pagamento para as tabelas que possuem esse campo;

**Gravar no log a ocorrência de registros existentes:**

Caso este campo esteja marcado, será exibido na mensagem de confirmação os logs que foram salvos;

**Não restaurar Composições e Insumos não utilizados no projeto:**   
Caso este campo esteja marcado, as composições e insumos que não são utilizados no projeto não serão importadas;

**BIM:** As tabelas do backup serão restauradas considerando as seguintes regras:

* MTIPOTAREFA: Somente registros nos quais seus respectivos códigos (CODTIPOTAREFA), não existam na base destino;
* MTIPOTAREFAFORMULA: Somente registros que não existam na base, onde a verificação é feita através das informações de Coligada, Aplicação e Código da Fórmula;
* MBIMMODELO: Somente registros onde o arquivo do modelo já está associado a algum projeto da base destino;
* MBIMMODELOTAREFA: Somente registros onde o modelo foi restaurado para o projeto destino;
* MBIMAPARENCIA: Somente registros que não existam na base, onde a verificação é feita através das informações de Descrição, Cor e Transparência;

 Veja Também

---
