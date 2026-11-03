---
content_hash: 175b120577374e17164e5f5bbc2b583f44efeb9d1f02756602a97fc6f79d602a
fetched_at: '2026-06-29T00:11:28.223962+00:00'
page_id: '73073081'
product: rm
source: tdn-rm
title: Uma Chamada a uma função do Windows falhou
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73073081
version: 10
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | Execução ou edição de relatório |
| **Subprocesso** | **:** | Verificação no ambiente 64 bits |
| **Data da publicação** | **:** | 24/07/2013 |

**Mensagem: UMA CHAMADA A UMA FUNÇÃO DO WINDOWS FALHOU**

Esta mensagem é apresentada na edição ou execução de algum relatório DELPHI em sistemas operacionais 64 Bits

Ao ser apresentada deverá ser avaliado algumas condições, são elas:

**-** **Imagem no relatório:** Deverá ser observado se o relatório em questão possui imagem.

Sugerimos que exclua a imagem (como teste) e salve o relatório realizando a execução do mesmo logo em seguida.

Se a geração for positiva insira novamente a imagem no relatório realizando um tratamento na mesma (Neste caso alterando a resolução e o tamanho da mesma).

OBS: Antes de realizar qualquer alteração no relatório realiza-se uma cópia do mesmo para segurança.

**- Número de registros retornados:** Deverá ser observado se o relatório está retornando um grande número de registros, sugerimos que realize uma alteração nos filtros para que retorne um número menor de registros. Realize a geração do mesmo e em seguida acompanhe o comportamento do sistema observando se a mensagem será apresentada.

**- Observar se nas propriedades deste relatório a opção:** **“Executa em BDE”** encontra-se habilitada. Para isto acesse o módulo gerador de relatórios -> Selecione o relatório que apresenta a mensagem e clique na opção para edição do mesmo -> Marque a opção sugerida:

**- Parametrizar a DLL Gerador para executar em 32 BITS:** Antes de realizar os passos abaixo, finalize todas as aplicações TOTVS e “PARAR” o serviço de Host, que encontra-se no diretório:

C:\totvs\CorporeRM\RM.Net (RM.Host.ServiceManager.exe)

**A)** Acesse no Prompt de Comando da máquina

**B)** Digitar o comando cd C:\totvs\CorporeRM\RM.Net

**C)** Execute o comando CorFlags RM.Lib.Gerador.Execute.exe /32bit+

**OBS: Se o ambiente encontra-se em 3 camadas este processo deverá ser realizado no servidor.**

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
