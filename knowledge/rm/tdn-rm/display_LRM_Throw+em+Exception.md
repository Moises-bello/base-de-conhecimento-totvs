---
content_hash: 5f1c15b57ae45aed4fbcbd10cdaa2765d6a4325bf51093d1b1ef28eabba1405a
fetched_at: '2026-06-29T00:08:49.519204+00:00'
page_id: '330839041'
product: rm
source: tdn-rm
title: Throw em Exception
type: documentation
url: https://tdn.totvs.com/display/LRM/Throw+em+Exception
version: 5
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Auxiliar na implementação/manutenção do Snowden.

# Execução:

---

        Devemos realizar **throw new Exception();** ou **throw ex;** apenas se temos a intensão de modificar os dados da exceção. Caso contrário, deve-se utilizar apenas a **throw;** pois desta forma, o StackTrace da Exception é preservado.

Ex.:

c#

        No código acima, a Exception propagada pelo método StackTraceCompleto contemplará o método GerarException enquanto o método StackTraceIncompleto não, perdendo informações importantes para a análise do problema.

Resultado:

StackTraceIncompleto:

   em RM.ExceptionThrow.Program.StackTraceIncompleto() na c:\Projetos\RM.ExceptionThrow\RM.ExceptionThrow\Program.cs:linha 41

   em RM.ExceptionThrow.Program.Main(String[] args) na c:\Projetos\RM.ExceptionThrow\RM.ExceptionThrow\Program.cs:linha 15

StackTraceCompleto:

   em RM.ExceptionThrow.Program.GerarException() na c:\Projetos\RM.ExceptionThrow\RM.ExceptionThrow\Program.cs:linha 58

   em RM.ExceptionThrow.Program.StackTraceCompleto() na c:\Projetos\RM.ExceptionThrow\RM.ExceptionThrow\Program.cs:linha 52

   em RM.ExceptionThrow.Program.Main(String[] args) na c:\Projetos\RM.ExceptionThrow\RM.ExceptionThrow\Program.cs:linha 24

        Desta forma, devemos sempre levar em consideração se a exceção será tratada ou apenas propagada no ponto do catch

        Fonte: <https://docs.microsoft.com/pt-br/dotnet/csharp/language-reference/keywords/throw>

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Throw em Exception

falsefalse

**Status:** Finalizado

false

**Data:** 15/01/2018

false

**Autores:**
