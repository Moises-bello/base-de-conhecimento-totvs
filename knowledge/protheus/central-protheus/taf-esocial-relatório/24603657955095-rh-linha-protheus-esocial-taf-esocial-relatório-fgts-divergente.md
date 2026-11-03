---
article_id: 24603657955095
category: TAF - eSocial - Relatório
content_hash: e15309a870995541aa6a17b6e61a47625a00c3779a0a67028a0dc8750779d538
fetched_at: '2026-06-28T22:45:19.933417+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Relatório FGTS Divergente.
type: support-article
updated_at: '2026-06-17T19:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24603657955095-RH-Linha-Protheus-eSocial-TAF-eSocial-Relat%C3%B3rio-FGTS-Divergente
---

**Dúvida**Relatório FGTS divergente, como validar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536661659927)

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório FGTS - (TAFA552A)- Todas as versões

**Solução**  
**1.** Validar os funcionários que estão com divergência. **Gere o relatório clicando em somente divergências**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25597316101655)

**Atenção**

**2.** Localizando os funcionários divergentes, valide se os valores relacionados as colunas do RH e TAF estão diferentes do que os valores relacionados a coluna do governo, se for esse o cenário, valide se a rubrica do valor que está diferente, está com a natureza e incidência de rubrica conforme documentação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536623051159)

**Documentação** <https://tdn.totvs.com/pages/releaseview.action?pageId=507969929#tabs-obs>

Caso a divergência seja nas colunas RH e TAF do **Deposito FGTS:**

Natureza de rubrica 9908 e com Tipo 3 - Informativa.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536637564951)**

Caso a divergência seja nas colunas RH e TAF do **Base FGTS:**

Natureza de rubrica 9902 e com o Tipo 3 - informativa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536637578391)

**2.1** Para auxiliar a encontrar a rubrica divergente siga a documentação: [RH (Linha Protheus) - eSocial - TAF eSocial - localizando a rubrica divergente no relatório de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25579577017367-RH-Linha-Protheus-eSocial-TAF-eSocial-localizando-a-rubrica-divergente-no-relat%C3%B3rio-de-confer%C3%AAncia?source=search)

**3.** Quando já souber a rubrica do valor que está dando divergência siga o passo da documentação para acessar a rotina de detalhamento de rubricas: [RH - Linha Protheus - TAF - eSocial - Eventos de tabelas - Como validar o cadastro de um evento de rubrica no TAF (S-1010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25509916713495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-tabelas-Como-validar-o-cadastro-de-um-evento-de-rubrica-no-TAF-S-1010)

A rubrica do **Deposito FGTS** terá que estar conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536623070999)

A rubrica do **Base FGTS** terá que estar conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25536637591703)

**Obs:** Caso a rubrica estiver diferente da documentação, esses valores não irão aparecer no relatório. E para ajustar a rubrica que está errada, terá que excluir o evento S-1200/S-2299 e reenviar ou retificar com a rubrica correta para ajustar o relatório.
