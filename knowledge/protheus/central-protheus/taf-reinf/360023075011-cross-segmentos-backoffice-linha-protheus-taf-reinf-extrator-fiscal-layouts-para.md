---
article_id: 360023075011
category: TAF - REINF
content_hash: e791977e9adc0c77d67d0807bb1d8303666a38ab2db9c55000c80f49f226f41b
fetched_at: '2026-06-28T22:41:33.395237+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: CROSS Segmentos -  Backoffice Linha Protheus - TAF - REINF -  Extrator Fiscal
  - Layouts para Reinf
type: support-article
updated_at: '2023-10-17T20:14:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023075011-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Extrator-Fiscal-Layouts-para-Reinf
---

**Dúvida:**  
  
Procedimentos de Utilização e Configuração do Extrator Fiscal  
  
**Ambiente:**

Microsiga Protheus - Livros Fiscais - A partir da versão 12  
  
**Solução:**   
  
A rotina Extrator Fiscal (EXTFISXTAF) está disponível no módulo 09 - Livros Fiscais e é responsável pela integração dos documentos fiscais e seus cadastros ao TAF para transmissão do REINF.

Nesta rotina podemos integrar diversas informações dos módulos livros fiscais e financeiro, porém para a extração dos dados que serão levados ao REINF apenas os layouts abaixo são considerados:

T001 - Complemento do cadastro de Estabelecimentos - R-1000

T001AB - Processos referenciados - R-1070

T001AO - Informações de suspensão de exigibilidade de tributos - R-1070

T001AN - Informações da Software House - R-1000

T002 - Informações do Contabilista - R-2099

T003 - Cadastro de Participantes - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T005 - Unidades de Medida - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T006 - Cadastro de Unidade de Medida para o Fator de Conversão - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T006AA - Fatores de Conversão de Unidade de Medida - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T007 - Identificação do item (Produtos/Serviços) - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T009 - Cadastro de Natureza da Operação - Utilizado pela rotina de processamentos para amarrar o código de produto a uma natureza de operação

T010 - Cadastro do Plano de contas Contábeis - Utilizado na integração dos dados para o TAF. É imprescindível a extração do plano de contas para que os dados sejam importados para o TAF.

T013 - Cadastro de Documentos Fiscais (Serviços/Mercadorias) - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T013AJ - Cadastro de Vencimento das Faturas - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T013AP - Cadastro dos Tributos por Documento Fiscal - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T015 - Itens do documento fiscal - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T015AE - Cadastro de Tributos por Item do Documento - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T015AK - Indicativo de Suspensão para Processos Judiciais - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060/R-1070

T082 - Contribuição Previdenciaria sobre a Receita Bruta - R-2060

T154 - Cadastros de Recibos / Fatura - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T154AA - Tipos de Serviço - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T154AB - Parcelas da Fatura/Recibo - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

T154AF - Indicativo de suspensão  para Processos Administrativos - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060/R-1070.

T157 - Cadastros de Obras - R-2010/R-2020/R-2030/R-2040/R-2050/R-2060

A rotina do Extrator Fiscal está preparada para extrair apenas os dados do REINF, através da pergunta "Filtra Apenas REINF". Com esta pergunta igual a "Sim", o sistema irá extrair apenas os layouts necessários para geração do REINF. É recomendado a utilização desta pergunta para aumento de performance do extrator e consequentemente nos processamentos dentro do TAF.

<https://tdn.totvs.com/display/public/TAF/FIS0001_Extrator_Fiscal_x_TAF#FIS0001_Extrator_Fiscal_x_TAF-ProdutorRural>

* **Filtra Apenas Reinf? (7):**

Este campo permite que seja feita a extração apenas dos leiautes pertinentes a REINF.

**![](https://tdn.totvs.com/download/thumbnails/233757571/image2019-3-18_18-44-12.png?version=1&modificationDate=1552945452900&api=v2)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048125073/mceclip1.png)

**As perguntas "Deseja Integrar" e "Filtra Apenas Reinf" são executadas em conjunto com as seguintes combinações:**

**![](https://tdn.totvs.com/download/attachments/233757571/image2019-7-4_18-31-29.png?version=1&modificationDate=1562275890073&api=v2)**

![](https://tdn.totvs.com/download/attachments/233757571/image2019-3-19_16-9-33.png?version=1&modificationDate=1553022573520&api=v2)

**Registros que serão gerados para REINF de acordo com a opção selecionada na pergunta "Deseja Integrar", lembrando que os registros "filhos" são gerados automaticamente de acordo com os registros "pais".**

![](https://tdn.totvs.com/download/attachments/233757571/image2019-3-18_19-11-26.png?version=1&modificationDate=1552947086910&api=v2)

* **Opção: 1 - Somente Cadastros**

Se utilizado em conjunto com o campo **"Filtra Apenas Reinf"**igual a**"1-Sim"**, o sistema não irá apresentar a tela de seleção dos leiautes, mas apresentará a tela abaixo, informando quais os leiautes serão integrados.

![](https://tdn.totvs.com/download/attachments/233757571/image2019-3-18_19-13-16.png?version=1&modificationDate=1552947196763&api=v2)

* **Opção: 2 - Somente Movimentos:**

Se utilizado em conjunto com o campo **"Filtra Apenas Reinf"**igual a**"1-Sim"**, o sistema não irá apresentar a tela de seleção dos leiautes, mais apresentará a tela abaixo, informando quais os leiautes serão integrados.

![](https://tdn.totvs.com/download/attachments/233757571/image2019-3-18_19-15-12.png?version=1&modificationDate=1552947313157&api=v2)

* **Opção: 3 - Ambos:**

Se utilizado em conjunto com o campo **"Filtra Apenas Reinf"**igual a**"1-Sim"**, o sistema **não** irá apresentar a tela de seleção dos leiautes, mais apresentará a tela abaixo, informando quais os leiautes serão integrados.

![](https://tdn.totvs.com/download/attachments/233757571/image2019-3-18_19-16-12.png?version=1&modificationDate=1552947372193&api=v2)

**Atualização**

O pacote de atualização abaixo contém a atualização que criou a pergunta da "Filtra apenas REINF" na rotina do Extrator Fiscal:

<https://suporte.totvs.com/portal/p/10098/download?e=695526>

Além disso é necessário a execução do UPDDISTR. Substitua o arquivo sdfbra.txt da pasta systemload pelo arquivo disponibilizado no link acima e execute o UPDDISTR em acesso exclusivo.

**OBS:****Carga de Cadastros**

**É altamente recomendável realizar uma carga inicial de todos os cadastros no TAF, ou seja, selecionar os registros de cadastro do layout ( T003, T007, T010, entre outros... ) de um longe período e processar a importação desses registros no TAF.**

**Exemplo:**

* **Executar a rotina utilizando a pergunta Deseja integrar = Somente Cadastros.**

Mais informações referente ao Extrator Fiscal: <https://tdn.totvs.com/display/public/PROT/FIS0001_Extrator_Fiscal_x_TAF>
