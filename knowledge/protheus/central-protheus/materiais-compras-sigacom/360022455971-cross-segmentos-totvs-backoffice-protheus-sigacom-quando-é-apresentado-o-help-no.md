---
article_id: 360022455971
category: Materiais - Compras (SIGACOM)
content_hash: 10e0b648d127d5f0c4bbea9a8b9dc0ba72c63a57d68b9dd0b7d7d0b352924309
fetched_at: '2026-06-28T22:41:10.420587+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quando é apresentado
  o Help NOAMARRA01 na rotina Documento de Entrada (MATA103) ?
type: support-article
updated_at: '2022-09-20T19:38:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022455971-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quando-%C3%A9-apresentado-o-Help-NOAMARRA01-na-rotina-Documento-de-Entrada-MATA103
---

**Dúvida**Quando é apresentado o Help NOAMARRA01 na rotina Documento de Entrada (MATA103) ?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**A validação (**NOAMARRA01**) é feita nos campos CTT->**CTT\_CRGNV1** e CT1->**CT1\_RGNV1**, onde a validação encontra divergência nos campos de acordo com a regra estipulada pelo analista.  
  
Exatamente, ao utilizar o parâmetro MV\_CTBAMAR com o conteúdo 1 ou 2 e existir amarrações para a conta contábil e centro de custo, a validação será feita também na inclusão da solicitação do armazém.   
  
Por exemplo:  
- MV\_CTBAMAR = 1  
- Conta Contabil (CT1\_RGNV1) = 001  
- Centro de custo (CTT\_CRGNV1) = 001  
  
Se incluso uma Solicitação de Armazém informando o centro de custo 001 porém a conta contábil não for a 001, será Apresentado o assistente "**NOAMARRA01**", pois conforme definido na regra, o centro de custo 001 só pode ser incluso com a conta contábil 001.  
  
**MV\_CTBAMAR**  
Indica se ativa controle de amarração nos lançamentos contábeis.  
**0** - Não tem amarração;  
**1** - Regra de níveis;  
**2** - Regra de amarração tabela CTA.

![Help_NOAMARRA01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360019507592/Help_NOAMARRA01.png)

Verifique como está configurada a regra nas tabelas de Centro de Custo e Conta Contábil e caso necessário faça o acerto.

Outro ponto a ser analisado é como está configurado o parâmetro ***MV\_DAMARCT***:  .T. / .F.

A criação do parâmetro ***MV\_DAMARCT*** permite desconsiderar ou manter a checagem da amarração Conta Contábil x Centro de Custo na inclusão de Documentos de Entrada, tanto para o tipo Normal quanto de Devolução, bem como no rateio do mesmo.  
  
***MV\_DAMARCT:*** Desconsidera checagem da amarração contábil na inclusão de documento de entrada. .T. = Desconsidera checagem; .F. = Considera checagem.

**Rotina de validação das amarrações** :

CTBA250 disponível no módulo 34 - contabilidade gerencial.

[**CTBA250 - Validação de amarrações de entidades contábeis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006746912-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA250-Valida%C3%A7%C3%A3o-de-Amarra%C3%A7%C3%B5es)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
