---
article_id: 6744079619479
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 90132662c450f57b3b69fb2eaeef57817d98bfa842d20eda760c84b14e0a6f2f
fetched_at: '2026-06-28T22:39:09.464017+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Como incluir
  campos no Browse do Cadastro de Produto?
type: support-article
updated_at: '2022-06-13T19:12:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6744079619479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-incluir-campos-no-Browse-do-Cadastro-de-Produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como configurar campos específicos na tela (*browse*) da rotina Cadastro de Produto?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para que um campo (SB1) seja apresentado no *Browse* da rotina de Cadastro de Produtos, veja os passos abaixo:

Via Configurador (SIGACFG), acesse ao Dicionário de Dados (Dicionário -> Base de Dados -> Dicionário).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6743818835095/mceclip0.png)

Selecione a tabela SB1 e o campo que deseja que apareça no Browse. Exemplificaremos usando o campo B1\_LOCPAD (Armazém Padrão).

Na coluna "Uso", marque a opção "Browse":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6743856391575/mceclip1.png)

Clique no ícone do Disquete (atualizar base de dados) e avance até a conclusão do salvamento:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6743861746583/mceclip2.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6744233809815/mceclip4.png)

Após isso, vamos acessar à rotina de Cadastro de Produtos (04 - Estoque/Custos -> Atualizações -> Cadastros -> Produto). Podemos perceber que o Sistema apresentou no Browse o campo especificado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6744077616407/mceclip3.png)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
