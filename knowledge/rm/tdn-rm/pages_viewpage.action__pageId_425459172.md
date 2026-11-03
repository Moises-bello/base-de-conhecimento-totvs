---
content_hash: c736d90669eca9f4a8bc4a8a675cd59f2d2ae43032ff74db5adcf591fb716bd8
fetched_at: '2026-06-29T00:09:34.501711+00:00'
page_id: '425459172'
product: rm
source: tdn-rm
title: 14.02 - Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459172
version: 9
---

**14.02.01 - Usuário da Biblioteca**  
    
O objetivo desta etapa é definir as características gerais do cadastro de usuários da biblioteca.  
   
**Sincronizar acesso às filiais/unidades do usuário do Corpore RM com o usuário da biblioteca:** Este parâmetro define que ao alterar os acessos de um usuário da biblioteca, os acessos do usuário RM vinculado, também serão alterados, mantendo uma sincronização entre o usuário RM e o usuário de biblioteca.  
   
**SDK Utilizado para o funcionamento da Biometria**: Este parâmetro define qual SDK será utilizado no sistema de  (Figerprint ou Verifinger).  
   
**Utilizar cobrança de taxas para cadastro de usuários:** Parâmetro disponível apenas quando o TOTVS Gestão Bibliotecária tem integração com o TOTVS Gestão Financeira. Permite definir taxas para o cadastro e a renovação de usuários na biblioteca. No caso do cadastro de um usuário, são contemplados, também, usuários cadastrados por meio de importação importados de outros sistemas. Quando um usuário é cadastrado, ou sua data de validade é renovada, seu status ficará "Cadastro Pendente**"**, até que o lançamento, referente à taxa, seja baixado.

A partir da versão 12.1.2302 caso TOTVS Gestão Bibliotecária esteja integrado ao TOTVS Educacional, será necessário realizar o cadastro de Serviços Taxas de Bibliotecária para gerar a Taxa de cadastro de usuário, Taxa de empréstimo ou Taxa de multa. Para saber mais [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=710556941).

**Parâmetro - Utilizar nome social no lugar do nome civil:** foi criado o parâmetro para utilizar o nome social no lugar do nome civil na tela de Movimentações. Através desta funcionalidade o sistema permite que o usuário utilize o nome civil ou nome social conforme a parametrização (Movimentação\Geral\Utilizar nome social no lugar do nome civil). Para que o sistema consiga pesquisar pelo nome social na Localização avançada é necessário utilizar o filtro Nome social.
