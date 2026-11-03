---
content_hash: 9d3f9ec62fb00b6803afe29c2da1c3d306701613446b20c1196f101ef3d0f339
fetched_at: '2026-06-29T00:10:42.242606+00:00'
page_id: '547231277'
product: rm
source: tdn-rm
title: Segurança de Jobs Fracionáveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547231277
version: 13
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A tela de Segurança de Jobs Fracionáveis tem por função, realizar a segurança do Job que está sendo executado, de acordo com os parâmetros solicitados na tela.

**02. EXEMPLO DE UTILIZAÇÃO**

      Descrição dos campos que estão disponíveis na tela:

**Lookups:**

* **Perfil:** Selecionar o perfil que será utilizado.
  + **Obs.:** Estarão disponíveis para seleção somente os perfis do contexto atual.
* **Classe de Job:** Processo que está sendo utilizado (para o exemplo foi utilizado o processo "FopRotinasContabilizacaoProcess")

**NumericCupdown****:**

* **Min.Frações:** Mínimo de frações (partes) em que o processo pode ser dividido.
* **Max.Frações:** Máximo de frações (partes) em que o processo pode ser dividido.

**Check box****:**

* **Ativo:** Ativa o fracionamento do processo. 
  + Se o parâmetro estiver marcado o fracionamento é visualizado de acordo com a parametrização realizada pelo usuário na tela de Segurança de Jobs Fracionáveis.

* Caso esteja desabilitado (0) a caixa de escabilidade (Fracionamento) não é visualizado na execução do processo.

Caso o processo não possa ser fracionado o mesmo não é executado.

* **Agendável:** Se marcado o parâmetro, o processo é passível de agendamento, caso esteja desabilitado o processo não poderá ser agendado.
