---
content_hash: 7ecf6aee590ce92eb9d440c085eb8e16bd9de6c23f07f2653c0094b542c466ad
fetched_at: '2026-06-29T00:08:19.969110+00:00'
page_id: '267802555'
product: rm
source: tdn-rm
title: TVXWG8_DT_Cadastro_Aluno_Sempre_Em_Edicao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVXWG8_DT_Cadastro_Aluno_Sempre_Em_Edicao
version: 111
---

# Cadastro de aluno

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Cadastro de aluno |
| **Situação/Requisito:** | Ao abrir o cadastro de aluno, o botão de salvar fica sempre habilitado mesmo clicando para salvar, ele não é desabilitado.  Ao tentar editar um Afiliado, sempre é exibida uma mensagem informando que é necessário salvar para editá-lo. |
| **Solução/Implementação:** | Foi identificado que o sistema do RH realiza um ajuste na máscara de CEP após a leitura das informações do banco de dados.  Isso faz com que o registro sempre esteja em edição.  Foi realizado um ajuste para que essa edição seja tratada e o cadastro volte ao estado normal. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
