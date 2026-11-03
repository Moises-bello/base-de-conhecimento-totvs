---
content_hash: 97882680f841a31984996c3db88e65bd99cecb6b585aeed669397965604eecb1
fetched_at: '2026-06-29T00:06:16.769746+00:00'
page_id: '212899386'
product: rm
source: tdn-rm
title: TTNQY6_DT_ERRO_Sessao_Expirada
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNQY6_DT_ERRO_Sessao_Expirada
version: 1
---

# PORTAL PROCESSO SELETIVO - INSCRIÇÃO DE CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Inscrição de Candidato* |
| **Situação/Requisito:** | *Ao acessar o portal de inscrição, e deixar a sessão expirar, o sistema aprensenta a mensasgem "Object reference not set to an instance of an object."* |
| **Solução/Implementação:** | Foi incluído uma validação para verificar se o contexto da sessão está nulo, caso positivo o portal é redirecionado para a tela de login. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs

O portal de inscrições do processo seletivo apresenta a mensagem de referência de objeto não identificada, quando a seguinte situação ocorre:   
1) candidato loga no portal e deixar a sessão expirar.2) em seguida, vai até a página http://www.ifmg.edu.br/vestibular/ e clica no botão "INSCREVA-SE AQUI"
