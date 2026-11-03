---
article_id: 360020205051
category: GPE - eSocial - Periódicos
content_hash: b76c79ea740d6526615853add9a7c7d391afbeaf26dee34ec5c974b8d110e499
fetched_at: '2026-06-28T22:45:07.271972+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 553
  - Grupo #39;Informacoes complementares contratuais do trabalhador#39; nao deve ser
  preenchido ou deve ser preenchido. Verifique as condicoes de preenchimento no leiaute'
type: support-article
updated_at: '2026-06-26T19:17:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205051-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-553-Grupo-39-Informacoes-complementares-contratuais-do-trabalhador-39-nao-deve-ser-preenchido-ou-deve-ser-preenchido-Verifique-as-condicoes-de-preenchimento-no-leiaute
---

**Ocorrência**Inconsistência do RET - 553 - Grupo #39;Informacoes complementares contratuais do trabalhador#39; nao deve ser preenchido ou deve ser preenchido. Verifique as condicoes de preenchimento no leiaute  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Normalmente o erro ocorre na tentativa de envio do evento S-1200 quando o Trabalhador Sem Vínculo tem um evento S-2300 protocolado no RET (Governo) e dentro do evento S-1200 estão preenchidas as informações complementares ou não estão sendo preenchidas.  
  
O conceito de informações complementares de Trabalhadores Sem Vínculo é trazido no item 25 do evento S-1200 dentro do **Leiaute S-1.2.****Tag [infoComplem](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-versao-s-1-2-nt-04-2024/index.html#1200_ideTrabalhador_infoComplem)**  
Grupo preenchido quando o evento de remuneração se referir a trabalhador cuja categoria não está sujeita ao evento de admissão ou ao evento TSVE - Início, bem como para informar remuneração devida pela empresa sucessora a empregado desligado ainda na sucedida. No caso das categorias em que o envio do evento TSVE - Início for opcional, o preenchimento do grupo somente é exigido se não houver o respectivo evento. As informações complementares são necessárias para correta identificação do trabalhador.  
  
**Solução****1 -** Ambiente esteja atualizado com os últimos pacotes disponibilizados através da página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw);  
  
**2 -** Verifique a necessidade de envio do evento S-2300 de acordo com cada categoria - **[MP - GPE - eSocial - S-2300 - Como gerar trabalhador autônomo (trabalhador sem vinculo) no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013341771)**;  
  
**3 -** Certifique-se que as informações complementares **NÃO estejam preenchidas** no evento S-1200 para os Trabalhadores Sem Vínculo **que têm evento S-2300 protocolizado no RET (Governo)**.  
  
**4 -**Para gerar as informações complementares (Nome, data de nascimento e CBO e se o trabalho é urbano ou rural) o sistema realiza a verificação no cadastro do trabalhador no TAF tabela (C9V), ou seja, caso exista um evento S-2300 para o autônomo, o evento S-1200 será enviado sem as informações complementares, e caso não exista o S-2300 será enviado com as informações complementares.  
  
Para facilitar a conferencia, gere o xml do S-1200 no GPE e no TAF:  
[**TAF**: Como gerar ou comparar os arquivos XML do SIGAGPE e SIGATAF.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026656853-RH-Linha-Protheus-GPE-eSocial-Como-gerar-ou-comparar-os-arquivos-XML-do-SIGAGPE-e-SIGATAF-dentro-do-m%C3%B3dulo-SIGATAF)  
**GPE**: Acesse o modulo configurador (SIGACFG) e altere o parâmetro MV\_XMLGPE para .T. conforme detalhado no artigo: [Como definir o local onde é gerado os arquivos XML's de eventos eSocial quando utilizado o parâmetro MV\_XMLGPE.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035286913-RH-Linha-Protheus-GPE-eSocial-Como-definir-o-local-onde-%C3%A9-gerado-os-arquivos-XML-s-de-eventos-eSocial-quando-utilizado-o-par%C3%A2metro-MV-XMLGPE)

**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
