---
content_hash: a405c6d5f56f3fbe6ba6a48fc612216587f55539e208e47d4f720bce324e04fc
fetched_at: '2026-06-29T00:09:08.503871+00:00'
page_id: '389550256'
product: rm
source: tdn-rm
title: 3566048 EDUCACIONAL01-6098 DT Datas de Competência Contábil do Período Letivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389550256
version: 1
---

# DATAS DE COMPETÊNCIA CONTÁBIL NO PERÍODO LETIVO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Período Letivo |
| **Situação/Requisito:** | Ao tentar realizar alguma alteração em um período letivo o sistema não permite emitindo mensagem de erro: “Coluna ‘DTCOMPETENCIAFINAL’ é somente leitura.” |
| **Solução/Implementação:** | Em alguns casos, o sistema tenta alterar a data final de competência contábil quando o registro é alterado. Porém, essa data está desabilitada para edição por existir contabilidade gerada. Portanto, o sistema foi alterado para verificar se não existe contabilidade gerada, antes de tentar alterar a data de competência contábil. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
