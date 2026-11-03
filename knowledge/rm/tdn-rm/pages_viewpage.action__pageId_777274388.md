---
content_hash: dc7eb49010ca70ad0b525a0eec8bbed186173a1b1a037dd199783eeaaf16a2a4
fetched_at: '2026-06-29T00:11:37.418484+00:00'
page_id: '777274388'
product: rm
source: tdn-rm
title: Pré Venda - Roleta de Vendas (Nova Visão 12.1.2310 e Superiores)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=777274388
version: 55
---

---

## **Conceito**

A roleta de vendas serve para automatizar a distribuição de compradores cadastrados no Portal de Imóveis para corretores específicos, garantindo uma atribuição justa e equitativa. Essa ferramenta ajuda a otimizar a gestão de leads e o processo de atendimento aos compradores, promovendo uma distribuição imparcial e eficiente entre os corretores disponíveis.

false

**Observação:** Se você já usava roletas em seu portal de imóveis antes de mudar para a nova, é fundamental realizar a conversão. Isso é importante porque, se você tentar usar a Nova Roleta sem fazer essa conversão, o sistema não conseguirá migrar seus dados antigos e o processo de conversão não funcionará. Para mais informações acesse: [Conversão de roletas](https://tdn.totvs.com/pages/viewpage.action?pageId=802022183)

01Ações

As ações de roleta de venda oferecem a capacidade de criar regras que serão executadas pela roleta. Para que o sistema possa gerenciar o processo e a rotina de distribuição de Leads, algumas configurações devem ser realizadas:

## **Cadastro de Equipes**

---

O cadastro de equipes serve para organizar os membros de uma equipe que será utilizada na roleta, isto permite que os gestores atribuam os leads para cada membro da equipe. Isso contribui para uma distribuição linear e mais eficiente para cada corretor.  
  
Cada equipe poderá ser incluída com um nome definido pelo Gestor. A opção Ativo \ Inativo, possibilita disponibilizar ou não a utilização da roleta.

Ao incluir cada equipe, você terá, como ponto central, as seguintes informações: o nome da equipe, o dia da semana em que a equipe atua e os corretores com seus respectivos status. Em relação aos dias da semana, o administrador poderá selecionar os dias em que cada equipe receberá leads que entraram no sistema. O Período (horário de atendimento da equipe) é um novo recurso adicional que pode ser configurado no cadastro de equipes, permitindo a definição do horário de atuação da equipe.

* Nome da Equipe: Insira um título para identificar a equipe de vendas.
* Ativo: Por padrão a equipe de vendas será criada no status "Ativo". Este status pode ser alterado para "Inativo" no momento do cadastro.
* Imobiliária: Informe o nome da imobiliária à qual a equipe de vendas está vinculada, se aplicável.
* Corretor: Insira o nome do corretor responsável pela equipe, que atuará na distribuição dos Leads (poderá selecionar mais de 1 registro)
* Dias da semana: Selecione os dias da semana nos quais a equipe estará disponível para a roleta parametrizada. Isso permitirá que o sistema direcione os Leads para essa equipe nos dias selecionados.
* Período:  Indica os horários de atendimento da equipe. A atuação da equipe estará limitada aos dias e horários especificados neste campo, portanto, é necessário informar um período compatível com a demanda.
* Ordenar Corretores: Permite a ordenação e inativação de corretores neste espaço. Para reordenar os corretores basta clicar e arrastar os mesmos para as posições apropriadas. Para inativar um corretor da equipe, basta clicar no botão "Ativo", que passará a ser "Inativo". O mesmo procedimento pode ser feito para ativar um corretor na equipe.  
  **Observação:** Caso seja inserido um novo corretor na roleta após o primeiro giro, esse corretor não receberá Leads enquanto a roleta estiver em execução.  
  Somente participam da distribuição os corretores que já estavam cadastrados antes do giro inicial.
* **Exemplo prático:**

  + Antes do giro inicial, estavam cadastrados **Corretor 01** e **Corretor 02**.
  + A roleta realiza o primeiro giro e começa a distribuir Leads entre eles.
  + Após isso, é incluído o **Corretor 03**.
  + Nesse caso, o **Corretor 03** não receberá Leads, pois ele entrou somente depois que a roleta já havia iniciado o primeiro giro.

Ao preencher esses dados e salvar as configurações, a nova equipe será criada e poderá ser utilizada na configuração da roleta de vendas, associando-a aos dias disponíveis para atendimento e distribuição de Leads.

**Lista de Equipes** permite habilitar quais equipes estarão ativas para a roleta que está sendo parametrizada. Nessa tela, você terá as seguintes opções de gerenciamento:

* Ativar: Ao ativar uma equipe nesta lista, você poderá habilitá-la para associá-la em uma determinada roleta. Isso significa que os Leads serão distribuídos para essa equipe de vendas de acordo com as regras estabelecidas na roleta.
* Editar equipe: Caso seja necessário fazer alguma alteração nas configurações da equipe, você poderá selecioná-la na lista e realizar as edições necessárias, como a localização, imobiliária, corretor ou os dias disponíveis.
* Excluir equipe: Caso uma equipe não esteja mais em uso ou não seja necessária para a roleta, você pode removê-la da lista por meio da opção de exclusão.

Observação: estar ativo na equipe e participar da ordenação da roleta não garante, por si só, que o corretor receberá todos os leads. A distribuição também depende do acesso do usuário ao empreendimento do lead.

## **Cadastro de roletas**

---

O cadastro de roletas serve para organizar e gerenciar a distribuição ordenada de clientes em uma equipe. Através desse cadastro, é possível designar cada equipe para receberem leads (clientes em potencial) de forma ordenada e eficiente. Esse processo inclui informações como qual será a equipe que será utilizada na roleta,  tempo de espera (podendo ser configurado por minutos e horas), a origem (que refere-se a mídia), data de entrada do lead no sistema, e o empreendimento que será atribuido a esta roleta.

* Título: Insira um título para identificar a roleta de venda.
* Ativo: Por padrão a roleta de vendas será criada no status "Ativo". Este status pode ser alterado para "Inativo" no momento do cadastro. O sistema permitirá o cadastro de uma roleta inativa, porém a mesma não será considerada nos fluxos e giros de corretores. Esta roleta poderá ser ativada posteriormente através da tela de edição.
* Equipe: Selecione as equipes responsáveis pela distribuição dos Leads, que farão parte desta roleta.
  + *Importante: Ao selecionar várias equipes o sistema automaticamente irá compor a lista de ordenação de equipes no cadastro da roleta. Neste momento também é possível ativar ou desativar uma determinada equipe nesta lista, clicando no botão "Ativo". Para ordenar as equipes, basta clicar e arrastar o cadastro.*
  + *Não será possível associar a nova roleta uma equipe no status "Inativo".*
* Tempo de espera: É necessário escolher o tempo de espera antes de redirecionar o Lead para a próxima etapa. Selecione entre minutos ou horas.
* Dados do Lead: Informe a origem do Lead (midias) e a data de entrada do Lead.
* Empreendimento: Selecione os empreendimentos que farão parte desta roleta. Não será possível associar o mesmo empreendimento em roletas diferentes e ativas no sistema. Entretanto o mesmo empreendimento pode ser associado em roletas inativas.
* Ordenar Equipes: Permite a ordenação e inativação de equipes neste espaço. Para reordenar as equipes basta clicar e arrastar as mesmas para as posições apropriadas. Para inativar uma equipe, basta clicar no botão "Ativo", que passará a ser "Inativo". O mesmo procedimento pode ser feito para ativar uma equipe.

**Lista de roletas** permite que o gerente selecione as roletas que estarão ativas no sistema. Nessa tela, o gerente terá as seguintes opções:

* Editar roleta: Ao selecionar uma roleta específica da lista, o gerente poderá efetuar alterações nas configurações, como título, equipe, tempo de espera, dados do Lead, entre outros. Além disso, nesta tela, é possível visualizar as Equipes ativas para esta roleta. Observe que existe um botão que indica o status atual dessa equipe (Ativo ou Inativo). Esse status reflete a decisão de mantê-la ativa ou desativada, de acordo com a gestão da roleta.
* Ativo: Neste botão podemos alterar o status da roleta de ativo para inativo e vice versa.
* Excluir roleta: O gerente terá a opção de remover uma roleta da lista caso ela não seja mais necessária ou esteja desativada.

**Importante:** Ao excluir uma roleta de vendas, os corretores que receberam leads nos giros anteriores continuarão com esses leads. Os leads não serão liberados ou redistribuídos para próximos giros após a exclusão da roleta. Caso o gestor deseje redistribuir esses leads, **a retirada (desvinculação) do corretor atual deverá ser feita manualmente** no cadastro de cada lead. Esta ação de exclusão da roleta não poderá ser desfeita.

Visão Geral

Na guia de visão geral, o gerente terá acesso a dados e números que fornecerão um resultado do cenário em relação aos leads em espera, atendidos, em atendimento, não atendidos e tempo médio para atendimento.   
Para extrair essas informações, é necessário preencher alguns campos disponíveis na visão:

* **Roleta:** Campo onde serão selecionadas as roletas cadastradas no sistema, podendo ser selecionado um ou mais registros;
* **Data:** Campo que filtra a data desejada para listar os dados.

Após a aplicação do filtro, os dados serão exibidos da seguinte forma::

**Leads em espera** referem-se aos prospects *que já possuem empreendimento informado em **seu cadastro** (menu Prospects > Perfil > campo: Empreendimento Procurado)* e estão aguardando o giro da roleta para distribuir cada um destes registros para cada corretor. A medida em que o giro da roleta for executado este valor será alterado.

**Leads em atendimento** fornece um panorama dos leads que já possuem corretores associados em seu cadastro atrvés do processo do giro da roleta e que tenham alguma informação incluída na timeline.

Na prática, ao realizar o giro da roleta será atribuido um corretor ao lead, em seguida, quando o corretor acessar o cadastro deste lead e modificar a time Line, o status do lead se torna "em atendimento".   
É importante observar que se o status do lead for alterado para "EM ATENDIMENTO" sem a associação de um corretor através do Giro da Roleta, o lead não receberá automaticamente um corretor na próxima rodada, sendo necessária a inclusão manual de um corretor no cadastro.  
*OBS: Para alterar um Lead para o status EM ATENDIMENTO será necessário em seu cadastro alterar ou incluir alguma informação em sua Time line: [Saiba mais: Pessoas - Time Line](https://tdn.totvs.com/pages/viewpage.action?pageId=701668855#M%C3%A3o-C_5)*

**Percentual em atendimento** fornece um percentual dos leads em atendimentos, este resultado trata-se da soma de todos os leads em atendimento, dividido pela soma de leads em espera, em atendimento e não atendidos multiplicado por 100.

**Aguardando atendimento** indicam leads que já se encontram associados a corretores, mas ainda aguardam o início do atendimento.

**Leads sem perfil :** Indica um lead que ainda não possui dados do empreendimento informado em seu perfil (localizado no menu prospect)

Por fim, o **tempo médio de atendimento** é um indicador de qualidade do atendimento aos leads. Esse indicador é calculado a partir do momento em que um lead entra em contato até o momento em que seu status é alterado para "ATENDIMENTO" em sua timeline. Um tempo médio de atendimento elevado pode indicar possíveis gargalos no processo ou a necessidade de treinamento adicional da equipe. Ao monitorar esse dado, o gerente pode identificar oportunidades para otimizar o tempo de resposta e garantir um atendimento mais rápido e eficaz.

O gerente visualizará uma tela semelhante a este exemplo abaixo:

Esteira de Atendimento

A opção **"Esteira de atendimento"** permite realizar filtros de acordo com alguns campos disponíveis.  Para que estes filtros funcionem, deve ser necessário executar ou agendar o processo de Giro da roleta, para que os atendimentos sejam distribuídos conforme as especificações das roletas.  
Essa visão gerencial permite que o gestor visualize a roleta numa forma simples e genérica, e entenda a posição dos leads e sua distribuição entre as equipes disponíveis. Abaixo uma descrição dos campos disponíveis para filtro:

1. **Roleta:** Selecione a roleta de venda específica que será utilizada para o direcionamento dos atendimentos. Essa roleta pode conter regras e critérios predefinidos para a distribuição dos Leads.
2. **Equipe:** Escolha a equipe de vendas que será responsável pelo atendimento dos Leads que seguirem essa esteira.
3. **Imobiliária:** Informe a imobiliária à qual o atendimento está relacionado, se aplicável. Isso pode ajudar a categorizar e organizar os atendimentos de acordo com a imobiliária específica.
4. **Empreendimento:** Insira o nome ou identificador do empreendimento ao qual o atendimento está relacionado, caso exista. Isso pode auxiliar na segmentação dos atendimentos por empreendimento específico.
5. **Mídia:** Indique a origem do Lead ou a fonte da qual ele foi adquirido. Isso pode ser útil para rastrear a efetividade das fontes de aquisição de Leads.

Ao preencher esses campos e salvar as configurações na tela de "Esteira de atendimento", você estará filtrando os atendimentos com base nos critérios estabelecidos, como a roleta selecionada, equipe responsável, imobiliária, empreendimento e mídia.

## **Lead**

---

Na esquerda do card da esteira de atendimento, temos as informações do Lead. O objetivo dessa tela é permitir que o gestor analise e acompanhe o estado atual dos Leads na fila de atendimento.

Alguns detalhes que estarão disponíveis são:

1. **Nomes dos Leads:** Os nomes dos Leads serão apresentados individualmente, permitindo a identificação de cada um na fila.
2. **Limite de espera:** Será exibido o limite de tempo estabelecido para cada Lead na fila. Isso significa que o gestor poderá verificar por quanto tempo um Lead específico aguarda atendimento antes de ser redirecionado ou receber um acompanhamento adicional.
3. **Equipe responsável:** A equipe de vendas atribuída a cada Lead será indicada na tela. Dessa forma, o gestor poderá identificar qual equipe é responsável pelo atendimento de um determinado Lead.
4. **Data de entrada:** A data em que cada Lead entrou na fila será exibida, possibilitando uma análise do tempo que ele aguarda atendimento.
5. **Tempo de espera:** Será apresentado o tempo decorrido desde a entrada do Lead na fila. Essa informação permitirá ao gestor avaliar quanto tempo um Lead específico aguardou atendimento até o momento.

Com base nessas informações, o gestor poderá acompanhar de perto o fluxo de atendimento dos Leads, verificar os limites de espera, identificar a equipe responsável, analisar a data de entrada e o tempo de espera de cada Lead. Isso ajudará o gestor a tomar decisões estratégicas e garantir um bom gerenciamento da fila de atendimento.

## **Corretor**

---

Na direita do card, temos a informação do **Corretor,** o supervisor terá acesso aos nomes dos corretores que estão atuando em cada um dos leads. Essa visualização permitirá ao supervisor acompanhar quais corretores estão responsáveis por determinados leads na roleta de vendas. Além disso, o supervisor terá opções de mídia disponíveis para entrar em contato com os corretores, como telefone, mensagens e e-mail.

Essas opções de mídia servem como meios de comunicação direta entre o supervisor e os corretores, facilitando a coordenação, o suporte e o acompanhamento do trabalho realizado. Por exemplo:

1. **Telefone:** Exibe uma informação com o número de telefone do corretor, para realização de chamadas.
2. **WhatsApp**: Ao clicar neste botão, o supervisor poderá utilizar essa opção para enviar mensagens de texto através do WhatsApp. Para que essa opção funcione, é necessário estar logado no WhatsApp no mesmo browser onde está sendo visualizada a roleta.
3. **E-mail:** O supervisor poderá utilizar essa opção para enviar e-mails aos corretores, permitindo uma comunicação mais formal e detalhada sobre os leads ou outros assuntos pertinentes.

Essas opções de mídia disponíveis ajudam o supervisor a manter uma comunicação eficiente e direta com os corretores responsáveis pelos leads, facilitando a supervisão, a resolução de problemas e o suporte necessário durante o processo de atendimento e venda.

Fila do Lead

Uma fila de leads é como uma "lista de espera" inteligente que ajuda os gerentes a entender quanto tempo um potencial cliente (Lead) está aguardando para ser atendido. Essa fila oferece uma linha do tempo, mostrando quanto tempo o Lead passa na fila antes de ser atendido pelo corretor, e também apresenta o tempo total de espera desde o início.

Ao analisar essa fila, os gestores conseguem visualizar claramente quanto tempo cada Lead ficou esperando. Isso significa que podemos identificar áreas onde podemos ser mais rápidos, entender padrões de espera e tomar decisões para tornar o processo de atendimento mais eficaz.

Quando um corretor começa a atender um Lead (alterando seu status para EM ATENDIMENTO), o sistema automaticamente retira esse Lead da fila.

Giro da roleta

O giro da roleta é um processo que distribui leads (que não possuem corretor associado) para cada corretor configurado na equipe da roleta.

Esse processo severá ser realizado pelo supervisor logo após a conversão dos leads. Para os próximos "giros" de distribuição de leads, o processo pode ser agendado automaticamente, como veremos a seguir.

Para realizar o processo inicial, siga as etapas no Backoffice: acesse Gestão de Imóveis > Utilitários > Roleta de Leads > Giro da Roleta.

A primeira tela fornecerá informações relacionadas ao "giro da roleta".

Em seguida, ao avançar, você encontrará a tela onde poderá agendar esse processo em 3 camadas para execuções automatizadas, eliminando a necessidade de o supervisor executá-lo manualmente. Mais informações sobre o agendamento de processos podem ser encontradas na página específica: *[Agendamento de Processos - Job Server](https://tdn.totvs.com/pages/viewpage.action?pageId=4816357#Configura%C3%A7%C3%A3odoJobServernaLinhaRM-1.1AgendamentodeProcessos)*  
  
  
  
Ao final você visualizará a mensagem de conclusão do processo;

Se o giro for realizado e não houver nenhum lead para distribuição na roleta, o sistema informará que não encontrou nenhum lead para distribuir.

**Importante:**

Sempre que um Lead for atribuído a um corretor, o mesmo receberá um e-mail confirmando essa atribuição.

## **Visualizando a distribuição no Portal de imóveis:**

---

Após executar o giro no Backoffice, ao acessar o portal de imóveis e entrar no cadastro de Pessoas, você poderá visualizar a distribuição de leads feita para cada corretor associado àquela roleta.  
  
  
  
Ao editar cada um desses registros, o corretor estará vinculado a eles, permitindo que ele inicie suas atividades relacionadas a propostas.

Regras de Funcionamento da Roleta de Vendas

A Roleta de Vendas é uma ferramenta que distribui automaticamente os leads entre os corretores disponíveis. Para que ela funcione corretamente, algumas regras importantes precisam ser seguidas. Abaixo explicamos essas regras de forma simples e objetiva.  
  
**Regras básicas para o lead entrar na Roleta**

---

Para que um lead seja distribuído pela roleta, ele precisa cumprir todas as condições abaixo:  
 **Tempo de espera configurado**

* O sistema exige que exista um tempo de espera maior que zero cadastrado.
* Esse tempo é o período que o lead deve aguardar antes de ser distribuído.

**Sem corretor/dono do lead definido**

* O lead não pode ter nenhum corretor já associado como dono do lead.
* Se já houver alguém atribuído, o sistema entende que esse lead já está em atendimento. (e não entrará na roleta)

**Não estar em atendimento**

* Se algum registro de atendimento for gerado na timeline do lead (como anotações, ligações, mensagens, etc.), ele será considerado como "em atendimento" e ficará fora da roleta.   
  ***Mais informações:*** **[Time Line](https://tdn.totvs.com/pages/viewpage.action?pageId=701668855#M%C3%A3o-C_5)**

**Perfil do lead preenchido**

* Os campos "Mídia" e "Empreendimento Procurado", que ficam na aba "Perfil do Lead", devem estar preenchidos.
* Isso garante que o sistema tenha informações mínimas para distribuir o lead de forma inteligente.

**Reatribuição de lead com corretor atual**

---

Existe uma situação especial onde o lead já tem um corretor associado, mas ainda pode entrar na roleta. Isso acontece quando:

* O lead está em aguardando atendimento.
* Ele já atingiu o tempo de espera configurado.
* Ele atende a todas as outras regras listadas acima (exceto a de corretor vazio).

 Nesse caso, o sistema entende que o corretor atual não está atendendo o lead a tempo, e o lead pode ser redistribuído para outro corretor.

**Validação de acesso ao empreendimento durante o giro da roleta**

Durante a distribuição, além da ordem configurada na roleta, o sistema também valida se o corretor da vez possui acesso ao empreendimento do lead.  
Se o corretor não possuir permissão para atuar no empreendimento vinculado ao lead, ele não receberá a distribuição naquele giro. Nesse caso, o sistema continuará a busca pela próxima posição elegível da roleta, mantendo a integridade da ordenação configurada.

Recomendação: para evitar perda de oportunidades por restrição de acesso, avalie cuidadosamente a configuração de empreendimentos permitidos no cadastro do usuário.  
**Mais informações**: [**Imobiliárias**](https://tdn.totvs.com/pages/viewpage.action?pageId=656060917)Leads Integrados com RD Station

No caso do Portal de Imóveis integrado ao RD Station, além das regras padrão da roleta de leads, existem regras adicionais específicas para esses casos.  
  
Mesmo que o lead venha do RD Station, ele ainda precisa cumprir todas as regras gerais da roleta, como:

* Tempo de espera cadastrado.
* Não ter corretor associado (ou já ter ultrapassado o tempo de espera para possível troca).
* Não estar em atendimento.
* Campos de Mídia e Empreendimento Procurado preenchidos.

Além disso, os seguintes passos são obrigatórios para que a roleta funcione corretamente com os leads do RD Station:

* Sincronizar o Funil de Vendas
* Você precisa sincronizar o funil de leads e todas as suas etapas entre o RD Station e o sistema.
* Definir a Etapa Inicial no PI (Painel de Integração)
* Após sincronizar o funil, é necessário acessar o PI e definir qual etapa será considerada a etapa inicial no seu sistema. ***Mais informações:*****[Portal de Imóveis - Backend - Globais - Etapas do funil de leads](https://tdn.totvs.com/pages/viewpage.action?pageId=699798333)**
* Etapa Inicial é Obrigatória para Distribuição
* A roleta só atuará nos leads integrados com o RD Station que estiverem exatamente na etapa inicial definida. **Obs.:** A etapa inicial do RD Station CRM não poderá ter campos obrigatórios não preenchidos. Caso tenha campos obrigatórios não preenchidos nessa etapa, a roleta de vendas não distribuirá o lead para um corretor.
* Se o lead estiver em outra etapa, o sistema não irá distribuí-lo nem permitir troca de corretor.

👉 Resumindo: Para leads do RD Station entrarem na roleta, eles devem cumprir todas as regras normais da roleta e estar na etapa inicial configurada após a sincronização do funil.
