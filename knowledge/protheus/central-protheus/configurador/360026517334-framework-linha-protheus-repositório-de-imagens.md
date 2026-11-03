---
article_id: 360026517334
category: Configurador
content_hash: b63f7b2f6dc88d1d83cde3919894683c85a6bc8d5c80d68d2a99ab2100f9225d
fetched_at: '2026-06-28T22:42:19.249386+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Repositório de Imagens
type: support-article
updated_at: '2024-05-14T11:12:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026517334-Framework-Linha-Protheus-Reposit%C3%B3rio-de-Imagens
---

**Dúvida**  
Como fazer a configuração do Repositório de Imagens no Protheus?  
  
**Ambiente**  
Protheus - Configurador - A partir da versão 12  
  
**Solução**  
Existe uma configuração que possibilita a classificação das imagens por **Alias** ou por **Todas as tabelas**, e permite a parametrização do tipo de armazenamento (Banco de Dados).  
Com o vínculo da imagem com uma tabela do Protheus, é possível apresentar a imagem somente para cadastros do Protheus que utilizem a tabela.  
Quando o usuário estiver cadastrando um produto e for adicionar a foto do mesmo, o repositório é apresentado com as imagens relacionadas à tabela SB1, facilitando a seleção da imagem relacionada ao produto. Sendo assim, quando for cadastrar um usuário, as imagens não serão exibidas, pois estão vinculadas à SB1. O que irá definir é a forma que o parâmetro MV\_REPOSIT esta configurado, conforme informação abaixo.  
  
O parâmetro apenas irá servir para segmentar a utilização das imagens em cada módulo.  
  
**MV\_REPOSIT=1** - Tratamento de forma genérica, ou seja, independente de qual Módulo o usuário acessou o Cadastro de Produto, etc , e realizou a inclusão da imagem, o mesmo será apresentado também em qualquer módulo que tiver a mesma rotina para acesso.  
  
**MV\_REPOSIT=2** - Tratamento de forma Individual, ou seja, se o usuário cadastrou uma imagem no Cadastro de Produto pelo Módulo Estoque/Custo, a imagem só será exibida no Módulo Estoque/Custo.  
  
- As imagens são gravadas dentro da tabela PROTHEUS\_REPOSIT no Banco de Dados.  
- Existem alguns nomes que são reservados pelo sistema. Se tentar usar um desses nomes, o sistema irá apontar um erro, e não permitirá a inclusão da imagem com este nome. Neste caso, recomendamos a troca do nome da imagem.
