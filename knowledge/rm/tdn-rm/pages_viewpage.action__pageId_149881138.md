---
content_hash: f1408c816c4d64d99191ea62dc10f34b69cfe922ff888edc77a183e22d9f0536
fetched_at: '2026-06-29T00:05:56.003740+00:00'
page_id: '149881138'
product: rm
source: tdn-rm
title: Utilizando a atividade "Gerar Exceção"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881138
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework |
| **Processo** | **:** | Fórmula Visual |
| **Subprocesso** | **:** | Utilizando a atividade "Gerar Exceção" |
| **Data da publicação** | **:** | 21/07/2014 |

**Objetivo:**A finalidade da atividade de "Gerar Exceção" é interromper o processo e exibir uma mensagem.

Primeiramente é necessário arrastar a atividade "Gerar Exceção" para o "fluxo de trabalho" sequencial em sua fórmula visual.

|  |
| --- |
|  |

Após a atividade ter sido adicionada ao fluxo de trabalho é necessário configurar as propriedades da atividade.

|  |
| --- |
| O conteúdo da propriedade "Mensagem de Erro" será exibido caso a execução do fluxo de trabalho sequencial passe por esta atividade. |

Propriedade Tipos de Exceção

A propriedade **Tipo de Exceção** não é obrigatória, mas especificar um desses tipos, se implementado, faz com que a tratativa da exceção seja mais acertiva. Existem diversos tipos de exceção, dos quais se tratam uma diversidade de exceções, por exemplo:

1. Existem tipos de exceção do próprio .NET Framework, tais como:

+ [NullReferenceException](http://msdn.microsoft.com/en-us/library/system.nullreferenceexception.aspx)

  > *A exceção é mostrada quando um objeto não possui uma referencia na memória.*
+ [OutOfMemoryException](http://msdn.microsoft.com/en-us/library/system.outofmemoryexception.aspx)

  > *A exceção é mostrada quando não existe memória suficiente para continuar a execução de um programa.*

  ***Mais em: [Classe Exception, Tipos de Exceção](https://msdn.microsoft.com/pt-br/library/system.exception(v=vs.110).aspx)***

*2.* Existem também tipos customizados, desenvolvidos para uso no RM, tais como:

+ RMSAbortException

  > *A exceção é mostrada quando a operação Abort() é chamada.*
+ RMSMaxRecordsException

  > *A exceção é mostrada quando o máximo de registros por visão foi alcançado.*

O uso de um **tipo genérico de Exceção**, por exemplo, **Exception (System.Exception)**, traz mensagens genéricas do que pode ter causado à exceção, porém o uso de um **tipo de Exceção** específico, faz com que as mensagens de erro sejam direcionadas àquela exceção, ou seja, mensagens com textos mais detalhados do que causou àquela exceção.

|  |
| --- |
|  |

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
