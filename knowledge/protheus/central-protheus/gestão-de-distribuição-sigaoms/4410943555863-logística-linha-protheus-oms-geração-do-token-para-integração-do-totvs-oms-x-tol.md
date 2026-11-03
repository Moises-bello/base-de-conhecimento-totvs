---
article_id: 4410943555863
category: Gestão de Distribuição (SIGAOMS)
content_hash: e7fc3bbd8ae0220023abd27d39a552abb57ab7745118650bba45db78b438f69b
fetched_at: '2026-06-28T22:45:49.844824+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Geração do Token para integração do TOTVS
  OMS x TOL/TRE
type: support-article
updated_at: '2026-05-29T20:26:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410943555863-Log%C3%ADstica-Linha-Protheus-OMS-Gera%C3%A7%C3%A3o-do-Token-para-integra%C3%A7%C3%A3o-do-TOTVS-OMS-x-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40836160156055) Tempo aproximado para leitura: **00:02:18 min**  
  
**Dúvida**  
Como gerar e validar o **Token** para integração do **TOTVS** **OMS** x**TOL/TRE**?  
  
**Ambiente**  
TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**  
No processo de integração do **TOTVS OMS** x **TOL/TRE** é necessária a utilização de um **token** valido. Abaixo descrevemos os parâmetros relacionados ao **token**:

* **MV\_USRCPL** - Usuário de autenticação do **Webservice**.   
  Usuário utilizado para efetuar *login* no **TOL/TRE**, para obtenção do **token**. É obrigatório preencher este campo quando houver **URL** de autenticação.  
  Verifique se o usuário  de autenticação é válido.
* **MV\_PSWCPL** - Senha de autenticação do **Webservice.**  
  Senha do usuário utilizado para efetuar *login* no **TOL/TRE**, para obtenção do **token**. É obrigatório preencher este campo quando houver **URL** de autenticação.  
  Verifique se a senha de autenticação é válida.
* **MV\_CPLUAUT** - Endereço do **Webservice** de autenticação do **TOL/TRE**.  
  Exemplo: **http://<IP ou nome>:<porta>/cockpit-gateway/ws/authentication**   
  Este endereço fornecerá um **token** de autenticação que deverá ser utilizado nas requisições efetuadas ao **TOL/TRE**, quando estiver parametrizado para solicitar autenticação.  
  Verifique se o endereço do **WebService** de autenticação informado é válido e está disponível.
* **MV\_TOKCPL** - Armazena o **token** recebido **TOL/TRE**.  
  Verifique se o **token** armazenado no parâmetro é válido. Limpe o parâmetro e tente realizar a integração novamente para forçar a gravação do **token** atualizado.
* **MV\_EXPTOK** - Quantidade de horas para considerar **token**.   
  Indica a quantidade de horas que devem ser consideradas para que um **token** expire. Enquanto este limite não for atingido, o mesmo **token** recebido na primeira solicitação será reutilizado para envio das próximas mensagens. Verifique a quantidade de horas informada para considerar que um **token** expire. No padrão o o **token** é atualizado a cada **24 horas**. Configure esse parametro para valor **inferior a 24 horas**.

É possível realizar um teste de conexão acessando o menu **Atualizações/Cockpit Logístico/Parâmetros Integração - OMSXCPL1**, botão **Outras Ações/Testar Webservice Planejamento de Viagem**.  
  
**Importante**  
O **TOL/TRE** é responsável por retornar a informação do **token** de acesso ao **TOTVS OMS**. Caso o **token** não seja retornado, será necessário acionar o **time de atendimento da Otimização Logística**, pois existem configurações na solução de **Otimização Logística** que permitem retirar a obrigatoriedade do **token**.Entretanto, no **TOTVS OMS**, o **token** é obrigatório para o processamento da integração.

**Saiba mais**  
Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Parâmetros para integrar o TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402272406551-Log%C3%ADstica-Linha-Protheus-OMS-Par%C3%A2metros-para-integrar-o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
