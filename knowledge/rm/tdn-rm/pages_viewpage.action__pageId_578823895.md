---
content_hash: 24157ad645593e1769d4b92a01312a3d39d68b4594767b9dc19f44267a1d0336
fetched_at: '2026-06-29T00:10:53.711786+00:00'
page_id: '578823895'
product: rm
source: tdn-rm
title: Processo de Envio e Gestão de Documentos (Contratos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578823895
version: 133
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

Esta funcionalidade permite o envio manual (individual ou em lote) e o gerenciamento do ciclo de vida dos contratos.

**Quando utilizar esta rotina?** Utilize o envio manual ou a gestão de documentos nos seguintes cenários:

* 🔁 **Reenvio de Contratos:** Correção de documentos enviados com erro ou expirados.
* 📦 **Processamento em Lote:** Envio massivo para matrículas realizadas presencialmente.
* 📜 **Legado:** Regularização de contratos de períodos anteriores.
* 🔍 **Auditoria e Gestão:** Conferência de status ou cancelamento de envelopes enviados indevidamente.

false🔐 Pré-requisitos de Acesso (Permissões)

Antes de executar o processo, valide se o perfil do usuário possui as permissões adequadas nos Serviços Globais.

**Caminho para Validação:** Serviços Globais > Segurança > Perfis > **Sistema: Educacional** > Acesso a Menus

**Permissão Obrigatória:** Habilite a permissão no seguinte caminho: 📂 **Financeiro/Contábil** └── 📂 **Contrato** └── ✅ **Integração TOTVS Assinatura Eletrônica**

false🔐 Autenticação de Usuário (Login TAE)

Para garantir a integridade dos dados, o sistema realiza uma validação de credenciais em tempo real sempre que a rotina de envio é acionada. Isso garante que apenas usuários autenticados no TAE possam disparar documentos.

#### **Fluxo de Verificação**

Ao acessar o menu ou executar o processo de integração, o TOTVS Educacional realiza a seguinte verificação automática:

👤 **Usuário acessa o menu  
Integração TOTVS Assinatura Eletrônica**

⬇️

❓ **Sistema verifica:**  
Existe token de autenticação válido?

✅ **Sim**  
Token válido

⬇️

🔓 **Acesso liberado ao menu  
Integração TOTVS Assinatura Eletrônica**

🔒 **Não**  
Token inexistente ou expirado

⬇️

🔐 **Sistema solicita autenticação**  
(pop-up de login)

⬇️

🔓 **Token gerado/renovado  
Acesso liberado ao menu**
