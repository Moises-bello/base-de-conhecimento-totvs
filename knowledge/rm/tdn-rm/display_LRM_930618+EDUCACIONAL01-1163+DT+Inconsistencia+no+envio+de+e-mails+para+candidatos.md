---
content_hash: 6d9a589a7ae4b77c8c8bd1e8878f8b911bd8a0a46e0ed8f89b6a171271bd8fa0
fetched_at: '2026-06-29T00:08:35.969579+00:00'
page_id: '283396071'
product: rm
source: tdn-rm
title: 930618 EDUCACIONAL01-1163 DT Inconsistencia no envio de e-mails para candidatos
type: documentation
url: https://tdn.totvs.com/display/LRM/930618+EDUCACIONAL01-1163+DT+Inconsistencia+no+envio+de+e-mails+para+candidatos
version: 99
---

# INCONSISTÊNCIA NO ENVIO DE E-MAILS DE PROCESSOS SELETIVOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Envio de e-mails para candidatos* |
| **Situação/Requisito:** | *Ao executar o processo de envio de e-mails para candidatos, o sistema não está envio para aqueles que possuem boletos baixados.* |
| **Solução/Implementação:** | **Foi identificada uma alteração que limitava o envio de e-mails somente a candidatos que tinham boletos em aberto. Foi realizado um ajuste para que não haja essa condição, um vez que a relação com o boleto é somente para que possamos informar o seu código de IPTE.**  **Com esse ajuste, o sistema não considerará mais filtros com relação a situação do boleto, porém foi restringido a geração de apenas um boleto por lançamento de inscrição de candidato. Caso haja mais de um boleto em aberto para uma mesma inscrição o sistema irá buscar o IPTE do primeiro registro retornado no filtro, uma vez que temos apenas uma TAG para a sua informação.**  **Com isso, o código IPTE será retornado em branco, caso o filtro não encontre nenhum boleto em aberto ou não tenha um código gerado.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
