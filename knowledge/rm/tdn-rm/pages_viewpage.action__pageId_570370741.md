---
content_hash: b712a45a11e8dc6ff850e4bb6d3b491f955c0568b6e6368bd56792e150ca130c
fetched_at: '2026-06-29T00:10:52.163821+00:00'
page_id: '570370741'
product: rm
source: tdn-rm
title: DEDUSAGA-977 DT O campo Procedimento do Atendimento perde toda a sua formatação
  configurada no sistema ao ser exibido no portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570370741
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Segmento: | Educacional |
| Módulo: | CRM |
| Função: | Solicitações |
| Ticket: | [10115795](https://totvssuporte.zendesk.com/agent/tickets/10115795 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | DEDUSAGA-977 |

## **02. SITUAÇÃO/REQUISITO**

Estamos inserindo um texto ao campo Procedimento do Atendimento, porém o texto perde toda a sua formatação ao ser exibido no Requerimento do Portal do Aluno. Nesse campo, também queremos adicionar uma imagem, exibindo os planos de pagamento disponíveis para a definição do plano de pagamento, porém o campo não aceita imagem.

## **03. SOLUÇÃO**

Otimizado o processo para que seja possível realizar a quebra de linha no campo: "Procedimento" no cadastro do Tipo de atendimento.

## **04. DEMAIS INFORMAÇÕES**

Para incluir uma imagem neste campo, orientamos usar TAG HTML de Imagem <img>, adicionando uma imagem com URL pública ou vincular uma imagem seguindo o padrão Data URI Scheme (<https://en.wikipedia.org/wiki/Data_URI_scheme#Syntax>).  
A imagem pode ser convertida para Base64 (opção de conversão online <https://base64.guru/converter/encode/image>).

**Para converter a imagem:**

**4.1)**Carregar a imagem no campo: Local file

**4.2)**Clicar no botão: "Encode imagem to Base"

**4.3)**Após clicar no botão, irá gerar a string da imagem. Clicar no link: Copy, para copiar a estrutura.

**4.2)**Acessar o CRM (Gestão de relacionamento com o cliente) | WorkFlow | Tipos de Atendimento | Tipos. Editar o tipo de atendimento e colar a estrutura string da imagem convertida.
