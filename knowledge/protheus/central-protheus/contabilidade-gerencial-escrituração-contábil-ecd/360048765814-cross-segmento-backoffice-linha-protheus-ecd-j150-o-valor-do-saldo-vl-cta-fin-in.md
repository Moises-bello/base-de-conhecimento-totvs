---
article_id: 360048765814
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: f8a5c1e334d514ab2d0df27d82907f2e797f9479b2f592a890efa94d9c6df849
fetched_at: '2026-06-28T22:40:44.247774+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ECD J150 O valor do saldo (VL_CTA_FIN)
  informado na linha de detalhe da Demonstração de Resultado (J150.IND_COD_AGL="D")
  é diferente do resultado calculado com base nos registros de saldos periódicos (I155)
type: support-article
updated_at: '2024-04-23T18:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048765814-Cross-Segmento-Backoffice-Linha-Protheus-ECD-J150-O-valor-do-saldo-VL-CTA-FIN-informado-na-linha-de-detalhe-da-Demonstra%C3%A7%C3%A3o-de-Resultado-J150-IND-COD-AGL-D-%C3%A9-diferente-do-resultado-calculado-com-base-nos-registros-de-saldos-peri%C3%B3dicos-I155
---

**Dúvida**

O valor do saldo (VL\_CTA\_FIN) informado na linha de detalhe da Demonstração de Resultado (J150.IND\_COD\_AGL="D") é diferente do resultado calculado com base nos registros de saldos periódicos (I155) e de

saldos das contas de resultado (I355) na mesma data.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360073836633)  
**Ambiente**Microsiga Protheus – Contabilidade  – A partir da versão 11.80

**Requisitos**

* Caso tenha gerado a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* Apuração de resultado devera ser feita pelo sistema (inclusive a apuração da conta transitória para conta de patrimônio,caso possua) . [Exemplo - Apuração Trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search) e [Exemplo - Apuração Anual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* Veja se o  [Nivel\_AGL está correto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048123714-MP-SIGACTB-ECD-J150-Nivel-AGL-N%C3%A3o-deve-existir-mais-de-uma-linha-de-n%C3%ADvel-igual-a-1-na-DRE?source=search)
* Veja se o  [VL\_CTA e COD\_AGL estão corretamente cadastrados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
* Veja como esta a **[ORDENAÇÃO RELATÓRIO (DRE e BALANÇO) X ECD (J00 e J150)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023832631-MP-SIGACTB-CTBA161-ORDENA%C3%87%C3%83O-RELAT%C3%93RIO-DRE-e-BALAN%C3%87O-X-ECD-J00-e-J150-?source=search)**
* Veja se o procedure da ECD [MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search) esta configurado
* Obs : necessário aplicação deste pacote para que os fonte CTBXATU , CTBA190 e os demais fontes de atualização de saldo estejam atualizados
* Um vez que os pacotes foram aplicador e as procedures atualizadas Realize um reprocessamento de saldo, pois os registro são gerado com base na tabelas de saldo

**Solução**

O Validador esta realizando a comparação do [J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150-?source=search) , [I350 ,I355 , I150 e I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search)

Diante disso se faz necessário realiza a conciliação do registro para verificar qual deles não esta sendo gerado corretamente

* Ao informar formula na visão gerencial , o sistema considera formula la informada para apresentação dos saldo  , com isso sugerimos que não informe formula
* Identifique se a diferença de saldo apresentado por alguma conta especifica que está amarrada a visão , veja o que diferente essa conta das demais
* Ao conciliar os blocos necessário verificar qual não esta sendo gerado o saldo correto
* Situação ocorre somente para alguma conta especifica (ativo, passivo, receita ou despesa)?
* Em algum momento essa conta teve saldo?
* Esta sendo gerado com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)?
* Realize um teste sem gerar com centro de custo a situação é apresentada
* Verifique se o erro esta sendo gerado nos Lote de apuração
* Veja como sistema preenche os campos[\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)
* [Realize o reprocessamento de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search) (CTBA190) (Miscelânea > Refaz Saldos > Reprocessamento) com o objetivo de atualizar os saldos e corrigir o problema apresentado no validador.

Saiba mais ;

[ECD : Deve existir pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração Contábil) informado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-MP-SIGACTB-ECD-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado-?source=search)
