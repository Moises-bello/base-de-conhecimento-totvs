---
content_hash: 0777a4ee3615c3c4e66ba6ed16d1b69acfd0e13aa077c6484980723f66cc7d38
fetched_at: '2026-06-29T00:05:48.892783+00:00'
page_id: '1032880106'
product: rm
source: tdn-rm
title: Encerrar / Rescindir - Taxa de Administração na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1032880106
version: 3
---

## 📌VISÃO GERAL

Esta funcionalidade permite informar uma **Taxa de Administração diferenciada** no momento de realizar a rescisão de um contrato de locação.

Anteriormente, o sistema utilizava obrigatoriamente a mesma taxa mensal do contrato para os cálculos finais.  
Com esta atualização, a imobiliária passa a ter **maior flexibilidade**, permitindo a aplicação de **regras comerciais específicas** ou **negociações pontuais** no encerramento do contrato, sem a necessidade de cálculos manuais externos.

---

## 📅QUANDO UTILIZAR?

Utilize este recurso quando a **negociação de saída do imóvel** prever um percentual de administração sobre as **verbas rescisórias** diferente daquele praticado mensalmente no aluguel.

---

## 🧮EXEMPLO PRÁTICO

**Taxa Mensal (Contrato):**  
➡️ 10%

**Acordo na Rescisão:**  
➡️ A imobiliária cobrará **15%** sobre o valor da multa e dias proporcionais.

---

## ⚙️COMO CONFIGURAR (PASSO A PASSO)

1️⃣ Acesse o menu **Contratos** e localize o contrato desejado.

2️⃣ Clique na opção:  
      ➡️ **Anexos / Encerrar / Rescindir** para iniciar a rescisão.

3️⃣ Siga a documentação **[Contrato de Locação – Anexo – Encerrar / Rescindir](https://tdn.totvs.com/pages/viewpage.action?pageId=435105386)** para cadastrar uma nova rescisão.

4️⃣ Localize o campo:  
      ➡️ **Taxa de Adm. para Rescisão (%)**.

5️⃣ Preencha o campo com o novo percentual desejado.

**🚨Nota:**  
O campo aceita casas decimais (ex.: **12,5%**).

6️⃣ Prossiga com a geração do cálculo e **efetive a rescisão**.

7️⃣ Verifique nos lançamentos gerados  
      ➡️ (**Evento Financeiro de Rescisão**) que o valor da taxa administrativa foi calculado com base no **novo percentual informado**.

---

## 📋COMPORTAMENTO DO SISTEMA

**Regras de Aplicação**

---

Para garantir a **segurança dos dados** e a **agilidade no processo**, o sistema segue a seguinte lógica:

| Ação do Usuário | Comportamento do Sistema |
| --- | --- |
| **Preencher** o campo "Taxa de Adm. para Rescisão" | O sistema **ignorará** a taxa do contrato e usará **exclusivamente** este novo valor para os cálculos desta rescisão. |
| **Deixar em branco** o campo "Taxa de Adm. para Rescisão" | O sistema **manterá** a taxa padrão já definida no cadastro do contrato de locação. |
