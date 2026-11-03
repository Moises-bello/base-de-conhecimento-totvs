---
content_hash: 4e2b9003a787743e4e23cf34e963301ed34fb50b277e92446dc465eb93d7c1ba
fetched_at: '2026-06-29T00:08:41.375515+00:00'
page_id: '286723927'
product: rm
source: tdn-rm
title: DT Melhoria Permissões por Tipo de Movimento por Usuário.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286723927
version: 106
---

# Melhoria Permissões por Tipo de Movimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Permissões por Tipo de Movimento* | *MovUsrTmvAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Cadastro de Usuários*.* | *GlbUsuarioAction* | |  |  | |
| **Cadastros Iniciais:** | *Cadastro de Usuários*  *Cadastro de Tipo de Movimento* |
| **Parâmetro(s):** | *Não se aplica* |
| **Ponto de Entrada:** | **Não se aplica** |
| **Tickets relacionados** | *Não se aplica* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | **MATESTCNTFTOF01-638** |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle* |
| **Tabelas Utilizadas:** | *TUSRTMV* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Essa implementação visa melhorar a usabilidade do processo de concessão de permissões de tipo de movimento por usuário.

No anexo "Permissões por Tipo de Movimento" do Cadastro de Usuários agora é possível pesquisar por Código e Nome do Tipo de Movimento, possibilitando navegar facilmente entre registros e assim definir/alterar permissões de tipo de movimentos com mais agilidade.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da Biblioteca RM *12.1.18.*

## Procedimento para Utilização

       1.            Acessar Serviços Globais |  Segurança | Usuários.

       2.            Selecionar o "Sistema : Gestão de Estoque, Compras e Faturamento", o usuário desejado e o acessar Anexos | Permissões por Tipo de Movimento.

       3.            Na tela de Permissões por Tipo de Movimento clicar no botão "Procurar".

       4.            São apresentados para seleção os campos Código e Nome do Tipo de Movimento.

       5.            Após escolher o campo para pesquisa, basta digitar os dados do movimento desejado para realizar a busca. Ao inserir os dados do Tipo de Movimento desejado, automaticamente na grid inferior, a seleção será posicionada sobre o tipo movimento.

       7.            Com o Tipo de Movimento selecionado, basta escolher as permissões desejadas e Salvar.

divs
