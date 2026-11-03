---
article_id: 360033101334
category: GPE - eSocial - Periódicos
content_hash: 44f54aa59d5a5cad0453b14795ecbad179b16134bb8a5ad9cb4b7da54fb76e4a
fetched_at: '2026-06-28T22:45:07.227741+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência
  do evento S-1200 no módulo GPE
type: support-article
updated_at: '2025-07-21T16:24:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27050129222423) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Como gerar relatório de conferência do evento S-1200?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**1. Acesse a rotina **Eventos Periódicos** no **SIGAGPE**;  
Caminho: *Miscelânea > eSocial > Eventos Periódicos:*  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18433806321047)  
2. Na tela dos **Eventos Periódicos**, selecione a competência e na opção **Processo > Relatório**;  
  
3. Selecione o evento **S-1200** e caso a folha esteja aberta marque a opção considerar dados do período em aberto.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27050129226135)  
  
O relatório pode ser gerado antes e depois da integração dos eventos e com roteiro da folha de pagamento aberto ou fechado.

4. Ao gerar o relatório, ele será aberto na aba que contém as informações geradas no evento S-1200 (como CPF do funcionário, ideDmDev e verba), e as informações do cadastro das verbas (como ID de cálculo, tipo da verba, incidências eSocial e incidências da Folha):

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filial do Funcionário | CPF do Funcionário | Nome do Funcionário | Categoria eSocial | ideDmDev | Estabelecimento (Tipo - Nr. Inscrição) | Lotação | Matrícula eSocial | Ind. Simples | Verba | Descrição | ID Cálculo | Tipo da Verba | Valor | Natureza | Incidência INSS eSocial | Incidência IRFF eSocial | Incidência FGTS eSocial | Incidência INSS Folha | Incidência IRRF Folha | Incidência FGTS Folha | **Data de Pagamento** |

Além dessa aba, terá outras abas que podem ou não ter informações:

* A aba **Demonstrativo Verbas** irá exibir as verbas geradas no grupo <*infoPerApur*>, além do código de natureza e as incidências para INSS, IRRF e FGTS, tanto para o eSocial quanto para a Folha.
* A aba **Dem. Plano de Saúde** irá exibir as verbas geradas no grupo <*infoSaudeColet*>, além do código do fornecedor e o código do dependente.
* A aba **MV - Outras Empresas** irá exibir as verbas geradas nos grupos <*indMV*> e <*remunOutrEmpr*>.
* A aba **Dem. Meses Anteriores-PLR** irá exibir as verbas geradas no grupo <*infoPerAnt*>, além do código de natureza e as incidências para INSS, IRRF e FGTS, tanto para o eSocial quanto para a Folha.
* A aba **S-2299-S-2399** irá exibir os funcionários que não terão o evento S-1200 devido a existência de um evento S-2299 ou S-2399 no período.
* A aba **Inconsistências** irá exibir inconsistências gerais que ocasionam que o evento não seja gerado e também as verbas que são desprezadas da geração do evento devido natureza ou incidência para IRRF, por exemplo verba do desconto de IRRF ou pensão alimentícia, que apenas são geradas no evento S-1200. Outro exemplo são verbas de pagamento da diferença do dissídio que ao invés de ser gerada no grupo <*infoPerApur*> é gerada no grupo <*infoPerAnt*>, nessa aba também é demonstrada as verbas que não estão sendo enviadas no evento S-1200, isso ocorre pois a verba esta informada no campo **RV\_CODCOM\_** de outra verba indevidamente.
* A aba **Legenda** irá exibir a descrição para os códigos de Tipos de Estabelecimento, Indicador do Simples, Tipo da Verba, Tipos de Dependente e Indicador de Tipo de Recolhimento do Múltiplo Vínculo.
* A aba **Dem. Verbas + Dem. Meses An** contem todas as verbas geradas para cada ideDemDev, assim como as incidências destas verbas, e a **data de pagamento do ideDmDev.**

Para atualização do relatório e demais fontes envolvidos, acesse [eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
  
**Saiba Mais**

Para adquirir mais conhecimento acesse os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
