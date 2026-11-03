---
content_hash: 68a5b5a3ba68fbcb290ee0071c846bdc3a8e2757cecedcf107cebdba56e97247
fetched_at: '2026-06-29T00:09:17.429639+00:00'
page_id: '421388590'
product: rm
source: tdn-rm
title: Log de Alteração do Cliente/Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388590
version: 4
---

Através deste anexo é possível verificar informações sobre a atualização de alguns campos do cadastro do Cliente/Fornecedor.

Os campos são:

* Nome
* CPF
* CNPJ
* Inscrição Estadual
* Município
* Pais
* Rua
* Numero
* Complemento
* Bairro
* Suframa
* Estado

Ao alterar as informações de algum destes campos acima, será registrado no anexo "Log. de Alteração" o "Valor Anterior" e a "Data de Alteração".

Será armazenada somente a primeira alteração de cada dia, as demais serão desconsideradas. Os registros são usados para rotinas fiscais do módulo TOTVS Gestão Fiscal do BackOffice RM que precisam enviar o valor de campos fiscais quando alterados.

**Exemplo**

No dia 29/10/2008 o "Nome" do cliente "Cliente 1 SA" é alterado para "Cliente 1 LTDA".  
No Log. de Alteração é gravado: Identificação do Campo: Nome Valor Anterior: Cliente 1 SA Data da Alteração: 29/10/2008  
No mesmo dia o nome do mesmo cliente é alterado para "Cliente 2 LTDA", esta alteração não é gravada no Log. de Alteração.
