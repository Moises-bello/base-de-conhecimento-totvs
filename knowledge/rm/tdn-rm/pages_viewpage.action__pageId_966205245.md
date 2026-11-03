---
content_hash: fd13d878468e8b3bbb0ff82fe63014ed3712442912df0d674aa06f447bc30a5d
fetched_at: '2026-06-29T00:12:14.161310+00:00'
page_id: '966205245'
product: rm
source: tdn-rm
title: DT - Hierarquias - Cópia de hierarquias entre coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=966205245
version: 13
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Hierarquias - Cópia de hierarquias entre coligadas |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-14931](https://jiraproducao.totvs.com.br/browse/DRHHCM-14931https://jiraproducao.totvs.com.br/browse/DRHHCM-14931) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir do release:

* 12.1.2510

## **03. SITUAÇÃO/REQUISITO**

* **Funcionalidades da Rotina de Cópia de Hierarquias:**

  + Permitir a seleção de uma, várias ou todas as hierarquias para cópia.
  + Permitir a **inclusão** da hierarquia nas coligadas selecionadas. Caso o nível da hierarquia não exista na coligada de destino, ele será criado automaticamente.
  + Permitir a **alteração** (sobrescrita) das hierarquias já existentes nas coligadas de destino.
  + Permitir a seleção de um ou mais registros específicos para copiar.
  + Criar o histórico da hierarquia na coligada de destino.
  + Ao executar o processo de cópia de uma hierarquia, todas as hierarquias **filhas** também serão copiadas automaticamente.

## **04. SOLUÇÃO**

Criada processo para copia de hierarquias entre coligadas:

1true1Copiando EstruturaCopiando estrutura de hierarquia

**Demonstração da Cópia de Hierarquias:**

Selecione a hierarquia que deseja copiar e, em seguida, acesse:  
**Menu Processos** > **Processo: Cópia de Hierarquias entre Coligadas**

 

Selecione a(s) coligada(s) de destino > Avançar > Executar:

Aguarde a execução:

3Sobrescrevendo estruturaSobrescrevendo estrutura de hierarquia

A rotina também permite atualizar a estrutura da coligada de destino por meio da opção **Sobrescrever**.

Quando essa opção está selecionada, o processo atualiza as estruturas já existentes e cria aquelas que ainda não estão presentes na coligada de destino.

> ⚠️**Atenção:** Ao marcar a opção **Sobrescrever**, as hierarquias existentes na coligada de destino serão atualizadas.  
> Essa ação pode resultar na **perda de históricos ou dados associados** às hierarquias anteriores.  
> **Certifique-se de que essa substituição é realmente necessária antes de prosseguir.**

**Passos:**  
Selecione a(s) coligada(s) de destino > clique em **Avançar** > clique em **Executar**.

Aguarde a execução:

4Cenários de InconsistênciasCenários de Inconsistências

Segue a demonstração de alguns cenários de inconsistências apresentadas a cópia:

**01. Hierárquia existente**

A mensagem está relacionada ao executar o processo sem a opção sobrescrever marcada e a existencia de uma hierarquia no coligada destino com o mesmo ID:

**02. Nivel Hierarquico existente**

A mensagem está relacionada ao executar o processo sem a opção sobrescrever marcada e a existencia de um nivel hierarquico no coligada destino com o mesmo ID:

**03. Gestão de Hierarquia não habilitada**

A mensagem está relacionada ao executar o processo e a coligada destino não tenha a Gestão de hierarquia habilitada:

## **05. DEMAIS INFORMAÇÕES**

Não se aplica
