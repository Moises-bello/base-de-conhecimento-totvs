---
content_hash: 50b3d8c270c773ec8889095ac7c4b5b3882b48cee78ce5b59513aabc2e379a52
fetched_at: '2026-07-02T19:24:21.560471+00:00'
page_id: '268586713'
product: protheus
source: tdn-tec
title: Problema de tela desconfigurada quando utilizado o componente TWorkSpaceFolder
type: documentation
url: https://tdn.totvs.com/display/tec/Problema+de+tela+desconfigurada+quando+utilizado+o+componente+TWorkSpaceFolder
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Quando o tamanho do componente TWorkSpaceFolder é alterado depois da criação da session, a tela não é exibida corretamente, ficando desconfigurada.  Simulação:  1. Abrir o programa FIN30058; 2. Realizar uma pesquisa, para trazer todos os registros; 3. Com o primeiro registro exibido em tela, clicar em Documentos & Títulos; 4. Abrir um dos relacionamentos exibidos na tela de "Relacionamento ADs"; 5. Nesse momento, a tela do FIN30058 não é exibida corretamente. |
| Correção | Corrigido para que seja atualizado o tamanho da session quando o tamanho da TWorkSpaceFolder é alterado. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: SCHTML-474 * Disponível a partir da build 7.00.131227A - 3.2.1 |
