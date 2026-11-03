---
content_hash: 367810edd2a5f5522489086184a715b7d71c1e6a617ae172c683896f9d59a622
fetched_at: '2026-06-29T00:10:58.235198+00:00'
page_id: '604527981'
product: rm
source: tdn-rm
title: 9764766 FISCAL01-14082 - DT REINF - Processo de Geração dos Eventos para Filial
  SCP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=604527981
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Ticket: | 9764766 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14082 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que ao gerar a REINF pelo RM, não está conseguindo gerar as informações para filial SCP, o mesmo informa que na geração da rotina pela integração com o TAF era parametrizado o "Código da Filial em sistemas externos", onde através dessa parametrização as informações da filial SCP era enviado através do CNPJ da filial matriz. Atualmente no envio pelo RM o sistema não está consistindo da mesma maneira, pois apresenta inconsistência devido o CNPJ da filial SCP ser diferente da filial matriz.

"Falha ao processar o evento de identificador 13 e tipo R-1000: O evento foi rejeitado, pelo(s) seguinte(s) motivo(s):

Código MS0015: Deve ser utilizado certificado digital do tipo e-CNPJ ou e-PJ cujo CNPJ base seja o mesmo do contribuinte responsável pela informação, ou do tipo e-CPF ou e-PF cujo CPF pertença ao representante legal do contribuinte ou qualquer certificado que pertença a um procurador devidamente habilitado no sistema de Procuração Eletrônica da RFB."

## **03. SOLUÇÃO**

Foi criado uma flag no cadastro de Filiais, a fim de considerar filiais SCP que não possuem a mesma raiz de CNPJ na geração dos eventos da REINF.

Para acessar o novo campo, vá em: Anexos | Dados Fiscais e marque a opção “Filial SCP transmite REINF através da Filial Matriz”

Comportamento:

* Flag marcada: O sistema gera os eventos da Filial SCP na Filial Matriz.
* Flag desmarcada: Os eventos da Filial SCP são gerados separadamente.

Disponível a partir da versão 12.1.29
