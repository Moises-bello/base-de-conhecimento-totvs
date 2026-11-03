---
content_hash: 3488b807008d6da48b274f4b6a80cb710f977b037b2f3a8dfb502768213ff0b5
fetched_at: '2026-06-29T00:09:35.484418+00:00'
page_id: '425459365'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459365
version: 2
---

**TOTVS Obras e Projetos x BackOffice Protheus - Cadastro Cliente/Fornecedor**

---

A inclusão, alteração e exclusão do cadastro de clientes e fornecedores são realizadas no Protheus e sincronizadas automaticamente para o TOP, onde é permitido consultar os registros.  
    
 Para incluir, alterar ou excluir um cliente, acesse: Protheus | SigaCom (módulo padrão) | Atualizações | Cadastros | Clientes  
 Para incluir, alterar ou excluir um fornecedor, acesse: Protheus | SigaCom (módulo padrão)| Atualizações | Cadastros | Fornecedores   
 Para visualizar os clientes e/ou fornecedores no TOP, acesse: RM | BackOffice | Compras, Estoque e Faturamento | Cadastros | Clientes/Fornecedores   
     
 **Dados Sincronizados**  
    
 Os dados sincronizados do Protheus para o TOP referente ao cadastro Cliente/Fornecedor são:

* Código da coligada
* Data de nascimento
* Código do cliente/fornecedor
* CPF/CNPJ
* Nome
* Bairro
* Nome fantasia
* CEP
* Ativo
* Email
* Tipo (pessoa física ou jurídica)
* Telefone
* Status

***Observação***

Embora o cadastro de loja não seja sincronizado, com o objetivo de manter um índice único o código do cliente/fornecedor no TOP será a concatenação da Loja e do Código do cliente/fornecedor no Protheus. Por exemplo:

* + Protheus: **Loja 1** e **Cliente 100  -**TOP: **1;C100**
  + Protheus: **Loja 2** e **Cliente 100 -** TOP: **2;C100**
  + Protheus: **Loja 1** e **Fornecedor100 -** TOP: **1;F100**
