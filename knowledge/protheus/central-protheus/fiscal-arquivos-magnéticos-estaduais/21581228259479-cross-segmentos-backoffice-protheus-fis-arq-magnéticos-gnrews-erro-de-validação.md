---
article_id: 21581228259479
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 931e625de8f05ee00b3af46d2a59ec9ef99fa88495e1615a1e083c75926bd00d
fetched_at: '2026-06-28T22:42:09.183357+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - GNREWS - Erro
  de validação 215 - "Descrição: A receita informada exige um produto!"'
type: support-article
updated_at: '2024-02-26T16:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21581228259479-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNREWS-Erro-de-valida%C3%A7%C3%A3o-215-Descri%C3%A7%C3%A3o-A-receita-informada-exige-um-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21581274334871) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir a **GNRE WS** pela rotina **FISA095** acontece erro de validação:

**215 - "Descrição: A receita informada exige um produto!"**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21581274335895)  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Conteúdo vazio ou incorreto no campo **F6\_CODPROD** da guia de recolhimento .  
  
**Solução**

Para corrigir esse erro , preencha o código do produto (**F6\_CODPROD**) na guia de recolhimento (**tabela SF6**)

O preenchimento tem de ser feito conforme os produtos disponíveis para a **UF** de destino da **Guia e Código da Receita** usado, disponíveis no **Portal da GNRE**:

<http://www.gnre.pe.gov.br/gnre/portal/automacao.jsp#>

Exemplo*:*

![](https://totvssuporte.zendesk.com/attachments/token/8yXJ53UPwtnVzku6PLzK5PQbE/?name=inline-294346736.png)
