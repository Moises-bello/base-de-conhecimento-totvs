---
content_hash: a2b8c154f0cc9ff0667f078bf1799f7195982161f7c547938a9e8957ecf50c9a
fetched_at: '2026-06-29T00:08:12.830391+00:00'
page_id: '243650764'
product: rm
source: tdn-rm
title: TVBCZV_DT_ALTERAR_DATA_PAGAMENTO_SUGESTAO_FERIAS
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBCZV_DT_ALTERAR_DATA_PAGAMENTO_SUGESTAO_FERIAS
version: 114
---

# SUGESTÃO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Sugestão de Férias* |
| **Situação/Requisito:** | Ao tentar editar a data de pagamento de uma sugestão de férias via webservices, o dataserver FopFUFeriasPerData tenta inserir uma nova sugestão. |
| **Solução/Implementação:** | *O dataserver foi tratado para aceitar em suas requisições via webservice, um novo parâmetro chamado "NOVADATAPAGTO", permitindo assim que seja alterada a data de pagamento da sugestão.*    Ao realizar a chamada via webservice para o GetSchema, o serviço retornará o schema com um campo a mais, o NOVADATAPAGTO.  Quando chamar o DoSaveRecord, deve ser passado esse novo schema com esse campo, bem com o campo com o novo valor, por exemplo:    .....  </xs:schema>    <PFUFeriasPer>      <CODCOLIGADA>1</CODCOLIGADA>      <CHAPA>00001</CHAPA>  ...      <DATAPAGTO>1992-01-30T00:00:00</DATAPAGTO>      <NOVADATAPAGTO>1992-01-31T00:00:00</NOVADATAPAGTO>  ...    </PFUFeriasPer>  Onde DATAPAGTO deve possuir o valor da Data de Pagamento original que se deseja alterar, e NOVADATAPAGTO deve conter o novo valor. |
| **Chamados relacionados:** | *TVBCZV* |

divs
