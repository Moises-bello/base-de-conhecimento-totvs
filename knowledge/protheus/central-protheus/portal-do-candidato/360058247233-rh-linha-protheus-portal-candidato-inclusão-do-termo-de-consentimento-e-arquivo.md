---
article_id: 360058247233
category: Portal do Candidato
content_hash: 7dac5861d123b933193559754a50c775714c97c1a3c8b645e60dfd5a60e50fc6
fetched_at: '2026-06-28T22:42:57.885578+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - Inclusão do Termo de Consentimento
  e Arquivo Modelo
type: support-article
updated_at: '2022-04-05T19:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058247233-RH-Linha-Protheus-PORTAL-CANDIDATO-Inclus%C3%A3o-do-Termo-de-Consentimento-e-Arquivo-Modelo
---

**Dúvida**Como realizar a inclusão do Termo de Consentimento na rotina Gerenciamento dos modelos de termo e aceites de consentimento **(GPEA940)** Versionamento de Consentimento, como incluir o termo? Como salvar o Modelo, exemplo de utilização e configuração.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal do Candidato – Todas as versões  
  
**Solução  
Visão Geral** - Implementação da rotina de Gerenciamento dos Termos de Consentimento **(GPEA940)** para inclusão, alteração, visualização e exclusão dos termos de consentimento. A rotina armazenará as datas e horas de início/fim de vigência dos termos e os detalhes do modelo. Não será permitida a alteração de modelos vigentes ou com aceites vinculados.  
  
Não será possível excluir modelos de termos de consentimento que estejam vinculados a aceites dos usuários. A data máxima de aceite do termo deverá ser no máximo igual a data + hora final - 1 minuto. Um período de vigência de modelo de termo de consentimento não poderá intercalar com os demais períodos cadastrados.  
  
Para realizar o seu cadastro é necessário ter criado a opção do Menu  Gerenciamento dos Termos de Consentimento **(GPEA940)**, caso ainda não tenha sido criada em seu ambiente [**Clique Aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056374334).  
**1.** Será necessário definir alguns parâmetros de configuração, para correto direcionamento do diretório do termo. Antes de definir o  campo **Arquivo\*,** importante configurar os parâmetros abaixo:  
  
O parâmetro **MV\_DIRCONS** deve informar qual o diretório **(subpasta da pasta WEB do portal)** na qual os modelos de termo de consentimento serão salvos.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101301214/mceclip0.png)  
 **Observação**: caso o Server do ERP seja distinto do Server do Portal, deve-se utilizar o parâmetro **MV\_DIRTERM**.   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002414342/mceclip1.png)  
  
**2.** Para inclusão de novo termo e arquivo modelo acesse: Módulo 07 **(SIGAGPE)**, no seguinte caminho: **Atualizações > Miscelânea > Portal Protheus > Ger. Termo de Consentimento.**Clique em Incluir e defina as informações de seu termo, conforme exemplo abaixo.  
  
![E4rEuBImJj.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002456721/E4rEuBImJj.gif)  
  
Para configurar corretamente sua extensão para exibição do termo não deixe de acessar o link abaixo.  
[Qual extensão é necessária ter no navegador para visualizar o Termo de Consentimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5228044897815)  
Informações complementares sobre o termo de consentimento **[aqui](https://tdn.totvs.com/display/public/PROT/Gerenciamento+dos+modelos+de+termo+e+aceites+de+consentimento)  
  
Dica:**Importante apontar corretamente na Seção HTTP do appserver.ini o caminho até a pasta WEB conforme exemplo abaixo. 

**![](https://totvssuporte.zendesk.com/attachments/token/G1YGXJBkBUUfwxPr6dFYbbKrR/?name=inline-298050887.png)  
  
3.** Ao acesse o Portal do Candidato, na inclusão de um currículo será apresentado o Termo cadastrado.  
  
![](https://tdn.totvs.com/download/attachments/562470439/image2020-9-11_18-24-59.png?version=1&modificationDate=1599859499883&api=v2)  
  
O candidato deverá clicar na opção Aceite.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095702974/mceclip2.png)  
  
Mensagem apresentada ao candidato após o aceite do termo de consentimento.  
  
![](https://tdn.totvs.com/download/attachments/562470439/image2020-9-11_18-25-33.png?version=1&modificationDate=1599859534147&api=v2)  
  
Mensagem apresentada ao candidato quando o mesmo não aceita os termos de consentimento.  
  
![](https://tdn.totvs.com/download/attachments/562470439/image2020-9-11_18-28-13.png?version=1&modificationDate=1599859693633&api=v2)

**Saiba Mais**[Artigos Portal do Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0%20%C2%A0)[Atualizações para adequação Lei Geral de Proteção de Dados (LGPD)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054147634)
