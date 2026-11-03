---
article_id: 360004815932
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 8cc36661cf525a4b5d50640c0bf915aa0d6516489c79a0fa48c2b781ddfaab65
fetched_at: '2026-06-28T22:39:07.860081+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como incluo imagem
  no Cadastro de Produtos?
type: support-article
updated_at: '2025-05-16T13:55:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004815932-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-incluo-imagem-no-Cadastro-de-Produtos
---

**Dúvida**Como incluo imagem no **Cadastro de Produtos (MATA010)**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Primeiramente inclua a imagem no banco de imagens do**Microsiga Protheus**.

Para isso, efetue os procedimentos abaixo:

* Acesse a rotina**Repositório de Imagens**, no ambiente **Configurador** > **Cadastros** > **Reposit. Imagens**;
* Pela opção **Incluir**, selecione o diretório no qual a imagem se encontra e selecione a imagem para inclusão;
* Confirme a inclusão da imagem;
* Acesse a rotina**Cadastros de Produtos** e na inclusão ou alteração de um produto, acesse pela aba **Atendimento**, o botão **Imagem**, para selecionar aquela já incluída no repositório de imagens e vincule-a ao produto escolhido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000624042)

**Observações**:

- Somente imagens com tamanho máximo de 1MB são suportadas;

- Quando o parâmetro MV\_REPOSIT é acionado, os arquivos SIGAADV permanecem intactos, não são alterados;

- Ao trocar o repositório de imagens dos arquivos locais para o banco de dados, as imagens permanecem no arquivo SIGAADV.BMD. Os arquivos somente são copiados para o banco de dados ao utilizar a rotina de Importação;

- As imagens são gravadas dentro da tabela PROTHEUS\_REPOSIT no Banco de Dados;

- No padrão, não é possível incluir uma Imagem sem que ela esteja previamente vinculada no repositório de imagens do Configurador.

- Somente formato BMP ou JPG

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18083263804951)

- Qual a resolução indicada para a imagem? (a melhor que se adequa a sua necessidade)

[Framework - Linha Protheus - Repositório de Imagens](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026517334-Framework-Linha-Protheus-Reposit%C3%B3rio-de-Imagens)

Para saber mais sobre o tamanho padrão da imagem no cadastro de produto acesse nossa documentação:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual o tamanho de imagem padrão para o Cadastro do Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410823845271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-tamanho-de-imagem-padr%C3%A3o-para-o-Cadastro-do-Produto?source=search)

**Saiba mais:**

*[MP - FRAME - Repositório de Imagens](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026517334-MP-FRAME-Reposit%C3%B3rio-de-Imagens)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
