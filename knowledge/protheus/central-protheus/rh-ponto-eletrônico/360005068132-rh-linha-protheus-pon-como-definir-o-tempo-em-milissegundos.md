---
article_id: 360005068132
category: RH - Ponto Eletrônico
content_hash: 15b4e41cd55c08126f928d07e9f7b0fba50a15181281192c5f9c6f8c98e67ced
fetched_at: '2026-06-28T22:44:58.259044+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON -  Como definir o tempo em milissegundos
type: support-article
updated_at: '2021-09-09T20:22:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005068132-RH-Linha-Protheus-PON-Como-definir-o-tempo-em-milissegundos
---

**Dúvida**Como definir o tempo em milissegundos através do parâmetro MV\_P340ATU?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Criação do parâmetro **MV\_P340ATU**, que permite definir o **tempo em milissegundos**, utilizado para atualização automática da tela.  
  
No Ponto Eletrônico acesse Atualização > Cadastro de Visitantes > **Visitas**. A tela será atualizada automaticamente de acordo com o valor informado no parâmetro MV\_P340ATU:

|  |  |
| --- | --- |
| **Nome da Variável** | MV\_P340ATU |
| **Tipo** | N |
| **Descrição** | Informe a quantidade de milissegundos que será utilizado para atualização automática do cadastro de visitas. |
| **Valor Padrão** | 5000 |

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408181556759/mceclip0.png)**
