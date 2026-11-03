---
article_id: 360063623233
category: Portal Facilities
content_hash: 3fe09000cdfa341e22e3edf94860fd2bc3371a02727c0c279aa3da2eedef479d
fetched_at: '2026-06-28T22:42:36.172191+00:00'
product: protheus
section_id: 360010992234
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Desabilitar Pesquisa de Satisfação Facilities
type: support-article
updated_at: '2021-09-23T19:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063623233-Manufatura-Linha-Protheus-MNT-Desabilitar-Pesquisa-de-Satisfa%C3%A7%C3%A3o-Facilities
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como desabilitar o questionário de satisfação para que não seja solicitada a **Pesquisa de satisfação**, quando parametrizado para utilizar **Facilities**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Portal Facilities - Todas as versões  
  
**Solução**Para desabilitar o processo de **Pesquisa de satisfação**, é necessário seguir os passos abaixo:

1. Acessar o **Configurador - SIGACFG**;
2. Ir em **Ambiente / Cadastros / Parâmetros - CFGX017**;
3. Configurar parâmetros:   
   **MV\_NGPSATI - Indica se utiliza Pesquisa de Satisfação** igual a **S - Sim**;   
   **MV\_NG1FAC** - **Indica se utiliza Facilities ou Solicitação de Serviço** igual a **1**;   
   **MV\_NGSSWRK** **- Identifica se no módulo de Solicitação de Serviços será utilizado envio de mensagens por workflow** igual a **S - Sim**;
4. Acessar o **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
5. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Calendário - MATA780**, incluir um **Calendário**;
6. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Centros de Custos - CTBA030**, incluir um **Centro de Custo**;
7. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Fornecedores - MATA020**, incluir um **Fornecedor**;
8. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Funcionários - GPEA010**, incluir um **Funcionário**, informando um **CPF - Cadastro de Pessoa Física**;
9. Em **Atualizações / Controle de Oficina / Bens / Veículos - MNTA084**, incluir um **Veículo** de **Categoria** igual a **Frota não integrada ao TMS** preenchendo o campo **Tanque - TT8\_CODCOM** e **placa - T9\_PLACA**;
10. Em **Atualizações / Controle de Oficina / Manutenção / Especialidade - MNTA010**, incluir uma **Especialidade**;
11. Em **Atualizações / Controle de Oficina / Manutenção / Funcionários - MNTA020**, incluir o **Funcionário** cadastrado anteriormente relacionando a **Especialidade** cadastrada no passo anterior, um **Código de Usuário** e em **Atendimento Ambos**;
12. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Tipo de Serviço - MNTA040**, incluir um **Serviço**;
13. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Quest. Satisfação -** **MNTA307**, no cadastro da **Pesquisa** informar **1 - Sim no campo Desabilita?** e em **Opção** utilizar **3 - Bem relacionando o código ao Bem** anteriormente cadastrado;
14. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Solicitação - MNTA280**, incluir uma **Solicitação de Serviço - S.S** para o **Bem** cadastrado anteriormente;
15. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Distribuição -** **MNTA296**, distribuir a **S.S** cadastrada;
16. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Atendimento -** **MNTA291**, reportar horas na **S.S** distribuída e posteriormente, fechar a **S.S**;
17. Em **Atualizações / Controle de Oficina / Solicitação Serv. / Satisfação SS - MNTA305**, acessar a rotina e verificar que a última **S.S** cadastrada não foi para **Pesquisa de satisfação** devido ao questionário estar desabilitado.

Seguindo os passos supracitados, a **Solicitação de Serviço** não solicitará resposta na **Pesquisa de satisfação**.
