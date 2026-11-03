---
article_id: 360018713611
category: Escrita Fiscal - Impostos - ICMS
content_hash: d2c0175345ecbb252931c46a5e3a79fc26d1d2f25ce9c4e1c56a0434a019474b
fetched_at: '2026-06-28T22:39:24.217546+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Devolução de compra
  referente a uso e consumo não destaca valor do ICMS
type: support-article
updated_at: '2021-07-28T02:37:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018713611-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Devolu%C3%A7%C3%A3o-de-compra-referente-a-uso-e-consumo-n%C3%A3o-destaca-valor-do-ICMS
---

**Dúvida**Foi efetuada uma compra para material de uso e consumo ou ativo imobilizado onde não foi calculado o ICMS pelo fato da operação não dar direito ao crédito. Ao lançar a nota de devolução o ICMS precisa ser destacado, porém o sistema não está efetuando o cálculo.  
   
 **Ambiente**Protheus - Faturamento - Todas as versões  
  
**Solução**

Ao realizar o lançamento de uma nota de entrada referente a material de uso e consumo ou ativo imobilizado, o correto é que seja efetuado o cálculo do ICMS na operação para que nos casos de devolução dessas notas o valor do ICMS seja destacado corretamente.  
Dessa forma a Tes de entrada deverá ser configurada conforme orientado abaixo:

Calcula ICMS (F4\_ICM) = Sim  
L.Fisc.ICMS (F4\_LICMS) = Outros   
Calc.Dif.Icm (F4\_COMPLE) = Esse campo configurado = Sim define que será calculado o diferencial de alíquota na operação Interestadual.  
Sit. Trib. ICM (F4\_SITTRIB) = informar o CST.

\*Obs.: o campo Material de Consumo (F4\_CONSUMO) deverá ser utilizado nos casos em que possui redução na base de cálculo do ICMS.  
Para melhores detalhes referente ao conceito desse campo orientamos verificar a documentação abaixo:

http://tdn.totvs.com/pages/releaseview.action?pageId=6076755

Efetuando o lançamento da nota conforme orientado, o sistema irá apresentar o valor do ICMS na aba impostos do Documento de Entrada (MATA103), porém não irá gerar esse valor como crédito nos Livros Fiscais (MATR930) e nem na Apuração do ICMS (MATA953).

A Tes de devolução deverá ser configurada da mesma forma que a Tes de entrada, tendo em vista que a nota de devolução deverá ser um espelho da nota de origem.

Obs.: Caso a nota de entrada tenha sido escriturada de forma incorreta, orientamos que efetue a exclusão da nota para que possa ser lançada da forma correta.
