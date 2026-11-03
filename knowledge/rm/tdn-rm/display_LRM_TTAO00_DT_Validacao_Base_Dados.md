---
content_hash: 93aff4fbe4f8e13c2dd9c005eb5320b5ffc7af79bfa0492f29e415c2779e6491
fetched_at: '2026-06-29T00:06:07.733936+00:00'
page_id: '201737381'
product: rm
source: tdn-rm
title: TTAO00_DT_Validacao_Base_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAO00_DT_Validacao_Base_Dados
version: 3
---

# VALIDAÇÃO DE BASE DE DADOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Realizar validação dos campos na base de dados.* |
| **Situação/Requisito:** | Ao gravar a rua no cadastro do funcionário com mais de 40 caracteres, ao realizar a verificação da base de dados, é apresentado mensagem que o tamanho é muito grande. |
| **Solução/Implementação:** | Alterado o número de caracteres para 100 na validação do campo RUA na verificação de base de dados. |
| **Versões/Release:** | *11.82.41* |
