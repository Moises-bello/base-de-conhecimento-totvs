---
content_hash: 1021ca73e8cd5efc80a7cb65e06125aa6bb79f0a204c438f193f4844111082be
fetched_at: '2026-06-29T00:06:06.257668+00:00'
page_id: '201729428'
product: rm
source: tdn-rm
title: TTDHGJ_DT_Copia_Referencia
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDHGJ_DT_Copia_Referencia
version: 1
---

# Cópia por Referência

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Cópia por Referência* |
| **Situação/Requisito:** | Durante o processo de Cópia por Referência, após salvar o movimento gerado, o sistema demora alguns segundos para fechar a tela de conclusão do processo. |
| **Solução/Implementação:** | Foram realizadas melhorias de performance no processo responsável pela cópia por referência de movimento. Após salvar o registro, a tela do assistente de cópia demorava alguns segundos para fechar, identificamos uma solicitação de processamento ao servidor de Jobs desnecessária, ao remover tal solicitação tivemos um ganho em performance. |
| **Conversores e Parâmetros:** | *Não se Aplica.* |
| **Chamados relacionados:** | *Não se Aplica.* |
| **Requisito (ISSUE):** | *Não se Aplica.* |
| **Versões/Release:** | *12.1.8* |
|  |  |
