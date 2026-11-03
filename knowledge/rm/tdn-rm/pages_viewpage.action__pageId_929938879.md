---
content_hash: 8e4c8014b7e02e6090e545812cf28b2d6af8d4c027dfa92a325d3398c2961919
fetched_at: '2026-06-29T00:12:08.246158+00:00'
page_id: '929938879'
product: rm
source: tdn-rm
title: Apuração de Competência - Fechar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929938879
version: 3
---

## 🔐 **Fechamento da Apuração**

O processo de **fechar a apuração** segue regras específicas para garantir a integridade e o controle dos dados financeiros. Abaixo estão os critérios e comportamentos aplicados:

### ✅ **Condições para Fechamento**

* O fechamento **somente pode ser executado para competências em aberto ou parcialmente fechada**.
* **Todas as vendas da coligada e competência selecionadas devem estar apuradas**.  
  → Caso existam vendas pendentes, o fechamento será bloqueado.
* **Não é permitido fechar novamente uma competência que já está fechada**.

---

### 🔒 **Restrições Aplicadas após o Fechamento**

Ao fechar uma competência, o sistema aplicará restrições automáticas para **impedir alterações retroativas**. A partir desse momento, as seguintes ações **não serão mais permitidas naquela competência**:

* **Baixa de lançamentos financeiros**
* **Cancelamento de baixa**
* **Distrato de vendas**
* **Criação de aditivos contratuais**

Essas operações **somente serão permitidas na competência posterior mais recente que esteja aberta**, garantindo que qualquer movimentação financeira ou contratual ocorra apenas em períodos válidos.

---

### ℹ️ **Importante**

> O fechamento por coligada e competência promove um controle robusto das movimentações financeiras e contratuais, alinhando o processo com as melhores práticas de **governança, auditoria e compliance contábil**.
