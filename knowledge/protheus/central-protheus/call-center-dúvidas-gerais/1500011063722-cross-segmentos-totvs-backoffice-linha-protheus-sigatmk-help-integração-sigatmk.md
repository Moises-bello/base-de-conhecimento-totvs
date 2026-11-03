---
article_id: 1500011063722
category: Call Center - Dúvidas Gerais
content_hash: a6808d77814e5ec6ed54bf9e538b0c37f076dc0a8ea4be7c1bf23004b20bae39
fetched_at: '2026-06-28T22:41:26.780907+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGATMK - Help integração
  SIGATMK x SIGAQNC
type: support-article
updated_at: '2021-05-17T18:17:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011063722-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Help-integra%C3%A7%C3%A3o-SIGATMK-x-SIGAQNC
---

**Ocorrência**Ao acessar a rotina de Atendimentos do Call Center (TMKA271) e tentar incluir um atendimento, o sistema apresenta um help informando "Devido a integração com Ambiente SIGAQNC Verificar parametros referentes com o Controle de Nao-Conformidades E necessário a configuração dos parâmetros: **MV\_QNCFORI / MV\_QNCDORI / MV\_QNCFDES / MV\_QNCDDES / MV\_QNCFRES / MV\_QNCMRES.**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Call Center (SIGATMK) - Todas as versões.  
  
**Causa**Ao habilitar a integração entre o módulo "Call Center" (SIGATMK) e o módulo "Controle de Não-Conformidades" (SIGAQNC) através do parâmetro **MV\_QLYXCAL (.T.)**, o sistema passa a validar se os demais parâmetros do módulo de "Controle de Não-Conformidades" (SIGAQNC) estão habilitados:

* **MV\_QNCFORI**: Define, na Integração com o SIGAQNC, a Filial Origem da FNC;
* **MV\_QNCDORI**: Define, na Integração com o SIGAQNC, o Departamento Origem da FNC;
* **MV\_QNCFDES**: Define, na Integração com o SIGAQNC, a Filial Destino da FNC;
* **MV\_QNCDDES**: Define, na Integração com o SIGAQNC, o Departamento Destino da FNC;
* **MV\_QNCFRES**: Define, na Integração com o SIGAQNC, a Filial do Responsável da FNC;
* **MV\_QNCMRES**: Define, na Integração com o SIGAQNC, a Matricula do Responsável da FNC.

**Solução**

* Caso **não utilize** a integração com o módulo "Controle de Não-Conformidades" (SIGAQNC), desabilite o parâmetro **MV\_QLYXCAL (.F.)**;
* Caso **utilize** a integração realize a configuração dos parâmetros citados acima.

Necessitando de suporte quanto ao preenchimento dos parâmetros, entre em contato com o time de Suporte ao módulo "Controle de Não-Conformidades" (SIGAQNC).
