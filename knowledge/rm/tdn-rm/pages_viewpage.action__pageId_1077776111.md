---
content_hash: bc9eb40a52e19ee650d3ab0ab155515070fba542d01a1314df5c01a3e93f9c94
fetched_at: '2026-06-29T00:05:54.303010+00:00'
page_id: '1077776111'
product: rm
source: tdn-rm
title: 3 - Sincronização de Usuários e Corretores com o RD CRM (Versão 12.1.2606+)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077776111
version: 2
---

## **Sincronização de Usuários e Corretores com o RD CRM (Versão 12.1.2606+):**

---

Para que o "Dono do Lead" seja consistente entre os sistemas, é fundamental que os corretores do Portal de Imóveis estejam vinculados aos seus perfis no RD Station CRM.

**Vinculação Automática no Cadastro:** Com a integração do CRM ativa, ao criar/ativar ou inativar um novo usuário no Portal, o sistema verifica automaticamente se aquele e-mail já existe no RD. 

* **Com sucesso:** O vínculo é feito, a mensagem "Vinculado ao RDStation CRM" aparece e um ícone da RD fica visível ao lado do nome do corretor na listagem.
* **Não encontrado:** O usuário é criado no Portal, porém nenhuma mensagem de vínculo é exibida.

**Sincronização em Lote (Para bases existentes):** Se você já possui corretores cadastrados e acabou de ligar a integração, não precisa editar um por um.

1. Acesse a tela de **Integração > Aplicativos**.
2. Na linha da integração CRM, clique no botão de ações (**...**) e depois em **Vincular corretores**.
3. O sistema sincronizará de uma só vez todos os usuários ativos do Portal que possuam correspondência no RD CRM, garantindo o alinhamento da base.
