---
article_id: 360008353712
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: d918e777fc6a094e6653bf282ba18ce52df516e3049164b35ab3dbb204a59752
fetched_at: '2026-06-28T22:40:44.657419+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - 4-VL_LCTO - REGISTRO
  I200
type: support-article
updated_at: '2023-05-19T15:20:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008353712-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-4-VL-LCTO-REGISTRO-I200
---

**Ocorrência**

***VALIDAÇÃO ECD***

***Duvida:***

Soma das partidas do lançamento, a crédito, diferente do valor informado no registro Lançamento Contábil - REGISTRO I200

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008111412/mceclip1.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial – A partir da versão P12.1.25   
  
  
**Requisitos**

* **[Como atualizar o ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)**

* **Acesse aqui as ultimas expedições Pacote Acumulado Contábil:**

  [**Pacotes de Atualização - Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)
* **[Pacotes LIB](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)**
* **[Pacotes DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/search/searchAll)**
* **[Binário AppServer](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)**
* **[Binário SmartClient](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/)**
* **[DICIONARIOS\_DIF e DICIONARIOS\_COMPL](https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125DD/)**

**Solução**

Situação pode está sendo apresentada ,pois há  lançamentos contábeis partida simples em lotes diferentes e mês diferente.   
Desta forma, o validador verifica se a soma do crédito da conta, [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search) do lançamento é igual a soma do saldo a crédito da conta contábil.

* Os documentos contábeis não podem conter divergências entre débito e crédito, onde ambos devem possuir o mesmo saldo no fechamento do documento.
* Ao   localizar o lote e documento contendo esta diferença através das rotinas de lançamentos contábeis, efetue o ajuste manualmente.
* Caso esteja gerando ECD com centro de custo  é necessário primeiramente, que o Centro de Custo esteja apurado.Veja como realizar a [APURAÇÃO DA ENTIDADE CENTRO DE CUSTO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046635074-MP-SIGACTB-CTBA211-APURA%C3%87%C3%83O-DAS-ENTIDADES-CENTRO-DE-CUSTO-ITEM-CONTABIL-E-CLASSE-DE-VALOR?source=search)
* Caso esteja gerando  [ECD EMPRESA CONSOLIDADORA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045923434-MP-SIGACTB-ECD-EMPRESA-CONSOLIDADORA-COMO-GERAR-REGISTROS-I350-I355-I150-I155-?source=search)  , veja se esta gerando o registro I200,I250,[I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-MP-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155?source=search) , corretamente
* Realize a conciliação dos blocos para verificar se o sistema esta gerando valores a maior ou menor
* Identifique se a diferença de saldo apresentado por alguma conta especifica que está amarrada a visão , veja o que diferente essa conta das demais
* O Validador , realizar a comparação do saldos  I200 E I250   .  
    
  Diante disso necessário conciliar o blocos e verificar qual não esta sendo gerado o saldo correto   
    
  + Situação ocorre somente para alguma conta especifica (ativo, passivo, receita ou despesa)?
  + em algum momento essa conta teve saldo?
  + esta sendo gerado com centro de custo?
  + realize um teste sem gerar com centro de usto a situação é apresentada
  + Verifique se o erro esta sendo gerado nos Lote de apuração
  + Verifique na tabela CSA e CSB se o campo de numero de lote esta diference para o lote/lançamento de apuração de resultado
  + CSA\_NUMLOT e CSB\_NUMLOT Veja se as tabelas CSA e CSB o numero no lote de apuração esteja igual , caso esteja diferente o sistema não ira gerar
  + Verifique se o saldo gerados do I200 e I250 estão corretos ou se o sistema não gerou algum lançamento
  + veja de o sistema gerou no I250 todo o lote de apuração
* Veja se a apuração das contas  de receita e despesa estão corretas
* [Apuração Anual : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* [Apuração Trimestral : Apuração Sem conta PONTE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* veja se esse erro é apresentado [ECD - Erro na inclusão de dados nas tabelas CSA e (ou) CSB VIA PROCEDURE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027070511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Erro-na-inclus%C3%A3o-de-dados-nas-tabelas-CSA-e-ou-CSB-VIA-PROCEDURE?source=search)

Veja mais :

[I250 O REGISTRO LIDO TEM QUANTIDADE DE CAMPOS DIFERENTE DO ESPECIFICADO NO LAYOUT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047283673-MP-SIGACTB-ECD-I250-O-REGISTRO-LIDO-TEM-QUANTIDADE-DE-CAMPOS-DIFERENTE-DO-ESPECIFICADO-NO-LAYOUT?source=search)

[ECD ADVERTENCIA I200| FATO CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016244152-MP-SIGACTB-ECD-ADVERTENCIA-I200-FATO-CONTABIL?source=search)

[Registro I200: "Soma das partidas do lançamento, a crédito (ou débito), diferente do valor informado no registro Lançamento Contábil"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028621892-MP-SIGACTB-ECD-Registro-I200-Soma-das-partidas-do-lan%C3%A7amento-a-cr%C3%A9dito-ou-d%C3%A9bito-diferente-do-valor-informado-no-registro-Lan%C3%A7amento-Cont%C3%A1bil-?source=search)
