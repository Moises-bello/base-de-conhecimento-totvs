---
content_hash: 3498307368eec5ee05e4d41e3e5c1b305bc21595190b5b1b14e5bd8df081ba3d
fetched_at: '2026-06-29T00:08:07.244415+00:00'
page_id: '237375409'
product: rm
source: tdn-rm
title: TUWT51_DT_Cadastro_Candidato_Existe_Possui_Papel
type: documentation
url: https://tdn.totvs.com/display/LRM/TUWT51_DT_Cadastro_Candidato_Existe_Possui_Papel
version: 119
---

# CADASTRO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Cadastro de candidato* |
| **Situação/Requisito:** | *Ao tentar cadastrar um candidato que já existe e preenchendo todos os campos obrigatório, caso o candidato possua algum destes campos em branco no cadastro da base, o sistema alerta que tais campos são obrigatórios.* |
| **Solução/Implementação:** | *Foi identificado que foi inserido uma validação no cadastro de candidatos que se o usuário existir e possuir algum papel no sistema (aluno, professor ou funcionário) os dados cadastrais não poderão ser alterados porém existem campos em branco no cadastro do usuário que são obrigatórios no portal do processo seletivo, sendo assim, foi feito um ajuste para que os dados que já existem não sejam alterados, porém os dados que estão faltando no cadastro do usuário que são obrigatórios no portal sejam atualizados corretamente, assim permitindo o cadastro correto do candidato que já existe na base.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVBIOV* |
| **Requisito (ISSUE):** | *N/A* |

divs
