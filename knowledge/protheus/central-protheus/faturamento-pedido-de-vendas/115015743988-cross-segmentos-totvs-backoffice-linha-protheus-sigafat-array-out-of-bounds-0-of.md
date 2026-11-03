---
article_id: 115015743988
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 147d047303f7ffbc0fde5fd0b4433b8ffd391076682ccf70ec4c429000984b5d
fetched_at: '2026-06-28T22:38:41.078372+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 107 )  on F4LOTE(SIGACUS.PRW)
type: support-article
updated_at: '2022-12-13T11:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015743988-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-107-on-F4LOTE-SIGACUS-PRW
---

**Ocorrência**

Array out of bounds ( 0 of 107 ) on F4LOTE(SIGACUS.PRW)  
  
**Causa**

Ao tentar **inserir um pedido de venda incluindo o lote no item,** ocorre o erro:  
**array out of bounds ( 0 of 107 )  on F4LOTE(SIGACUS.PRW).**

Geralmente, erro de array ocorre quando o campo não existe ou o mesmo não está marcado como usado ou teve seu nível de campo alterado.  
  
Neste caso, a função **F4LOTE** está validando o campo **c6\_dtvalid** , que pode não estar marcado como usado ou pode ter tido o seu nível de a campo alterado do padrão que é 1.

Outra situação em que este erro pode ocorrer é na geração de um pedido do tipo complemento (preço, quantidade, icms, icms st ou ipi) ou devolução de compras, ao dar enter+F4 sob o campo de **nota fiscal de origem** (**c6\_nfori**).  Pa esra etsa segunda situação, o erro foi corrigido na issue **DMANMAT02-35464**.  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões  
  
**Solução**  
Para solucionar:

* **Erro na inclusão do lote:**
  + Acessar o modulo**SIGACFG - Configurador→ Base de Dados → Dicionário → Base de Dados**
  + Pesquisar a tabela **SC6** e buscar pelo campo **c6\_dtvalid**;
  + Alterar o campo ,selecionar a ABA **USO**, deixar o campo como  **USADO** e  o nível de campo igual **1**.
  + Salvar o campo, salvar a tabela e atualizar o dicionário de dados.
  + Reinicie o smartclient e efetue o procedimento novamente.

* **Erro na busca da nota de origem para pedidos de complemento de preço, IPI, ICM , ICMs st e devolução de compra:**
  + Efetue o download do **pacote de correção **DMANMAT02-35464**** , conforme a release de sistema:
    - **12.1.17: <https://r.totvs.io/p/1046250> ; (garantia estendida)**
    - **12.1.25: <https://r.totvs.io/p/1046251> ;**
    - **12.1.27: <https://r.totvs.io/p/1046252> ;**
    - **12.1.33: <https://r.totvs.io/p/1046253> ;**
  + Aplique o pacote via TDS , reinicie o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**

**O pacote de expedição contínua do Módulo de Materiais , onde o pacote já está incluído, está disponível para download através do link: [Pacotes de Atualização - Estoque e Custos e Automação e Coleta de Dados](https://tdn.totvs.com/x/2hgdHw)**
