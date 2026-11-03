---
article_id: 4407153055767
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: cda4e70b59fe02d5086222f0a3805a4eece35f42993f896c158c24268570295b
fetched_at: '2026-06-28T22:39:07.914317+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como cadastrar
  um produto no Protheus?
type: support-article
updated_at: '2026-03-12T17:31:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407153055767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-cadastrar-um-produto-no-Protheus
---

O artigo explica como cadastrar um produto no Protheus via rotina MATA010, acessível pelo módulo Estoque/Custos. Para cadastro simples, são obrigatórios código, descrição, tipo, unidade e armazém padrão. Produtos com código iniciando por "MOD" são restritos para mão de obra. A ordenação dos produtos pode ser feita por código ou descrição clicando na seta da coluna. A formatação de letras maiúsculas ou minúsculas é controlada pela máscara X3\_PICTURE no dicionário SX3.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28806770578071)** Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Como eu cadastro um produto novo no Protheus?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Neste artigo explicaremos como Cadastrar um Produto no Protheus.

**Acessando à rotina de Cadastro de Produtos (MATA010)**

Acessar ao módulo 04 - Estoque/Custos e seguir o caminho:  **Atualizações -> Cadastro -> Produto**

Outra forma de acessar é pelo código da rotina, pesquisando na barra de buscar abaixo do nome do módulo. O código desta rotina é **MATA010**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407151925527)

**Acessando à tela do Cadastro**

Assim que acessar à rotina, aparecerão (se houver cadastros feitos) os produtos já criados no ambiente. Para criarmos um novo, basta clicar em "Incluir":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407151952791)

**Preenchendo os dados básicos do Produto**

Ao acessar à rotina, esta é a tela de cadastro. É a rotina de mais campos para cadastros, porém, para um simples cadastros são obrigatórios os preenchimentos apenas dos seguintes campos:

- Código (B1\_COD) = Define o código do produto;

- Descrição (B1\_DESC) = Define a descrição do produto;

- Tipo (B1\_TIPO) = Define o tipo do produto (Matéria Prima, Embalagem, Produto Acabado, etc.);

- Unidade (B1\_UM) = Define a unidade de medida (Kilo, Unidade, Galão, Lata, Litro, etc.);

- Armazém Padrão (B1\_LOCPAD) = Define o local de estoque padrão onde o produto será armazenado ou que sairá no momento da venda ou movimento de saída.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407151989527)

Com isso, o produto tem seu cadastro efetivado. Para fazer movimentos de saída, será necessário um cadastro prévio de Saldo Inicial para o mesmo (via rotina MATA220), onde é delegado o saldo físico e financeiro inicial do produto para o armazém desejado. Porém, para Documentos de Entrada, basta ter o cadastro do produto para começar a utilizá-lo.

Lembrando que o Cadastro de Produto tem muitas opcionais onde pode-se mudar totalmente o dinamismo e usabilidade do produto, como por exemplo controle de [**Lote e Endereçamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-MP-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus). Então é importante atentar-se ao help dos campos (selecionando o campo e apertando o botão F1 do teclado) para entender qual função prática de cada campo do Cadastro do Produto.

**Existe restrição para uso da sigla MOD no codigo de produto?**

Sim, esse campo é reservado para sigla inicial com MOD, para tratativa de produtos "Mão de Obra", é uma validação legado e padrão do sistema, e não há remoção dessa validação.

No caso você não pode ter codigos de produtos, que venham a iniciar com "MOD", por exemplo: Sua empresa trabalha com modelos, e seus produtos seriam configurados como "MOD-001, MODELO001" etc, isso não podera ser realizado, pois a Sigla INICIAL = MOD é restrita para uso dos produtos Mão de obra.

Caso tentar cadastrar com essa silga, recebera a seguinte informação:

***Problema:** O Cadastro de Mão de Obra é feito com "MOD" + o código do Centro de Custos. O Centro de Custos digitado não foi encontrado.*  
***Solução:** Digite um Centro de Custos existente ou cadastre o Centro de Custos desejado.*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/28660412071447)*

Saiba mais sobre oque é produto mão de obra aqui:

<https://tdn.totvs.com/x/z6hEGQ>

**Como ordenar os produtos por código ou descrição?**

Para ordenar a exibição dos produtos por código, descrição ou por qualquer outra coluna, basta clicar no ícone da seta logo à esquerda do nome da coluna. No exemplo abaixo, perceba que o primeiro produto listado é de código PA28. Ao clicar, o Sistema ordenará de forma que puxará primeiro os números para depois os códigos iniciados por letras (em ordem alfabética). O mesmo acontece ao ordenar pela descrição, desta forma, como só temos produtos com descrição de texto, ele ordena alfabeticamente:

![Ordem_dos_codigos_produto.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4408089921815)

**Como funciona a definição de letras maiúsculas ou minúsculas em um campo no Protheus?**

No Protheus, a definição se um campo aceita **letras maiúsculas ou minúsculas** é controlada pela propriedade **X3\_PICTURE** da tabela **SX3**, que corresponde ao dicionário de dados dos campos do sistema.

O **PICTURE** funciona como uma máscara de formatação, determinando o padrão de preenchimento que o campo deverá seguir.

Por exemplo:

`!@`

Onde:

* `!` → define que o conteúdo será convertido para **letras maiúsculas**
* `@` → indica que todos os caracteres digitados no campo seguirão essa formatação

Quando essa máscara está configurada, o sistema automaticamente converte o conteúdo para maiúsculo, pois esse é o comportamento padrão definido no dicionário de dados do Protheus.

Caso seja necessário permitir a **diferenciação entre letras maiúsculas e minúsculas**, será necessário avaliar junto com um consultor Analista in loco para verificar a possibilidade de alteração na mascara do campo na base de dados.

Para mais informações sobre a máscara do campo acesse:

[Máscaras para campos](https://tdn.totvs.com/pages/releaseview.action?pageId=469450707)

[SX3 - Campos das tabelas](https://tdn.totvs.com/display/public/framework/SX3+-+Campos+das+tabelas)

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)
