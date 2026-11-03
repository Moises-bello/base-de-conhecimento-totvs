---
content_hash: 5415ea4b5feca8d054ff6075d99476ab2feb4f3e1bc9c551bc5c1addc1b256e1
fetched_at: '2026-06-28T21:35:26.795414+00:00'
page_id: '416853877'
product: fluig
source: tdn-fluig
title: BPM 098 - Porque minha solicitação foi atribuída ao usuário System:Auto e não
  um usuário do fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=416853877
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Em alguns casos, no fluxo de seu processo ao passar por uma atividade em que o fluig irá realizar alguma atuação como uma atividade de serviço ou mecanismo de atribuição, caso não seja possível resolver, o System:Auto ficará vinculado como responsável da solicitação. Isso ocorre para que o fluxo do seu processo não pare.

# Solução

Ao se deparar com uma solicitação em que o System:Auto é o responsável e deveria ser um usuário, será necessário da interferência do Gestor do Processo nessa solicitação para movimenta-lá para a próxima atividade, isso porque a atividade ficou presa com o System:Auto. Caso essa situação acontece com bastante frequência, o ideal é a análise do processo, sendo mais especifico, na atividade em que está ocorrendo isso.

Para obter mais informações sobre o que é o gestor e como atribui-lo a um processo, [acesse aqui](http://tdn.totvs.com/x/mga5Dw) a documentação.
