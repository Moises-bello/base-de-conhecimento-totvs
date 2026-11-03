---
article_id: 360025369431
category: Gestão de Transportes (TMS)
content_hash: 4c0c87eba9b979346706f991cb7ce2d4e205b3a6890865867d1c6330313d13f8
fetched_at: '2026-06-28T22:45:33.266112+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 663 na transmissão do MDF-e
type: support-article
updated_at: '2025-04-09T12:04:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025369431-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-663-na-transmiss%C3%A3o-do-MDF-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:18 min****Ocorrência**Rejeição **663 - Percurso informado inválido**, na transmissão do **MDF-e**.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**Parametrização/Cadastro inconsistente.   
  
**Solução**Para o **MDF-e** do modal rodoviário deverá indicar as **UF's** que serão percorridas pela unidade de carga, no grupo de informações **UF de Percurso**, sempre que existir pelo menos uma **UF** entre as **UF's** de carregamento e de descarregamento. Essa regra é aplicada sempre considerando as divisas estaduais possíveis, na ordem definida para o percurso, orientando-se da **UF** de carregamento até a **UF** de descarregamento.  
  
No módulo **SIGATMS**, em **Atualizações/ Logística/ Rotas - OMSA100,**há a aba **Percursos MDF-e**. Neste cadastro faz-se necessário informar todos os Estados que fazem fronteiras, considerando o percurso que o caminhão faz da origem até destino do **CT-e**.  
  
Exemplos de parametrização:

* **Exemplo 1:**  
  A transportadora está emitindo **CT-e** com origem no **RS** e destino **PR.**No cadastro de **Rotas**, aba **Percursos MDF-e** deverá ser inserido os seguintes Estados: **RS**, **SC** e **PR**. Caso falte algum Estado, o **MDF-e** continuará com a rejeição.

* **Exemplo 2:**  
  A transportadora emitente do **CT-e** está localizada no Estado de **GO**, porém a mercadoria será coleta no **MT** para ser entregue em **MG**. Com isso, no cadastro de **Rotas**, aba **Percursos MDF-e**, deverá ser inserido os seguintes Estados: **MT**, **GO** e **MG**, porém como o inicio da prestação de serviço começará no Estado de **MT**, no cadastro da **Rota**, no campo **Cd.Orig,MDF-e**, deverá ser informado a cidade de inicio do transporte do **MDF-e**.

**Importante**Sempre verificar o mapa do **Brasil** para que o cadastro não fique incompleto e a rejeição persista.  
  
**Saiba mais**  
Mais informações sobre o preenchimento do campo **Cd.Orig.MDF-e** podem ser verificadas no *link:* [Logística - Linha Protheus - TMS - Região de Origem do MDF-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025453271-MP-TMS-Regi%C3%A3o-de-Origem-do-MDF-e)  
  
**Glossário  
CT-e**- Conhecimento de transporte eletrônico  
**GO** - Goiás  
**MDF-e** - Manifesto de Documento Fiscal eletrônico  
**MT** - Mato Grosso  
**MG** - Minas Gerais  
**PR** - Paraná **RS** - Rio Grande do Sul  
**SIGATMS -** Gestão de Transportes  
**SC** - Santa Catarina  
**UF** - Unidade Federativa
