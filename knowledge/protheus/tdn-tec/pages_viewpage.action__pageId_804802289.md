---
content_hash: 6418adf62f5b6d597eae681a708e53c97abba235d5ff86d923a2ac28a632e4f4
fetched_at: '2026-07-02T19:24:28.670836+00:00'
page_id: '804802289'
product: protheus
source: tdn-tec
title: Correção - Não era possível iniciar o SmartClient Linux e MacOS com o "locallog"
  ligado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=804802289
version: 2
---

O SmartClient Linux e MacOS ficava travado após a tela de parâmetros iniciais quando o parâmetro "locallog" estava ligado.

|  |  |
| --- | --- |
| Situação | SmartClient Linux e MacOS ficam travados após a tela de parâmetro iniciais quando o "locallog" está ligado. |
| Ocorrência | O problema acontecia por um colateral numa melhoria para expandir a limitação do tamanho de texto que é possível ser colocado em buffer. |
| Correção | A expansão do limite de buffer foi corrigida para continuar suportando um tamanho de texto maior, porém sem o problema. |
| Informações adicionais | * Referente à ocorrência: DTCLIENT01-4405 * Disponível em builds superiores a 20.3.2.3 |
