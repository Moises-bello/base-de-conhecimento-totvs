---
content_hash: 05f3e225304989d12cc62bf1fc5078050aae1f6c923a7913f07e73f076dfde30
fetched_at: '2026-06-29T00:11:43.123027+00:00'
page_id: '802022183'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Conversão de Roleta de Leads
  12.1.2402
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=802022183
version: 35
---

# **Conceito:**

---

A conversão da roleta de leads é um processo que garante a integração adequada dos dados de Roletas de Vendas existentes na visão anterior do portal para a nova roleta. Isso significa que, após realizar a conversão, ao acessar a nova roleta, o sistema terá importado todas informações de roletas e corretores parametrizadas na versão anterior.  
Para ter um melhor entendimento referente a utilização da roleta e suas funcionalidades acesse: [Pré-Venda - Roleta de Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=777274388)

---

.Pré Requisitos:

Para que a conversão da roleta de Leads seja realizada com sucesso, é necessário cumprir algumas pré-condições. Primeiramente, é fundamental possuir instalada a **versão 12.1.2402 (ou superior) do Backoffice**. Além disso, a base de dados do RM deve já ter o portal de Imóveis convertido para a base RM.   
Certifique-se de que essas etapas foram concluídas antes de prosseguir com o processo de conversão. Para obter informações adicionais e detalhes sobre a conversão do portal de Imóveis para a base RM, acesse: [Conversor de Base de dados do Portal de Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=770956085)  
**Importante:** A conversão da roleta de Leads só será executada se não houver nenhum registro de roleta inserido manualmente na nova visão de roletas. Se o processo conversão for solicitado com dados já presentes na base, uma mensagem de alerta será exibida para o usuário.

Realizando o processo de conversão:

Para que a opção da conversão da roleta de Leads seja apresentada para o usuário, será necessário disponibilizar as permissões em seu perfil para executar esta operação. Esta permissão disponibilizará no menu utilitários a opção para esta funcionalidade, que visualizaremos na proxima etapa;

Em seguida acesse o módulo Gestão de Imóveis e menu utilitários execute o icone Roleta de Leads e selecione : Conversão roleta;

Na primeira tela ao acessar o conversor, você encontrará informações relacionadas ao processo de conversão. Após compreender as instruções, basta selecionar a opção "Executar" para iniciar o processo.

 O processo de conversão será executado, exibindo o percentual de conclusão da importação;  
  
  
  
Ao final, o log de conversão será apresentado, contendo informações sobre a conclusão do processo.

**Importante:** Como já descrito anteriormente, a conversão da roleta de Leads só será executada se não houver nenhum registro de roleta inserido manualmente na nova visão de roletas. Se o processo conversão for solicitado com dados já presentes na base, uma mensagem conforme a imagem abaixo será exibida.

Após a conversão:

Após a convesão o acessar a nova roleta o sistema realizou a importação dos seguintes dados:  
  
**Lista de Equipes:**   
Cada equipe foi incluída utilizando o nome da Roleta cadastrada no Portal de Imóveis antes da conversão. A opção Ativo \ Inativo seguiu o mesmo critério existente antes da conversão.

Ao editar cada equipe, você verá, como ponto central da conversão, as seguintes informações: o nome da equipe, o dia da semana em que a equipe atua e os corretores com seus respectivos status. Em relação aos dias da semana, o administrador poderá selecionar a partir da roleta convertida os dias em que cada equipe receberá leads que entraram no sistema. O Período é um novo recurso adicional que pode ser configurado na nova roleta, permitindo a definição do horário de atuação da equipe

**Lista de Roletas:**

Esta lista mostrará as roletas que foram convertidas, cada uma com seu status, que pode ser Ativo ou Inativo. Quando editada, o supervisor poderá acessar as configurações desta roleta, permitindo a modificação do seu status e também a ativação ou desativação da equipe associada a ela.

**Importante:** O sistema não controlará o tempo desta roleta, já que, antes da conversão, a ordem de distribuição de corretores era realizada pela ordem de entradas de leads e distribuidas na ordem de cada corretor configurado no cadastro de roletas.

Após concluir essas importações, é hora de girar a roleta para que a distribuição de leads seja feita aos corretores apropriados. Para entender melhor esse procedimento, consulte o link a seguir: [Pré-Venda - Roleta de Vendas](https://tdn.totvs.com/pages/viewpage.action?pageId=777274388)

Giro da roleta (distribuição de Leads)

O giro da roleta é um processo que distribui leads (que não possuem corretor associado) para cada corretor configurado na equipe da roleta.

Esse processo severá ser realizado pelo supervisor logo após a conversão dos leads. Para os próximos "giros" de distribuição de leads, o processo pode ser agendado automaticamente, como veremos a seguir.

Para realizar o processo inicial, siga as etapas no Backoffice: acesse Gestão de Imóveis > Utilitários > Roleta de Leads > Giro da Roleta.

A primeira tela fornecerá informações relacionadas ao "giro da roleta".

Em seguida, ao avançar, você encontrará a tela onde poderá agendar esse processo em 3 camadas para execuções automatizadas, eliminando a necessidade de o supervisor executá-lo manualmente. Mais informações sobre o agendamento de processos podem ser encontradas na página específica: *[Agendamento de Processos - Job Server](https://tdn.totvs.com/pages/viewpage.action?pageId=4816357#Configura%C3%A7%C3%A3odoJobServernaLinhaRM-1.1AgendamentodeProcessos)*  
  
  
  
Ao final você visualizará a mensagem de conclusão do processo;

Se o giro for realizado e não houver nenhum lead para distribuição na roleta, o sistema informará que não encontrou nenhum lead para distribuir.

# **Visualizando a distribuição no Portal de imóveis:**

---

Após executar o giro no Backoffice, ao acessar o portal de imóveis e entrar no cadastro de Pessoas, você poderá visualizar a distribuição de leads feita para cada corretor associado àquela roleta.  
  
  
  
Ao editar cada um desses registros, o corretor estará vinculado a eles, permitindo que ele inicie suas atividades relacionadas a propostas.
