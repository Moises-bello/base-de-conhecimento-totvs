---
article_id: 29000337545751
category: Financeiro - Conciliador Backoffice
content_hash: 63e84d2ec127117a5d4ab8714c8ed5c4e39dde34d00a8de9072e80fef8d56a9e
fetched_at: '2026-06-28T22:37:47.127800+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Ponto de entrada Conciliador
  Backoffice
type: support-article
updated_at: '2026-05-27T20:25:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29000337545751-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Ponto-de-entrada-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29000337538711) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Pontos de entrada disponíveis na rotina de Conciliação Manual/Automática do novo Conciliador Backoffice.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - a partir da release 12.1.2210.  
  
**Solução**

Os Pontos de Entrada disponíveis na Conciliação Manual/Automática são:

* [F474CTA - Ajustar informações bancárias para a busca dos registros a conciliar.](https://tdn.totvs.com/x/3e9ILg)
* [F474EFT - Aplicar regras de efetivação dos movimentos dos registros do extrato bancário na importação do arquivo de extratos.](https://tdn.totvs.com/x/nv9ILg)
* [F475AGRV - Ponto de entrada para manipulação nas ações de efetivação ou cancelamento de efetivação.](https://tdn.totvs.com/x/mfJILg)
* [F475PGRV - Ponto de entrada para manipulação após a transação da conciliação](https://tdn.totvs.com/x/fpZILg)
* [F475NAT - Ponto de entrada para manipulação da natureza para movimentos bancários](https://tdn.totvs.com/pages/viewpage.action?pageId=809523284)
* [FA473CON - Permite ao usuário conciliar movimentos do extrato bancário de acordo com chave definida](https://tdn.totvs.com/x/4qTtEw)
* [FA473MOD- Ponto de entrada para manipulação da estrutura de campos do modelo de dados da Conciliação Bancária](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491773)
* [F473CAGR - Complemento gravação cancelamento de efetivação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=697700078)
* [FA473001 - Permite manipular os dados dos movimentos bancário e do extrato para exibição em tela.](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491358)
* [FA473002 - Permite manipular a query que carrega os movimentos bancários](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491430)
* [FA473003 - Permite manipular a execução da conciliação bancaria manual](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491699)
* [FA473004 - Permite manipular a query que carrega os extratos bancários](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491676)
* [FA473011 - Validar os registros que serão gravados conciliação automática](https://tdn.totvs.com.br/pages/viewpage.action?pageId=573979124)
* [FA473013 - Ponto de entrada para manipulação da relação entre os campos das tabelas SE5 e SIG](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491758)

* **Pontos de entrada que perdem seu uso:**

[FA473005 - Ponto de entrada de validação na rotina FI473Pos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491718) - Regra de complemento de validação da conciliação manual no Conciliador TOTVS.

[F473VIEW- Ponto de entrada para manipulação da estrutura de dados da visualização da conciliação bancária automática](https://tdn.totvs.com/pages/viewpage.action?pageId=572491784)

* **Pontos de entrada mantidos - De/para dos nomes antigos para os novos**

| **Ponto de entrada antigo** | **Ponto de entrada novo** |
| --- | --- |
| [FA473006 - Permite manipular gravação dos campos da tabela SIG](https://tdn.totvs.com.br/pages/viewpage.action?pageId=573966542) | [F475AGRV - Ponto de entrada para manipulação nas ações de efetivação ou cancelamento de efetivação.](https://tdn.totvs.com/pages/viewpage.action?pageId=776532633) |
| [FA473012 - Ponto de entrada para manipulação após a transação da conciliação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=572491732) | [F475PGRV - Ponto de entrada para manipulação após a transação da conciliação.](https://tdn.totvs.com/x/fpZILg) |
| [F473ATUDT - Atualização da data de disponibilidade na conciliação bancária automática](https://tdn.totvs.com.br/pages/viewpage.action?pageId=697699409) | [F474EFET - Aplicar regras de efetivação dos movimentos dos registros do extrato bancário na importação do arquivo de extratos.](https://tdn.totvs.com/pages/viewpage.action?pageId=776535966) |
| [FA473CTA - Ajustar informações bancárias para a busca dos registros a conciliar.](https://tdn.totvs.com/pages/viewpage.action?pageId=697696820) | [F474CTA - Ajustar informações bancárias para a busca dos registros a conciliar.](https://tdn.totvs.com/x/3e9ILg) |

**Saiba mais**

[FINA474 - Manutenção de Extratos Bancários](https://tdn.totvs.com/pages/releaseview.action?pageId=721003882)  
[FINA475 - Configuração do Retorno de Extratos Bancários Automático](https://tdn.totvs.com/pages/releaseview.action?pageId=747320567)
