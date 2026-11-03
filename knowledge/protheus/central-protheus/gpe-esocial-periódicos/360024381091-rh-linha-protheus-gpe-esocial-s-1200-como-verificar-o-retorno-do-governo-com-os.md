---
article_id: 360024381091
category: GPE - eSocial - Periódicos
content_hash: 924be64c1b8ff51cecf25be725cf031a5c6e03934b1033d56f9bde1e2af4a3db
fetched_at: '2026-06-28T22:45:07.232427+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como verificar o retorno do
  governo com os valores do FGTS nos eventos S-5003 e S-5013
type: support-article
updated_at: '2025-07-21T15:35:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024381091-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-verificar-o-retorno-do-governo-com-os-valores-do-FGTS-nos-eventos-S-5003-e-S-5013
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33610832421911) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como verificar o retorno do governo com os valores do FGTS nos eventos S-5003 e S-5013?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**Quando transmitido o evento **S-1200** para o eSocial, o governo retorna o evento **S-5003 FGTS por Trabalhador** para o **TAF** onde é possível analisar os valores apurados pelo governo.   
  
Somente após o envio do **S-1299** (Fechamento dos Eventos Periódicos) o governo vai retornar as informações no evento **S-5013 FGTS por Contribuinte.**Para que o sistema receba o retorno do governo é necessário que o sistema esteja atualizado com os últimos pacotes da página [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) e que o parâmetro **MV\_TAFVLES** seja definido com S\_01\_03\_00.  
  
No TAF, após o envio do evento S-1200 ao eSocial é possível conferir os valores retornados pelo evento S-5003, gerando o relatório de conferência do FGTS:  
[TAF - Relatório - Acessando o Painel de Conferência de FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055612014-RH-Linha-Protheus-TAF-Relat%C3%B3rio-Acessando-o-Painel-de-Confer%C3%AAncia-de-FGTS)  
  
E após o envio do evento S-1299 ao eSocial é possível conferir os valores retornados pelo evento S-5013, gerando o relatório de conferência do FGTS:  
[TAF eSocial - Totalizadores - S-5013 - Como acessar a rotina de FGTS por Contribuinte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037660674-RH-Linha-Protheus-eSocial-TAF-eSocial-Totalizadores-S-5013-Como-acessar-a-rotina-de-FGTS-por-Contribuinte) 

**Saiba Mais**Para adquirir mais conhecimento acesse os links abaixo:   
[Manual de Orientação do FGTS](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-0-18-08-2023.pdf)   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
