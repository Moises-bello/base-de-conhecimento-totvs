---
content_hash: b43f4eb850dd207297b7b85d9dafb149ea2533a2b054a7b3ec5d970bb98ece34
fetched_at: '2026-06-28T21:35:31.816008+00:00'
page_id: '979805603'
product: fluig
source: tdn-fluig
title: Atualizações (2.0)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979805603
version: 398
---

75%

## Ciclo de atualização

Maior destaque para as atualizações evolutivas (**Update**). 

As liberações mais relevantes são identificadas por um selo especial:

 **Essential:** incluem correções e pequenas evoluções da plataforma.

 **Mandatory:**atualizações que possuem correções críticas emergenciais.

Veja todos os detalhes em: [Atualização da plataforma](https://tdn.totvs.com/x/2xVbB).

25%

trueIdioma

Saiba de todas as novidades do [My Fluig](https://tdn.totvs.com/x/B1y2Fg).

oculto

## 260630

## 30 de Junho de 2026

---

## Melhorias

## 260630

## 30 de Junho de 2026

---

## Correções

FGDN-1318

* Realizado ajuste para que os documentos em check-out possam ser editados normalmente.

---

***[ Ainda sem data de liberação ]***

**Épico**: <https://jiraproducao.totvs.com.br/browse/FCRF-1040>

### Atalho de componentes: uma forma mais dinâmica de modelar diagramas de processos!

Quer ganhar **agilidade** na modelagem e manter seu fluxo sempre organizado, sem precisar ir até a barra de componentes a todo momento? O **Atalho de componentes** veio para transformar sua experiência!

Agora, ao clicar em um componente do diagrama, você pode adicionar **rapidamente** o próximo passo do processo. E o melhor: a **conexão** entre os componentes já é criada automaticamente, **reduzindo** o tempo de construção e mantendo seu raciocínio **fluindo** sem interrupções.

Com esse atalho, é possível modelar processos de forma mais **natural**, **visual** e **contínua**, explorando possibilidades diretamente no contexto do diagrama, seja para criar novos caminhos, testar alternativas ou detalhar fluxos complexos, com tudo acontecendo de maneira mais fluída e produtiva.

Além disso, ao **criar** um processo, o evento **Início** já vem posicionado na área de modelagem do diagrama, agilizando o ponto de partida do processo.

Assim, você deixa de depender de ações repetitivas e ganha mais foco no que realmente importa: modelar processos **eficientes** e **alinhados** ao seu negócio. Experimente o atalho de componentes e leve sua modelagem a um novo nível de agilidade!

**Épico**: <https://jiraproducao.totvs.com.br/browse/FCRF-1071>

### Evento Finalizado: o encerramento global do processo

Precisa encerrar um processo inteiro de forma **imediata** e sem deixar pontas soltas? O evento **Finalizado** faz exatamente isso.

Com ele, quando o processo atinge esse ponto no fluxo, **todos os caminhos** paralelos e ativos são encerrados automaticamente, incluindo **atividades** pendentes e até **subprocessos** vinculados. É o **fim global** do processo, sem necessidade de aguardar outras ramificações.

Esse evento é ideal para cenários como **cancelamentos** por parte do solicitante, **inconsistências** críticas ou **decisões** que tornam os demais caminhos irrelevantes. Em vez de gerenciar múltiplos encerramentos, você resolve tudo com uma **única ação** no fluxo.

Diferente do evento Fim, que encerra **apenas** o caminho percorrido, o Finalizado garante o encerramento **completo** e imediato do processo, trazendo mais controle, simplicidade e segurança para suas automações.

Dica!

e obtenha mais detalhes sobre esse evento.

**Épico**: <https://jiraproducao.totvs.com.br/browse/FCRF-1078>

### Processos do Fluig Studio completos do Editor de processo!

Exportou um processo do Fluig Studio e sentiu falta de algum componente no Editor de processo? Calma, isso já ficou no passado!

Agora, os **componentes** que foram utilizados em processos exportados do **Fluig Studio** e que ainda não estão disponíveis na paleta de componentes do Editor de processo são **exibidos** corretamente no diagrama, sem deixar lacunas.

Com isso, você ganha uma **visão** muito mais fiel e **completa** do processo original, facilitando o entendimento e a análise da estrutura do fluxo. Além disso, a **compatibilidade** entre o que está sendo visto e o que está sendo executado ao longo do processo fica mais **evidente**.

Confira abaixo todos os  e  que agora estão disponíveis para visualização no Editor de processo.

Importante!

No momento, esses componentes estão disponíveis apenas para visualização no diagrama dos processos exportados, não sendo possível editá-los, apenas movê-los ou excluí-los. A exclusão pode ser desfeita, mas criar outro componente igual não é possível.

#ebecf025%

trueGreyTemporizador (evento inicial)

25%

trueIntermediário

25%

truecaptura de erro (evento final)

25%

trueAtividade de envio

25%

truesinal (evento inicial)

25%

trueSinal (evento intermediário de recebimento)

25%

trueSinal (evento final)

25%

trueAtividade manual

25%

truemúltiplo (evento inicial)

25%

trueSinal (evento intermediário de envio)

25%

trueMúltiplo (evento final)

25%

trueAtividade de usuário

25%

trueCondicional (evento inicial)

25%

trueMúltiplo (evento intermediário)

25%

truedocumento

25%

trueAtividade de negócio

25%25%

trueCondicional (evento intermediário)

25%

truedatabase

25%

trueAtividade de script

25%25%25%25%

trueAtividade ad-hoc

## 260623

## 23 de Junho de 2026

---

## Melhorias

### Nova ordenação para destacar regras de anexo recentemente alteradas

Agora, ao [editar](https://tdn.totvs.com/pages/viewpage.action?pageId=862123505#Plataforma%E2%9D%99Atividade-Editarregraparaanexos) uma regra de anexo configurada em uma atividade, ela passa a ser **exibida** no **topo** da listagem de regras. Ou seja, a ordem de exibição das regras é alterada, elas são exibidas em ordem de edição e depois de criação, da mais recente para a mais antiga.

Dessa forma, você ganha **rapidez** para localizar e revisar as regras recentemente modificadas, facilitando a **gestão** de regras ativas, garantindo que as regras mais relevantes sejam facilmente **acessíveis**, reduzindo o risco de erros ao destacar as alterações mais **recentes** e reforçando a qualidade da gestão de anexos dentro do processo. Tudo isso para aumentar a eficiência operacional do seu negócio!

## Correções

* Realizada correção no modo Quadro da Central de Tarefas para garantir que, ao tentar movimentar solicitações que possuam validações impeditivas, seja exibida corretamente a mensagem de alerta informando sobre o bloqueio.
* Corrigida a busca do recurso *Datasets* para exibir corretamente os resultados quando o recurso é acessado a partir do Painel de controle e é utilizado o banco de dados Oracle.
* Corrigida a inconsistência na contagem de visualizações de artigos.
* Realizada correção para sanar inconsistências em formulários pós atualização.

## 260616

## 16 de Junho de 2026

---

## Correções

* Realizada correção para sanar falha na publicação de posts com múltiplas imagens anexadas.
* Realizada correção para que as variáveis de visualização sejam atualizadas em todas as formas de acesso.
* Correções de segurança aplicadas para reforçar a robustez e a integridade da plataforma.
* Corrigida a atualização dos filtros da Central de Tarefas ao iniciar uma nova solicitação.

## 260609

## 09 de Junho de 2026

---

## Melhorias

### Componentes avançados na criação de processos com IA

A criação de processos com Inteligência Artificial (IA) foi **ampliada** para oferecer mais flexibilidade e suporte na modelagem de fluxos de processos. Agora, além dos componentes já disponíveis, a IA também é capaz de criar processos utilizando:

* + *gateway* **Exclusivo**;
  + **Temporizador**;
  + **Subprocesso**.

Com essa evolução, é possível descrever processos mais **complexos** em linguagem natural e contar com o apoio da IA para estruturar fluxos que envolvam **tomadas de decisão** com condições e desvios de fluxo, **controles de prazo**, espera e execuções baseadas em tempo e **agrupamento de atividades** com estruturas mais modulares e reutilizáveis.

A novidade amplia a capacidade da IA na modelagem de processos, apoiando cenários ainda mais sofisticados, ajudando você a criar processos mais **completos**, organizados e eficientes, reduzindo o esforço manual e **acelerando** a construção de fluxos mais aderente às necessidades de negócio.

### Mais transparência e flexibilidade na gestão de *scripts* de processos

Gerencie os *scripts* de processos de forma mais simples, organizada e transparente! Agora, na aba ***Scripts***, os *scripts* possuem um identificador de origem:

* + **Edição por desenvolvimento**: indica que o *script* foi criado na própria aba ***Script*** ou por ferramentas de desenvolvimento;

* + **Edição pela interface**: indica que o *script* foi criado automaticamente a partir das configurações de uma **atividade de serviço** existente no diagrama do processo.

Além disso, os *scripts* gerados automaticamente a partir da atividade de serviço podem ser convertidos para **edição avançada**, oferecendo mais liberdade para personalizações e adequações a cenários específicos de negócio. Ao habilitar a edição avançada, o *script* passa a ser gerenciado diretamente pela aba ***Scripts***, centralizando sua edição em um único local.

Dessa forma, você ganha mais clareza sobre a origem dos *scripts*, mais autonomia para personalizações e uma experiência mais consistente na manutenção de cada tipo de implementação.

Importante!

*Scripts* de atividades de serviço que já existem receberam o identificador **Edição por desenvolvimento** e já possuem a edição avançada habilitada. Apenas *scripts* de atividades de serviço configuradas a partir de agora receberão o identificar **Edição pela interface**.

Dica!

Obtenha mais detalhes sobre a gestão de *scripts* em *Scripts* do processo e .

### Gerencie permissões de APIs com mais facilidade

Gerenciar permissões ficou mais simples e rápido.

Agora, as permissões das APIs de Grupos podem ser atribuídas de forma muito mais prática, sem a necessidade de percorrer longas listas de APIs para configurar acessos individualmente.

### Permissões organizadas por ação

Antes, a atribuição de permissões exigia a configuração individual de cada API, tornando o processo mais trabalhoso e sujeito a erros.

Agora, na tela de **Permissões** do **Painel de Controle**, o agrupador **Pessoas **→**** **Grupos **→**** **Recurso que permite gerenciar APIs de Grupos**, centraliza o gerenciamento das APIs de Grupos. Ao configurar a permissão para uma ação, como Criar, Alterar ou Excluir, a plataforma realiza automaticamente todas as configurações necessárias relacionadas a ela.

Com isso, o gerenciamento de acessos se torna mais ágil, intuitivo e eficiente.

Essa facilidade também já está disponível para as APIs de **Papéis**.

RedAtenção!

Se sua organização possui permissões atribuídas à API de Grupos configuradas no modelo anterior, **é obrigatório realizar a reconfiguração dessas permissões após a atualização**.

A não realização dessa etapa pode causar impactos no funcionamento de recursos que dependem dessas permissões, incluindo a **interrupção** de integrações e processos automatizados.

**💡**Antes de concluir a atualização, verifique:

* Quais usuários e grupos possuem permissões relacionadas à API de Grupos;
* Se todas as permissões foram reconfiguradas no novo modelo;
* Se as integrações e processos dependentes foram validados após a alteração.

### O que vem por aí?

Simplificar tarefas e gerar mais eficiência no dia a dia continua sendo um dos nossos compromissos.

Por isso, já estamos trabalhando para levar esse mesmo conceito de agrupamento para outros recursos da plataforma em futuras atualizações.

Saiba mais!

Acesse a documentação [Plataforma | Recursos de permissão em APIs, datasets e webservices](https://tdn.totvs.com/x/pB2eI).

## Correções

* Correção no envio de anexos em formulários em que ocorria o travamento da interface ao enviar a solicitação.
* Correção da exibição indevida da mensagem de validação, garantindo o processamento correto de números decimais quando não há regras restritivas configuradas.
* Corrigida a exibição da data de atividades paralelas de uma solicitação.
* Realizada correção na funcionalidade de renomear documentos.
* Corrigido o comportamento do assistente.
* Ajustes realizados para garantir a movimentação de solicitações em processos que utilizam formulários configurados com armazenamento em tabela única.

## 260602

## 02 de Junho de 2026

---

## Melhorias

### Campos avançados e IA: a combinação ideal para evoluir seus formulários!

A criação de formulários com Inteligência Artificial (IA) evoluiu para tornar sua experiência ainda mais completa. Agora, além de criar, você também pode [complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=915177100#Plataforma%E2%9D%99Editordeformul%C3%A1rio-Complementarformul%C3%A1riocomFluigIA) formulários existentes com componentes mais **avançados**, permitindo construir formulários mais organizados, ricos em informações e alinhados a cenários mais **complexos** do negócio.

Os **novos campos** disponíveis para utilização com IA são:

* + **Múltipla escolha**;
  + **Avaliação**;
  + **Tabela**;
  + **Painel**;
  + **Abas**.

Dessa forma, basta descrever o que você precisa de **forma natural** e deixar que a IA ajude na **evolução** do formulário, adicionando estruturas mais sofisticadas sem precisar configurar tudo manualmente. O resultado é mais **produtividade**, menos esforço operacional e muito mais **agilidade** na construção das soluções!

E para trazer ainda mais segurança, também é possível **pré-visualizar** o formulário após a criação ou a complementação feita pela IA. Assim, você consegue **validar** rapidamente a estrutura gerada, **conferir** a experiência de preenchimento e **garantir** que o resultado esteja conforme o esperado antes de alterar o formulário efetivamente.

Com essa evolução, a IA deixa de apoiar apenas em formulários simples e passa a contribuir também na construção de **experiências mais completas**, organizadas e profissionais. Experimente o novo recurso e crie formulários mais aderentes ao seu negócio!

## Correções

* Realizada correção para que o campo `IDENTIFIER` seja populado corretamente em processos com formulários criados no Novo Editor, garantindo a exibição correta dos metadados e a identificação da solicitação na Central de tarefas.
* Realizada correção para que a classe processDefinition trate corretamente o atributo setBpmnVersion ao receber valores nulos, eliminando a inconsistência na abertura dos editores clássicos e garantindo a transição do novo editor para os editores clássicos.
* Realizada correção para que seja possível realizar login via SSO corretamente.
* Realizada correção para que o layout do menu lateral renderize corretamente não sobrepondo o conteúdo principal das páginas.
* Corrigido o componente  para permitir salvar as configurações corretamente ao definir condições que utilizam os operadores lógicos || e &&.
* Correção realizada para que o endpoint da API valide e trate corretamente os parâmetros recebidos nas requisições, garantindo a integridade dos dados armazenados e prevenindo a execução de scripts indesejados.
* Correção realizada para que as regras de obrigatoriedade dos campos sejam respeitadas em todas as etapas do processo, mesmo quando localizados em abas diferentes do formulário.
* Correção realizada para que, ao utilizar regras de formulário com múltiplos eventos configurados, todos os eventos sejam validados corretamente durante a execução.
* Realizada correção para que seja possível criar um serviço no Eclipse utilizando o plugin do Fluig.
* Realizada correção para sanar inconsistências relacionadas a widget de processos.

## 260526

## 26 de Maio de 2026

---

## Melhorias

### Mensagens mais claras e intuitivas na publicação de processos

Aprimoramos a forma como as [inconsistências](https://tdn.totvs.com/pages/viewpage.action?pageId=860245005#Plataforma%E2%9D%99Editordeprocesso-erros) são exibidas ao publicar um processo. Agora, as **mensagens** que informam as inconsistências existente no diagrama são mais **claras**, **objetivas** e com **instruções fáceis** de entender. Além disso, elas estão mais **organizadas** e **agrupadas** por tipo de componente, como atividade, evento de início, *gateway*, subprocesso, dentre outros.

Com isso, fica mais fácil **identificar**, **entender** e **corrigir** as inconsistências antes da publicação, tornando a modelagem mais ágil, evitando o retrabalho, reduzindo a frustração e aumentando a qualidade dos processos publicados. Muito bacana, não é mesmo?

## Correções

* Correção implementada para garantir a exibição e o download adequado de documentos que contenham caracteres não ASCII.
* Corrigida a movimentação de solicitações para que não ocorram inconsistências ao anexar um novo documento.
* Corrigida a edição do nível de segurança de pastas e documentos para que seja atualizado corretamente ao ser alterado.
* Efetuados ajustes para permitir configurar aprovação para uma pasta que não herda a configuração de aprovação da sua pasta pai.
* Corrigida a funcionalidade de cópia controlada, para que o download dos arquivos .docx sejam gerados corretamente em formato PDF.
* Corrigida a função `SOCIALBC.openAnswerForm('ID FORM')`, garantindo a abertura correta do formulário via dialog para a inclusão de registros.

## 260519

## 19 de Maio de 2026

---

## Correções

* Corrigido o recurso Iniciar solicitações para permitir abrir uma solicitação sem anexos quando há um histórico de *uploads* pendentes para o usuário.
* Efetuados ajustes no Agendador de tarefas para que as tarefas programadas sejam executadas corretamente.
* Ajustado o recurso Iniciar solicitações para que os dados dos processos sejam exibidos no idioma selecionado para uso na plataforma.
* Realizada correção para que o sistema informe caso o mesmo e-mail seja vinculado a múltiplas empresas sob o mesmo contexto do Identity com integração ativa, prevenindo bloqueios de acesso. Mais informações podem ser obtidas em [Integração da plataforma com Identity](https://tdn.totvs.com/x/Tx1bB).

## 12 de Maio de 2026

---

## Correções

* Efetuados ajustes na criação de artigos em comunidades para que a imagem de capa do artigo seja exibida corretamente para usuários comuns.
* Atualizado o ícone do evento  do Editor de processos para manter o padrão e a consistência visual.
* Efetuados ajustes para que um documento que está sendo criado possa ser enviado para aprovação logo em seguida sem que ocorram inconsistências de permissão do aprovador.
* Efetuados ajustes para permitir editar as propriedades de um documento quando ele está dentro de uma pasta configurada para criar nova revisão.
* Correção aplicada para que o evento global *validateCustomMetadata* publique documentos apenas se os campos customizados estiverem preenchidos.
* Corrigido o recurso de anexos em solicitações para permitir anexar corretamente mais de um documento ao abrir uma solicitação.

## 260505

## 05 de Maio de 2026

---

## Melhorias

### Adequação ao CNPJ alfanumérico

Devido ao crescimento contínuo de empresas e ao iminente esgotamento das combinações numéricas disponíveis para CNPJ, a Receita Federal do Brasil implementará o CNPJ alfanumérico a partir de **julho de 2026**.

Nesse novo formato, os 12 primeiros caracteres do CNPJ poderão ser compostos por **números** e **letras**, enquanto os 2 últimos dígitos verificadores permanecerão numéricos.

Com essa mudança, as validações de CNPJ disponíveis nos **editores de formulários clássico e atual da plataforma** foram atualizadas para aceitar letras nos 12 primeiros caracteres do CNPJ.

### Possui customização?

Se sua empresa possui **validações**, **máscaras** ou **regras customizadas** envolvendo CNPJ, é **essencial** revisar e validar essas implementações para garantir a compatibilidade com a nova estrutura alfanumérica.

## Correções

* Efetuados ajustes para permitir movimentar uma solicitação para um subprocesso sem que ocorram inconsistências de permissão.
* Efetuados ajustes no componente [Atividade de serviço](https://tdn.totvs.com/x/_5jHNg) para considerar o tipo de valor vindo do campo do formulário no *script* de execução (numérico, *string*, booleano etc), sem realizar nenhuma conversão. Também foi ajustado o tipo byte[] para aceitar a seleção de campos do formulário.

  Importante!

  Para ajustar o comportamento, basta editar a integração a partir das configurações da Atividade de serviço e salvar para gerar o *script* atualizado.  
  As integrações que já existem não serão impactadas, continuarão funcionando corretamente. Porém, quando forem editadas, o *script* será atualizado com o novo comportamento.
* Efetuados ajustes para não validar incorretamente as regras de anexos ao movimentar e transferir solicitações em bloco.
* Realizada correção para que que a consulta de serviços via plugin do Eclipse funcione corretamente.
* Realizado ajustes de segurança e melhorias de estabilidade garantindo uma experiência fluida.
* Realizada correção para que o formulário respeite as customizações visuais definidas em código, independente do tema aplicado na plataforma.
* Aprimoramos o componente de tabela em dispositivos iOS. Agora, a rolagem horizontal funciona de forma nativa e consistente, garantindo uma navegação mais fluida e consistente.

## 260428

## 28 de Abril de 2026

---

## Melhorias

### Novo no editor: cores do tema refletidas automaticamente

Mais uma novidade no editor de formulário e processo, agora, os ícones e botões de ação como **Salvar**, passam a refletir automaticamente a cor do tema definido na plataforma. Essa adequação também está presente na tela de pré-visualização do formulário , contribuindo para uma experiência mais consistente, fluida e alinhada ao padrão visual adotado pela sua empresa.

Vale destacar que essa adequação acontece diretamente nos editores, garantindo maior coerência visual durante a criação ou edição de um processo ou formulário. Neste momento, os *layouts* prontos ainda não acompanham automaticamente a cor do tema aplicado, sendo necessário adequá-lo caso haja necessidade.

Explore a novidade no seu próximo processo ou formulário e aproveite uma construção mais alinhada à identidade visual da sua empresa.

## Correções

* Corrigido o histórico de movimentação de solicitações para que as ações sejam exibidas corretamente depois que as solicitações são convertidas para outra versão do processo.
* Correção implementada para garantir a visualização correta de documentos em páginas customizadas.
* Realizado ajuste para que a importação de processos ocorra corretamente.
* Realizada correção para que o evento `beforeUpdateUser` não solicite a senha quando os parâmetros estiverem de acordo, permitindo outras edições como alteração de nomes ou papéis.
* Documentação sobre **`WCMAPI`** atualizada para incluir a propriedade `userCode.`Feita também a revisão geral dos métodos disponíveis, garantindo maior clareza e suporte aos desenvolvedores.

260422

## 22 de Abril de 2026

---

## Correções

* Correção aplicada para permitir o uso de espaços e múltiplos termos nos filtros da Central de Tarefas.
* Correção realizada para possibilitar a autenticação na widget Analytics pelo aplicativo My Fluig.

260414

## 14 de Abril de 2026

---

## Melhorias

### Descontinuação do Editor de processos clássico

Conforme já divulgado no Portal do ciclo de vida de produto, comunicamos que o **Desenhador de processos clássico****na atualização Voyager 2.0 e superiores**será descontinuado em **30/07/2026**, ou seja, **não estará mais acessível** a partir desta data.

A todos os clientes que ainda utilizam esta versão do recurso, sugerimos que adotem o recurso [Editor de processos 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=860245005), que permite **modelar**, **configurar** e **gerenciar** processos de negócio de forma **visual**, **padronizada** e muito mais **moderna**. Com ele, é possível criar e editar processos, definir etapas, atividades, responsáveis, configurar integrações, aplicar regras e validações e publicar processos, além de exportar e manter histórico de alterações.

Saiba mais detalhes em [Substituição do Editor de processos clássico - TOTVS Fluig](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38053949078039-Substitui%C3%A7%C3%A3o-do-Desenhador-de-Processos-Cl%C3%A1ssico-TOTVS-Fluig).

### Preparação para o novo CNPJ Alfanumérico

Devido ao crescimento contínuo de empresas e ao iminente esgotamento das combinações numéricas disponíveis para CNPJ, a Receita Federal do Brasil implementará o CNPJ alfanumérico a partir de **julho de 2026**.

Com isso, a plataforma vem se preparando antecipadamente para suportar o CNPJ Alfanumérico. Esta adequação visa garantir a continuidade e a integridade dos dados frente às mudanças regulatórias iminentes.

#### O que muda na estrutura do CNPJ?

* + - Composição: Os 12 caracteres iniciais poderão ser formados por uma combinação de letras e números.
    - Dígitos verificadores: Os 2 caracteres finais permanecerão **estritamente** numéricos.

#### Atualizações na Plataforma

Estamos implementando as validações necessárias no **Editor de Formulários** para garantir que a plataforma aceite e processe corretamente o novo formato assim que ele for oficialmente implementado.

#### Possui customização?

Se sua empresa possui customizações, máscaras de entrada ou regras de validação próprias que envolvam o campo de CNPJ, recomendamos que:

* + - * Realize a revisão das regras de código e lógica de validação.
      * Valide as implementações para assegurar a compatibilidade com a nova estrutura alfanumérica.

## Correções

* Ajustes nas permissões para que seja possível utilizar corretamente a widget Editor de conteúdo.
* Correção de inconsistência na API REST *updatedescription.*
* Realizado ajuste para que as imagens de banner dos artigos sejam apresentadas corretamente para usuários não administradores em comunidades.
* Correção aplicada para permitir que as cores definidas no tema global da plataforma sejam replicadas nos formulários do antigo editor sem a necessidade de ajustes manuais.
* Correção de inconsistência no cadastro de documento do tipo Aplicativo.

## 260408

## 08 de Abril de 2026

---

## Correções

* Correção de inconsistência relacionada aos serviços SOAP.

260407

## 07 de Abril de 2026

---

## Correções

* Realizados ajustes nos filtros da Central de Tarefas, para que sejam atualizados automaticamente após o início de uma solicitação que utilize integração com Datasets.
* Correção do evento *BeforeUpdateUser* para que seja possível realizar a alteração de senha via Editar perfil e assegurar a continuidade da sessão na plataforma.
* Correção realizada no alinhamento do campo Tabela ao utilizar a tecla TAB para mudar de campo, trazendo mais usabilidade tanto no editor quanto na movimentação de solicitações.
* Correção na visualização dos campos do formulários no mobile, para que sejam apresentados corretamente quando existirem dois campos na mesma linha.
* Corrigida inconsistência ao tentar iniciar solicitação com tabela pelo aplicativo My Fluig.
* Ajuste realizado para possibilitar alterações nos serviços existentes através do Painel de Controle.
* Ajustes nas mensagens do recurso de , para deixar mais clara a limitação na exportação avançada de processos que possuam grande volume de registros na tabela paiXfilho.
* Correção no layout do botão de *upload* ao adicionar muitos anexos ao documento.

## 260331

## 31 de Março de 2026

---

## Correções

* Corrigida a publicação de documentos para que o tamanho do documento publicado seja armazenado corretamente no campo Tamanho das suas propriedades.
* Corrigido o processo de *check-out* do documento para que seja feito corretamente quando o documento possui anexos.
* Efetuados ajustes para que seja possível excluir corretamente uma marca d'água existente.
* Efetuados ajustes para que o *status* da solicitação do processo principal seja atualizado e exibido corretamente assim que a solicitação do subprocesso for finalizada.
* Ajuste realizado na configuração de formulários de processo para garantir a extração correta de dados no Analytics.
* Corrigida a persistência de dados em campos ZOOM com Dataset, garantindo a integridade e a correlação correta dos registros em tabelas com mais de 10 linhas.
* Ajustada a API de atualização de usuários para garantir a integridade do e-mail entre perfil e comunidades quando o Identity está inativo e bloqueando edições parciais quando o Identity está ativo e assegurando a replicação correta dos dados nos demais cenários.

## 260324

## 24 de Março de 2026

---

## Melhorias

### Novos filtros na aba Sob minha gerência: Consulte solicitações Finalizadas e Canceladas.

Dando continuidade à novidade já disponível em Minhas solicitações, agora você tem total visibilidade na aba [Sob minha gerência](https://tdn.totvs.com/x/UPLuDQ). Com essa atualização você consulta rapidamente as solicitações **Finalizadas** ou **Canceladas** através do filtro por status. Garantindo controle total e ágil sobre todo o fluxo de solicitações.

### Mais mobilidade na aprovação de solicitações!

Agora, o Editor de processos conta com o recurso que leva as aprovações de solicitações diretamente para o aplicativo **My Approval**. Nas [configurações de aprovação](https://tdn.totvs.com/pages/viewpage.action?pageId=862123505#Plataforma%E2%9D%99Atividade-ConfiguraratividadeparaseraprovadapeloMyApproval), é possível configurar **atividades** para serem exibidas como uma tarefa no aplicativo, definindo quais informações devem ficar em **destaque** para o aprovador.

Além disso, o fluxo do processo pode ser controlado com **precisão**: basta indicar qual será a próxima etapa em caso de **aprovação** ou **rejeição**. O resultado é mais agilidade, decisões mais rápidas e processos que continuam fluindo a qualquer hora e em qualquer lugar. É muito mais **mobilidade** para o dia a dia da sua equipe!

## Correções

* Realizada correção para que o evento validateMetadata valide corretamente as informações inseridas em campos customizados.
* Realizada correção para permitir que campos inseridos em abas sejam identificados e selecionados como descritores no novo editor de formulários.

## 260317

## 17 de Março de 2026

---

## Melhorias

### Ordenação de campos para o Analytics mais ágil

Para otimizar a configuração de envio de campos para o Analytics, a ordenação dos campos foi aprimorada e agora, você define rapidamente a posição dos campos de forma simples, bastando arrastá-los (*drag and drop*) até a posição desejada. Essa mudança garante mais rapidez para você estruturar seus dados exatamente como precisa.

## Correções

* Correção realizada para que a exportação de processo via Eclipse ocorra normalmente após atualização para 2.0.
* Melhoria na mensagem exibida, tornando mais claro que processos não podem ser atribuídos a usuários desativados.
* Ajustes realizados para garantir a movimentação de solicitações em processos que utilizam formulários configurados com armazenamento em tabela única.
* Correção realizada para que o modal de permissões seja exibido corretamente, com os botões **Salvar** e **Cancelar**, sem impedir a edição das permissões.
* Criado parâmetro para permitir desabilitar o uso do recurso Documento externo na empresa. [Clique aqui](https://tdn.totvs.com/x/yx37PQ) e saiba mais.
* Efetuados ajustes para aumentar a segurança na visualização de documentos externos.
* Efetuados ajustes para permitir trocar o arquivo físico de um documento que está em *check-out* a partir da Central de tarefas sem que ocorram inconsistências.

## 260310

## 10 de Março de 2026

---

## Melhorias

### Mova o fluxo de um componente para outro

A partir de agora, para **trocar** o componente para onde o fluxo está direcionando no diagrama do processo, basta **mover** a **linha existente** de um componente para o outro, sem precisar remover e adicionar a linha novamente!

Dessa forma, fica mais **rápido** e **prático** editar o diagrama do processo. Confira!

### Indicador de rascunho do processo atualizado

O **indicador** de que um processo está em **rascunho** foi atualizado seguindo o **padrão** dos demais recursos e mantendo a **consistência** com a identidade visual da plataforma.

Assim, **reforçamos** visualmente o significado de cada indicador, facilitando o **reconhecimento** e **entendimento** do recurso.

### Mais flexibilidade para criar filtros em campos Pesquisa

Agora, ao configurar regras com eventos para filtrar em campos do formulário, você não fica limitado apenas às colunas existentes no dataset. Também é possível utilizar o *alias*— identificador usado para representar o nome de colunas personalizadas — criadas para atender regras específicas de negócio.

Isso significa que, ao definir o valor utilizado no filtro, é possível selecionar tanto uma coluna padrão do dataset quanto informar o alias de uma coluna criada e personalizada.

Trazendo formulários mais eficientes e filtros mais alinhados às regras de cada processo.

## Correções

* Ajustes realizados para garantir que a instalação e a atualização dos módulos Indexer e Realtime sejam executadas corretamente.
* Efetuados ajustes para que os emojis de publicações e comentários sejam exibidos corretamente no aplicativo My Fluig.
* Corrigido o recurso Meus documentos para que seja possível copiar corretamente pastas e documentos para outros locais.
* Realizado ajuste para que seja possível reativar um dataset corretamente.

## 260304

## 04 de Março de 2026

---

## Melhorias

### Formulários mais organizados com painéis expansíveis

Agora ficou mais fácil organizar seus formulários com muitos campos agrupados dentro de um Painel! Com a nova configuração do campo Painel, é possível definir se ele será exibido **expandido** ou **retraído** conforme a atividade do processo.

Essa melhoria reduz a poluição visual e oferece uma experiência mais fluida para quem preenche o formulário, destacando apenas o que é relevante **em cada etapa**.

A configuração de Expandir ou Retrair é feita nas **propriedades do campo Painel**. E para controlar em quais atividades o painel será apresentado expandido ou retraído, basta configurar **uma regra para o campo**, informando quais atividades você deseja que ele esteja expandido ou retraído.

Se a propriedade **Permitir abrir e fechar?** do campo for desativada posteriormente, a regra permanece cadastrada, porém não é executada, garantindo **segurança** e **flexibilidade** na personalização do formulário.

## Correções

* Realizado ajustes para que a exportação de páginas ocorra corretamente.
* Efetuados ajustes para permitir alterar as propriedades de um documento a partir da Central de tarefas quando ele possui uma nova versão ou revisão pendente de aprovação.
* Otimizado o recurso Central de diagnósticos para aumentar o desempenho e diminuir o tempo de espera para exibir as informações.
* Realizados ajustes para garantir a exibição correta do formulário em todos os acessos, utilizando toda a área disponível.
* Ajuste na validação do método *updateSimpleDocument* para evitar a exibição indevida da mensagem sobre configuração de segurança.

## 260224

## 24 de Fevereiro de 2026

---

## Melhorias

### Mais flexibilidade com múltiplas curvas na linha do fluxo

Acabamos de tornar a modelagem dos seus processos ainda **mais flexível**!

Agora é possível criar **mais de uma** **curva** na linha do fluxo entre as atividades do diagrama, facilitando a **organização visual** do processo.

Com isso, você ganha mais liberdade para estruturar o diagrama de forma clara, **evitando sobreposições** e mantendo a **leitura mais fluída**.

Mais **organização**, mais **precisão** e ainda mais **qualidade** na modelagem dos seus processos!

Dica!

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252119#Plataforma%E2%9D%99Diagramadoprocesso-Criardobranofluxoentrecomponentesdodiagrama) e veja mais detalhes.

### Ações a partir de atalhos do teclado no diagrama de processos

A partir de agora, você pode contar com ainda mais **rapidez** na edição dos seus processos.

Além das opções pela interface, utilize **atalhos do teclado** para executar diversas ações no diagrama, tornando sua modelagem muito mais dinâmica:

* + **Ctrl** + **z →** desfazer;
  + **Ctrl** + **y →** refazer;
  + **Ctrl** +"**+**"ou **Ctrl +** ***mouse up***→ aumentar *zoom*;
  + **Ctrl** +"**-**"ou **Ctrl** + ***mouse down***→ diminuir *zoom*;
  + **Ctrl** +**0**→ restaurar visão padrão em 100%.

**Corrija** inconsistências em segundos, **recupere** alterações com facilidade, **restaure** a visão mais confortável e **mantenha** o foco no que realmente importa: a construção de processos eficientes.

Mais produtividade, fluidez e praticidade para o seu dia a dia na modelagem de processos!

Dica!

Saiba mais detalhes em [Desfazer ou refazer ações no diagrama](https://tdn.totvs.com/pages/viewpage.action?pageId=860252119#Plataforma%E2%9D%99Diagramadoprocesso-Desfazerourefazera%C3%A7%C3%B5esnodiagrama) e [Aumentar ou diminuir diagrama](https://tdn.totvs.com/pages/viewpage.action?pageId=860252119#Plataforma%E2%9D%99Diagramadoprocesso-Aumentaroudiminuirdiagrama).

### Mais controle nas regras de campo de formulário: validação por formato com máscaras prontas

Agora, ao criar uma nova regra e selecionar a opção “Validado formato”, você passa a contar com as mesmas opções de máscara do campo Simples diretamente na condição de validação do campo. Isso permite validar automaticamente formatos como:

* + E-mail
  + CPF
  + CNPJ
  + IP
  + CEP
  + Data
  + Hora
  + Data e hora
  + Telefone fixo
  + Telefone celular
  + Placa de carro.

Essa evolução traz mais eficiência reduzindo falhas de preenchimento e evitando informações inválidas desde a origem. O resultado são formulários mais inteligentes, regras mais fáceis de configurar e dados muito mais confiáveis para seus processos. Atualize sua plataforma e aproveite essa novidade!

## Correções

* Corrigida a geração de relatórios de formulários de solicitações para incluir os dados preenchidos nos campos quando a opção Incluir dados do formulário está ativada.
* Disponibilização do IP do usuário logado no evento **[beforeLogin](https://tdn.totvs.com/x/EkDwP)** a fim de implementação de controle de acessos customizados.
* Realizado ajuste para garantir o comportamento correto do método **getCardAPIService().create**.
* Adequação realizada para permitir a utilização de diretórios em volumes compartilhados na rede identificados pelo nome da máquina.
* Ajustado o comportamento da Central de Tarefas para refletir corretamente as alterações dos campos do formulário quando houver filtros aplicados.
* Melhoria da mensagem de erro apresentada ao utilizar o método createDocument do webservice ECMDocumentService quando informada matrícula inválida de usuário ou grupo no campo attributionValue.
* Correção realizada para que o botão de Enviar e as demais opções de movimentação em solicitações sejam apresentadas.

## 260218

## 18 de Fevereiro de 2026

---

## Correções

* Efetuados ajustes para permitir  uma solicitação para a última versão do processo sem que ocorram inconsistências.
* Efetuados ajustes para permitir publicar uma estrutura de pastas com arquivos a partir do recurso  corretamente.
* Corrigida a exibição de informações no recurso  do Painel de controle para que não fiquem sobrepostas.
* Atualizada a mensagem sobre a expiração do suporte à versão atualmente instalada no ambiente para que fique mais clara e objetiva, evitando dúvidas e acionamentos para esclarecimentos.
* Corrigido o campo de formulário do tipo Seleção de dados para salvar corretamente a opção selecionada ao movimentar solicitações a partir do aplicativo My Fluig.
* Corrigido evento *beforeDocumentPublisher* para validar corretamente o preenchimento de informações ao publicar uma nova versão de documento a partir da opção Atualizar arquivo do recurso Documentos.
* Corrigida a exibição de formulários para que não ocorram quebras de *layout* quando acessados em tamanhos reduzidos, mantendo a responsividade de todos os componentes.
* Efetuados ajustes em índices de tabelas do recurso de agendamentos para que não ocorram inconsistências ao iniciar a plataforma.
* Efetuados ajustes em algumas tabelas para não ocorrer inconsistências ao aplicar a atualização Voyager 2.0.0-260127 na plataforma.
* Corrigido o *widget* Editor de conteúdo para exibir corretamente conteúdos HTML personalizados que possuem as *tags* *<script>* e *<style>*.

## 260210

## 10 de Fevereiro de 2026

---

## Melhorias

### Destaque visual do card no modo Coluna

Para aprimorar a experiência na Central de Tarefas, evoluímos o destaque visual do card selecionado no modo colunas. A mudança torna a identificação da solicitação ativa mais clara e imediata. Com isso, você passa a ter mais segurança sobre qual item está em foco, aumentando a fluidez da interação e garantindo o correto preenchimento da solicitação.

### Nova logo TOTVS Fluig

A plataforma Fluig ganhou uma nova logo, totalmente alinhada à identidade visual da companhia. Essa mudança acompanha a evolução da plataforma, conectando os novos recursos e melhorias à nova fase. Resultando em uma experiência mais moderna e consistente a cada atualização.

## Correções

* Realizada correção para garantir a atualização e integração de processos com a plataforma Fluig após a atualização do plugin Eclipse.
* Realizado ajuste para que os relatórios BIRT funcionem corretamente quando utilizados com SQL Server.
* Efetuados ajustes para permitir criar uma nova revisão ou versão de um documento quando ele possui aprovador.
* Correção realizada para que seja possível acessar os filtros da Central de tarefas.

## 260203

## 03 de Fevereiro de 2026

---

## Melhorias

### Adicione controle de tempo nos seus processos com o evento Temporizador!

Quer deixar seus processos mais previsíveis, alinhados ao negócio no que diz respeito ao tempo, cumprindo prazos legais ou aguardando carências acordadas? O evento  resolve isso!

Com ele, seus processos passam a **esperar**, **reagir** ou **disparar** ações automaticamente com base no **tempo**, sem depender de intervenções manuais. Eles podem **aguardar** um prazo antes de solicitar um atendimento, **executar** ações em datas específicas, **automatizar** rotinas recorrentes sempre no mesmo horário, **monitorar** atrasos e **iniciar** ações corretivas.

Assim, seus processos deixam de ser apenas sequências de atividades e passam a refletir como o negócio realmente funciona na linha do tempo. Experimente incluir o evento Temporizador nos seus processos e leve sua automação para o próximo nível!

### Download de anexos diretamente na listagem

Agora você pode baixar todos os anexos de uma tarefa diretamente pela listagem, sem a necessidade de acessar a tarefa individualmente. Ao clicar no ícone de anexos, você encontra a opção de download. Reduzindo ainda mais as etapas e deixando a rotina de uso mais pratica.

## Correções

* Efetuados ajustes para que, ao clicar em Criar formulário no Editor de processo, as alterações feitas no processo sejam salvas automaticamente para que sejam consideradas no formulário.
* Aumentada a segurança do recurso de anexos em solicitações para evitar a exploração de vulnerabilidades.
* Efetuados ajustes na exibição de informações na área Assuntos que acompanho do recurso Editar perfil.
* Corrigido o recurso Compartilhar de comunidades para que não seja permitido compartilhar publicações de comunidades ocultas.
* Realizada correção para que não haja lentidão em datasets customizados.
* Realizada correção para evitar a sobreposição do botão Adicionar Campo sobre os campos customizados na tela de propriedades do documento.
* Realizada correção para que a validação dos campos obrigatórios ocorra apenas na movimentação da atividade, não impedindo o salvamento ou a transferência da solicitação em caso de preenchimento parcial.

## 260127

## 27 de Janeiro de 2026

---

### Atualização obrigatória

Foi identificada uma vulnerabilidade relacionada a segurança de conta de usuário na plataforma; no entanto, o incidente já foi **solucionado**, assegurando seu desempenho e segurança. A correção está disponível no pacote liberado em**27/01/2026**.  
Mantenha sua plataforma sempre atualizada para assegurar uma experiência contínua e segura.

## Melhorias

### Controle de *zoom*: navegação mais precisa e visão mais acessível do diagrama do processo!

Agora ficou ainda mais fácil modelar e navegar pelo diagrama dos seus processos.

Com o novo **controle de *zoom***, você pode **aumentar ou diminuir o tamanho do diagrama** de acordo com sua necessidade, garantindo uma visão mais confortável e precisa. E, com apenas um clique, é possível **retornar rapidamente para a escala de 100%**, facilitando o alinhamento e a revisão dos elementos do processo.

Esse recurso torna a modelagem mais fluída, acessível e eficiente – especialmente em diagramas grandes e complexos ou cheios de detalhes. Mais agilidade para o dia a dia é o que a gente quer, não é mesmo? Confira já!

Dica!

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=860252119#Plataforma%E2%9D%99Diagramadoprocesso-Aumentaroudiminuirdiagrama) e saiba o quanto um diagrama pode ser aumentado ou diminuído.

## Correções

* Corrigido o evento **`beforeUpdateUser`**, resolvendo a falha que impedia o feedback visual ao utilizar a opção "Esqueci minha senha".
* Corrigida a exibição do identificador do processo nos resultados de busca da Central de Tarefas.
* Corrigida a busca geral quando está configurada para ser exibida no topo da plataforma para que os termos inseridos sejam considerados corretamente na busca por resultados.
* Efetuados ajustes nos campos de digitação livre das configurações do processo para que não ocorram inconsistências ocasionadas pela quantidade de caracteres inseridos.
* Complementado o *log* do TOTVS Fluig quando é  utilizado o sistema operacional Ubuntu para informar quando não é possível exportar a imagem de um processo por falta de pacotes de fontes que não estão instaladas no servidor.
* Adicionada mensagem na busca por documentos relacionados – ao editar um documento – para informar quando a busca não está disponível e instruir a entrar em contato com o administrador de plataforma.
* Realizada correção no comportamento do campo Fórmula para que, ao ser configurado como desabilitado, não permita a edição de seus valores.
* Realizada correção para que seja possível assumir solicitações em bloco na Central de tarefas.
* Realizada correção para que a validação dos campos obrigatórios ocorra apenas na movimentação da atividade, não impedindo o salvamento ou a transferência da solicitação em caso de preenchimento parcial.
* Realizada correção para que a configuração “Preenchido” do componente de Abas funcione corretamente no novo editor de formulários.
* Corrigida a situação que impedia atualizar de releases inferiores (1.7.1, 1.8.0 e 1.8.1) para a release 1.8.2. A versão mínima para atualização passa a ser a **1.8.2-260127.** Saiba mais no [guia de atualização](https://tdn.totvs.com/x/CkwxE) e na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN).

## 260120

## 20 de Janeiro de 2026

---

## Melhorias

### Artigos com mais segurança de conteúdo em comunidades

A partir de agora, vídeos publicados no recurso [Documentos](https://tdn.totvs.com/x/7e-uDQ) que são inseridos dentro de [Artigos](https://tdn.totvs.com/x/p-vuDQ) em [Comunidades](https://tdn.totvs.com/x/VKVuOQ), passam a considerar o que foi definido na opção ***Download* e impressão** do próprio artigo. Ou seja, se o artigo permite *download*, também será possível baixar o vídeo. Caso contrário, não é permitido que o vídeo inserido dentro do artigo seja baixado e, consequentemente, a opção **Baixar** não é exibida.

Dessa forma, é possível garantir o mesmo nível de permissão para todo o conteúdo que compõe o artigo, proporcionando privacidade para artigos internos ou que não podem ser compartilhados com quem não tem permissão para vê-los. Afinal, segurança nunca é demais, não é mesmo?

### Personalização de filtros na Central de tarefas

Pensando em oferecer uma experiência ainda mais prática e personalizada, a Central de tarefas do Fluig Voyager permite selecionar e organizar os dados da solicitação e os campos descritores do formulário ao personalizar um filtro, oferecendo total controle sobre as informações que deseja exibir.

Ao selecionar um processo que contém formulário com campos descritores, é possível adicionar estes campos no filtro a ser criado, possibilitando filtrar informações não só da solicitação como do formulário também, ampliando as possibilidades de visualização e filtragem.

Na aba **Exibir dados**, é possível selecionar quais dados das solicitações e quais campos descritores do formulário serão apresentados na lista de tarefas e, além disso, é possível também definir a ordem que essas informações aparecem por meio do ícone , trazendo para uma posição acima ou abaixo, priorizando o que realmente importa conforme sua necessidade, de forma simples e prática.

Essa novidade garante mais precisão, clareza e uma navegação mais eficiente na Central de tarefas.

Acesse a documentação [Plataforma | Central de filtros](https://tdn.totvs.com/x/PvLuDQ) e saiba mais.

### Regra de obrigatoriedade dinâmica para campos de formulário

Implementamos a possibilidade de alternar a obrigatoriedade de campos automaticamente através de eventos, permitindo que um campo passe de obrigatório para opcional e de opcional para obrigatório, conforme as regras definidas.

### Exibição do dataset no novo editor de formulários

Agora é possível visualizar o nome do dataset vinculado ao formulário diretamente na interface. Nas configurações do formulário dentro do editor , foi adicionado o campo obrigatório **Dataset do formulário**. Este campo é preenchido automaticamente e identifica o dataset gerado para armazenar os dados do formulário, facilitando consultas em processos, widgets, relatórios e integrações via API.

## Correções

* Corrigida a criação avançada de documentos para permitir criar corretamente um documento a partir da cópia de outro documento já existente.
* Correção na renovação do *token JWT*, eliminando a necessidade de iniciar uma nova sessão.
* Efetuados ajustes para permitir exportar corretamente as consultas de solicitações.
* Corrigido o *gateway* Exclusivo do desenhador clássico de processos para que os botões de ação sejam exibidos corretamente quando há muitas regras definidas.
* Corrigida a exibição das curvas dos fluxos do diagrama de processos – que foram criados a partir do Eclipse e exportados para a plataforma – depois de criar um formulário e recarregar a página.
* Realizada correção para que seja possível editar e excluir um serviço contendo caractere especial.
* Otimização implementada para corrigir a lentidão na Central de tarefas em solicitações com alto volume de anexos.
* Correção no componente de início condicional para permitir a abertura de solicitações via job agendado.
* Realizada correção para que seja possível atualizar relatórios BIRT via Plugin Fluig para Eclipse.
* Efetuados ajustes para que o evento de igualdade de campos considere corretamente o valor de campos do tipo pesquisa e múltipla escolha nas regras de formulário quando esses campos estão dentro de uma tabela.

## 260113

## 13 de Janeiro de 2026

---

## Correções

* Efetuados ajustes no recurso Documentos para permitir copiar o *link* de um documento e ver corretamente os documentos relacionados.
* Efetuados ajustes para exibir o nome dos grupos ao buscá-los para associar à aprovação de pastas.
* Efetuados ajustes em *updates* relacionados a usuários criados a partir do TOTVS Identity para que não ocorram inconsistências ao atualizar a plataforma para a 2.0.0-251209.
* Atualizado o recurso Documentos para que documentos com algumas propriedades específicas não fiquem com o conteúdo em branco ao serem publicados.
* Corrigido o recurso Iniciar solicitações para que processos inativos não sejam exibidos.
* Corrigido o *link* existente no *e-mail* de notificação para direcionar corretamente para a solicitação depois de autenticar-se na plataforma.
* Efetuados ajustes na exclusão de solicitações para que não ocorra inconsistência ao excluir muitas solicitações de uma única vez.
* Corrigido o *update* relacionado ao Agendador de tarefas para que não ocorram inconsistências ao atualizar para a Voyager 2.0.
* Atualizada a biblioteca *okhttp* para a prevenção de vulnerabilidades.
* Implementado ajuste no comportamento do formulário, padronizando seu funcionamento entre a Web e o aplicativo móvel e garantindo o carregamento correto dos arquivos **.js**.
* Correção realizada para que a barra de rolagem horizontal seja exibida automaticamente sempre que o conteúdo da tabela ultrapassar a largura disponível na tela.
* Correção realizada para que seja possível utilizar a hAPI setCardValue no evento afterStateEntry;
* Ajuste realizado para corrigir o cálculo automático do campo Fórmula e o cumprimento das regras definidas para o campo.
* Correção realizada para que, em cenários com campos obrigatórios ocultos, a plataforma exiba um modal informativo indicando de forma clara qual campo está sem preenchimento.

## 2512xx

## 16 de Dezembro de 2025

---

## Melhorias

### Filtre os resultados de datasets em seu formulário com as evoluções do campo Pesquisa

Com a evolução do campo **Pesquisa** no novo formulário, passa a ser possível buscar os dados de datasets dinâmicos e contextualizados, como listar apenas os usuários ativos da plataforma ou exibir automaticamente as cidades de acordo com o estado selecionado.

Essa novidade permite aplicar filtros entre os campos e definir limites de exibição e seleção de resultados, garantindo um melhor desempenho. Além disso, os valores selecionados em um campo Pesquisa podem ser utilizados para preencher automaticamente outros campos.

É possível também iniciar o campo com filtros pré-configurados, tornando o formulário mais eficiente e intuitivo para quem for respondê-lo.

Todas essas possibilidades são configuráveis sem a necessidade de codificação adicional. Atualize sua plataforma e aproveite essa evolução!

Saiba mais

Acesse a documentação [Plataforma | Editor de formulário](https://tdn.totvs.com/x/jH6MNg).

## Correções

* Corrigido o *flow*  para que a abertura de solicitações funcione corretamente ao utilizar o banco de dados SQL Server.
* Realizado ajuste para que as APIs de consulta do novo formulário retornem corretamente o nome do dataset associado.
* Ajuste realizado para que as regras do campo do formulário sejam apresentadas corretamente.
* Realizada correção para que seja possível utilizar o Fluig Studio em modo demo.

## 251209

## 09 de Dezembro de 2025

---

## Correções

* Realizado ajuste para garantir que novos registros de formulário criados na aba Anexos sejam gerados corretamente.
* Realizado ajuste para corrigir a inconsistência de cores, onde no Modo Claro a linha par aparecia com tonalidade do tema Escuro e vice-versa, garantindo a correta exibição.
* Ajustado o *log* da plataforma para não exibir a mesma mensagem diversas vezes e de forma inconsistente.
* Realizado ajuste para que a API Mobile capture o campo e faça a movimentação da solicitação corretamente.
* Realizada correção para que o evento global beforeDocumentPublisher valide corretamente também no fluxo de edição de documentos.
* Realizado ajuste para que a regra de ocultar aba seja executada corretamente.
* Realizado ajuste para que o componente *ECMBC.updateDocument* volte a funcionar corretamente, garantindo o comportamento esperado na atualização de documentos.
* Realizado ajuste para que a widget Gráfico de processos e tarefas seja exibida corretamente.
* Realizado ajuste para que a barra de rolagem horizontal seja exibida corretamente quando conteúdo da tabela ultrapassar a largura disponível na tela.

## 251202

## 02 de Dezembro de 2025

---

## Melhorias

### Componentes reestilizados com novo visual

Atualizamos os componentes do Style Guide abaixo, para refletir o padrão visual do Animalia Design System, alinhando a identidade visual do Fluig aos demais produtos da TOTVS. Essa evolução garante maior consistência visual e fortalece a comunicação entre as interfaces, proporcionando uma experiência moderna e coerente.

* + Accordion
  + Autocomplete Tags
  + Loading
  + Tabs
  + Breadcrumb
  + Label
  + Dropdown

Saiba mais

Acesse o [guia de estilos](https://style.fluig.com/) do Fluig para ver mais detalhes.

## Correções

* Realizado ajuste para que não existam referências ao CKEditor e que o DOMPurify esteja atualizado com a versão correta.
* Realizado ajuste para que seja possível renomear os anexos da solicitação corretamente.
* Correção realizada para que campos do tipo input radio não iniciem marcados com o primeiro valor disponível ao utilizar formulários exportados via Eclipse/Fluig Studio.
* Corrigida a exibição de versões de um documento para que seja possível ver o conteúdo da versão anterior antes de restaurá-lo.
* Realizado ajuste para que ao utilizar o campo de Múltipla escolha em um formulário de processo seja possível movimentar a solicitação corretamente.

## 251126

## 26 de Novembro de 2025

---

### Consulte suas solicitações Finalizadas e Canceladas

A consulta de solicitações ficou ainda mais completa. Agora, na aba Minhas solicitações, além de consultar as solicitações com o filtro de status Abertas, você também pode consultar as solicitações já **Finalizadas** e **Canceladas**.

Dessa forma, fica muito mais fácil controlar tudo o que já foi concluído, mantendo sua rotina organizada do início ao fim, trazendo mais controle e eficiência para acompanhar cada etapa das suas solicitações.

Saiba mais

Acesse a documentação [Plataforma | Solicitadas por mim](https://tdn.totvs.com/x/RvLuDQ). 

### Remoção do plugin jQuery Migrate

Confira a [**notícia**](https://tdn.totvs.com/x/5ZgfP) publicada sobre a remoção do plugin jQuery Migrate da plataforma. Caso ainda não tenha revisado seus códigos, este é o momento ideal para fazê-lo, garantindo total compatibilidade e evitando impactos indesejados.

Consulte a documentação [Como identificar o que precisa ser atualizado](https://tdn.totvs.com/x/zA2eI) e saiba como identificar possíveis pontos de ajuste.

### Títulos de formulários agora definidos automaticamente

Agora, os formulários criados pelo novo editor de processos/formulários passarão a receber automaticamente o nome padrão “Formulário + Nome do processo”, dispensando a necessidade de definir um título manualmente, caso desejado.

## Correções

* Adicionada mensagem informativa sobre a utilização do evento *beforeSendData* nos *scritps* do Editor de processos.
* Correção aplicada para que, ao usar a opção Valor específico, o campo passe a exibir o tipo de input correspondente à sua configuração, como moeda, numérico ou texto, assim como já ocorre em Definido Valor → Campo fixo.
* Implementada a evolução da API para permitir a alteração da propriedade **downloadEnabled** em documentos, garantindo o ajuste dessa configuração. [Clique aqui](https://api.fluig.com/latest/content-management/swagger-ui/#/Documents/update) e confira os detalhes na API.
* Corrigido o recurso Editar perfil para que seja possível editar os dados do usuário wcmadmin corretamente.

## 251118

## 18 de Novembro de 2025

---

## Melhorias

### Criação de processos com Inteligência Artificial

Agora ficou muito mais rápido transformar suas ideias em processos dentro do TOTVS Fluig. O recurso **Configurar processos** recebeu uma importante atualização: você já pode **criar processos completos com apoio da IA**, além de continuar usando os *templates* prontos!  
  
**O que mudou?**  
No menu **Processos → [Configurar processos](https://tdn.totvs.com/pages/viewpage.action?pageId=233763153)**, agora existe a nova opção **Deixe a IA cuidar do seu próximo processo**.  
A partir dela, basta descrever o que você precisa — etapas, objetivo e resultado esperado — e a IA gera automaticamente um processo inicial para você ajustar como quiser.  
Além disso, também é possível:

* + Ver **sugestões de processos** prontos para acelerar sua criação.
  + Escolher um **ícone** para facilitar a identificação.
  + Definir **código** e **título** do processo no próprio fluxo.
  + Revisar sua descrição e gerar uma nova versão com IA antes de finalizar.
  + Criar o diagrama automaticamente com **Sobrepor diagrama**.

**Por que isso importa?**  
Essa melhoria **encurta a jornada inteira de criação**, reduz retrabalho e ajuda times a tirarem ideias do papel em minutos — ideal para quem precisa documentar fluxos rápido, padronizar operações ou prototipar novos processos.

### Bloco de atividades: dois recursos em um único componente!

O  chegou para simplificar a modelagem de processos. Ele é um componente inovador que une – de forma simplificada e eficiente – os conceitos tradicionais de ***Pool*** e ***Swimlane*** em um único elemento visual, tornando a modelagem dos processos mais ágil e o diagrama mais claro e intuitivo.

Com ele, é possível representar o participante principal – **Organização** (*Pool*) – e as responsabilidades – **Subdivisões** (*Swimlanes*) – envolvidos em um processo. Tudo isso de forma gráfica, nomes personalizados, cores diferenciadas e um visual moderno para deixar seus processos muito mais bonitos e fáceis de entender. Muito bacana, hein!?

### Novos métodos para botões em formulários avançados

Implementamos novos métodos para manipulação dos botões de **“Adicionar”** e **“Lixeira”** em formulários avançados, fazendo com que seja possível ocultar ou adicionar os botões em tabelas paixfilho específicas, garantindo mais compatibilidade com diferentes tipos de ambientes.

**Novos métodos** 

* + **form.isHideDeleteButton**(String tableName);
  + **form.isHideAddButton**(String tableName);
  + **form.isHideAddButton**();
  + **form.setHideDeleteButton**(String tableName, boolean hideDeleteButton);
  + **form.setHideAddButton**(String tableName, boolean hideAddButton);
  + **form.setHideAddButton**(boolean hideAddButton);

Além disso, novos atributos de posicionamento dos botões também foram implementados**.**

* + **addbuttonposition**
  + **deletebuttonposition.**

Essas novidades ampliam o nível de personalização e controle disponível para desenvolvedores, permitindo ajustar o comportamento dos botões de forma mais precisa e alinhada às necessidades de cada formulário.

Saiba mais

Saiba mais detalhes nas documentações [FormController](https://tdn.totvs.com/x/GO_CJw) e [Personalização de formulários](https://tdn.totvs.com/x/OufTJw).

falsesample1Atualizações inferiores2Atualização 2.0 Voyager

## Correções

* Realizado ajuste para que seja possível consultar solicitações corretamente.
* Ajuste realizado para que seja possível redimensionar verticalmente campos *textarea*.
* Efetuados ajustes para que a autenticação funcione corretamente na atualização 2.0 ao utilizar o Fluig Studio quando há integração com o TOTVS Identity.
* Corrigida a criação e exibição da página do Editor de processos para que possa ser acessada corretamente ao atualizar para a Voyager (2.0).
* Melhoria realizada na mensagem apresentada quando uma atividade configurada com movimentação automática por prazo expirado é atribuída a um papel ou grupo, tornando a ação mais clara.

## 251111

## 11 de Novembro de 2025

---

## Correções

* Realizado ajuste para direcionamento correto à página de Política de Uso para novos usuários.
* Correção aplicada no carregamento do widget do Termo de Aceite, que resultava em tela branca e impedia o login inicial de novos usuários.
* Efetuada correção em caracteres de arquivos de configuração para que não ocorram inconsistências ao atualizar a plataforma da 1.8.2 para a 2.0.0.
* Criada validação da versão da plataforma e de aplicativos de parceiros para permitir atualizar o ambiente somente quando a versão dos dois produtos são compatíveis entre si.
* Efetuados ajustes para que usuários criados a partir do TOTVS Identity consigam acessar a plataforma corretamente na atualização 2.0.0.
* Efetuados ajustes para que a atividade que está em execução seja exibida com uma cor de destaque ao visualizar o diagrama do processo a partir de uma solicitação.
* Correção aplicada para ajustar a exibição de datasets dependentes durante o deploy e restaurar o ícone informativo no painel de controle.
* Correção aplicada para que seja possível remover documentos via API com autenticação OAuth1 sem ocorrer o erro de NullPointerException, garantindo o retorno correto do status.

## 251104

## 04 de Novembro de 2025

---

## Correções

* Realizado ajuste para que seja possível acessar páginas de forma pública corretamente.
* Correção aplicada para que seja possível visualizar as tarefas em pool para grupos que possuem caracteres especiais.
* Correção aplicada para que seja possível adicionar um grupo para permissão de visualização nas configurações de processos.
* Ajuste realizado para desabilitar corretamente o campo de botões mobile ao remover o fluxo entre etapas com configuração de botões de aceitar/rejeitar.
* Efetuados ajustes para não ocorrer inconsistências no aplicativo My Approval ao excluir um fluxo entre duas etapas de um processo quando uma delas possui configurações para *mobile*.

## 251029

## 29 de Outubro de 2025

---

## Melhorias

### Nova página de Iniciar solicitações

Compreendemos a importância de uma jornada fluida e eficiente na gestão de suas demandas. Por isso, desenvolvemos uma nova interface para otimizar o ponto de partida de cada solicitação. Ao iniciar uma solicitação, você pode ter a tranquilidade de que cada passo seguirá rigorosamente as atividades e os fluxos definidos na versão vigente do processo no momento da criação. Isso garante consistência e previsibilidade, mesmo com a publicação de novas versões do processo no futuro.

E para tornar sua adaptação ainda mais simples, preparamos um guia interativo de boas-vindas na própria página de iniciar solicitações. Você será conduzido(a) por um tour intuitivo, com uma breve descrição do que fazer e como se localizar, garantindo que você aproveite ao máximo todas as funcionalidades disponíveis desde o primeiro acesso.

Esperamos que a experiência ao iniciar solicitações ganhe uma nova vivência, permitindo que ela agilize e traga ainda mais facilidade a sua rotina. 

Para conferir a documentação completa, acesse [Iniciar solicitações](https://tdn.totvs.com/x/VfHuDQ) e fique por dentro de todos os detalhes.

## Correções

* Efetuados ajustes para que todas as colunas da tabela FDN\_ACCESSLOG sejam criadas corretamente ao atualizar a plataforma da Crystal Mist (1.8.2) para a Voyager (2.0).
* Por questões de segurança e prevenção de exploração de vulnerabilidades, a porta padrão utilizada pela plataforma para o FTP foi alterada de 21 para 9021.
* Validado o comportamento do sistema ao realizar o upload com [Impressão de cópia controlada](https://tdn.totvs.com/x/F5MbCQ), garantindo a correta abertura do PDF e a consistência das mensagens de log no processo PDFHandler.
* Ajuste realizado para melhorar o desempenho e reduzir o tempo de carregamento da página [Configurar processos](https://tdn.totvs.com/x/UfHuDQ).
* Efetuados ajustes para permitir autenticar-se corretamente no aplicativo My Fluig quando é utilizado o protocolo LDAP ou a senha em MD5.

## 251021

## 21 de Outubro de 2025

---

## Melhorias

### Novidades no editor de formulários

O editor de formulários passou por uma atualização e agora está mais completo!

falsesample1Duplicação de campos

* **Duplicação de campos**: crie cópias de campos já existentes de forma rápida, inclusive com as regras já definidas.

2Seleção múltipla campo Pesquisa

* **Seleção múltipla no campo pesquisa**: selecione mais de um registro por vez no campo.

3Limite de resultados campo Pesquisa

* **Nova propriedade** **Limite de resultados****no campo pesquisa****:** define o número máximo de resultados exibidos no campo Pesquisa.

4Eventos de preenchimento e filtro

* **Novos eventos de preenchimento e filtro no campo Pesquisa**: ao selecionar um item, agora é possível **preencher automaticamente** ou **filtrar outros campos** do formulário.

5Novas configurações em regras de formulário

* **Novas configurações para regras de formulários**: novas configurações disponíveis trazendo mais possibilidades de criação de lógicas.

### Novo histórico de versões de formulários

A partir desta atualização ficou mais fácil gerenciar e acompanhar as mudanças realizadas nos formulários vinculados a processos. 

Com o **histórico de versões**, que pode ser acessado através do ícone , é possível verificar os detalhes de cada versão, como data e hora de publicação, modificações feitas e o usuário responsável por cada modificação.

Além disso, também é possível visualizar **qualquer versão anterior**  e até mesmo **restaurá-la**  caso necessário, garantindo mais controle e agilidade para seus formulários.

Saiba mais

Acesse a documentação [Plataforma | Histórico de versões](https://tdn.totvs.com/x/Q69ZP) para saber mais detalhes.

## Correções

* Efetuados ajustes para que seja possível acessar o aplicativo My Approval quando a autenticação está configurada para utilizar o protocolo LDAP.
* Efetuados ajustes na validação de permissões para que usuários comuns sem permissão não consigam remover outros usuários de grupos por meio da API.
* Correção realizada para permitir a sincronização de um dataset, mesmo quando o método onsync está vazio ou não definido.
* Correção realizada para garantir que, ao acessar uma solicitação via notificações, o formulário seja exibido corretamente.
* Ajuste realizado para que, ao criar formulários no modelo Tabelas de Banco de Dados, a plataforma valide corretamente os nomes dos campos, evitando aqueles com caracteres que utilizem termos reservados do banco de dados.

## 251014

## 14 de Outubro de 2025

---

## Correções

* Efetuados ajustes de segurança relacionados à edição de matrícula de usuários.
* Realizado ajuste para que a função fluigAPI.getCardAPIService().create funcione corretamente.
* Corrigido o comportamento do método findChildrenByCardId para assegurar o retorno adequado dos tables id ao utilizar um dataset.
* Ajustado o serviço createDocument via SOAP para que, ao criar um documento em nome de outro usuário, a atribuição seja realizada corretamente.

## 251007

## 07 de Outubro de 2025

---

## Melhorias

### Novo modo de visualização na Central de tarefas!

O modo **Quadro** da Central de tarefas recebeu uma nova configuração! Agora você pode ajustar a exibição das tarefas conforme sua preferência, escolhendo entre dois layouts: **Padrão** ou **Compacto**. 

* + O layout Padrão, exibe as informações das solicitações com mais detalhes e maior destaque visual.
  + Já o Compacto exibe apenas as informações essenciais, reduzindo a carga visual e permitindo visualizar um número maior de solicitações na listagem.

Mais flexibilidade e praticidade para você acompanhar suas tarefas do seu jeito.

Saiba mais!

Acesse nossa documentação e saiba os detalhes no item [Modos de visualização](https://tdn.totvs.com/x/NPLuDQ).

### Mais acessibilidade na plataforma

Foram aplicadas melhorias de acessibilidade no header e no menu para aprimorar a experiência de usuários que utilizam leitores de tela e outras tecnologias assistivas.

## Correções

* Criada a API publica **[servidor\_fluig]/dataset/api/v2/datasets/synchronize/****[codigo\_dataset]** para a sincronização de datasets.
* Efetuadas melhorias nas rotinas de *login* para não permitir o uso de autenticações menos seguras.

## 250930

## 30 de Setembro de 2025

---

## Correções

* Corrigido o retorno das APIs de inclusão de usuários em grupos para que indiquem corretamente o que de fato aconteceu, se a ação foi bem-sucedida ou se ocorreu alguma inconsistência.
* Realizada correção para que ao utilizar a API **v2/requests/{processInstanceId}/activities** o parâmetro **expand=tasks**retorne corretamente as informações de atividades associadas ao processo.
* Correção aplicada para que consultas e fluxos sejam executados com maior agilidade, garantindo a mesma performance do ambiente de produção.

## 250923

## 23 de Setembro de 2025

---

## Melhorias

### Guia de primeiro acesso ao TOTVS Fluig Plataforma

Sem dúvida, esta é a uma inovação que transformará a experiência dos novos usuários em nossa plataforma: o Guia de Primeiro Acesso ao TOTVS Fluig Plataforma, juntamente com uma nova Home totalmente modificada e pensada nos usuários.

Ter uma início facilitado pode garantir o máximo aproveitamento de todas as funcionalidades. Por isso, ao fazer login pela primeira vez, os usuários serão conduzidos de forma intuitiva por um guia interativo de Primeiro Acesso.  
Este recurso foi cuidadosamente desenvolvido para familiarizar o usuário com as principais soluções e funcionalidades da plataforma, proporcionando uma experiência fluida e eficiente desde o primeiro contato.

Durante o guia de Primeiro Acesso, o usuário terá uma visão geral das principais soluções disponíveis, incluindo: Automação de fluxos de trabalho, Processos prontos e soluções com IA, Gestão de conteúdo empresarial, Gestão de tarefas e Portais e comunidades. Além disso, será possível personalizar o perfil, inserindo dados pessoais, área de atuação e função, escolher o tema da plataforma e selecionar o template de página que melhor se adequa à sua rotina de trabalho, tornando a experiência mais relevante e alinhada às suas necessidades.

Logo após concluir o guia, o usuário será recebido na nova Home do TOTVS Fluig Plataforma. Este novo layout foi projetado para ser o centro de comando do usuário, contendo widgets essenciais e conteúdos importantes que facilitam a descoberta de todas as possibilidades que só o Fluig pode proporcionar. A nova Home garante autonomia e agilidade, permitindo que o usuário explore e utilize o sistema com total confiança.

Para conferir a documentação contendo todos os detalhes, acesse [Meu primeiro acesso](https://tdn.totvs.com/x/JQ4KM).

sample2Primeiro acesso

### Atividade de serviço: novo componente do editor de processos para facilitar integrações!

Se você precisa fazer algum tipo de integração em seus processos, já pode comemorar: a Atividade de serviço já faz parte da paleta de componentes do !

A principal característica desse componente é sua capacidade de automatizar a execução de tarefas. Com suporte a serviços REST e SOAP, o componente permite a orquestração direta de serviços externos, promovendo mais automação, integração com outros sistemas e ganho de eficiência nos processos modelados.

Com configuração simplificada e suporte a parâmetros, cabeçalhos e autenticação, o componente oferece flexibilidade e aderência a cenários reais de negócio. Muito bacana, hein?

Dica!

Confira informações detalhadas sobre o componente em .

Nota:

Os serviços disponíveis para uso no componente Atividade de serviços são aqueles que estão cadastrados no recurso  do Painel de controle.

### Atividade de serviço com inconsistência na execução? A captura de erro identifica!

O Editor de processo também já conta com o evento , que é utilizado juntamente com a Atividade de serviço quando sua execução é automatizada.

Esse evento permite o tratamento estruturado de exceções durante a execução do serviço configurado na atividade. Com ele, é possível identificar falhas em chamadas a serviços externos e definir ações corretivas ou alternativas, aumentando a robustez e a confiabilidade dos fluxos automatizados.

Esse evento é essencial para garantir processos resilientes e melhor gerenciamento de incidentes, evitando que uma solicitação fique travada por causa de inconsistências de execução. Mais agilidade que se fala, não é?

### Organize e documente seus processos com o componente Anotação

O componente  veio para somar e agregar informações importantes aos seus processos!

Com ele, é possível adicionar comentários e informações extras diretamente no digrama do processo. Parece simples, mas é um recurso poderoso que visa facilitar a comunicação, o entendimento e a colaboração entre equipes durante a modelagem e a análise dos processos, tornando seus fluxos mais claros e documentados.

Além disso, com um processo bem documentado e com informações importantes à disposição, sua manutenção futura torna-se muito mais fácil e rápida. Informação nunca é demais, não é mesmo?

### Se você prefere codificar, confira as condições avançadas do componente Exclusivo!

Agora, é possível definir [condições avançadas](https://tdn.totvs.com/pages/viewpage.action?pageId=913802155#Plataforma%E2%9D%99Exclusivo-Condi%C3%A7%C3%A3oavan%C3%A7ada) no componente Exclusivo, que permitem criar as regras a partir de codificação, flexibilizando a criação de condições para pessoas mais técnicas que saibam programar e desejam criar expressões avançadas.

Desta forma, é possível criar regras de decisão mais complexas e dinâmicas, baseadas em variáveis do processo, funções personalizadas e operadores lógicos.

Esse tipo de condição é criada em uma IDE embutida no componente, que permite criar as expressões de forma estruturada, onde também são disponibilizados ***snippets*** prontos com as **hAPIs** da plataforma para facilitar a criação das condições. Se você prefere codificar, já pode começar!

Dica!

[Clique aqui](https://tdn.totvs.com/display/fluig/hAPI) e veja todos os métodos que estão disponíveis por meio da **hAPI** e que podem ser utilizados na criação de condições avançadas.

### Organização automática do diagrama do processo

Já pensou em organizar o diagrama do seu processo em um passe de mágica?! Com o novo recurso **Organizar diagrama**, o *layout* do diagrama dos processos é ajustado automaticamente para uma disposição mais limpa, alinhada e visualmente organizada.

Ganhe tempo, melhore a legibilidade dos fluxos e mantenha seus processos sempre claros e bem estruturados com apenas um clique! Assim, fica ainda mais fácil visualizar e entender seus processos. Confira!

Nota:

Esse recurso ainda está em uma versão beta, portanto, podem ocorrer inconsistências.

### Desfazer e refazer: mais agilidade na modelagem do diagrama dos processos

Agora você pode contar com mais controle e segurança na edição dos seus processos!

Com as novas ações **Desfazer** e **Refazer**, você pode modelar o diagrama com mais facilidade, corrigindo inconsistências rapidamente ou recuperando alterações com agilidade.

Trabalhe com mais confiança e flexibilidade na modelagem dos seus processos para agilizar o seu dia a dia!

## Correções

* Efetuados ajustes na lógica de *cache* de *updates* para não gerar excessivas mensagens no *log*.

## 250916

## 16 de Setembro de 2025

---

## Correções

* Corrigida a atualização da coluna Última execução do Agendador de tarefas para exibir corretamente as informações de sincronização de datasets.
* Corrigida a API pública api/public/search/advanced para retornar os resultados corretamente ao ser realizada uma requisição POST.

## 250910

## 10 de Setembro de 2025

---

## Correções

* Ajustado o recurso [Agendador de tarefas](https://tdn.totvs.com/x/W4H5DQ) para que a sincronização de múltiplos *datasets* seja feita corretamente.
* Efetuados ajustes no Editor de processos para salvar corretamente a configuração de mecanismos de atribuição.
* Realizado ajuste para que ao adicionar o componente datatable, seja possível visualizar as informações das colunas corretamente.
* Mensagem ajustada para indicar o limite de 15 caracteres no cadastro de novas áreas.

## 250826

## 26 de Agosto de 2025

---

## Correções

* Ajuste realizado para que a ordenação no histórico de solicitações seja apresentado corretamente.
* Realizado ajuste para que a notificação de novos participantes exiba o nome atualizado da comunidade corretamente.
* Ajuste realizado para que a imagem de perfil da comunidade seja exibida com melhor qualidade. Recomendamos, no entanto, que não contenham texto, para garantir a legibilidade.
* Efetuados ajustes para que a integração TOTVS Fluig x Analytics funcione corretamente.

$("b:contains('oculto')").parent().parent().hide();
]]>
