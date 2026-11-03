---
content_hash: b8e3dcb50b84a8fa872f7c4ce9ad0bb25041a5473b451df9b5bb3c08cc0cfd6b
fetched_at: '2026-06-29T00:06:21.975835+00:00'
page_id: '223908796'
product: rm
source: tdn-rm
title: TTSPYL_DT_Erro_Acessar_ConsultaQuiosque_Perfil_NaoAdministrador
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSPYL_DT_Erro_Acessar_ConsultaQuiosque_Perfil_NaoAdministrador
version: 118
---

# QUIOSQUE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Consulta pelo quiosque* |
| **Situação/Requisito:** | *Ao utilizar a consulta ao acervo pelo quiosque o sistema reporta um erro informando que não foi possível acessar um caminho do registro do windows.* |
| **Solução/Implementação:** | *Foi identificado que este erro ocorre quando a tela é aberta, pois o sistema tenta desativar o gerenciador de tarefas do windows para desabilitar funções do usuário, porém quando o usuário autenticado no windows não possui privilégios de administrador o sistema retorna erro ao desabilitar. Foi inserido um tratamento no momento que o sistema tenta desabilitar o gerenciador de tarefas para verificar se o usuário autenticado é administrador, se não for o sistema retorna uma mensagem de erro informando que não foi possível desabilitar o gerenciador de tarefas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | *12.1.9* |

divs
