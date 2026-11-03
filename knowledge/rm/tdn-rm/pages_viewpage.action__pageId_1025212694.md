---
content_hash: 49f0ee51634eaa58372bd0bf39f41bff0d74ac6804d83d78b9b7464b45434b9b
fetched_at: '2026-06-29T00:05:48.499851+00:00'
page_id: '1025212694'
product: rm
source: tdn-rm
title: Assinatura Contrato - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025212694
version: 13
---

**TOTVS Assinatura Eletrônica**

Esta seção descreve as configurações necessárias para habilitar a integração com o TOTVS Assinatura Eletrônica (TAE) especificamente durante a etapa de contrato no processo de Rematrícula Online (Novo Portal do Aluno).

Caminho da Parametrização

Acesse: **Ambiente > Parâmetros > Educacional > RM Portal > Matrícula > Portal - Assinatura contrato**.

Nesta etapa, define-se se a instituição utilizará a assinatura eletrônica integrada ao TAE ou o modelo tradicional de aceite.

Detalhamento dos Campos

### ✅ Utilizar assinatura com TOTVS Assinatura Eletrônica

Esta é a flag principal que ativa a integração. O comportamento do sistema ao marcar esta opção é:

* **Ciência no Portal:** O contrato será exibido durante a rematrícula com um campo para que o aluno ou responsável sinalize apenas a **ciência** do documento.
* **Assinatura Efetiva (TAE):** O "aceite" no portal não finaliza o status do documento. O contrato **não** ficará marcado como "Assinado" no sistema de imediato.
* **Fluxo de Envio:** Após a finalização da matrícula, o contrato deverá ser enviado para o TAE. Somente após a assinatura ser realizada de fato na plataforma de assinatura eletrônica (pelo link enviado por e-mail/token) é que o status será atualizado no TOTVS Educacional.

### ✅ Assinatura do contrato obrigatória na rematrícula

Este parâmetro define se a efetivação da rematrícula deve ser bloqueada até que a assinatura seja validada.

* **Comportamento:** Se marcado, o aluno/responsável **não consegue finalizar** o processo de rematrícula sem realizar a assinatura eletrônica do contrato.
* **Fluxo de Assinatura (Token):**

  1. O contrato é exibido em tela durante o processo.
  2. Ao optar por assinar, o TAE dispara automaticamente um **Token de Segurança** para o e-mail do usuário logado (que está realizando a rematrícula).
  3. O usuário deve copiar este token e inseri-lo no campo de validação exibido no próprio Portal do Aluno.
  4. Somente após a validação correta do token, o sistema confirma a assinatura do contrato e libera a conclusão da rematrícula.

### ✅ Restringir obrigatoriedade apenas conforme configurado na 'Parametrização por curso'

Este parâmetro ignora a configuração global, passando a respeitar a configuração individual da .

* **Comportamento:** Se marcado, a utilização e obrigatoriedade da assinatura com TOTVS Assinatura Eletrônica na rematrícula fica condicionada à 'Parametrização por curso' da habilitação da matrícula, podendo ter os seguintes comportamentos:

  + **Parametrização por curso com "Assinatura do contrato obrigatória na rematrícula":** o aluno/responsável **não consegue finalizar** o processo de rematrícula sem realizar a assinatura eletrônica do contrato;
  + **Parametrização por curso não configurada:** o aluno/responsável finaliza o processo de rematrícula apenas com aceite. O contrato ficará marcado como "Assinado" no sistema de imediato.
* **Nota:** Este parâmetro está disponível a partir dos patches **12.1.2510.223** e **12.1.2602.141.**

Definição de Assinantes

Neste grupo, selecione quais papéis (atores) devem assinar o documento.

* O sistema enviará o envelope para o e-mail cadastrado no RM para cada papel selecionado (Ex: Pai, Mãe, Responsável Financeiro, Fiador do contrato).
* **Nota:**

  + É imprescindível que os atores selecionados possuam CPF e E-mail válidos no cadastro de pessoas;
  + O fiador do contrato só será incluído como **co-assinante** no envelope enviado ao TAE, quando no contrato financeiro exista fiador associado, previamente, com os status "Aprovado" ou "Em avaliação";
  + A opção "Fiador do contrato" está disponível apenas no contexto do **Ensino Superior;**
  + A opção "Fiador do contrato" está disponível a partir dos patches **12.1.2510.223** e **12.1.2602.141.**

Nome do Documento

Permite personalizar como o arquivo será nomeado ao ser enviado para o TAE e salvo no GED.

* É possível utilizar **Tags Dinâmicas** (ex: `[RA]`, `[COD PERIODO LETIVO]`) para facilitar a identificação e busca posterior dos arquivos assinados.

 Veja Também

---

[Guia de Configuração da integração](https://tdn.totvs.com/pages/viewpage.action?pageId=1036767989)

[Guia de Envio e Gestão de Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=578823895)

[Guia Assinatura na Rematrícula](https://tdn.totvs.com/pages/viewpage.action?pageId=708104832)

[Guia Assinatura na Matricula - PS](https://tdn.totvs.com/display/LRM/02.06+Assinatura+do+contrato)
