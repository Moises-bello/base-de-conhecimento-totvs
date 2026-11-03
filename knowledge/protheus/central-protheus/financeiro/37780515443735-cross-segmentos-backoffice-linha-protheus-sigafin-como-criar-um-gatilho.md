---
article_id: 37780515443735
category: Financeiro
content_hash: b3722be4ab035a4fac833c964ff5517b441ccf8a27179dbe3d074e69c2cf20a8
fetched_at: '2026-06-28T22:38:00.909752+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como criar um gatilho?
type: support-article
updated_at: '2026-01-21T14:08:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37780515443735-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-criar-um-gatilho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37780515429015) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como criar um gatilho?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões.  
  
**Solução**  
No Metadado do **Microsiga Protheus**, existe o recurso que permite o **preenchimento automático de campos a partir da ação de outro campo**, sem a necessidade de criação de rotinas customizadas ou alteração das rotinas padrão do sistema.  
Esse comportamento é controlado por meio dos **gatilhos**, configurados diretamente no dicionário de dados.

O Protheus disponibiliza **três tipos de gatilho**, cada um com uma finalidade específica, conforme descrito a seguir.

## 1. Gatilho Primário

O **gatilho primário** é o tipo mais utilizado no sistema. Sua configuração exige apenas a definição do:

* Campo que disparará o gatilho
* Campo de destino (contra domínio)
* Regra de preenchimento

Após a validação do campo de disparo, o sistema preenche automaticamente o campo de contra domínio por meio da **macroexecução da regra definida**.

Quando o campo **X7\_SEEK** estiver configurado com o valor **“S”**, o sistema efetuará o posicionamento da tabela indicada. Nesse cenário, o campo **X7\_REGRA** pode conter o nome de um campo da tabela posicionada, cujo valor será atribuído ao campo de destino.

## 2. Gatilho Estrangeiro

O **gatilho estrangeiro** é responsável pelo preenchimento de um campo em uma tabela externa, definida pelo conjunto de parâmetros:

* **X7\_ALIAS**
* **X7\_ORDEM**
* **X7\_CHAVE**

Diferentemente do gatilho primário, esse tipo de gatilho **é executado apenas no momento da confirmação da tela**, e o preenchimento ocorre **diretamente na base de dados**, não atuando no buffer de memória.

## 3. Gatilho de Posicionamento

O **gatilho de posicionamento** é utilizado quando há necessidade de **posicionar uma tabela específica**, permitindo a recuperação de informações a partir de um determinado índice e chave definidos nos parâmetros do gatilho.

## Campos Utilizados na Configuração dos Gatilhos

A seguir, estão descritos os principais campos envolvidos na configuração dos gatilhos no Protheus:

| Campo | Tipo | Descrição |
| --- | --- | --- |
| **X7\_CAMPO** | Caracter | Campo que irá disparar o gatilho. Deve existir no SX3 e possuir o atributo **X3\_TRIGGER** configurado como “S”. |
| **X7\_SEQUENC** | Caracter | Sequenciador dos gatilhos vinculados a um mesmo campo. |
| **X7\_REGRA** | Caracter | Regra de preenchimento atribuída ao campo de destino (contra domínio). O conteúdo é macroexecutado e seu resultado é atribuído ao campo definido em **X7\_CDOMIN**. |
| **X7\_CDOMIN** | Caracter | Campo de destino (contra domínio) que receberá o valor resultante da execução da regra. |
| **X7\_TIPO** | Caracter | Tipo de gatilho. Valores aceitos: **P** (Primário), **E** (Estrangeiro) e **X** (Posicionamento). |
| **X7\_SEEK** | Caracter | Indica se haverá posicionamento de tabela. Valores aceitos: **“S”** (Sim) ou **“N”** (Não). |
| **X7\_ALIAS** | Caracter | Tabela que será posicionada durante a execução do gatilho. |
| **X7\_ORDEM** | Numérico | Número do índice que será utilizado para a pesquisa. |
| **X7\_CHAVE** | Caracter | Chave de pesquisa utilizada na tabela definida em **X7\_ALIAS**. O conteúdo é macroexecutado e o resultado é utilizado como chave de busca. |
| **X7\_CONDIC** | Caracter | Função condicional que determina se o gatilho deverá ou não ser executado. |
| **X7\_PROPRI** | Caracter | Prioridade do parâmetro: **“S”** para Sistema ou **“U”** para Usuário. |

**Importante**

Em caso de dúvidas, sugerimos o acionamento da equipe de suporte framework.

**O suporte padrão não presta auxílio na criação ou configuração de gatilhos. Esse processo deve ser analisado, validado e implementado pela equipe de TI da própria empresa ou através do HUB plataformas.**

Saiba mais

[**GATILHO**](https://tdn.totvs.com/display/public/PROT/ADV0001_GAT_COMO_CRIAR_UM_GATILHO)
