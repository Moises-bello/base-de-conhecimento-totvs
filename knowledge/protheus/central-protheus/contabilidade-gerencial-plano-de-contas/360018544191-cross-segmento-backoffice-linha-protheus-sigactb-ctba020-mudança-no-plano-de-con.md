---
article_id: 360018544191
category: Contabilidade Gerencial - Plano de Contas
content_hash: 7e883acf699d545d009674dfaa0ff2997a192095f625303720e2a076456eec35
fetched_at: '2026-06-28T22:40:33.382444+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA020 Mudança no plano
  de contas  como proceder
type: support-article
updated_at: '2023-12-18T16:27:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018544191-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Mudan%C3%A7a-no-plano-de-contas-como-proceder
---

**Duvida**Mudança no plano de contas (CT1) como proceder?  
  
**Ambiente**Protheus– Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**Atualmente o Protheus não controla dois planos de contas (CT1).

Em caso de mudança de plano de conta, deverá haver uma nova estruturação de ambiente.

O ambiente anterior permanecerá como base história, para consultas e entregas anteriores.

Após encerramento de resultados (CTBA211- Apuração de resultados) no ambiente anterior, iremos cadastrar, ambiente novo, o novo plano de contas e realizar toda manutenção nos lançamentos padrões, Pontos de entradas e customizações (caso possua).

No ambiente novo, o ideal é que no último dia do ano anterior seja cadastrado os lançamentos de implantação de saldos. Para que os relatórios tenham o saldo anterior das contas Patrimoniais.

Exemplo:

Rotina CTBA102 (Lançamentos Automáticos)

31/12/17

Débito- 11100101 Conta Caixa- 5.000,00 Histórico Implantação de Saldos.

Rotina CTBR400 (Razão Contábil)

01/01/18

Saldo Anterior 5.000,00

**\*Importante!**

Para que haja apuração de resultados CTBA211, rotina que processa os zeramentos das contas de resultados, os lançamentos tem que estar na base, por isso o ideal é fazer a apuração na base anterior (onde consta toda movimentação) e só implantar no ambiente novo os saldos das contas patrimoniais.

Veja Também :

* Como gerar o registro I157 a partir do leiaute 8:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102 - Como gerar o registro I157 da ECD?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD-?source=search)

* [Como preceder no caso de troca de Contador, ou alteração no Plano de Contas durante o período da ECF a ser entregue?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008496508-MP-SIGACTB-ECF-Como-preceder-no-caso-de-troca-de-Contador-ou-altera%C3%A7%C3%A3o-no-Plano-de-Contas-durante-o-per%C3%ADodo-da-ECF-a-ser-entregue-?source=search)
