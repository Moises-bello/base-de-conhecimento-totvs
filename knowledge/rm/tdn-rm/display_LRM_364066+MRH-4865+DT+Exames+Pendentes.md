---
content_hash: d8b0c39beb4fa39b5a61c5661c198a2f3a9db36764ab656fec5fd63290e74856
fetched_at: '2026-06-29T00:08:28.658796+00:00'
page_id: '271678342'
product: rm
source: tdn-rm
title: 364066 MRH-4865 DT Exames Pendentes
type: documentation
url: https://tdn.totvs.com/display/LRM/364066+MRH-4865+DT+Exames+Pendentes
version: 109
---

# EXAMES PENDENTES

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Segurança e Saúde Ocupacional |
| **Função:** | Exames Pendentes |
| **Situação/Requisito:** | Ao cadastrar rescisão por transferência para funcionário, é lançado exame pendente demissional para a chapa. Porém, ao dar continuidade no processo de transferência, a chapa é transferida para o registro ativo e o registro demitido fica com nova chapa mas o exame pendente que foi lançado não é atualizado, induzindo o usuário a pensar que o exame demissional foi lançado para a chapa ativa do funcionário. |
| **Solução/Implementação:** | Realizada melhoria de forma a atualizar a chapa no anexo de exames pendentes ao realizar uma transferência com rescisão, quando a flag "Altera Chapa do Funcionário Demitido" estiver marcada. Neste caso todos os exames pendentes da chapa atual e ativa serão migrados para a nova chapa demitida. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** | 364066 |
| **Requisito (informe o requisito relacionado):** |  |

divs
