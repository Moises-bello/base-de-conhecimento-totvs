---
article_id: 8081072652055
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c5fab8c649099e465a5324dee918f84e869aec26583d43ad8f1d74119932d7f2
fetched_at: '2026-06-28T22:42:00.861134+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - Como gerar
  o registro  E115 no Sped Fiscal automaticamente?
type: support-article
updated_at: '2023-09-22T17:49:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8081072652055-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-E115-no-Sped-Fiscal-automaticamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17743263671831) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como gerar o **Registro E115** no **Sped Fiscal** automaticamente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**Para gerar o **Registro E115** automaticamente é preciso seguir os seguintes passos:

**1.** O primeiro passo do processo é ter dados referente ao **Código de Valor Declaratório**  na tabela **CDY - Cod. Inf. Adicionais da Apuração.** É possível atualizar ou alimentar essa tabela de duas formar: importando a tabela **5.2 - Tabela de Informações Adicionais da Apuração - Valores Declaratórios** referente à UF no Protheus  ou cadastrando o código manualmente via rotina **FISA156 - Códigos de Valores Declaratórios.**

Para importar a **tabela 5.2** para o **Protheus** realize o procedimento abaixo:

-  Acesse site da Receita no *link*  
<http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

-  Selecione a tabela desejada referente a **UF**

-  Baixe a tabela de código de **Valores Declaratórios** (Arquivo txt)

-  Renomeie o arquivo txt baixado do site do **SPED** referente a **tabela 5.2** para **TABELA52.txt**

-  Coloque o Arquivo txt renomeado dentro da pasta *System*

- Execute o compatibilizador **U\_IMPSPED**

-  Durante o processo será feita pergunta **(deseja efetuar a importação das informações cadastrais do SPED?)** selecione botão **SIM**

- Selecione a pasta que esta o arquivo txt (*System*)

Após continuar processo será exibido **Relatório** com as tabelas atualizadas.

**2**. Acesse a rotina **FISA140 - Prod. x Cod.V.Decl**, caminho: **Módulo de livros fiscais > Atualizações > Sped > Prod. x Cod.V.Decl. Manual do cadastro Prod. x Cod.V.Decl**.: <https://tdn.totvs.com/pages/releaseview.action?pageId=640905665>e defina o **Tipo de Enquadramento** dos valores declaratórios, ou seja, se o enquadramento será feiro por **Produto** ou por **Grupo de Tributação (Produto, Cliente e Fornecedor).**O enquadramento é definido pelo parâmetro **MV\_MTCLF3K**.  Se **1 - Enquadramento por Grupos de Tributação: cliente, produto e fornecedor** e se 0**- Enquadramento por Produto.**

Se o enquadramento for definido por **Produto** é preciso informar o código de produto desejado no campo  **Produto - F3K\_PROD**.

Se for definido por **Grupo de Tributação** é preciso informar o respectivo grupo nos campos **Grp. Clientes - F3K\_GRCLAN, Grp.Produto - F3K\_GRPLAN ou Grp Fornec -  F3K\_GRFLAN** de acordo com o grupo que desejar informar. No cadastro de **Clientes, Produto ou Fornecedores** o **Grupo de Tributação** precisa ser o mesmo informado nos campos.

Exemplo:

**Grupo de Tributação de Produto:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8080390379415)

**Cadastro de Produtos**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8080487189399)

Campos quanto ao **Grupo de Tributação** nos cadastros:  
Cadastro de Produtos: Aba Impostos - **Grupo Trib - B1\_GRTRIB**Cadastro de Clientes:  Aba Fiscais - **Grp. Clientes - A1\_GRPTRIB**Cadastro de Fornecedores: Aba Fiscais - **Grp. Tribut - A2\_GRPTRIB**

**3**. Ainda na rotina **FISA140** informe:

- **CFOP** da operação a ser aplicado aquele código  
- **Código de valor declaratório**  
- **CST** da operação a ser aplicado aquele código  
- **Código de Reflexo** conforme  necessidade

- No código de reflexo informado deve estar definida uma regra de cálculo para ser executada no momento de inclusão da nota.

**Importante**

O campo de reflexo estará disponível na rotina **Produto X Código de Valores declaratórios (FISA140)** somente quando parâmetro **MV\_GIAEFD** estiver como desativado **(.F.)**

O código de reflexo utilizado deverá retornar algum valor para que as informações sejam gravadas na tabela  **CDV.** Se o campo **Valor (CE0\_NFVALO)** retornar zero as informações não serão gravadas.

O cálculo será aplicado quando a nota possuir o mesmo **Produto, CFOP e CST** do cadastro realizado na rotina de **Produto X Código de Calores Declaratórios.**

**4.** Gere o lançamento do documento fiscal, utilizando cadastro de **TES** com o **CST e CFOP** informados na **FISA140** e verifique se  na aba de **Lançamentos de Apuração**, clicando no botão  **Valor****Delatório** as informações de código de valores são apresentadas.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8079931403415)

No **Pedido de Venda** (**MATA461**) será exibido na planilha financeira botão de **Valores Declaratórios** para exibir cálculo aplicado no pedido.

**Exemplo:**

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17743291956247)

**5**. Acesse a Rotina **MATA953** e gere a **Apuração do ICMS:**

**Parâmetros****Livro Selecionado** = \* -> “Todos os livros”  
**Apuração** = Mensal  
**Período**= 1º

**Importante:** O parâmetro **MV\_USASPED** deve estar = **.T.** para que seja gravada informação na tabela **CDH.** O código de valor declaratório não precisa ser apresentado na **Apuração do ICMS** mas é necessário rodar a apuração com o parâmetro ativado para que o valor declaratório seja levado ao Bloco **E do Sped Fiscal.**

**6.** Acesse a Rotina **SPEDFISCAL** e gere o arquivo txt do **Sped Fiscal.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8080036808599)

**Manuais relacionados:**

**SPED fiscal**

<http://tdn.totvs.com/display/PROT/FIS0005_SPED_FISCAL>

**FISA140 – Produto X Código de valor declaratório**

<https://tdn.totvs.com/pages/releaseview.action?pageId=640905665>

**FISA072 – Códigos de Reflexos**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Configuração Códigos de Reflexo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042440814-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-C%C3%B3digos-de-Reflexo?source=search)

Informações Técnicas: 

Tabelas Utilizadas: **CDV - Informações adicionais da Apuração**  
Rotinas Envolvidas: **MATA017 - Cadastro das informações adicionais da Apuração**  
Sistemas Operacionais: *Windows* e *Linux*. 

Link contendo as informações acima: 

* [Arq.Magnéticos - Informações Adicionais da Apuração de ICMS (E115 e 1925)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024619954-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Informa%C3%A7%C3%B5es-Adicionais-da-Apura%C3%A7%C3%A3o-de-ICMS-E115-e-1925-)
