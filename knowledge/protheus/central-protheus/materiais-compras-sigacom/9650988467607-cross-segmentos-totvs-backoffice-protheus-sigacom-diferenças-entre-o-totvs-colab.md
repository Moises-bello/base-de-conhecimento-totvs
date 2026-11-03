---
article_id: 9650988467607
category: Materiais - Compras (SIGACOM)
content_hash: 08498495b2dfddd6d30e6d9ad3026b163824893b062bf1104113df5937ac5444
fetched_at: '2026-06-28T22:41:17.156822+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Diferenças entre o
  Totvs Colaboração (Neogrid), Importador XML e Importador XML x TOTVS Transmite
type: support-article
updated_at: '2022-10-19T13:55:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9650988467607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Diferen%C3%A7as-entre-o-Totvs-Colabora%C3%A7%C3%A3o-Neogrid-Importador-XML-e-Importador-XML-x-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Diferenças entre o Totvs Colaboração (Neogrid), Importador XML e Importador XML x TOTVS Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução:**

|  |  |  |
| --- | --- | --- |
| **Totvs Colaboração** | **Importador XML** | ****Importador XML x Totvs Transmite**** |
| Necessita Neogrid  E Neogrid é responsável por toda validação do XML. | NÃO necessita Neogrid  **Cliente é responsável por utilizar um XML valido e colocá-lo manualmente na pasta IN para que seja importado.** | Necessita Totvs Transmite  E Totvs Transmite é responsável por toda validação do XML. |
| Parâmetros de configuração:  MV\_NGINN  MV\_NGLIDOS  MV\_NGOUT  TDN: [Estrutura (Pastas/Parâmetros)](https://tdn.totvs.com/pages/viewpage.action?pageId=271662259) | Parâmetros de configuração:  MV\_NGINN  MV\_NGLIDOS  MV\_NGOUT  TDN: [Estrutura (Pastas/Parâmetros) - Importador XML](https://tdn.totvs.com/pages/viewpage.action?pageId=485869252) | Parâmetros de configuração:  MV\_NGINN  MV\_NGLIDOS  MV\_NGOUT  TDN: [Estrutura (Pastas/Parâmetros) - Importador XML](https://tdn.totvs.com/pages/viewpage.action?pageId=485869252) |
|  | MV\_IMPXML (Identificador para saber se é utilizado Importador XML ou Totvs Colaboração)  Necessidade de um campo novo na CKO (CKO\_ARQXML - Gravação do nome do XML que sera informado dentro da pasta IN)  Novo índice na CKO  TDN: [IX01 - Compatibilizadores](https://tdn.totvs.com/display/PROT/IX01+-+Compatibilizadores) | MV\_IMPXML (Identificador para saber se é utilizado Importador XML ou Totvs Colaboração)  Necessidade de um campo novo na CKO (CKO\_ARQXML - Gravação do nome do XML que sera informado dentro da pasta IN)  Novo índice na CKO  TDN: [IX01 - Compatibilizadores](https://tdn.totvs.com/display/PROT/IX01+-+Compatibilizadores) |
| Lista de Documentos a serem importados:   * 109 - Nota Fiscal de Entrada (NF-e) * 319 - Nota Fiscal de Serviço (NFS-e) * 214 - Conhecimento de Frete (CT-e) * 273 - Conhecimento de Transporte Eletrônico para Outros Serviços (CTEOS) | Lista de Documentos a serem importados:   * Nota Fiscal de Entrada * Conhecimento de Frete   **Obs: Não há importação de Notas Fiscais de Serviço devido cada prefeitura ter um layout específico.** | Lista de Documentos a serem importados:   * 109 - Nota Fiscal de Entrada (NF-e) * 319 - Nota Fiscal de Serviço (NFS-e) * 214 - Conhecimento de Frete (CT-e) * 273 - Conhecimento de Transporte Eletrônico para Outros Serviços (CTEOS) |
|  | Não há necessidade de alterar a nomenclatura dos arquivos XML de NFE e/ou CTE, a conversão é feita automática.  **Obs: Campo CKO\_ARQUIV ficara com a nomenclatura convertida e o campo novo CKO\_ARQXML estará com o nome do XML informado na pasta IN.** |  |
| * Tela do Monitor é a mesma para ambos * Tabela CKO deve ser alterada para CKOCOL em ambos * Não existe tratativa para utilizar o **Importador XML** e o **Totvs Colaboração** em conjunto. A definição de qual ferramenta utilizar é informada no parâmetro **MV\_IMPXML.** | | |

***Saiba Mais:***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [TOTVS Transmite](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195)
