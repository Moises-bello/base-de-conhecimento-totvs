---
content_hash: 84e6c4e2241070a23cc50f80cb4d801f5d81e5feb61468ab3cdd0f6d49e0ac02
fetched_at: '2026-06-29T00:11:02.783818+00:00'
page_id: '61934696'
product: rm
source: tdn-rm
title: Contabiliza número de páginas de impressão - Delphi
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61934696
version: 13
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gerador de Relatórios                      **Versão:**11.50 |
| **Processo** | **:** | Renumeração de página em relatórios Delph |
| **Subprocesso** | **:** |  |
| **Data da publicação** | **:** | 11/06/2013 |

O Gerador Delphi não possui ferramentas para este fim.

Porém como solução paliativa pode-se obter o desejado utilizando uma consulta SQL, configurações do sistema e geração dupla do mesmo relatório.

         Como seria esta ação:

         Primeiramente o sistema deve estar configurado para manter o log de execução dos relatórios.

         Esta configuração é feita através dos parâmetros globais do sistema.

Salva a configuração na estrutura do relatório onde deseja-se incluir o respectivo controle de página deve ser incluído um componente “Página” (). Este componente irá retornar o número atual da página gerada pelo relatório.

         Inclua em seguida uma consulta SQL que irá retornar o total de páginas do relatório. A consulta SQL deverá ter o seguinte conteúdo;

SELECT TOP 1 PAGINAS

FROM  RLOGEXEC

WHERE IDRELAT = ( SELECT      ID

                             FROM  RRELAT

                             WHERE CODRELATORIO = :ESPELHO#4\_S

                                   AND   CODAPLIC = 'T' )

            AND INICIO < (    SELECT      Max ( INICIO )

                                   FROM  RLOGEXEC

                                   WHERE IDRELAT = ( SELECT      ID

                                                                 FROM      RRELAT

                                                                 WHERE      CODRELATORIO = :ESPELHO#4\_S

                                                                       AND   CODAPLIC = 'T' )

            AND CODCOLIGADA = :CODCOLIGADA\_N )

            AND CODCOLIGADA = :CODCOLIGADA\_N

ORDER BY    INICIO DESC

|  |
| --- |
| *Obs.: Onde consta a condição “*CODAPLIC = 'T'*” deve-se alterar conforme o aplicativo que usará a consulta SQL. Neste exemplo estamos utilizando o RM Nucleus.* |

         O agrupamento de ambos os compoentes devem ficar da seguinte forma;

Lembrando que mesmo após ter feito todo este aparato **o sistema não irá realizar a contagem das páginas** corretamente quando impresso o relatório pela primeira ou única vez. Deve-se gerar o relatório uma primeira vez para que esta geração seja computada no banco de dados com informações deste relatório, inclusive com o número de páginas gerados. Somente após a segunda geração do relatório a contagem de páginas será realizada corretamente.

         Friso que esta é **uma saída paliativa para o cliente**, pois dependendo do tempo gasto para gerar o primeiro relatório não vale a pena aguardar a primeira geração para iniciar a segunda somente para obter a contagem de páginas com total e página atual.

**OBS: Este recurso já encontra-se disponibilizado em .NET - Acesse:**

---

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
