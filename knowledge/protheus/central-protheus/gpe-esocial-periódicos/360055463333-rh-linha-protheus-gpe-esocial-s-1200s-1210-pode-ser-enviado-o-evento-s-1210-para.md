---
article_id: 360055463333
category: GPE - eSocial - Periódicos
content_hash: 3651529672f2a27c3ae29e3fc0fbf6ce7c7292fee152cc81c0c84587f9a5a06f
fetched_at: '2026-06-28T22:45:08.795883+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - Pode ser enviado o evento
  S-1210 para o governo antes de enviar o S-1200
type: support-article
updated_at: '2024-09-06T17:48:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055463333-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Pode-ser-enviado-o-evento-S-1210-para-o-governo-antes-de-enviar-o-S-1200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26178034486807)** Tempo aproximado para leitura:**00:01:00 min****Dúvida**Pode ser enviado o evento S-1210 para o governo antes de enviar o S-1200?  
Qual o pré requisito para envio do evento S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O evento S-1210 são as informações prestadas relativas aos pagamentos feitos a trabalhadores, com ou sem vínculo empregatício. Para que o eSocial recepcione o evento S-1210, o envio dos eventos S-1200, S-1202, S-1207, S-2299 ou do S-2399 devem ter sido realizados pois são eventos remuneratórios que são relacionados ao evento de pagamento (S-1210)A ordem cronológica de envio dos eventos deverá ser seguida, ou seja, realizar primeiro o envio do evento **S-1200/S-2299/S-2399** e em seguida o **S-1210**.  
  
No evento **S-1200** existe a coluna **Iden Dem Pgt** (*tag*ideDmDev) que contém a chave do recibo de pagamento criado no momento da geração dos eventos periódicos. E no evento **S-1210** na coluna **Ident Dem Vl** (*tag*ideDmDev) existe a mesma chave que está no S-1200 que pertence ao mesmo mês de referencia.   
  
Caso seja enviado o evento S-1210 antes do S-1200/S-2299/S-2399 o governo irá retornar a inconsistência 723/724 pois não foi localizado o S-1200 com a *tag* i**deDmDev** correspondente ao S-1210.  
  
Para saber mais como é formado o relacionamento dos eventos consulte o artigo:  
[MP - GPE - eSocial - S-1210 - Como é formado o relacionamento entre os eventos S-1210 e S-1200 e suas chaves de identificação ideDmDev](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018448812-MP-GPE-eSocial-S-1210-Como-%C3%A9-formado-o-relacionamento-entre-os-eventos-S-1210-e-S-1200-e-suas-chaves-de-identifica%C3%A7%C3%A3o-ideDmDev?source=search)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
Para conhecimento dos **eventos futuros**, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
