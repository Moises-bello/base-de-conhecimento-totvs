---
article_id: 34898703795479
category: Reforma Tributária
content_hash: dd7bcaa972e63ce27045af5bd2a84e2a63317b67fca4877aad85dd7ba4178994
fetched_at: '2026-06-28T22:39:53.707320+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  - 1094 Rejeição: Total da NFe difere da soma do total dos itens da Nota'
type: support-article
updated_at: '2025-12-02T23:25:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34898703795479-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-1094-Rejei%C3%A7%C3%A3o-Total-da-NFe-difere-da-soma-do-total-dos-itens-da-Nota
---

**Dúvida**  
Como corrigir a **Rejeição 1094**: Total da NFe difere da soma do total dos itens da Nota?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões      
  
**Solução**  
O erro ocorre pela falta da tag **vItem** no xml.

Para correção é necessario estar com fonte nfesefaz com data 17/09/2025 ou superior.

**RDMAKE**  
<https://suporte.totvs.com/portal/p/10098/download#detail/1152113>

Necessario estar com as atualizações abaixo no TSS.

**TSS**  
**1.** **Arquivos de Schema:**[Download dos schemas](https://suporte.totvs.com/portal/p/10098/download?e=761857)  
Apoio caso necessário: [Procedimento: Substituir na pasta schemas do TSS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**2.** **Atualizar RPO do TSS:** [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS) Atualizado em 19/09/2025  
Documentação: [maiores detalhes.](https://tdn.totvs.com/pages/releaseview.action?pageId=956646956)  
  
**Caso esteja na release 12.1.2310 sem garantia estendida, será necessário a migração para a release 12.1.2410:**  
- Veja como **migrar o TSS** [**aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038065954-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Migra%C3%A7%C3%A3o-para-12-1-2410-Instala%C3%A7%C3%A3o)!

**Para montar a tag vItem em produção facultativa antes de 05/01/2026, precisa criar o parâmetro MV\_NT25002 = 10/11/2025 na tabela SPED000 do TSS para a entidade que deseja mandar IBS e CBS um produção.**

Obs: Caso já possua a tag vItem e esteja ocorrendo a rejeição 1094, será necessario entrar em contato com suporte Totvs para analisar o xml e tabelas CJ3 e F2D.

Para maiores informações consulte a documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária – Nota Técnica 2025.002 v.1.10 e v1.20. IBS - CBS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-e-v1-20-IBS-CBS)
