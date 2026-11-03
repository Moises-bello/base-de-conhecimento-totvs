---
article_id: 360052624413
category: RH - Folha de Pagamento
content_hash: 759e2e242543cab112ac0c6153bedd58c9cfa7ab4ab00fd254c358588e420632
fetched_at: '2026-06-28T22:44:15.074304+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - No Dissídio Retroativo, Sistema não considera valor
  de INSS já reajustado nos vínculos Anteriores
type: support-article
updated_at: '2024-09-04T20:13:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052624413-RH-Linha-Protheus-GPE-No-Diss%C3%ADdio-Retroativo-Sistema-n%C3%A3o-considera-valor-de-INSS-j%C3%A1-reajustado-nos-v%C3%ADnculos-Anteriores
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22248768368791) Tempo aproximado para leitura: 00:03:00 min****Ocorrência**Tratamento INSS de múltiplos vínculos.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**No novo cálculo de múltiplos vínculos (mnemônico **P\_MULTV** ativo), ao efetuar o cálculo do dissídio, o sistema não considerava o valor de INSS já reajustado nos vínculos anteriores, se já havia sido recolhido o teto do INSS no mês original, se considerar os vínculos, o sistema chegava a gerar diferença a ser recolhida no 1º  vínculo e no cálculo de folha com férias o sistema considerava o INSS de férias dos vínculos posteriores.  
  
**Solução**

Ajustes no novo cálculo de múltiplos vínculos (mnemônico **P\_MULTV** ativo):

- No dissídio, será considerado o INSS **já reajustado** no dissídio dos vínculos anteriores;

- No dissídio, será considerado o INSS descontado na folha dos outros vínculos para evitar a geração de **diferença** quando no mês original já chegou ao teto do desconto;

- Na folha, se houver férias será considerado o INSS apurado até a ordem do funcionário, ou seja, se estiver calculando o primeiro vínculo, **não** será considerado o INSS apurado nas férias do(s) vínculo(s) posterior(es). Dessa forma, pode ocorrer que nos vínculos posteriores seja devolvido a diferença descontada a mais na verba de provento do ID de cálculo 1412.  
  
Acesse o *link* a seguir para obter os pacotes de correção:   
<https://tdn.totvs.com/pages/viewpage.action?pageId=556371063>  
  
**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
