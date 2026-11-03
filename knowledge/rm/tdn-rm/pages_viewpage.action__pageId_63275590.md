---
content_hash: daa8401df384c3a0bbcae3a892ed18740fd89ce715b7e14f959e264578484400
fetched_at: '2026-06-29T00:11:06.115331+00:00'
page_id: '63275590'
product: rm
source: tdn-rm
title: Variáveis Dinâmicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=63275590
version: 24
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é mostrar quais são as variáveis dinâmicas que podem ser usadas no sistema.

# Introdução

---

          A consulta SQL permite o uso de variáveis dinâmicas que podem ser usadas como parâmetros. Essas variáveis trazem dados de datas atuais ou dados sobre o contexto do sistema. São elas:

**VARIÁVEIS DE DATA**

:$Hoje Compara com a data de Hoje.  
:$NaSemana Compara se a data está entre o início e fim desta semana.  
:$NoMes Compara se a data está entre o início e fim deste mês.  
:$NoAno Compara se a data está entre o início e fim deste ano.

**VARIÁVEIS DE CONTEXTO**

:$CHAPAFUNCIONARIO chapa do funcionário logado.  
 :$CODCOLIGADA código da coligada do contexto.  
 :$CODFILIAL código da filial do contexto.  
 :$CODIGOEXTERNO código externo da filial do contexto.  
 :$CODLOCPRT código da localidade do portal do contexto.  
 :$CODSISTEMA código do sistema que o usuário está logado.  
 :$CODTIPOCURSO código do tipo de curso do contexto.  
 :$CODUSUARIO código do usuário logado.  
 :$CODUNIDADEBIB código da unidade bibliotecária do contexto.  
 :$CODUSUARIOSERVICO código do usuário rodando o serviço RM.Host.Service.exe  
 :$EDUTIPOUSR código do tipo de usuário do Educacional.  
 :$EXERCICIOFISCAL código do exercício fiscal do contexto.  
 :$IDPRJ ID do projeto do contexto.  
 :$RHTIPOUSR tipo de usuário de RH do contexto.

# Exemplo

---

            A consulta SQl a seguir utiliza a variável :$CODUSUARIO (código do usuário logado).

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

 

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.1.XX

false

**Processo:** Variáveis Dinâmicas

false

**Subprocesso:** Variáveis Dinâmicas

falsefalse

**Status:** Finalizado

false

**Data:** 18/01/2017

false

**Autores:**

**Douglas Maxwell de Oliveira**
