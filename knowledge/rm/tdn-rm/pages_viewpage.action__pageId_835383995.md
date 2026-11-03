---
content_hash: aea4a28eb3f72f6f5582661d720eae4e495f36405fd7caad3ac24f8254429b18
fetched_at: '2026-06-29T00:11:49.596842+00:00'
page_id: '835383995'
product: rm
source: tdn-rm
title: Configurações dos Parâmetros Gerais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=835383995
version: 10
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Configuração de Parâmetros**

PainelVisão Geral

## **01. VISÃO GERAL**

Esta documentação detalha as funcionalidades disponíveis para configuração no Portal do Paciente. O objetivo é definir comportamentos padrões e personalizar a experiência do usuário no sistema, garantindo uma interação intuitiva e eficiente.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

A configuração de parâmetros no Portal do Paciente é uma ferramenta que permite aos administradores definir e personalizar o comportamento do sistema. Com essa funcionalidade, é possível:

* Mensagens Personalizadas: Configurar menagens específicas que serão exibidas para os usuários em diferentes etapas do agendamento ou em outras interações com o portal.
* Gerenciar Informações de Contato: Definir quais informações de contato serão exibidas no portal, como números de telefone ou endereços de e-mail, para facilitar a comunicação entre pacientes e a instituição.
* Estabelecer Relatórios Padrões de E-mail: Selecionar os relatórios que serão enviados automaticamente aos pacientes após a realização de agendamentos, consultas ou exames.
* Bloquear ou Permitir Ações: Determinar quais ações específicas da instituição e dos usuários, como a possibilidade de cancelar um agendamento ou agendar para outra pessoa.
* Criação de parâmetros para disponibilizar documentos do PEP no Portal do paciente, como:
  1. Atestados e Documentos
  2. Receitas
  3. Interconsulta Ambulatorial
  4. Solicitação/Pedido de Exame
  5. Pedido de internação e procedimento

Essas configurações garantem que o portal possa ser adaptado às necessidades específicas da instituição e dos usuários, proporcionando uma experiência personalizada e eficiente.

Tela Configuração de Parâmetros

## **03.****TELAS CONFIGURAÇÃO DE PARÂMETROS**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Permitir Agendamento | * Habilita ou desabilita a opção de agendar **Consultas, Tele consulta e Exames**, permitindo aos administradores controlar essa funcionalidade no Portal. * Define uma atividade padrão para cada tipo de agendamento. |
| Permitir Agendar para outra pessoa | * Habilita ou desabilita a opção de agendar para outra pessoa, permitindo aos administradores controlar essa funcionalidade no Portal. |
| Permitir Cancelamento via portal | * Habilita ou desabilita cancelar agendamentos pelo portal do paciente, permitindo aos administradores controlar essa funcionalidade no Portal. * Define quantas horas antes do agendamento marcado pode cancelar via portal do paciente. |
| Permitir Seleção de Convenio no agendamento | * Habilita ou desabilita o passo de seleção de convenio no portal do paciente. * Define um convenio padrão particular para instituição. |
| Relatórios | * Define relatório padrão para Agendamentos e Cancelamentos. |
| Avisos | * Permite a configuração de avisos específicos para agendamentos e resultado de exames, mantendo os usuários informados sobre procedimentos importantes. |
| Termos e Politicas do Portal do Paciente | * Estabelece o modelo para Termos de Uso e Políticas de Privacidade, permitindo o uso padrão do sistema, URL para ser redirecionado ou um relatório pré-definido no sistema. |
| Contatos para Exibir no Portal | * Exibe ou não o contato da instituição com telefone ou e-mail na parte inferior de toda as páginas do portal |
| Disponibilizar documentos do PEP no portal | * Permite configurar quais tipos de documentos do PEP serão disponíveis para download no portal do paciente; |
| Envio obrigatório de documentos | * Responsável por deixar obrigatório ou não, os campos de anexo de documentações do portal do paciente:   + Documentos de Identificação Pessoal;   + Documentos do Convênio;   + Documentos referentes ao Procedimento a ser realizado; |
| Tipo de documento | * Refere ao tipo de arquivo que será inserido em SZARQUIVO quando o anexo for enviado pelo paciente. O tipo é padrão pode ser selecionado para cada documento do portal do paciente: documentos pessoais, carteira do convênio e documentos relacionados a procedimento; |

## **04.****TELA CONFIGURAÇÃO DE PARÂMETROS**

**Principais Campos e Parâmetros**

| Campo | Descrição |
| --- | --- |
| PermitirAgendConsultaPortal | Habilita ou desabilita a opção de agendar consultas. |
| PermitirAgendTeleconsultaPortal | Habilita ou desabilita a opção de agendar tele consultas. |
| PermitirAgendExamePortal | Habilita ou desabilita a opção de agendar exames. |
| AtividadeConsultaPortal | Adiciona qual a atividade padrão para agendar consultas. |
| AtividadeTeleconsultaPortal | Adiciona qual a atividade padrão para agendar tele consultas. |
| AtividadeExamePortal | Adiciona qual a atividade padrão para agendar exames. |
| AgendarOutraPessoaPortal | Habilita ou desabilita a opção de agendar para outras pessoas. |
| CancelarAgendamentoPortal | Habilita ou desabilita o cancelamento de agendamentos via portal. |
| HorasCancelamentoAgPortal | Determina quantas horas antes do agendamento pode cancelar o mesmo via portal. |
| ConvenioParticularPadraoPortal | Habilita ou desabilita a seção convenio. |
| CodConvenioParticularPortal | Determina qual o convenio particular padrão da instituição. |
| CodPlanoParticularPortal | Determina qual o plano particular padrão da instituição. |
| CodSubplanoPortal | Determina qual o sub plano particular padrão da instituição. |
| RelAgendamentoPortal | Determina qual o relatório será utilizado para agendamentos e cancelamentos. |
| AvisoAgendamentoPortal | Permite a configuração de avisos específicos para agendamentos, mantendo os usuários informados sobre procedimentos importantes. |
| AvisoResultExamePortal | Permite a configuração de avisos específicos para resultados de exames, mantendo os usuários informados sobre procedimentos importantes. |
| TermoUsoPortal | Determina qual padrão de exibição o portal irá utilizar para mostrar os termos de uso, Padrão, URL ou relatório. |
| UrlTermoUsoPortal | Informa a ULR caso os termos de uso será URL. |
| RelTermoUsoPortal | Informa o relatório caso os termos de uso será relatório. |
| PolPrivacidadePortal | Determina qual padrão de exibição o portal irá utilizar para mostrar as politicas de privacidade, Padrão, URL ou relatório. |
| UrlPolPrivacidadePortal | Informa a ULR caso os politicas de privacidade será URL. |
| RelPolPrivacidadePortal | Informa o relatório caso os politicas de privacidade será relatório. |
| TelContatoPortal | Informa o telefone de contato da instituição caso preenchido. |
| EmailContatoPortal | Informa o e-mail de contato da instituição caso preenchido. |

Para que as configurações sejam usadas no portal, é preciso que configure todas as variáveis necessárias antes de iniciar o uso do portal do pacienteIMPORTANTE!

## **05. TABELAS UTILIZADAS**

Para configurar os parâmetros gerais, utilizamos a mesma tabela que foi convertida de Delphi para C#. A documentação detalhada do uso desta tabela pode ser encontrada no seguinte link: [Documentação Totvs Gestão Hospitalar - Parâmetros](https://tdn.totvs.com.br/pages/viewpage.action?pageId=829293510).
