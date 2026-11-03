---
content_hash: d27cce706ee9e62695e1aaa7a6a223687155a3cc796e9c015c1933afbe907e4b
fetched_at: '2026-06-29T00:06:14.999439+00:00'
page_id: '210051025'
product: rm
source: tdn-rm
title: TTNNME_DT_Validacao_Base_De_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTNNME_DT_Validacao_Base_De_Dados
version: 2
---

# VALIDAÇÃO DA BASE DE DADOS REFERENTE AO CAMPO BAIRRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Validação da base de dados referente ao campo bairro* |
| **Situação/Requisito:** | Ao informar o bairro no cadastro do funcionário com 31 caracteres e realizar a validação da base de dados, apresenta uma mensagem no log do funcionário com o seguinte incidente: Verificação do funcionário XXXXX. Erro - String p/ bairro – CIDADE ANTONIO ESTEVAO CARVALHO muito grande. |
| **Solução/Implementação:** | Realizado a validação do campo Bairro para aceitar até 80 caracteres. Pois no banco de dados o campo banco da tabela ppessoa permite até 80. |
| **Chamados relacionados:** | TTNNME |
| **Versões/Release:** | *12.1.8* |

divs
