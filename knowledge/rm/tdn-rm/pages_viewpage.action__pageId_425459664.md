---
content_hash: 9b33a081af6e0e30e8af11a79c676c9471a7c1f36a36c0ea2a12822bafa82a2a
fetched_at: '2026-06-29T00:09:37.992004+00:00'
page_id: '425459664'
product: rm
source: tdn-rm
title: Transferência de Exemplares Entre Filiais/Unidades
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459664
version: 4
---

Este processo ocorre entre as  de uma mesma coligada em que um exemplar vai ser transferido para outra unidade

Para realizá-lo é necessário que o usuário tenha acesso ao Menu e que o contexto do TOTVS Gestão Bibliotecária (Filial/Unidade) esteja selecionado.

Opções disponíveis no processo:

**Manter número de tombo:** indica que o exemplar será transferido mantendo o mesmo número do tombo.

**Em caso de conflito no número do tombo, gerar novo número de tombo**:

**Filial:** Filial para a qual o exemplar será transferido.

**Unidade:**Unidade para a qual o exemplar será transferido.

**Manter o tombo de Origem com Situação:**Indica qual situação será mantida no tombo de origem.

* Serão transferidos somente exemplares com status diferente de "Emprestado" e "Atrasado" e que não estejam baixados.
* Na unidade de origem, após a transferência, o exemplar estará baixado. A data é referente ao momento que o processo foi executado e a justificativa estará cadastrada com o seguinte texto: "Exemplar transferido para a filial/unidade <nome da filial>/<nome da unidade>.". E na unidade de destino será criado um novo exemplar, com os mesmos dados do exemplar de origem.
* Se o parâmetro "Utilizar número do tombo por tipo de publicação" que se encontra em Controle de Acervo | Exemplar estiver habilitado, o sistema irá permitir que seja criado números de tombos iguais porém para tipos de publicações diferentes após o término do processo de Transferência de exemplares entre filiais/unidades. Caso o parâmetro estiver desabilitado o sistema não irá permitir que o exemplar seja transferido como o mesmo tombo.
