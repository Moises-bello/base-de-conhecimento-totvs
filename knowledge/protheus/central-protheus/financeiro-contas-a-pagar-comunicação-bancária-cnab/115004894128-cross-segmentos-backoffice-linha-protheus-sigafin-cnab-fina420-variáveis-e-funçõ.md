---
article_id: 115004894128
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 96c05946c83473bf3c6faa3d8654410c805058ddf8498731ad79ab27ccd26cce
fetched_at: '2026-06-28T22:37:55.343918+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA420 - Variáveis
  e funções para configuração de CNAB
type: support-article
updated_at: '2026-05-05T14:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004894128-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA420-Vari%C3%A1veis-e-fun%C3%A7%C3%B5es-para-configura%C3%A7%C3%A3o-de-CNAB
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25174214774807)** Tempo aproximado para leitura: **00:05:00min**  
  
**Dúvida**  
Existem variáveis e funções que possam ser utilizadas na configuração de CNAB?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Solução**

**Funções CNAB:**

**. MOD10****→** Calcula o digito verificador de uma seqüência de números baseado no módulo 10.  
**. VLDCODBAR****→** Valida o Código de Barras ou Linha Digitável.  
**. SOMAVALOR****→** É composta pelo conteúdo dos campos: **Saldo** + **Acréscimo** - **Decréscimo**. Obs: Função disponível para Cobrança e Pagamentos ( mesmo conceito para variável "**nSomaValor**").

**. INCREMENTA****→** Incrementa um a um, à determinado Número:  
**. NOSSONUM →** Retorna digito de controle.  
**. NUMTITULO****→** Função de busca por chave única (Prefixo+Número+Parcela+Tipo+Fornecedor) - Utilizada Somente em **CNAB de Pagamentos**.  
**. GRAVADATA****→** Retorno de um campo data com formatos diferentes conforme parametrização desejada.  
**. SOMAABAT****→** Calcular o total de abatimentos do título.  
. **SUBSTR** → Extrai uma parte de uma cadeia de caracteres.  
. **STRZERO** → A partir de um numérico esta função retorna uma string formatada, inserindo zeros à esquerda.  
**. MODULO11 →** Calcula dígito verificador do Nosso Numero.  
**.** **CNABCED** **→**Retorna o cedente/beneficiário do boleto bancário:  
 [CNABCED - Retorna o cedente/beneficiário do boleto bancário.](https://tdn.totvs.com/pages/releaseview.action?pageId=513430989)

**Variáveis CNAB**

**· TITULO →** Referência utilizada para encontrar o número do título no Banco de dados - Ex: Conteúdo definido nas posições "001009" do arquivo de retorno, devem ser iguais ao  **E2\_IDCNAB**.  
**· ABATIMENTO →** Referência ao Abatimento aplicado no título.  
**· ESPECIE →** Referência à descrição da tabela 17 na SX5. Ex: "01" - DP.  
**· MULTA →** Referência ao valor de Multa aplicado no título.  
**· OCORRENCIA →** Referência ao código da ocorrência cadastrada na tabela SEB.  
**· IOF→** Referência ao valor de IOF cobrado.  
**· DATA →** Referência à data da ocorrência. Ex: Ocorrência "06" - Baixa de título - Data: 01/01/2018 - A data da baixa é 01/01/2018.  
**· OUTROSCREDITOS →** Referência à créditos aleatórios.  
**· VALOR →** Referência ao valor do título a ser processado.  
**· DATACREDITO →** Referência à data de disponibilidade do valor cobrado ou do valor pago.  
**· DESPESA →** Referência à despesa de cobrança. (Valor cobrado pelo banco).  
**· MOTIVO →** Referência ao motivo da ocorrência retornada pelo banco. (Usada geralmente quando á ocorrência é de rejeição).  
**· DESCONTO →** Referência ao valor de desconto aplicado no título.  
**· NOSSONUMERO →** Referência ao número disponível para identificação do título.  
**· JUROS →** Referência ao valor de Juros aplicado no título.  
**· RESERVADO →**Esse campo é informado a variável **título** no arquivo de configuração de retorno.  
**· SEGMENTO →** Definição do Segmento utilizado em cada registro.  
**. CGC →** Referência ao CPF/CNPJ do Fornecedor / Sacador.  
**. CODBAR →** Referência ao Código de Barras do título (Geralmente utilizado com autenticação do segmento Z).  
**. SEGJ52 →** Referência ao detalhamento do segmento J-52.  
**. IDENT REG OPCIO →** Referência ao identificado de registro opcional. Ex: Detalhe Tipo 5.

**Saiba mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
* Estrutura de arquivos, Variáveis e funções : [Estrutura dos arquivos de configuração CNAB](https://tdn.totvs.com/pages/releaseview.action?pageId=327329139)
