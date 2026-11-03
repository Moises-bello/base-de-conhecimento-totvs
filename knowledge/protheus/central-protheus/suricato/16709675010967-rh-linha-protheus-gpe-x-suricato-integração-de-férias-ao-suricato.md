---
article_id: 16709675010967
category: Suricato
content_hash: 085077058625e9343eabe7d72de195fc9a25b5750c74553ceec713272fd3c6d8
fetched_at: '2026-06-28T22:44:57.367141+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - GPE x Suricato - Integração de Férias ao Suricato
type: support-article
updated_at: '2023-12-20T12:56:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16709675010967-RH-Linha-Protheus-GPE-x-Suricato-Integra%C3%A7%C3%A3o-de-F%C3%A9rias-ao-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16709666677271) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como funciona a integração de Férias do Protheus para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23  
  
**Solução**As **Férias** calculadas dentro do Protheus geram **integração** automática para o **Suricato,** para que seja feito o **bloqueio do Acesso** do funcionário no **período de ausência.**Para que sejam gerados os **XMLs da integração** como demonstrados nesta documentação, é necessário que o conteúdo do parâmetro **MV\_TSATLOG** esteja como**5**. Os arquivos serão gerados **dentro da pasta System** do ambiente com nomes contendo um **número sequencial + SND** (XML de envio do Protheus) e **número sequencial + RCV** (XML de retorno do Suricato):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16775425749527)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708815019287)  
  
**OBS:** o parâmetro **MV\_TSATLOG** também permite que o usuário gere os ***logs***da integração através de **Email** ou **Arquivo**. Para isso, basta deixar o conteúdo do parâmetro como **1 = Email, 2=Arquivo, 3=Ambos**, porém, para **análise** dos times de **Suporte** da TOTVS e Telematica, serão solicitados os arquivos **XMLs**, gerados através do conteúdo do parâmetro como **5**.  
  
Para os casos de **Férias**, o **XML** que trás estes dados é o que possui a ***tag*** **AbsenceReason**. Para **inclusões**, a ***tag*** virá como **insertUserAbsenceReason:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16706817716887)  
  
Para **exclusões** de **Férias**, virá como **removeUserAbsenceReason:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16706878059159)  
  
Para uma **Férias** calculada **dentro do mês** vigente, por exemplo, mês de Agosto/23, considerando Férias do dia 14.08.2023 ao dia 28.03.2023, e que o cálculo tenha sido feito no máximo até um dia antes da data de saída do descanso do funcionário, ou seja, dia 14, será gerado o **XML** para integração dos dados ao **Suricato**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16707362289559)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708948218775)  
**OBS:** neste cenário, não serão gerados os **XMLs** de pessoa física e com os dados do funcionário, conforme exemplos abaixo:  
  
**- XML de pessoa física:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16707512567703)  
  
**- XML com os dados do funcionário:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16707505562263)  
  
  
Para uma **Férias** que esteja sendo calculada **durante o período de gozo** do funcionário, por exemplo: hoje é dia 11, e o período de gozo é de 01 à 20, será gerado apenas o **XML** contendo os dados do afastamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708942155415)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708914724631)  
  
  
Para uma **Férias** que esteja sendo calculada para um período que o funcionário **já tenha saída e voltado**, por exemplo, o cálculo está sendo feito no dia 11 e o período de Férias foi de 01 à 10, serão gerados os **XMLs** do afastamento, pessoa física e funcionário, porém, o **Suricato** não terá nenhuma ação, visto que o **Controle de Acesso** do funcionário deve estar liberado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708792520087)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16708970895639)  
  
  
Para uma **Férias** que ocorrerá no **mês seguinte**, por exemplo, o cálculo está sendo feito em Agosto mas a saída efetiva será apenas em Setembro, para que o **XML** de afastamento seja gerado, o usuário deverá **integrar, calcular e fechar o período** de Agosto da Folha. Com esta ação, o **XML** será gerado e o **Suricato** recebe a informação (neste caso, não serão gerados os **XMLs** de pessoa física e funcionário):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16709293345815)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16709322116887)  
  
  
Quando uma Férias é calculada no Protheus, e a pessoa encontra-se ausente, existe uma rotina no **Suricato** chamada **Processo Online**, que faz uma varredura nos dados recebidos do **Protheus**, para que sejam feitos os **bloqueios de acesso** e atualizados os ***status*** dos funcionários afastados.  
Este processo deve ser parametrizado pelo cliente, com uma recorrência que o melhor atenda.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711162558999)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711191567255)  
  
  
**Saiba Mais:**  
[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
