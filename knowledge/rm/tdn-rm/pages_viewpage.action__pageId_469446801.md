---
content_hash: 86f7c3659ec2fccc7f4eea5e50ee5d34344c5369b340de6c2afad0f3275259ea
fetched_at: '2026-06-29T00:10:16.436614+00:00'
page_id: '469446801'
product: rm
source: tdn-rm
title: 5381947 FISCAL01-8527 DT NFS-e Vespasiano - Código Município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469446801
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Enviar NFS-e |
| Ticket: | 5381947 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8527 |

## **02. SITUAÇÃO/REQUISITO**

Quando é emitido uma NFS-e (Vespasiano-MG), onde o tomador é de nacionalidade Estrangeira e endereço no Brasil ocorre a seguinte inconsistência: Não foi possível enviar a nota. Identificador do Movimento: 10251 TSS - Erro na validação desta nota. Element 'CodigoMunicipio': Conteúdo do campo não obedece ao Esquema da NFS-e. O valor '99999' não é aceito pelo padrão estabelecido pela SEFAZ: '[0-9] {7} '. O RM gera a tag como 99999 e a tag como EX. Segue anexo os logs da wslogxml. De acordo com a manual da prefeitura de Vespasiano, a tag deve ter tamanho 7. ![](<https://totvssuporte.zendesk.com/attachments/token/cWipN0ZWgWJuARfR3V5zWaLYO/?name=inline101468> 693.png)

## **03. SOLUÇÃO**

Foi alterado a consistência que validava os Municípios e o tipo de Layout para geração do Código Município no sistema, agora está fixo para ser 9999999 (7 dígitos), refletindo nas tags ***codmunibge*** ou ***codmunsiafi***.
