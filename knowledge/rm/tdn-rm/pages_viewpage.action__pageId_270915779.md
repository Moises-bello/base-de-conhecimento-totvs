---
content_hash: ffe5988103c2f84f5780cd8e3cd2a6ff995ff61f6764e120d59bf405f85969a0
fetched_at: '2026-06-29T00:08:25.454181+00:00'
page_id: '270915779'
product: rm
source: tdn-rm
title: Imprimir se grupos internos forem vazios RMREPORTS.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270915779
version: 3
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo desse documento é orientar a maneira de configurar no RMREPORTS caso o detalhe filho (SubDetalhe) não possua dados, o detalhe principal (Detalhe1) não seja impresso.

# Exemplo:

---

***Segue abaixo exemplo do relatório:***

Para exemplificar, criei um relatório simples utilizando como fonte de dados duas tabelas, a PFUNC (Funcionários) no Detalhe1 e no SubDetalhe1 inseri a tabela PFDEPEND (Dependentes dos funcionários). Além do Detalhe1 e do SubDetalhe1, inseri também o CabeçalhodoDetalhe1 [para realizar a quebra no relatório conforme](http://tdn.totvs.com/display/public/rm/Como+Criar+Totalizador+com+Quebra+por+Grupo) [documento](http://tdn.totvs.com/display/public/rm/Como+Criar+Totalizador+com+Quebra+por+Grupo) [e também um CabeçalhodoDetalhe2 apenas para controlar os dados que serão impressos, assim não há necessidade de inserir esse grupo em seu relatório.](http://tdn.totvs.com/display/public/rm/Como+Criar+Totalizador+com+Quebra+por+Grupo)

Ao gerar o relatório dessa maneira, o mesmo irá retornar todos os funcionários da base de dados utilizada e também seus dependentes mesmo que algum funcionário não possua dependente, conforme print abaixo:

Para realizar a configuração para imprimir somente se o grupo interno possuir dados, acesse as propriedades do relatório (RPTREPORT Relatório) e em Impressão, expanda Relatório Opções de impressão configure conforme abaixo:

* Contagem Detalhe em tempo de Design = 0
* Contagem Detalhe Vazia = 0
* Detalhe Contagem quando a fonte de dados está vazio = 0
* Imprime se fonte de dados está vazio = Sim

Além dessas configurações nas propriedades do relatório, acesse as propriedades do Subdetalhe1 em Impressão, expanda Relatório Opções de impressão configure:

* Contagem Detalhe em tempo de Design = 0
* Contagem Detalhe Vazia = 0
* Detalhe Contagem quando a fonte de dados está vazio = 0
* Imprime se fonte de dados está vazio = Não

Ao realizar essas configurações, o relatório será gerado somente com os funcionários da base de dados utilizada que possuam dependentes cadastrados.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Imprimir se grupos internos forem vazios RMREPORTS.

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
