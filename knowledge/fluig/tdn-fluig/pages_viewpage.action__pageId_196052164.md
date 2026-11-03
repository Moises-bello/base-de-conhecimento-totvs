---
content_hash: 4c75d8f60c7ec1a6b3d92a6bb7820b738545e45ab6d394554827d8bff6b91d11
fetched_at: '2026-06-28T21:35:19.152072+00:00'
page_id: '196052164'
product: fluig
source: tdn-fluig
title: Identity | Por que não consigo usar a autenticação automática nos aplicativos
  após alterar a senha no AD?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=196052164
version: 11
---

**Ocorrência**

Após modificar a senha do usuário no Active Directory, a autenticação automática para os aplicativos cadastrados no Identity deixou de funcionar. Se a nova senha for inserida manualmente, o login é feito com sucesso.

**Causa**

Foi feita análise no código fonte do Identity e concluiu-se que isto pode ter ocorrido após execução de alguns passos específicos. Acredita-se que após alteração da senha no Active Directory, o usuário passou a utilizar apenas a senha pessoal para acessar o Identity. Desta maneira, o Identity não recebeu a nova senha informada no AD para poder atualizá-la nos aplicativos.

Apenas para entendimento, devido a um padrão de segurança adotado pelo Identity, a senha do AD não é trafegada pela rede, ou seja, se for feita atualização da senha no AD e não for feita autenticação no Identity usando a senha nova do AD, a mesma não será salva em banco para realizar autenticação dos aplicativos.

**Solução**

Esta é uma regra de negócio do produto, o usuário precisa realizar o login com a nova senha do AD para que o Identity possa realizar a autenticação dos aplicativos.
