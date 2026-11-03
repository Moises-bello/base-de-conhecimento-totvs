---
content_hash: a91f57e2f6241c7a69676da96dc67bd014392142e592504404b4d167bed18264
fetched_at: '2026-06-29T00:10:22.555390+00:00'
page_id: '497211952'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Faturamento > Particular e Convênios > Outros > Encerramento
  Automático de Contas sem Débitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497211952
version: 10
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela de Processo de encerramento de conta sem débito**
4. **Tabelas utilizadas**
5. **Processo de utilização**

## **01. VISÃO GERAL**

Esta funcionalidade permiti o encerramento automático de contas sem débitos da seguinte forma:

* Contas manualmente selecionadas pelo usuário na tela de visão;
* Contas do tipo de atendimento retorno de forma automática;

Disponibilizado a partir da versão 12.1.25.

## **02. EXEMPLO DE UTILIZAÇÃO**

É possível agendar**\*** a execução do processo para que não seja necessário intervenção do usuário no encerramento das contas diariamente.

**\*Agendamento disponível apenas em ambiente três camadas ou Simulação de ambiente três camadas local.IMPORTANTE!**

## **03. TELA DO PROCESSO DE ENCERRAMENTO DE CONTA SEM DÉBITO**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| 1 - Contas selecionadas anteriormente na tela de visão | Nesta ação serão processadas as contas previamente selecionadas manualmente pelo usuário na tela de visão. |
| 2 - Contas de atendimentos com status de retorno (automático) | Nesta ação sistema processará todas as contas de atendimentos com status de retorno automaticamente. |

## **04. TABELAS UTILIZADAS**

* SZATENDIMENTO
* SZPARCIALATEND
* SZATENDHONORARIO
* SZATENDMATMED
* SZATENDSADT

## **05.** **PROCESSO DE UTILIZAÇÃO**

* Menu Faturamento / Particular e Convênios / Encerramento de Contas sem Débitos

* Utilize o filtro desejado

* A partir desta etapa há duas opções:
  + Encerrar as contas que serão previamente selecionadas na tela de visão
    - Nesta opção as contas previamente selecionadas serão processadas e encerradas.
  + Encerrar as contas de atendimentos de retorno de forma automática
    - Nesta opção, o sistema irá buscar as contas de atendimentos de retorno automáticamente e processar as mesmas para encerrá-las

## **05.1** **PROCESSO DE UTILIZAÇÃO - CONTAS SELECIONADAS PREVIAMENTE NA TELA DE VISÃO**

* Na tela de visão marque as contas que deseja processar / Menu Processos / Processo de Encerramento de Conta Sem Débito

* Na opção **Tipo de Contas** opte por **Contas selecionadas anteriormente na tela de visão /** botão **Executar**

* Ao final do processamento a tela de execução concluída será apresentada
  + 1 - Log de contas que foram encerradas
  + 2 - Log de contas que não foram encerradas e precisam ser verificadas

* Ao fechar a tela de execução concluída as contas que foram processadas com sucesso terão seu status apresentado como **Faturada**.

## **05.2** **PROCESSO DE UTILIZAÇÃO - CONTAS DE ATENDIMENTOS COM STATUS DE RETORNO**

* Neste cenário de exemplo apresenta-se uma conta sem débito na qual o atendimento está em status de retorno
  + Para verificar o status de retorno de uma conta é necessário pesquisá-la no registro de atendimento
    - Menu Atendimento / Pronto Atendimento - Ambulatório / Registro de Atendimento Externo
    - Na lista de atendimento é possível verificar que a conta está com status **Em aberto/ Retorno**
* Na tela de visão observe que a conta do cenário exemplo é apresentada, neste caso não é necessário marcá-la

* Menu Processos / Processo de Encerramento de Conta Sem Débito
* Na opção **Tipo de Contas** opte por **Conta de Atendimentos com Status de Retorno (automático) /** botão **Executar**

* Ao final do processamento a tela de execução concluída será apresentada
  + 1 - Log de contas que foram encerradas
  + 2 - Log de contas que não foram encerradas e precisam ser verificadas

* Ao fechar a tela de execução concluída as contas que atendem o critério de status de retorno são processadas com sucesso e terão seu status apresentado como **Faturada**.

## **05.3** **PROCESSO DE UTILIZAÇÃO - AGENDAMENTO**

* Por tratar-se de um processo, o mesmo pode ser agendado para execução recorrente sem a necessidade diária de intervenção por parte do usuário
* Quando disponibilizado ao final do processo antes da execução a tela de agendamento é apresentada

A etapa de agendamento só é apresentada quando o ambiente está configurado para utilizar três camadas ou simular três camadas local. Para mais informações sobre configuração de ambiente três camadas consulte a seguinte documentação: http://tdn.totvs.com/pages/viewpage.action?pageId=266969509IMPORTANTE!

]]>
