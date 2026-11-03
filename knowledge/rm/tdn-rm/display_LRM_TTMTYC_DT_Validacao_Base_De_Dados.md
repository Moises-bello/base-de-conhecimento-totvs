---
content_hash: 843af32b9882c178fd2d1c1e3ff9c0f93c07233d569f9ec763c8f6f2b5a8684d
fetched_at: '2026-06-29T00:06:14.984041+00:00'
page_id: '210050929'
product: rm
source: tdn-rm
title: TTMTYC_DT_Validacao_Base_De_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMTYC_DT_Validacao_Base_De_Dados
version: 3
---

# VALIDAÇÃO DA BASE DE DADOS REFERENTE AO CAMPO BAIRRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Validação da base de dados referente ao campo bairro* |
| **Situação/Requisito:** | Ao informar o bairro no cadastro do funcionário com 31 caracteres e realizar a validação da base de dados, apresenta uma mensagem no log do funcionário com o seguinte incidente: Verificação do funcionário XXXXX. Erro - String p/ bairro – CIDADE ANTONIO ESTEVAO CARVALHO muito grande. |
| **Solução/Implementação:** | Realizado a validação do campo Bairro para aceitar até 80 caracteres. Pois no banco de dados o campo banco da tabela ppessoa permite até 80. |
| **Chamados relacionados:** | TTMTYC |
| **Versões/Release:** | *11.82.42* |

divs
