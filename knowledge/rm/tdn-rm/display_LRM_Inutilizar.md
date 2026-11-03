---
content_hash: 75aae4e752c52415fc5cd5367b3558daf905497b85e4a326084512f4c2feb42f
fetched_at: '2026-06-29T00:09:19.525311+00:00'
page_id: '422545601'
product: rm
source: tdn-rm
title: Inutilizar
type: documentation
url: https://tdn.totvs.com/display/LRM/Inutilizar
version: 10
---

Através deste processo é possível fazer a inutilização de numeração de NF-e que não é emitida.

Este processo pode ser executado acessando-se a visão da NF-e e em seguida clicando-se no botão Processo | Inutilizar.

Neste caso, devem ser preenchidos os parâmetros de Filial, série, modelo (NF-e 55) número inicial, número final e observação da inutilização.

Após concluído o processo, se bem sucedido os registros das numerações das NF-e inutilizadas serão gravados no anexo NF-e Inutilizadas do Cadastro da Filial utilizada no processo.

O processo poderá ser executado para registros que estejam com os status de Inconsistente ou Rejeitados. Neste caso deverá ser feito um filtro para a localização dos registros desejados, os mesmos deverão ser selecionados e o processo disparado. Os registros serão transportados para o anexo do Cadastro da Filial. Os movimentos relacionados a estas NF-e inutilizadas não serão cancelados automaticamente. Esta operação deverá ser feita pelo usuário.

As NF-e inutilizadas poderão ainda ser incluídas manualmente no anexo da filial. O processo manual não inutiliza a numeração! Ele serve somente para a inclusão de alguma numeração que por algum motivo não tenha sido inutilizada pelo RM, no início de uma implantação por exemplo.

Não será permitida a inutilização de numeração de NF-e de filiais cadastradas com emitente de pessoa física.

---
