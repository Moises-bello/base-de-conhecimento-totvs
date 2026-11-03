---
content_hash: c7f329048ff2007657210d54f4e9cff6b16b3ded2844476982b71cd77ebee0ad
fetched_at: '2026-06-29T00:10:09.905966+00:00'
page_id: '452719728'
product: rm
source: tdn-rm
title: Desfazer transferência de candidatos entre perfis de vaga
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719728
version: 3
---

**Desfazer transferência de candidatos entre perfis de vaga**

Esse processo desfaz a transferência entre perfis de vaga caso o usuário tenha cometido algum engano.

Ao executar o processo o candidato será removido da etapa atual e será registrado um histórico deste procedimento no campo de observações do registro original do candidato que havia sido transferido.

O status do candidato na etapa deverá ser "Pendente análise" e o campo transferido será alterado para nulo.

**Importante**

-Em vagas com etapas sequenciais, o candidato recém transferido deverá estar na mesma etapa para a qual foi transferido e ainda com o status "pendente de análise". Se ele avançou para etapas seguintes devido à conclusão de etapas, não será possível desfazer a transferência.

-Em vagas com etapas paralelas, o candidato recém transferido possuirá status "pendente de análise" em todas as etapas para que seja possível desfazer a transferência.
