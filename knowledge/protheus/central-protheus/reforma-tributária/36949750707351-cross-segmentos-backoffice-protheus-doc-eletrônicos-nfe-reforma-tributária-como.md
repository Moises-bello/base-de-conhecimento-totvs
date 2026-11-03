---
article_id: 36949750707351
category: Reforma Tributária
content_hash: 908c7f8ab4e9bd4e92abbaf26177f51e4adb60533f5ae9f237f2922a90935b00
fetched_at: '2026-06-28T22:39:53.785818+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  – Como gerar as novas tags do grupo IBS e CBS no xml.
type: support-article
updated_at: '2025-12-11T17:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36949750707351-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Como-gerar-as-novas-tags-do-grupo-IBS-e-CBS-no-xml
---

**Dúvida**  
Como gerar as novas tags do grupo IBS e CBS no xml?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**

Primeiro passo é configurar os cálculos do IBS e CBS no protheus na rotina fisa1710 para que eles sejam destacados na planilha financeira do pedido de venda ou na aba Impostos do documento de entrada, verifique a documentação abaixo:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o calculo do IBS e CBS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS)

Para gerar as novas tags do IBS e CBS no xml é necessario que o ambiente Protheus e TSS estejam com as atualizações da documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS)

É necessario criar os parâmetros abaixo no Protheus via SIGACFG.

[Documentação do parâmetro MV\_CSTGXML](https://tdn.totvs.com/pages/viewpage.action?pageId=1011566715)

[Documentação do parâmetro MV\_RTC55](https://tdn.totvs.com/pages/viewpage.action?pageId=1013641031)

Criar os parâmetros abaixo no TSS na tabela SPED000 por entidade.

[MV\_NT25002](https://tdn.totvs.com/pages/releaseview.action?pageId=1002497291)

[MV\_RTC130](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36864716890135-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Cria%C3%A7%C3%A3o-e-atualiza%C3%A7%C3%A3o-do-par%C3%A2metro-MV-RTC130)

Abaixo um exemplo de como são geradas as tags referente ao IBS e CBS nos blocos **IBSCBS** e **IBSCBSTot**:

![tags.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36949886657303)

![tags2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36949886660631)

Validadores da sefaz:

<https://dfe-portal.svrs.rs.gov.br/Cff/ValidadorNfe>

<https://www.sefaz.rs.gov.br/NFE/NFE-VAL.aspx>
