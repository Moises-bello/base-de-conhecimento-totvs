---
article_id: 360027512652
category: GPE - eSocial - Periódicos
content_hash: 18ea2f123b369c14a49b0db4a8856a43150bc7b2bd37624ea5dbd6f584a5c08c
fetched_at: '2026-06-28T22:45:07.739925+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como informar o FGTS para funcionários
  afastados no eSocial
type: support-article
updated_at: '2025-07-21T15:02:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027512652-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-informar-o-FGTS-para-funcion%C3%A1rios-afastados-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22331201153687) Tempo aproximado para leitura: 00:01:30 min**  
**Dúvida**Como informar o FGTS para funcionários afastados no eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O FGTS no eSocial é apurado com base nos valores das Verbas/Rubricas informadas ao RET (Governo) através do evento S-1200.  
  
Para que o Sistema receba o retorno do RET (Governo) dos totalizadores S-5003 e S-5013 é necessário que o Sistema esteja atualizado com os últimos pacotes da página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw).  
  
Também é necessário verificar se as Verbas/Rubricas que compõem a base de Cálculo do FGTS estão com o **código de incidência correto no RET (Governo).**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22330624856215)  
  
Há situações que o Trabalhador não tem remuneração, mas tem base de cálculo da FGTS, nos casos de Acidente de Trabalho o Sistema gera a verba de ID **1432 - Valor de Afastamento por Acidente pago pela Previdência** e ela pode ser utilizada com código de incidência de FGTS para o eSocial compor a base de cálculo, sugerimos utilizar a **incidência FGTS [codIncFGTS] 11.**Essa alteração deve ser realiza no cadastro de verbas **somente na aba eSocial,** a aba incidências de folha deve continuar como '**Não**' para FGTS.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046209154)  
  
Por fim deve-se verificar se foi gerado um evento S-1200 para o Trabalhador Afastado e se todas as verbas da Folha de Pagamento do GPE estão sendo informadas nele.  
  
**Observação**: Em alguns casos de afastamento só será gerado o evento S-1200 e/ou S-1210 se selecionada as opções destacadas abaixo da rotina do GPE de integração dos Eventos Periódicos.  
  
![](https://totvssuporte.zendesk.com/attachments/token/QpEPlBqgkBEFk47ucwy5QB14D/?name=inline397737213.png)  
 **Saiba Mais**Para adquirir mais conhecimento acesse os *links* abaixo:   
[Como configurar a Natureza e Código de Incidência Tributária das Verbas/Rubricas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121291)  
[RH - FGTS Digital](https://centraldeatendimento.totvs.com/hc/pt-br/sections/17829152532503-RH-FGTS-Digital)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
