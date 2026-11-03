---
content_hash: 8ff5692beb48ccec41960ae44fbb2c0a320004267d80f3e4338499e1c8b6ce73
fetched_at: '2026-06-29T00:10:15.878734+00:00'
page_id: '465382513'
product: rm
source: tdn-rm
title: DT Novo Ensino Médio - Atividades Acadêmicas – Certificação no Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465382513
version: 8
---

# CERTIFICAÇÃO NO ENSINO BÁSICO

## Geração do certificado para o contexto do ensino Básico.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Certificação | Certificação no nível de ensino Básico |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro da atividade acadêmica "Certificados". | Certificação no ensino Básico | | Cadastro da atividade acadêmica "Certificados", via anexo do Aluno |  | | Cadastro da atividade acadêmica "Certificados", via anexo do Professor |  | | Cadastro da atividade acadêmica "Certificados", via anexo da Comissão Coordenadora da matriz aplicada. |  | |
| **Cadastros Iniciais:** | - Atividades Acadêmicas | Certificados/Diplomas | Competência.  - Atividades Acadêmicas | Certificados/Diplomas | Mais | Tipo de participação.  - Atividades Acadêmicas | Certificados/Diplomas | Mais | Tipo de certificação. |
| **Parâmetro(s):** | *N/A* |
| **Tickets relacionados** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | EDUCACIONAL01-8305 / [EDUCACIONAL01-8306](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-8309) / [EDUCACIONAL01-8307](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-8309) / [EDUCACIONAL01-8308](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-8309) / [EDUCACIONAL01-8309](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-8309) / [EDUCACIONAL01-8575](http://jiraproducao.totvs.com.br/browse/EDUCACIONAL01-8309) |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SCERTIFICADO, SCOMPETENCIA, STIPOCERTIFICADO, STIPOPARTICIPACAO, SPARTICIPANTE |
| **Sistema(s) Operacional(is):** | *Windows 7, 8 e 10* |

## Descrição

A atividade acadêmica foi alterada para permitir o cadastro de Certificação no contexto do ensino Básico, bem como seus anexos e cadastros auxiliares. Nos cadastros de Alunos, Professores, Comissão Coordenadora possuem anexos com a descrição "Certificação" que faz acesso à esta atividade acadêmica.

Este módulo era disponibilizado somente para o ensino superior, com a descrição de "Certificação / Diplomas".

Importante: Diplomação, Solenidade e Registro no Livro **não** serão disponibilizados para o ensino básico.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da release 12.1.24 contendo script de criação de campos.

## Procedimento para Utilização

## 1 - Cadastro de Certificação na Atividade Acadêmica - Ensino Básico

Para cadastrar um Certificado na atividade acadêmica, para o ensino básico, deve-se acessar o menu "Atividades Acadêmicas | Certificados".

Este mesmo cadastro pode ser acesso através dos seguintes anexos:

- Currículo e Ofertas | Alunos | Anexos | Certificação

- Currículo e Ofertas | Professores | Anexos | Certificação

- Currículo e Ofertas | Matrizes Curriculares | Anexos | Matriz Aplicada | Anexos | Comissão coordenadoras | Anexos | Certificação

Descrição do menu

No contexto do ensino superior este menu tem a descrição de "Atividades Acadêmicas | Certificados/Diplomas", já no contexto do ensino básico a descrição do menu é "Atividades Acadêmicas | Certificados".

Os itens abaixo não serão disponibilizados para o contexto de ensino básico. Estes campos encontram-se disponíveis somente para os contextos relacionados ao nível de ensino superior.

Geração de Diplomação e Solenidade.

## 2 - Processo de Geração de Certificados na Atividade Acadêmica - Ensino Básico

As informações referentes a Registro no Livro foram ocultados. Apenas são disponíveis para o nível superior.

No contexto do ensino Básico, um dos itens chama-se "Certificação", já no contexto do ensino Superior teremos "Diplomação" .

**Exemplo:**
