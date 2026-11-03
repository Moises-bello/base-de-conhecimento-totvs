---
content_hash: e3e77887470359cf602a1a7d3ca38987074ba9c2754a1f4190b98f8d13c94fef
fetched_at: '2026-06-29T00:11:03.532263+00:00'
page_id: '62390449'
product: rm
source: tdn-rm
title: Gerador de relatórios no RM (nova MDI)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=62390449
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                         **Versão:**11.80 |
| **Processo** | **:** | Gerador de Relatórios |
| **Subprocesso** | **:** | Uso do Gerador de relatórios no RM |
| **Data da publicação** | **:** | 11/06/2013 |

Objetivo: Visualização dentro do RM de relatórios criados em aplicativos Delphi.

Considerando que os relatórios Delphi, do antigo Gerador de relatórios, não podem mais ser editados na nova MDI do RM (RM.exe), estes somente poderão ser gerados e exibidos.

1. Acesse o módulo do produto desejado. Neste caso utilizaremos TOTVS Folha de Pagamento (RM Labore):

     2. Gestão | Ferramentas de Análise | Gerador de Relatórios.Note que o símbolo do Gerador de relatórios é diferente ao do RM Reports.

    3. Selecione o relatório desejado e clique em Processos | Gerar Relatório.

   4. Avançar.

   5.Informe filtros se for o caso.

Observação

Caso o filtro informado contiver parâmetros a serem informados pelo usuário, exemplo: Data de Admissão BETWEEN [DATAINICIAL] AND [DATAFINAL]

O preenchimento será obrigatório. Caso não seja informado, um aviso será emitido.

    6. Informe se o relatório gerado será ou não enviado por email. Neste caso não, será apenas gerado.

    7. Execute-o. Pronto. O relatório será gerado

   8.  A exibição será uma tela semelhante a esta abaixo:

Observações:

* Estes relatórios não podem ser exportados nem muito menos editados.
* A ideia é que os relatórios antigos (feitos em sistemas Delphi) possam ainda ser aproveitados (no modo somente leitura) e que os novos relatórios sejam criados pelo usuário utilizando o RM Reports.
* Relatórios enviados por email estarão no formato ".REL" , exemplo: **Relatório1.REL.** Sendo assim, para visualizá-los será necessário necessário  que o aplicativo RM REL Viewer esteja presente na estação que visualiza o relatório.

Para maiores informações:

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 2 (Software), 2 (Suporte Técnico), 3 (RM), 9 (Demais Áreas), 4 (BI) e 3 (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
