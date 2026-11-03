---
article_id: 360052015714
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 06d0245ff11e96188158d525b343d51d92671c3e9e79445aef16149e3d1d7815
fetched_at: '2026-06-28T22:38:31.167106+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Atenção - O controle de transações (MV_TT) está desligado.
type: support-article
updated_at: '2021-04-28T15:52:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052015714-MP-FAT-Aten%C3%A7%C3%A3o-O-controle-de-transa%C3%A7%C3%B5es-MV-TT-est%C3%A1-desligado
---

**Dúvida**

Como remover a mensagem abaixo que aparece ao logar no sistema:

**Atenção - O controle de transações (MV\_TT) está desligado.**

![](https://totvssuporte.zendesk.com/attachments/token/EebvkLnIY6DHDtzfEexflQncL/?name=inline1749171804.png)  
   
 **Ambiente**

Microsiga Protheus - todas as versões.

**Solução**

Habilite o parâmetro **mv\_tts** via configurador e a mensagem deixará de ocorrer.

Ob: É importante  que o parâmetro esteja habilitado, pois num erro de comunicação do sistema com o Banco de Dados em algum processo, o sistema dará o rollback e não afetará o Banco de dados.
