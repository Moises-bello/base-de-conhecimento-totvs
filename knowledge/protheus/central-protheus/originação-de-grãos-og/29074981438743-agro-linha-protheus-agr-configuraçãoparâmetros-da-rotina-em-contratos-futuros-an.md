---
article_id: 29074981438743
category: Originação de Grãos (OG)
content_hash: cf9aa6500ab954eaba9a154c0052a1daf344428362126274ddaac90623829688
fetched_at: '2026-06-28T22:45:37.757803+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: 'Agro - Linha Protheus - AGR - Configuração/Parâmetros da Rotina em Contratos
  Futuros: Análise de Exposição'
type: support-article
updated_at: '2025-06-25T19:07:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29074981438743-Agro-Linha-Protheus-AGR-Configura%C3%A7%C3%A3o-Par%C3%A2metros-da-Rotina-em-Contratos-Futuros-An%C3%A1lise-de-Exposi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29074981418519) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Para que serve uma **Configuração/Parâmetros da Rotina em Contratos Futuros: Análise de Exposição**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução****Principais parâmetros:**

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** | **Conteúdo exigido para esta rotina** |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Utiliza novo modelo de comercialização. | .F. | .T. |
| [MV\_AGRO041](https://tdn.totvs.com/x/zDNLHw) | Utiliza controle de gestão risco para fixação de preço? | .F. | .T. |
| [MV\_AGRO011](https://tdn.totvs.com/pages/viewpage.action?pageId=370616257) | Campos do cadastrado do Novo negócio | <vazio> | N7C\_DESCRI,N7C\_DMOECO,N7C\_UMCOM,N7C\_TIPORD,N7C\_VLRIDX,N7C\_QTAFIX,  N7C\_VLRCOM,N7C\_QTDFIX,N7C\_VLRFIX,N7C\_TXCOTA,N7C\_VLRUN1,  N7C\_VLRUN2,N7C\_VLTOTC,N7C\_HEDGE,N7C\_QTDCTR,N7C\_CODBCO,N7C\_OPEFIX |
| [MV\_AGRO00](https://tdn.totvs.com/x/BTIXFg)6 | Aprovação de Banking no registro de negócio | 1;2;3 | 1;2;3 |

**Pré-requisitos:**

* Parâmetros [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326), [MV\_AGRO041](https://tdn.totvs.com/x/zDNLHw) habilitados e [MV\_AGRO011](https://tdn.totvs.com/pages/viewpage.action?pageId=370616257), [MV\_AGRO00](https://tdn.totvs.com/x/BTIXFg)[6](https://tdn.totvs.com.br/pages/releaseview.action?pageId=370618885) preenchidos corretamente;
* Possuir os componentes de preço devidamente cadastrados. Ter um componente definido como bolsa e índice informado;
* Possui cadastro da bolsa de referência e definido o volume padrão do contrato futuro.
