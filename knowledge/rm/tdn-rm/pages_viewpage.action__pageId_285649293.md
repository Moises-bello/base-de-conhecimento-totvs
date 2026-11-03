---
content_hash: 894ca77aedc3a3090b42d371dc46f8e095223f6f4a78b728c163b4d5dcf35d1a
fetched_at: '2026-06-29T00:08:38.361085+00:00'
page_id: '285649293'
product: rm
source: tdn-rm
title: "3.\tMódulo PDC – Portal do Cliente"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285649293
version: 1
---

O atendimento a cliente para o Grupo Casitas está baseado na entrega de chaves e Garantias. Ambos os recursos deverão ser desenvolvidos no Winform e Web

 A seguir descreveremos cada uma das demandas.

**1.1.** **Atendimento ao cliente**

**1.1.1.** **Entrega de Chaves**

 A entrega de chaves pode ser feitas somente depois da venda efetivada e assinada, por este motivo a equipe de atendimento deve visualizar quais vendas que devem entregar as chaves, mas para isso devem verificar:

A subunidade deve ter CVT, se não tiver deve solicitar a uma área especifica a liberação do CVT.

Antes de entregar a subunidade deve ser feita uma verificação (checklist) para verificar se a subunidade está com todos os itens necessários, como pintura em bom estado, lâmpadas e brindes que foram *prometidos* na proposta.

Se o brinde não estiver disponível, deve solicitar a uma área espeficica.

Se a subunidade necessitar de uma nova limpeza, pintura, etc terá que solicitar a outra área.

Depois da subunidade verificada e estando apta a entrega é emitido o DTC.

**Agenda**

A entrega da subunidade deve ser agendada pela equipe de atendimento e para isso devem ser criados os seguintes recursos:

* *“Entregadores”*, para que se possa atribuir uma agenda;
* Agenda, onde possam ser parametrizados dias semanais especificos onde se possam fazer as entregas, além de um calendário par feriados e dias úteis. Depois de parametrizada a agenda deve permitir marcar por *“Entregadores”* os dias e horários que farão a entrega. Neste agendamento o atendente deve saber os dados do cliente e da subunidade. (ex: Nome, Telefone, e-mail, endereço da subunidade.)

Os agendamentos devem ter um tempo minimo para a entrega (hoje é de 48 horas, mas pode alterar) portanto há necessidade de parametrizar quanto tempo antes (días úteis ou horas ) devem ser agendadas as entregas de chaves.

Restrições

* Uma entrega de chave só pode ser agendada se a Proposta de Venda estiver assinada;
* Só pode ser entregue as chaves se tiver CVT, se a venda estiver assinada mas se não tiver CVT gerado, deve disparar solicitação de CVT para o setor de Obra. O Setor de Obra deve ger o CVT e marcar no sistema que está criado. Criar processo que permita marcar que varios CVTs foram criados de uma vez, pois em caso de edificios libera-se este documento para todas as subunidades.

A área de atendimento deve poder ainda:

* Solcitação para entrega de Kits, como lampadas, etc.
* Solcitação para entrega brindes, como ar condicionado, grades de proteção e outros itens que podem ter sido estabelecidos na venda como promoção.
* Solicitação de outros manutenções, como revisão de pintura

Cliente pode não aceitar a vivenda  e se isso acontecer debe ser registrado e rever  check list e registra o pq não aceitou, pois geralmente é um problema.

Se o cliente aceita a subunidade, assina o RET e finaliza a entrega no sistema.

**1.1.2.** **Garantias**

O atendimento a cliente também deve permitir que sejam tratadas as garantias, onde os clientes entram em contato com o Grupo Casitas e fazem a solicitação de reparos na subunidade. O atendente deve ser capaz de identificar se a solicitação está coberta por uma garantia, e somente neste caso será feito o reparos, mas há exceções que serão tratadas mais adiante neste documento.

 Para que o atendimento seja feito será necessário que se identifiquem os seguintes dados:

* Atendente, que recebe o e-mail, ligação, whatsapp e que registra no sistema a solicitação do cliente;
* Coberturas, deve ser feito um cadastro prévio de coberturas que posteriormente serão associadas a contratos de venda. Estas coberturas podem ser um período de uso podendo ser desativada.
* Tipo de Manutenção, catálogo de possíveis serviços que serão executados para cada cobertura.

Depois de criados os pre cadastros, as coberturas poderão ser associadas ao empreendimento/ subunidade e assim que uma venda for feita automaticamente esta cobertura será atribuída a ela. Por cobertura entendemos um conjunto de itens que podem ter tempos diferentes. *Ex: Cobertura elétrica, cobertura hidráulica, cobertura estrutural, etc.*

**Controle de Cobertura no cadastro do Contrato e da Venda**

Deve ser criado um cadastro associado a venda que identifica quais são as coberturas previstas para cada contrato de Venda e por quanto tempo. Este cadastro pode ser alimentado pelo processo de criação de venda, ou manuamente para permitir uma carga inicial.

As coberturas podem ter tempos diferente e sua data base para o calculo por ser diferente, por isso deve ser criado um parâmetro para informar qual será a data base para calculo da garantia.

**Agenda de Vistoria**

Para atender a garantia será necessária a criação de uma agenda com dois tipos, que são: Agenda de Vistoria e Agenda de Manutenção. Nesta agenda poderá haver um atendente para cada tipo ou o mesmo atendente para os dois tipos. Em ambos os casos há a necessidade de delimitar dias da semana que podem ser agendadas as visitas, como por exemplo, segunda – quarta- sexta, e com faixas de horários.

**Atendimento da Garantia**

Quando o cliente entra em contato por telefone ou e-mail o atendente deve verificar se a solicitação tem cobertura, para isso deve haver recurso que permita localizar o cliente usando filtros, como:

* Nome do cliente;
* Contrato de Venda;
* Subunidade;
* Endereço da Subunidade;

Depois de localizado o cliente e sua subunidade, o atendente terá acesso as coberturas e seus prazos. Constatando que a solicitação tem procedência e está coberto pela garantia, o atendente deve iniciar o atendimento e agendar uma vistoria no sitema para um técnico,  que por sua vez poderá consultar sua lista de agendamentos.

Todo atendimento está associado ao centro de custo da respectiva subunidade.

Durante a vistoria o técnico deve fotografar os problemas relatados e registrar no sistema o que viu além de anexar as fotos, informando se o relato procede ou não. Caso o técnico não encontre o cliente em casa, deve registrar a ausência no sistema, que por sua vez retorna o chamado para o reagendamento.

Após a confirmação da necessidade de manutenção coberta pela garantia, um novo agendamento deve ser feito, mas desta vez para a manutenção do problema. O sitema deve permitir a identificaçao de um ou mais problemas previamente cadastrados como defeitos, e relatos descritivos, bem como todo material usado para o conserto deve ser registrado, bem como a quantidade de horas gastas. Se em algum dos agendamentos da manutenção o cliente se ausentar, deve ser registrado no sistema e um novo agendamento deve ser feito até o termino no serviço.

Este mesmo processo de manutenção pode ser executado para problemas fora da garantia, se assim autorizado por usuário com este perfil.

Após concluída a manutenção deve haver o registro fotográfico da solução e estas fotos devem ser anexadas ao atendimento, so depois a demanda é encerrada.

As solicitações de manutenções também podem ser feitas pelo portal do cliente.

Não há restrição para o número de agendamento de vistoria ou visitas de manutenção.

*Integração com modulo de assitencia técnica do Protheus. Com apuração de custos**?*

**Perda de Garantia**

Durante uma visita de vistoria pode ser constatado que houve perda da garantia, por mau uso do bem, como por exemplo, alteração estrutural, alteração elétrica, etc, e neste caso o técnico deve comunicar ao cliente, registrar no atendimento o ocorrido através de um motivo pre cadastrado que permita apuração posterios, e com um descritivo livre, e somente após isso poderá encerrar o atendimento.

Para casos como este é importante o registro fotográfico da alteração que ocasionou a perda da garantia e anexa-las ao atendimento.

**1.1.3.** **Equipe de Qualidade**

A equipe de de qualidade deve ter acesso a todas as subunidade que tenha a necessidade de revisões ou geração de CVTs. A prioridade é a data de entrega e ordem crescente de solicitação, assim que a revisão da subunidade for feita, o atendimento desta equipe deve indicar a data de conclusão do CVT ou da revisão, para que a subunidade possa retornar a equipe de entrega.

*Dados que devem ser extraídos em formato de **relatórios**.:*

* *Casas como mesmo problema varias vezes*
* *Casas com varios problemas*
* *Um problema em várias casas*
* *Problemas por modelo de casa*
* *Problemas / defeitos que mais ocorrem*

**PONTO DE ATENÇÃO**

Para consultar a cobertura da garantía de vendas ocorridas antes da implantação do sistema será necessária uma carga e dados para
