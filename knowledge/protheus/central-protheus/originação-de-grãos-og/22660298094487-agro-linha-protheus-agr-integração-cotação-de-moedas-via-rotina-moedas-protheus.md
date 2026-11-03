---
article_id: 22660298094487
category: Originação de Grãos (OG)
content_hash: 733f3aa296db2a2b2e91639ea56a73c82503d1e1abab2d064e5fc29f120ccbec
fetched_at: '2026-06-28T22:45:39.653978+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Integração Cotação de Moedas Via Rotina Moedas
  PROTHEUS X EXTERNO - OGA011 em Integração moeda, índice, commodities
type: support-article
updated_at: '2025-01-03T19:30:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22660298094487-Agro-Linha-Protheus-AGR-Integra%C3%A7%C3%A3o-Cota%C3%A7%C3%A3o-de-Moedas-Via-Rotina-Moedas-PROTHEUS-X-EXTERNO-OGA011-em-Integra%C3%A7%C3%A3o-moeda-%C3%ADndice-commodities
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22660298081943) Tempo aproximado para leitura: **00****:02:00 min** **Dúvida**  
Como configurar uma ****Integração Cotação de Moedas Via Rotina Moedas PROTHEUS X EXTERNO - OGA011******em Integração moeda, índice, commodities**?  
  
**Ambiente**TOTVS Agro – TOTVS Agro – Comercialização (Linha Protheus) - Originação de Grãos (OG) – Versão 12  
  
**Solução**Para solucionar essa dúvida, será necessário configurar os parâmetros: **[MV\_AGRO200](https://tdn.totvs.com/x/bpEOFQ), [MV\_AGRO201](https://tdn.totvs.com/pages/viewpage.action?pageId=353276354), [MV\_AGRO202](https://tdn.totvs.com/pages/viewpage.action?pageId=539531069),** **[MV\_AGRO202](https://tdn.totvs.com/pages/viewpage.action?pageId=539531069), [MV\_AGRO203](https://tdn.totvs.com/x/KZIOFQ) e**[**MV\_AGRO204**](https://tdn.totvs.com/x/rpIOFQ), realize os seguintes passos abaixo:

**1.** Verifique, no módulo de **Gestão de Agronegócio**, acessando o menu **Atualizações > Comercialização > Cadastros Básicos > Moeda Protheus x Externo**. Exclusivamente para Moedas, nesse programa devem ser informados os códigos externos correspondente a moeda que deverá ser requisitado ao parceiro **M2M**, para que o mesmo disponibilize as respectivas cotações; 

**2.** Veja na imagem abaixo é apresentado um exemplo do cadastro da **Moeda Protheus x Externo**;

![INT.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22670572553367)

**3.** Faça a integração e atualização da **Cotação Atual da Moeda** do dia é necessário preencher o campo **Cód. Atual** com o código externo que o parceiro **M2M** disponibiliza;

**4.** Realize a integração e atualização da **Cotação futura da Moeda** é necessário preencher o campo **Cód. Futuro** com o código externo que o parceiro **M2M** disponibiliza;

**5.** Realize a integração por demanda da cotação da moeda, acessando no menu em**Outras Ações > Atualizar Cotação**;

![INT1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22670856631959)

**6.** Observe que para conferência, a **Cotação da Moeda** poderá ser verificada na rotina **Moedas - MATA090**.
