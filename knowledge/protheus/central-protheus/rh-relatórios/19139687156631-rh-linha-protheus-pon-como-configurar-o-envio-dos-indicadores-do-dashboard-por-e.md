---
article_id: 19139687156631
category: RH - Relatórios
content_hash: d26a8fa5e31b4706d6387963a81f5c4b259c065882a0be9fcd4bb58c35fd3541
fetched_at: '2026-06-28T22:44:43.443060+00:00'
product: protheus
section_id: 32419371267223
source: central-protheus
title: RH - Linha Protheus - PON - Como configurar o envio dos indicadores do Dashboard
  por email via Schedule
type: support-article
updated_at: '2025-10-08T14:49:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19139687156631-RH-Linha-Protheus-PON-Como-configurar-o-envio-dos-indicadores-do-Dashboard-por-email-via-Schedule
---

**Dúvida**Como configurar o envio dos indicadores do *Dashboard* por e-mail?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No ***Dashboard*** temos opção de enviar os indicadores por **por *e-mail***, mas para que o *e-mail* seja enviado corretamente, é necessário que suas configurações estejam corretas (servidor de *e-mail*, endereço do servidor, usuário, senha, entre outros). Temos também a opção de enviar *e-mail* dos **Indicadores via agendamento no Schedule**, para isso é necessário seguir os procedimentos abaixo:  
  
Acessar o módulo **Configurador (SIGACFG)**, no caminho **Ambiente>*E-mail/proxy*>Configurar** e preencher os campos, conforme o servidor de *e-mail* que será utilizado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874731415)  
  
Preencha os campos conforme o servidor de *e-mail* que será utilizado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874733079)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874733975)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874735383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490886231703)  
  
Após realizar todo os preenchimento utilizando o **configurador**, teremos que preencher o conteúdo dos parâmetros **MV\_GPEMAIL** e **MV\_PONREST**.

**1. MV\_GPEMAIL -** Preencher com o destinatário do e-mail.  
\*\*Se o parâmetro não for preenchido o sistema irá utilizar o **MV\_RELAUSR**. Se nenhum dos dois parâmetros (MV\_GPEMAIL e o MV\_RELAUSR) não estiverem preenchidos, o sistema não **irá enviar o *e-mail****.*Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490886232983)  
  
**2. MV\_PONREST -**Preencher com o endereço do servidor Rest configurado no Protheus.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490886235031)  
  
Para o envio do *e-mail* do **Dashboard** através do Schedule, certifique que o ambiente esteja atualizado com o [**pacote da expedição contínua**](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO) a partir de 12/09/2022 (Atualizado pacote de fontes e o pacote de dicionário de dados - UPDDISTR). Com essa atualização, teremos a rotina **PONA480A**, que será responsável por realizar o envio do *e-mail* com as informações do Dashboard.  
  
**Importante:**A rotina PONA480A deverá ser executada apenas via Schedule, não é possível utiliza-la pelo menu do Protheus.  
  
**Configuração do Schedule:**  
**1.** Preencha no Schedule o campo rotina com **PONA480A  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874742039)****2.** Ao clicar em parâmetros será possível definir o filtro que será utilizado para trazer os indicadores do Dashboard.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874743831)  
  
Para a configuração existem 3 campos, que são:  
**1. Filial:**Será possível selecionar várias filias e até mesmo definir um range das filiais para a utilização do filtro.  
Abaixo está um exemplo selecionando a filial D MG 01 e utilizando o range da M SP 01 à M SP 04.  
![](https://tdn.totvs.com/download/attachments/706921605/image2023-5-4_11-15-24.png?version=1&modificationDate=1683209724677&api=v2&effects=drop-shadow)  
  
**2. Período:****- Mensal**Para a data inicial será considerado o primeiro dia do mês atual e para a data final o dia atual, por exemplo, hoje é dia 08/10/2025, então a data inicial será 01/10/2025 e a data final 08/10/2025  
  
**- Semanal**Para a data inicial será considerada a segunda-feira da semana atual e para a data final o dia atual, por exemplo, hoje é dia 08/10/2025, a segunda-feira da semana atual é 06/10/2025, então a data inicial será 06/10/2025 e a data final 08/10/2025.  
  
**- Quinzenal**Para a data inicial será considerado a quinzenal atual e para a data final o dia atual, por exemplo, hoje é dia 08/10/2025, a data inicial será 01/10/2025 e a data final 08/10/2025. Caso a data de hoje seja superior ao dia 15, será utilizada a segunda quinzena do mês. Por exemplo, hoje é dia 25/10/2025, então a data inicial será 15/10/2025 e a data final 25/10/2025.  
  
**3. Qtde Dias**Quantidade de dias que será utilizada para subtrair com a data de hoje, para utilização da data inicial do filtro do Dashboard. Este parâmetro só deverá ser preenchido caso a Opção do período seja "Qtde Dias", caso contrário este parâmetro será ignorado. Essa opção é limitada a 60 dias.  
  
**3 - Gestor**É possível selecionar o gestor desejado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490886245527)  
  
Após a configuração do Scheduler a rotina irá enviar o e-mail de acordo com a periodicidade definida e o parâmetros serão utilizados no filtro do Dashboard. Abaixo está um exemplo do e-mail enviado.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874747543)![](https://centraldeatendimento.totvs.com/hc/article_attachments/35490874748439)**

**Saiba mais:**[RH - Linha Protheus - PON - Como utilizar o Dashboard do Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19054544447639-RH-Linha-Protheus-PON-Como-utilizar-o-Dashboard-do-Ponto-Eletr%C3%B4nico?source=search)  
[RH - Linha Protheus - PON - Como configurar o envio dos indicadores do Dashboard por email](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18986073972119-RH-Linha-Protheus-PON-Como-configurar-o-envio-dos-indicadores-do-Dashboard-por-email?source=search)[Dashboard Ponto Eletrônico](https://tdn.totvs.com/display/public/PROT/SIGAPON+-+Dashboard+Ponto%20Pacote%20de%20Expedi%C3%A7%C3%A3o%20Cont%C3%ADnua%20Acumulado%20de%20RH)  
[MP - FRAME - Configurar o SMTP para envio de relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-MP-FRAME-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)  
[Application Server - Uso de e-mail com GMail](https://tdn.totvs.com/display/tec/Application+Server+-+Uso+de+e-mail+com+GMail)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
