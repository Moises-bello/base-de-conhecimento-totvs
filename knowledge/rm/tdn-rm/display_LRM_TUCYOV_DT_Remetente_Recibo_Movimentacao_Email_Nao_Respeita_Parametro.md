---
content_hash: 507685112016641f4c737f61f3361ab68db8f385e325fd2f1f75946b17ad1838
fetched_at: '2026-06-29T00:06:25.894466+00:00'
page_id: '224450184'
product: rm
source: tdn-rm
title: TUCYOV_DT_Remetente_Recibo_Movimentacao_Email_Nao_Respeita_Parametro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUCYOV_DT_Remetente_Recibo_Movimentacao_Email_Nao_Respeita_Parametro
version: 123
---

# ENVIO DE E-MAILS - RECIBOS DE MOVIMENTAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentações - Envio de recibos por e-mail* |
| **Situação/Requisito:** | *Quando a movimentação utiliza envio de recibos por e-mail, mesmo com o parâmetro do remetente marcado nos parâmetros de envio da aplicação para utilizar o remetente informado o sistema envia os dados do e-mail de retorno como o usuário logado e o remetente do email como o padrão da coligada definido nas configurações globais de envio de e-mails.* |
| **Solução/Implementação:** | *Foi feito o ajuste para que ao enviar um e-mail o sistema identifique corretamente o parâmetro definido e faça o envio utilizando o remetente correto, ou seja, caso esteja definido para utilizar o email da biblioteca, o sistema enviará o email utilizando como remetente o endereço informado nos parâmetros, caso contrário irá utilizar o email configurado nos parâmetros globais de envio de email.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUGHJ2* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
