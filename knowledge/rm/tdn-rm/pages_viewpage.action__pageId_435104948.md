---
content_hash: df7528d1f98f1697349df1f7924d7d7d14602250c4babb3fb65f6fcb325c5e50
fetched_at: '2026-06-29T00:09:47.152324+00:00'
page_id: '435104948'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração de Locatário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104948
version: 13
---

## 📝 **Aditivo de Alteração do Locatário**

O Aditivo de Alteração do Locatário de um imóvel tem como objetivo permitir a troca da titularidade entre os locatários de um Contrato de Locação que já foi efetivado e que já possui lançamentos financeiros criados.  
Por meio do aditivo, é possível adicionar novos locatários ao contrato e também substituí-los, conforme a necessidade.

---

## ⚙️ **Pré-condições**

Antes de incluir o aditivo, é necessário atender aos seguintes requisitos:

🔐 Ter habilitada a permissão **[02.03.01.15 e 02.03.01.16] – Efetivar / Desfazer Aditivo de Alteração de Locatário**, no perfil do **TOTVS Gestão de Imóveis**, localizada em:  
**Serviços Globais > Segurança > Perfis**.

📄 Ter o Contrato de Locação efetivado.

👤 Ter incluído um Locatário no contrato.

🧾 Ter incluído um Motivo do Aditivo.

---

## ➕ **Incluindo um Aditivo de Locatário do Imóvel**

🔎 Selecione o **Contrato de Locação** e acesse o caminho:  
**Anexo > Aditivo > Locatário do Imóvel**.

➡️ Clique em Incluir Aditivo de Locatário do Imóvel.

## 📋 Preenchimento dos campos do Aditivo

🆔 **Código do Aditivo**  
• Campo de preenchimento automático.

📅 **Data do Aditivo**  
• Data do cadastro do aditivo.

🧩 **Tipo do Aditivo**  
• Preenchido automaticamente pelo sistema.

📌 **Situação do Aditivo**  
• Preparação.

📝 **Motivo do Aditivo**  
• Informar o motivo do aditivo.

🔢 **Número do Aditivo no Cliente**  
• Campo onde o cliente informa o número do aditivo no contrato físico, permitindo o agrupamento de vários aditivos do sistema em um único aditivo físico.

---

## 👥 **Adicionando Locatário no Aditivo**

➡️ Clique em **Adicionar Locatário no Aditivo**.

Será exibida a tela para preenchimento dos dados do locatário. Preencha os seguintes campos:

👤 **Locatário Principal Anterior**  
🆔 **Identificador do Locatário Anterior**  
📅 **Data Inicial e Final Anterior**

👤 **Novo Locatário Principal**  
👥 **Novo Locatário**

📆 **Nova Data Inicial e Final**  
• Preenchida automaticamente com o período de vigência do **Contrato de Locação**.

💾 Clique em **Salvar** para concluir o cadastro do aditivo.  
  
✔️

false

## 🚀**Flexibilização de Aditivo com Condomínio Apurado**

Foi implementada uma nova funcionalidade no processo de **Aditivo de Alteração de Locatário** que permite ao usuário ignorar o bloqueio de "condomínio já apurado".  
Agora, o sistema apresenta o parâmetro opcional **"Desconsiderar Condomínio"**. Quando ativado, ele permite que a troca de locatário (ou desfazer essa troca) ocorra mesmo que a competência atual já tenha tido seu fechamento de condomínio realizado antecipadamente.

## 🔹 Por que essa mudança foi feita?

Em muitos condomínios, a apuração é feita de forma antecipada (ex: fechar janeiro ainda em dezembro). Anteriormente, se houvesse uma troca de inquilino nesse meio tempo, o sistema impedia o aditivo porque o financeiro do condomínio já estava "travado".  
Essa melhoria garante que a operação imobiliária (aluguel/contrato) não pare por causa de rotinas contábeis do condomínio.

## 📌 Exemplo Prático (Passo a Passo)

Imagine a seguinte situação real:

🔹 **Cenário**Estamos em 20/Dezembro. A administração já rodou o fechamento do condomínio da competência Janeiro/2026. O boleto de condomínio de R$ 500,00 já foi gerado para o Locatário Antigo.

🔹 **O Problema**  
No dia 05/Janeiro, o locatário sai e um Locatário Novo assume o contrato.

🔹 **A Solução (Com a Melhoria)**

O gestor inicia o Aditivo de Alteração de Locatário para 05/Janeiro.  
O sistema identifica o condomínio já fechado, mas o gestor marca a opção **[X] Desconsiderar Condomínio**.

## **✅** Resultado

O aditivo é efetivado com sucesso.

🔹 **Financeiro**

* + O condomínio de R$ 500,00 permanece no nome do Locatário Antigo (pois já foi apurado).
  + O Aluguel e Fundo de Promoção de Janeiro começam a ser calculados para o Locatário Novo a partir do dia 05.
  + Se surgir um novo encargo de condomínio no fim de janeiro, o sistema permitirá gerá-lo para o Locatário Novo.

---

false🔄 **Regeração de Lançamentos após Aditivo**

📌 **A partir da versão 12.1.25**, ao efetivar o aditivo, os eventos avulsos e de locação complementar poderão ser regerados por meio da opção:  “Regerar lançamentos após data do aditivo”.

---

  
📅 **Cálculo Proporcional (Pró-rata Dia)**

Quando o contrato estiver configurado como **pró-rata dia**, na guia de **Reajuste**, e atroca de locatário ocorrer no meio de um período de competência, o sistema realizará o cálculo do aluguel de forma proporcional.

## ✅ **Validação da Efetivação do Aditivo**

✔️ Verifique se o **status do Aditivo** foi alterado para **Efetivado**.

✏️ Selecione o **Aditivo** e clique em **Editar Aditivo de Locatário**.

📂 Acesse a aba **Histórico**.  
Será exibida a informação do campo **Observação**, preenchido no momento da **efetivação do Aditivo**.
