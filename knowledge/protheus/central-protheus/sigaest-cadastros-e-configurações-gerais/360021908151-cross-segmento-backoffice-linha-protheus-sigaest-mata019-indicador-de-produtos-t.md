---
article_id: 360021908151
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 25db1f3964e053406781f92a2e8dfb9d66c81927e4a1d5e96154d4182b66448a
fetched_at: '2026-06-28T22:39:07.929402+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA019 - Indicador
  de Produtos, tabela SBZ e parâmetro MV_ARQPROD
type: support-article
updated_at: '2025-08-04T18:05:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021908151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA019-Indicador-de-Produtos-tabela-SBZ-e-par%C3%A2metro-MV-ARQPROD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30283672645911) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Qual a utilidade da rotina de **Indicador de Produtos (MATA019)** e qual a relação com o parâmetro MV\_ARQPROD com esta rotina?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
O *Protheus* permite a utilização do Cadastro de Produtos (SB1) de forma compartilhada, porém, determinadas características dos produtos podem ser exclusivas por filial para alguns registros da SB1. Para atender esta peculiaridade existe o a rotina de Cadastro de Indicadores de Produtos (MATA019) que permite tratar  determinadas características de cada produto de forma exclusiva para cada filial. Quando cadastramos um Indicador (campo da SB1) de um produto, estas características são gravadas na tabela SBZ.

**O que é necessário para o correto uso desta rotina?**

Para o uso desta rotina, é importante que o parâmetro **MV\_ARQPROD** (que basicamente permite ao usuário escolher se os dados de indicadores de produtos serão considerados pela tabela **"SB1" ou "SBZ"**) esteja habilitado. Normalmente é configurado com conteúdo SBZ justamente para, nas rotinas que checam este parâmetro, o Sistema sempre buscar os dados do Indicador de Produtos (SBZ) primeiramente. Só em caso de não existência do registro dos campos da SBZ para uma filial, ele buscará os mesmos pela SB1.

***Observação Importante*****:** O parâmetro MV\_ARQPROD ***não deve*** **ser criado exclusivo para cada Filial**, no padrão esse parâmetro deve ser Compartilhado para todas as Filiais. Ou seja, no parâmetro o **campo Filial deve manter em Branco** como no exemplo do print abaixo.

![MV_ARQPROD.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/29471458283927)

**Exemplo prático do uso da rotina Indicadores de Produtos usando o campo "****Armazém Padrão****" (B1\_LOCPAD)**

Usaremos um produto (PA23) para exemplificar a utilidade desta rotina. Este produto, na Filial batizada "Matriz", foi cadastrado com Armazém Padrão 01 (B1\_LOCPAD = 01). Porém, na "Filial 02", o Armazém Padrão (BZ\_LOCPAD) dele será o 50. Veja:

![Cadastro_Produto_e_Indicador_do_Produto.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406680794903)

Com isso, perceba que na tabela SB1 (Dados Cadastrais de Produto), teremos o nosso PA23 com Armazém Padrão 01, enquanto na tabela SBZ (Indicador de Produtos), teremos com o Armazém Padrão 50.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406681172119)

Obs: O campo de Filial na SB1 está em branco por ser compartilhado (premissa básica para uso do Indicador de Produtos).

**1° Caso de Teste - Inclusão de Documento de Entrada do PA23 na Filial 01 (Matriz)**

Com isso, vamos incluir um Documento de Entrada com o nosso produto. É importante lembrarmos que **só configuramos Indicador de Produto do PA23 para a Filial 02**. Logo, na Filial 01, ele não encontrará registro deste produto da SBZ, então, restará puxar da SB1, onde o Armazém configurado é o 01.

![Doc_de_Entrada_filial_01.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406681338391)

**2° Caso de Teste - Inclusão de Documento de Entrada do PA23 na Filial 02**

Agora vamos incluir o Documento de Entrada selecionando a Filial 02. Da mesma forma, como configuramos o parâmetro **MV\_ARQPROD = SBZ**, ele primeiramente irá checar nesta tabela se há registro para o produto PA23 na Filial 02. Desta vez irá encontrar e atribuir o Armazém 50. Veja:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406681442199)

![Doc_de_entrada_na_filial_02.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4406672695959)

Portanto, todas as rotinas que por padrão buscam registros da tabela SB1 (Cadastro de Produtos) e validam o parâmetro MV\_ARQPROD, passarão a checar primeiramente a tabela SBZ (Indicador de Produtos). Portanto, o funcionamento de todas as rotinas são idênticas ao funcionamento normal, exceto as que passam a considerar as informações contidas no Cadastro de Indicadores de Produtos (SBZ), considerando o parâmetro MV\_ARQPROD.

**Todo e qualquer processo de implantação ou mudança para uso, deve-se avaliar juntamente de um consultor especialista em estoque custos, para validação da regra de negócios, visando uma configuração do inidicador de forma funcional.**

**Observação:** A checagem pela SBZ se dá por todo o registro, e não unicamente no campo configurado, isto é, deve-se considerar, no cadastramento do Indicador, não só o campo que tem o valor diferente (especifico), mas também os que tem o valor igual, pois o fonte vai olhar todo o registro, e não somente o campo com valor específico.

**O controle via SBZ funciona para o conceito de rastreabilidade?**

**Não**, o controle de RASTRO é exclusivamente com o uso da SB1, o controle de rastro não tem funcionalidade para o processo com **MV\_ARQPROD**.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*SIGAEST - Campo BZ\_TIPO qual o conceito e utilização ao incluir na tabela SBZ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29453306467351-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Campo-BZ-TIPO-qual-o-conceito-e-utiliza%C3%A7%C3%A3o-ao-incluir-na-tabela-SBZ)
