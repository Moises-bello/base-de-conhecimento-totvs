---
article_id: 360062332073
category: Gestão de Frotas
content_hash: 3b1f2c1413d150ddf95da0882122c5a05ba7a764132348de35542ba7d53a9dae
fetched_at: '2026-06-28T22:42:39.358817+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Controle ARLA32 no Manutenção de Ativos
type: support-article
updated_at: '2021-08-03T21:14:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332073-Manufatura-Linha-Protheus-MNT-Controle-ARLA32-no-Manuten%C3%A7%C3%A3o-de-Ativos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:04:3****0 min****Dúvida**É possível fazer o controle do **ARLA32** ou outro aditivo no **Manutenção de Ativos** com **Gestão de Frotas**?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**É possível fazer o controle do **ARLA32** ou outro aditivo no **Manutenção de Ativos** com **Gestão de Frotas**.  
O **Diesel**, a **Gasolina**, o **Álcool**, ambos são tratados pelo Sistema como combustíveis, portanto lançados na rotina de abastecimento. Já o **ARLA32** se trata de um produto, que não é combustível, portanto precisa ser tratado à parte.  
O **ARLA32** é classificado como produto de categoria de risco mínimo no transporte de fluidos. Não é um combustível, nem um aditivo de combustível.  
**Fonte:**<http://brasil.air1.info/pt/all-about-adblue/what-is-adblue/>  
  
O **ARLA32** deverá ser cadastrado como produto e utilizado no processo de consumo via **Ordem de Serviço - O.S**., nunca como combustível. A utilização de outros produtos que não são combustíveis como abastecimento poderá prejudicar na extração de consultas e relatórios relacionados a performance do veiculo.    
  
Procedimento para controle do aditivo **ARLA 32** durante abastecimento em **posto externo**:

* Em **Atualizações > Controle de Oficina > Cadastros Básicos > Produto - MATA010** incluir um **produto** para utilizar como **ARLA 32**.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095012.png?version=1&modificationDate=1627908760337&api=v2)

* Em **Atualizações > Controle de Oficina > Lubrificação > Lubrificantes - MNTA030** cadastrar um lubrificante para utilizar como **ARLA 32**, vinculando ao **produto** incluído no passo anterior.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095114.png?version=1&modificationDate=1627908805223&api=v2)

* Em **Atualizações > Controle de Oficina > Bens > Veículos - MNTA084** incluir um **veículo** que possua tanque de combustível, no tanque deve-se especificar o produto destinado ao **ARLA 32** como **Aditivo/Lubrificante**.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095214.png?version=1&modificationDate=1627908832190&api=v2)

* Em **Atualizações > Controle de Combustíveis > Abastecimento > Abast. Manual - MNTA655** incluir um abastecimento para o **veículo** cadastrado anteriormente, neste passo somente será informado o combustível utilizado no abastecimento. Importante mencionar, que diferente do processo realizado para **posto interno**, o **aditivo/lubrificante** não é informado junto ao abastecimento nesta rotina, sendo este somente informado manualmente no processo apresentado no próximo passo.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20082208.png?version=1&modificationDate=1627907971607&api=v2)

* Em **Atualizações > Controle de Oficina > Retorno de OS > Retorno em Lote - MNTA401** informar como insumo o **produto** cadastrado para controle do **ARLA32**. A opção **Gera Estoque** deve ser mantida como **Não** para que não seja realizada a baixa de estoque. Na linhas inferiores, inserir o veículo anteriormente cadastrado e incluir a quantidade de **ARLA32** utilizado no abastecimento.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20083442.png?version=1&modificationDate=1627907947703&api=v2)

Procedimento para controle do aditivo **ARLA 32** durante abastecimento em **posto interno**:

* Em **Atualizações > Controle de Oficina > Cadastros Básicos > Produto - MATA010** incluir um produto para utilizar como **ARLA 32**.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095012.png?version=1&modificationDate=1627908760337&api=v2)

* Em **Atualizações > Controle de Oficina > Lubrificação > Lubrificantes - MNTA030** cadastrar um lubrificante para utilizar como **ARLA 32**, vinculando ao **produto** incluído no passo anterior.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095114.png?version=1&modificationDate=1627908805223&api=v2)

* Em **Atualizações > Controle de Oficina > Bens > Veículos - MNTA084** incluir um **veículo** que possua tanque de combustível, no tanque deve-se especificar o produto destinado ao **ARLA 32** como **Aditivo/Lubrificante**.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20095214.png?version=1&modificationDate=1627908832190&api=v2)

* Em **Atualizações > Controle de Combustíveis > Abastecimento > Abastecimento Lote Posto Interno - MNTA656** incluir o **abastecimento** com **lubrificação**, sendo que as informações de produto tem colunas especificas no *grid* de abastecimento. Os campos referentes a **produto** somente serão disponíveis para preenchimento quando o campo **Tipo Lançamento** esteja informado como **Produto** ou **Abastecimento + Produto**.  
  Ao confirmar o **abastecimento** é aberta e finalizada de forma automática uma **O.S. - Ordem de serviço** contendo como insumo os produto informando no abastecimento. O número desta **O.S.** fica registrado no campo **O.S. Lubrificação - TQN\_OSLUBR**.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20104707.png?version=1&modificationDate=1627912080903&api=v2)

Procedimento indicadores de controle do consumo do aditivo **ARLA 32**:

* Em **Consulta > Indicadores > Consulta Indicadores - NGIND001** selecionar o indicador **Rendimento Médio de Aditivo**, em seguida no botão **parâmetros**, preencher os **filtros** para que seja contemplado os abastecimentos e reporte de lubrificação realizados, feito isso, clicar em calcular.

![](https://tdn.totvs.com/download/attachments/618888376/Captura%20de%20tela%202021-08-02%20133718.png?version=1&modificationDate=1627922326097&api=v2)

**Saiba mais**  
Veja nos *links* abaixo conteúdos relacionados a abastecimentos  
[Abastecimento Manual (MNTA655 - SIGAMNT)](https://tdn.totvs.com/x/8daFI)  
[Abastecimento de Posto Interno em Lote (MNTA656 - SIGAMNT)](https://tdn.totvs.com/x/qfDLIg)
