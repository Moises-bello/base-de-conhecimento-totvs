---
content_hash: 3a294c42ef391471e41c8ba4f18bb3de1181514dfddde6b8ee4919a88fd175a4
fetched_at: '2026-06-29T00:12:08.201320+00:00'
page_id: '929925557'
product: rm
source: tdn-rm
title: Cadastro do eventos S-2500 - Leiaute 1.3 - NT 03/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929925557
version: 14
---

Evento S-2500 - Leiaute 1.3NovidadesO que está diferente?

* **Criação dos campos {ideSeqTrab} no grupo {ideTrab}**

 

Importante

As seguintes validações serão realizadas pelo sistema, garantindo a conformidade com as regras do eSocial:

* + Se o campo **"ideSeqTrab"** for preenchido, não poderá existir outro evento S-2500 com os mesmos **"nrProcTrab"** e **"cpfTrab"** sem o campo **"ideSeqTrab"**.
  + Se o campo **"ideSeqTrab"** **não** for preenchido, não poderá existir outro evento S-2500 com os mesmos **"nrProcTrab"** e **"cpfTrab"**.
  + O valor **`0`** para **"ideSeqTrab"** é reservado para uso interno e não deve ser utilizado.
  + O campo **"ideSeqTrab"** não pode ser informado se todos os contratos do evento tiverem **"indContr = [S]".**

A interface do sistema realizará a validação apenas entre os campos exibidos na tela.

A interface de pesquisa teve a adição do campo Sequencial para que este também seja um fator de pesquisa/filtragem

Na tela de inclusão, o campo **{ideSeqTrab}** estará visível e disponível para entrada de um possível número sequencial, permitindo ao usuário definir a necessidade de um identificador único para o conjunto de dados do processo trabalhista.

Após a persistência do registro, o campo **{ideSeqTrab}** será desabilitado, pois faz parte da **chave identificadora do evento**, garantindo a integridade dos dados e evitando alterações indevidas.
