---
article_id: 24605214247191
category: TAF - eSocial - Relatório
content_hash: 539ee8133474a4325223a380efcf771165b74d9534e9cb0d20b9c0dee295ad1e
fetched_at: '2026-06-28T22:45:19.942834+00:00'
product: protheus
section_id: 1500001536821
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS Divergente
type: support-article
updated_at: '2026-05-18T13:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24605214247191-RH-Linha-Protheus-eSocial-TAF-eSocial-Relat%C3%B3rio-INSS-Divergente
---

**Dúvida**Relatório INSS divergente, como validar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25535455357975)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Relatório INSS- (TAFA552A)- Todas as versões  
  
**Solução**  
**1.** Validar os funcionários que estão com divergência. **Gere o relatório clicando em Somente divergências**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25534560086679)

**Atenção**

**2.** Localizando os funcionários divergentes, valide se os valores relacionados as colunas do TAF estão diferentes do que os valores relacionados a coluna do governo, se for esse o cenário, valide se a rubrica que está levando esse valor que está dando a diferença, se está com a natureza e incidência de rubrica conforme documentação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25534771623319)

**Documentação** <https://tdn.totvs.com/pages/releaseview.action?pageId=394211788>

Caso a divergência seja nas colunas do **Valor INSS.**

Natureza de rubrica 9201 e com a incidência 31

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25533965668503)

Caso a divergência seja nas colunas do **Base INSS.**

Natureza de rubrica 9901 e  com Tipo 3 informativo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25533965673111)

**2.1** Para auxiliar a encontrar a rubrica divergente siga a documentação: [RH (Linha Protheus) - eSocial - TAF eSocial - localizando a rubrica divergente no relatório de conferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25579577017367-RH-Linha-Protheus-eSocial-TAF-eSocial-localizando-a-rubrica-divergente-no-relat%C3%B3rio-de-confer%C3%AAncia?source=search)

**3.** Quando já souber a rubrica do valor que está dando divergência siga o passo da documentação para acessar a rotina de detalhamento de rubricas: [RH - Linha Protheus - TAF - eSocial - Eventos de tabelas - Como validar o cadastro de um evento de rubrica no TAF (S-1010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25509916713495-RH-Linha-Protheus-TAF-eSocial-Eventos-de-tabelas-Como-validar-o-cadastro-de-um-evento-de-rubrica-no-TAF-S-1010)

Ao acessar a rotina de detalhamento valide se a rubrica está conforme abaixo:

A rubrica do **Valor INSS** terá que estar conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25533987607063)

A rubrica do **Base INSS** terá que estar conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25533987612439)

**Obs:** Caso a rubrica estiver diferente da documentação, esses valores não irão aparecer no relatório. E para ajustar a rubrica que está errada, terá que excluir o evento S-1200/S-2299 e reenviar ou retificar com a rubrica correta para ajustar o relatório.
