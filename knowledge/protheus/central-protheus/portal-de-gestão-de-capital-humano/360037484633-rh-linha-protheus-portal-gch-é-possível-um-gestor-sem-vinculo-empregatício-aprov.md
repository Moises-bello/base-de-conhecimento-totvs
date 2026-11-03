---
article_id: 360037484633
category: Portal de Gestão de Capital Humano
content_hash: f99e324a768fdac42d36c1c0c8bdbd4da9c1c4819237b9714235eff75929bdfa
fetched_at: '2026-06-28T22:43:00.044081+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: 'RH - Linha Protheus - PORTAL GCH - É possível um gestor sem vinculo empregatício
  aprovar solicitações via portal para funcionários de filiais diferentes ? '
type: support-article
updated_at: '2021-04-07T12:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037484633-RH-Linha-Protheus-PORTAL-GCH-%C3%89-poss%C3%ADvel-um-gestor-sem-vinculo-empregat%C3%ADcio-aprovar-solicita%C3%A7%C3%B5es-via-portal-para-funcion%C3%A1rios-de-filiais-diferentes
---

**Dúvida** É possível um gestor sem vinculo empregatício aprovar solicitações via portal para funcionários de filiais diferentes ?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Sim, é possível, para isso a tabela SQB deve estar compartilhada e no SIGAGPE o gestor deve estar amarrado aos departamentos.

Para solucionar essa dúvida, realize os seguintes passos:

**1**. A tabela SQB deve estar compartilhada para filiais:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049287373/mceclip0.png)  
**2.** O gestor sem vinculo deve ser cadastrado como Autônomo/Contribuinte Individual:

Ex: Gestor - Matricula 900000 - Matriz

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049287493/mceclip1.png)  
3. O gestor deve ser informado como Matricula Responsável no cadastro dos departamentos:

Ex:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Filial** | **Matricula** | **Funcionário** | **Departamento** | **Matric Responsável** |
| Matriz | 15 | Carin Teste | 000001014 | 900000 |
| Filial 01 | 31 | Ricardo PLR | 000001017 | 900000 |
| Filial 02 | 40 | Jorge | 000001015 | 900000 |

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048398154/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048398694/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049288233/mceclip4.png)

4. O funcionário fará a solicitação via Portal Gestão de Capital Humano:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049288413/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049288493/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049288513/mceclip7.png)

5. O Gestor fará a aprovação das solicitação via Portal:

Para isso deverá acessar Solicitações -> Acompanhamento: Clicar no código e aprovar.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049288553/mceclip8.png)
