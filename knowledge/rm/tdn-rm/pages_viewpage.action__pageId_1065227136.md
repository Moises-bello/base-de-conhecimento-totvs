---
content_hash: df56a27c338362c85ffcbedade6cb51a6f55e5770361fe99018b90bfaabf13c2
fetched_at: '2026-06-29T00:05:53.075294+00:00'
page_id: '1065227136'
product: rm
source: tdn-rm
title: Proposta/Contratos - Envio de Mensagens e E-mails
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1065227136
version: 4
---

# Documentação – Envio de Mensagens e E-mails

**Módulo:** Portal de Imóveis (PI) – TOTVS  
**Escopo:** Propostas e Contratos

---

## 1.  Objetivo

Permitir a comunicação entre usuários vinculados a uma proposta (corretor, gestor, cliente), com possibilidade de:

* Registro de mensagens no histórico da proposta
* Envio imediato de notificação por e-mail

---

## 2.  Tela de Envio de Mensagens

### Campos disponíveis:

* **Para:** destinatário da mensagem
* **Público:** define se a mensagem pode ser visualizada por outros usuários
* **Visível para grupos:** restringe visualização por grupo
* **Enviar E-mail:** habilita o envio de e-mail
* **Mensagem:** conteúdo digitado pelo usuário

### Ação:

* **Enviar:** grava a mensagem e executa o envio (quando marcado)

---

## 3.  Funcionamento

### 3.1 Registro da mensagem

Ao clicar em **Enviar**:

* A mensagem é salva em **Mensagens da proposta**
* Fica disponível para consulta posterior

---

### 3.2 Envio de e-mail (tempo real)

Quando a opção **“Enviar E-mail”** está marcada:

* O sistema realiza o envio **imediatamente após o clique**
* O disparo é feito diretamente via SMTP configurado
* Não há uso de fila, agendamento ou processamento posterior

---

## 4.  Estrutura do E-mail

### Conteúdo padrão:

* **Assunto:**

  ```
  Nova Mensagem - Proposta {ID} - De: {Usuário}
  ```
* **Corpo:**
  + Saudação ao destinatário
  + Identificação da proposta:
    - Número
    - Empreendimento
    - Unidade/Lote
    - Cliente
    - Valor
  + Texto da mensagem enviada

---

## 5.  Destinatários

O envio ocorre para:

* Usuário selecionado no campo **“Para”**
* Desde que possua **e-mail cadastrado**

---

## 6.  Dependências

Para funcionamento correto:

* Configuração válida de SMTP (ex: Gmail ou outro servidor)
* Usuários com e-mail preenchido
* Permissão de envio habilitada no sistema

---

## 7.  Regras de Negócio

* O envio de e-mail é **opcional** (checkbox)
* A mensagem é **sempre registrada**, independente do envio
* O e-mail reflete exatamente o conteúdo informado no momento do envio
* O histórico da proposta mantém todas as interações (públicas e privadas)

---

## 8.  Resumo do Fluxo

1. Usuário preenche mensagem
2. Seleciona destinatário
3. (Opcional) marca “Enviar E-mail”
4. Clica em **Enviar**
5. Sistema:
   * grava a mensagem
   * envia o e-mail imediatamente
