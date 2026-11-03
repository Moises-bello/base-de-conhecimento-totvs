---
article_id: 16463848208919
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 435bca2f0563fe81fa25e10f5231d32b2b8ce33b4fb9449bfd319d7162e8b9cd
fetched_at: '2026-06-28T22:39:07.936763+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MILE importação de
  arquivo da tabela SB1 (Cadastro de Produtos)
type: support-article
updated_at: '2026-06-03T12:24:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16463848208919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB1-Cadastro-de-Produtos
---

O artigo explica como importar o Cadastro de Produtos (SB1) pelo arquivo MILE no Protheus, destacando que a operação é apenas inclusão e que a filial usada é sempre a corrente. Apresenta passo a passo para criar o layout, configurar o arquivo TXT, importar via rotina MATA010 e verificar o produto importado. Inclui links para correção de erros e mais informações sobre MILE no Estoque.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16463834202647) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como importar Cadastro de Produtos (SB1) pelo arquivo pelo MILE?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

***Sugestão*****:**Assista abaixo o ***vídeo com exemplo prático sobre o processo importar o Cadastro de Produtos pelo MILE*** no Protheus:

Para importar arquivo MILE para a tabela SB1 é necessário os seguintes passos, exemplo com a criação de arquivo TXT para importação:

|  |
| --- |
| ***Observação importante antes de iniciar*****:** Como indicado na [Documentação](https://tdn.totvs.com/x/kYQbCQ) da ferramenta MILE, a operação executada para adapters de rotina automática (MSExecAuto) sempre será apenas INCLUSÃO. No MILE **não é possível** passar conteúdo para campo Filial pois, é utilizado sempre a **FILIAL CORRENTE** no momento do processamento.  Ou seja, os dados de importação são sempre para cada Filial, quando utilizar o **compartilhamento da tabela SB1 Exclusivo**, deve criar o arquivo de importação para cada Filial. |

***- 1 -*** Criação do Layout da tabela SB1 com todos os campos padrões utilizados no Cadastro de Produto, exemplo no print abaixo;

![sb1a.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39101464200983)

![sb1b.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39101455835287)

![sb1c.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39101464204823)

![sb1d.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39101455839383)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16464605487127)

Use a condicão **Pad( xa , Len( SB1->B1\_COD ) )** no camo SB1 caso voce queira efetivar tanto inclusão como tambem alteração:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MILE - Erro fatal ao executar adapter. Como corrigir?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012774541-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-Erro-fatal-ao-executar-adapter-Como-corrigir)

***- 2 -*** Configurar o arquivo TXT de importação do MILE para a tabela SB1, veja no exemplo abaixo importando 1 registro para a tabela SB1, caso desejar esta anexo o arquivo TXT;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16464845957911)

***- 3 -*** Na rotina Cadastro de Produtos (MATA010) importar o arquivo criado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16464919753623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16465014733335)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16465025259159)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16465103240087)

***- 4 -*** Pesquisar pelo produto importado pelo MILE, veja o resultado abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16465160814615)

**E para a alteracao tem algum especificação para nao gerar erro?**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MILE - Erro fatal ao executar adapter. Como corrigir?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012774541-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-Erro-fatal-ao-executar-adapter-Como-corrigir)

- Conheça mais detalhes sobre o MILE no Estoque [***clicando aqui***](https://tdn.totvs.com/x/9bA6Kw)

**Saiba Mais:**  
[*Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[*SIGAEST - MILE importação de arquivo da tabela SB7 (Digitação do inventário)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10573324218007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MILE-importa%C3%A7%C3%A3o-de-arquivo-da-tabela-SB7-Digita%C3%A7%C3%A3o-do-invent%C3%A1rio-?source=search)
