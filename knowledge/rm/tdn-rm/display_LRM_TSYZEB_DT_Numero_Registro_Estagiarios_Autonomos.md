---
content_hash: 1fc32bde346f92aeba8024de159a922797c88bb4ba28d758a6891340710e3b01
fetched_at: '2026-06-29T00:06:02.874800+00:00'
page_id: '198949709'
product: rm
source: tdn-rm
title: TSYZEB_DT_Numero_Registro_Estagiarios_Autonomos
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYZEB_DT_Numero_Registro_Estagiarios_Autonomos
version: 4
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário* |
| **Situação/Requisito:** | *Ao ativar o parâmetro "Não cadastrar número de Ficha de Registro para Estagiários e Autônomos" e cadastrar um novo funcionário, caso seja preenchido o número de registro antes de mudar o tipo de funcionário para Autônomo ou Estagiário, o campo é bloqueado mas fica preenchido, exibindo a mensagem de erro ao tentar salvar o registro do funcionário.* |
| **Solução/Implementação:** | *Foi alterada a função para além de desabilitar o campo de Registro, também limpar qualquer valor previamente preenchido.* |
| **Chamados relacionados:** | *TSUDL9* |
| **Versões/Release:** | *12.1.7* |
