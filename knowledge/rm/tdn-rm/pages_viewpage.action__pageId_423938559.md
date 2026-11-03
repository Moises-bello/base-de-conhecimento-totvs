---
content_hash: 917c97fec5cf91f8ebaf9fa99d5e2a25f295c673b2b424eb36bf9867ac8dcdfa
fetched_at: '2026-06-29T00:09:27.887241+00:00'
page_id: '423938559'
product: rm
source: tdn-rm
title: Versão 11.0.0 (TOTVS Manutenção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938559
version: 4
---

**Inclusão de Vários itens no Plano de Manutenção** Nesta versão foi implementado um novo processo dentro do cadastro de Plano de Manutenção que permite ao usuário adicionar vários itens ao plano de manutenção de uma única vez. 11.0.0 – Botões "Novo" e "Excluir" na tela de Apropriação Direta de Produtos. Foi implementado os botões incluir e excluir na tela de apropriação direta de produtos, esses botões possibilitam que os usuários façam a inclusão de um novo objeto de manutenção ou exclua lançamentos indevidos de objetos de manutenção durante o processo.

**Botões "Item - Tab Opcional" e "Mov - Tab Opcional" na tela de Apropriação direta de Produtos.** Nessa versão foram adicionados na tela de Apropriação direta de Produtos dois botões para preenchimento dos campos opcionais do movimento. Os botões adicionados foram "Item - Tab Opcional" e "Mov - Tab Opcional". Ao clicar nesses botões o usuário poderá, ao gerar uma Apropriação direta de Produtos, inserir os dados referentes às Tabelas Opcionais do Financeiro (Mov e Item) que serão visualizados no movimento que será gerado para o TOTVS Gestão de Estoque, Compras, e Faturamento ao se fazer a apropriação.

**Exclusão de Movimentos Relacionados** Nesta versão foi implementada uma restrição que, se o usuário tentar excluir uma requisição de material que possua movimentos relacionados será exibido uma mensagem informando que o movimento não pode ser excluido e o processo será barrado.

**Inclusão de Vários itens no Plano de Manutenção** Nesta versão foi implementado um novo processo dentro do cadastro de Plano de Manutenção que permite ao usuário adicionar vários itens ao plano de manutenção de uma única vez.  
  **Novidades Futuras – Versão 11.20.0**

**Ordem de Serviço** Como novidade futura o Cadastro da Ordem de Serviço será migrado para a plataforma .NET. A nova interface de cadastro da Ordem de serviço será a mesma interface do movimento .NET do RM Nucleus, com isso o usuário do RM Officina terá a possibilidade de utilizar as mesmas funcionalidades e recursos já disponibilizados pelo TOTVS Gestão de Estoque, Compras, e Faturamento através do movimento .NET. Ao incluir ou editar uma Ordem de Serviço, será aberta a tela do movimento .NET e dentro dessa tela haverá uma aba de nome "Ordem de Serviço" onde conterá os dados da Ordem de Serviço aberta. Os Itens da Ordem não serão cadastrados de dentro da tela de ordem de serviço como era feita até a versão 10.80.0 do RM Officina. Na versão 11.20.0, para cadastrar um item, o usuário devera acessar a aba "Itens" que também se encontra na tela do movimento .NET.  
    
 **Cópia da Ordem de Serviço** Na versão 11.20.0 será implementado a funcionalidade de cópia de Ordem de Serviço. Com isso o usuário poderá fazer a cópia de uma Ordem de Serviço já existente inclusive copiando para a nova OS os itens contidos na OS de origem.

**Fórmulas de Consistência** Com a migração da ordem de serviço para a plataforma .NET, agora é possível utilizar formulas de consistência para consistir a geração do movimento. As fórmulas podem ser usadas tanto para a consistência da geração da ordem quanto para o item da ordem.

**Vincular e desvincular indicador de uso na Ordem de Serviço** Na versão 11.0.0 foi implementado a funcionalidade de vincular e desvincular um indicador de uso à Ordem de Serviço. Essa funcionalidade esta disponível na aba indicador de uso da edição da ordem de serviço e permite que o usuário selecione o indicador de uso que quer vincular ou desvincular a ordem de serviço.  

**Tela de acessórios da ordem de serviço foi migrada para a plataforma .NET** Nesta versão a tela de acessórios da Ordem de Serviço foi migrada para a plataform .NET  

**Alterar OS cancelada e Preço de tabela** Na versão 11.20.0 não será mais possível editar uma OS que se encontra com Status "Cancelado" e também aumentar ou diminuir o preço do item da ordem de serviço. Os parâmetros "Permite Alterar OS Cancelada" e "Preço de Tabela" foram retirados do sistema para os clientes que utilizarem o novo modelo de Backoffice.  

**Produto substituto/Similar** Na versão 11.20.0 os clientes que migrarem para o novo modelo terão acesso à funcionalidade de alterar o produto da OS por um produto substituto ou similar. Haverá um botão na interface de Ordem de Serviço onde o usuário fará a troca dos produtos no momento de incluir, editar ou faturar uma Ordem de Serviço.

**Acessórios da Ordem de Serviço** Na versão 11.20.0 a tela de acessórios da ordem de serviço acessada de dentro da visão e da edição da ordem será migrada para a plataforma. NET.

**Vincular e desvincular indicador de uso na Ordem de Serviço** Na versão 11.20.0 foi implementado a funcionalidade de vincular e desvincular um indicador de uso à Ordem de Serviço. Essa funcionalidade esta disponível na aba indicador de uso da edição da ordem de serviço e permite que o usuário selecione o indicador de uso que quer vincular ou desvincular a ordem de serviço.

**Cadastro de Problemas da Ordem de serviço migrado para plataforma .NET.** Na versão 11.0.0 o cadastro de Problemas da Ordem de Serviço foi migrado para a palaforma.NET.
