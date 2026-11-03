---
content_hash: b9e2ddeb36fc36a3e5f4475d32edfe7611a9594ce3b6a42124ed7f1ae87df547
fetched_at: '2026-06-29T00:10:19.356247+00:00'
page_id: '4813484'
product: rm
source: tdn-rm
title: Sentença SQL - Informações do item de movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813484
version: 5
---

BLOCK

Sentença SQL - Informações do item de movimento

FAQ: **Sentença SQL - Informações do item de movimento**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Avaliação

***Como Fazer***

Como buscar informações pertinentes aos Itens de Movimento, sem a necessidade de editá-los, um a um?

***Definição do Processo***

Tem por finalidade a criação de uma Consulta SQL, associando esta Consulta como Anexo da visão de Movimentos, permitindo a apresentação de dados específicos dos Itens de Movimento, sem a necessidade da edição do Movimento.

Solução

***Parametrizações Necessárias***

- Não se aplica

***Descrição do Processo***

Criar uma consulta SQL com a finalidade de retornar dados dos itens e configurar a sentença para utilizá-la na visão de movimentos.

***Criação da Consulta SQL***

Acessar Menu Utilitários | Consultas SQL:

- Incluir uma nova Consulta SQL, com o seguinte texto:

SELECT ITEM.NSEQITMMOV AS 'Seq. Item', PRD.NOMEFANTASIA AS 'Nome do Produto',

FAT.CODTB1FAT AS 'Código', FAT.DESCRICAO AS 'Descrição'

FROM TTB1 FAT, TITMMOV ITEM, TMOV MOV, TPRD PRD

WHERE FAT.CODCOLIGADA = ITEM.CODCOLIGADA

AND FAT.CODTB1FAT = ITEM.CODTB1FAT

AND ITEM.CODCOLIGADA = MOV.CODCOLIGADA

AND ITEM.IDMOV = MOV.IDMOV

AND ITEM.IDPRD = PRD.IDPRD

AND MOV.IDMOV =:ID

Importante:

- Esta Consulta SQL pode (e deve) ser adaptada para as necessidades dos Clientes. Para o exemplo demonstrado, esta Consulta retorna as informações da Tabela de Classificação 1 do Item de Movimento.

***Configuração do Anexo da Visão***

Na visão dos Movimentos, acessar Menu Anexos | Consultas SQL | Inserir Consulta SQL:

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJSImhQu0I/AAAAAAAAFEk/ny8XwXyjo_I/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJSIOBBiVI/AAAAAAAAFEg/XukB3mvc9eA/s1600-h/clip_image002%5B1%5D.jpg)

Na tela que se abre, deverá ser selecionada a Consulta SQL criada no primeiro passo:

[![clip_image004](http://lh6.ggpht.com/_G7KXZLoZDsY/TQJSNSWKaQI/AAAAAAAAFE8/o8FBxzNj_vI/clip_image004_thumb%5B1%5D.jpg?imgmax=800 "clip_image004")](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJSJnsD35I/AAAAAAAAFEw/HHTdQ7b-HbM/s1600-h/clip_image004%5B1%5D.jpg)

Na próxima etapa da configuração, deverá ser selecionado o campo da visão que corresponde ao campo da Consulta SQL:

[![clip_image006](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJSQCGB1BI/AAAAAAAAFFI/-ucmkr1Gk8A/clip_image006_thumb%5B5%5D.jpg?imgmax=800 "clip_image006")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJSPs5-blI/AAAAAAAAFFE/ZKB366BcCHk/s1600-h/clip_image006%5B5%5D.jpg)

Após esta configuração, defina o Grupo de Usuários que poderá ter acesso à este Anexo da Visão:

[![clip_image008](http://lh4.ggpht.com/_G7KXZLoZDsY/TQJSRoljwdI/AAAAAAAAFFY/nwrTzQ94N0I/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh5.ggpht.com/_G7KXZLoZDsY/TQJSRCROMUI/AAAAAAAAFFQ/_rtYTgcMcjc/s1600-h/clip_image008%5B1%5D.jpg)

Para verificar o resultado da parametrização, basta concluir o processo e acessar o Anexo criado.

[![a](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJSTvxSK2I/AAAAAAAAFFo/IOzz2_IDpQY/a_thumb%5B1%5D.jpg?imgmax=800 "a")](http://lh3.ggpht.com/_G7KXZLoZDsY/TQJSS2q9ZVI/AAAAAAAAFFg/zo7DTBT6pfc/s1600-h/a%5B1%5D.jpg)

Importante:

- Este recurso se trata de uma ferramenta muito poderosa, já que permite a demonstração de qualquer informação que esteja relacionada a um movimento: Informações sobre Objetos de Manutenção, Informações Financeiras do Cliente/Fornecedor, entre outros fatos específicos do sistema.

- Como se trata da utilização de uma Consulta SQL, é importante deixar a cargo de um Analista especializado a criação desta Consulta, para evitar sobrecargas e lentidão nos sistemas.

- Para um melhor aproveitamento do recurso, tenha em mente as informações desejadas e sua finalidade. Assim se consegue evitar a perda de tempo em obtenção de informações desnecessárias para o seu negócio.
