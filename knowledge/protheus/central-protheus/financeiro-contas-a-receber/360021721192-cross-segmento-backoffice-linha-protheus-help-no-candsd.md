---
article_id: 360021721192
category: Financeiro - Contas a Receber
content_hash: 14458c76d80d4128d80c749fc28bbb8e84e6a1bc547e3da8eb71cf72535b69f8
fetched_at: '2026-06-28T22:38:12.710589+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - HELP NO_CANDSD
type: support-article
updated_at: '2021-08-16T18:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021721192-Cross-Segmento-Backoffice-Linha-Protheus-HELP-NO-CANDSD
---

**Dúvida**No Contas a Pagar ou Contas a Receber ao tentar excluir um desdobramento apresenta a mensagem HELP NO\_CANDSD.

**Ambiente**Microsiga Protheus - Financeiro  - A partir da versão 12  
  
**Solução**Para  o cancelamento do **desdobramento** seja possível, é necessário que o parâmetro **MV\_NRASDSD** esteja preenchido como .**F**. e a tabela **FI8** e **FI7** esteja com o mesmo nível de compartilhamento que a tabela  **SE2**.  
O parâmetro **MV\_NRASDSD** foi criado para definir se o processo de **inclusão de títulos** via **desdobramento** ocorrerá de acordo com o processo antigo, ou seja, o título originador será excluído e os desdobramentos poderão ser excluídos manualmente, sem que seja necessário cancelar desdobramentos. Vale salientar que com o emprego desta funcionalidade, o rastreamento não será utilizado mais para **desdobramentos**, apenas para **faturas** e **liquidações.**

Caso o parâmetro **MV\_NRASDSD** não exista, acesse o **Configurador** (SIGACFG), opção **Ambientes** >**Cadastros** > **Parâmetros** (CFGX017), crie-o conforme estas instruções:

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Informações** | |
| Nome | MV\_NRASDSD |
| Tipo | Lógico |
| Cont. Por. | .F. |
| **Descrição** | |
| Descrição | Permite que o desdobramento de títulos seja realizado na sistemática antiga, sem rastreamento, excluindo o título originador. |

**Procedimentos para Utilização**

1. Acesse o módulo **Financeiro** (SIGAFIN), nas opções **Contas a Receber** (FINA040) ou **Contas a Pagar**(FINA050).  
2. Conforme a configuração do parâmetro **MV\_NRASDSD** - não rastrear desdobramentos – os títulos gerados terão a seguinte condição:

* Se configurado como **.T.** (*true* – verdadeiro):

O **desdobramento** ocorre de acordo com o **processo antigo**, **sem rastreabilidade** e com a **exclusão do título originador**.

* Se configurado como **.F.** (*false* – falso):

O **desdobramento** ocorre de acordo com o **processo atual**, **com** **rastreabilidade** e mantendo o **título originador**.

**OBS:**Caso o parâmetro **MV\_NRASDSD** seja preenchido com **.T.**, será possível inserir dois títulos na rotina **FINA040** com o mesmo numero e tipo, porém a diferença será nas parcelas onde o diferenciará do outro titulo com o mesmo numero, porém sem parcela preenchida pelo campo **E1\_PARCELA.**

**Informações Técnicas**  
Tabelas Utilizadas SE1, SE2, SE5, FI7, FI8 e SFQ
