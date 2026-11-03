---
article_id: 1500010494141
category: SIGAEST - CUSTOS
content_hash: 7de38bee4c53f6293d7ca00ec40f61029f0976c5cfc740e0a154b90ad85785f2
fetched_at: '2026-06-28T22:39:02.168722+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Exemplo
  prático de Execução Automática da Rotina
type: support-article
updated_at: '2025-03-12T12:23:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010494141-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Exemplo-pr%C3%A1tico-de-Execu%C3%A7%C3%A3o-Autom%C3%A1tica-da-Rotina
---

**Dúvida**Quais os passos práticos para conseguir configurar a execução automática (EXECAUTO) da rotina de Recálculo do Custo Médio (MATA330)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17  
  
**Solução**

Antes de entrarmos no mérito prático, para ter maiores detalhes sobre o que deve ser previamente configurado e ter ciência antes de programar o uso da rotina MATA330 de forma automática, **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060477354-MP-SIGAEST-MATA330-EXECAUTO-Execu%C3%A7%C3%A3o-Autom%C3%A1tica-da-rotina)**

**Exemplo prático de execução da rotina MATA330 - Recálculo do Custo Médio**

|  |
| --- |
| #INCLUDE "RWMAKE.CH" #INCLUDE "TBICONN.CH"  User Function JOBM330() Local lCPParte := .F. //-- Define que não será processado o custo em partes Local lBat := .T. //-- Define que a rotina será executada em Batch Local aListaFil := {} //-- Carrega Lista com as Filiais a serem processadas Local cCodFil := '' //-- Código da Filial a ser processada Local cNomFil := '' //-- Nome da Filial a ser processada Local cCGC := '' //-- CGC da filial a ser processada Local aParAuto := {} //-- Carrega a lista com os 21 parâmetros  ConOut(Repl("-",80)) ConOut(PadC("Rotina Recalculo Custo Medio",80)) ConOut(PadC("Conectando Ambiente.....",80))  PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "EST" TABLES "AF9","SB1","SB2","SB3","SB8","SB9","SBD","SBF","SBJ","SBK","SC2","SC5","SC6","SD1","SD2","SD3","SD4","SD5","SD8","SDB","SDC","SF1","SF2","SF4","SF5","SG1","SI1","SI2","SI3","SI5","SI6","SI7","SM2","ZAX","SAH","SM0","STL"  ConOut(PadC("Ambiente Conectado com Sucesso...",80)) ConOut(Repl("-",80))  Conout("Início da execução do JOBM330")  //-- Adiciona filial a ser processada dbSelectArea("SM0") dbSeek(cEmpAnt)  Do While ! Eof() .And. SM0->M0\_CODIGO == cEmpAnt  cCodFil := SM0->M0\_CODFIL cNomFil := SM0->M0\_FILIAL cCGC := SM0->M0\_CGC //-- Somente adiciona a Filial 01 If cCodFil == "01"  //-- Adiciona a filial na lista de filiais a serem processadas Aadd(aListaFil,{.T.,cCodFil,cNomFil,cCGC})  EndIf dbSkip()  EndDo  //-- Executa a rotina de recálculo do custo médio MATA330(lBat,aListaFil,lCPParte, aParAuto) ConOut("Término da execução do JOBM330")  Return |

**Outras informações:**

* aListaFil,{PARAMIXB[1],PARAMIXB[2],PARAMIXB[3],PARAMIXB[4]})

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Nome** | **Tipo** | **Descrição** | **Default** | **Obrigatório** |
| PARAMIXB[1] | Lógico | Execução em Batch?: .T.(Sim) / .F.(Não). |  | X |
| PARAMIXB[2] | Vetor | Lista com as filiais a serem consideradas (Batch). |  | X |
| PARAMIXB[3] | Lógico | Usa custo em partes?: .T.(Sim) / .F.(Não). |  |  |
| PARAMIXB[4] | Array | Coleção de elementos contendo os parâmetros de execução da rotina |  |  |

* Parâmetros:

  aParAuto :  
  MV\_PAR01 = Data Limite Final  
  MV\_PAR02 = Mostra lanctos. Contábeis  
  MV\_PAR03 = Aglutina Lanctos Contábeis  
  MV\_PAR04 = Atualizar Arq. de Movimentos  
  MV\_PAR05 = % de aumento da MOD  
  MV\_PAR06 = Centro de Custo  
  MV\_PAR07 = Conta Contábil a inibir de  
  MV\_PAR08 = Conta Contábil a inibir até  
  MV\_PAR09 = Apagar estornos  
  MV\_PAR010 = Gerar Lancto. Contábil  
  MV\_PAR011 = Gerar estrutura pela Moviment  
  MV\_PAR012 = Contabilização On-Line Por  
  MV\_PAR013 = Calcula mão-de-Obra  
  MV\_PAR014 = Método de apropriação  
  MV\_PAR015 = Recalcula Nível de Estrut  
  MV\_PAR016 = Mostra sequência de Cálculo  
  MV\_PAR017 = Seq Processamento FIFO  
  MV\_PAR018 = Mov Internos Valorizados  
  MV\_PAR019 = Recálculo Custo transportes  
  MV\_PAR020 = Cálculo de custos por  
  MV\_PAR021 = Calcular Custo em Partes

**E para etapa de Contabilização dos movimentos?**  
A rotina **MATA331** não teve sua criação para ser executada por Execauto() (Rotina automática).  
Não é recomendado devido que as rotinas podem sofrer mudanças internas em processos de melhorias e seus parâmetros podem mudar sem prévio aviso, o que pode fazer com que uma customização pare de funcionar, portanto não podemos fornecer um exemplo do que não é recomendado.

[Cross Segmento - Backoffice Linha Protheus - ADVPL - Existe ExecAuto() para o programa MATA331](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047674113-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Existe-ExecAuto-para-o-programa-MATA331?source=search)

**Saiba mais:**

*[MP - SIGAEST - MATA330 - EXECAUTO (Execução Automática) da rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060477354-MP-SIGAEST-MATA330-EXECAUTO-Execu%C3%A7%C3%A3o-Autom%C3%A1tica-da-rotina)*

*[MP - SIGAEST - Rotina MATA330 - Perguntas do Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805291-MP-SIGAEST-Rotina-MATA330-Perguntas-do-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
