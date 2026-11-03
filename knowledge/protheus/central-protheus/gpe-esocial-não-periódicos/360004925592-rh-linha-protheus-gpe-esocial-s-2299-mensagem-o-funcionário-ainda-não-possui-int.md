---
article_id: 360004925592
category: GPE - eSocial - Não Periódicos
content_hash: c2dcdbc1d0a9f7a36e2e02da5efe8fc654dcde8c867c066032688c3a4338eee0
fetched_at: '2026-06-28T22:45:05.865528+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2299 - Mensagem: O funcionário ainda
  não possui integração com o TAF. Realize a sua integração para poder gerar a rescisão.
  A rescisão não será efetivada.'
type: support-article
updated_at: '2026-06-16T13:46:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004925592-RH-Linha-Protheus-GPE-eSocial-S-2299-Mensagem-O-funcion%C3%A1rio-ainda-n%C3%A3o-possui-integra%C3%A7%C3%A3o-com-o-TAF-Realize-a-sua-integra%C3%A7%C3%A3o-para-poder-gerar-a-rescis%C3%A3o-A-rescis%C3%A3o-n%C3%A3o-ser%C3%A1-efetivada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28086452019479)**Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**  
Ao tentar calcular uma rescisão o sistema apresenta a mensagem:  
  
**Help:** Atenção  
**Problema:** O funcionário ainda não possui integração com o TAF. Realize a sua integração para poder gerar a rescisão. A rescisão não será efetivada  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34449971624471)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esse erro pode acontecer nos seguintes cenários:

* O evento S-2200 do trabalhador não foi enviado para o TAF;
* O evento S-2200 do trabalhador foi enviado para o TAF mas não foi transmitido para o RET;
* O evento S-2200 do trabalhador foi transmitido para o RET mas está sem o número de recibo no TAF;
* Rotina de desligamento está desatualizada;
* Código de matrícula do trabalhador encontra-se divergente entre SIGAGPE e TAF.
* Data de admissão do trabalhador no TAF está diferente do informado no SIGAGPE.

**Solução**

1. Verificar se o registro S-2200 da matricula está no TAF e se tem o número de recibo do governo.
2. Verificar se os campos RA\_CODUNIC e C9V\_MATRIC encontram-se com o mesmo código.  
   [Como visualizar a matricula eSocial (RA\_CODUNIC) no SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045583393)  
   [Como visualizar a matrícula eSocial (C9V\_MATRIC) no SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059736733)
3. Verificar se o sistema está atualizado com os últimos pacotes disponibilizados no link: [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

**Artigos Relacionados:**

* [RH - Linha Protheus - GPE - eSocial - S-2200 - Matrícula duplicada no cadastro do funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034699694)
* [RH - Linha Protheus - GPE - eSocial - S-2200 - Como executar o rdmake UPDCODUNIC, para correção de matriculas duplicadas no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466294)

**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
