---
article_id: 360029343531
category: Contabilidade Gerencial - Ponto de entrada, Customização,Funções, Execauto
content_hash: b4ac4eeecdef97d2e79b5a47d1b2c06063ee91c0daa9a701cbb6f80aa656e54e
fetched_at: '2026-06-28T22:41:00.715929+00:00'
product: protheus
section_id: 1500001548462
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGACTB :CTBA020 PONTO
  DE ENTRADA '
type: support-article
updated_at: '2022-06-03T23:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029343531-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGACTB-CTBA020-PONTO-DE-ENTRADA
---

**Dúvida**

Quais pontos de entrada disponíveis para a rotina de cadastro Plano de Contas CTBA020?   
  
**Ambiente**Microsiga Protheus – Contabilidade  – A partir da versão 11.80  
  
**Solução**

Os pontos de entrada serão substituídos pelos pontos nativos do MVC ([Ponto de Entrada Padrão do MVC](http://tdn.totvs.com/pages/viewpage.action?pageId=208345968)) sendo necessária a adequação pelos clientes na migração Abaixo o detalhamento :

|  |  |  |
| --- | --- | --- |
| **Ponto de Entrada** | **Descrição** | **ID Ponto de Entrada** |
| [AT020VCA](http://tdn.totvs.com/display/mp/AT020VCA+-+Valida+campos+de+memoria+--+109581) | Executado na ativação da tela de inclusão. | MODELPRE |
| [CT020BUT](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Adiciona opções no grupo "Outras Opções" nas telas de inclusão, alteração, exclusão e visualização. | BUTTONBAR |
| [CT020EXC](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado antes de deletar um registro. | MODELPRE |
| [CT020LOK](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Validação das linhas do Plano Referencial. | FORMLINEPRE |
| [CT020TOK](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Validação geral do Plano Referencial. | MODELPRE |
| [CT20ALTA](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado no inicio da tela de alteração. | FORMLINEPRE |
| [CT20ALTD](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado após a alteração, mas dentro da transação. | MODELCOMMITNTTS |
| [CT20EXCA](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado no começo da função de exclusão de um registro. | FORMLINEPRE |
| [CT20EXCD](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Depois de deletar um registro, porem dentro da transação. | MODELCOMMITNTTS |
| [CT20GRA](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado no inicio da rotina de inclusão. | FORMPRE |
| [CT20GRD](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado após inclusão do registro. | MODELCOMMITNTTS |
| [CTB020VG](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado na validação da inclusão ou alteração. | MODELPOS |
| [CTB020VLD](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado antes da apresentação da tela de inclusão, alteração e exclusão  de um registro. | MODELPRE |
| [CTBA20CT](http://tdn.totvs.com/pages/releaseview.action?pageId=274656763#) | Executado dentro da transação dos processo de inclusão, alteração e exclusão. | MODELCOMMITNTTS |

Para mais Detalhes Veja :

<http://tdn.totvs.com/pages/releaseview.action?pageId=274656763>

<http://tdn.totvs.com/display/public/PROT/Ponto+de+Entrada+-+Contabilidade+Gerencial>
