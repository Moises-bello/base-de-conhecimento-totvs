---
content_hash: 9bc87c231add6cd615f70e8d965ea3233dcc5c882fe496c6b3e7d67961b70603
fetched_at: '2026-06-29T00:06:04.115554+00:00'
page_id: '200905708'
product: rm
source: tdn-rm
title: ER_Migracao_Calculo_do_Custo_Horario
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Migracao_Calculo_do_Custo_Horario
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP(Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6004 |
| **Requisito1** | PCREQ-6006 | **Subtarefa1** | PDR\_CP\_TOP007-1320 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

        Esta especificação tem como objetivo demonstrar como será tratado o calculo de Custo Horário a partir da versão 12.1.7. Com a migração da arquitetura Delphi para .Net tornou-se necessário modificar a chamada das planilhas dependendo da arquitetura utilizada pelo cliente.

## Definição da Regra de Negócio

Com a mudança de arquitetura Delphi para .Net, tornou-se necessário modificar a chamada da planilha para o calculo de custo horário de Equipamento e Mão de Obra.  O Custo Horário é um calculo realizado pelo orçamentista para identificar o custo de um equipamento ou mão de obra baseado em algumas variáveis definidas no insumo.O Totvs Obras e Projetos possui 2 planilhas (Equipamento e Mão de Obra) padronizadas que realizam este calculo, bastando informar no cadastro de insumo, a planilha e a célula ao qual o usuário deseja receber o valor calculado.

 Como esta ocorrendo a migração de arquitetura Delphi para .Net, é necessário que o calculo de custo horário funcione para as duas plataformas, respeitando a seguinte restrição:

* Planilha RM (RMSolum.exe - Delphi) : Funciona com Planilha RM Delphi ou Planilha RM .Net
* Planilha RM (RM.exe - .Net) :  Funciona apenas com Planilha RM .Net, caso o usuário tenha planilha em Delphi é necessário realizar a migração da planilha.

**Passos para Cálculo e Impressão do Custo Horário de Equipamentos:**

1. Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Parâmetros de Projeto -> aba Projetos | Custo Horário).

2. Criação da planilha com estas variáveis e fórmulas para o cálculo dos valores produtivo e improdutivo do equipamento.

3. Indicação da planilha e das células dos valores produtivo e improdutivo do equipamento (Janela de Edição do Insumo).

4. Cálculo dos valores produtivo e improdutivo na Janela de Edição de Insumo (pasta custo horário) ou pela opção “Calcular Custo Horário” (Aba Orçamento | Insumo).

**Passos para Cálculo e Impressão do Custo Horário de Mão-de-obra:**

1. Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Parâmetros de Projeto -> aba Projetos | Custo Horário).

2. Criação da planilha com estas variáveis e fórmulas para o cálculo do valor unitário da mão-de-obra.

3. Indicação da planilha e da célula do valor unitário da mão-de-obra (Janela de Edição do Insumo).

4. Cálculo do valor unitário do insumo na Janela de Edição de Insumo (pasta custo horário) ou pela opção “Calcular Custo Horário” (Aba Orçamento | Insumo).

A planilha de Custo horário de Equipamento e Mão de obra possuem algumas variáveis que serão acessadas pelo TOP no momento do calculo, essas variáveis podem ser definidas na planilha .Net, acessado o Menu-> Variáveis e escolhendo qual variável é necessária para o calculo.

Ao solicitar o calculo pelo cadastro de Insumo, o TOP substitui temporariamente as variáveis da planilha pelos valores dos campos livres informados no insumo, assim o usuário possui o calculo de custo por insumo.

**Os Valores de custo Horário Produtivo e Improdutivo são definidos pelas células informadas nos campos "Célula de Custo Horário Produtivo" e "Célula de Custo Horário Improdutivo".**

O Calulo de custo também poderá ser feito através de um processo definido no menu Insumo, este processo encarrega de calcular o custo de todos os insumos de equipamento e mão de obra que possuem planilha RM vinculada. 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
