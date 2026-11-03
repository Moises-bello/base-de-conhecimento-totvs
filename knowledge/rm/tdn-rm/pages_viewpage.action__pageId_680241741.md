---
content_hash: 5d4cdb018d9f85f05e4877fdd55d5fa353594bcce4dbaf85e2560ec134040494
fetched_at: '2026-06-29T00:11:17.429756+00:00'
page_id: '680241741'
product: rm
source: tdn-rm
title: FISCAL01-17626 - DT - Tratamento de regra do Sonar de manipulação de diretório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680241741
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Guias Apuração |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17626 |

## **02. SITUAÇÃO/REQUISITO**

Substituir o uso de métodos nativos do .Net para manipulação de diretórios pelos métodos propostos pela Lib.

Neste caso substituir o System.IO.Directory.CreateDirectory pelo RM.Lib.IO.RMSDirectory.CreateDirectory.

Atuar na rotina RM.Fis.RotinasFiscais\Municipais\NFSe\SalvaXml.

## **03. SOLUÇÃO**

Alterado o uso da função nativa pela função da Lib.

Essa chamada:

Pôde ser ser simplificada para:

O create directory da Lib tem um comportamento diferente que o nativo quando está sendo executado no server. O path que a função recebe como parâmetro não é absoluto, sendo concatenado com um path padrão: “C:\RM\Atual\Release\Bin\Arquivos”.

Se a função receber o código de coligada 1 o caminho “C:\RM\Atual\Release\Bin\Arquivos\1” seria obtido.

Quando a função é utilizada no lado client o comportamento é o mesmo da nativa.

Em todos os casos a verificação se o diretório existe é desnecessária, a função apenas cria o diretório se o mesmo não existir.
