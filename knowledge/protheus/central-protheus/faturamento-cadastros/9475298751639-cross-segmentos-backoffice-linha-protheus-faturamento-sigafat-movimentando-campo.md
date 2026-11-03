---
article_id: 9475298751639
category: Faturamento - Cadastros
content_hash: d490b771ddeef62c77174c2ae6541a527f9b8521141b5625890c1bd2effd8102
fetched_at: '2026-06-28T22:38:36.668434+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Movimentando
  campos no Cadastro de Clientes (SA1)
type: support-article
updated_at: '2022-10-21T10:49:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9475298751639-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Movimentando-campos-no-Cadastro-de-Clientes-SA1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como movimentar os campos para onde desejo visualizá-los na rotina Cadastro de Clientes?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões  
  
**Solução**

Há 3 formas de disponibilizar os campos no cadastro de clientes:

Exemplo 1 - Feito para movimentar entre as abas da rotina

Exemplo 2 - Feito para movimentar entre as divisões/segmentos dentro de abas da rotina

Exemplo 3 - Feito para movimentar a ordem de aparecimento do campo dentro do segmento

**1 - Movimentar campos entre abas** **(****Cadastrais  |  Adm/Fin.  |  Fiscais  |  Vendas  |  Outros****)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474077292951)**

**Caminho para alteração:** Ambiente Configurador (SIGACFG) -> Base de Dados -> Dicionário -> Bases de Dados -> Empresa -> Dicionário de Dados -> Procurar Tabela 'SA1' e posicionar sobre:

**Editar -> [1] Opção "Pastas" -> [2] Botão "Mover campo"**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474138849943)

Faça as alterações necessárias de acordo com a descrição:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474143870871)

**1.1 -** Campo "Pasta:": Selecione nesse campo **em qual aba** está o **campo que será movimentado** entre as abas.

**1.2 -** Marque todos os campos **que deseja mudar de aba**

**1.3 -** Campo "Mover para:": Selecione nesse campo **qual aba será movido** os campos selecionados no passo 2

**2 - Movimentar campos entre segmentos** **(Dados cadastrais  |  Endereços Complementares  |  Dados Financeiros  |  Dados Contabéis  |  Dados Fiscais  |  Vendas  |  Segmentos  |  Outros)**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474444133271)

**Caminho para alteração:** Ambiente Configurador (SIGACFG) -> Base de Dados -> Dicionário -> Bases de Dados -> Empresa -> Dicionário de Dados -> Procurar Tabela 'SA1' e posicionar sobre:

**Editar -> [1] Opção "Agrupamentos" -> [2] Botão "Mover campo"**

Faça as alterações necessárias de acordo com a descrição:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474471267223)

**2.1 -** Campo "Agrupamento:": Selecione nesse campo **em qual segmento** está o **campo que será movimentado** entre os segmentos.

**2.2 -** Marque todos os campos **que deseja mudar de agrupamento**

**2.3 -** Campo "Mover para:": Selecione nesse campo **qual segmento será movido** os campos selecionados no passo 2

**OBS:** Caso a aba em que o campo será movido não tenha o segmento escolhido será criado naquela aba.

**3 - Movimentar campos entre posições** **(![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474944364183))**

**![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474932427671)**

**Caminho para alteração:** Ambiente Configurador (SIGACFG) -> Base de Dados -> Dicionário -> Bases de Dados -> Empresa -> Dicionário de Dados -> Procurar Tabela 'SA1' e posicionar sobre:

**Editar -> Campos**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9474987862039)**

1 - De dois cliques no ![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9475016457239) caso queira que o campo vá para cima na visualização da rotina

2 - De dois cliques no ![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9475036241559) caso queira que o campo vá para baixo na visualização da rotina

**OBS1:** Essa mudança será refletida dentro do segmento/divisão dentro da aba da rotina, colocar em posições muito altas não significa mudar o campo de segmento/aba, por exemplo, ser o primeiro campo na aba "Dados Cadastrais". Caso o campo não esteja nessa aba/segmento ele não irá ser o primeiro nessa parte.

**O campo será o primeiro dentro de seu segmento.**

**OBS2:** Campos com círculo vermelho não podem mudar de posição, são travados naquela ordem. Os campos com círculo verde pulam a posição do registro que tem círculo vermelho na disposição dos campos.
