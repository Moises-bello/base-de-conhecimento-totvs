---
article_id: 36166212190615
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 8789fb1200822af5be81f8491dc39ed7fe0ae1f9904f5a93f54e18d7e1ceb792
fetched_at: '2026-06-28T22:42:05.104935+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Como gerar o registro C100 para Documentos de Entrada utilizando o Configurador
  de Tributos - Regime Não-Cumulativo
type: support-article
updated_at: '2026-05-29T13:06:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36166212190615-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-o-registro-C100-para-Documentos-de-Entrada-utilizando-o-Configurador-de-Tributos-Regime-N%C3%A3o-Cumulativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207001111) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
Como gerar o registro **C100** para Documentos de Entrada, utilizando o **Configurador de Tributos**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão 2310  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

**1.** Acesse a rotina **Configurador de Tributos (FISA170)**

**2.** Abra o diretório **Perfis**, Selecionar o **Perfil de Produto** e clicar em **Incluir:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207001367)  
  
Em seguida, inclua um **Código** para o Perfil, uma **Descrição** e abaixo de **"Cod. Produto"** dê dois cliques, selecione a Lupa e escolha um dos **Produtos** que tenha cadastrado.   
**Observação:** Ao clicar com a seta do teclado para baixo, é possível adicionar outros produtos.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212175767)  
  
**3.** Selecione o **Perfil de Participante** e clique em **Incluir:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207005719)  
  
Em seguida, inclua um **Código** para o Perfil, uma **Descrição**, selecione o **Tipo** e abaixo de **"Participante"** dê dois cliques, selecione a Lupa e escolha um dos **Fornecedores** que tenha cadastrado.   
**Observação:** Ao clicar com a seta do teclado para baixo, é possível adicionar outros fornecedores.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207007639)  
  
**4.** Abra o diretório **Regras de Calculo Documento Fiscal.** Para cada regra dentro deste diretório, será necessário criar 3, uma para cada tributo **PIS, Cofins e ICMS**, alterando o **Código** e a **Descrição**.  
  
**5.** Selecione a **Regra de Base de Calculo** e clique em **Incluir.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207008023)  
  
No campo **Valor Origem** selecione a opção **01 - Valor da Mercadoria** nos três cadastros.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207008407)  
  
**Observação:** O **Valor Origem** pode ser configurado conforme a regra de negócio da empresa e também é possível criar uma fórmula escolhendo a opção **11 - Fórmula Manual** e montando ela na aba **"Detalhamento de Fórmula de Calculo"**. Para mais detalhes entrar em contato com o módulo Protheus Fiscal.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212177687)  
  
**6.** Selecione a **Regra de Alíquota** e clique em **Incluir.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212178455)  
  
No campo **Valor Origem** selecione a opção **04 - Alíquota Informada Manualmente** e no campo **Tp. Alíquota** selecione a opção **1 - Percentual** (nos três cadastros).   
  
E por fim, no campo **Alíquota**, preencha o percentual de cada um deles, por exemplo, para o **PIS** e **COFINS Não Cumulativo será 1,65% e 7,60%** respectivamente, e para o **ICMS 12%**.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212179223)  
  
**7.** Selecione a **Regra de Escrituração** e clique em **Incluir.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36174983095575)  
  
No campo **Incidência** selecione a opção **1 - Tributado** nos três cadastros.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207010199)  
  
E na parte inferior configure pontualmente com a **Tabela CST** do determinado tributo e o **CST** que será utilizado na Entrada (Ex.: 50) para o **PIS** e **COFINS**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207010711)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212181911)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207012375)  
  
**8.** Selecione a **Regra de Calculo - Documentos Fiscais** e clique em **Incluir.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212183959)  
  
É importante selecionar os **Tributos** corretos (**PIS, COF e ICMS**) para a apuração, pois existem cadastros diferentes para PIS e Cofins, como por exemplo PISRET e COFRET. Incluir uma **Data Início** para utilização da regra e o **Status** igual a **2 - Aprovada.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207014167)

Nas **Regras** **de Cálculo** e **Regras de Escrituração,** selecione as criadas anteriormente. A **Regra de Apuração** é necessária nos cadastros de **PIS** e **COFINS**, então no exemplo abaixo foi utilizada uma padrão do sistema, para o regime **Não Cumulativo**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212184983)  
  
Nas **Definições dos Perfis**, no **Participante** e no **Produto** selecione os cadastros criados no início do processo e para a **Origem** e **Operação** selecione conforme a regra de negócio. No exemplo abaixo foram selecionados dois cadastros padrões do sistema.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212185367)  
  
**9.** Inclua um **Documento de Entrada** utilizando os cadastros de Fornecedor e Produto vinculados nos **Perfis**. O cadastro de **TES** deve ter o campo **Atual Ativo = Não** e o **Código Fiscal** preenchido conforme a necessidade.   
Os campos de **Calcula** impostose **Livros Fiscais** devem estar **igual a Não**.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212186007)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166212186519)  
  
**10.** Acesse a rotina **FISA001** e realize o processamento da **Apuração** e após gere o **arquivo txt,** os registros **C100** e **C170** serão gerados:  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/36166207015575)**  
  
  
**Saiba mais**  
[**CFGTRIB - Cálculos no Configurador de Tributos**](https://tdn.totvs.com/pages/releaseview.action?pageId=676039354)  
[**Como calcular IPI no Configurador de Tributos?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34605029826455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-IPI-no-Configurador-de-Tributos)
