---
article_id: 360016655831
category: Materiais - Compras (SIGACOM)
content_hash: 72f76e5b7fd22d6d179911b065c05841391b5d624d3a989da63cf0b8d0558d3e
fetched_at: '2026-06-28T22:41:10.237914+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada Importador
  XML
type: support-article
updated_at: '2024-06-11T13:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016655831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-Importador-XML
---

**Dúvida**Quais são os pontos de entrada disponíveis para a funcionalidade do Importador Xml/ Totvs Colaboração ?

**Ambiente**Protheus – Compras – A partir da versão 11.80   
  
**Solução**Abaixo temos a descrição dos pontos de entrada disponíveis e o respectivo link de documentação do TDN.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Ponto de entrada** | **Descrição** | **Link** |
| COMXCOL | COLFILDUP | Informar empresa e filial quando for encontrada duplicidade durante a importação. | [TC02015 - COLFILDUP - Ponto que permite informar um empresa e filial quando for encontrada duplicidade na importação](https://tdn.totvs.com/pages/viewpage.action?pageId=369628567) |
| COMXCOL | COLDVIMP | Manipular a aba Impostos do Monitor para alterar divergências nos impostos de cada item | [TC02014 - COLDVIMP - Ponto que permite manipular a aba impostos do monitor Totvs Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=244429547) |
| COMXCOL | COLSTTS | Adicionar informações complementares depois da inclusão do documento nas tabelas Cab - Doc Entrada (SF1) / Itens - Doc Entrada (SD1). | [TC02013 - COLSTTS - Ponto que permite adicionar informações depois da inclusão do documento](https://tdn.totvs.com/pages/viewpage.action?pageId=233760407) |
| COMXCOL | COLF1D1 | Adicionar acrescentar campos customizados na SF1 e SD1 antes da geração do documento. | [TC02012 - COLF1D1 - Ponto que permite adicionar campos customizados na geração do documento](https://tdn.totvs.com/pages/viewpage.action?pageId=233760370) |
| COMXCOL | COMXPROC | Validação da geração de Documentos | [TC02011 - COMXPROC - Valida processamento de documentos do TOTVS Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=167313624) |
| COMXCOL | EVCOL | Alterar/Substituir a mensagem enviada por e-mail conforme eventviewer utilizado. | [TC02010 - EVCOL - Processamento de Mensagem Enviada por E-Mail (EventViewer - Totvs Colaboração)](https://tdn.totvs.com/pages/viewpage.action?pageId=307828136) |
| COMXCOL | COMXPARA | Ajustes dos Parâmetros MV\_COMCOL1 e MV\_CTECLAS, utilizado no momento da Geração do Documento. | [TC02009 - COMXPARA - Valida Parâmetros do TOTVS Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=285646728) |
| COMXCOL | COMXLEG | Manipular o array de legendas | [TC02008 - COMXLEG - Manipula o array com a descrição das legendas](https://tdn.totvs.com/pages/viewpage.action?pageId=658749525) |
| COMXCOL | COMXACOR | Manipular array com as cores no Browse | [TC02007 - COMXACOR - Manipula o array com as regras e cores do Browse](https://tdn.totvs.com/display/PROT/TC02007+-+COMXACOR+-+Manipula+o+array+com+as+regras+e+cores+do+Browse) |
| COMXCOL | COMCOLSD | Verificar os campos alterados na tabela SDT depois da gravação do vínculo de documento no Monitor | [TC02006 - COMCOLSD - verifica os campos alterados na tabela SDT - vínculo de documento TOTVS Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=165283404) |
| COMXCOL | COMCOLRT | Incluir rotinas adicionais no menu | [TC02005 - COMCOLRT - Inclusão de Rotinas Adicionais no Menu TOTVS Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=58097979) |
| COMXCOL | COMCOLPC | Efetuar validações no pedido de compras que está sendo amarrado à nota. | [TC02004 - COMCOLPC - Validação do Pedido de Compras antes de vincular à Nota Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=110429891) |
| COMXCOL | COMCOLF4 | Obter novo código da tes de entrada, caso não seja utilizado a TES do cadastro de produtos | [TC02002 - COMCOLF4 - Novo código da TES no cadastro de Produtos](https://tdn.totvs.com/pages/viewpage.action?pageId=51250499) |
| COMXCOL | COMCOL2 | Processar somente documentos do tipo transferência entre filiais | [TC02001 - COMCOL2 - CUSTOMIZAÇÃO PARA PROCESSAR SOMENTE DOCUMENTOS DO TIPO TRANSFERÊNCIA ENTRE FILIAIS.](https://tdn.totvs.com/pages/viewpage.action?pageId=51250475) |
| COMXCOL | A140ICOND | Alterar / Validar condição de pagamento | [TC02016 - A140ICOND - Ponto que permite alterar e validar a condição de pagamento no monitor do Totvs Colaboração.](https://tdn.totvs.com/pages/viewpage.action?pageId=505755731) |
| MATA140I | A140IVPED | Vincular Pedidos de Compras ao importar um documento | [TC02035 - A140IVPED - Ponto para vincular pedidos de compras ao importar um documento.](https://tdn.totvs.com/pages/viewpage.action?pageId=234616659) |
| MATA140I | A140IFOR | Informar cliente/fornecedor caso haja duplicidade | [TC02034 - A140IFOR - Ponto paa informar Fornecedor/Cliente da NF-e](https://tdn.totvs.com/pages/viewpage.action?pageId=223927514) |
| MATA140I | M104ISER | Sugerir series diferentes baseados nos arrays para documentos ja importados | [TC02031 - M140ISER - Séries alternativas para o arquivo XML importado](https://tdn.totvs.com/pages/viewpage.action?pageId=89622433) |
| MATA140I | A140IPRD | Identificação do produto | [TC02029 - A140IPRD - Customização da Identificação do Produto](https://tdn.totvs.com/pages/viewpage.action?pageId=6085834) |
| MATA140I | A140IPED | Adiciona campos na interface de vinculo com PC | [TC02028 - A140IPED - Campos para vínculo com pedido de compras](https://tdn.totvs.com/pages/viewpage.action?pageId=36309009) |
| MATA140I | A140IGRV | Manipular dados da SDS/SDT na importação de uma NFE | [TC02027 - A140IGRV - Ponto executado após a gravação dos registros importados da SDS e SDT.](https://tdn.totvs.com/pages/viewpage.action?pageId=6085827) |
| MATA140I | A140IIMP | Determinar filial em que nota deve ser importada | [TC02026 - A140IIMP - XML de Nota Fiscal de Entrada importado pelo TOTVS Colaboração](https://tdn.totvs.com/pages/viewpage.action?pageId=39682521) |
| MATA140I | A140IDOC | Manipular numero e serie da NF-e sendo importada | [TC02025 - A140IDOC - Utilizado para manipular o número e a série da NFe](https://tdn.totvs.com/pages/viewpage.action?pageId=198955980) |
| MATA140I | A140ICFOP | Identificar o tipo de nota por meio da CFOP | [http://tdn.totvs.com/display/public/PROT/TC02023+-+A140ICFOP+-+Identifica+o+tipo+da+nota+por+meio+do+CFOP](https://tdn.totvs.com/display/public/PROT/TC02023+-+A140ICFOP+-+Identifica+o+tipo+da+nota+por+meio+do+CFOP) |
| MATA140I | A140IQTD | Permite alterar quantidade/valor unitario/total do item | [TC02036 - A140IQTD - Ponto que permite alterar quantidade e valor unitário e total](https://tdn.totvs.com/pages/viewpage.action?pageId=525798609) |
| MATA116I | MT116XMLCT | Manipular dados da SDS/SDT na importação de um CTE | [TC02022 - MT116XMLCT Ponto utilizado na importação do XML da NF Eletrônica.](https://tdn.totvs.com/pages/viewpage.action?pageId=243012688) |
| MATA116I | A116TECT | Alterar TES e condição de pagamento na importação | [TC02021 - A116TECT - Altera TES e Condição de pagamento para CTe](https://tdn.totvs.com/pages/viewpage.action?pageId=51250511) |
| MATA116I | A116PRDF | Identificação do produto frete | [TC02020 - A116PRDF - Customização da Identificação do Produto Frete](https://tdn.totvs.com/pages/viewpage.action?pageId=47908250) |
| MATA116I | A116ITPCT | Determina se o CTE deve ser gerado como uma nota do tipo Normal | [http://tdn.totvs.com/display/public/PROT/TC02019+-+A116ITPCT+-+Determina+se+o+CTe+deve+gerar+nota+do+tipo+Normal](https://tdn.totvs.com/display/public/PROT/TC02019+-+A116ITPCT+-+Determina+se+o+CTe+deve+gerar+nota+do+tipo+Normal) |
| MATA116I | A116IFOR | Identifica cliente/fornecedor com duplicidade | [TC02018 - A116IFOR - Identifica fornecedor/cliente da mercadoria do CT-e](https://tdn.totvs.com/pages/viewpage.action?pageId=89622923) |
| MATA116I | A116IDOC | Manipula numero e serie do documento | [TC02017 - A116IDOC - Manipula número e série do CTe](https://tdn.totvs.com/pages/viewpage.action?pageId=189303764) |
| MATA116I | A116ICOMP | Manipular gravação dos itens do CTE | [http://tdn.totvs.com/display/public/PROT/TC02016+-+A116ICOMP+-+Ponto+de+Entrada](https://tdn.totvs.com/display/public/PROT/TC02016+-+A116ICOMP+-+Ponto+de+Entrada) |
| MATA116I | A116ICHV | Manipulação de chave do documento de origem | [TC02015 - A116ICHV - Manipulação de chave do documento de origem](https://tdn.totvs.com/pages/viewpage.action?pageId=184782339) |
| MATA116I | A116ICTEN | Determina se o CTE deve ser gerado como uma nota do tipo Norma, mesmo que possua vinculo com NF de origem | [TC02023 - A116ICTEN - Determina se o CTe deve gerar nota do tipo Normal mesmo que possui vinculo com NF de origem.](https://tdn.totvs.com/pages/viewpage.action?pageId=568923219) |

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[IX02 - Pontos de Entrada - Importador XML](https://tdn.totvs.com/display/PROT/IX02+-+Pontos+de+Entrada)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
