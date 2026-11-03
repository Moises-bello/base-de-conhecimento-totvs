---
content_hash: 03db042bf425112596f513ee7b30a2e7e780419f41acda85d11dc670f9863753
fetched_at: '2026-06-29T00:10:30.120059+00:00'
page_id: '519198454'
product: rm
source: tdn-rm
title: Log de Auditoria - LGPD (Lei Geral de Proteção de Dados)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519198454
version: 12
---

Com o Log de Auditoria podemos obter um histórico de todas as inclusões, alterações e exclusões que ocorreram na(s) tabela(s) selecionada(s) para serem auditadas.

O Log de auditoria é composto por uma série de Procedures, onde quando é(são) selecionada(s) uma tabela(s) a ser(em) auditada(s), cria-se uma "**Tabela Espelho**" em um Schema exclusivo do Log de Auditoria(**TOTVSAUDIT**) e **Trigger(s)**no banco de dados, dependendo da ação escolhida (**Insert, Update, Delete**).

Quando houver transações que utilizam a(s) tabela(s) selecionada(s), a Trigger é disparada e grava na tabela de Log (**ZAUDITCHANGES**) as informações sobre o autor da ação, e os dados que foram criados, alterados ou deletados é salvo na "Tabela Espelho"  (Ex.: TOTVSAUDIT.PFUNC, tabela espelho a tabela do sistema RM.PFUNC).

Estas informações podem ser consultadas através de QUERY´s no banco de dados ou através da interface do usuário do Log de Auditoria.

Com a criação da lei do LGPD (Lei Geral de Proteção de Dados), o Log de Auditoria sofreu algumas alterações.

A partir deste momento tabelas que possuam ao menos um campo considerado SENSÍVEL/PESSOAL passará a ser auditada automaticamente caso o Log de Auditoria esteja habilitado, nesta condição o usuário não poderá desmarcar a(s) tabela(s) que possuem este tipo de dados.

Além de serem automaticamente auditadas pelo sistema, os campos que sejam considerados SENSÍVEL/PESSOAL não poderão ser excepcionados.

O funcionamento do Log de Auditoria para LGPD será mostrado mais abaixo no manual.

**Pré - requisitos:**

**Homologação Conversões de Bases de Dados Oracle**

Caso seja necessário se restaurar uma base de dados Oracle em um ambiente de homologação, utilizando-se das ferramentas IMP e IMPDP, deve-se restaurar o Schema RM,  após o final da restauração deve-se executar a Stored Procedure p\_FixNovoLog.

**Comando:** EXEC p\_FixNovoLog

Esta nova Stored Procedure faz uma verificação e cria/recria os objetos necessários para o correto funcionamento do Novo Log de Auditoria, Schema, Tabelas, Grants, Etc.

**Passo a passo:**

1. Para habilitar o Log de Auditoria vá em Serviços Globais, Administração, Log de Auditoria, Configurações:
2. Após clique no botão Inativo para que o mesmo mude para Ativo:

    3. Clique em Salvar

Com a implementação da LGPD, a partir do momento em que o Log de Auditoria é habilitado todas as tabelas que possuem ao menos um campo considerado SENSÍVEL/PESSOAL, passará a ser auditada automaticamente, e será apresentada na lista de tabelas com o fundo cinza, e sem opção de se desmarcar as ações de auditoria.  
  
Abaixo temos o exemplo da GUSUARIO, que neste exemplo possui campos considerados SENSÍVEL/PESSOAL

**A partir do momento que o Log estiver ativo você poderá selecionar as tabelas que serão necessárias para auditoria, lembrando que tabelas que possuem ao menos um campos considerado SENSÍVEL/PESSOAL não podem ser desabilitadas devido a LGPD.**

1. Para habilitar a auditoria na tabela PFUNC, vamos em [P] Totvs Folha de Pagamento e pressione CTRL + F para localizar a tabela, ou se preferir busque a mesma na lista de tabelas.

   Assim que a tabela é localizada escolhemos o tipo de Auditoria que necessitamos na tabela, elas são, Update (Quando um registro é alterado na tabela), Delete (Quando um registro é excluído na tabela) e Insert (Quando um registro e inserido na tabela):

          2. Após selecionar é só clicar em salvar que as Triggers de auditoria serão criadas no banco para a tabela em questão e um log será exibido:

     3. É possível manipular quantas Triggers forem necessárias ao mesmo tempo, tanto habilitando quanto desabilitando:

   4. Para remover uma Trigger é só desmarcar todas as opções da tabela:

   5. No novo Log foi implementada a funcionalidade de Exceção.

Existem 2 tipos de exceções, uma por Tabelas/Colunas e outra de DataServer da aplicação.

A primeira (Tabelas/Colunas), não audita a tabela especifica caso somente esta coluna tenha sido alterada.  
Com a implementação da LGPD, campos considerados SENSÍVEL/PESSOAL não poderão ser excecionados, assim os mesmos não irão aparecer na lista de campos que pode ser colocados em exceção  
Mais abaixo será mostrado um exemplo de uma tabela que possui campos considerados SENSÍVEL/PESSOAL:

|  |  |
| --- | --- |
| **Produto:** | Log de Auditoria |
| **Versões:** | 12.1.27 + |
| **Ocorrência:** | Manual |
| **Ambiente:** | RM |
| **Introdução:** | Com o Log de Auditoria podemos obter um histórico de todas as inclusões, alterações e exclusões que ocorreram na(s) tabela(s) selecionada(s) para serem auditadas.  O Log de auditoria é composto por uma série de Procedures, onde quando é(são) selecionada(s) uma tabela(s) a ser(em) auditada(s), cria-se uma "**Tabela Espelho**" em um Schema exclusivo do Log de Auditoria(**TOTVSAUDIT**) e **Trigger(s)**no banco de dados, dependendo da ação escolhida (**Insert, Update, Delete**).  Quando houver transações que utilizam a(s) tabela(s) selecionada(s), a Trigger é disparada e grava na tabela de Log (**ZAUDITCHANGES**) as informações sobre o autor da ação, e os dados que foram criados, alterados ou deletados é salvo na "Tabela Espelho"  (Ex.: TOTVSAUDIT.PFUNC, tabela espelho a tabela do sistema RM.PFUNC).  Estas informações podem ser consultadas através de QUERY´s no banco de dados ou através da interface do usuário do Log de Auditoria.  Com a criação da lei do LGPD (Lei Geral de Proteção de Dados), o Log de Auditoria sofreu algumas alterações.  A partir deste momento tabelas que possuam ao menos um campo considerado SENSÍVEL/PESSOA, passará a ser auditada automaticamente caso o Log de Auditoria esteja habilitado, nesta condição o usuário não poderá desmarcar a(s) tabela(s) que possuem este tipo de dados.  Além de serem automaticamente auditadas pelo sistema, os campos que sejam considerados SENSÍVEL/PESSOAL não poderão ser excecionados.  O funcionamento do Log de Auditoria para LGPD será mostrado mais abaixo no manual. |
| **Homologação Conversões de Bases de Dados Oracle** | Caso seja necessário se restaurar uma base de dados Oracle em um ambiente de homologação, utilizando-se das ferramentas IMP e IMPDP, deve-se restaurar o Schema RM,  após o final da restauração deve-se executar a Stored Procedure p\_FixNovoLog.  **Comando:** EXEC p\_FixNovoLog  Esta nova Stored Procedure faz uma verificação e cria/recria os objetos necessários para o correto funcionamento do Novo Log de Auditoria, Schema, Tabelas, Grants, Etc. |
| **Passo a passo:** | 1. Para habilitar o Log de Auditoria vá em Serviços Globais, Administração, Log de Auditoria, Configurações: 2. Após clique no botão Inativo para que o mesmo mude para Ativo: 3. Clique em Salvar:   Com a implementação da LGPD, a partir do momento em que o Log de Auditoria é habilitado todas as tabelas que possuem ao menos um campo considerado SENSÍVEL/PESSOAL, passará a ser auditada automaticamente, e será apresentada na lista de tabelas com o fundo cinza, e sem opção de se desmarcar as ações de auditoria.  Abaixo temos o exemplo da GUSUARIO, que neste exemplo possui campos considerados SENSÍVEL/PESSOAL.   A partir do momento que o Log estiver ativo você poderá selecionar as tabelas que serão necessárias para auditoria, lembrando que tabelas que possuem ao menos um campos considerado SENSÍVEL/PESSOAL não podem ser desabilitadas devido a LGPD.   1. Para habilitar a auditoria na tabela PFUNC, vamos em [P] Totvs Folha de Pagamento e pressione CTRL + F para localizar a tabela, ou se preferir busque a mesma na lista de tabelas.  Assim que a tabela é localizada escolhemos o tipo de Auditoria que necessitamos na tabela, elas são, Update (Quando um registro é alterado na tabela), Delete (Quando um registro é excluído na tabela) e Insert (Quando um registro e inserido na tabela): 2. Após selecionar é só clicar em salvar que as Triggers de auditoria serão criadas no banco para a tabela em questão e um log será exibido: 3. E possível manipular quantas Triggers forem necessárias ao mesmo tempo, tanto habilitando quanto desabilitando: 4. Para remover uma Trigger é só desmarcar todas as opções da tabela: 5. No novo Log foi implementada a funcionalidade de Exceção.  Existem 2 tipos de exceções, uma por Tabelas/Colunas e outra de DataServer da aplicação.  A primeira (Tabelas/Colunas), não audita a tabela especifica caso somente esta coluna tenha sido alterada. Com a implementação da LGPD, campos considerados SENSÍVEL/PESSOAL não poderão ser excecionados, assim os mesmos não irão aparecer na lista de campos que pode ser colocados em exceção Mais abaixo será mostrado um exemplo de uma tabela que possui campos considerados SENSÍVEL/PESSOAL: 6. No campo domínio, digite o nome da tabela que você deseja criar a exceção de coluna: 7. E selecione as colunas que serão ignoradas, clique em Salvar e depois OK:   No exemplo abaixo onde o campo NOME da tabela PFUNC é considerado sensível, vemos que o mesmo não é apresentado na lista de colunas que podem sofre exceção: 8. Marcação de muitas colunas, pode acarretar em uma queda de performance na execução da Trigger que será montada, desta forma criamos uma validação apenas para informar o cliente: 9. Caso o cliente marque todas as colunas da tabela, neste caso entendemos que o correto é retirar a coluna da auditoria, nestes casos será mostrado a seguinte mensagem: 10. Somente poderá ser cadastrado uma exceção por Domínio, caso tentem realizar a adição duplicada será apresentado a seguinte mensagem: 11. Após o cadastro do registro, no momento da edição o campo Dominio ficará desabilitado para edição: 12. Exceção criada com sucesso, as triggers já refletirão esta nova exceção: 13. A Segunda (DataServer), ignora processos específicos do sistema, como o Recalculo da Folha.  Para adicionar uma exceção de Dataserver vá até a aba DataServers, e depois botão incluir: 14. As exceções de DataServer são globais, assim elas se aplicam a todas as tabelas que estão sendo utilizadas pelo processo e que estão sendo auditadas.  **Exemplo: Caso seja incluída uma exceção de DataServer no processo RM.Fop.CalcularFolha.FopCalcLogServer (Calculo da Folha) e a tabela PFUNC esteja sendo auditada, nenhum registro modificado pelo processo será auditado, porem caso exista uma alteração manual (realizada pelo usuário) sendo realizada ao mesmo tempo (alteração no cadastro do funcionário) a mesma será auditada normalmente.**  Inclua o código do Dataserver no campo Descrição, Salvar e depois OK:  1338px 15. Assim como nas exceções de Colunas quando o registro é salvo a exceção reflete em todas as triggers do sistema, então quanto mais tabelas auditadas, maior poderá ser o tempo para finalizar o processo: 16. Para excluir uma exceção, tanto de coluna quanto de DataServer é só selecionar a mesma e clicar no X para excluir: 17. Para desativar o Log de auditoria em todas as tabelas, é só clicar no botão ATIVO e Salvar: 18. Com isso todas as triggers serão removidas, mas irá manter a configuração que você já realizou, para caso queira reativar o Log: 19. Visualização do Log de Auditoria 20. Para visualizar selecione o registro desejado e de um duplo clique no mesmo, nesta tela teremos as informações do Usuário que gerou a auditoria. 21. Para verificar o que foi alterado vá em Detalhe das alterações do Log de Auditoria, selecione o registro e de um duplo clique. Neste exemplo vemos que os campos Apelido, Investtreinament e CodNaturalidade foram alterados. 22. Expurgo parcial é realizado quando desejamos excluir das tabelas de auditoria registros específicos. Vá em Processos, e Expurgo Parcial do Log de Auditoria 23. Nesta etapa temos que selecionar o filtro de Limpeza/Expurgo 24. Neste exemplo iremos expurgar os registros de 14/01/2018 a 15/01/2018 para operações de Update 25. Aqui selecionamos as tabelas que desejamos que seja feito o expurgo. 26. Expurgo Total Aqui iremos fazer o expurgo de todos os dados das tabelas de auditoria, esta é a forma mais rápida e pratica para quando a auditoria não é mais necessária. 27. Podemos gerar os relatórios a partir dos dados coletados pela auditoria para isso vamos em Processos, **Gerar Relatório com Base no Log de Auditoria**  Aqui teremos a tela de filtros  Definimos os filtros necessário e onde o arquivo deve ser gerado.  Selecionamos as tabelas que desejamos que o relatório seja gerado   Abaixo modelo de relatório gerado.         A partir da versão **12.1.2506.224** o relatório foi otimizado quanto ao campo **IP** e passa a exibir também a informação de **Session ID**. |
| **Observações:** | Para mais informações:    **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)  **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
