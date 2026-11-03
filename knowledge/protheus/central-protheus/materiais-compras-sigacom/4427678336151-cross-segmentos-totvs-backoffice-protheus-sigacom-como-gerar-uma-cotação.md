---
article_id: 4427678336151
category: Materiais - Compras (SIGACOM)
content_hash: 5ca4e27ecd3bceb863eb34b560c70d6798e8731ed5fdfede8f472f942722d33d
fetched_at: '2026-06-28T22:41:15.897721+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gerar uma cotação?
type: support-article
updated_at: '2024-03-13T14:02:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427678336151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-uma-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **5 min****Dúvida**Exemplo para gerar uma cotação.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**  
Passo a passo para Gerar a cotação (exemplo):

1 - Acessar via módulo de Compras a rotina de Solicitação de Compras (**MATA110**):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427565857047/mceclip0.png)

2 - Em seguida acessara rotina Gerar Cotação (**MATA131**):

Ao acessar a rotina de cotação o sistema pode apresentar a tela abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427568520727/mceclip1.png)

Caso não haja necessidade de utilização é possível clicar em cancelar.

*Para desativar a exibição da tela acima, preencha o conteúdo do parâmetro* **MV\_COTFILT = .F.**

Em seguida informe a parametrização conforme necessidade.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427586768663/mceclip2.png)

Após preenchimento selecione a Solicitação de Compras e clique em Gerar Cotação:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427580522519/mceclip3.png)

Nesse momento o sistema consulta validação do parâmetro **MV\_SELFOR** para prosseguir, se estiver desabilitado após clicar em **'Gerar Cotação'** a informação é direcionada para Atualização da Cotação (**MATA150**).

A demonstração a seguir será com o parâmetro **MV\_SELFOR=****S**ou seja habilitado.

***Vantagens do parâmetro MV\_SELFOR***

* *Com o parâmetro **MV\_SELFOR** igual a **S** é possível visualizar a disposição dos produtos que fazem parte da cotação conforme o grupo de produto.*
* *É permitido a inclusão de fornecedor participante para a cotação sem a necessidade de cadastrá-lo previamente na rotina de Fornecedores. Para mais detalhes [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=336397076).*
* *Há disponível o botão com funcionalidade para replicar os Fornecedores para o Grupo de Produtos ou para Todos os grupos.*

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427581305623/mceclip4.png)

Após revisar as informações sobre a Cotação clique em Confirmar.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427581868951/mceclip5.png)

Se ao acessar esta rotina, o comprador configurou o parâmetro Imprime Cotações como Sim, após confirmar a geração da cotação, o sistema apresenta uma nova janela para a impressão das cotações geradas.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427600222487/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427592085911/mceclip7.png)

3 - Em seguida acessara rotina Atualiza Cotação (**MATA150**)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427608684183/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427593177367/mceclip9.png)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427610068759/mceclip10.png)

4 - Em seguida acessara rotina Analisa Cotação (**MATA161**)

*Obs.: O sistema valida a marcação da proposta vencedora com base no **F12**da rotina*

*![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427595437847/mceclip11.png)*

*![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427595952023/mceclip12.png)*

*4 - Em seguida acessar rotina Pedido de compras (**MATA120**)*

*![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4427605483927/mceclip13.png)*

**Importante:**

Apesar *da  cotação poder ser composta por mais de um fornecedor / mais de um produto, uma vez que um registro de cotação é editado por um usuário, a tabela SC8 de cotação é lockada ( Selecionada a tabela do  processo), o registro é liberado para edição por outro usuário apenas após liberação do lock (após liberação do primeiro usuário) este comportamento é notado em diversas rotinas/ tabelas do ERP como medida de segurança.*

***Saiba Mais Processo em cada rotina:***

Gerar cotação: [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como Gerar Cotação ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417420194455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Como-Gerar-Cota%C3%A7%C3%A3o-)

Atualizar cotação: [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como incluir Novo participante na Cotação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417441454103)

**Pontos de entrada:**

Gerar cotação:

[MP - SIGACOM - Pontos de Entrada disponíveis na rotina Gera Cotação - MATA131](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001417762-MP-SIGACOM-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Gera-Cota%C3%A7%C3%A3o-MATA131)

Atualizar cotação:

[Cross Segmento - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada na rotina de Atualiza Cotações ( MATA150 )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028037612-Cross-Segmento-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-na-rotina-de-Atualiza-Cota%C3%A7%C3%B5es-MATA150-)

Analise de cotação:

[MP - SIGACOM - Pontos de Entrada para Análise de Cotação (MATA161)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026227233-MP-SIGACOM-Pontos-de-Entrada-para-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-MATA161-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
