---
content_hash: 28f96f49468be890649cd6beedc12a4e2a8891210a056196169a64f1f6f7b610
fetched_at: '2026-06-29T00:06:05.509549+00:00'
page_id: '201723266'
product: rm
source: tdn-rm
title: ER_migracao_relatorio_composicoes_custo_horario
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_relatorio_composicoes_custo_horario
version: 5
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6008 |
| **Requisito1** | PCREQ-6010 | **Subtarefa1** | PDR\_CP\_TOP007-1350 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Migração do relatório de composições de custo horário utiliando a Planilha.NET. 

## Definição da Regra de Negócio

* Serão listados na tela de filtro os insumos da coligada corrente, projeto corrente e que possuem o seguinte filtro: [“MISm.IdPlan <> zero” e “MIsm.CustoHorValorProd <>  nullo”], conforme consulta abaixo:

SELECT IDISM, CODISM, DESCISM, GRUPODNER, IDPLAN, IDISM, CODISM, DESCISM, GRUPODNER, IDPLAN,

                   CLIVREVALOR1, CLIVREVALOR2,CLIVREVALOR3, CLIVREVALOR4,CLIVREVALOR5, CLIVREVALOR6,CLIVREVALOR7, CLIVREVALOR8,

                   CLIVREVALOR9, CLIVREVALOR15,CLIVREVALOR16, CLIVREVALOR17,CLIVREVALOR18, CLIVREVALOR19,CLIVREVALOR20, CLIVREVALOR21,

                   CLIVREVALOR22, CLIVREVALOR23,CLIVREVALOR24, CLIVREVALOR25

           FROM MISM (NOLOCK)

           WHERE (CODCOLIGADA = :CODCOLIGADA) AND

                 (IDPRJ = :IDPRJ) AND

                 (IDPLAN <> 0) AND

                 (CUSTOHORVALORPROD IS NOT NULL) 

**Obs:** as opções de filtro “Equipamentos” e “Mão de obra”, serão usadas para filtrar os registros da tabela consulta acima através do campo “GrupoDNER”; 

* Após selecionar os insumos(seleção obrigatória) e clicar  no botão “**Gerar**”, será enviado diretamente para impressora relatórios (um relatório para cada insumo selecionado) contendo informações recuperadas através do recálculo de uma planilha. Essa planilha será recuperada da tabela “GPlan – cadastro de planilhas do RM” através do campo “IdPlan” recuperado da tabela “MIsm.IdPlan”. Para efetuar o cálculo dessas planilhas de “Custo horário”, algumas informações do cadastro de insumos e dos parâmetros gerais são enviadas para essas planilhas substituindo as constantes presentes nessas planilhas do Solum, entre elas:

**a)** **Dados recuperados da tabela MIsm:** 

* Constante = "CISM " | Valor = Parametro.CODISM;
* Constante = "DISM " | Valor = Parametro.DESCISM;
* Constante = "QTDEISM" | Valor = [Somatório da quantidade recuperada da tabela MABCIsm.Quantidade (filtrada por coligada, id projeto, insumo)]
* Constante = "CLI1" | Valor = MIsm.CLIVREVALOR1;
* Constante = "CLI2" | Valor = MIsm.CLIVREVALOR2;
* Constante = "CLI3" | Valor = MIsm.CLIVREVALOR3;
* Constante = "CLI4" | Valor = MIsm.CLIVREVALOR4;
* Constante = "CLI5" | Valor = MIsm. CLIVREVALOR5;
* Constante = "CLI6" | Valor = MIsm.CLIVREVALOR6;
* Constante = "CLI7" | Valor = MIsm.CLIVREVALOR7;
* Constante = "CLI8" | Valor = MIsm.CLIVREVALOR8;
* Constante = "CLI9" | Valor = MIsm.CLIVREVALOR9;
* Constante = "CLI10" | Valor = MIsm. CLIVREVALOR15;
* Constante = "CLI11" | Valor = MIsm.CLIVREVALOR16;
* Constante = "CLI12" | Valor = MIsm.CLIVREVALOR17;
* Constante = "CLI13" | Valor = MIsm.CLIVREVALOR18;
* Constante = "CLI14" | Valor = MIsm.CLIVREVALOR19;
* Constante = "CLI15" | Valor = MIsm. CLIVREVALOR20;
* Constante = "CLI16" | Valor = MIsm.CLIVREVALOR21;
* Constante = "CLI17" | Valor = MIsm.CLIVREVALOR22;
* Constante = "CLI18" | Valor = MIsm.CLIVREVALOR23;
* Constante = "CLI19" | Valor = MIsm.CLIVREVALOR24;
* Constante = "CLI20" | Valor = MIsm. CLIVREVALOR25;

**b)** **Dados recuperados da tabela de parâmetros (MParametro):** 

* Constante = "CLP1" | Valor = Parametro.CLIVREVALOR1PAR;
* Constante = "CLP2" | Valor = Parametro.CLIVREVALOR2PAR;
* Constante = "CLP3" | Valor = Parametro.CLIVREVALOR3PAR;
* Constante = "CLP4" | Valor = Parametro.CLIVREVALOR4PAR;
* Constante = "CLP5" | Valor = Parametro.CLIVREVALOR5PAR;
* Constante = "CLP6" | Valor = Parametro.CLIVREVALOR6PAR;
* Constante = "CLP7" | Valor = Parametro.CLIVREVALOR7PAR;
* Constante = "CLP8" | Valor = Parametro.CLIVREVALOR8PAR;
* Constante = "CLP9" | Valor = Parametro.CLIVREVALOR9PAR;
* Constante = "CLP10" | Valor = Parametro.CLIVREVALOR10PAR;
* Constante = "CLP11" | Valor = Parametro.CLIVREVALOR11PAR;
* Constante = "CLP12" | Valor = Parametro.CLIVREVALOR12PAR;
* Constante = "CLP13" | Valor = Parametro.CLIVREVALOR13PAR;
* Constante = "CLP14" | Valor = Parametro.CLIVREVALOR14PAR;
* Constante = "CLP15" | Valor = Parametro.CLIVREVALOR15PAR;
* Constante = "CLP16" | Valor = Parametro.CLIVREVALOR16PAR;
* Constante = "CLP17" | Valor = Parametro.CLIVREVALOR17PAR;
* Constante = "CLP18" | Valor = Parametro.CLIVREVALOR18PAR;
* Constante = "CLP19" | Valor = Parametro.CLIVREVALOR19PAR;
* Constante = "CLP20" | Valor = Parametro.CLIVREVALOR20PAR;

Ele poderá ser acessado da seguinte forma: 

* No menu Relatórios -> Composições -> Composições de custo horário.

Será disponibilizado no formulário de impressão do relatório a opção de "Enviar para impressora". Quando esta opção estiver selecionada o processo irá enviar direto para impressora padrão instalada, todas as planilhas associadas aos insumos selecionados. Caso este parâmetro não estiver selecionado, o relatório irá exibir para o usuário as planilhas, exibindo cada insumo por vez.

**Restrições** 

* As planilhas do RM Solum cadastradas atualmente na ferramenta de planilhas Delphi deverão ser convertidas para a nova ferramenta de planilhas da RM utilizando o executável MigradorPlan.exe.

## Protótipo de Tela

**Protótipo 01**

* **Equipamentos e Mão de obra:** informação para filtrar a tabela MIsm através do campo DNER.
* **Relação de insumos a serem impresso.**

### Protótipo 2

**Planilha de custo horário de equipamentos**

**Planilha de custo horário de Mão de obra**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
