---
article_id: 29091308296599
category: Originação de Grãos (OG)
content_hash: ec0c3ae96f48e63b077f56cbabb5ac5678acf8bb0ede65f17b3a747c6f4c536f
fetched_at: '2026-06-28T22:45:37.536232+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Comercialização Clássica com Operação Triangular
  PT 1 em Gestão Agroindústria - Manutenção
type: support-article
updated_at: '2025-06-24T20:27:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29091308296599-Agro-Linha-Protheus-AGR-Comercializa%C3%A7%C3%A3o-Cl%C3%A1ssica-com-Opera%C3%A7%C3%A3o-Triangular-PT-1-em-Gest%C3%A3o-Agroind%C3%BAstria-Manuten%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29091332806295) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Como é realizado um processo de **Comercialização Clássica com Operação Triangular PT 1 em Gestão Agroindústria - Manutenção**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução  
Dados Gerais:**

| Produto: | TOTVS Agro Beneficiamento |
| --- | --- |

| Linha de Produto: | Linha Protheus |
| Segmento: | Agroindústria |
| Módulo: | Gestão de Agronegócio |
| Função: | OGA250 - Romaneio com pesagem |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DAGROCCO-3901 |

**Requisito/Requisito:**No romaneio disponibilizar o campo subtipo na aba comercialização para o modelo clássico.  
No atualizar do romaneio validar contrato e **TES**, se for operação triangular seta subtipo do romaneio como **45 -** **(S) Venda a Ordem**.

**Solução:**Disponibilizado os campos de subtipo e descrição do subtipo na aba comercialização.  
Ao informar o contrato no romaneio, será **gatilhado** a **TES** financeira do contrato no romaneio.  
Ao atualizar será validado se contrato é de operação triangular, caso seja, a **TES** do romaneio deverá ser igual a **TES** financeira do contrato, e será **setado** no campo subtipo o valor **45 - (S) Venda a Ordem** na aba comercialização.
