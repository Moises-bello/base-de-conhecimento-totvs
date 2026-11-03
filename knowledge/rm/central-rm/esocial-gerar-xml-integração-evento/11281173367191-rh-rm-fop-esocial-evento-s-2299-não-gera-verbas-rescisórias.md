---
article_id: 11281173367191
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8e55b64b984e201b4bd0c4e60a0506e86d4d845cd6dc0a29e09ffd2615943c8e
fetched_at: '2026-06-28T22:47:13.014095+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Evento S-2299 não gera verbas rescisórias
type: support-article
updated_at: '2026-01-09T11:42:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11281173367191-RH-RM-FOP-eSocial-Evento-S-2299-n%C3%A3o-gera-verbas-rescis%C3%B3rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22409360031255) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
O que fazer quando ao gerar o evento S-2299 não saem as verbas rescisórias no XML?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
Para correção da ocorrência será necessário realizar as validações abaixo:  
  
• **Data de obrigatoriedade** dos eventos  
Caso as data de obrigatoriedade dos Eventos Periódicos seja posterior a data de desligamento, as verbas não sejam geradas. Por isso, é necessário verificar se estão com as datas de acordo com o cronograma do eSocial.  
Para isso, acesse em **Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais 1/7** e confira as datas de obrigatoriedade dos eventos periódicos conforme [cronograma eSocial](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao).   
Abaixo segue resumo do Cronograma eSocial:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23949430576023)

• Falta de **distribuição do SEFIP**  
1. Para empresas que utilizam tomadores de serviço, o sistema irá buscar as verbas para montagem do XML na distribuição do SEFIP realizada. Caso exista eventos faltantes na distribuição, não considerará as verbas no XML. Desta forma, verifique em **Encargos | SEFIP |** [**Distribuir SEFIP**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026677233-RH-RM-FOP-eSocial-Hist%C3%B3rico-de-rateio-por-tomador-de-servi%C3%A7os?source=search) a distribuição realizada para o mês/ano correspondente ao período de apuração;  
2. Em seguida, na fila de eventos gere o XML novamente e envie ao eSocial.

• Falta ou preenchimento incorreto do **Tipo de regimento trabalhista**no **Registro**do funcionário

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12757400794391)

**•** **Situação do Funcionário**não constar como D - Demitido

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23949430590999)

• **Rescisão não calculada**  
Para identificar se a rescisão foi calculada, a consulta abaixo no banco de dados do RM deverá retornar com o preenchimento 1:  
SELECT RESCISAOCALCULADA FROM PFUNC WHERE CHAPA='INSIRA AQUI A CHAPA DO FUNCIONÁRIO'

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37555375352599)](https://chat.google.com/u/0/api/get_attachment_url?url_type=DOWNLOAD_URL&attachment_token=AMzByC1t9c2QHozZqCKlY%2FeLIqJd82Ztnl7LerS0s%2BEwdtkCRQDvObryIajOUPx2gzUMC7kurCmwrmtuRjCo1GiP7kDirzLrduvA7gkmsURTB3BeLTsqH1R2yAF1iUmwu44Rx%2BuE8PqRCG%2FG9G1B1KfHKFrj9RLihrw4QFjDT6f0RkFxhwIPe1dZiPhu0vmoMSH9ulZTS9gcKJaHEiB110qYPK037pmuuI7EKRW%2FTTyD1M5xOJVrTRcidJjEmcZxY8UGK8PJJxLZKepjhv2FasfLjXjwIAnraiOIkeZ6RwgBZap5JBToIBkuavA0x6X%2FqBS7KQaQBKJJD1spn5PpUZFiM3TyGSxaD9BOsrbBGKp%2B5aeqJgG5AUN63EL6JzqTcUJwwiBGi3xUqtcUbvnviJeJSpCimWC2EgRfXuiYq%2BIRMXMupJWOO6cLWPy4eEXHpygC7DEoMdHZQdeZ%2FaglFHA9ofIz&content_type=image%2Fpng&auto=true)

Coluna - rescisaocalculada | **1 = Calculada   0 = Não calculada**

**Saiba mais**  
Para mais informações acesse: 

* [Retificação do evento de rescisão/desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017501692-RH-RM-FOP-eSocial-Retifica%C3%A7%C3%A3o-do-evento-de-rescis%C3%A3o-desligamento?source=search)
* [Distribuição de SEFIP de meses anteriores para tomadores de serviços em retificação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028703594)
* [Histórico de rateio por tomador de serviços](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026677233-RH-RM-FOP-eSocial-Hist%C3%B3rico-de-rateio-por-tomador-de-servi%C3%A7os?source=search)
