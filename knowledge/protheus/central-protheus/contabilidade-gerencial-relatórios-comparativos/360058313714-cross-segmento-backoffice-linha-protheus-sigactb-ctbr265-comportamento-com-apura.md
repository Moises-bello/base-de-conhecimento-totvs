---
article_id: 360058313714
category: Contabilidade Gerencial - Relatórios Comparativos
content_hash: 755ee1f622fb6cdd5c62b2696536accbcf8b286d15df07968cfb3b164bc8edc7
fetched_at: '2026-06-28T22:40:37.151480+00:00'
product: protheus
section_id: 1500001548922
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR265 Comportamento
  com apuração trimestral
type: support-article
updated_at: '2022-05-26T12:54:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058313714-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR265-Comportamento-com-apura%C3%A7%C3%A3o-trimestral
---

**Ocorrência**Comportamento do relatório CTBR265 quando a apuração de resultado foi executada [Trimestral Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)

**Ambiente**Microsiga Protheus – Contabilidade Gerencial  – A partir da versão P12  
  
**Solução**

#### Conforme documentação [Conta\_X\_12\_Meses\_CTBR265](https://tdn.totvs.com/display/public/PROT/CTB0152_Conta_X_12_MESES_CTBR265), o relatório compara as movimentações das contas entre meses, para acompanhamento da evolução dos saldos.

Como a apuração da empresa é efetuada de forma Trimestral, indicamos que seja efetuada a emissão do relatório de forma também trimestralmente no período 01/01 a 31/03, ou seja se houver mais de uma apuração no período esta não será desconsiderada. Somente será desconsiderado a Apuração de Resultado informado no parâmetro "Data Lucros e Perdas?".

De acordo com a configuração dos parâmetros "Posição Ant. L/P?" está como NÃO e a "Data Lucros e Perdas?" está em BRANCO será apresentado todos os saldos conforme indicado no período.

Considerando os lançamentos normais do período e os lançamentos de apuração, apresentando o total dos movimentos.

Saiba mais : [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR265 Ao emitir o relatório o saldo é apresentado zerado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058317434-MP-SIGACTB-CTBR265-APURA%C3%87%C3%83O-TRIMESTRAL-AO-EMITIR-O-RELAT%C3%93RIO-Posi%C3%A7%C3%A3o-Ant-L-P-como-SIM-e-a-Data-Lucros-e-Perdas-PREENCHIDO-SALDO-APRESENTADO-ZERADO?source=search)
