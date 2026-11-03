---
content_hash: f1019cf466c04d78583e512c9637dc3caf1179dc35630b1339f88e1b48aac173
fetched_at: '2026-06-29T00:08:47.176488+00:00'
page_id: '318613248'
product: rm
source: tdn-rm
title: Correção de erros na geração de rotinas que geram arquivos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=318613248
version: 2
---

FAQ: **Correção de erros na geração das rotinas que geram arquivos**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | Todas |

Dica para corrigir problemas de processos que geram arquivos.

No teste abaixo foi simulado um erro no comparativo Sefip x Folha Analítica. Siga os passos para correção deste erro, ainda que sejam gerados em outras rotinas.

1. Usuário tenta executar o relatório (Ex: Comparativo SEFIP x Folha Analítica) e o sistema exibe o erro abaixo;  
     

   Isso acontece porque provavelmente o processo gera um arquivo em uma máquina (máquina X) e depois tenta acessar o mesmo arquivo em uma outra máquina (máquina Y).

   Para corrigir este problema basta seguir os passos abaixo:

   1. Abra o RM.exe;  
   2. Navegue até **"Configurações | Parametrizador | Folha Normal | Geral"**;  
   3. No campo **"Diretório utilizado para processos que geram arquivos em .NET (Jobserver)"** coloque um diretório público com todas as permissões.  
   3.1 O diretório deve possuir o nome da máquina na rede, iniciando com \\NOMEDAMAQUINA\;  
    3.2 O diretório deve ser público e conter todas as permissões de gravação;  
   4. Salve e tente gerar novamente o relatório.
