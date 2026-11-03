---
article_id: 8736173147671
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 693abdee008bed9be8b06487fc1c354ce8838191e81a5c5f2442e48f5228bec3
fetched_at: '2026-06-28T22:42:05.021592+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os
  registros 1100 e 1500 do EFD Contribuições pelas Rotinas Controle de Saldo de Crédito,
  Rotinas FISA044 e FISA045
type: support-article
updated_at: '2024-05-10T15:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8736173147671-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-registros-1100-e-1500-do-EFD-Contribui%C3%A7%C3%B5es-pelas-Rotinas-Controle-de-Saldo-de-Cr%C3%A9dito-Rotinas-FISA044-e-FISA045
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23395029720727) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar os registros **1100** e **1500** do **EFD Contribuições** pelas **Rotinas Controle de Saldo de Crédito**, Rotinas **FISA044** e **FISA045**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Se os créditos anteriores não foram gerados automaticamente na **Apuração PIS/ COFINS**, é necessário utilizar a Rotina de Controle de créditos de PIS e COFINS para gravar os créditos na **Apuração** e gerar no **arquivo txt.**

Acesse a Rotina da **Apuração do EFD Contribuições (FISA001)**, no Menu clique na opção **Controle de Saldo de Crédito de PIS** e **Controle de Saldo de Crédito de COFINS**.  
  
A Rotina **FISA044** é o **Controle de Saldo de Crédito de PIS**, as informações são gravadas na **Tabela CCY** e com isso é gerado o **Registro 1100 Controle de Créditos Fiscais – PIS/PASEP** do **EFD Contribuições.**

A Rotina **FISA045** é o **Controle de Saldo de Crédito de COFINS**, as informações são gravadas na **Tabela CCW** e com isso é gerado o **Registro 1500 Controle de Créditos Fiscais – COFINS** do **EFD Contribuições.**Na tabela **CCY**, há o campo **CCY\_CREDUT**, onde pode-se verificar o **valor total do crédito de PIS** utilizado no período e o campo **CCY\_CRDISP**, para indicar o **valor de crédito de PIS disponível** para ser utilizado nos próximos períodos.  
  
**Importante:**A rotina utiliza esta data para filtrar todos os créditos que são utilizados no período de escrituração do **EFD PIS e COFINS**, no caso de sobra de valor, ele considera com Saldo para o período posterior, alimentando as tabelas **Controle de Crédito de PIS (CCY)** e **Controle de Crédito de COFINS (CCW)**.

**Período (MMAAAA**): Informe o período de cálculo. Este período deve ser imediatamente anterior ao período a ser gerado no EFD-Contribuições.

Exemplo: Informar mês 03/2024, se você quiser levar os créditos na Apuração de Abril/ 2024.  
Por que, se você inserir 03/2024 e Processar a Apuração de 03/2024, as tabelas CCY e CCW serão zeradas.

**Ano de Origem Crédito**: Informe o ano de origem do crédito, ou seja, em qual período realmente ocorreu o crédito.

**Mês de Origem Crédito**: Informe o mês de origem do crédito, ou seja, em qual período realmente ocorreu o crédito.

**Código**: Informe o código de crédito conforme tabela 4.3.6 da tabela da receita.

**Total de Crédito**: Informe o valor total do crédito referente ao código informado para o período de origem. Este é o total do crédito apurado e não somente o saldo credor.

**Crédito Utilizado**: Informe o valor total do crédito utilizado no mesmo mês da origem, portanto não disponível.

**Utilizado**: Informe a somatória do crédito utilizado desde o mês da origem até o mês anterior ao da escrituração informado no campo **Período**, portanto não disponível.

**Ressarcimentos anteriores**: Informe valor do crédito utilizado como ressarcimento em períodos anteriores ao da escrituração informada em **Período**.

**Compensações anteriores**: Informe valor do crédito utilizado como compensação em períodos anteriores ao da escrituração informada em **Período**.

**Ressarcimento**: Informe valor do crédito utilizado como ressarcimento no período da escrituração informada em Período.

**Compensação**: Informe valor do crédito utilizado como compensação no período da escrituração informada em **Período**.

**Crédito Disponível**: Informe o valor de crédito disponível para ser utilizado nos próximos períodos.

**CNPJ PJ Cendente Cred**: Informar o CNPJ da Pessoa Jurídica cedente do crédito.

**Origem do Credito**: Informar o Indicador da origem do crédito: 01-Créd decorrente de operações próprias ou 02-Crédito Transferido por PJ sucedida.

**Também existe a Rotina (FISA046) - Cadastro de Créditos Extemporâneos**  
Crédito extemporâneo é aquele cujo período de apuração ou competência do crédito se refere a período anterior ao da escrituração atual, mas que somente agora está sendo registrado. O crédito extemporâneo deve ser informado, preferencialmente, mediante a retificação da escrituração cujo período se refere o crédito. No entanto, se a retificação não for possível, devido ao prazo previsto na Instrução Normativa RFB nº 1.052, de 2010, a Pessoa Jurídica deve detalhar suas operações através deste registro.  
  
Após realizar o cadastro no menu do SPED a rotina **Créditos Extemporâneos (FISA046)** inserir os dados como segue abaixo:

**Tipo Nota Fiscal:** Tipo da Nota Fiscal 0 = Entrada ou 1 = Saída.

**Cliente ou Fornecedor:** Informe o código do Cliente ou do Fornecedor.

**Loja:** Informe a Loja do Cliente ou do Fornecedor.

**Nota Fiscal:** Informe o Número da Nota Fiscal.

**Serie:** Informe a Série da Nota Fiscal.

**Espécie Nota Fiscal:** Informe a Espécie da Nota Fiscal.

**Escrituração:** Informe da Data de utilização do crédito na escrituração do SPED PIS e COFINS.  
  
Após a realização do cadastro dos **Créditos Extemporâneos** o Sistema fará a escrituração dos Créditos nos Registros **1100, 1101, 1102, 1500, 1501 e 1502** e atualiza os registros do **Bloco M** para a utilização dos mesmos.  
  
Mais Informações:  
  
*Link* **Apuração EFD Contribuições**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>  
  
*Link* **Arquivo EFD Contribuições**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=715144991>
