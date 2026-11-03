---
article_id: 9041888557975
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b5da8b0443c827cf8916c3c00e31f5488fcee9a5b2e53ee5887450c811ebae2f
fetched_at: '2026-06-28T22:37:24.206499+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT -  Informações adicionais
  na Consulta padrão do campo Contrato CND_CONTRA da Nova Medição
type: support-article
updated_at: '2024-02-21T18:17:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9041888557975-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Informa%C3%A7%C3%B5es-adicionais-na-Consulta-padr%C3%A3o-do-campo-Contrato-CND-CONTRA-da-Nova-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19573198063895) Tempo aproximado para leitura: **00:06:00 min**

**Dúvida**Informações adicionais na Consulta padrão da Nova Medição - Campo "Contrato" ( CND\_CONTRA )

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos- Todas as versões

**Solução**

Para a consulta padrão existente (**CN9003**), a tela foi totalmente reformulada, permitindo ao usuário realizar a pesquisa por qualquer um dos campos, além de realizar filtros personalizados. Por conta dessa consulta padrão possibilitar diversas customizações através de pontos de entrada que modificam seu comportamento, não foram incluídos novos campos.

Para utilizar essa funcionalidade atualize a ultima [Expedição contínua do Módulo Gestão de Contratos](https://tdn.totvs.com/pages/releaseview.action?pageId=679961416) em ambiente de teste e  depois aplique o ultimo dicionário que consta no pacote para rodar UPDDISTR em ambiente de teste.

Abaixo uma comparação entre a tela antiga e a nova:

Antes:

![consulta padrão antiga](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-33-35.png?version=1&modificationDate=1658856816040&api=v2 "consulta padrão antiga")

Depois:

![consulta padrão nova](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-39-40.png?version=1&modificationDate=1658857180517&api=v2 "consulta padrão nova")

Além da atualização da consulta atual, disponibilizamos uma nova consulta padrão (**CN9005**) com dados adicionais que ajudam o usuário na identificação dos contratos. Os campos exibidos são: número do contrato, revisão, filial do contrato, espécie(venda ou compra) e código, loja e nome do fornecedor/cliente.

![novos campos da consulta padrão](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-9-57.png?version=1&modificationDate=1658855398200&api=v2 "novos campos da consulta padrão")

![novos campos da consulta padrão](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-10-33.png?version=1&modificationDate=1658855433900&api=v2 "novos campos da consulta padrão")

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19573179149207)

Para utilizar a nova consulta padrão no campo Contrato (**CND\_CONTRA**), basta acessar Base de Dados→ Dicionário→ Base de dados e pesquisar pela tabela CND:

![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-51-23.png?version=1&modificationDate=1658857883383&api=v2)

![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_15-2-24.png?version=1&modificationDate=1658858544763&api=v2)

Em seguida basta posicionar-se no campo **CND\_CONTRA** e clicar em editar, selecione a consulta padrão criada e clique em salvar:

![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_15-5-21.png?version=1&modificationDate=1658858722240&api=v2)

Após salvar a consulta padrão, basta atualizar a base de dados para salvar as alterações:  
![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_15-7-9.png?version=1&modificationDate=1658858830163&api=v2)

A nova consulta será disponibilizada na próxima expedição contínua do módulo Gestão de Contratos, porém é possível cadastrar a mesma manualmente, basta seguir os passos abaixo em seu configurador:

![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_16-47-19.png?version=1&modificationDate=1658864840177&api=v2)

![](https://tdn.totvs.com/download/attachments/700490585/image2022-7-26_14-54-37.png?version=1&modificationDate=1658858077517&api=v2)

***Obs:***

Para a modificação e adição de outros campos na consulta padrão existente a possibilidade é apenas através de customização (somente para consulta padrão **CN9003**), utilizando os pontos de entrada abaixo em conjunto, não sendo possível essa customização na nova consulta padrão **CN9005**, conforme infomraões abaixo do TDN [DT Informações adicionais na consulta padrão da Medição](https://tdn.totvs.com/pages/releaseview.action?pageId=700490585):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21518440770583)

[CN120ESY - Customização da query da consulta especifica do contrato à Medição](https://tdn.totvs.com/x/yutc)

[CN120CMP - Possibilita a adição de campos customizados](https://tdn.totvs.com/x/zutc)

***Saiba Mais:***

[DT Informações adicionais na consulta padrão da Medição](https://tdn.totvs.com/pages/releaseview.action?pageId=700490585)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
