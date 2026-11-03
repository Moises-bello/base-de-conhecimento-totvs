---
content_hash: d6429409ff97bdcb0ba824a3c1385047cfee7f0c01cae2ba10f92549a5978a78
fetched_at: '2026-06-28T21:35:22.813027+00:00'
page_id: '240301110'
product: fluig
source: tdn-fluig
title: BPM 061 - Como solucionar problema ao anexar documento à uma solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240301110
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

**Versão:** 1.5.9 ou inferior

# Ocorrência

Ao tentar movimentar uma solicitação, ocorre o erro "Erro ao salvar os anexos: Erro ao anexar documento à solicitação: JBAS011469: Transação é requerida para executar essa operação (tanto use a transação ou o contexto de persistência estendido).

A mensagem também pode aparecer em inglês: "Erro ao salvar os anexos: Erro ao anexar documento à solicitação: JBAS011469: *Transaction is required to perform this operation (either use a transaction or extended persistente context*).

**Figura 1 - Mensagem de erro ao salvar anexos durante a movimentação da atividade**

# Causa

Este erro geralmente ocorre devido alguns problemas que ocorreram na transação.

# Solução

Para contornar o problema é possível reiniciar os serviços do fluig e do banco de dados para que o sistema limpe a fila do JMS. Após este procedimento o erro não irá mais ocorrer ao movimentar a solicitação.

Para corrigir atualize o fluig para a versão 1.5.10 ou superior.

# Observações

Para saber mais sobre o procedimento de atualização acesse o .

Acompanhe as correções do produto e novas funcionalidades acessando o .
