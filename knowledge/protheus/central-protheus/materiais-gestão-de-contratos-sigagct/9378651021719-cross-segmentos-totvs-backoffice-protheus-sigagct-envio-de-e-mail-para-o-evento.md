---
article_id: 9378651021719
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d2facd659d6114a1aebdfa4d7a9bade98d5ea33f0667fe988011fa9f81f48e5e
fetched_at: '2026-06-28T22:37:22.725752+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Envio de e-mail para
  o Evento 041 do Messenger - Log de Execução de Medição Automática
type: support-article
updated_at: '2026-03-18T11:21:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9378651021719-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Envio-de-e-mail-para-o-Evento-041-do-Messenger-Log-de-Execu%C3%A7%C3%A3o-de-Medi%C3%A7%C3%A3o-Autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20582620061207) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Envio de e-mail para o evento 041 do Messenger.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Gestão de Contratos.

**Solução**

O envio de *e-mail's* para os eventos do GCT, são orientados pelo parâmetro MV\_ATUGCT  
  
1. Verifique se o parâmetro MV\_ATUGCT não se encontra com período superior a *database*;  
2. Corrija a data do parâmetro para a *database* do sistema.

3. Segue exemplo de Configuração de e-mail de envio do menssenger para configuração em seu ambiente -[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Exemplo de configuração Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011724292-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Exemplo-de-configura%C3%A7%C3%A3o-Messenger-?source=search)

Após realizar a configuração de envio de e-mail conforme documentação acima configure o parâmetro **MV\_CNSCHED = 3.**

4. No cadastro do Tipo de contrato(CNTA021) ou Tipo de planilha(CNTA230), informar o campo  CN1\_MEDAUTO = SIM ou CNL\_MEDAUTO = SIM.

Tipo de Contrato.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9375186482839)

Tipo de Planilha.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9375287985175)

5. **CONFIGURAÇÃO DO EVENTO 041.**  
  
Acesse a rotina MATA045 (Messenger) e efetue a amarração dos evento 041 ao usuário e respectivo e-mail, na aba Usuários SIGA é possível amarrar um grupo de usuários e na aba não usuários é possível informar qualquer e-mail que necessite receber a notificação.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9375343660055)

6. **MV\_CNGRMSG =**De onde os e-mails para alerta devem ser obtidos(0=usuários x eventos, 1=Grupo de Aprovação, 2=Todos, 3=Entidades Contábeis X Grp.Apr.)

|  |  |
| --- | --- |
| • | Valor igual a 0: são informados por e-mail somente os responsáveis cadastrados para receber avisos de eventos do tipo Aviso de Vencimento - (SIGAGCT) [038] e Término do Contrato - (SIGAGCT) [039] definidos pela rotina de M-Messanger, mesmo que haja grupo de aprovação responsável pelo contrato. |

|  |  |
| --- | --- |
| • | Valor igual a 1: é informado por e-mail somente o grupo de aprovação do contrato definido pelo campo Grp. Apr. Sit. na rotina de Tipos de Contrato. Importante: o e-mail não será gerado se o parâmetro tiver valor igual a 1 e não existir grupo de aprovação para o contrato. |

|  |  |
| --- | --- |
| • | Valor igual a 2: são informados por e-mail os responsáveis cadastrados e o grupo de aprovação responsável. |

**IMPORTANTE:** houve uma mudança na geração de senha do gmail segue o novo processo na documentação abaixo para que possa configurar a senha conforme abaixo para preenchimento dos parãmetros de senha corretamente..  
  
Geração de senha de app gmail  
<https://tdn.totvs.com/pages/releaseview.action?pageId=689063841>

Exemplo de envio de e-mail de **Evento 041 (Log execução medição automática)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39122515278999)

**Obs**: Na mensagem acima apresenta somente o log do dia e horário que foi executado a rotina de Medições Automáticas CNTA260.

***Saiba Mais:***

[GCT0020\_Configuração para utilização dos eventos 040(Limite saldo na planilha) e 041(log execução medição automática)](https://tdn.totvs.com/pages/releaseview.action?pageId=663613194)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Envio de e-mail para os eventos 038 e 039 do Messenger](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017787171-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Envio-de-e-mail-para-os-eventos-038-e-039-do-Messenger?source=search)

[GCT0028\_MV\_ATUGCT\_Eventos\_038\_e\_039](http://tdn.totvs.com/display/PROT/GCT0028_MV_ATUGCT_Eventos_038_e_039)

[GCT0127\_Eventos\_038\_e\_039\_Configuração\_via\_Schedule](https://tdn.totvs.com/pages/releaseview.action?pageId=402071753)

[GCT0125 - Ativando e-mails de avisos automáticos do módulo GCT](https://tdn.totvs.com/pages/releaseview.action?pageId=393363398)

[GCT0032\_Aviso\_de\_Vencimento](https://tdn.totvs.com/display/public/PROT/GCT0032_Aviso_de_Vencimento)

[GCT0158\_Cadastrando eventos no EventViewer do GCT](https://tdn.totvs.com/x/Nyz2MQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
