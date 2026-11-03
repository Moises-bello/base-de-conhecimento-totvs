---
content_hash: 3ac6af0383fc7549c0b5861de24c63eb307bc702186cc20e122e56ce39af6ce1
fetched_at: '2026-06-29T00:11:56.728700+00:00'
page_id: '870395335'
product: rm
source: tdn-rm
title: Apuração RET (Regime Especial de Tributação)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870395335
version: 23
---

#FFA500#FFFACD#FFE766dashedAviso Importante:1%99%

Com o objetivo de proporcionar uma melhor experiência e alinhamento às atualizações mais recentes dos nossos produtos, informamos que o cadastro de **Evento Tributário** (utilizado para Apuração do RET)**,** já disponível no Módulo Gestão Fiscal, não será mais suportado no produto **RM Liber.exe** a partir da **versão 12.1.2502**

Reforçamos que essa alteração faz parte do nosso processo de evolução tecnológica, com a descontinuidade gradual de funcionalidades no **RM** **Liber.exe**. Para garantir a continuidade do processo de **Apuração do RET** recomendamos que sejam realizados testes no Evento Tributário diretamente no **Módulo Gestão Fiscal**, antes do prazo final.

# Conteúdo

**Conteúdo**

# 1. Sobre

O **RET (Regime Especial de Tributação)** é um regime fiscal que simplifica e unifica o recolhimento de tributos para determinados segmentos, como o **setor imobiliário** e de **infraestrutura**. Ele tem como objetivo facilitar o cumprimento das obrigações tributárias, ao consolidar diversos tributos, como **IRPJ, CSLL, PIS** e COFINS, em uma alíquota única, reduzindo a complexidade de cálculo e o volume de guias a serem pagas. O RET é uma opção para empresas que atendem a critérios específicos definidos pela legislação, permitindo maior previsibilidade e controle sobre a carga tributária.

No **Módulo Gestão Fiscal**, a apuração do RET é realizada pelo processo de  considerando o  Vigente para o período. A seguir, detalharemos algumas das principais configurações e cadastros para garantir o correto funcionamento da apuração deste regime.

# 2. Cadastros

Para a apuração correta do RET, é essencial configurar corretamente os seguintes cadastros:

CadastrosFilialCadastro da Filial

No cadastro da Filial marque a opção “**Apura pelo Regime Especial de Tributação**”.

> *Cadastros | Filial | Selecione a Filial | Anexos |  | Aba Tributos.*

ImagemTributoCadastro do Tributo

O tributo correspondente ao **RET** deve estar corretamente cadastrado com o **tipo RET**

> *Cadastros |*

Imagem

644px

Evento TributárioCadastro do Evento Tributário

É necessário cadastrar um  específico para o tributo **RET**.

>  *Obrigações Principais | Evento Tributário**| Estrutura*

Este evento deve ter a opção **"Regras por Filial"** marcada, pois a apuração será realizada por filial.

A **Forma de Tributação** deverá estar configurada como **"Outros"**.

Imagem

O Evento Tributário do **RET** permite a configuração de duas  : **Receitas** e **Exclusões da Receita**. 

Imagem

Os itens das Regras Tributárias do RET são baseadas em informações **contábeis**, sendo esta a única origem possível para este Evento Tributário

ImagemVigência do Evento TributárioVigência do Evento Tributário

Deverá ser cadastrado uma  que determinará as regras aplicáveis à apuração do **RET** para o período.

> *Obrigações Principais |  Eventos Tributários | Vigência*

ImagemPeríodo de ApuraçãoPeríodo de Apuração

Deverá ser cadastrado um  para o tributo RET.

> *Obrigações Principais | Período de Apuração*

Imagem

# 3. Encerramento do Período de Apuração

O processo  é responsável por identificar as Regras Tributárias e realizar os cálculos do imposto.

Ao executar o processo, será solicitado a escolha do **Evento Tributário** vigente para o período em questão. Serão exibidos apenas os Eventos Vigentes para o período selecionado.

Imagem

# 4. Rotina ECF (Escrituração Contábil Fiscal)

Ao gerar a  o sistema automaticamente irá verificar se existe apuração do RET. Se sim, será gerado o  – Linha 16 e  – Linha 14.

**Lembrando que o registro P300 refere-se a Calculo do IRPJ com Base no Lucro Presumido, e o registro P500 refere-se ao  Calculo da CSLL com base no Lucro Presumido.**

Segue trecho de exemplo do arquivo da ECF: 

Exemplo de Arquivo da ECF

# 5. Simulação - Regra de Apuração

> *Obrigações Principais |  Eventos Tributários | Estrutura*

O processo de  permite simular a apuração do imposto sem realizar efetivamente os cálculos e o encerramento do período.  
Ao executar o processo, será solicitado a escolha do **Período de Apuração**.

Imagem

 

Para o tributo RET, abaixo algumas observações importantes:

* O processo não poderá ser executado de forma comparativa, por tanto é necessário selecionar apenas um evento tributário.
* A forma de tributação e o cálculo acumulativo não se aplicam a este tributo.
* O Saldo Credor Anterior só é apresentado caso seja maior do que zero.
