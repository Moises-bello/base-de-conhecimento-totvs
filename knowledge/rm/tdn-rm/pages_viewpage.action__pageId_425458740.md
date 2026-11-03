---
content_hash: 9b5e9e709259683497f9aa1a8387a6e47e7805d3f002dbbdd632524e001ee5a3
fetched_at: '2026-06-29T00:09:31.832967+00:00'
page_id: '425458740'
product: rm
source: tdn-rm
title: Copiar Matriz Aplicada para outro Período letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458740
version: 7
---

O processo Cópia de matriz aplicada para outro período letivo tem por objetivo realizar a cópia dos parâmetros definidos em uma "Parametrização por curso", para uma ou várias matrizes de destino, ou para um período letivo completo, podendo-se copiar além das configurações da "Parametrização por curso", também os documentos obrigatórios, modelos de etapas e modelos de avaliações, anexados a cada parametrização por curso.

**Para este processo existem duas condições:**

1. Cópia de parametrizações por curso para outro período letivo:

    Será permitido selecionar várias parametrizações por curso de um mesmo período letivo e estas configurações serão copiadas para o período letivo de destino selecionado. Nesta opção, antes da execução do processo, será permitido informar os seguintes dados: períodos de matrícula, numeração e trancamento, plano de pagamento default e para personalização e competência contábil.

1. Cópia de parametrização para o mesmo período letivo:

    Será permitido selecionar somente uma parametrização por curso e as matrizes aplicadas de destino. Os dados da parametrização por curso serão copiados para todas as matrizes aplicadas selecionadas, no mesmo período letivo.

Assinatura Eletrônica - Parametrização do Documento do Diário de Classe

**Essa funcionalidade estará disponível a partir da versão 12.1.2310**

A Instituição de ensino, poderá definir o documento de diário de classe que será utilizado nas turmas/disciplinas e estará disponível no portal para os professores assinarem.

Ao informar o relatório no cadastro da Parametrização por curso, o mesmo documento estará disponível para a(s) Turma(s)/Disciplina(s) associada(s) a ela.

Caso a Matriz seleciona de ***Origem***, tenha um Documento para assinatura no Diário associado, o mesmo será copiado para as Matrizes de ***destino*** selecionadas.

A partir da versão 12.1.2402, foi incluído o campo Ocultar Quadro de Horários na matrícula através do portal.

A partir da versão 12,1,2510, foi incluído o campo "Copiar dados do contrato anterior na rematrícula":

A partir das versões 12,1,2510.223, 12.1.2602.141 e 12.1.2606 foi incluído o campo "Assinatura do contrato obrigatória com TOTVS Assinatura Eletrônica na rematrícula".  
É importante ressaltar que, esse parâmetro só ficará disponível, quando em Ambiente > Parâmetros > Educacional > RM Portal > Matrícula > Portal - Assinatura contrato, estiver marcado o parâmetro "Restringir obrigatoriedade apenas conforme configurado na 'Parametrização por curso'", conforme documentação [Assinatura Contrato - Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=1025212694).

A partir da versão 12.1.2510, ao marcar a opção para copiar os [documentos exigidos do aluno](https://tdn.totvs.com/display/LRM/Documentos+Exigidos+do+Aluno), os [documentos](https://tdn.totvs.com/display/LRM/Cadastro+de+Documentos) que estiverem com a flag '**Validar documento pela inteligência artificial'** também serão copiados mantendo essa configuração ativada.
