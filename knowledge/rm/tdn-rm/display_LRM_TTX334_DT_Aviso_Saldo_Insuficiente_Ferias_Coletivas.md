---
content_hash: 34fd260674028da20a2397068314ac6a0abcbfc16c74de225f950a051c64355a
fetched_at: '2026-06-29T00:06:21.767617+00:00'
page_id: '223181013'
product: rm
source: tdn-rm
title: TTX334_DT_Aviso_Saldo_Insuficiente_Ferias_Coletivas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTX334_DT_Aviso_Saldo_Insuficiente_Ferias_Coletivas
version: 1
---

# AVISO DE SALDO INSUFICIENTE NO CADASTRO DE FÉRIAS COLETIVAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Férias Coletivas* |
| **Situação/Requisito:** | *No cadastro de férias coletivas, quando o campo "Dias de Férias" não está preenchido, não é exibida a mensagem de aviso de saldo de férias menor que os dias concedidos.*  *Este problema só acontece caso pelo menos um Sindicato esteja com o parâmetro "Ignora feriados na contagem das férias" marcado.* |
| **Solução/Implementação:** | *Ajuste na consistência de saldo insuficiente no cadastro de férias coletivas, para exibir a mensagem de aviso, independente se for informado os dias de férias ou a data final do período.* |
| **Chamados   relacionados:** | *TTX334* |
| **Versões/Release:** | *12.1.9* |
