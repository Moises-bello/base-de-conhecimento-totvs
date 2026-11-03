---
article_id: 360013755072
category: Contabilidade Gerencial - Plano de Contas
content_hash: 8f814507818dcd675711684716701539eb738602fada2803701286064c5181f7
fetched_at: '2026-06-28T22:40:33.336398+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: ' Cross Segmento - Backoffice Linha Protheus - SIGACTB - Na contabilização
  ocorre HELP: CTA_BLOQ'
type: support-article
updated_at: '2026-01-27T16:37:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013755072--Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Na-contabiliza%C3%A7%C3%A3o-ocorre-HELP-CTA-BLOQ
---

**Ocorrência**No módulo **Contabilidade Gerencial**, ao tentar realizar uma conta contábil, ou em processos  contabilização, ocorre a mensagem HELP CTA\_BLOQ.  
  
**Ambiente**  
Protheus – Contabilidade – A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois a parametrização do sistema está encontrando alguma amarração na entidade.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se existe dados nos campos [CT1\_RGNV1, CT1\_RGNV2, CT1\_RGNV3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-MP-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es?source=search) onde poderá conter código de amarração para a conta;  
2. Verifique se as entidades [estão configuradas para controlar saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007497491-MP-SIGACTB-CTBA130-Saldos-das-Entidades-Centro-de-Custos-Item-Conta-e-Classe-de-Valor-?source=search);  
3. Verifique, no cadastro da entidade o campo de Dt Ini Exist e data fim de existência a data contida, e compare com a data do lançamento que esta sendo gerado, confira também o campo de bloqueio se a entidade esta bloqueada;  
4. Se a conta tem o campo data inicio 01/01/18 e o lançamento for com data de 10/12/18 a conta será bloqueada, pois esta com o movimento fora da data de criação da conta.
