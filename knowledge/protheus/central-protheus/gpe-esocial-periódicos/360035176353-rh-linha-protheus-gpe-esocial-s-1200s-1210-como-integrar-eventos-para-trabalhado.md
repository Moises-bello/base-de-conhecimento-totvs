---
article_id: 360035176353
category: GPE - eSocial - Periódicos
content_hash: bc778586ff2d64effeaeb4560c3f46547aaaa394505d456179e3f829975941ef
fetched_at: '2026-06-28T22:45:08.791695+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-1210 - Como integrar Eventos
  para Trabalhadores que recebem por mais de um Pagamento/Semana e para que serve
  o parâmetro MV_PERAUT
type: support-article
updated_at: '2025-07-22T20:50:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035176353-RH-Linha-Protheus-GPE-eSocial-S-1200-S-1210-Como-integrar-Eventos-para-Trabalhadores-que-recebem-por-mais-de-um-Pagamento-Semana-e-para-que-serve-o-par%C3%A2metro-MV-PERAUT
---

**Dúvida**Como integrar Eventos para Trabalhadores que recebem por mais de um Pagamento/Semana e para que serve o parâmetro **MV\_PERAUT**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para integrar os eventos periódicos para Trabalhadores que recebem mais de um Pagamento/Semana, deve ser executada a rotina de integração dos eventos periódicos do GPE > Miscelânea > eSocial > Eventos Periódicos.  
  
Para essa integração ocorrer corretamente sugerimos que mantenha o conteúdo do parâmetro **MV\_PERAUT** igual a '**.T.**'.  
  
Para acessar a documentação técnica sobre a criação do parâmetro **MV\_PERAUT**, **[clique aqui](https://tdn.totvs.com/display/PROT/3852795+DRHESOCP-7981+Evento+S-1200+autonomos)**.  
  
O evento S-1210 é um evento de Pagamento e ele sempre vai gerar o evento S-1210 baseado nas datas de pagamento, ou seja, se existe **mais de um Pagamentos/Semanas** será criado **uma linha para cada data de pagamento** e consequentemente um identificador (Ident Dem Vl) diferente para cada.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045898373)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045898413)  
  
Com o parâmetro **MV\_PERAUT** igual a '**.T.**' o Sistema vai gerar no evento S-1200 uma linha de Remuneração do Trabalhador para cada Pagamento/Semana e também um identificador (Ident Dem Vl) para cada, seguindo a mesma lógica do evento S-1210 e sendo aceito pelo RET (Governo).  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045898273)  
  
Caso o parâmetro **MV\_PERAUT** esteja igual a '**.F.**' o Sistema vai gerar vai gerar uma linha no evento S-1200 aglutinando a Remuneração do Trabalhador de todos os Pagamentos/Semanas, com um único identificador (Ident Dem Vl), o que causará a inconsistência 723/724 no momento de tentar enviar o evento S-1210.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045029834)  
  
Para entender a diferença de conceito entre o evento S-1200 e S-1210 sugerimos a leitura do artigo abaixo:

- [RH - Linha Protheus - GPE - eSocial - S-1200/S-2299/S-1210 - Conteúdo do Evento x Regime de Apuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027707032-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-S-1210-Conte%C3%BAdo-do-Evento-x-Regime-de-Apura%C3%A7%C3%A3o)

Segue abaixo o artigo sobre um dos problemas que pode ocorrer com o parâmetro **MV\_PERAUT** caso esteja com conteúdo igual a '**.F.**':

- [RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência do RET - 723, 724, 726 no retorno do evento transmitido ao governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024125112-RH-Linha-Protheus-GPE-eSocial-S-1210-Inconsist%C3%AAncia-do-RET-723-724-726-no-retorno-do-evento-transmitido-ao-governo)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
