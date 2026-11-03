---
content_hash: f5945c054955f89a80765ada31abc660895fae5505688edf4e13f76a4ed9f3f4
fetched_at: '2026-06-29T00:06:08.543080+00:00'
page_id: '201749288'
product: rm
source: tdn-rm
title: TTEYGW_DT_Cadastro_De_Funcionario_Com_Dados_Existentes
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEYGW_DT_Cadastro_De_Funcionario_Com_Dados_Existentes
version: 1
---

# CADASTRO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Cadastro de Funcionário* |
| **Situação/Requisito:** | *Ao tentar cadastrar um novo funcionário utilizando os dados de uma pessoa previamente cadastrada no sistema é exibida uma mensagem de erro: "Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados."* |
| **Solução/Implementação:** | *O erro se dava por uma inconsistência dos dados após a cópia dos dependentes. A inconsistência foi resolvida para que o cadastro pudesse continuar sem erros.* |
| **Chamados relacionados:** | TTEYGW |
| **Versões/Release:** | 12.1.7 |
