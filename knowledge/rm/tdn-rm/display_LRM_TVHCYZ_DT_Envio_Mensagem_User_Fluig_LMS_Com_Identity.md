---
content_hash: 414da3145b70d73a42472dbfe97a81c9000ba7b750b66f1058780ce41a43b46a
fetched_at: '2026-06-29T00:08:16.349982+00:00'
page_id: '244939080'
product: rm
source: tdn-rm
title: TVHCYZ_DT_Envio_Mensagem_User_Fluig_LMS_Com_Identity
type: documentation
url: https://tdn.totvs.com/display/LRM/TVHCYZ_DT_Envio_Mensagem_User_Fluig_LMS_Com_Identity
version: 111
---

# ENVIO DE MENSAGEM USER PARA INTEGRAÇÃO COM FLUIG LMS EM AMBIENTE INTEGRADO COM IDENTITY

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Educacional.* |
| **Módulo:** | *TOTVS Gestão Educacional.* |
| **Função:** | *Envio de mensagem única para integrações entre Educacional e Fluig LMS* |
| **Situação/Requisito:** | *O sistema não envia mensagens únicas de usuários, em ambientes integrados com Identity, para integrações entre Educacional e Fluig LMS* |
| **Solução/Implementação:** | *Foi realizado um ajuste no sistema para permitir o envio de mensagens únicas de usuários, através da mensagem USER, quando houver ambiente integrado com o Identity.*  *Essa alteração se fez necessária para permitir atualização de informações de papéis e grupos de usuários, no Fluig, definidos nos parâmetros de integração no RM.*  *O envio da mensagem USER, de usuários de alunos e professor, será realizada através do cadastro de alunos professores, quando os mesmos tiverem usuários associados,*  *do processo de geração de usuários, do processo de carga inicial, dos processos integrados de matrícula com o Processo Seletivo e Terceirizado e a transferência de alunos entre coligadas.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | N/A |
| **Versões/Release:** | *12.1.10.161* |

divs
