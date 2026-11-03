---
content_hash: 2187f3a483cd1245a9216f56ba24f5e48fb9eb9f34d5cb4c8dbb24218717498d
fetched_at: '2026-06-29T00:09:21.778379+00:00'
page_id: '422545905'
product: rm
source: tdn-rm
title: Apuração Diferencial de Alíquota (Nota a Nota)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545905
version: 21
---

## **01. Visão Geral**

A apuração do diferencial de alíquota visa demonstrar os valores a serem pagos e recolhidos em operações interestaduais, onde há diferença entre a alíquota interna do Estado destinatário e a alíquota interestadual do Estado remetente.  
No TOTVS Gestão Fiscal, há diferentes lugares onde estes valores podem ser originados, conforme a particularidade de cada tipo de operação. Dependendo da origem, os valores podem ser considerados no cálculo da apuração ou gerados em guias de recolhimento nacional - guias GNR.  
Este documento visa esclarecer as parametrizações necessárias para as possíveis origens dos valores de diferencial de alíquota que serão considerados na apuração do DIFAL e dos seus valores gerados nas guias GNR,

## **02. DIFAL na apuração**

Para dar flexibilidade à apuração do diferencial de alíquota, é possível selecionar parâmetros que especificam de onde virão os valores do diferencial de alíquota a serem considerados na apuração.   
Estes parâmetros podem ser acessados pelo caminho "Ambiente | TOTVS Gestão Fiscal | 03.02 - Apuração de Tributos | ICMS | Apur. ICMS por Filial". Dê um clique duplo na filial desejada, clique em avançar e selecione "Parâmetros".

Caso nenhuma das opções acima estejam marcadas, o valor do diferencial de alíquota não será considerado na apuração, sendo considerado apenas o valor do ICMS Próprio.  
Cada um dos parâmetros acima possui um comportamento na apuração do DIFAL:

* **Parâmetro "Considera Diferencial Alíquota - Outros Débitos"**   Indica se o campo Diferencial de Alíquota - Entradas deverá ser totalizado como Débito no Livro Resumo de Apuração do ICMS (Válido para lançamentos fiscais de entrada).

* **Parâmetro "Considerar Diferencial de Alíquota no Saldo Credor/Devedor da Apuração"**   Quando marcado, será considerado no saldo credor/devedor da apuração os lançamentos que possuam diferencial de alíquota (Válido para lançamentos fiscais de saída).

* **Parâmetro "Gerar valor Difal destino por Nota Fiscal"**          
     Indica se a guia referente ao Diferencial de Alíquota no Saldo Devedor/Credor da Apuração será gerada nota a nota.  
     Esta opção não pode ser selecionada caso o parâmetro "Considerar Diferencial de Alíquota no Saldo Credor/Devedor da Apuração" esteja marcado.

* **Parâmetro "Considera Operação Ativo - Outros Créditos"**   Quando marcado, serão considerados na apuração os lançamentos de "Outros Débitos/Créditos" cujo tipo seja "Créditos" e o subtipo seja "Crédito Ativo Imobilizado".  
     Além disso, valor do ICMS dos lançamentos fiscais 1/48 CIAP (série W) não serão somados no total de ICMS de crédito ativo do período de apuração.

Relembrando que, se nenhuma opção estiver marcada, não haverá necessidade de cadastro de lançamentos de Outros Débitos/Créditos.

Caso todas as opções estiverem marcadas - com exceção da opção "Gerar valor Difal destino por Nota Fiscal" - os valores relativos ao ICMS próprio deverão ser totalizados como débito ao encerrar o período de apuração do ICMS.  
Neste caso, será necessário incluir os seguintes Lançamentos de Outros Débitos\Créditos para zerar o Valor do Débito do Difal gerada para UF Origem:

* **Débito:** Fazer lançamento de Outros Débitos com o Subtipo "Não se aplica", usar o código de ajuste adequado, (exemplo: SP000202), com o valor do diferencial de alíquota de origem.
* **Crédito**: Fazer lançamento de Outros Créditos com o Subtipo "DIFAL – Origem Destino", usar o código de ajuste adequado, (exemplo: "SP229999"), com o valor do diferencial de alíquota de origem.

## **03. DIFAL no processo de geração de guias**

Para o ICMS, podem ser geradas guias normais, que serão relativas ao ICMS próprio; e guias GNR, sendo estas relativas ao Diferencial de Alíquota.  
Quando se trata de Diferencial de Alíquota, são considerados na geração automática de guias os valores dos lançamentos de saída.  
Para que os valores do DIFAL dos lançamentos de saída sejam considerados na geração automática de guias, eles devem possuir a seguinte parametrização:

* O estado do Cliente/Fornecedor é diferente do da Filial do contexto (pois será o estado de destino);
* Campo "Operação com Consumidor Final" marcado;
* Possua CFOP com:
  + "Origem/Destino" Interestadual;
  + Regra de ICMS da CFOP com:
    - * "Operação Tributária" marcado com "Diferencial de Alíquota" (aba "Identificação");
      * "% ICMS UF Destinatário" preenchido (aba "Dados ICMS S.T.");
* Na aba de "Diferencial de Alíquota" na Situação Tributária, o campo "Percentual UF Destinatário" deve estar preenchido com o valor do "% ICMS UF Destinatário";

## **04. Particularidades DIFAL por estado da filial**

Em alguns cenários, pode ser específico fazer alguma parametrização específica de DIFAL, dependendo do estado da sua filial, conforme documentações abaixo:

* (específico para filiais de São Paulo)

## **05. Outras informações**

***Importante!***

**1 -** Para que não ocorram erros de validação, os códigos de ajuste devem estar de acordo com a tabela 5.1.1 do SPED, nos lançamentos de Outros Débitos/Créditos.

No período de apuração, incluir manualmente as guias de DIFAL e FECP no anexo "Guias GNR". No anexo "Guias Normal", a guia do ICMS próprio é gerada automaticamente (Processos | Geração de Guias Automaticamente).

**2 -** Não foi realizada a verificação de guias existentes no parâmetro "Gerar valor Difal destino por Nota Fiscal", pois podem existir duas ou mais guias com mesmo valor de FECP ou DIFAL. Com isso, o processo poderia ignorar umas das guias.

Foi criada uma regra para que ao se realizar os procedimentos de Escrituração do Lote Fiscal, inclusão manual do Lançamento Fiscal de Saída, edição do Lançamento Fiscal de Saída e cópia do Lançamento Fiscal de Saída a UF do Lançamento Fiscal de Saída seja obtida de acordo com a seguinte premissa: Quando o tipo de emitente não for empresa e o tipo de documento for NFe a UF de entrega for diferente da UF do CliFor, será retornado a UF de entrega, sendo assim gerando o DIFAL para a mesma.
