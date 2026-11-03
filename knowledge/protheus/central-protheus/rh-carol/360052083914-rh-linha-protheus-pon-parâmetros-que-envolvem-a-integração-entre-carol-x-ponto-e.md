---
article_id: 360052083914
category: RH - Carol
content_hash: f87119eb365a295844a16770111a3f13d8da9c47bb9bd2e7ca9575368370d28f
fetched_at: '2026-06-28T22:44:56.627171+00:00'
product: protheus
section_id: 19035556880407
source: central-protheus
title: RH - Linha Protheus - PON - Parâmetros que envolvem a integração entre Carol
  x Ponto Eletrônico
type: support-article
updated_at: '2025-11-11T17:39:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083914-RH-Linha-Protheus-PON-Par%C3%A2metros-que-envolvem-a-integra%C3%A7%C3%A3o-entre-Carol-x-Ponto-Eletr%C3%B4nico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33800778343703) Tempo aproximado para leitura: 01:00:00 min  
  
Dúvida**Quais parâmetros envolvem a integração entre a**Carol** e o **Ponto Eletrônico**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Os parâmetros que devem estar cadastrados no ambiente para que ocorra a **integração entre a plataforma Carol com o Ponto Eletrônico** são:

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Descrição do Parâmetro** | **Tipo** | **Exemplo de Utilização** |
| MV\_APICLO0 | Clock In da Carol - Utiliza integração com Carol Clock in? | Lógico | Exemplo: .T. |
| MV\_APICLO1 | Clock In da Carol - Endereço de Acesso ao EndPoint | Caractere | https://domínioCliente.carol.ai |
| MV\_APICLO2 | Clock In da Carol - Patch de Acesso ao EndPoint. | Caractere | api/v2/oauth2/token |
| MV\_APICLO3 | Clock In da Carol - ID de Conexão de Acesso. | Caractere | clockinmobile |
| MV\_APICLO4 | Clock In da Carol - Username de Acesso ao EndPoint. | Caractere | username@totvs.com.br |
| MV\_APICLO5 | Clock In da Carol - Password de Acesso ao EndPoint. | Caractere | senha1 |
| MV\_APICLO6 | Clock In da Carol - Domain Name de Acesso EndPoint. | Caractere | domínioCliente |
| MV\_APICLO7 | Clock In da Carol - Path do EndPoint DeviceList. | Caractere | api/v2/queries/named/deviceList |
| MV\_APICLO8 | Clock In da Carol - Path EndPoint clockinrecordsList. | Caractere | api/v2/queries/named/clockinrecordsList |
| MV\_APICLO9 | Clock In da Carol - Nome da Organização de acesso EndPoint | Caractere | ambiente |
| MV\_APICLOA | Clock In da Carol - Codigo do API Token (Connector Token) | Caractere | 00a00a0a000007e597b39b8a07qw5f60 |
| MV\_APICLOB | Clock In da Carol - Define se na integração com Carol Clock In será efetuada pesquisa por lacuna na numeração do NSR (.T.) ou se será efetuado pesquisa a partir do último NSR gravado (.F.) | Lógico | Exemplo: .T. |
| MV\_APICLOC | Define se será gerado o log de integração com a Carol. .T. = Gera o log; .F. = Não gera o log | Lógico | Exemplo: .T. |
| MV\_APICLOD | Define se a integração utilizará a tabela RR1 ou  MSA\_CONTROL\_MARCAC. .T. = RR1 .F. = MSA | Lógico | Exemplo: .T. |

**Importante:**A URL de acesso da Plataforma Carol, bem como o nome do ambiente, usuário, senha e token, são gerados/fornecidos pelo time de Suporte da Plataforma Carol/Clock In. **Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Clock In by Carol - Importação de marcações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061232453-RH-Clock-In-by-Carol-Importa%C3%A7%C3%A3o-de-marca%C3%A7%C3%B5es?source=search)  
[Integração Protheus x Carol Clock In](https://tdn.totvs.com/pages/releaseview.action?pageId=515294516)  
[RH - Linha Protheus - PON - Como cadastrar um relógio para integração do Clock In com o Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083354-RH-Linha-Protheus-PON-Como-cadastrar-um-rel%C3%B3gio-para-integra%C3%A7%C3%A3o-do-Clock-In-com-o-Ponto-Eletr%C3%B4nico?source=search)
