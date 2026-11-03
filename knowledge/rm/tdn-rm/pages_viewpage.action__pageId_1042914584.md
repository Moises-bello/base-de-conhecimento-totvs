---
content_hash: bb2c9341d3fc246ba3c96c6f720dc3191beab6425b4f73601179721c1e028a67
fetched_at: '2026-06-29T00:05:49.888207+00:00'
page_id: '1042914584'
product: rm
source: tdn-rm
title: Pré-Venda - WhatsApp
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1042914584
version: 11
---

Importante!

**Somente a partir da versão 12.1.2602**

# 📘 Guia de Uso – Integração de Notificações via WhatsApp

## 📌 Visão Geral

A integração via WhatsApp permite que corretores recebam notificações automáticas sempre que ocorrerem eventos importantes no sistema, como a atribuição de Leads ou a ativação de reservas.

O envio das mensagens é realizado por meio da integração com o **Worknow Chat**, utilizando modelos de mensagens (templates) que são preenchidos automaticamente com os dados do cliente, do corretor e do empreendimento.  
**Como Habilitar:** **[TCGI - WhatsApp - Como Habilitar WorkNow](https://tdn.totvs.com/pages/viewpage.action?pageId=1058177208)**

Essa funcionalidade garante mais agilidade no atendimento e reduz o risco de perda de oportunidades comerciais.

✅ Pré-requisitos para Funcionamento

Para que as notificações sejam enviadas corretamente, é necessário:

* Ter a **integração com o Worknow Chat ativa e configurada**.
* O **corretor possuir um número de celular cadastrado no sistema**.
* Existir um **template de mensagem configurado** para cada tipo de notificação.

  Importante!

  As configurações para notificação estão em: Ambiente >> Parâmetros >> Gestão de Imóveis >> 22.16 Portal de Imóveis >> Notificações whatsapp  
    
  Você deverá informar os templates utilizados para cada etapa: As etapas *Atribuição de Lead* e *Roleta de Leads* utilizam o mesmo template:  
  **[Como montar e aprovar mensagens](https://tdn.totvs.com/pages/viewpage.action?pageId=1042914608#:~:text=Como%20s%C3%A3o%20as%20mensagens%3F)**

Sem essas condições, o envio da mensagem não será realizado.

---

## 🔔 Quando as Notificações São Enviadas

Atualmente, o sistema envia notificações automáticas em três situações principais:

### 🟢 Lead Atribuído

Ocorre quando um Lead passa a ser responsabilidade de um corretor.

Essa atribuição pode acontecer de duas formas:

* **Manual:** realizada diretamente por um gestor ou usuário do sistema.
* **Automática via RD Station:** quando o Lead entra no sistema por integração e já é direcionado a um corretor.  
  (Caso o Lead já exista no PI - somente será atribuido o corretor para o mesmo se já tiver roleta configurada ou se já vier o corretor/usuário informado do RD e que exista no PI. Sendo que este ainda deve esta na situação "Banco Prospects")

👉 Objetivo da notificação: garantir que o corretor entre em contato com o cliente o mais rápido possível.

---

### 🎯 Roleta de Leads

A roleta é um processo automático que distribui Leads entre os corretores disponíveis, seguindo critérios definidos pela empresa.

Quando um corretor recebe um Lead por esse processo, ele é imediatamente notificado via WhatsApp.

👉 Objetivo da notificação: dar rapidez à distribuição e evitar que Leads fiquem sem atendimento.

---

### 🏢 Reserva Ativa

A notificação é enviada quando um corretor realiza a **reserva de um imóvel** para um Lead ou comprador.

Essa mensagem funciona como uma confirmação e reforça as informações importantes da negociação.

👉 Objetivo da notificação: manter o corretor informado e apoiar o acompanhamento da venda.

---

## ✉️ Como Funcionam as Mensagens

As mensagens são baseadas em **templates pré-configurados**, que recebem automaticamente informações como:

* Nome do corretor
* Nome do Lead / comprador
* Empreendimento
* Unidade reservada (quando aplicável)
* Outras informações relevantes

Isso garante padronização na comunicação e evita erros manuais.

Além disso, o sistema pode incluir um **rodapé personalizado**, conforme configuração da empresa.

---

## ⚠️ Pontos de Atenção

Para evitar falhas no envio:

* Verifique se o celular do corretor está preenchido corretamente.
* Confirme que os templates estão ativos.
* Certifique-se de que a integração com o WhatsApp está funcionando.

Caso alguma informação essencial esteja ausente, a mensagem não será enviada.

---

## 🚀 Benefícios da Integração

* Atendimento mais rápido ao cliente
* Redução de perdas de Leads
* Comunicação automática e padronizada
* Mais produtividade para o time comercial
* Melhor acompanhamento das reservas
