---
content_hash: 2d873f02f964eba10e3992146fedfd53a772fe690e71e0c09c4c23c795200212
fetched_at: '2026-06-29T00:11:21.122741+00:00'
page_id: '687766289'
product: rm
source: tdn-rm
title: 2.5 - Projeto de Teste
type: documentation
url: https://tdn.totvs.com/display/LRM/2.5+-+Projeto+de+Teste
version: 40
---

## O que é?

Um **Projeto** é uma atividade que agrupa outras atividades interdependentes, organizadas em uma sequência específica para automatizar testes de maneira controlada. Ele permite a execução automática de ações, avaliando condições de sucesso, falha ou alerta entre as atividades, garantindo que o teste siga um fluxo lógico.

## Para que serve?

Serve para criar uma Automação de testes estruturada e sequencial, onde atividades dependentes são organizadas para serem executadas de forma flexível. Assim, ele permite que diferentes tarefas do processo de teste se conectem de forma eficiente e que as ações subsequentes dependam do sucesso ou falha das anteriores.

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Projetos** → **Projetos de Teste.**

 2. Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Ações Rápidas de Atividade

## Ações Rápidas de Atividade

Este componente atua como uma barra lateral de ferramentas de ação rápida, projetada para facilitar a administração e edição de atividades e do Projeto de Teste. As opções disponíveis ficam habilitadas de acordo com o elemento selecionado na tela.

Aqui está o que cada item apresenta:

Adicionar Atividade 

## Adicionar Atividade

* Esta função permite adicionar uma nova atividade ao fluxo de projeto, integrando um elemento que interaja com o processo atual e facilite a expansão ou personalização do fluxo conforme necessário.

Editar Atividade

## Editar Atividade

* Ao selecionar esta opção, a Atividade será aberta e você poderá modificar as informações da atividade previamente selecionada.

Apagar Item 

## Apagar Item

* Com esta função, você poderá remover uma atividade ou um fluxo selecionado da interface. Esta ação é útil para manter o fluxo organizado, excluindo etapas desnecessárias ou obsoletas, o que ajuda a manter a interface limpa e o processo eficiente.

Propriedades

## Propriedades

Esta tela permite a edição das propriedades da atividade dentro do sistema, onde você poderá configurar parâmetros específicos da atividade selecionada de acordo com as necessidades do fluxo de trabalho.

**Elementos da tela:**

* **Ignorar Resultado**: Uma caixa de seleção que, ao ser marcada, indica que o resultado dessa atividade será ignorado no fluxo. Esse recurso pode ser útil para atividades auxiliares ou não obrigatórias, onde o resultado não afeta o fluxo geral.
* **Parâmetros JSON**: Uma área de edição que permite inserir ou modificar parâmetros em formato JSON. Esses parâmetros configuráveis fornecem um meio flexível de personalizar o comportamento da atividade, ajustando detalhes específicos diretamente no código JSON.

*Exemplo de parâmetros* JSON *para uma Atividade de inicialização de Ambientes.*

Recursos

## Recursos

Esta tela permite configurar os Recursos específicos necessários para a execução da atividade, bem como os recursos que a atividade disponibiliza para outras etapas do processo. Esses recursos são elementos essenciais que podem representar dados, conexões ou resultados de etapas anteriores, fundamentais para o andamento correto e eficiente do fluxo de trabalho.

Necessita (Recursos Consumidos)

* **Recursos consumido**s são aqueles que a atividade precisa para ser executada corretamente. Esses recursos podem ser fornecidos por outras atividades ou configurados no início do fluxo de teste.
  + **Observação:** As atividades que necessitam de recursos para serem executadas, irão buscar este recurso automaticamente no contexto do Projeto de Teste, identificando nos recursos já oferecidos pelas atividades anteriores a ela, o recurso que ela precisa. Caso tenha mais de uma Atividade que oferece o recurso que ela necessita, ela pegará automaticamente a da primeira atividade. Se for necessário utilizar um recurso diferente do primeiro da lista, este deve ser informado manualmente.

#### Oferece (Recursos Disponibilizados)

* **Recursos oferecidos** são aqueles que a atividade gera ou disponibiliza para que outras atividades utilizem posteriormente no fluxo de teste. Eles podem incluir objetos instanciados durante a execução da atividade ou dados processados que serão necessários em atividades subsequentes.

*Exemplo utilizado numa atividade [Cria Alias](https://tdn.totvs.com/display/LRM/Cria+Alias+RM?draft=true#CriaaliasRM--729033878) de um Projeto de Teste que Inicializa Ambientes do produto RM.*

Atividade Inicial

## Atividade Inicial

Define a atividade como o ponto de partida do fluxo de trabalho, estabelecendo-a como a primeira etapa a ser executada. Isso ajuda a organizar a sequência do fluxo e garante que o sistema compreenda onde o processo deve começar.

Finalização Automática

## Finalização Automática.

Após a criação deste recurso, não é mais necessário inserir no seu Projeto de Teste atividades para finalizar processos ou deletar bases de dados restauradas, por exemplo.

Todas as Atividades que disponibilizam recursos após sua execução, terão estes mesmo recursos listados nesta tela de Finalização Automática e estes serão finalizados automaticamente em ordem inversa a sua criação.

**Exemplo:** Ao criar uma **atividade em C#** que implemente a interface **IDisposable**, será possível utilizar esse recurso. Com isso, você poderá, por exemplo, iniciar uma API de terceiros e, no final da execução do seu Projeto, encerrá-la automaticamente através do método **Dispose**. Para que isso funcione, a sua classe deve herdar a interface **IDisposable** e implementar o método **Dispose**, conforme o exemplo abaixo.

c#Exemplo de C# com IDisposabletruetrue(this);
}
}
]]>

## Como funciona:

Na tela de edição de Projeto quando inserir uma Atividade note que no item Finalização Automática será acrescentado um contador. Isto quer dizer que esta Atividade (do exemplo) possui dois recursos que podem ser finalizados automaticamente.

Ao clicar no botão será aberto o widget de Recursos do Projeto.

No processo de execução do projeto, você pode configurar a finalização dos recursos de acordo com as seguintes opções:

* **Finalizar automaticamente todos os Recursos do Projeto passíveis de finalização**: Todos os recursos configurados para serem finalizados no fim da execução do projeto serão automaticamente encerrados.
* **Ignorar o resultado da finalização de todos os Recursos**: Caso habilitado, qualquer falha na finalização de um recurso será ignorada e não afetará o resultado final da execução.
* **Desativar a finalização automática e configurar recursos individualmente**: Se preferir, pode desativar a finalização automática de todos os recursos e configurar manualmente quais recursos devem ser finalizados ao término do projeto.
* **Não ignorar o resultado da finalização para todos os recursos, mas escolher recursos específicos a serem ignorados**: Nesta opção, você pode definir que falhas de finalização específicas sejam ignoradas, sem aplicar isso globalmente a todos os recursos.

O que significa Ignorar Resultado da Finalização?

Quando "Ignorar Resultado da Finalização" está ativado, falhas na finalização de um recurso não interferem no resultado final do projeto. Por exemplo:

Imagine uma **Atividade de Restauração de Base de Dados** que é automaticamente finalizada ao término do projeto. Caso a exclusão desta base falhe por algum motivo, o sistema levantará uma exceção. Se "Ignorar Resultado da Finalização" estiver habilitado, essa exceção será desconsiderada, e a execução do projeto será considerada bem-sucedida.

Caso contrário, a exceção será levada em conta no cálculo do resultado, e a execução do projeto será marcada como falha.

Para visualizar as informações da finalização automatica após a execução do projeto, clique em **mais detalhes** na linha correspondente ao projeto (a primeira).

Será aberto os detalhes da execução do Projeto e dos passos onde serão mostrados os logs de todas as execuções e de todas as finalizações de Recursos. A finalização será feita do último Recurso iniciado para o primeiro para evitar erros de Recursos que estão sendo utilizados por outros nodos.

Caso tenha algum dos Recurso que esteja com o parâmetro para ignorar finalização habilitado e o mesmo apresente algum erro, ao ser finalizado, seu log será mostrado na aba ALERTAS dos detalhes da execução.

Observação: Para recursos que estão sendo utilizados por outras atividade é possível escolher se este será ou não encerrado mesmo que este parâmetro esteja habilitado para o Projeto inteiro. O mesmo vale para o parâmetro de ignorar resultado da finalização.

Os recursos utilizados por alguma Atividade no projeto tem os botões apresentados coloridos. Os recursos não utilizados serão obrigatoriamente finalizados e não poderão ter seu resultado ignorado.

Tela Inteira 

## Tela Inteira

Expande o painel para uma visualização em modo de tela cheia, oferecendo uma visão ampla dos fluxos e atividades. Esta visualização é vantajosa para uma análise mais detalhada ou para a edição que exige maior foco e visibilidade dos elementos.

Fluxo de Execução

## Fluxo de Execução

Atividades em Fluxo 

Um **Projeto** é uma atividade que agrupa várias outras atividades, permitindo a automação de um teste de forma estruturada. Diferentemente dos agrupadores simples, as atividades dentro de um Projeto seguem uma **sequência de execução** e são interdependentes. O fluxo de execução dessas tarefas é definido com base nas condições de sucesso ou falha de suas predecessoras. Por isso, a criação do Projeto deve ser a última etapa na configuração de Automação do seu teste. Qualquer atividade disponível no **TOTVS Automação de Testes** pode ser utilizada em Projetos.

Para exemplificar o cadastro de Projetos, vamos considerar um fluxo de Automação com as seguintes atividades:

1. **Restauração de base**
2. **Cria Alias RM**
3. **Inicia RM.HOST.exe**
4. **Chamada de WebService**
5. **Comparação de Banco de Dados**

No projeto, cada atividade é representada por um **nó** (ou "nodo"). Dessa forma, cada atividade representada no Projeto pode seguir um fluxo de **sucesso**, **erro**, **alerta** ou uma combinação desses, sendo que os fluxos são exclusivos: um nó não pode, por exemplo, ter dois fluxos de sucesso ou combinar um fluxo de todos com um de erro.

*Abaixo está um exemplo de fluxo de execução de um Projeto de Teste utilizando uma chamada de WebService para um produto imobiliário no RM.*

Configuração de Fluxos entre Atividades no Projeto

## Configuração de Fluxos entre Atividades no Projeto

Para criar o fluxo no seu Projeto de Teste, selecione o tipo de fluxo que deseja estabelecer entre uma atividade e a próxima. As Atividades serão ligadas por uma seta que indica o fluxo selecionado.

### Tipos de Fluxo e Suas Representações

* **Fluxo de Sucesso (Seta Verde)**:  
  Indica que a próxima atividade será executada somente se a atividade anterior for concluída com sucesso. A seta verde representa o caminho de continuidade quando não há falhas.
* **Fluxo de Erro (Seta Vermelha)**:  
  Indica que a próxima atividade será executada apenas se a atividade anterior falhar. A seta vermelha representa o caminho de erro, garantindo que o fluxo responda a uma falha específica.
* **Todos os Fluxos (Seta Azul)**:  
  Indica que a próxima atividade será executada independentemente do resultado da atividade anterior, seja ele sucesso ou falha. A seta azul mostra um fluxo incondicional, permitindo a continuidade em qualquer situação.
* **Fluxo de Alerta (Seta Laranja)**:  
  Indica que a próxima atividade será executada com um Status de Alerta. Este fluxo é ativado quando há uma situação intermediária ou uma advertência que requer atenção, mas não interrompe o processo. A seta laranja representa esse caminho de alerta para informar que o processo prossegue, mas com observação.

Para conectar as Atividades/nodos do projeto clique na seta com a cor correspondente, arraste e solte no nodo desejado.

Exemplo prático

## Exemplo Prático

Imagine um analista de testes responsável por assegurar o correto funcionamento de um produto RM imobiliário da empresa, garantindo que os dados processados pelas APIs sejam consistentes e precisos. Esse analista deve validar o processo de cadastro de imóveis realizado via API de WebService, confirmando que os dados registrados estejam corretamente refletidos no banco de dados. Para isso, ele utilizará um projeto de testes automatizado que abrange todas as etapas essenciais da validação de dados, incluindo a restauração do banco, a configuração do ambiente e uma verificação final para garantir a consistência e integridade dos dados.

Este projeto verifica a integridade dos dados de um produto do RM imobiliário usando uma sequência de atividades. Cada etapa tem um propósito específico para garantir que os dados sejam restaurados, configurados, verificados e, finalmente, comparados. Abaixo está a descrição de cada atividade e a justificativa de sua presença no fluxo.

1. **Restauração de Banco de Dados**

* **Descrição**: Restaura uma cópia específica do banco de dados para garantir que os dados estejam em um estado conhecido e controlado antes de iniciar os testes.
* **Justificativa**: É fundamental começar com uma base limpa e padronizada para evitar interferências de dados residuais de testes anteriores. Isso garante a consistência dos resultados ao longo do fluxo de teste.

2. **Cria Alias RM**

* **Descrição**: Cria um alias para o sistema **RM**, o que configura a conexão entre o ambiente de teste e o banco de dados restaurado.
* **Justificativa**: O alias é necessário para que os serviços e o sistema **RM** possam localizar o banco de dados restaurado. Essa configuração permite que os próximos passos acessem o banco de dados correto, essencial para uma integração eficaz.

3. **Inicia RM.Host.exe**

* **Descrição**: Inicia o serviço **RM.Host.exe**, que é um processo essencial para permitir a comunicação com o WebService e garantir que o sistema esteja pronto para processar as solicitações de teste.
* **Justificativa**: Este serviço é necessário para que a chamada ao **WebService** funcione corretamente, já que ele atua como intermediário entre o sistema e o WebService. Sem ele, o sistema não consegue realizar a chamada de forma confiável.

4. **WebService Cadastro Imobiliário**

* **Descrição**: Executa uma chamada ao **WebService** responsável pelo cadastro de dados imobiliários. Essa etapa simula a interação com o sistema e a adição de dados relevantes para o teste.
* **Justificativa**: A chamada ao WebService é fundamental para verificar se o sistema responde corretamente às requisições de cadastro. Isso ajuda a validar que os dados estão sendo enviados e recebidos conforme esperado, um passo importante antes de comparar os dados.

5. **Comparação de Banco de Dados - Imobiliário**

* **Descrição**: Realiza uma comparação entre o banco de dados restaurado após a execução da automação com um resultado esperado (Mock). Isso inclui verificar se os dados foram adicionados ou atualizados conforme o esperado pelo WebService.
* **Justificativa**: Esta etapa final é crucial para garantir que as operações de cadastro funcionaram corretamente e que os dados estão consistentes. A comparação permite identificar discrepâncias, garantindo a integridade e precisão dos dados no sistema imobiliário.

**Conclusão do Fluxo**

Este fluxo de teste garante que todas as configurações e operações necessárias para a automação do cadastro e comparação de dados foram concluídas corretamente. Cada etapa desempenha um papel essencial, assegurando que o sistema funcione conforme o esperado e que os dados no banco estejam íntegros após o teste.

*Resultado do Fluxo de Atividades para a Realização do Teste*

Análise de Execuções e Logs do Projeto de Teste

## Análise de Execuções e Logs do Projeto de Teste

Esses menus são fundamentais para o sucesso e a confiabilidade de um Projeto de Teste, pois permitem que o analista acompanhe o desempenho e a precisão das atividades realizadas. A análise detalhada das execuções e o acesso aos Logs são essenciais para identificar onde o sistema está atendendo ou falhando em relação aos requisitos especificados.

Histórico de Execução

Este menu permite analisar as execuções das atividades conforme o Projeto de Teste definido, proporcionando acesso detalhado aos logs de cada atividade. Assim, é possível revisar o histórico de execuções, verificar os resultados específicos de cada etapa e identificar eventuais falhas ou oportunidades de melhoria com base nos registros gerados durante os testes.

[Clique aqui para Obter mais Informações sobre a Visualização dos Logs](https://tdn.totvs.com/pages/viewpage.action?pageId=862608096).

Status de Execução

Os status de execução do seu projeto de teste refletem o progresso e o resultado de cada etapa ou conjunto de ações realizadas durante o teste. Esses status permitem identificar rapidamente se cada teste foi concluído com sucesso, se ocorreram falhas ou se o teste ainda está em execução. Abaixo, listamos os status mais comuns que um projeto de teste pode apresentar.

Esses Status podem ser visualizados de duas formas:

* [Detalhado](https://tdn.totvs.com/display/LRM/2+-+Detalhado)**:** Com informações específicas de cada etapa do teste**.**
* [Gráficos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680234953): Uma visão geral visual do progresso e dos resultados, facilitando a análise rápida.

---

# Saiba mais

O planejamento dos [Casos de Teste](https://tdn.totvs.com/display/public/LRM/7+-+Casos+de+Teste) antes da criação do Projeto de Teste é fundamental para assegurar a eficácia e precisão do processo de testes, além de facilitar manutenções futuras.

Organize as Atividades de Forma Lógica, configurando as atividades em uma sequência lógica, garantindo que cada etapa dependa do sucesso ou falha da anterior, criando um fluxo eficiente e evitando erros desnecessários.

Escolha o Fluxo de Execução adequado Utilizando os diferentes tipos de fluxo (sucesso, erro, alerta, ou todos) para que o projeto responda adequadamente a cada situação, garantindo uma automação robusta e confiável.

Monitore os Logs de Execução e Finalização**:** Os logs mostram detalhes importantes sobre cada atividade executada e são essenciais para identificar e resolver erros ou alertas que ocorram no fluxo.

# FAQ

**P: Posso reutilizar atividades entre diferentes Projetos?**R: Sim! Aproveite atividades comuns entre Projetos para reduzir o tempo de criação e manter a consistência entre testes. Versione e documente bem essas atividades para que possam ser reutilizadas com facilidade e segurança

**P: Como escolher o tipo de fluxo certo entre atividades (Sucesso, Erro, Alerta, Todos)?**

R: Escolha o fluxo de acordo com o comportamento esperado após cada atividade

**Sucesso:** Use quando a próxima atividade depende do êxito da anterior. **Erro:** Configure para tratar falhas específicas. **Alerta:** Para situações intermediárias que não exigem interrupção, mas precisam de atenção. **Todos:** Para atividades que precisam ocorrer independentemente do resultado da anterior.

**P: Qual é a melhor maneira de gerenciar erros durante a execução de um Projeto?**

R**:** Utilize o fluxo de erro (seta vermelha) para definir o caminho a ser seguido caso uma atividade falhe. Isso permite executar ações específicas para lidar com falhas, como realizar uma limpeza do ambiente ou enviar notificações. Além disso, os logs ajudam a identificar pontos problemáticos para aprimorar o fluxo no futuro.
