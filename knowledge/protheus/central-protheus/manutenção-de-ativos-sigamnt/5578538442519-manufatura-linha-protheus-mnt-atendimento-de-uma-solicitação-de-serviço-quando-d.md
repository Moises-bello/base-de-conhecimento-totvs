---
article_id: 5578538442519
category: Manutenção de Ativos (SIGAMNT)
content_hash: b28b2948c357198019b1412e852c9ba4819c73a2a858e1918a172b4e0371dbd5
fetched_at: '2026-06-28T22:42:32.765957+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Atendimento de uma Solicitação de Serviço
  quando distribuída para uma equipe
type: support-article
updated_at: '2023-12-10T02:53:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5578538442519-Manufatura-Linha-Protheus-MNT-Atendimento-de-uma-Solicita%C3%A7%C3%A3o-de-Servi%C3%A7o-quando-distribu%C3%ADda-para-uma-equipe
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:45 min** **Dúvida**Como atender uma **S.S. - Solicitação de Serviço**, quando é distribuída para uma equipe?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
 **Solução**Para atendimento de uma **S.S.** quando distribuída por equipe, é necessário seguir os passos abaixo:  
  
1. Acessar o **Configurador - SIGACFG**;   
2. Ir em **Ambiente - Cadastros - Parâmetros - CFGX017**;  
3. Configurar o parâmetro **MV\_NG1FAC- Indica se utiliza Facilities ou Solicitação serviço.** igual a **1 - Facilities**;  
4. Acessar o módulo **Manutenção de Ativos - SIGAMNT**;  
5. Em **Atualizações - Controle de Oficina - Bens -** **Bens - MNTA080** incluir um **Bem**;  
6. Em **Atualizações - Controle de Oficina - Manutenção - Especialidade - MNTA010**, incluir uma **Especialidade**;  
7. Em **Atualizações - Controle de Oficina - Manutenção - Funcionários -** **MNTA020**, incluir dois **Funcionários** relacionando a especialidade cadastrada no passo anterior, um **Código de Usuário** e no campo **Atendimento** informar a opção **3 - Ambos**;  
8. Em **Atualizações - Controle de Oficina - Manutenção - Equipes - MNTA800**, incluir uma Equipe, e no campo **Responsável**, informar um dos **Funcionários** cadastrados:

* Na **Aba Calendários** inserir um calendário existente;
* Na **Aba Funcionários**, incluir os 2 **Funcionários** que foram cadastrados;

9. Em **Atualizações - Controle de Oficina - Solicitação de Serviço - Tipo de Serviço s - MNTA285**, incluir um **Serviço**;  
10. Em **Atualizações - Controle de Oficina - Solicitação de Serviço - Solicitação - MNTA280**, incluir uma **S.S.** para o **Bem** cadastrado;11. Em **Atualizações - Controle de Oficina - Solicitação de Serviço - Facilities - Distribuição - MNTA296**, selecionar a **S.S.** cadastrada:

* Na caixa inferior da direita chamada **Atendentes**, selecionar a aba **Equipes**, e marcar a **Equipe** criada.

12. Em **Atualizações - Controle de Oficina - Solicitação de Serviço - Facilities - Atendimento MNTA291**, irá solicitar um funcionário para efetuar o atendimento. Nesse caso é necessário informar o **Responsável** pela equipe na abertura da tela:

* No canto inferior esquerdo da tela, existem dois ícones para a visualização das **S.S.** distribuídas.  
  ![](https://tdn.totvs.com/download/attachments/271658458/image2017-2-14%2011%3A21%3A2.png?version=1&modificationDate=1487083674000&api=v2) Mostram as **S****olicitações de Serviço** do **Atendente**  
  ![](https://tdn.totvs.com/download/attachments/271658458/image2017-2-14%2011%3A21%3A41.png?version=1&modificationDate=1487083674000&api=v2) Mostram as **S****olicitações de Serviço** da **Equipe**;
* Clicar no segundo ícone, em **Solicitações de Serviço da equipe**, e marcar a **S.S.** para efetuar o **Atendimento**
* Em seguida, no menu esquerdo acionar o botão no **Transferir Atendimento**

**![Atendimento_ss_equipe.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5578993666327/Atendimento_ss_equipe.png)**

13. Na tela de **Transferência de Atendimento**:

* Em **Detalhes da Solicitações**, vai mostrar as informações **S.S.** selecionada
* **Atendentes da Solicitação**, vai mostrar a equipe que a **S.S.** foi distribuída.
* Em **Atendentes Disponíveis**, vão mostrar as opções que existem para fazer a **Distribuição da S.S.**, para **Equipe**, para um **Atendente** ou para um **Terceiro**.

1. ![transferencia_atendimento.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5579154696983/transferencia_atendimento.png)
