---
article_id: 6391991572759
category: GPE - eSocial - Carga Inicial
content_hash: 590f416ed3ed9967017d6f79146779ee9a8afe7f66fb94613611bcf7a468cf06
fetched_at: '2026-06-28T22:45:03.023085+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial -  O que analisar quando alteramos o campo
  RV_INCIRF e o sistema emite a mensagem: A partir do dia 01/05/2021, as verbas não
  poderão ser aceitas com este código de incidência de IRRF'
type: support-article
updated_at: '2025-08-27T20:27:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6391991572759-RH-Linha-Protheus-GPE-eSocial-O-que-analisar-quando-alteramos-o-campo-RV-INCIRF-e-o-sistema-emite-a-mensagem-A-partir-do-dia-01-05-2021-as-verbas-n%C3%A3o-poder%C3%A3o-ser-aceitas-com-este-c%C3%B3digo-de-incid%C3%AAncia-de-IRRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25790792907671)** Tempo aproximado para leitura: **00:01:00 min** **Dúvida**O que analisar quando alteramos o campo **RV\_INCIRF** e o sistema emite a mensagem: A partir do dia 01/05/2021, as verbas não poderão ser aceitas com este código de incidência de IRRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Com a alteração dos parâmetros MV\_VLESOC e MV\_TAFVLES o sistema passa a validar os campos e informações do cadastro de verbas para atender o leiaute simplificado.  
  
Conforme Manual de Orientação do eSocial, as rubricas cujos valores não são considerados na tributação de IRPF devem ter o campo {codIncIRRF} preenchido conforme a **[Tabela 21](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/tabelas.html#21)**. Para visualização acesse a [documentação técnica esocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) e selecione o leiaute vigente.  
  
**Inconsistência apresentada ao utilizar o código de incidência IRRF 0**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25793792070551)  
  
  
É possível também verificar na **[Tabela 21](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/tabelas.html#21)** que existem códigos com **data término**, pois o **eSocial cessou** o envio e utilização desses códigos de incidência. No **Protheus**, ao informar um desses códigos com data término, será emitida a mensagem que as verbas não poderão ser aceitas.  
  
Veja abaixo alguns que retiramos do leiaute simplificado como exemplo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF** | | | |
| **CÓDIGO** | **DESCRIÇÃO** | **INÍCIO** | **TÉRMINO** |
| 0 | Rendimento não tributável | 01/10/2015 | 30/06/2021 |
| 1 | Rendimento não tributável em função de acordos internacionais de bitributação | 01/10/2015 | 30/06/2021 |
| 15 | Rendimentos Recebidos Acumuladamente - RRA | 01/10/2015 | 30/06/2021 |
| 35 | Rendimentos Recebidos Acumuladamente - RRA | 01/10/2015 | 30/06/2021 |
| 44 | PSO - RRA | 01/10/2015 | 30/06/2021 |
| 55 | Pensão alimentícia - RRA | 01/10/2015 | 30/06/2021 |
| 78 | Valores pagos a titular ou sócio de microempresa ou empresa de pequeno porte, exceto pró-labore e aluguéis | 01/10/2015 | 30/06/2021 |
| 81 | Depósito judicial | 01/10/2015 | 30/06/2021 |
| 82 | Compensação judicial do ano-calendário | 01/10/2015 | 30/06/2021 |
| 83 | Compensação judicial de anos anteriores | 01/10/2015 | 30/06/2021 |
| 91 | Remuneração mensal | 01/10/2015 | 30/06/2021 |
| 92 | 13º salário | 01/10/2015 | 30/06/2021 |
| 93 | Férias | 01/10/2015 | 30/06/2021 |
| 94 | PLR | 01/10/2015 | 30/06/2021 |
| 95 | RRA | 01/10/2015 | 30/06/2021 |

O Protheus sofreu alteração na tabela S138 para adequação da tabela de rubricas, assim como estipulado no leiaute simplificado: [RH - Linha Protheus - GPE - Tabela S138 Códigos de Incidência Tributária da Rubrica para o IRRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409044099223-RH-Linha-Protheus-GPE-Tabela-S138-C%C3%B3digos-de-Incid%C3%AAncia-Tribut%C3%A1ria-da-Rubrica-para-o-IRRF)  
Veja o boletim técnico: **[Tabela de Verbas: Dicionário V.1 e rotina de Cadastro de verbas](https://tdn.totvs.com/pages/releaseview.action?pageId=590020960#)**Deve ser analisado a tabela 21 de Rubricas do governo e informar o código de acordo com analise que se adeque a verba que está sendo criada ou alterada.  ![smartclient_hHGNa9TzLs.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6391984095511)  
  
**Atenção:** Ao confirmar a alteração, pois o sistema perguntará a competência. Exemplo, se informado 06/2022 o sistema e o esocial entenderão a alteração somente para eventos enviados da competência 06 ou posterior.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25790792911127)  
  
O sistema deve estar devidamente atualizado com os pacotes disponibilizados em nossa página centralizadora [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
 **Saiba Mais**  
Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
