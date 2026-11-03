---
content_hash: 98b794f703d7c3642552f874098d23a98868ebb66fd596b89d834da34106eca2
fetched_at: '2026-06-29T00:08:38.893881+00:00'
page_id: '285999917'
product: rm
source: tdn-rm
title: RHU01-1047 Exame Toxicológico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=285999917
version: 102
---

# Exames

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Segurança e Saúde Ocupacional |
| **Rotina:** | |  | | --- | | **Rotina** | | *Exames* |  |  | | --- | | **Rotina(s) envolvida(s)** | | *Parametrizador* | | *Assistente de Lançamento de Exames* | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RHU01-1047 |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | VEXAMESPRONT |

## Descrição

Foi criada a coluna CODLAUDOEXAME na tabela VEXAMESPRONT, que deverá ser preenchida com o código do laudo do exame. Porém o mesmo não é um campo de preenchimento obrigatório e se fez necessário para enviar informações para o RMLABORE contemplar a legislação do [CAGED](http://tdn.totvs.com/pages/viewpage.action?pageId=285656485).

## Procedimento para Implantação do 'Exame Toxicológico'

O sistema é atualizado logo após a aplicação do pacote *12.1.18*.

1. No parametrizador do Segurança e Saúde Ocupacional, parametrize o exame toxicológico
2. Ao lançar o exame informe o código do laudo
3. Estas informações serão utilizadas pelo RMLabore na geração do [CAGED](http://tdn.totvs.com/pages/viewpage.action?pageId=285656485).

divs
