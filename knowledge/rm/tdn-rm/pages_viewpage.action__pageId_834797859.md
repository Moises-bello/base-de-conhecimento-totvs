---
content_hash: a1ea3fa7dff1a4af88401e369021ad853e5d87ea7c50ea8ff1b795b9823c67e9
fetched_at: '2026-06-29T00:11:49.495333+00:00'
page_id: '834797859'
product: rm
source: tdn-rm
title: Envio e Consulta Inutilização (CT-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834797859
version: 1
---

O processo de Inutilização permite ao usuário informar a SEFAZ alguns números de movimentos não serão utilizados para emissão de Conhecimento de Transporte para uma determinada série e filial. É possível inutilizar numerações de movimentos que ainda não tenham sido criados ou movimentos já criados mas que o CT-e ainda não tenham sido autorizados (CT-e’s com status de Inconsistente ou Rejeitados).

## **Envio**

Este processo pode ser executado acessando a visão do CT-e (Vendas > Faturamento > Conhecimento de Transporte Eletrônico) e em seguida Processos | Inutilizar CTE.   
Devem ser preenchidos os parâmetros de Filial, Série, Número Inicial, Número Final e Observação da inutilização. Vale ressaltar que os números de faixa inicial e final representam um range no qual o RM irá solicitar a inutilização perante a Sefaz.

Após o envio da solicitação de inutilização, as solicitações de inutilização não ficarão visíveis na grid de Conhecimentos de Transporte. Estas estarão presentes no anexo do Cadastro da Filial (Anexos > CT-e’s Inutilizados).

Como é possível solicitar a inutilização para CT-e's com status de Inconsistente ou Rejeitados, é necessário selecionar os registros destes documentos na grid de Conhecimentos de Transporte e realizar o processo. 

## **Consulta**

Após o envio, o registro ficará com o Status de Pendente, sendo ainda necessário realizar a consulta para obter o retorno da Sefaz. Para consultar a inutilização, na tela dos Conhecimentos de Transporte, clique no menu Processos >  Consultar Inutilização. Se o processo for bem sucedido o registro presente no anexos do cadastro filial terá o Status alterado para Inutilizada. Se por algum motivo a SEFAZ recusar a inutilização este registro ficará com o status Rejeitada.

Os movimentos relacionados a estas CT-e inutilizadas não serão cancelados automaticamente, sendo de responsabilidade do usuário realizar o cancelamento dos movimentos de forma manual.

As CT-e inutilizadas poderão ainda ser incluídas manualmente no anexo da filial. O processo manual não inutiliza a numeração! Ele serve somente para a inclusão de alguma numeração que por algum motivo não tenha sido inutilizada pelo RM, no início de uma implantação por exemplo.

**Nota:** Não será permitida a inutilização de numeração de CT-e de filiais cadastradas com emitente de pessoa física.
