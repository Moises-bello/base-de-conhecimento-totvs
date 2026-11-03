---
article_id: 360055609834
category: Suricato
content_hash: 81a2e73c05f6493708956c02195420f31c541833a6beffc0c835e958b6d617bc
fetched_at: '2026-06-28T22:44:57.374964+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - GPE x Suricato - Integração de Rescisão para o Suricato
type: support-article
updated_at: '2023-12-20T12:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055609834-RH-Linha-Protheus-GPE-x-Suricato-Integra%C3%A7%C3%A3o-de-Rescis%C3%A3o-para-o-Suricato
---

**Dúvida**Como é feita a Integração de uma Rescisão para o Suricato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.23  
  
**Solução**Quando uma **Rescisão** é calculada no **Protheus**, este desligamento é **integrado** ao **Suricato**, de modo que o **Acesso** desta pessoa seja **bloqueado**.  
A ação do **bloqueio do Acesso** é feita no **dia da demissão**, às **23h59 por padrão**, para que a pessoa consiga finalizar os trâmites internos antes de sair da empresa, porém, se for preciso que o bloqueio seja feito antes, é possível ajustar a configuração do **Processo Online** no **Suricato** para que este mapeamento seja feito em um intervalo menor.  
Após a varredura feita pelo **Processo Online**, o ***status*** do funcionário será alterado para **Demitido** no cadastro do **Suricato**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16710675038103)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711050626839)  
  
  
Para que sejam gerados os **XMLs da integração** como demonstrados nesta documentação, é necessário que o conteúdo do parâmetro **MV\_TSATLOG** esteja como**5**. Os arquivos serão gerados **dentro da pasta System** do ambiente com nomes contendo um **número sequencial + SND** (XML de envio do Protheus) e **número sequencial + RCV** (XML de retorno do Suricato):  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711126783383)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16711100603415)  
  
**OBS:** o parâmetro **MV\_TSATLOG** também permite que o usuário gere os ***logs***da integração através de **Email** ou **Arquivo**. Para isso, basta deixar o conteúdo do parâmetro como **1 = Email, 2=Arquivo, 3=Ambos**, porém, para **análise** dos times de **Suporte** da TOTVS e Telematica, serão solicitados os arquivos **XMLs**, gerados através do conteúdo do parâmetro como **5**.  
  
O **XML** que informa a **demissão** ao **Suricato** é o que trata dos dados do funcionário. Nele, existe a ***tag*** **fireDate**, que é preenchida com a **data do desligamento**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16710425141143)  
  
Além deste, será gerado o **XML** contendo os dados de pessoa física, conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16710456784535)  
  
  
Os **XMLs** serão gerados quando:  
- a **Rescisão** for calculada com **data antecipada ao dia do desligamento**;  
- a **Rescisão** for calculada no **dia do desligamento**;  
- a **Rescisão** for calculada em **data posterior ao desligamento.**  
  
**Saiba Mais**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
