---
content_hash: 62dd4f8dfdb9e0c452ab5c2a158e4ae044bf6cadf3972d7cedffd89e1f0c8cb8
fetched_at: '2026-06-29T00:11:25.673088+00:00'
page_id: '714243501'
product: rm
source: tdn-rm
title: Configurador De/Para de empresas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=714243501
version: 26
---

Atenção

Recurso disponível na release 12.1.2302 ou superior.

## **01. VISÃO GERAL**

Inclusão ou alteração de De/Para de empresas para integrações de EAI dos pacotes TOTVS CRM e NG Quírons com BackOffice RM.

Será alimentado apenas o De/Para do lado da linha RM. Para as demais integrações existentes caso seja executado esta rotina, no sistema de destino os de/paras precisaram ser criados manualmente para cada empresa.

## **02. EXEMPLO DE UTILIZAÇÃO**

1. No módulo de  Gestão de Estoque, Compras e Faturamento em **Integrações → Integrações com Parceiro** selecione a opção do **Configurador De/Para de Empresas.**
2. Será aberto uma janela contendo a visão abaixo.
3. No campo de seleção de pacotes da integração serão exibidos todos os pacotes ativos de integração cadastrados no seu ambiente.  
   O primeiro passo para utilização deste recurso é a definição do pacote para o qual será feita a inclusão/alteração do De/Para.  
     
   *Obs.: Este campo ficará desativado quanto não houver pelo menos um pacote da integração ativo no ambiente, apresentando a seguinte mensagem:*
4. Informe a coligada e Filial do RM assim como a Empresa e Filial do sistema para o qual será feita a integração.
5. Clique no botão **Adicionar De/Para**.
6. Na região abaixo serão exibidos todos os De/Paras cadastrados, ou seja, será possível realizar a inclusão de várias De/Paras, conforme a necessidade.
7. Após o cadastro de todos os De/Paras desejados, clique no botão **Executar** e a ação será realizada.  
   *Obs.: O botão de execução ficará desativado quando ainda não tiver sido selecionado um pacote da integração ou quando não houver pelo menos um De/Para cadastrado.*

## **03. TABELAS UTILIZADAS**

* GEAIAPP
* GEAIPACOTEINSTALADO
* GEAIDEPARA
