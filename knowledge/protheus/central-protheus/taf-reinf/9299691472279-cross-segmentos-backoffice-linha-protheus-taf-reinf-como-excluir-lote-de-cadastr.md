---
article_id: 9299691472279
category: TAF - REINF
content_hash: 1e523cccee0c0b32d30074083957284ffce822229e4c018aeb10d42e3a075072
fetched_at: '2026-06-28T22:41:33.415436+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Como excluir lote
  de cadastros e movimentos integrados pelo Extrator fiscal. '
type: support-article
updated_at: '2023-03-30T16:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9299691472279-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Como-excluir-lote-de-cadastros-e-movimentos-integrados-pelo-Extrator-fiscal
---

**Dúvida** Como excluir lote de cadastros e movimentos integrados pelo Extrator fiscal.  
  
**Ambiente**12.1.33  
  
**Solução**  Ao realizar a integração de movimentos e cadastros, através do extrator fiscal é possível excluir o lote de informações enviada através da rotina de gerenciador de integração.

   Acesse o gerenciador de integração,  selecione a integração que deseja excluir e clique na opção excluir,

![ger_nciador_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9299392362391/ger_nciador_1.png)

  Há duas possibilidades de exclusão.

1° Excluir registros e o ticket do gerenciador de integração, nesta opção ambas informações serão excluídas a bolinha selecionada e os dados serão excluídos da base de dados do TAF.

2° Excluir apenas os registros da base de dados, neste opção a bolinha(integração) selecionada continuara presente no gerenciador, mais as informações serão excluídas da base de dados do TAF.

![Ger_nciador_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9299416885143/Ger_nciador_2.png)

   Ao confirma e concluir a exclusão das informações será apresentada a quantidade de registros excluídos.

![Ger_nciador_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9299417031959/Ger_nciador_3.png)

Importante:  Todas informações podem ser excluídas diretamente no TAF e de forma individual, nesse formato só é recomendado quando é feito envio indevido de um lote grande, as informações excluídas não poderão ser recuperadas, recomendamos que o procedimento seja realizado por usuário ou consultor com conhecimento da rotina.
