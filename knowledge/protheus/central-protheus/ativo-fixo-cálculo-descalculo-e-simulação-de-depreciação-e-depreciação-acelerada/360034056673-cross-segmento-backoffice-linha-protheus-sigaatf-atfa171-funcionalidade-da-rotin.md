---
article_id: 360034056673
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: ebe6def2bfbea2567df8b8a08062d2a90ffedf93b95db1fe8a4bb02368b71ad5
fetched_at: '2026-06-28T22:41:43.304555+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA171 FUNCIONALIDADE
  DA ROTINA  -DEPRECIAÇÃO ACELERADA
type: support-article
updated_at: '2023-06-30T12:49:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034056673-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA171-FUNCIONALIDADE-DA-ROTINA-DEPRECIA%C3%87%C3%83O-ACELERADA
---

**Dúvida**Como que funciona a rotina de depreciação acelerada no Protheus?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução:**

A rotina de depreciação acelerada possui os seguintes coeficientes:

A) 1,5 - para dois turnos de 8 horas de operação

B) 2,0 - para três turnos de 8 horas de operação

Nessas condições, um bem, cuja taxa normal de depreciação é de 10% ao ano, poderá ser depreciado em 15% ao ano se operar 16 horas por dia ou 20% ao ano operando 24 horas por dia.

Proporcional:

Com esta rotina, a empresa poderá utilizar o bem em um período determinado do mês, aplicando uma taxa específica de 15% (bem operante por 16 horas), que corresponderá à depreciação acelerada, justificada pelo excesso de utilização deste bem neste período e para  
o restante do mês utilizará a taxa normal de depreciação de 10%, calculada pela rotina Cálculo mensal.

Somente poderá se executar a depreciação acelerada dentro do mês do próximo cálculo de depreciação. O sistema utiliza a data-base como referência para registrar tanto o movimento da depreciação acelerada como para atualizar os saldos das contas. No último dia do mês, o usuário gerará pela rotina de Cálculo Mensal o cálculo correspondente à depreciação mensal. Se neste período também acontecer o cálculo de depreciação acelerada para alguns bens, este valor será subtraído do valor total da depreciação para obtenção do valor da depreciação contábil do mês. Na contabilização, a depreciação acelerada utiliza o lançamento padronizado 840.

**Importante:**

* **Sempre que for necessário pode executar a depreciação acelerada durante o mês. Entretanto, este cálculo será irreversível. Após efetuá-lo não há como desfazer, exceto se houver um backup gerado antes de executar a rotina.**
* **MV\_ULTDEPR não será alterado.**

Rotina ATFA171:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043962333)**

Na SN4 irá gerar o registro no campo N4\_OCORR= 10 (depreciação acelerada)

Na SN3 os campos N3\_DTACELE e N3\_VLACEL1 serão preenchidos.

[Depreciacão acelerada proporcional (ATFA171 - SIGAATF)](https://tdn.totvs.com/pages/viewpage.action?pageId=312160301)

Depreciação Acelerada no relatório de Posição Valorizada na Data - ATFR072

<http://tdn.totvs.com/pages/releaseview.action?pageId=274637929>
