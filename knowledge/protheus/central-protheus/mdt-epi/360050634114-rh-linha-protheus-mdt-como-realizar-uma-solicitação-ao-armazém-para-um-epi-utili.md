---
article_id: 360050634114
category: MDT - EPI
content_hash: d79a3d7ea252533df268999a1791f1393238822c5755583719e9530f164a3188
fetched_at: '2026-06-28T22:44:25.402537+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Como realizar uma solicitação ao armazém para um  EPI
  utilizando Indicador de Produto tabela (SBZ)
type: support-article
updated_at: '2024-11-05T10:51:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634114-RH-Linha-Protheus-MDT-Como-realizar-uma-solicita%C3%A7%C3%A3o-ao-armaz%C3%A9m-para-um-EPI-utilizando-Indicador-de-Produto-tabela-SBZ
---

**Dúvida**Como realizar uma entrega de EPI usando Indicador de Produto tabela (SBZ)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para realizar a configuração acesse o Ambiente Configurador **(SIGACFG)**, no seguinte caminho: Atualizações > Cadastro > Parâmetros > Ative os parâmetros conforme modelo abaixo:  
 **MV\_ARQPRO** =**SBZ**: O sistema utiliza os campos da tabela de Indicadores de Produtos (SBZ).  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077874114)****MV\_NGMDTES=**Integração do Medicina e Segurança do Trabalho com o Estoque. Conteúdo deve ser S=Sim ou N=Não.    
 **![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077874194)  
  
MV\_NG2SA=**Indica se gera solicitação ao armazém ao invés de baixar do estoque. Conteúdo deve ser S=Sim ou N=Não.  
 **![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079020873)**  
Deverá realizar o cadastro do produto EPI, para maiores informações de como cadastrar acesse  
[MP - MDT - Como cadastrar um produto com o tipo EPI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048704353/)  
Após o cadastro do EPI deverá cadastrar o Indicado do Produto, para isto acesso o Módulo 04 **(SIGAEST)**, no seguinte caminho: Atualizações > Cadastro > Produto > Indicadores.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077874574)  
  
Clique em incluir e selecione o produto EPI cadastrado anteriormente.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079021193)  
  
Realize o cadastro conforme necessidade da empresa e no campo Armazém Padrão aponte o registro relacionado ao cadastro. Feito isto salve.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077874714)  
  
Observe que no cadastro do Produto EPI esta relacionado a um código diferente de armazém.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079021553)  
  
Conforme a configuração do parâmetro **MV\_ARQPRO**, ao realizar uma solicitação de entrega de EPI deverá olhar para o armazém do Indicador do Produto tabela **RBZ**.  
  
Para realizar a entrega acesse Módulo 35 **(SIGAMDT)**, no seguinte caminho: Atualizações > EPI > Funcionário x Epi **(MDTA695)**, clique em EPI´s > selecione o EPI relacionado ao Indicador de produto > Observe o campo Armazém será preenchido conforme cadastro do Indicador de produtos.  
 **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079038493)  
  
Saiba Mas**[Central de artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)
