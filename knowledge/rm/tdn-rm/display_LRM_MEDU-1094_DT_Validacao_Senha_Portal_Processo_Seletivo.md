---
content_hash: 9807361b1bff3443a55245192e9a08e812f1b4e2746e241cc88ed15864cc188d
fetched_at: '2026-06-29T00:08:22.221487+00:00'
page_id: '269085468'
product: rm
source: tdn-rm
title: MEDU-1094_DT_Validacao_Senha_Portal_Processo_Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-1094_DT_Validacao_Senha_Portal_Processo_Seletivo
version: 113
---

# PROCESSO SELETIVO - ACESSO AO PORTAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Processo Seletivo - Portal* |
| **Função:** | *Acesso ao portal de inscrições por meio de autenticação* |
| **Situação/Requisito:** | *Foi identificado uma inconsistência não tratada na mensagem de falha de logon no portal do processo seletivo.* |
| **Solução/Implementação:** | *A situação informada só ocorre quando por coincidência a senha informada é a mesma da criptografa no banco, o sistema valida corretamente que as senhas são diferentes ao criptografar a senha informada e comparar com atual salva no banco de dados, porém no momento de validar por qual ponto o usuário não autenticou, a comparação da senha é feita considerando a senha informada e a criptografada do banco, assim o sistema não identifica diferença e não trata esse tipo de situação, assim retorna um erro não esperado, sendo assim foi feito um tratamento para sempre comprar as senhas verificando se a base está criptografada ou não, ou seja, validará corretamente se as senhas são iguais ou não.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
