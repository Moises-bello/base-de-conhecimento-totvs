---
content_hash: ea3ddef30a0d962de87590b5b44768391cc0c8026c629f4492b0745634ecccc6
fetched_at: '2026-06-29T00:09:35.858877+00:00'
page_id: '425459397'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Parametrização de Cliente / Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459397
version: 2
---

**Backoffice RM x Protheus SigaMNT - Parametrização de Cliente / Fornecedor**

---

**Parametrização de Cliente e Fornecedor Protheus.**

Para funcionamento da integração Backoffice RM x Protheus SigaMNT é necessária a parametrização dos campos código e loja, nas tabelas de cliente e fornecedor , dentro do módulo sigaCFG do sistema Protheus.

**Tabela Clientes (SA1)**

1. Acessar o Protheus , Módulo SigaCFG.
2. Acessar : Base de dados / Dicionário / Bases de Dados.
3. Acessar : Empresas / Dicionario de dados.
4. Pesquisar por SA1 . Selecione a tabela e clique em editar.
5. Acesse : Clientes / Campos.
6. Pesquisar pelo campo loja do cliente (A1\_LOJA) e editá-lo.
7. Selecionar o campo A1\_LOJA e clique em editar.
8. Informar o valor "01" ao campo Inic.Padrão localizado na aba Opções e confirmar.
9. Pesquisar pelo campo código do cliente (A1\_COD) e editá-lo.
10. Informar o valor GETSXENUM("SA1", "A1\_COD") ao campo Inic.Padrão localizado na aba Opções e confirmar.

**Tabela Fornecedores(SA2)**

1. Acessar o Protheus , Módulo SigaCFG.
2. Acessar : Base de dados / Dicionário / Bases de Dados.
3. Acessar : Empresas / Dicionario de dados.
4. Pesquisar por SA2 . Selecione a tabela e clique em editar.
5. Acesse : Clientes / Campos.
6. Pesquisar pelo campo loja do fornecedorb(A2\_LOJA) e editá-lo.
7. Selecionar o campo A2\_LOJA e clique em editar.
8. Informar o valor "01" ao campo Inic.Padrão localizado na aba Opções e confirmar.
9. Pesquisar pelo campo código do fornecedor(A2\_COD) e editá-lo.
10. Informar o valor GETSXENUM("SA2", "A2\_COD") ao campo Inic.Padrão localizado na aba Opções e confirmar.
