---
content_hash: 116ce14d84f26668caf5ee1d401dd25c77fce15354facc884b8d0c173946712d
fetched_at: '2026-06-28T21:35:28.278771+00:00'
page_id: '644018092'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Central de Diagnósticos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=644018092
version: 44
---

# Falando de central de diagnósticos...

---

O objetivo da central de diagnósticos é possibilitar aos clientes um lugar único para que seja possível visualizar e validar processos e solicitações que estejam com alguma inconsistência, ou seja, é necessário que a *solicitação ou processo criado contenham algum erro em sua movimentação* ou que os *processos apresentem alertas de práticas não recomendadas de desenvolvimento.*

Além disso, a central de diagnósticos também extrai os dados dos workflows do Fluig, permitindo que essas informações sejam facilmente visualizadas e ainda podendo ser enviadas para os times de atendimento, consultoria e desenvolvimento.

1Central de DiagnósticosCentral de Diagnósticos na práticaslide

1000800

## Acessando a central de diagnósticos

---

**01**. Navegue até o nível de menu **Processos > Central de diagnósticos**.

## Estatísticas gerais

---

Na seção Estatísticas gerais é possível verificar a quantidade de solicitações e processos com algum tipo de erro ou alerta.

#f2f2f2#f2f2f2

Para consultar o total de solicitações e processos com erro, utilize a seta no canto superior direito da tela para navegar entre os dias, deslizando para a esquerda ou para a direita . É possível visualizar dados de dias anteriores ou retornar ao dia atual. Também é possível aplicar um filtro clicando na seta ao lado da data e selecionando outros períodos que deseja consultar.

**01**. Clique na seta, localizada ao lado da data atual e selecione uma das opções disponíveis.

#f2f2f2#f2f2f2

**Hoje**: mostra o total de solicitações e processos com erro ou alerta no dia atual.

**Últimos 7 dias**: mostra o total de solicitações e processos com erro ou alerta nos últimos 7 dias.

**Últimos 15 dias**: mostra o total de solicitações e processos com erro ou alerta nos últimos 15 dias.

**Últimos 30 dias**: mostra o total de solicitações e processos com erro ou alerta nos últimos 30 dias.

**Período personalizado**: Permite incluir um período de tempo para que seja exibido o total de solicitações e processos com erro ou alerta, após incluir o período, clique em **Aplicar.**

## Visualizar log diário do ambiente

---

Nesta opção, é possível visualizar o log diário do ambiente, com recursos para aplicar filtros, realizar buscas e selecionar o tipo de log que deseja consultar.

**01**. Clique no botão **Visualizar log diário do ambiente**.

**02**. Utilize o campo de busca, localizado no canto superior esquerdo para buscar palavras ou termos específicos.

**03**. Em **Filtros do log**, é possível definir algumas informações para que a busca se torne mais prática e assertiva.

#f2f2f2#f2f2f2

**Período personalizado**

Permite definir um intervalo de tempo, em horas, para exibir apenas o trecho do log correspondente ao período selecionado. Defina o período desejado nos campo A partir de: e Até:.

**Tipo de log**

Permite selecionar quais tipos de log que devem ser exibidos entre:

* Error
* Warm
* Info
* Debug

**04.** Após definir todas as informações para o filtro, clique em **Aplicar**.

#f2f2f2#f2f2f2

Para remover os filtros aplicados, clique em **Limpar filtros**, no canto superior direito da tela.

## Solicitações

---

Na aba **Solicitações**, são exibidas todas as solicitações que estão em estado de erro. É possível aplicar filtros por tipo de solicitação e visualizar o diagnóstico detalhado de cada caso. A listagem apresenta informações como número da solicitação, processo, versão, responsável, data do erro, atividade e diagnóstico.

**01**. No **Filtro**, localizado ao lado do campo de busca é possível filtrar: **Por solicitação**, **Por processo**, **Por responsável**, **Por atividade** ou **Por erro**.

**02**. Em Mostrar "x" resultados, localizado na parte inferior direita, é possível definir a quantidade de solicitações que aparecerão na listagem em 10, 25, 50 ou 100 solicitações por página.

**03**. Para visualizar o diagnóstico da solicitação, clique no ícone .

**04**. Uma nova tela será exibida, mostrando algumas informações do diagnóstico da solicitação, como número da solicitação, o processo ao qual ela pertence, versão, data de erro e atividade. Para ver mais detalhes, clique em **Ver detalhes e ações**.

**05**. Na página de **Diagnóstico da solicitação**, é possível visualizar informações gerais como a **Mensagem de erro**, **Log da solicitação**, **Ações** e **Acessar a central de atendimento**.

**06**. Na seção **Mensagem de erro**, é possível ter uma breve descrição do tipo de erro.

**07**. Na seção **log da solicitação**, é possível copiá-lo para a área de transferência clicando no ícone  ou ainda expandir para visualizar em tamanho maior, clicando no ícone .

**08**. Ao clicar em **Visualizar solicitação,** o usuário será direcionado diretamente para dentro da solicitação na [central de tarefas](https://tdn.totvs.com/x/AfDuDQ).

**09**. No botão **Ações**, é possível realizar movimentações relacionadas à solicitação e ao processo.

#f2f2f2#f2f2f2

Da solicitação:

**Reenviar solicitação** - permite reenviar novamente a solicitação.

**Gerar log descritivo** - gera um log descritivo da solicitação para que seja reexecutada. 

#000000#f2f2f2

Ao escolher esta opção, clique em **Continuar** para que a solicitação seja reexecutada.

**Download da solicitação** - permite fazer o download da solicitação.

#000000#f2f2f2

Ao fazer o download da solicitação, os dados relacionados ao processo como formulários, logs e anexos poderão ser incluídos no arquivo de exportação.

Para dar continuidade na solicitação, será necessário selecionar se deseja exportar seus anexos ou anonimizar seus campos do formulário.

Para isso, basta clique nas opções que deseja para deixá-las em verde.

É necessário também marcar a opção de que está ciente e de acordo sobre os dados que serão expostos para o arquivo de download, referentes a solicitação em questão.

Após feito todos os passos, clique em **Realizar download**.

Um arquivo **.zip** do download será gerado com todas as informações da solicitação.

Do processo:

**Diagnóstico do processo** - ao escolher esta opção, uma nova janela será aberta, permitindo verificar o diagnóstico do processo. Mostrando ainda seus alertas de desenvolvimento, sua mensagem de alerta e o script.

#000000#f2f2f2

Caso deseje copiar o script para a área de transferência, clique no ícone .

**Editar scripts** - ao escolher esta opção, uma nova janela será aberta, direcionando para o editor de script. Permitindo assim a visualização e edição dos scripts do processo.

#000000#f2f2f2

As edições feitas nos scripts do processo geram uma nova versão que é aplicada apenas à solicitação específica. Se o erro diagnosticado for corrigido com essa edição, a nova versão do script poderá ser atualizada para todas as solicitações futuras do processo. Todas as versões podem ser consultadas e restauradas por meio do gerenciador de versões.

Para editar, basta clique na área de edição em **Editar**. 

Para visualizar versões anteriores e gerenciá-las, clique em **Versões**. 

Na **Lista de script do processo**, é possível visualizar todos os scripts contidos no processo e selecionar um a um para edição.

Para copiar o script desejado, clique no ícone .

Após finalizada as verificações e edição, clique em **Reenviar solicitação**.

**10**. É possível ainda chamar o suporte diretamente de dentro da central de diagnósticos. Clique no botão **Acessar Central de Atendimento** e será feito o direcionamento para o suporte do TOTVS Fluig.

## Processos

---

Na aba **Processos**, é possível visualizar todos os processos em estado de erro ou alerta. É possível filtrar os processos pelo status e realizar buscas pelo código ou pela descrição. A lista exibe informações como código, nome do processo, versão, status de ativo, indicação de edição e diagnóstico.

**01**. No filtro, **Por Processos**, localizado ao lado direito do campo de busca, podemos filtrar **Processos com erro**, **Processos com alerta**, **Processos ativos**, **Processos inativos**, **Processos liberados**, **Processos em edição**, **Todas as versões** e **Últimas versões**.

**02**. Em Mostrar "x" resultados, localizado na parte inferior direita, é possível definir a quantidade de solicitações que aparecerão na listagem em 10, 25, 50 ou 100 solicitações por página.

**03**. Para visualizar o diagnóstico do processo, clique no ícone .

**04**. Uma nova página será exibida. Em **Diagnóstico do processo**, é possível visualizar as abas de **Alertas de desenvolvimento** e **Erros em solicitações.**

#f2f2f2#f2f2f2

Aba **Alertas de desenvolvimento**:

Contém informações de mensagem de alerta e script.

Aba **Erros em solicitações**:

Contém informações da mensagem de erro e demais informações da solicitação com erro.

Para visualizar a solicitação, clique no ícone  para ser direcionado diretamente para o diagnóstico da solicitação.

## Práticas não recomendadas de desenvolvimento

---

A seguir estão listadas as práticas de desenvolvimento que classificamos na Central de Diagnóstico como não recomendadas:

* **Ao utilizar um mecanismo por usuário ou executor da atividade, é recomendável que se tenha um gestor no processo caso o usuário em questão seja desativado:**

#f2f2f2#f2f2f2

Quando uma atividade está configurado com um mecanismo por usuário, caso este usuário seja desativado, ao movimentar a solicitação, a solicitação é movimentada para o gestor do processo. Mas, caso não haja um gestor, ocorrerá um erro. O mesmo acontece ao utilizar um mecanismo por executor da atividade e este executor seja desativado. Por isso é recomendável configurar um gestor nestes casos.

Link: 

Imagem:

* **A propriedade AutomaticTasks está descontinuada desde a versão 1.5.9 e pode parar de funcionar sem avisos:**

#f2f2f2#f2f2f2

Esta propriedade não deve ser mais utilizada pois foi descontinuada. Para evitar problemas em futuras atualizações do fluig a propriedade deve ser removida bem como ajustado o processo para não fazer uso dela.

* **Este é um processo padrão do fluig e somente é atualizado a primeira versão. Ao criar uma nova versão, as atualizações do produto não terão efeitos sobre este processo:**

#f2f2f2#f2f2f2

Frequentemente em nossas atualizações fazemos pequenos ajustes, correções e melhorias no processo de listar tarefas e no subprocesso adhoc. Porém, aplicamos somente na versão 1. Ao fazer modificações nesse processo você não recebe nossas modificações.

* **A atividade condicional possui um timer com menos de 3 minutos o que pode, em caso de falhas, acumular várias solicitações rodando ao mesmo tempo e em um curto período de tempo:**

#f2f2f2#f2f2f2

Ao criar uma atividade condicional, o fluig vai executar o script conforme configurado. Caso não consiga a resposta desejada, é agendado uma re-execução. NO caso de uma integração que apresente instabilidade ou mesmo em alguma outra falha no código, esses agendamentos podem acabar se acumulando conforme aumenta o número de solicitações o que pode levar à uma massa de agendamentos excessivamente grande causando lentidão no fluig como um todo.

* **A atividade de serviço possui um timer de 1 minuto com mais de 7 tentativas o que pode, em caso de falhas, acumular várias solicitações rodando ao mesmo tempo e em um curto período de tempo:**

#f2f2f2#f2f2f2

Ao criar uma atividade condicional, o fluig vai executar o script conforme configurado. Caso não consiga a resposta desejada, é agendado uma re-execução. NO caso de uma integração que apresente instabilidade ou mesmo em alguma outra falha no código, esses agendamentos podem acabar se acumulando dependendo da quantidade de solicitações abertas por minuto, o que pode levar à uma massa de agendamentos excessivamente grande causando lentidão no fluig como um todo.

* **O script de customização está usando as conexões internas do fluig com o banco de dados. Utilize a conexão /jdbc/AppDS**

#f2f2f2#f2f2f2

O Fluig disponibiliza a conexão AppDS que deve ser utilizada pelas customizações no lugar do FluigDS e FluigDSRO.

Link: 

* **Os arquivos de tradução estão referenciando uma atividade que não existe:**

#f2f2f2#f2f2f2

Nos arquivos de tradução, constam atividades que não existes na diagramação. Isso acontece quando uma atividade foi removida normalmente. Para evitar confusões futuras, é recomendável remover essas traduções de atividades que não existem mais

* **A propriedade da atividade está diferente do que encontrado nos arquivos de tradução:**

#f2f2f2#f2f2f2

Ao configurar um processo e gerar as traduções, o fluig ignora as propriedades da atividade e utiliza conforme configurado na tradução. Por isso gerar confusão no desenvolvedor, recomenda-se que em ao menos um idioma esteja igual a configuração que foi feita na atividade ou que escolha um idioma e remova um dos arquivos de tradução desse idioma, assim, ao tentar movimentar a solicitação neste idioma que foi removido, vai utilizar os dados conforme configurado na tela.

* **A propriedade do processo está diferente do que encontrado nos arquivos de tradução:**

#f2f2f2#f2f2f2

Ao configurar um processo e gerar as traduções, o fluig ignora as propriedades do processo e utiliza conforme configurado na tradução. Por isso gerar confusão no desenvolvedor, recomenda-se que em ao menos um idioma esteja igual a configuração que foi feito no diagrama ou que escolha um idioma e remova um dos arquivos de tradução desse idioma, assim, ao tentar movimentar a solicitação neste idioma que foi removido, vai utilizar os dados conforme configurado na tela.

* **O script de customização está levantando um erro em um método que não vai parar a transação e não vai impedir a movimentação da solicitação:**

#f2f2f2#f2f2f2

Levantar uma exceção no script, além de interromper a execução do script em si consegue impedir a movimentação toda da solicitação. Porém, nem todos os métodos possuem essa característica, já que as informações já foram persistidas no ponto em que o script é executado. Confira a documentação para saber quais são estes métodos.

Link: 

* **O script de customização está conectando a um serviço durante a movimentação o que pode gerar lentidão na movimentação. Utilize a atividade de serviço:**

#f2f2f2#f2f2f2

O Fluig possui a atividade de serviço que deve ser utilizada para realizar integrações com outros serviços de terceiros ou mesmo do próprio fluig. Como vantagem, ele oferece re-tentativas automáticas ou mesmo um fluxo de contorno para eventuais problemas de conexões ou dados. Utilizar em outro ponto do produto pode gerar lentidão na movimentação de processos. Mais sobre a atividade de serviço:

Link: 

Imagem:

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
