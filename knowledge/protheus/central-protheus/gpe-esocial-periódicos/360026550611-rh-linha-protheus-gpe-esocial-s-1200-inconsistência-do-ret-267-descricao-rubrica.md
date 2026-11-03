---
article_id: 360026550611
category: GPE - eSocial - Periódicos
content_hash: ff5f605c4c7d4091382464dfe7fa770a352fa401e61408ef2d293480a5f6402d
fetched_at: '2026-06-28T22:45:08.658010+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Inconsistência do RET - 267
  - Descricao: Rubrica incompatível com Estagiário'
type: support-article
updated_at: '2025-07-21T15:36:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026550611-RH-Linha-Protheus-GPE-eSocial-S-1200-Inconsist%C3%AAncia-do-RET-267-Descricao-Rubrica-incompat%C3%ADvel-com-Estagi%C3%A1rio
---

**Ocorrência**Descrição: Rubrica incompatível com Estagiário.   
Ação Sugerida: Se for relativa ao estagiário, não podem ser aceitas rubricas cujo Código de Incidência tributária de Contribuição Previdenciária ou Código de Incidência tributária de FGTS seja  diferente de [00].  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**A inconsistência é retornada pelo RET (Governo) quando no evento S-1200 é informado uma Rubrica/Verba (S-1010) que o Código de **Incidência tributária de Contribuição Previdenciária** ou Código de **Incidência tributária de FGTS** seja diferente de "**00 = Não é Base de Cálculo**".  
  
**Solução**Verifique no cálculo e no portal do eSocial se não existem Rubricas/Verbas com **Incidência tributária de Contribuição Previdenciária** e/ou **Incidência tributária de FGTS**, de acordo com o RET (Governo) o Trabalhador de categoria "**901 - Estagiário**" não é contemplado por esses institutos.  
  
Se sua Empresa tem Incidências nessas Rubricas/Verbas por algum motivo especifico (sindicato, acordo, customização, etc.), elas **não poderão ser utilizadas para Trabalhadores de categoria** **901 - Estagiário**, vide a mensagem de inconsistência retornada do RET (Governo).  
  
Se for fazer a alteração das Rubricas/Verbas, verifique a data base do Sistema, ela deve estar no mesmo mês da competência da folha, para que no RET (Governo) a alteração não fique com inicio superior ao mês da folha.  
  
Para uma conferência mais efetiva, gere o relatório do S-1200 e verifique no portal do eSocial todas as rubricas geradas no xml.  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no módulo GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[MP - GPE - eSocial - S-1010 - Como configurar a Natureza e Código de Incidência Tributária das Verbas/Rubricas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121291)  
[S-5001 - Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)  
  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
