---
article_id: 30206028044439
category: GPE - eSocial - Periódicos
content_hash: f2c9d431434df8514c0f4d8d5f63bdbf4b229b7436dcab8e83c3f3fed001682f
fetched_at: '2026-06-28T22:45:07.299175+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Por que a apuração do PIS no
  eSocial (DCTFWEB) está incorreta para trabalhadores que receberam férias no período
type: support-article
updated_at: '2025-07-25T19:04:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30206028044439-RH-Linha-Protheus-GPE-eSocial-S-1200-Por-que-a-apura%C3%A7%C3%A3o-do-PIS-no-eSocial-DCTFWEB-est%C3%A1-incorreta-para-trabalhadores-que-receberam-f%C3%A9rias-no-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30206053304599) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Por que a **apuração do PIS** no eSocial (DCTFWEB) está incorreta para trabalhadores que receberam **férias** no período?Integração de roteiro FER no período de pagamento das férias para clientes que recolhem PIS apresenta valores em duplicidade na tag ***valorPisPasep*** do evento **S-5001**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**No leiaute S-1.3, o eSocial passa a totalizar a base de cálculo do PIS conforme a incidência codIncPisPasep informada no evento S-1010.  
Como as verbas de férias possuem incidência de PIS e são transmitidas no recibo de férias do período em que foram pagas,  é indispensável a criação de IDs de cálculo que atuam como contrapartida da base do PIS no recibo de férias.  
  
Efetuado a criação dos Id`s de cálculo:  
**1969** - Informativa dedução Base PIS férias   
**1970** - Informativa dedução Base PIS férias - Susp Judic.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Id Verba** | **Tipo da Verba** | **Natureza** | **Cd. Inc. CP** | **Cd. Inc. FGTS** | **Cd.Inc. IRRF** | **Cd. Inc. PIS** |
| 1969 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 00 | 00 | Sem Tributação\* | 11 |
| 1970 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 00 | 00 | Sem Tributação\* | 91 |

\* Os identificadores não terão tributação de IRRF, a escolha do código de incidência a ser utilizado nesse preenchimento é de responsabilidade da empresa.   
  
A verba de **Id 1969** tem o objetivo de ser a contrapartida da base de PIS Férias. Essa verba será composta pela somatória das verbas com incidência 11 para PIS e não irá alterar o líquido de folha do funcionário por se tratar de base e por não ter incidências para folha. Desta forma a base de PIS apurada pelo eSocial ficará correta. A verba deverá ser cadastrada com natureza informativa 9989, de tipo base (desconto) para ser utilizada como Informativa Dedutora no eSocial e com incidência 11 para PIS.  
  
A verba de **Id 1970** tem o objetivo de ser a contrapartida da base de PIS Férias, para os clientes que tem Suspensão Judicial do recolhimento do PIS.  
Foi feita uma alteração no roteiro de **Férias** para que essas verbas sejam **calculadas automaticamente**, mas para quem **já processou as férias** e gerou o evento S-1200 deve ser utilizado a rotina **GPEM026I** para geração das verbas.

[RH - Linha Protheus - GPE - Rotina GPEM026I (Antigo Rdmake UPDBINFER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER)

**Importante**

* Para os casos onde o valor de PIS está incorreto no governo é necessário que reavalie todos os tópicos abaixo, e com atenção especial a incidências de cada verba, pois muitos casos estão relacionados a ausência da rubrica ou configuração incorreta, para essa conferência utilize os relatório **[S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE)** e/ou [**S-2299**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299).  
  Também é necessário que consulte no site do governo a incidência da verba (rubrica) afim de verificar se a alteração compete ao período de apuração que está sendo realizado. **[S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534)   
  Ressaltamos que caso realize criação/ajuste de alguma verba deverá obrigatoriamente realizar o passo a passo da documentação abaixo  
  [RH - Linha Protheus - GPE - eSocial - Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254-RH-Linha-Protheus-GPE-eSocial-Como-retificar-ou-reprocessar-os-Totalizados-DCTFWEB-no-eSocial?source=search)**
* Para os casos no qual os valores de férias já estavam integrados com a folha e calculados antes de cadastrar as verbas com os ID's, temos a rotina **GPEM026I** **.** O objetivo dessa rotina é gerar ID's mencionados nessa documentação que não foram calculados nas férias (seja por inconsistência no cálculo ou ausência do cadastro das verbas) . Essa funcionalidade deve ser executada apenas após a integração do roteiro **FER**, portanto a rotina não deve ser executada caso este roteiro ainda esteja aberto, sendo necessário apenas o recálculo das férias para ajuste.
* Para ter acesso a funcionalidade é necessário que o sistema esteja com o ultimo pacote de expedição do RH, *link*: [Pacote e Dicionário Correções Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)   
  Além disso, é necessário que seja feita as orientação do tópico "**Sobre o Ajuste**" destacado na documentação do boletim técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=916390520>

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant/](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
