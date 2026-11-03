---
content_hash: 1e5a12c5f439e77387c3d22bee7c9a5760dd253ca5239df9b1337967d9056b74
fetched_at: '2026-06-29T00:11:40.068383+00:00'
page_id: '794362068'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Sincronismo portal de Imóveis
  12.1.2402
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=794362068
version: 35
---

---

## **Conceito**

A sincronização desempenha um papel essencial no processo de integração dos registros entre o sistema RM e o Portal de Imóveis. Sua importância fundamental está na capacidade de buscar e atualizar dados diretamente no sistema RM, integrando esses registros de forma consistente nos cadastros do Portal de Imóveis.   
Esse procedimento assegura que as informações permaneçam constantemente atualizadas e consistentes entre os dois sistemas, viabilizando, assim, uma integração eficiente e altamente necessária. Este material tem como objetivo guiar você por esse processo de sincronização, proporcionando uma compreensão e um uso eficaz dessa funcionalidade indispensável para a operação integrada de ambos os sistemas.  
  
É possível sincronizar os seguintes dados do RM, seja de forma completa ou individual:  
01. Empreendimentos   
02. Blocos   
03. Unidades   
04. Vagas   
05. Tabela de Preço   
06. Tabela de Preço (Preço unidades) ***\**** *veja aviso ao final da página [Execução da Sincronização](https://tdn.totvs.com/pages/viewpage.action?pageId=794362068#1--1694457321)*   
07. Modalidade Venda   
08. Componente x Modalidade   
09. Modalidade x Tabela de Preço   
10. Região   
11. Mídia   
12. Profissão   
13. Comunhão de Bens   
14. Vendas Distratadas   
15. Cidades   
16. Parâmentros   
17. Aditivo de Troca de Unidade

---

1Pré-Requisitos:

Antes de realizar a sincronização no RM é importante considerar alguns pré-requisitos técnicos e de permissões:

**Permissões de Acesso:** É necessário disponibilizar permissões específicas para que os usuários tenham acesso à funcionalidade de sincronização. Os administradores do sistema devem assegurar que os usuários envolvidos tenham autorização para visualizar e utilizar a opção de sincronismo no menu Utilitários.

Após a disponibilização das permissões, o usuário irá visualizar a opção "Sincronismo Portal Imóveis" no menu "Utilitários".

**Observação:**  
Para que a sincronização ocorra corretamente, é necessário que **existam empreendimentos ativos no Portal de Imóveis**.

Somente com empreendimentos ativos o processo de sincronização irá considerar e integrar as entidades relacionadas a eles.

Aumento do Tempo de execução

**DBSCommandTimeout:** Esta configuração permite ajustar o tempo máximo que uma consulta SQL pode ser executada antes de ser interrompida devido a um timeout. O timeout é um mecanismo de segurança que evita que consultas demoradas afetem negativamente o desempenho do sistema ou causem bloqueios prolongados.  
Esta TAG deverá ser incluída na edição do arquivo de RM Host: no ambiente onde o Sistema encontra-se instalado.

`<``add` `key``=``"DBSCommandTimeout"` `value``=``"600"` `/>`

---

Execução da Sincronização

Para que possamos obter um entendimento completo sobre o processo de sincronização, vamos utilizar um exemplo prático que inclui o registro de um novo empreendimento por meio do cadastro de empreendimentos via RM. Ao final, poderemos observar a sincronização em ação, tornando esse empreendimento disponível no portal de imóveis.

Inicialmente, um novo empreendimento é adicionado ao sistema. Neste ponto, todas as informações relevantes sobre o empreendimento, como localização, características, preço e disponibilidade, são inseridos no cadastro. Em seguida salve esta inclusão.

Após a inclusão do empreendimento no RM, o processo de sincronização já poderá ser iniciado. Esse processo é realizado para garantir que todas as informações incluidas ou atualizadas sobre o empreendimento sejam sincronizadas de forma eficiente para o portal de imóveis.

## **Para realizar a sincronização, siga os seguintes passos:**

---

1. Acesse o menu utilitários > Sincronismo portal imóveis. Na visão aberta selecione processos > Sincronização do portal de imóveis 

2. Inclua um *novo filtro* que permita listar as tarefas existentes que você deseja selecionar para a sincronização;  
  
  
  
3. Selecione os itens específicos que você deseja sincronizar, em seguida avançar para prosseguir com o processo de sincronização;   
Ao sincronizar suas tarefas, *considere a possibilidade de selecionar todas elas, a fim de manter a integridade e a precisão dos dados em seu sistema* que serão sincronizados. Isso contribuirá para um melhor desempenho e uma gestão mais eficaz de suas operações.  
  
Neste exemplo, optamos por destacar a seleção de "Empreendimentos" exclusivamente como uma ilustração para tornar a explicação mais clara.  
  
  
  
4. Selecione a tarefa empreendimento e clique em avançar;

***Observação:*** O processo também pode ser agendado via job, como detalhado na imagem a seguir. Além disso, informações adicionais serão destacadas ao final desta página para melhor entendimento;

5. Ao final, as informações referentes aos itens selecionados para sincronização serão apresentadas. Neste exemplo, realizamos a sincronização do empreendimento, e ao término do processo, recebemos a notificação de conclusão com sucesso.  
  
  
  
6. Visualização no Portal de Imóveis: Após a sincronização realizada, o novo empreendimento é incorporado ao portal de imóveis, tornando-se visível para os usuários corretores que acessam o portal.   
  
  
  
Este exemplo prático demonstra como a sincronização de dados desempenha um papel importante na manutenção de informações atualizadas e acessíveis entre os sistemas. Através desse processo, garantimos que as informações sobre os empreendimentos sejam consistentes e disponíveis no portal de imóveis, promovendo assim uma experiência mais eficaz para os usuários e aprimorando a eficiência operacional.

Ao selecionar a Tarefa **tabelapreco\_unidade** para sincronização, durante o processo, você notará que as tarefas ***Unidades,* *Tabela de Preços e Tabela de Preços (unidades)*** estarão pré-selecionadas. No entanto, você pode desmarcá-las se preferir. Isso ocorre porque a tabela de preços (unidades) depende da unidade e da tabela de preços, mas a escolha de sincronização é flexível.

---

Agendamento via JOB

Além da disponibilização da funcionalidade de sincronização, a partir da versão 12.1.2402, também é possível realizar o agendamento deste serviço através de um Job. Isso possibilita que a sincronização seja executada de tempos em tempos, conforme definido pelo usuário administrador. Este recurso oferece maior flexibilidade e automação no processo de integração.   
Para configurar o agendamento via Job, siga os passos disponibilizados neste material: *[Agendamento de Processos - Job Server](https://tdn.totvs.com/pages/viewpage.action?pageId=4816357#Configura%C3%A7%C3%A3odoJobServernaLinhaRM-1.1AgendamentodeProcessos)*

***Sugerimos que o agendamento seja configurado para execução de 12 em 12 horas***No exemplo a seguir, apresentamos uma maneira de realizar essa configuração sugerida.  
  
1. No menu "Utilitários", ao clicar no ícone "Sincronismo do portal de imóveis", na visão apresentada, clique em "Processos" (selecione a opção: "Sincronização do portal de imóveis").

2. Inclua um *novo filtro* que permita listar as tarefas existentes que você deseja selecionar para a sincronização;  
  
  
  
3. Selecione os itens específicos que você deseja sincronizar, em seguida avançar para prosseguir com o processo de sincronização;   
Neste exemplo, optamos por destacar a seleção de "Empreendimentos" exclusivamente como uma ilustração para tornar a explicação mais clara.  
  
  
  
4. Selecione a tarefa que deseja sincronizar, clique em "Avançar";

No entanto, é importante ressaltar que, *para alcançar a máxima consistência de dados* durante o processo de sincronização, é *recomendável selecionar todas as tarefas disponíveis.* Isso garantirá que todos os aspectos relevantes do sistema possam ser atualizados no portal, evitando discrepâncias de informações.

5. Na tela apresentada referente ao agendamento, destacamos duas informações técnicas importantes.   
*A primeira delas é a "Hora da Execução" (1ª Execução)*, que representa o horário programado para a primeira execução da tarefa.   
*A segunda informação é a configuração de "Repetir a execução"*, onde foi selecionada a opção diária e informado o horário das 12 horas. Isso indica que a partir de hoje, o serviço de sincronização será realizado automaticamente a cada 12 horas, de acordo com essa configuração técnica.  
  
  
  
6. Para visualizar o serviço agendado, acesse o menu "Ambiente" e clique em "Gerenciamento de Jobs". Após isso, os dados dos serviços agendados na base de dados serão listados na tela. Basta filtrar o processo de sincronização do Portal de Imóveis. Abaixo, estão duas telas: a primeira mostra o menu de acesso aos serviços agendados, e a segunda exibe o agendamento selecionado.  
  
  
  
Entenda como o serviço é descrito na tela para visualização:

1. **Nome do processo:** Este é o nome ou identificador da tarefa que foi agendada. Ele descreve a natureza ou finalidade da tarefa que será executada automaticamente de acordo com o agendamento.
2. **Usuário que criou o agendamento:** Indica o nome ou identificação do usuário que criou o agendamento. Isso ajuda a rastrear quem configurou a tarefa de agendamento e é útil para fins de responsabilidade.
3. **Horário de execução:** Este é o horário programado para que a tarefa agendada seja executada automaticamente. É o momento em que a tarefa será ativada de acordo com as configurações definidas.
4. **Status de execução:** Este campo indica o estado atual da execução da tarefa agendada. Quando estiver vazio, significa que a tarefa ainda não foi executada. Quando exibe "OK", significa que o job foi executado com sucesso em seu horário agendado. Esse status é uma maneira de monitorar e verificar se a tarefa está sendo executada conforme o planejado.

7. Após a execução do processo, observe que o campo Status apresenta a informação "OK", significando que a execução do serviço foi concluída.

Outra informação mais detalhada que também pode ser visualizada pelo usuário é acessada ao clicar duas vezes sobre o serviço executado. Nesse momento, a tela apresentará um resumo da execução, incluindo dados relativos à hora de início e término, bem como outras informações complementares relacionadas a esse serviço.

   

---
