---
content_hash: 80d7943b9018a69fe1d5b60951440ac961d7481f6d790efc0be82dc7fe6bb7ae
fetched_at: '2026-06-29T00:08:28.181882+00:00'
page_id: '271666499'
product: rm
source: tdn-rm
title: 361204 MRH-6106 DT Candidato - Permissao de Acesso
type: documentation
url: https://tdn.totvs.com/display/LRM/361204+MRH-6106+DT+Candidato+-+Permissao+de+Acesso
version: 113
---

# CANDIDATO - PERMISSÃO DE ACESSO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Candidato - Permissão de Aceso |
| **Situação/Requisito:** | Quando um usuário possui um perfil de acesso apenas ao módulo do Gestão de pessoas, no qual o acesso ao item '02.01.02.08 - Endereço Principal: Alterar' está negado, é apresentada a mensagem de erro abaixo, ao acessar o cadastro de Candidatos: ''Coluna 'CEP' é somente leitura. Código da Informação: [7534cb43f97fed6c9ef2534490fac6ca]'' |
| **Solução/Implementação:** | Melhorado o método pois o campo CEP precisa passar por uma máscara antes de mostrar na tela, assim é necessário que o campo fique como 'ReadOnly = false', para fazer as alterações, depois ele volta para o estado inicial. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | 361204 |
| **Requisito (ISSUE):** |  |

divs
