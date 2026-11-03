---
content_hash: 0bcfdab088a38004a7d5d4c72c5c2e690d3978b8759ec5c0fd6607eb13163c6e
fetched_at: '2026-06-29T00:06:02.867613+00:00'
page_id: '198949665'
product: rm
source: tdn-rm
title: TSUDL9_DT_Numero_Registro_Estagiarios_Autonomos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUDL9_DT_Numero_Registro_Estagiarios_Autonomos
version: 3
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário* |
| **Situação/Requisito:** | *Ao ativar o parâmetro "Não cadastrar número de Ficha de Registro para Estagiários e Autônomos" e cadastrar um novo funcionário, caso seja preenchido o número de registro antes de mudar o tipo de funcionário para Autônomo ou Estagiário, o campo é bloqueado mas fica preenchido, exibindo a mensagem de erro ao tentar salvar o registro do funcionário.* |
| **Solução/Implementação:** | *Foi alterada a função para além de desabilitar o campo de Registro, também limpar qualquer valor previamente preenchido.* |
| **Chamados relacionados:** | *TSUDL9* |
| **Versões/Release:** | *11.82.41* |
