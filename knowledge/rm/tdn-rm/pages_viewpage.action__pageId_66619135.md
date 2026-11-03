---
content_hash: c92322c5fb195b10f009168794b8a141bd920b91151c8d7a2d014d5779fac2eb
fetched_at: '2026-06-29T00:11:16.314752+00:00'
page_id: '66619135'
product: rm
source: tdn-rm
title: Apuração IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=66619135
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                       **Versão:** 11.52 |
| **Processo** | **:** | Apuração de Tributos |
| **Subprocesso** | **:** | Apuração IRRF |
| **Data da publicação** | **:** | 15/07/2013 |

Auxílio na apuração do tributo **IRRF** no período de apuração RM Liber.

O sistema RM Liber apenas gera o vencimento da fatura, baseado nas informações do lançamento financeiro. Vide consistências do sistema, para correta geração da guia:

**A) Verifique a Data Base para Geração do IRRF-PF/PJ nos parâmetros do sistema de Gestão Financeira.**

**OPÇÕES – PARÂMETROS – GERAIS/TABELAS – INTEGRAÇÃO – FINANCEIRO – LANÇAMENTOS A PAGAR – GERAÇÃO IRRF PF/PJ.**

Obs.: O parâmetro e o período de apuração devem estar condizentes.

Obs.: Uma vez alterado o parâmetro, apenas terá efeito para os novos lançamentos, realizados após a alteração. Verifique no cadastro do tributo, quanto ao tipo Tributo utilizado:

Exemplo:

Verifique a Integração entre sistemas **Liber x Fluxus e Fluxus x Liber**:

Acesse o menu **OPÇÕES – PARÂMETROS - INTEGRAÇÕES**

Exemplo da tela:

**Consistências no lançamento financeiro:**

* + - Deve ser observado se o Tipo de documento utilizado **"GERA IRRF"**;  
    - A pagar ou a receber;
    - No cadastro do cliente/fornecedor, Pessoa Física ou Jurídica;
    - Valores do **IRRF** e código da Receita.

Verifique os valores de IR e código da Receita.

**Processo de geração de guias:**

* + Verifique se o período de apuração está encerrado (RMLiber – menu Lançamentos – período de apuração).
  + Seleciona o periodo de apuração e clica-se em Processos – Encerramento Período

Após período encerrado, clica em **Processos - Opção de geração de guias a partir de lançamentos financeiros**.

Será exibido uma nova tela para ser informado os dados da fatura e executar o processo. Os campos referem às informações financeiras e pode ser consultado no Help do sistema maiores informações a respeito aos significados dos campos. 

Após executar o processo, o sistema emitirá uma mensagem de processo realizado com sucesso:

Para visualizar as guias geradas, edite o período de apuração, clique na opção Anexos – Guias Darf ( Obs.: Pode ser criado um filtro pelo campo "Valor Apurado" e operador "Is Not Null")

**INFORMAÇÕES ADICIONAIS – POSSÍVEIS ERROS ENCONTRADOS**

* + Erro 1: Processo deverá ser executado em períodos da Filial Matriz!

Solução 1: Deve ser verificado os parâmetros do sistema: **OPÇÕES – PARÂMETROS – GERAIS/TABELAS – APURAÇÃO DE TRIBUTOS – IRRF PF/PJ –Etapa Guias recolhimento 4/4**.  Se não estiver selecionado por Filial, a geração das guias será realizada apenas em períodos de apuração da filial definida como Matriz (**Opções – parâmetros – gerais/tabelas – apuração de tributos – etapa Filial Matriz**).

Significado das opções de Regras Geração **DARF**:

* + Por Beneficiários: Gera todos os impostos na Matriz e agrupando por CNPJ.  
  + Por Filial: Agrupa por Código da Receita, porem por Unidade.  
  + Por Lançamento: Agrupa na Matriz, mas por lançamento.

* + Erro 2: Erro no processo: Não existem Lançamentos Fiscais com incidência do imposto no período com os filtros informados!

Solução 2: Rever as consistências do sistema tratadas anteriormente, pois deve existir algum lançamento onde o tipo documento não é gerador de IRRF ou o tributo IRRF está sem código da Receita ou não valores do IR ou o parâmetro de data base não esta de acordo. Obs.: Quando os lançamentos são originados do aplicativo RM Labore a apuração será realizada pela data de emissão independente da data parametrizada e será consistido o tipo documento vinculado nos lançamentos do Labore.

Para maiores informações:

 [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ApuracaoTribuosRetidos.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
