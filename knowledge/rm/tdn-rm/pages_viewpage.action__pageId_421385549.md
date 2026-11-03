---
content_hash: 5a1953d9ee2e84b8ed0b68954d5c4d10a9a2d7f593c4fea27fe18889bbabc9cb
fetched_at: '2026-06-29T00:09:16.763361+00:00'
page_id: '421385549'
product: rm
source: tdn-rm
title: Restaurar Backup de Projeto 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385549
version: 3
---

---

Essa funcionalidade permite a realização de um backup de um projeto selecionado ou a restauração de um backup existente.

**Para fazer backup do projeto**

O processo está disponível em "Projeto | Backup/Restore" e devem ser efetuados os seguintes procedimentos: Marque a opção "Fazer Backup do Projeto"; Informe o local onde backup será salvo; Execute o processo.

Ao efetuar backup de projetos que utilizam a funcionalidade [Mobilidade](http://wikihelp.totvs.com.br:11801PRJ.Mobilidade) serão incluídas as tabelas relacionadas à Equipe.

**Observação:** As tabelas de mobilidade que serão restauradas possuem relação com a tabela PPESSOA que não estavam presente no processo de Backup/Restore, portanto ao restaurar um backup que não foi gerado a partir da mesma base em que está sendo restaurado, é possível que alguns registros não sejam criados, por não conter os respectivos códigos relacionados ao cadastro de pessoas. No entanto, caso o registro seja inserido sem erros, mesmo que a base destino seja diferente da origem, é porque o código existe na base, porém pode não ser o correspondente exato, ou seja, o código pode ser o mesmo mas o membro cadastrado pode não ser o correto.

**Exemplo:**

Base Origem: EQUIPE 001: Responsável (Relação PPESSOA): 01 – João da Silva

Base Destino: EQUIPE 001: Responsável (Relação PPESSOA): 01 – Maria de Souza

Depois do processo executado, os arquivos do backup do projeto corrente estarão disponíveis no diretório selecionado.

**Para restaurar o backup do projeto**

O processo esta disponível em "Projeto | Backup/Restore". Siga os passos abaixo:

Informe o diretório onde está armazenado o Backup do Projeto que será restaurado. Informe o novo código do projeto. O código é um campo obrigatório e caso não seja informado, o backup não será restaurado.

Opções de checkbox:

**Importar dados do BackOffice:** Caso este campo esteja marcado, o processo irá importar informações de condição de pagamento para as tabelas que possuem esse campo;

**Gravar no log a ocorrência de registros existentes:** Caso este campo esteja marcado, será exibido na mensagem de confirmação os logs que foram salvos.

**Não restaurar Composições e Insumos não utilizados no projeto:** Caso este campo esteja marcado, as composições e insumos que não são utilizados no projeto não serão importadas;

**Utilizar recursos Globais da coligada de destino:** Caso este campo esteja marcado fará com que a restauração não transforme em locais os recursos Globais existentes no destino, ou seja, o projeto será restaurado utilizando os recursos (Insumos, Composições e Grupo de Custo) Globais existentes na coligada, caso não exista o mesmo será restaurado como local.

Caso o parâmetro "Utilizar recursos Globais da coligada de destino" esteja marcado e a restauração esteja sendo realizada em outra coligada ou em uma base de dados que contenha  os insumos globais com preços divergentes dos preços globais de origem e estes insumos sejam calculados com base no preço Global poderá ocorrer alterações no valor

Assim que restaurados, os códigos dos insumos globais serão recodificados para RG-XXX, onde XXX é o id do insumo (campo IDISM, da tabela MISM). Todos os vínculos existentes antes de gerar o backup entre composições e insumos globais ou mesmo com tarefas, irão permanecer após a restauração. As integrações do projeto serão removidas durante o processo de restauração de backup. Os períodos liberados em contratos no projeto de origem serão apresentados apenas como períodos medidos depois da restauração do backup. Os pedidos de materiais serão excluídos depois da restauração assim como os períodos de estorno.

As Filiais, Centro de Custos e Departamentos não serão restaurados. Apenas se existir algum vínculo na tarefa ou contrato, sendo necessário ainda que exista a filial, centro de custo ou departamento cadastrado na base de dados.

Os dados da condição de pagamento só serão garantidos e importados corretamente se a restauração do backup estiver acontecendo na mesma base e coligada na qual foi realizado o backup. Funcionará também se a base/coligada na qual o backup foi realizado possuir o mesmo código identificador da condição de pagamento da base/coligada na qual o projeto será restaurado.

É recomendado que, para restauração entre coligada/base diferentes, a opção "Importar dados do BackOffice" seja desmarcada e a condição de pagamento informada depois da restauração concluída, pois, existe o risco de não ser importado ou de ter valores substituídos.

 Informações Complementares

---

[Agendamento de Backup](http://tdn.totvs.com/pages/viewpage.action?pageId=421385146)
