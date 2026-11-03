---
content_hash: 3a7d8e9d527a40f01f7720995e36f4ad7bd308b183f2f1aa0b89d2c0b3853259
fetched_at: '2026-06-29T00:10:42.110651+00:00'
page_id: '546695939'
product: rm
source: tdn-rm
title: Ao ativar o Middleware ocorre erro sobre cadastro de municípios na coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546695939
version: 3
---

# Objetivo:

---

       O objetivo deste documento é orientar como proceder caso seja apresentado o erro: "Ocorreu erro que impediu a execução do processo. O município informado no cadastro da coligada não foi localizado no Cadastro de Municípios"

0Solução

O sistema verifica no cadastro da coligada, qual é o município informado, para poder buscar no cadastro de municípios o código a ser levado no processo de ativação do middleware.

Caso o campo esteja em branco, ou tenha informado algum nome abreviado ou incorreto, que não coincida exatamente com os existentes em eSocial I Endereços I Municípios, será apresentado o erro "Ocorreu erro que impediu a execução do processo. O município informado no cadastro da coligada não foi localizado no Cadastro de Municípios".

Nesse caso deve acessar o cadastro da Coligada em Administração de Pessoal I Cadastro Globais I Coligadas, e na aba "Endereço" digitar corretamente o nome da Cidade conforme está no cadastro de municípios:

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.26 |
| 12.1.27 |

falsefalse

**Status: Concluido**

false

**Data: 24/03/2020**

false

**Autor:**
