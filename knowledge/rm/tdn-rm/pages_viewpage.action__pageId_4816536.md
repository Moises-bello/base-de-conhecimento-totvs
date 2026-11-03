---
content_hash: a48c85f9d1b1b40b1c4809cbd7b4932c5b0c9ed016723179a49cd02053303503
fetched_at: '2026-06-29T00:10:19.598116+00:00'
page_id: '4816536'
product: rm
source: tdn-rm
title: Alterando o Numero de Registros da Visão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4816536
version: 5
---

BLOCK

Alterando o Numero de Registros da Visão

FAQ: **Alterando o Numero de Registros da Visão**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | XX.XX |

Solução

|  |
| --- |
| **Produto:** Globais **Versão:** XX.XX |
| **Processo:** Alterando o Numero de Registros da Visão |

|  |  |  |
| --- | --- | --- |
|  | **Introdução**   O documento tem como objetivo orientar o usuário a alterar o número de registros que são exibidos na visão, quando selecionado um filtro, que contém muitos registros e por ventura é retornado à mensagem: “Número de registros (XX registros) desta consulta excede o limite máximo permitido (YY registros). Tente especificar melhor sua consulta”.  Cada tela do aplicativo é denominada como Action e cada Action possui um nome. Neste documento será apresentado o processo de acesso ao cadastro de funcionários. Lembrando que este processo é valido para qualquer aplicativo e qualquer Action.  Ao selecionar um filtro que me traz todos os registros da tabela de funcionários, conforme ilustrado abaixo, a mesma vai exceder o numero de registros que a visão comporta.  [clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TQi9KzcJrOI/AAAAAAAAEwU/WbSgLbxq-W4/s1600-h/clip_image004%5B4%5D.jpg)  [clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TQi9PzAZBII/AAAAAAAAEwc/JN9Sq32hD1A/s1600-h/clip_image002%5B4%5D.jpg) |  |
|  |  |  |
|  | **Desenvolvimento/Procedimento**   1. Notem que ao abrir o cadastro de funcionários, na barra de Status à esquerda é exibido o nome da action (“FopFuncAction”), conforme ilustrado abaixo:  [clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TQi9XJSSqWI/AAAAAAAAEwk/8bVYqf6h1uk/s1600-h/clip_image006%5B4%5D.jpg)   2. Para alterar os registros da visão, deveremos acessar o menu Cadastros / Segurança / Administrativa / Servidores de Aplicação.  [clip_image008](http://lh5.ggpht.com/_G7KXZLoZDsY/TQi9jPMo3sI/AAAAAAAAEws/GUtpbjkH69E/s1600-h/clip_image008%5B4%5D.jpg)  3. Em servidores de Aplicação devemos criar um filtro com a expressão ID do Server IS NOT NULL.  [clip_image010](http://lh4.ggpht.com/_G7KXZLoZDsY/TQi9rmEFptI/AAAAAAAAEw0/JVuYXPQJAro/s1600-h/clip_image010%5B4%5D.jpg) |  |
|  | 4. Configurando o servidor de aplicação  [clip_image012](http://lh6.ggpht.com/_G7KXZLoZDsY/TQi90WI4bjI/AAAAAAAAEw8/3zQtxrxALWs/s1600-h/clip_image012%5B4%5D.jpg) |  |
|  |  |  |
|  |  |  |
|  | 5 – Inserir o numero de registros a serem exibidos na visão  [clip_image013](http://lh3.ggpht.com/_G7KXZLoZDsY/TQi9_Hq68EI/AAAAAAAAExM/U4bkVm81ysA/s1600-h/clip_image013%5B4%5D.jpg) |  |

Feito todo o processo acima, basta acessar novamente o cadastro de funcionários.
