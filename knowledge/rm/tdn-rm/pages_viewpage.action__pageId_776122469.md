---
content_hash: 00eba08404901c2f39ee3b9bc8cf6884024ce368b0f3402ddd163036258170c6
fetched_at: '2026-06-29T00:11:37.003293+00:00'
page_id: '776122469'
product: rm
source: tdn-rm
title: Finalização Automática de Recursos do Projeto de Teste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776122469
version: 9
---

Após a criação deste recurso não é mais necessário inserir no seu Projeto de Teste as Atividades que finalizam processos ou deletam bases de dados restauradas por exemplo.

AO CRIAR UMA ATIVIDADE C# SE ELA IMPLEMENTAR A INTERFACE IDISPOSABLE PODERÁ FAZER USO DESTE RECURO. Neste caso por exemplo você poderá, por exemplo, subir uma API de terceiros e através do método finalizá-la ao terminar a execução do seu Projeto. Para que funcione sua classe deverá herdar a interface IDisposable e implementar o método Dispose como no exemplo abaixo.

c#Exemplo de C# com IDisposabletruetrue(this);
}
}
]]>

**Como funciona:**

Na barra de ações na tela de Edição de Projetos foi criado o botão **Finalização Automática.**

Na tela de edição de Projeto quando inserir uma Atividade note que no item Finalização Automática será acrescentado um contador. Isto quer dizer que esta Atividade (do exemplo)possui dois recursos que podem ser finalizados automaticamente.

Ao clicar no botão será aberto o widget de Recursos do Projeto.

Você pode:

* Finalizar automaticamente todos os Recursos do Projeto passíveis de finalização.
* Ignorar o resultado da finalização de todos os Recursos
* Ou não habilitar a finalização geral e finalizar somente os Recursos que necessitar.
* Ou não ignorar o resultado da finalização de todos os Recursos e ignorar somente os que necessitar.

O que significa Ignorar Resultado da Finalização?

Vamos tomar como exemplo uma Atividade que restaura uma base de dados. Caso você marque para que ela seja finalizada automaticamente ao final da execução do Projeto esta base de dados será automaticamente deletada. Se por algum motivo o TestFlow não conseguir deletá-la será levantada uma exceção. Se o Ignorar Resultado da finalização estiver habilitado:

* Então esta exceção será ignorada no cálculo do resultado da Execução do seu Projeto e o resultado será sucesso.
* Senão esta exceção será considerada no cálculo do resultado e neste caso a execução apresentará falha.

Log de execução dos Projetos

As informações da Finalização Automática dos Recursos é gravada nos detalhes da execução do Projeto e não nas Atividades.

Para visualizar clique em detalhes no log de execução.

Em seguida na árvore que será aberta clique em **mais detalhes**linha correspondente (a primeira) ao projeto.

Será aberto os detalhes da execução do Projeto e dos passos serão mostrados os logs de todas as execuções e de todas as finalizações de Recursos. A finalização será feita do último Recurso iniciado para o primeiro para evitar erros de Recursos que estão sendo utilizados por outros nodos.

Caso tenha algum dos Recurso esteja com o parâmetro para ignorar finalização habilitado e o mesmo apresente algum erro ao ser finalizado seu log será mostrado na aba ALERTAS dos detalhes da execução.

Observação: Para recursos que estão sendo utilizados por outras atividade é possível escolher se este será ou não encerrado mesmo que este parâmetro esteja habilitado para o Projeto inteiro. O mesmo vale para o parâmetro de ignorar resultado da finalização.

Os recursos utilizados por alguma Atividade no projeto tem os botões apresentados coloridos. Os recursos não utilizados serão obrigatoriamente finalizados e não poderão ter seu resultado ignorado.
