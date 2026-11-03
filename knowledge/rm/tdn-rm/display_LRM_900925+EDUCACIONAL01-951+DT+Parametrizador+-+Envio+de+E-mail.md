---
content_hash: 58e2c1f7c73c9b1714ba6bb419cfe3d57407d5d92f21c296aa99252dec832da6
fetched_at: '2026-06-29T00:08:34.767862+00:00'
page_id: '274840321'
product: rm
source: tdn-rm
title: 900925 EDUCACIONAL01-951 DT Parametrizador - Envio de E-mail
type: documentation
url: https://tdn.totvs.com/display/LRM/900925+EDUCACIONAL01-951+DT+Parametrizador+-+Envio+de+E-mail
version: 98
---

# PARAMETRIZADOR - ENVIO DE E-MAIL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo* |
| **Função:** | *Parametrizador - Envio de E-mail* |
| **Situação/Requisito:** | *Todos os e-mails enviados a partir do processo seletivo, tem como remetente o e-mail (cadastrado em: Parâmetros > Parâmetros do Sistema > Portal > E-mails , campo "E-mail do remetente de remetente do processo Seletivo") não grava nada no campo SENDER da tabela GMAILSEND, com isso Ao acessar Serviços Globais > Serviços > Histórico de e-mail enviados, o campo está em branco.* |
| **Solução/Implementação:** | *Incluído nos parâmetros de envio de e-mail do Processo Seletivo o campo de Nome do Remetente de e-mail, tal campo tem função de informar qual foi o remetente que enviou aquele e-mail, onde este será gravado no histórico de envio de e-mail.* |
| **Conversores e Parâmetros:** | *Processo Seletivo | Parâmetros | Parâmetros do Sistema | Portal | E-mails:*   * *Nome do remetente do processo seletivo* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
