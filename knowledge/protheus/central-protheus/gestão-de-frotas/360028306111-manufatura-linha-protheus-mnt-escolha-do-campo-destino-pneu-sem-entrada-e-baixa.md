---
article_id: 360028306111
category: Gestão de Frotas
content_hash: e15359335387b3e7468318bd207e4f802799bd5ba93bd24829e7a58bf92db05b
fetched_at: '2026-06-28T22:42:39.407481+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Escolha do campo Destino Pneu sem entrada
  e baixa no estoque
type: support-article
updated_at: '2021-08-13T18:48:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028306111-Manufatura-Linha-Protheus-MNT-Escolha-do-campo-Destino-Pneu-sem-entrada-e-baixa-no-estoque
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)*** Tempo aproximado para leitura: **00:04:00 min****Dúvida**É possível indicar no momento de escolher o campo **Destino Pneu**, quais são os destinos que ocorrem as entradas e baixas no estoque?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Todas as versões  
  
**Solução**Na rotina **MNTA600 -** **Análise Técnica** o parâmetro **MV\_NG1ANAT - Indica quais serão os destinos que sofrerão entradas/baixas no estoque**, serve para indicar no momento de escolher o campo **Destino Pneu**, quais são os destinos que ocorrem as entradas e baixas no estoque. O parâmetro é criado com o valor *default* de **3467**, nesse caso, todos os quatro números sofrem modificações nas tabelas **SD3** e **SB2**.Esse é o valor *default* que o Sistema faz antes desta atualização. Caso a necessidade seja apenas um dos valores, é preciso que ele seja configurado no módulo do **Configurador - SIGACFG**. É necessário a entrada no Sistema em qualquer rotina, para a criação do novo parâmetro **MV\_NG1ANAT**.  
  
Procedimentos para implementação

* No **SIGACFG -** **Configurador** acesse **Ambientes/Cadastros/Parâmetros** - **CFGX017**. Configure os parâmetros a seguir:  
  **MV\_NGSTAGR - Código do status para Aguardando Reforma  
  MV\_NGSTAGC - Código do status para Aguardando Conserto  
  MV\_NGSTAEU - Código do status para Estoque Usado  
  MV\_NGSTAER - Código do status para Estoque Reformado  
  MV\_NGSTAAT - Código do status para Aguardando Análise Técnica Trânsito. Utilizado pelo programa de transferência entre filiais  
  MV\_NGSTAEN - Código do status para Estoque Novo****MV\_NGMNTES - Integração Manutenção - MNT com Estoque - EST. Informar S=Sim ou N=Não  
  MV\_NG1ANAT - Indica quais serão os destinos que sofrerão entradas/baixas no estoque**
* **Produtos - MATA010** - inclusão de dois **Produtos**.
* **Pneus - MNTA083** - inclusão de dois **Pneus** e campo **Estoque** deve ser preenchido com o primeiro produto cadastro e o campo **Status** com o mesmo conteúdo do parâmetro **MV\_NGSTAEU**.
* Acesse **Atualizações / Controle de Pneus / Análise Técnica / Análise Técnica** - **MNTA600**.
* Clique em **Incluir**, informe um dos **pneus** cadastrados.
* No campo **Destino Pneu**, informe **3 = Estoque Usado**.
* Observe que o Sistema não apresenta mais a janela para informar o novo código do produto e do almoxarifado.
* Confira os dados e confirme.
* Acesse **Consultas/Genéricos - LERDA**.
* Procure a tabela de **Movimentações Internas - SD3**, verifique que não houve movimentação.
* Procure a tabela **Saldos Físicos e Financeiro - SB2**, verifique que não houve atualização.
* Acesse **Atualizações/Controle de Pneus/Análise Técnica/Análise Técnica - MNTA600**.
* Clique em **Incluir**, informe outro pneu cadastrado.
* No campo **Destino Pneu**, informe o outro pneu cadastrado.
* No campo **Destino Pneu**, informe **4 = Estoque Reformado**.
* Observe que o Sistema apresenta a janela para informar o novo código do produto e do almoxarifado.
* Informe o código do segundo produto cadastrado.
* Confira os dados e confirme.
* Acesse **Consultas/Genéricos - LERDA**.
* Procure a tabela de **Movimentações Internas - SD3**, verifique que houve movimentação.
* Procure a tabela de **Saldos Físico e Financeiro - SB2**, verifique que houve atualização.
