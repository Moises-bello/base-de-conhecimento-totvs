---
article_id: 360028854992
category: PMS - Integrações
content_hash: 6c15fcc82034da03ef48022115e18c0505f050f5215d327bfdff0385d4685dbf
fetched_at: '2026-06-28T22:37:16.719839+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerenciamento de Projetos:
  Integração com o MS Project'
type: support-article
updated_at: '2026-04-28T21:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028854992-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerenciamento-de-Projetos-Integra%C3%A7%C3%A3o-com-o-MS-Project
---

**Dúvida**  
Quais são os dados que o Microsoft Project importa e exporta na integração com o módulo Gestão de Projetos?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões  
  
**Solução**  
**Veja nosso vídeo How To sobre o assunto:** [How To | MP - SIGAPMS - Integração PMS x MS Project](https://www.youtube.com/watch?v=4zYe2BKW0XE)  
  
O MS Project é uma ferramenta de administração de projetos da Microsoft, que possui uma interface gráfica muito amigável para a visualização e montagem de projetos.

Essa interface pode ser utilizada para manter os projetos do ambiente de gestão de projetos, integrando assim todos os recursos do Protheus para o gerenciamento da execução.

A integração acontece em dois níveis :

**• Exportação**  
É possível abrir um projeto do ambiente de gestão de projetos no MS Project para ele ser visualizado e gravado neste aplicativo.

**• Sincronização**  
É possível abrir um projeto do ambiente de gestão de projetos no MS Project e manipulá-lo, atualizando a informação no ambiente de gestão de projetos, depois de manipulado, podendo, desse jeito, utilizar a interface do MS Project para montar e manipular partes da estrutura do projeto, sem perder a integração com o módulos do ERP, como seria se fosse utilizado só o MS Project;

Opção Exportar da rotina **PMSC010**:

![exportar_project.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360030256992)

A opção "Exportar" realiza a leitura de dados, exportando de determinado projeto para o MS Project, as seguintes informações:

* Calendários (Opcional);
* Recursos (Opcional);
* Estrutura completa do projeto, considerando os direitos de usuários (tarefas, EDTs, códigos, etc.);
* Relacionamentos (Opcional);
* Datas previstas para execução;
* Recursos alocados nas tarefas (Opcional);
* Percentual de execução física das tarefas na database (Opcional).

Para exportar o projeto é necessário informar o idioma da versão do Project com a que será feita a integração (isto é necessário para interpretar algumas siglas no idioma correto).

O sistema abre o MS Project com o projeto, posicionado em um novo arquivo com o formato padrão para os novos arquivos que estiverem configurados para o MS Project.

Para utilizar um arquivo padrão diferenciado (com outras configurações, como por exemplo, posicionamento de colunas diferente), deve-se informar o nome do arquivo desejado, na pergunta **Projeto Modelo?** apresentada na janela de parâmetros do sistema.

Nesta janela também estão disponíveis as seguintes opções para exportação do cadastro de recursos do Sistema:

* Planilha de Recursos
* Recursos Alocados
* Relacionamentos
* Progresso Físico.

Nesta janela de parâmetros existe outra opção de exportação que define se os recursos alocados em cada tarefa serão exportados com a tarefa em questão.

Depois de confirmadas as opções é aberto um arquivo no MS Project com os dados do projeto posicionado.

Antes de finalizar, caso seja necessário, grave o arquivo, pois está operação não será permitida após a finalização. Para finalizar a integração com o **MS Project**, clique em sair.

Os dados importados pelo MS Project são:

* Estrutura completa do projeto (tarefas, EDTs, códigos, etc.);
* Relacionamentos (Opcional);
* Datas previstas para execução;
* Recursos alocados nas tarefas;
* Percentual de execução física das tarefas na database.

**IMPORTANTE:** Antes de fazer a sincronização, deve ser verificado o formato de data utilizado no MS Project na aba (Opções). **O formato deve ser : “dd/mm/aa hh:mm”.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40083398446871)  
  
Para fazer a sincronização devem ser seguidos os mesmos passos do processo de exportação, a diferença é que a tela de **Assistente de Integração** é exibida depois da abertura do projeto no MS Project.

Com o projeto aberto no MS Project, devem ser feitas as modificações desejadas e quando finalizada a atualização deve-se selecionar a opção **Importar**. Todos os dados do projeto, se editados no MS Project, serão importados para o projeto no **PMS**.

Acessando a opção de **Visualizar** há a possibilidade de ver a estrutura atual do projeto; utilize esta opção após a opção **Importar** para verificar se os dados foram importados de acordo com as modificações feitas.

Para finalizar a integração deve-se selecionar a opção **Sair**, que fecha o Ms Project e volta para a tela de projetos.

**Importante:**Para importar um projeto para o PMS, crie um projeto vazio, chame a integração com o Project.
