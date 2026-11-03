---
article_id: 360057007854
category: RH - Fechamento Período
content_hash: 4205afe1f85950387bd5715c1399d57a7f694874563c77efa2039af36ba72932
fetched_at: '2026-06-28T22:43:24.478935+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - O cadastro de verba mês seguinte com o campo RV_CODMSEG
  vazio, não permite o fechamento do período
type: support-article
updated_at: '2024-06-03T20:23:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057007854-RH-Linha-Protheus-GPE-O-cadastro-de-verba-m%C3%AAs-seguinte-com-o-campo-RV-CODMSEG-vazio-n%C3%A3o-permite-o-fechamento-do-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23922066349719) Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**

No log de fechamento da folha ocorre a mensagem: "Não há cadastro de verba de mês seguinte da(s) verba(s) abaixo: 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096776254)

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Recursos Humanos - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, caso tenha verbas para o mês seguinte nos lançamentos e o campo RV\_CODMSEG estiver vazio o fechamento do período não é finalizado. Pois a verba do mês seguinte não foi informado o código da verba correspondente.  
  
**Solução**Acessar em **Atualizações -> Definições Cálculo -> Verbas (GPEA040)**, na aba **Geral** preencher o campo **RV\_CODMSEG** de todas as verbas de mês seguinte ou mês anterior com código da verba correspondente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23922104276503)

**Obs.:** Os códigos descritos no log, referem-se ao código do cadastro da verba e não aos identificadores de cálculo, ou seja, para cada cliente será gerado os códigos conforme seu cadastro de verbas.

**Saber Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)
