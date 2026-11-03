---
content_hash: 9ad21f3d8cf920500e848324794a8658cc4d90c84c05c9b5d7cf7c8c6fd982f3
fetched_at: '2026-06-29T00:09:07.743191+00:00'
page_id: '385844597'
product: rm
source: tdn-rm
title: DT_TOPEXECONTROL01-3360_ApropriaçãoRM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=385844597
version: 11
---

# Processo de Importação de Apropriação - Totvs Obras e Projetos x BackOffice RM Nucleus

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Controle e Execução |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Importação de Apropriações de Apropriações | PrjConsultaApropEaiProcAction / PrjConsultaApropEaiCronogramaAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cronograma Apropriado | PrjCronogramaAction | |  |  | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** | Parâmetros do Projeto (F6) -> Apropriação -> Geral    "Utiliza processo de importar apropriações BackOffice" "Campo Data de Apropriação: Movimentos  → Data de Emissão do movimento  → Data de Entrega do movimento  → Data de Entrega do item de movimento  Lançamentos Financeiros  → Data de Emissão  → Data da Baixa  → Data do vencimento  → Data da Previsão da Baixa  → Data de Criação  → Data do Pagamento" |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | TOPEXECONTROL01-3360 |
| **Tabelas Utilizadas:** | MAPROP |

## Descrição

A partir da ativação do parâmetro de importação de apropriações, sera disponibilizado processo para que as apropriações oriundas do BackOffice (TMOV, FLAN ..) sejam importadas para a tabela do TOP MAPROP. A partir disto sera possível consultar estas apropriações em uma tela de apropriações e como anexo de apropriações na planilha de atividades.

**Processo de Importação de Apropriações:**

**Executando através do botão "Importar Apropriações das Tarefas no BackOffice" do cronograma**

Este processo é executado somente para a tarefa relacionada ao cronograma e considerando a faixa de períodos dos parâmetros de projeto.

Quando executado para obra ou etapa, o sistema considera o primeiro e o último serviço na hierarquia do código da tarefa.

**Processo Importar Apropriações das Tarefas no BackOffice - Processo na planilha de Atividades**

Neste processo o sistema selecionará durante a execução todas as tarefas da planilha de atividades e o intervalo de períodos definidos nos parâmetros de projeto.

Executando e agendando o processo com parâmetro "Importar toda a Planilha" marcado.

 

Executando e agendando o processo com parâmetro "Importar toda a Planilha" desmarcado.

# Visão de Apropriação Discriminada

A visão de apropriações discriminada tem por objetivo mostrar de forma discriminada os registros correspondentes ao cronograma apropriado da planilha de atividades.

Podendo ser exibido como anexo a planilha de atividades ou para todo o projeto pelo executar "apropriações". Nesta visão serão exibidas as apropriações Medição de Contrato, Insumo / Serviços, Integração (Oriundas do BackOffice).[Apropriação Discriminada](http://tdn.totvs.com/pages/viewpage.action?pageId=301182692)

# Visão de Apropriação Anexo

O anexo de apropriações tem por objetivo mostrar de forma discriminada as apropriações referentes a tarefa selecionada.

Detalhes Técnicos - Apropriações BackOffice

| ORIGEMAPROP | TIPOAPROP | IDPRJ | IDTRF | QUANTIDADE | PRECOUNITARIO | VALORTOTAL | DATAAPROPRIACAO | MOEDA | CODCFO | IDPRD | CODUND | NUMERODOC | NUMEROITMDOC | IDISM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BackOffice | Movimento | TITMMOVRATCCU.IDPRJ | TITMMOVRATCCU.IDTRF | TITMMOV.QUANTIDADE | TITMMOV.PRECOUNITARIO | TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO \* TITMMOVRATCCU.PERCENTUAL / 100 | **Configurada** | TMOV.CODMOEDA | TMOV.CODCFO | TITMMOV.IDPRD | TITMMOV.CODUND | NUMEROMOV | NSEQITMMOV | JOIN TPRD COM MISMPRD |
| BackOffice | Titulo a Pagar | FLANRATCCU.IDPRJ | FLANRATCCU.IDTRF | 1 | FLANRATCCU.VALOR | FLANRATCCU.VALOR | Configurada | FLAN.CODMOEVALORORIGINAL | FLAN.CODCFO | Vazio | Vazio | FLAN.NUMERODOCUMENTO | VAZIO | VAZIO |
