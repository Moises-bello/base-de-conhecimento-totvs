---
content_hash: 792d0364ede4d6e2acc0ce732079b14c8474b0513fe5e5516a0fb2640cdfb143
fetched_at: '2026-06-29T00:10:12.251372+00:00'
page_id: '453302736'
product: rm
source: tdn-rm
title: DT TOP Mobile - Sincronismo automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453302736
version: 7
---

# TOP MOBILE - SINCRONISMO AUTOMÁTICO

## Características do Requisito

1553542711930\_-1548781199

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Sincronizar | Sincronizar Apontamentos | |
| **Cadastros Iniciais:** | Projeto, Insumos, Tarefas, Coletor, Usuário de Coletor, Folhas Tarefas |
| **Parâmetro(s):** | Não se aplica |
| **Ponto de Entrada:** | Não se aplica |
| **Tickets relacionados** | Não se aplica |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | Não se aplica |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | Não se aplica |

## Descrição

Possibilidade de sincronizar automaticamente os apontamentos de Avanço Físico caso exista rede disponível wifi ou rede de celular.

## Procedimento para Utilização

No TOP Mobile, na tela de configurações serão criados os seguintes campos:

* Habilitar/desabilitar o sincronismo automático.
  + "intervalo de tempo" (em minutos) que será realizado o sincronismo periodicamente.
  + tipo de rede que poderá ser executado o sincronismo:
    - wifi
    - wifi e celular (3g)

Haverá também uma tela com a listagem de log de execução do sincronismo informando:

* Data e hora da execução.
* Status da execução
  + Sucesso
  + Falha
* Mensagens de erros do sincronismo.

Caso o sincronismo seja habilitado, o botão de "sincronizar" (manualmente) deverá ser desabilitado.
