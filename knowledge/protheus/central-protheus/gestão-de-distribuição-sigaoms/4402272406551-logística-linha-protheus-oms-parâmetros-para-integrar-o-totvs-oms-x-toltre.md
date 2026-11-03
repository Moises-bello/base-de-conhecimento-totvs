---
article_id: 4402272406551
category: Gestão de Distribuição (SIGAOMS)
content_hash: 4c7f8b29789a2e1b14044ae169637f8e71204531303b069dda96d6ee8d44e3ee
fetched_at: '2026-06-28T22:45:49.989131+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Parâmetros  para integrar o TOTVS OMS x
  TOL/TRE
type: support-article
updated_at: '2022-10-20T18:56:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-para-integrar-o-TOTVS-OMS-x-TOL-TRE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:09:12min**  
**Dúvida**Quais os **Parâmetros** são utilizados para integrar o **TOTVS OMS** x **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões.  
  
**Solução**Para o correto funcionamento da integração, será necessário configurar os **Parâmetros** no **TOTVS OMS.**Acesse o menu **Atualizações/Cockpit Logístico/Parâmetros Integração - OMSXCPL1:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Descrição** | **Parâmetro** | **Opções** | **Valor Integração** | **Validação** |
| Permite enviar quantidades não liberadas para o **TOL/TRE**? | Ao ativar esse parâmetro o **TOTVS OMS**  permitirá a integração de pedidos sem liberação de estoque com o **TOL/TRE**. Com isso, todas as informações serão integradas com base na tabela SC6-Itens do Pedido de Venda. | **MV\_CPLPELB** | 1 - Sim 2 - Não | 2 - Não - padrão |  |
| Embarcador | Código de um Embarcador do **TOL/TRE**. Todos os produtos integrados do **TOTVS OMS** para o **TOL/TRE** serão relacionados a um mesmo Embarcador no **TOL/TRE**, pois no **TOTVS OMS** a relação variável de produto x cliente é utilizada opcionalmente, apenas na importação de Notas Fiscais de Cliente pelo **EDI**. | **MV\_CPLEMB** |  | Conforme cliente | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT =1** |
| Invólucro Padrão | Código de um Invólucro-embalagem do **TOL/TRE**. Todos os itens de Pedidos de Transporte recebidos do **TOTVS OMS** no **TOL/TRE** serão associados a esse invólucro, pois não há uma entidade no **TOTVS OMS** que corresponda exata e obrigatoriamente a esse dado do **TOL/TRE**.É recomendável informar um invólucro cujas medidas sejam obtidas do item do pedido, esta característica é parametrizada no **TOL/TRE**. | **MV\_CPLINV** |  | Conforme cliente |  |
| Origem dos Dados | Define o nome do ERP que origina os dados enviados ao **TOL/TRE**. | **MV\_CPLIDS** |  | Deve ser informada a fonte de dados criada dentro do **TOL/TRE**. Exemplo: **Protheus** | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT = 1** |
| *E-mail* do Administrador | *E-mail* do administrador para notificações de falha de conexão. | **MV\_CPLMAL** |  | Conforme cliente |  |
| Endereço **Webservice** de Autenticação | Endereço do **Webservice** de Autenticação do **TOL/TRE**. Este endereço fornecerá um **token** de autenticação, que deverá ser utilizado nas requisições efetuadas ao **TOL/TRE**, quando este estiver parametrizado para solicitar autenticação. | **MV\_CPLUAUT** |  | Conforme cliente  Exemplo:  http://<ip ou nome>:<porta>/cockpit-gateway/ws/authentication |  |
| Endereço **Webservice**  Monitoramento | Endereço do **Webservice** de Monitoramento do **TOL/TRE**. É necessário informar  somente quando a integração com o monitoramento encontra-se ativa. Mais detalhes avaliar com a Equipe do **TOL/TRE**. | **MV\_CPLURL** |  | Conforme cliente |  |
| Endereço **Webservice**  Planejamento Viagem | Endereço do **Webservice**do módulo de Planejamento do **TOL/TRE**. | **MV\_CPLURL** |  | Conforme cliente  Exemplo: http://<ip ou nome>:<porta>/cockpit-gateway/integration/services | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT = 1** |
| Endereço **Webservice** de Autenticação | Endereço do **Webservice** de Autenticação do **TOL/TRE**. Este endereço fornecerá um **token** de autenticação, que deverá ser utilizado nas requisições efetuadas ao **TOL/TRE**, quando este estiver parametrizado para solicitar autenticação. | **MV\_CPLUAUT** |  | Conforme cliente  Exemplo: http://<ip ou nome>:<porta>/cockpit-gateway/ws/authentication |  |
| Usuário de Autenticação do **Webservice** | Usuário utilizado para efetuar *login* no **TOL/TRE**, para obtenção do **token**. | **MV\_USRCPL** |  | Conforme cliente | Deve ser obrigatoriamente preenchido quando possuir URL de autenticação. |
| Senha de Autenticação do **Webservice** | Senha do usuário utilizado para efetuar *login* no **TOL/TRE**, para obtenção do **token**. | **MV\_PSWCPL** |  | Conforme cliente | Deve ser obrigatoriamente preenchido quando possuir URL de autenticação. |
| Quantidade de Horas para Considerar que o **Token**Expirou | Indica a quantidade de horas que devem ser consideradas para que um **token** esteja expirado. Enquanto este limite não for atingido, o mesmo **token** recebido na primeira solicitação será reutilizado para envio das próximas mensagens. | **MV\_EXPTOK** |  | Conforme cliente |  |
| Regional | Regional enviada para o **TOL/TRE**. | **MV\_CPLREG** |  | Conforme cliente | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT = 1** |
| Embarcador | Código de um Embarcador do **TOL/TRE**. Todos os produtos integrados do **TOTVS OMS** para o **TOL/TRE** serão relacionados a um mesmo Embarcador no **TOL/TRE**, pois no **TOTVS OMS** a relação variável de produto x cliente é utilizada opcionalmente apenas na importação de Notas Fiscais de Cliente pelo **EDI**. | **MV\_CPLEMB** |  | Conforme cliente | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT = 1** |
| Categoria de Produto? | Para o **TOL/TRE**, categorias de produto são agrupamentos relevantes de produtos com características logísticas semelhantes. Com esse parâmetro é possível determinar se a categoria dos produtos integrados do **TOTVS OMS** para o **TOL/TRE**, sendo que:  1 - Grupo Produto: será o código do grupo do produto do **TOTVS OMS**.  2 - Padrão **TOL/TRE**: será informada por alteração manual, em cada produto no **TOL/TRE**. Com essa opção é necessário cadastrar as Categorias de Produtos no **TOL/TRE** com os mesmos códigos dos Grupos de Produtos do **TOTVS OMS**, pois não há **Webservice**de integração para essa tabela. | **MV\_CPLCAT** | 1 - Grupo Produto  2 - Padrão  **TOL/TRE** | 2 - Padrão **TOL/TRE** |  |
| Invólucro Padrão | Código de um Invólucro-embalagem do **TOL/TRE**. Todos os itens de Pedidos de Transporte recebidos do **TOTVS OMS** no **TOL/TRE** serão associados a esse invólucro, pois não há uma entidade no **TOTVS OMS** que corresponda exata e obrigatoriamente a esse dado do **TOL/TRE**. É recomendável informar um invólucro cujas medidas sejam obtidas do item do pedido, esta característica é parametrizada no **TOL/TRE**. | **MV\_CPLINV** |  | Conforme cliente |  |
| Origem dos Dados | Define o nome do ERP que origina os dados enviados ao **TOL/TRE**. | **MV\_CPLIDS** |  | Deve ser informada a fonte de dados criada dentro do **TOL/TRE**. Exemplo: Protheus | Deve ser obrigatoriamente preenchido quando **MV\_CPLINT = 1** |
| *E-mail* do Administrador | *E-mail* do administrador para notificações de falha de conexão. | **MV\_CPLMAL** |  | Conforme cliente |  |
| UM a Considerar? | Este parâmetro permite indicar a unidade de medida a ser considerada na integração dos Itens dos Pedidos de Venda com o **TOL/TRE**, onde:   * 1ª UM; * 2ª UM dos produtos. | **MV\_CPLUMIT** | 1 - 1ª UM 2 - 2ª UM | 1 - 1ª UM - padrão |  |
| Geração das Cargas | Quando for:  1 - Automático: para as viagens vindas do **TOL/TRE**, o **TOTVS OMS** gera a carga automaticamente.  2 - Manual: para as viagens deve ser gerada manualmente a carga.  Este parâmetro implica na necessidade da liberação ser automática-**MV\_CPLLVA**, pois somente é permitido a montagem de cargas de viagens liberadas. | **MV\_CPLAUT** | 1 - Automático 2 - Manual | 2 - Manual - padrão |  |
| Liberação automática da viagem? | O uso deste parâmetro ocorre somente para o **TOTVS OMS**. Quando habilitado, ao realizar a integração da viagem vinda do **TOL/TRE**,  o Sistema realizará o envio da liberação de viagens de forma automática. | **MV\_CPLLVA** | 1 - Sim 2 - Não | 2 - Não - padrão |  |
| Permite enviar quantidades não liberadas para o **TOL/TRE**? | Ao ativar esse parâmetro o **TOTVS OMS** permitirá a integração de pedidos sem liberação de estoque com o **TOL/TRE**. Com isso, todas as informações serão integradas com base na tabela SC6-Itens do Pedido de Venda. | **MV\_CPLPELB** | 1 - Sim 2 - Não | 2 - Não - padrão |  |
| Permite estorno automático da carga ao cancelar ou reprogramar viagem? | Indica se será permitido efetuar o estorno automático da carga ao cancelar ou reprogramar uma viagem. Quando o usuário do **TOL/TRE** solicitar o cancelamento ou reprogramação da viagem, caso exista carga montada no **TOTVS OMS** esta será estornada.  Importante  Para que esta opção funcione corretamente é necessário que o **TOL/TRE** esteja parametrizado para informar ao **TOTVS OMS** as alterações sofridas na viagem. | **MV\_CPLESCG** | 1 - Sim  2 - Não | 2 - Não - padrão |  |
| Atualiza viagem no **TOL/TRE** ao cancelar a integração do pedido? | Indica se será atualizada a viagem no **TOL/TRE** ao cancelar a integração no T**OTVS OMS.** Se esse parâmetro estiver definido como 1-Sim, ao cancelar um item integrado que já encontra-se em uma viagem, será solicitada a alteração da viagem no **TOL/TRE** para que reflita os ajustes sofridos no **TOTVS OMS**.  Caso esteja definido como **2-Não**, a viagem permanecerá intacta, sendo ajustada apenas a carga e os status no **TOTVS OMS**.  Importante  Para que essa opção funcione corretamente é necessário que o **TOL/TRE** esteja parametrizado para permitir alterações na viagem. Atualmente esta opção não está disponível para a solução **TOTVS Roteirização e Entregas**. | **MV\_CPLATVG** | 1 - Sim 2 - Não | 2 - Não - padrão |  |
| Tempo máximo-em segundos, de inatividade permitida para a recepção da resposta-Timeout. | Indica o tempo máximo que o **TOTVS OMS** aguardará por uma resposta do **TOL/TRE**. Válido para todos as as mensagens. | **MV\_CPLTIME** |  | 30 - padrão |  |
| Integração Monitoramento? | Indica se a integração com o monitoramento do **TOL/TRE** está ativa. | **MV\_CPLMON** | 1 - Sim 2 - Não |  |  |

**Saiba mais**Mais informações poderão ser acessadas nos *link's*:[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar LOG de integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
