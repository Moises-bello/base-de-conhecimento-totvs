---
content_hash: c8e48bb228b1e1d884a0734475eb5bf529c962bae4c21c09e83cd55d1688dafc
fetched_at: '2026-06-29T00:08:47.019250+00:00'
page_id: '317319862'
product: rm
source: tdn-rm
title: DT Rematrícula Visualização do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317319862
version: 1
---

# Exibição de Contrato no processo de Rematrícula

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional. |
| **Função:** | Rematrícula - Listagem de Disciplinas |
| **Situação/Requisito:** | Exibição do contrato do aluno no processo de Rematrícula |
| **Solução/Implementação:** | Descrição da história criada para solução    Como: Aluno ou Responsável pelo Aluno Eu preciso: Visualizar o contrato Para conseguir: Informações legais sobre a minha matrícula.  Critérios de aceitação: • Se o parâmetro de "disponível para impressão" do contrato estiver marcado (Parâmetros -> Portal -> Matrícula), após a seleção do plano de pagamento, deve ser exibido o contrato para o aluno/responsável efetuar o aceite (será exibido um checkBox para que o aluno/responsável marque o aceite). Só será possível habilitar a próximo etapa da rematrícula se o checkBox em questão estiver marcado. • O contrato deve possuir um formato de título, cabeçalho, corpo e assinaturas. Alguns parâmetros podem definir a visualização de cada parte conforme abaixo (Parâmetros -> Portal -> Matrícula): -> Nome a ser utilizado para o contrato: Esse nome é visível na parte mais alta da janela a ser exibida. -> Visualizar cabeçalho: Esse cabeçalho deve conter os dados de logo da instituição, nome, CNPJ, Dados do endereço da instituição, telefone, Nome do aluno, CPF, Dados do endereço do aluno, Curso, Período letivo, Ciclo/Ano (Ensino básico)/Habilitação (Ensino superior) e Turno. -> Visualizar assinaturas: Essas assinaturas devem aparecer no final da tela de visualização do contrato e são as assinaturas da Instituição (parâmetro que define se será do diretor, secretário 1 ou secretário 2), do Aluno, do contratante (caso não seja o próprio aluno) e de duas testemunhas. No caso do contratante (caso não seja o próprio aluno), deve ter um espaço para o nome, RG, CPF e endereço. Para as testemunhas, espaço para nome, RG e CPF. • O corpo/texto do contrato deve ser exibido conforme o parâmetro "Texto do contrato financeiro" (Parâmetros -> Portal -> Matrícula) e as tags utilizadas devem ser substituídas de acordo com a informação solicitada. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/PORTALMOBILE01-13> |
| **Modelo:** |  |

Link documento de referência:
