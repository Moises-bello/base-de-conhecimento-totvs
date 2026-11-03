---
content_hash: b2edf7de4d310a58c5638149293c38866787ea34edf24972e7f03eeaf27e2918
fetched_at: '2026-06-29T00:08:22.113263+00:00'
page_id: '269072244'
product: rm
source: tdn-rm
title: MRH-1857_DT_Parametrizador_Configuração_Chapa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269072244
version: 110
---

# CONFIGURAÇÃO DE CHAPA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrizador - Configuração de Chapa* |
| **Situação/Requisito:** | Quando o usuário alterar a configuração de chapas para numérica e marca o parâmetro ‘Cadastro Automático de Chapas Sequenciais’, ao tentar concluir o processo retorna erro. A máscara altera, mas o parâmetro não fica marcado. Mesmo se já tiver configurado a mascara e em um segundo momento marcar o parâmetro retorna o mesmo erro.  Não é possível realizar o processo de alteração do parâmetro 'Cadastro automático de chapas sequenciais'. Esse parâmetro é exclusivamente numérico. Favor verificar. |
| **Solução/Implementação:** | Foi implementada uma mensagem informativa sobre a funcionalidade do parâmetro 'Cadastro Automático de Chapas Sequenciais'.  Mensagem: Para a aplicação deste parâmetro todas as chapas já registradas na base devem estar em formato numérico.  Através da mensagem fica mais claro para o usuário que o parâmetro quando aplicada a uma base de dados já existente ela deve seguir a regra de chapas apenas com valores numéricos. |
| **Chamados relacionados:** | *MRH-1857* |

divs
