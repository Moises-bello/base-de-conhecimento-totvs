---
article_id: 6297344354711
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 4ff27ce1847365dd01e66440a9ec2b7192fad923ded66994c7b4ca4ef22bb4a3
fetched_at: '2026-06-28T22:38:23.977279+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Usuário não
  possui vinculo com um Vendedor! (TGV)
type: support-article
updated_at: '2025-01-10T20:16:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6297344354711-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Usu%C3%A1rio-n%C3%A3o-possui-vinculo-com-um-Vendedor-TGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao tentar acessar o TOTVS Gestão de Vendas, apresenta a mensagem **"Acesso Negado - Usuário não possui vinculo com um Vendedor!";**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 12.1.33;  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:  
1. Acessar o modulo do Faturamento (SIGAFAT), ir em Atualizações >> Cadastros >> **Vendedores(MATA040)**;  
2. Realizar a inclusão/Alteração do Vendedor;  
3. Localizar na rotina o campo **"Cod. Usuário - A3\_CODUSR"**, e informar o código do usuário criado no Configurador(SIGACFG);

![20220524_110002.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/6296180641815/20220524_110002.gif)

**Observação**

Verifique no Configurador (SIGACFG), se este usuário esta com a permissão em **"Restrições de Acesso >> Ambientes"** ao modulo do **Faturamento.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10058413752727)**

**Importante**

Para o correto funcionamento das APIs do **Portão Gestão de Vendas**, é de extrema importância que a chave **SECURITY** do **APPSERVER**esteja habilitada.

[HTTPREST]

. . .

SEGURITY=1

. . .

**Atenção**

Um usuário pode ser vinculado somente a um vendedor no Protheus.

Caso após configuração ainda permanecer a mensagem, verifique com a equipe do MINGLE se o ALIAS configurado esta vinculado ao Grupo/Empresa e Filial.

Caso na configuração do Appserver a chave **PrepareIn**estiver igual a "ALL", ou com **"PrepareIn=01,0101"** tem que passar para a equipe do **Mingle** o acesso do Protheus.

Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444589598871/mceclip0.png)

**Exemplo:**

Por Favor criar para o REST o acesso ao grupo/empresa:

REST: localhost:8080/rest

Grupo/Empresa: 01

Filial: 0101

**Observação:** A mensagem **"Acesso Negado - Usuário não possui vinculo com um Vendedor!"** também é apresentada, se não estiver acessando através de um navegador não homologado pela aplicação TGV!

Quais navegadores são suportados pela aplicação?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6516860834327/mceclip0.png)

Fonte: <https://angular.io/guide/browser-support>

**Saiba Mais:**

[Portal Gestão de Vendas: Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=579468339)

[Perguntas mais frequentes do Portal Gestão de Vendas](https://tdn.totvs.com/pages/releaseview.action?pageId=649301318)
