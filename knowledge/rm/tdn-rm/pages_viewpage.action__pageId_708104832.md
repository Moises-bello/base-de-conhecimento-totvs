---
content_hash: 5751f7c931168dcee79d32975f601c6774328f228a6008d8b30fbd6be7bffde5
fetched_at: '2026-06-29T00:11:25.378331+00:00'
page_id: '708104832'
product: rm
source: tdn-rm
title: Assinatura Eletrônica de Contratos na Rematrícula – TOTVS Educacional + TAE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708104832
version: 124
---

📌 Novidades da Funcionalidade

Esta seção centraliza as **evoluções, melhorias e ajustes funcionais** da integração de assinatura eletrônica de contratos.

🔄 Flexibilidade no Reenvio de Contratos

**Impacto:** Assinatura de contratos via Educacional

A partir das versões indicadas, foi removida a restrição de reenvio de contratos cancelados no TOTVS Assinatura Eletrônica quando o fluxo é iniciado pelo TOTVS Educacional.

Sempre que um documento for **cancelado no TAE** e o status for sincronizado no Educacional, o sistema **permite um novo disparo de assinatura**, alinhando o comportamento ao fluxo já existente na **Rematrícula Online**.

**Patches disponíveis:**  
12.1.2602 · 12.1.2510.162 · 12.1.2506.235 · 12.1.2502.273

🔍 Melhoria na Rastreabilidade de Cancelamentos

**Impacto:** Conferência de documentos

Nas versões anteriores, documentos cancelados diretamente no portal do TAE podiam ser removidos ou retornar com status **“Não Localizado”** no RM.

Com a melhoria, ao executar a **conferência**, esses documentos passam a receber o status definitivo de **“CANCELADO”**, preservando o histórico e viabilizando um reenvio estruturado.

**Patches disponíveis:**  
12.1.2602 · 12.1.2510.162 · 12.1.2506.235 · 12.1.2502.273

🧭 Evolução no Fluxo de Assinatura da Rematrícula

**Impacto:** Portal do Aluno e assinatura contratual

A partir das versões mais recentes, o fluxo de assinatura foi aprimorado para garantir **maior controle e consistência** entre rematrícula e contrato:

* O **assinante que realiza a rematrícula no Portal do Aluno** recebe por e-mail **apenas o token**;
* Os **demais assinantes** (responsável financeiro e/ou fiador) continuam recebendo o **e-mail com link para o TAE**;
* A **rematrícula só é confirmada** após a inserção do token no Portal do Aluno;
* A **assinatura do contrato ocorre junto com a confirmação da rematrícula**

**✅ Benefício da melhoria**Esse comportamento evita que a assinatura ocorra diretamente no TAE sem a efetiva finalização da rematrícula, garantindo integridade, consistência e rastreabilidade em todo o processo.

**Patches disponíveis:**  
12.1.2510.142 · 12.1.2506.214 · 12.1.2502.256

🧭 Evolução na Obrigatoriedade do TAE e Inclusão de Fiador como assinante

**Impacto:** Parametrização por curso e Portal do Aluno (Ensino Superior)

* Foi disponibilizada a flexibilização da exigência de assinatura eletrônica (TAE), que agora pode ser configurada individualmente na **Parametrização por Curso**, não sendo mais obrigatoriamente global.
* Para o **Ensino Superior**, foi adicionada a possibilidade de incluir o **Fiador** automaticamente como co-assinante no envelope no momento do envio do contrato financeiro.

✅ **Benefício da melhoria** Isso permite uma adoção gradual da assinatura eletrônica por parte da instituição (reduzindo custos operacionais ao ativar apenas para cursos específicos) e automatiza a coleta de assinaturas de fiadores no mesmo envelope, garantindo maior segurança jurídica e agilidade no processo de rematrícula.

**Patches disponíveis:**  
12.1.2602.142 · 12.1.2510.224

### ℹ️ Objetivo:

Esta página apresenta as orientações para configurar a integração entre o **TOTVS Educacional** e o **TOTVS Assinatura Eletrônica (TAE)** para assinatura eletrônica de contratos no processo de **rematrícula**, tanto para **Ensino Básico** quanto para **Ensino Superior**.

O objetivo é garantir um processo de rematrícula mais ágil, seguro e com validade jurídica, eliminando a necessidade de assinaturas físicas e reduzindo etapas operacionais.

#4C9AFF#E6F2FF#0747A6solid✔ Quando utilizar esta configuração

* ✅ Rematrícula via Portal do Aluno
* ✅ Ensino Básico e Superior
* ✅ Uso do TOTVS Assinatura Eletrônica (TAE)

🔄 Detalhamento do fluxo da rematrícula

1. Aluno ou responsável acessa o **Portal do Aluno**
2. O **contrato é gerado automaticamente** pelo TOTVS Educacional
3. O contrato é **enviado ao TOTVS Assinatura Eletrônica (TAE)**
4. Aluno, responsável financeiro e/ou fiador realizam a **assinatura eletrônica**
5. Após a assinatura, a **rematrícula é confirmada automaticamente**
Regras de negócio importantes

* A assinatura eletrônica via **TOTVS Assinatura Eletrônica (TAE)** não pode ser utilizada simultaneamente com **Token ou Chave de Segurança**;
* Quando configurada como **obrigatória**, a rematrícula **somente será concluída após a assinatura do contrato**;
* Caso exista **fiador**, seus dados (**nome, CPF e e-mail**) devem estar corretamente cadastrados;
* A **data de assinatura** do contrato é registrada no TOTVS Educacional **apenas após a conclusão do processo no TAE**;
* Quando o **aluno for o próprio responsável financeiro**, os cadastros de **Aluno** e **Cliente/Fornecedor** devem estar **idênticos**, considerando **Nome, CPF e e-mail**, incluindo grafia, espaçamentos e acentuação, garantindo a correta identificação dos dados no envio ao TAE.
* A obrigatoriedade do uso do TAE agora pode ser flexibilizada por curso. Para isso, é necessário configurar o parâmetro global correspondente e ativar a exigência na **Parametrização por Curso**;
* No contexto do **Ensino Superior**, o fiador será incluído como **co-assinante** no envelope enviado ao TAE apenas se possuir, previamente, um vínculo associado ao contrato financeiro com o status "Aprovado" ou "Em avaliação";
* **Importante:** Para evitar custos com envios inválidos à nuvem, o Portal do Aluno fará uma validação prévia. Se a rematrícula exigir fiador e este estiver com status reprovado ou pendente no RM, o portal bloqueará o avanço **antes** de gerar o documento e chamar o modal do TAE.

### 🔧 Configurações necessárias no TOTVS Educacional

**📍 Local no sistema:** Configurações → Parâmetros  → RM Portal  → Matrícula

| Parâmetro | Descrição | Impacto |
| --- | --- | --- |
| Portal – Assinatura de contrato | Habilita o uso do TAE | 🟠 Opcional |
| Assinatura obrigatória na rematrícula | Exige assinatura para concluir o processo | 🟢 Obrigatório |
| \*Restringir obrigatoriedade apenas conforme configurado na 'Parametrização por curso' | Permite que a obrigatoriedade da assinatura via TAE não seja global, passando a respeitar a configuração individual de cada curso. | 🟠 Opcional |
| Fiador do contrato | Habilita o envio do fiador como um dos assinantes do documento no TAE. *(Nota: Parâmetro visível exclusivamente no contexto de Ensino Superior).* | 🟠 Opcional |

*Utilize assinatura eletrônica **ou** token/chave de segurança. As opções são excludentes.*

\*Restringir obrigatoriedade apenas conforme configurado na 'Parametrização por curso'

**Configuração na Parametrização por Curso** Local no sistema: *Currículo e Oferta → Parametrização por Curso → (Edição do curso) → Aba: Configuração de matrícula*

Quando o parâmetro global de restrição por curso estiver ativo, a obrigatoriedade deverá ser definida individualmente por matriz aplicada.

* Marque a flag **"Assinatura do contrato obrigatória com TOTVS Assinatura Eletrônica na rematrícula"** para exigir o TAE na última etapa do portal para os alunos daquele curso específico.
* Para detalhes sobre a replicação desta regra via processos em lote, consulte a [Documentação de Parametrização por Curso](https://tdn.totvs.com/pages/viewpage.action?pageId=425458887).

🖥 Exemplo de configuração dos parâmetros no sistema

### 📤 Envio do contrato ao TOTVS Assinatura Eletrônica

* O envio do contrato ocorre **automaticamente** durante a rematrícula, conforme parametrização;
* Também é possível realizar o envio manualmente pelo processo **Integração TOTVS Assinatura Eletrônica**, disponível na visão de contratos;
* O sistema considera todos os signatários configurados no contrato (aluno, responsável e fiador).

### 👤 Experiência do usuário no Portal do Aluno

#F4F5F7solid👤 O que o aluno ou responsável visualiza no portal📄 Visualização do contrato de rematrícula✉️ Recebimento de e-mail do TOTVS Assinatura Eletrônica✍️ Realização da assinatura eletrônica✅ Confirmação automática da rematrícula após assinatura

### 🔍 Atualização de status e rastreabilidade

* O status do contrato no **TOTVS Educacional** é mantido **consistente** com o status do documento no **TOTVS Assinatura Eletrônica (TAE)**;
* A **data de assinatura** do contrato é registrada **somente após a conclusão do processo por todos os assinantes**;
* Dependendo do fluxo adotado, a atualização do status pode exigir a **execução do processo de Conferência de Documentos**, responsável por sincronizar as informações entre o TAE e o TOTVS Educacional;
* Melhorias recentes evitam o envio duplicado de contratos em casos de reprocessamento.

📌 **Importante**  
Para validar e atualizar o status das assinaturas no TOTVS Educacional, é necessário executar o processo **Conferência de Documentos**, conforme orientações disponíveis na documentação abaixo:  
👉

📌 Onde verificar status, data de assinatura e documento do contrato

#### **1️⃣ Verificar status e data de assinatura do contrato**

📍 **Local no sistema:** Financeiro Contábil → Contratos

Exemplo de contrato com status atualizado após a conclusão da assinatura no TOTVS Assinatura Eletrônica.

#### 2️⃣ Rastreabilidade do documento assinado

📍 **Local no sistema:** Financeiro Contábil → Contratos → Anexo/Integração TOTVS Assinatura Eletrônica

O documento terá o status de Finalizado, quando ele for enviado somente para um Assinante, caso seja enviado para mais de um o status estará pendente aguardando a Assinatura eletrônica dos demais. 

false🧾Quando um novo documento é enviado ao TOTVS Assinatura Eletrônica (TAE)

Um novo documento será gerado e enviado ao TAE nas seguintes situações:

• Documento cancelado no TAE e reenvio pela matrícula no Portal do Aluno;    
• Finalização da matrícula e do documento no TAE, seguida da repetição do processo de matrícula no portal;    
• Envio do documento para e-mail incorreto, com posterior correção e novo envio pela matrícula no portal.

**📌 Importante sobre a correção de e-mail**

A correção do e-mail deve ser realizada no cadastro correspondente ao perfil do assinante:

- 👩‍👦 Mãe, Pai ou Responsável Acadêmico → Cadastro da **Pessoa**  
- 🎓 Aluno → Cadastro do **Aluno**  
- 💼 Responsável Financeiro → Cadastro do **Cliente/Fornecedor**

### 🛠 Veja os problemas mais comuns e como resolver

⚠ Destinatários com e-mail duplicado

**Situação**  
Caso os assinantes selecionados possuam o **mesmo e-mail**, sendo **pessoas diferentes**, ao tentar enviar o contrato para assinatura no TOTVS Assinatura Eletrônica o sistema exibirá uma mensagem de erro informando que não é possível realizar o envio devido a **destinatários com e-mail repetido**.

**O que verificar**

* Validar se cada assinante (aluno, responsável financeiro e fiador) possui **e-mail único** em seu cadastro;
* Ajustar o e-mail duplicado antes de reenviar o contrato para assinatura.
* Caso o Aluno seja também o Responsável Financeiro, verificar se os dados do cadastro do **Cliente Fornecedor e do Aluno estão idênticos**, considerando **Nome, CPF e e-mail**, incluindo grafia, espaçamentos e acentuação
⚠ Divergência de nacionalidade no contrato

**Situação**  
Caso os dados de nacionalidade do assinante (seja ele o aluno ou o responsável financeiro) estejam divergentes entre os cadastros base do sistema, ao tentar realizar a assinatura do contrato no TOTVS Assinatura Eletrônica, o sistema exibirá uma mensagem de erro informando que não é possível prosseguir devido a uma **inconsistência na divergência dos dados de nacionalidade**.

**O que verificar**

* Validar se o campo **Nacionalidade** no cadastro de **Pessoa (Global)** está idêntico ao campo **Nacionalidade** no cadastro de **Cliente/Fornecedor (Financeiro)**;
* Acessar o menu **Cadastros | Pessoas**, localizar o assinante e verificar a nacionalidade na aba **Identificação**;
* Acessar o menu **Finanças | Gestão Financeira | Cadastros | Clientes e Fornecedores** e verificar a nacionalidade na aba **Identificação** (quadro Nacionalidade);
* Garantir que ambos os cadastros possuam a mesma opção selecionada (ambos como **Brasileira** ou ambos como **Estrangeira**) antes de tentar reenviar o contrato para assinatura.
⚠ Usuário não habilitado para assinatura no portal

**Situação**  
O usuário que estiver logando no Portal do Aluno precisa atender aos requisitos mínimos para realizar a assinatura do contrato. Caso contrário, será apresentada uma mensagem de erro impedindo a continuidade do processo.

**O que verificar**

* Se o **e-mail** está preenchido no cadastro do usuário;
* Se o usuário está marcado como **Assinante** no caminho: *Educacional > Parâmetros > RM Portal > Matrícula > Portal – Assinatura de Contrato*.
⚠ CPF ou E-mail não informados

**Situação**  
Para usuários de **nacionalidade brasileira**, o CPF é obrigatório para realização da assinatura eletrônica. Caso o CPF não esteja informado no cadastro, o sistema apresentará mensagem de erro. Além do CPF o usuário deve ter o **e-mail** preenchido. 

**O que verificar**

* Confirmar se os campos **CPF** e **e-mai**l estão devidamente preenchido no cadastro do usuário;
* Atualizar o cadastro antes de reenviar o contrato para assinatura.
⚠ Reenvio de e-mail de assinatura

**Situação**  
Após acionar a opção **Reenviar e-mail**, caso a tela seja fechada por qualquer motivo, o envio de um novo token não ocorre imediatamente.

**O que verificar**

* Aguardar o prazo mínimo de **5 minutos** para realizar um novo reenvio do e-mail de assinatura;
* Evitar múltiplos acionamentos em sequência.
⚠ Usuário responsável financeiro sem vínculo de acesso

**Situação**  
Quando o usuário logado é o **responsável financeiro**, independentemente de possuir outros papéis no sistema, recomenda-se que o campo **Usuário de acesso** esteja preenchido.

**O que verificar**

* Confirmar se o responsável financeiro possui o campo **Usuário de acesso** preenchido;
* Garantir que os dados de **e-mail e CPF** associados ao cadastro de Cliente/Fornecedor estejam corretos;
* Esse vínculo permite que o sistema identifique corretamente as informações utilizadas no envio ao TAE.
⚠ Bloqueio de Rematrícula por Inconsistência do Fiador (Ensino Superior)

**Situação**  
Ao tentar avançar para a etapa de contrato no Portal do Aluno, o sistema apresenta uma mensagem de erro e bloqueia a exibição do documento, não realizando o envio para o TAE.

**O que verificar**

* Confirmar se o parâmetro "Fiador do contrato" está ativo e se a Parametrização do Curso está exigindo fiador;
* Acessar o cadastro do contrato do aluno no RM e verificar se o **Status do Fiador** está como "Aprovado" ou "Em avaliação". Status diferentes (ex: Reprovado) bloqueiam a geração do contrato;
* Validar no cadastro da **Pessoa** (associada ao Fiador) se o campo **E-mail** está devidamente preenchido. Sem e-mail, a nuvem da TOTVS não consegue despachar o token de assinatura para o fiador.

 Veja Também

---

[Guia de Configuração da integração](https://tdn.totvs.com/pages/viewpage.action?pageId=1036767989)

[Guia de Envio e Gestão de Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=578823895)

[Guia Assinatura na Matricula - PS](https://tdn.totvs.com/display/LRM/02.06+Assinatura+do+contrato)

  Recursos Adicionais

---

[TOTVS Assinatura Eletrônica](https://tdn.totvs.com/pages/viewpage.action?pageId=605018639)

[Utilizando o TOTVS Assinatura Eletrônica - Vídeos](https://tdn.totvs.com/pages/viewpage.action?pageId=606837574)
