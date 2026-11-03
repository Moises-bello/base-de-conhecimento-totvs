---
article_id: 1500004885922
category: RH - Relatórios Folha
content_hash: 7dd041c1bd6d3da68000ee32012424120bd64047a3f307ab8c5319c823266034
fetched_at: '2026-06-28T22:43:17.440720+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar o título do rodapé do relatório de
  Folha de Pagamento
type: support-article
updated_at: '2025-08-04T11:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004885922-RH-Linha-Protheus-GPE-Como-alterar-o-t%C3%ADtulo-do-rodap%C3%A9-do-relat%C3%B3rio-de-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25976658053911) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como alterar o título do rodapé do relatório de Folha de Pagamento?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Via Configurador (SIGACFG), acesse **Ambiente > Cadastros > Parâmetros (CFGX017)**, pesquise pelo parâmetro **MV\_RODAPE** e altere o título conforme sua necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31429707348631)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31429707350807)  
No exemplo abaixo, o conteúdo do parâmetro foi definido como Relatório Periódico Folha:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31429707351575)  
  
Acessando **Relatórios > Periódicos > Folha Pagamento (GPER040)** para imprimir o relatório, veja que o rodapé estará conforme definido no parâmetro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31429707352855)

**Observação:** O parâmetro MV\_RODAPE altera o rodapé do relatório GPER040 somente, **não altera** o relatório GPER106.

**Saiba mais:**[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
