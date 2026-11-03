---
article_id: 1500003409082
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 79fd46364842dbcf51173656e97ee63401634f5c3a70ffb89d49c568d13563fe
fetched_at: '2026-06-28T22:40:44.820859+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA102 - Como gerar
  o registro I157 da ECD
type: support-article
updated_at: '2024-06-28T20:51:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003409082-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-gerar-o-registro-I157-da-ECD
---

**Dúvida**Como gerar o registro I157, Transferência de saldos de Planos de Contas anterior, da ECD?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.  
  
**Solução**Ao mudar de plano de contas, em uma nova base, deve ser implantado os saldos para as novas contas. Deixando a base que contem o plano de contas antigo , como base histórica.  
  
**Procedimento em vídeo:**

**Mais sobre o assunto:**

* [Mudança no plano de contas como proceder](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018544191-MP-SIGACTB-CTBA020-Mudan%C3%A7a-no-plano-de-contas-CT1-como-proceder-)

1. Contas Patrimoniais que possuem saldo anterior - implantação de saldos (CTBA102)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003458362)

Rotina CTBA102, Posicionar sobre o lançamento que foi "implantado os saldos" em 31/12/XX

**+ outras ações + LCT. TRANSF. SALDO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24514262540695)

Caso a conta na qual deseja realizar a transferência esteja com o lançamento contábil a débito, a transferência deve ser registrada como débito, seguindo o mesmo procedimento para contas credoras.  
  
Importante que o campo CQW\_DATAAL esteja preenchido corretamente , caso contrario o I157 não será gerado no arquivo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406665303703)

     2.  Contas de Resultados ou contas sem saldo anterior.

No primeiro lançamento contábil, que houver para as novas contas “sem saldo anterior”, deverá haver o relacionamento da  “transf. de saldos” 

Na rotina de lançamentos automáticos, posicionar no lançamento + outras ações + Lançto de transp saldos. Para essa situação a pergunta Saldo zero?= SIM.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008094461)

Campos da **CQW**:

Ind. Partida: Informe se a conta nova está a Débito ou a Crédito.

Conta Antiga: Digite o número da conta antiga, lembrando que essa conta não estará mais na CT1 atual.

Centro de custo Antigo: Digite o centro de custo antigo (caso possua).

Saldo Zerado? NÃO, se este lançamento é de implantação de saldos (31/12/xx). SIM, quando a conta antiga foi zerada no período anterior.

Dt. Alteração: A data que houve a alteração do plano de contas.

3. Ao gerar o arquivo através da rotina de escrituração (CTBS001) informe o parâmetro abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11935597255063)

No arquivo TXT. O registro I157 é posicionado embaixo do registro I155 da conta nova.

O saldo do I157 deve corresponder ao saldo anterior do registro I155

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102332154)

**Importante**

Conforme manual o registro I157 só deve ser gerado:

 "...Quando não forem realizados, lançamentos contábeis transferindo o saldo da conta analítica antiga para a conta analítica nova nos registros I200 e I250".

![](https://totvssuporte.zendesk.com/attachments/token/D4lKUAInFJRSEccjywTHg7aSz/?name=inline1959921183.png)

Saiba mais

[ECD Erro campo VL\_SLD\_IN registro I157 não corresponde a soma dos saldos iniciais, registro I157](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003410762-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Erro-campo-VL-SLD-IN-registro-I157-n%C3%A3o-corresponde-a-soma-dos-saldos-iniciais-registro-I157?source=search)

[ECD0037\_ECD\_Registro\_I157](https://tdn.totvs.com/display/public/PROT/ECD0037_ECD_Registro_I157)

[ECD0041\_Lançamentos de Implantação de Saldos para geração dos registros I155 e I157](https://tdn.totvs.com/pages/releaseview.action?pageId=623892035)

[Tabelas](https://tdn.totvs.com/pages/viewpage.action?pageId=623892035)

* CT2 - Lançamentos Contábeis
* CQW - Lançamentos de Transferência de Saldos
* CSB - Itens de Movimentações - ECD
