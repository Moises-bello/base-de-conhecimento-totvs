---
article_id: 360034157334
category: RH - Férias
content_hash: 79338110dd7affad60e3771364da702b3fd16f1472228d4a2fa6d1114b22f7fe
fetched_at: '2026-06-28T22:43:58.182892+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar Workflow para notificação automática
  de Férias em dobro
type: support-article
updated_at: '2025-10-31T14:09:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034157334-RH-Linha-Protheus-GPE-Como-parametrizar-Workflow-para-notifica%C3%A7%C3%A3o-autom%C3%A1tica-de-F%C3%A9rias-em-dobro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18191794308247)** Tempo aproximado para leitura: **00****:02:30 min**

**Dúvida**Como parametrizar *Workflow* para envio de notificações de Férias em dobro?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução****1.** Acesse o ambiente SIGACFG (Configurador) com senha de Administrador  
**2.** Vá até a rotina de parâmetros através do menu **Base de Dados > Dicionário > Base de Dados****3.** Clique no símbolo de mais no canto superior esquerdo ao lado da empresa para expandir opções:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11176930166423)

**4.** Selecione a opção Parâmetros e busque conforme abaixo:   
**- MV\_WFFERVE:** Informe a quantidade de dias somados a data atual para a busca  
**- MV\_WFFEREM:** Inclua o Endereço de e-mail padrão  
**- MV\_RHSERV:** Insira o servidor de e-mail utilizado para o envio  
**- MV\_RHAUTEN:** Determine se o servidor de e-mail requer autenticação. Conteúdo **.T. requer** ou **.F. não requer** autenticação.  
  
**5.** Cadastre na rotina de ***Schedule***um ***job*** para envio do aviso conforme exemplo:  
  
![](https://tdn.totvs.com/download/attachments/233763727/Sem%20t%C3%ADtulo.jpg?version=1&modificationDate=1563364530463&api=v2)

Caso esteja usando o *smart schedule*, abaixo segue exemplo de configuração:  
  
![smart schedule.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24404897556759)  
  
Desta forma será encaminhado e-mail com listagem dos funcionários com terão férias vencidas e em dobro.

**IMPORTANTE**- O sistema realiza uma verificação inicial no **cadastro de hierarquias** pelo **Controle de Hierarquias do SIGAORG.** Caso não utilize o **SIGAORG**, o sistema irá verificar o **cadastro de departamentos** e seu respectivo **superior.** Caso não haja um **email cadastrado para o superior**, o sistema irá enviar o email e log para os emails cadastrados no parâmetro **MV\_WFFEREM.**  
- Depois que o funcionário **quitar** as férias vencidas relacionadas a férias em dobro (**dias pagos = 30 e situação = pago**), ele **não** entrará mais na relação de funcionários enviados por e-mail.  
- O e-mail origem das notificações será o e-mail definido no **SMTP** (Módulo Configurador > Ambiente > E-mail/Proxy).  
- Para **verificação de férias em dobro**, o sistema só irá conferir as férias calculadas em **períodos fechados,** por exemplo, se a folha estiver aberta em Abril, o funcionário possui férias em dobro que foi calculada em Abril e esse período está aberto, **o sistema ainda enviará a notificação.** Quando o período de Abril for fechado, a notificação referente ao funcionário não será mais enviada.

**Saiba Mais:**[Boletim Técnico - Worflow Férias em dobro](https://tdn.totvs.com/pages/viewpage.action?pageId=518463153)  
[RH - Linha Protheus - GPE - Schedule para Aviso de Vencimento do Período de Experiência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050787734-RH-Linha-Protheus-GPE-Schedule-para-Aviso-de-Vencimento-do-Per%C3%ADodo-de-Experi%C3%AAncia)  
[RH - Linha Protheus - GPE - Quais são os parâmetros de integração do SIGAGPE com o SIGAORG](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057495354-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-os-par%C3%A2metros-de-integra%C3%A7%C3%A3o-do-SIGAGPE-com-o-SIGAORG?source=search)  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961)

[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
