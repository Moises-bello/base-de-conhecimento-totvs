---
article_id: 30456953977495
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 19ccd2fa26411f5600838985e470468fd1d0d5c554fc44963ce4e8e0f78c09fa
fetched_at: '2026-06-28T22:39:09.556370+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 Copiar Produto
  Não Replica Dados para Filial ao Usar SB1 Exclusiva
type: support-article
updated_at: '2025-03-12T12:26:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30456953977495-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Copiar-Produto-N%C3%A3o-Replica-Dados-para-Filial-ao-Usar-SB1-Exclusiva
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30456970144791) Tempo aproximado para leitura: **00:02:15 min** **Dúvida**

Ao copiar produto quando SB1 totalmente Exclusiva estando posicionado em outra Filial, os dados são criados para a Filial origem. É possível no padrão copiar os registros da Filial Origem para outra Filial?

![sb1 exclusivo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30457462170775)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões   
  
**Solução**

No Protheus padrão quando a **tabela SB1 totalmente Exclusiva**, atualmente a função Cópia do Cadastro de Produtos (MATA010) **não efetua a cópia para outras Filiais**, essa funcionalidade é exclusiva por Filial. Ao efetuar a cópia identifica a Filial que existe o produto e copia para a mesma Filial indicada no registro existente. Esse caso não se trata de erro, e sim o comportamento esperado da rotina.  
  
Na rotina MATA010 existem Pontos de Entrada que permitem alterar o comportamento padrão, verificar juntamente com o seu Analista Desenvolvedor para customizar conforme sua necessidade específica se os pontos de entrada [MT010VLD](https://tdn.totvs.com/x/_uRc) e [A010TOK](https://tdn.totvs.com/x/TuwKDg) permitem ajustar conforme sua necessidade específica.

***MT010VLD - Verifica se a copia do produto está apta para utilização.***  
***<https://tdn.totvs.com/x/_uRc>***  
  
***A010TOK: Validação para inclusão ou alteração do Produto.***  
***<https://tdn.totvs.com/x/TuwKDg>***

Nesse cenário abordado, recomendamos também que entre em contato com a Central Colaborativa sugerindo uma Melhoria no processo padrão que permita **replicar os cadastros de produtos para outras filiais quando utiliza a tabela SB1 EXCLUSIVA**.

Seguem abaixo as instruções para que possa entrar em contato diretamente com eles.

Sugestões de melhoria no produto e deve ser incluída na [Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), localizada em nosso [Portal do Cliente](https://suporte.totvs.com/portal/10098/customer-portal/). É um espaço que você poderá sugerir melhorias, acompanhar a evolução das solicitações já realizadas, comentar, seguir, votar em sugestões feitas por outros clientes e muito mais!  
  
Para conhecer mais sobre as suas funcionalidades [clique AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=14) e assista o nosso vídeo ou acesse nosso artigo [Central Colaborativa - Funcionalidades Disponíveis](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Central-Colaborativa-Funcionalidades-Dispon%C3%ADveis).  
  
Você pode acompanhar as suas sugestões e comentários [clicando AQUI](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br).

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[SIGAEST - MATA010 - Quais são os Pontos de Entrada da rotina de Cadastro de Produtos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003591241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Produtos)
