---
content_hash: 963a7100ddeb8a3ffa2344bc7c5d996d0df46b5f23cab0572bd614b69620874f
fetched_at: '2026-06-29T00:12:07.396894+00:00'
page_id: '925343696'
product: rm
source: tdn-rm
title: Visualizações dos dentes no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925343696
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Visualização de Dentes**
   2. **Visualização das Faces dos Dentes**
   3. **Visualização do Estado dos dentes**

sumarioVisão Geral

## **01. VISÃO GERAL**

Este documento descreve a implementação do novo menu "Odontologia" no sistema RM.  
O menu possui tres telas para visualização de informações odontológicas sem  
possibilidade de edição ou inclusão de novos dados.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Visualização dos Dentes, Visualização das Faces dos dentes e Visualização do Estado dos Dentes

**Acesso**

* Menu de navegação: RM > Cadastros > Odontologia

**O menu "Odontologia" contém tres telas:**

MenusVisualização de Dentes Cadastrados

# **Visualização de Dentes Cadastrados**

Esta tela exibe uma tabela com os dentes cadastrados no sistema internacional (FDI). Os dados foram previamente preenchidos e não podem ser editados, excluídos ou novos dados adicionados.

**Colunas da tabela:**

* **Número do Dente**: Identificação numérica do dente segundo o sistema FDI.
* **Nome do Dente**: Nome correspondente ao dente.
* **Quadrante do Dente**: Quadrante ao qual o dente pertence.
* **Tipo de Dente**: Informa se o dente é permanente ou decíduo.

Visualização das Faces dos Dentes

# **Visualização das Faces dos Dentes**

Esta tela apresenta uma tabela com as faces dos dentes cadastradas no sistema. Assim como a tela anterior, os dados são apenas para visualização.

**Colunas da tabela:**

* **Sigla da Face do Dente**: Código ou sigla representando a face do dente.
* **Nome da Face do Dente**: Nome descritivo da face do dente.

Visualização do estado dos dentes

## **03. VISUALIZAÇÃO DO ESTADO DOS DENTES**

**Comportamento da Tela**

* Apresenta uma **lista ou grid** com todos os registros de estados dos dentes cadastrados.
* Cada linha representa um estado do dente com as seguintes colunas:

+ **Estado**

* A interface **não possui botões de ação** para adicionar, editar ou excluir registros.

**Permissões**

A funcionalidade é **somente leitura**, não sendo necessário controle de permissões específicas além do acesso à tela

## **03. TERMOS PADRONIZADOS PARA ESTADO DO DENTE**

| **Estado** |
| --- |
| ✅ Hígido |
| ✅ Restaurado |
| ✅ Cariado |
| ✅ Extração Indicada |
| ✅ Ausente |
| ✅ Implante |

# 

## **03.** **Restrições e Funcionalidades**

* Os dados foram preenchidos automaticamente durante a criação do sistema.
* Nenhum dado pode ser editado, excluído ou inserido manualmente.
* As telas são exclusivamente para visualização das informações odontológicas.

## **04.** **Considerações Finais**

O menu "Odontologia" foi projetado para facilitar o acesso às informações odontológicas cadastradas no sistema, garantindo que os dados sejam apresentados de forma estruturada e padronizada sem possibilidade de alteração.
