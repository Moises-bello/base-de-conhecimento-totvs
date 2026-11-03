---
article_id: 6778582967063
category: GPE - eSocial - Periódicos
content_hash: 71aab402e3c723c1c04508d34cdf7f5d4e93f380c037e5617a67e005ea91d82b
fetched_at: '2026-06-28T22:45:08.595983+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Diferença no INSS quando existe
  Férias no mês e verba com incidência de suspensão 91 ou 95
type: support-article
updated_at: '2025-07-23T20:34:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6778582967063-RH-Linha-Protheus-GPE-eSocial-S-1200-Diferen%C3%A7a-no-INSS-quando-existe-F%C3%A9rias-no-m%C3%AAs-e-verba-com-incid%C3%AAncia-de-suspens%C3%A3o-91-ou-95
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25783483670295) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**  
Diferença no INSS quando existe Férias no mês e verba com incidência de suspensão.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**Em casos que existe **suspensão de incidência sobre salário de contribuição em decorrência de decisão judicial em verbas de férias**, como por exemplo verbas com incidência de INSS com código **91** (Mensal), **95** (Exclusiva do empregador - Mensal) nas férias o valor de Base e Desconto de INSS fica divergente no eSocial.   
Isso ocorre porque no *layout* simplificado as informações dos valores de Férias são geradas no S-1200 em recibo separado, e também é gerado novamente no recibo de folha, isso faz com que duplique o valor que esta com incidências de suspensão pois a verba é gerada no recibo **FOL** e recibo **FER**.  
  
**Solução**Para que o valor fique correto no governo é necessário que exista no calculo de férias as verbas com os IDs **1891** para incidência de suspensão **91** e **1892** para incidência de suspensão **95.**Abaixo existe um quadro com as informações de como deve ser preenchido as verbas:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Id Verba** | **Tipo da Verba** | **Natureza** | **Cd. Inc. CP** | **Cd. Inc. FGTS** | **Cd.Inc. IRRF** | **Incidência Folha** |
| 1891 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 91 | 00 | Sem Tributação\* | Não |
| 1892 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 95 | 00 | Sem Tributação\* | Não |

\* Os identificadores não terão tributação de IRRF, o preenchimento dessa informação é de responsabilidade da empresa. Para essa configuração orientamos verificar a [tabela 21](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-nt-05-2022-html/tabelas.html#21) do Leiaute*.***Atenção**

Com as verbas cadastradas corretamente, as verbas com incidência INSS e FGTS devem apresentar no cálculo FER, e a de IRRF no cálculo FOL. Caso não esteja deve ser executado o UPDBINFER, conforme apresentado na documentação: [RH - Linha Protheus - GPE - Rotina GPEM026I (Antigo Rdmake UPDBINFER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER).  
  
Para casos onde o valor de INSS está incorreto no governo, é necessário que reavalie todos os tópicos anteriores, e com atenção especial a incidências de cada verba, pois muitos casos está relacionado a tributação incorreta.   
Também é necessário que consulte no site do governo a incidência da verba (rubrica): [S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534)

Caso seja necessário fazer algum ajuste de incidência, ou verbas, será necessário enviar o S-1200 novamente ao governo para reprocessar as informações da base de calculo. Consulte: [Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254)

**Importante:**

* Para os casos onde já existe verbas com os IDs **1891** ou **1892** no cálculo das férias, não é necessário executar a [Rotina GPEM026I (Antigo Rdmake UPDBINFER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER).
* Para os casos no qual os valores de férias já estavam calculados antes de cadastrar as verbas com os ID's, existe a [Rotina GPEM026I (Antigo Rdmake UPDBINFER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER) que gera os ID's dentro do calculo já realizado. A Rotina GPEM026I deve ser executado apenas após a integração do roteiro **FER**, portanto a rotina não deve ser executada caso este roteiro ainda esteja aberto.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[S-1200 - O INSS, FGTS e IRRF fica incorreto no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
