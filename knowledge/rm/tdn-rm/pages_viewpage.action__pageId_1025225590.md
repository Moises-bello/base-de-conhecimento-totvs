---
content_hash: 651d373380e7cff323ba4a98ffdb8d5bd2b74327c79a185c0d89e70923a31ae2
fetched_at: '2026-06-29T00:05:48.555782+00:00'
page_id: '1025225590'
product: rm
source: tdn-rm
title: 1 - Parametrização TOTVS Gestão Financeira.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025225590
version: 16
---

Esta configuração permite habilitar no **TOTVS Gestão Financeira** as funcionalidades do **Recebe+ Boleto Híbrido**, incluindo:

* Geração do **QR Code Pix**
* Registro do **IPTE (linha digitável)** e **código de barras**
* **Baixa automática** dos lançamentos após o pagamento
* Execução dos **processos agendados** relacionados às transações

No menu do sistema, acesse:

**Ambiente → Parâmetros → TOTVS Gestão Financeira**

Na lista de parâmetros, selecione:

**Contas a Receber → Boleto Híbrido**

Na tela de configuração, acesse a guia **Credenciais** e informe os dados de acesso cadastrados no **Painel de Pagamentos**.

A parametrização pode ser realizada de duas formas:

* **Por Coligada**
* **Por Filial**

No exemplo apresentado, a configuração está sendo realizada **por Coligada**.

Preencha os seguintes campos:

**Tenant**  
Informe a **Tenant cadastrada no Painel de Pagamentos**.

**Usuário**  
Informe o **usuário cadastrado no Painel de Pagamentos**.

**Senha**  
Informe a **senha do usuário cadastrado no Painel de Pagamentos**.

Após preencher as informações, avance para a próxima guia.

Acesse a guia **Baixa** para configurar os meios de pagamento.

### Meio de Pagamento PIX

**Meio de Pagamento Boleto**

Nesta etapa, será configurado o comportamento do sistema quando houver **diferença entre o valor pago e o valor do lançamento**, seja:

* **Pagamento a maior**
* **Pagamento a menor**

Para realizar essa configuração, acesse o seguinte caminho:

**Ambiente → Parâmetros → TOTVS Gestão Financeira → Integração Bancária → Cobrança Eletrônica**

Nessa tela será possível definir as regras de tratamento para essas diferenças durante o processo de baixa.
