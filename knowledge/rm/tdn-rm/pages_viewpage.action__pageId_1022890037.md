---
content_hash: bbb77727e1636252930e522231a1b3c48edb54636c0a93be370e378807a699ba
fetched_at: '2026-06-29T00:05:48.098990+00:00'
page_id: '1022890037'
product: rm
source: tdn-rm
title: Portal de Imóveis - Criação e Manutenção de Usuários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022890037
version: 5
---

### Contexto Geral

Atualmente, ao cadastrar um usuário no PI, é obrigatório que esse usuário também exista como *cliente / fornecedor* para que tenha acesso às comissões. Essa funcionalidade automatiza o processo de inclusão de *cliente/fornecedor* ao criar o usuário no Portal de Imóveis.

---

### Criação de Usuário

Ao criar um novo usuário, o sistema deve executar automaticamente as seguintes ações:

* Criar, de forma automática e vinculada, o respectivo cadastro de *cliente / fornecedor* no Backoffice.
* Criar o usuário de acesso associado a este cli/for, baseado no usuário padrão cadastrado em *Parâmetros / Portal de Imóveis:*

  + [Parâmetros: Usuário Padrão do Portal de Imóveis (Clique aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=801997247)

Para mais informações, veja também a documentação [Portal de Imóveis - Permissão Usuário CRUD Proposta (Clique aqui)](https://tdn.totvs.com/pages/viewpage.action?pageId=1001616047)

Lembrando que, mesmo com o cadastro automático de usuários, o usuário padrão deve ter um perfil básico que possibilite acesso as vendas, comissões e outros cadastros. Um modelo deste perfil pode ser visto na documentação acima.

---

### Atualização de Cliente ou Fornecedor

Quando um *usuário no PI* for editado, torna-se necessário garantir a consistência dos dados do usuário vinculado. Para isso:

* Alterações realizadas no cadastro de *usuário* no PI devem refletir nos dados do cli/for correspondente.
* O processo de atualização vai assegurar que usuário e cliente ou fornecedor permaneçam sempre sincronizados.

---

### Regras do Campo CPF

O campo **CPF** é tratado como chave de identificação no processo de criação do cliente ou fornecedor. Por esse motivo:

* O CPF ou CNPJ **não deve ser alterado** após a criação do *cliente/fornecedor*.
* A alteração deste campo mudaria a chave utilizada para identificar a existência do usuário na base, comprometendo as validações e buscas do sistema.
* Caso o CPF ou CNPJ seja alterado, será criado um novo *cliente/fornecedor* que irá refletir essa mudança

---

### Comportamento para Cliente ou Fornecedor Local

* Para criação de cliente ou fornecedor local, o sistema vai buscar a **coligada do usuário de origem**, conforme definida nos parâmetros do RM.

---

### Importante

O sistema gera um arquivo de log técnico no diretório `tmp`, nomeado `Erro_API_Criar_Usuario_Backoffice`, sempre que o cadastro automático de um usuário falhar. Este arquivo é essencial para o diagnóstico, detalhando erros como a existência de campos obrigatórios na tabela `FCFO` não mapeados no `PI`, falhas na inicialização de jobs, entre outros.
