---
content_hash: f0027c71b80216d0c9de04e960ec7bafa8a00b0cfba373ea1c48de03faa7c035
fetched_at: '2026-06-29T00:06:07.104989+00:00'
page_id: '201735189'
product: rm
source: tdn-rm
title: DT_Avaliacao_Final_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Avaliacao_Final_Estagio
version: 7
---

# Avaliação final do estágio

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Totvs Educacional |
| **Módulo:** | Educacional |

## Descrição

Foi implementado a opção do aluno e o supervisor criarem a Avaliação final do estágio.

**Aluno realiza avaliação final:**

O aluno cria a avaliação final através do portal no menu Acadêmico | Estágio/Emprego | Acompanhamento (Aba Estágios, botão Avaliação Final).

Para cadastrar uma avaliação o aluno deve informar a descrição, anexar arquivos se necessários, e o relatório final, caso o termo de compromisso do estágio esteja caracterizado como exigindo relatório final. Depois do cadastro a mesma deve ser enviada para aprovação do professor orientador.

Caso o parâmetro 1 esteja marcado, o aluno visualizará a descrição da avaliação do supervisor da empresa através da aba "Avaliação do Supervisor".

**Professor aprova/reprova avaliação final**:

O professor tem a opção de selecionar um aluno no qual ele orienta, para visualizar a avaliação final.

Caso o parâmetro 2 esteja marcado, o professor orientador visualizará a descrição da avaliação do supervisor da empresa através da aba "Avaliação do Supervisor".

**Supervisor realiza avaliação final:**

O supervisor da empresa cria a avaliação final através do portal no menu Administração | Estágio/Emprego | Avaliação Final.

Para cadastrar uma avaliação o supervisor deve informar a descrição, anexar arquivos se necessários, e o relatório final, caso o termo de compromisso do estágio esteja caracterizado como exigindo relatório final.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Totvs Educacional**, acesse **Configurações | Parâmetros | Estágio (Estágio 6/7)**.

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Permitir ao aluno visualizar a avaliação final do supervisor da empresa. |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Permite ao aluno visualizar no cadastro da avaliação final, qual foi a descrição da avaliação final do supervisor da empresa. |

        2. No **Totvs Educacional**, acesse **Configurações | Parâmetros | Estágio (Estágio 6/7)**.

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Permitir ao professor visualizar a avaliação final do supervisor da empresa. |
| **Tipo:** | Booleano (True/False) |
| **Cont. Por.:** | False |
| **Descrição:** | Permite ao professor visualizar no cadastro da avaliação final, qual foi a descrição da avaliação final do supervisor da empresa. |
