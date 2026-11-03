---
content_hash: 647c48a57b9b7238ed81e2ba2d4119f42a631b4c2fc3c0b7a6a318fb2797e5ef
fetched_at: '2026-06-29T00:08:49.514959+00:00'
page_id: '330839014'
product: rm
source: tdn-rm
title: RMSProcess
type: documentation
url: https://tdn.totvs.com/display/LRM/RMSProcess
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Auxiliar na implementação/manutenção do Snowden.

# Execução:

---

        O novo recurso de Reportar erros para TOTVS pode ser exibido também em processos.

        No desenvolvimento de um novo processo, o server é herdado da classe RMSProcess. Ao sobrescrever o método DoExecute normalmente é inserido um bloco Try-Catch com o intuído de realizar algum tratamento ou apenas para alterar o status do processo para erro.

        No caso acima, o Log do processo é alterado na linha 127 adicionando informações do erro do processo.

        Após o tratamento do Log, duas ações poderiam ser tomadas para que o botão para reportar para Totvs seja exibido.

        Realizar o throw na exceção, fazendo com que a Lib alterasse o processo para erro e exibisse o Snowden baseado na exceção repassada.

        Repassar para o RMSProcess na propriedade Exception a exceção levantada

        Assim o botão Reportar para TOTVS e aba com a Solução caso ela exista será exibido para o usuário

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** RMSProcess

falsefalse

**Status:** Finalizado

false

**Data:** 15/01/2018

false

**Autores:**
