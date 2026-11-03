---
content_hash: 7851777974c4f4544ebf20bb1971871ae095cfd193555d5f426d5b6501b9e9c2
fetched_at: '2026-06-29T00:08:16.312606+00:00'
page_id: '244936697'
product: rm
source: tdn-rm
title: TVIKT4_DT_DataServer_FopFichaFinancData
type: documentation
url: https://tdn.totvs.com/display/LRM/TVIKT4_DT_DataServer_FopFichaFinancData
version: 110
---

# WEBSERVICE FOPFICHAFINANCDATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *WebService do DataServer FopFichaFinancData* |
| **Situação/Requisito:** | Quando o parâmetro "Visualização de eventos com valores zerados no envelope" está desmarcado e tentamos alterar um evento que está zerado via DataServer FopEnvelopeData, sistema retorna a mensagem:     Não foi possível adicionar um ou mais eventos ao envelope de pagamento pois existem itens cadastrados com os mesmos códigos nesse envelope.     Possível causa: O sistema está parametrizado para não apresentar eventos com valores zerados e o item adicionado já está cadastrado com o valor 0,00. Verifique a parametrização do sistema:     'Visualização de eventos com valores zerados no envelope' em Opções > Parâmetros > RM Labore > Outros Parâmetros > Parâmetros III |
| **Solução/Implementação:** | *Folha de Pagamento: Foi ajustado o webservice para que seja possível utilizar o DoReadRecord informando os parâmetros necessários via OwnerData.*  *Exemplo:* <tot:DataServerName>FopFichaFinancData/2011;9;1;00001;mestre</tot:DataServerName>  *Conector:* Alteração para que o ownerdata recebido seja tratado no SaveRecord do WSDataServer e o ReadRecord interno realizado para verificar se o registro existe ou sofreu alterações também utilize as informações do ownerdata. |
| **Chamados relacionados:** | *TVIKT4* |

divs
