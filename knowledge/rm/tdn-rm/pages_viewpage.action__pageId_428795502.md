---
content_hash: 7700511b89788947649b9d9c297ee6b2e6800e96ce7ff4dd051378390376d9d1
fetched_at: '2026-06-29T00:09:38.676557+00:00'
page_id: '428795502'
product: rm
source: tdn-rm
title: 4246970 PORTALMOBILE01-6090 DT MaxLength no campo Complemento durante a inscrição
  de candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=428795502
version: 1
---

# Definição de MaxLength no campo Complemento durante a inscrição de candidato

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Educacional |
| **Função:** | Inscrição de candidato |
| **Situação/Requisito:** | O campo de Complemento de endereço para o Pai e Mãe do candidato, não possuía MaxLength definido. Permitindo ao usuário digitar uma grande quantidade de caracteres, porém, emitindo erro ao confirmar a inscrição. |
| **Solução/Implementação:** | Foi incluído a tag de MaxLength no campo de Complemento do endereço, para Pai e Mãe do candidato durante o processo de inscrição. Desta forma, não irá permitir ao usuário digitar uma quantidade maior do que 30 caracteres, no qual é o limite do campo no banco de dados. Evitando com que ocorra erros durante a confirmação da inscrição. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
