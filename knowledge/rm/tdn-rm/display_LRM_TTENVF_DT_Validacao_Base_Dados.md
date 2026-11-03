---
content_hash: 7d6731adee9b5fad884a2d973d246ffc86fc66d3df102d99f612881777268d70
fetched_at: '2026-06-29T00:06:07.766610+00:00'
page_id: '201737679'
product: rm
source: tdn-rm
title: TTENVF_DT_Validacao_Base_Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTENVF_DT_Validacao_Base_Dados
version: 4
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
| **Chamados relacionados:** | *TTENVF* |
| **Versões/Release:** | *12.1.8* |
