---
article_id: 360055590174
category: Suricato
content_hash: 3a86cf559d06109d5b0fe248bc6f48fb1751aa18a1ba1c6f57e74ecf64e82b78
fetched_at: '2026-06-28T22:43:05.651055+00:00'
product: protheus
section_id: 33998256658455
source: central-protheus
title: RH - Linha Protheus - GPE x Suricato - Integração de Afastamentos Médicos ao
  Suricato
type: support-article
updated_at: '2025-08-06T20:44:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055590174-RH-Linha-Protheus-GPE-x-Suricato-Integra%C3%A7%C3%A3o-de-Afastamentos-M%C3%A9dicos-ao-Suricato
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16705324231959)**Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como funciona a integração de Afastamentos Médicos do Protheus para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23  
  
**Solução**O cadastro de qualquer tipo de **Afastamento Médico** no Protheus, gera **integração** automática para o **Suricato**, desde que o registro seja criado **até no máximo** a **data de afastamento** do funcionário OU se no momento do **cadastro**, o funcionário **ainda estiver ausente.**  
  
Para que sejam gerados os **XMLs da integração** como demonstrados nesta documentação, é necessário que o conteúdo do parâmetro **MV\_TSATLOG** esteja como **5**. Os arquivos serão gerados **dentro da pasta System** do ambiente com nomes contendo um **número sequencial + SND** (XML de envio do Protheus) e **número sequencial + RCV** (XML de retorno do Suricato):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704377377687)  
 **![](https://centraldeatendimento.totvs.com/hc/article_attachments/16709734130327)  
  
OBS:** o parâmetro **MV\_TSATLOG** também permite que o usuário gere os ***logs*** da integração através de **Email** ou **Arquivo**. Para isso, basta deixar o conteúdo do parâmetro como **1 = Email, 2=Arquivo, 3=Ambos**, porém, para **análise** dos times de **Suporte** da TOTVS e Telematica, serão solicitados os arquivos **XMLs**, gerados através do conteúdo do parâmetro como **5**.  
  
Para os casos de **Afastamentos**, o **XML** que trás estes dados é o que possui a ***tag*** **AbsenceReason**. Para inclusões, a ***tag*** virá como **insertUserAbsenceReason:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704593058455)  
  
Para exclusões, virá como **removeUserAbsenceReason:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704435443607)  
  
Para um **afastamento médico** apenas no dia 11.08.2023, por exemplo, se o registro for **criado** no Protheus **até o próprio dia 11**, ele será **integrado via XML** ao Suricato:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704626718103)  
  
Se o **afastamento** for **criado** no Protheus **a partir do dia 12 em diante**, **não será gerado o XML** que trata do afastamento e consequentemente o dado **não será integrado ao Suricato**.  
**OBS:** serão gerados apenas os **XMLs** que tratam dos dados de **pessoa física e do funcionário**, porém, em **nenhum** destes arquivos o **Afastamento** será informado.  
  
**Exemplo** de um **XML** com dados de **pessoa física**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704654277015)  
  
**Exemplo** de um **XML** com **dados do funcionário**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704729339543)  
  
Nos casos onde for cadastrado um **Afastamento** e a pessoa ainda **estiver ausente**, o **XML** que trata do **Afastamento** será **gerado** normalmente. Por exemplo: afastamento médico de 10 dias, a partir de 11.08.2023, se o registro for criado no Protheus **até o dia 20.08.2023** (data fim do afastamento), o **XML** que trata do **afastamento** será gerado, mas **se for feito após esta data**, o arquivo **não será gerado.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16704796494999)  
  
O processo é tratado desta forma, pois deve ser levado em consideração que o intuito do **Suricato** é administrar o **Controle de Acesso** das pessoa na empresa, ou seja, nos casos onde o funcionário já se afastou e retornou, o Protheus não gera o **XML** com a ***tag* AbsenceReason** pois para o **Suricato** não terá nenhuma ação a ser feita.  
  
Quando um **Afastamento** é cadastrado no Protheus, e a pessoa encontra-se ausente, existe uma rotina no **Suricato** chamada **Processo Online**, que faz uma varredura nos dados recebidos do **Protheus**, para que sejam feitos os **bloqueios de acesso** e atualizados os ***status*** dos funcionários afastados.  
Este processo deve ser parametrizado pelo cliente, com uma recorrência que o melhor atenda.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711216069783)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711187818903)  
  
  
**Saiba Mais**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
