---
article_id: 10625309882135
category: Originação de Grãos (OG)
content_hash: d2ea041dc69cd2222875c68e32ea5bc108807d00ee6b8bfeb061b0183c6abfd9
fetched_at: '2026-06-28T22:45:44.759813+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Registro de Negócio - O conteúdo dos parâmetros
  pode ser alterado Parâmetros do módulo Configurador
type: support-article
updated_at: '2025-06-21T16:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10625309882135-Agro-Linha-Protheus-AGR-Registro-de-Neg%C3%B3cio-O-conte%C3%BAdo-dos-par%C3%A2metros-pode-ser-alterado-Par%C3%A2metros-do-m%C3%B3dulo-Configurador
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20624741305367)** Tempo aproximado para leitura**: 00:00:45 min****Ocorrência**  
No módulo **Comercialização (Linha Protheus) - Originação de Grãos (OG)**, ao tentar realizar rotina é apresentada a mensagem de aviso **O conteúdo dos parâmetros pode ser alterado Parâmetros do módulo Configurador**.  
**Ambiente**OTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois o conteúdo dos parâmetros podem serem alterados na rotina **Parâmetros** do módulo **Configurador.**  
  
**Solução**Os parâmetros utilizados no módulo de Gestão Agroindústria do Microsiga Protheus:

|  |  |  |
| --- | --- | --- |
| **Parâmetro** | **Descrição** | **Conteúdo padrão** |
| [MV\_AGRO002](https://tdn.totvs.com/pages/viewpage.action?pageId=370616326) | Parâmetro utilizado para informar o uso do novo modelo de comercialização. | .T. |
| [MV\_AGRO011](https://tdn.totvs.com/pages/viewpage.action?pageId=370616257) | Define os campos dos componentes da negociação. | N7C\_DESCRI,N7C\_DMOECO,N7C\_UMCOM,N7C\_TIPORD,N7C\_VLRIDX,  N7C\_QTAFIX,N7C\_VLRCOM,N7C\_QTDFIX,N7C\_VLRFIX,N7C\_TXCOTA,N7C\_VLRUN1,  N7C\_VLRUN2,N7C\_VLTOTC,N7C\_HEDGE,N7C\_QTDCTR,N7C\_CODBCO,N7C\_OPEFIX |
| [MV\_AGRO007](https://tdn.totvs.com/pages/viewpage.action?pageId=315228636) | Define se irá utilizar a tela simplificada fixação /cancelamento. | .T. |
| [MV\_AGRO003](https://tdn.totvs.com/pages/viewpage.action?pageId=370618087) | Indica quais processos irá  utilizar a aprovação de negócios :   1=Novo negócio requer aprovação; 2=Fixação requer aprovação; 3=Cancelamento requer aprovação. | 1;2;3 |
| [MV\_AGRO006](https://tdn.totvs.com/pages/viewpage.action?pageId=370618885) | Indica quais processos irá  utilizar a aprovação de banking : - 1=Novo negócio requer aprovação; 2=Fixação requer aprovação; 3=Cancelamento requer aprovação. | 1;2;3 |
| [MV\_AGRO015](https://tdn.totvs.com/pages/viewpage.action?pageId=370619272) | Define que o Corretor é o destinatário padrão do e-mail de aceite. | .T. |
| [MV\_AGRWFFD](https://tdn.totvs.com/pages/viewpage.action?pageId=370619940) | Pasta definida no qual o sistema irá gerar os fomulários workflow de reposta. | negociação |
