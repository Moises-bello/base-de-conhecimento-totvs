---
content_hash: b5a51dd61b583b74738deb349ee7abda5aabded4563b1472edef5dea90ebc254
fetched_at: '2026-06-29T00:05:47.082582+00:00'
page_id: '1005899520'
product: rm
source: tdn-rm
title: Cópia de Hierarquias entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1005899520
version: 22
---

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Gestão de Pessoas (VITAE) |
| Versão: | 12.1.2510 ou Superior. |

O processo de Cópia de Hierarquias entre coligadas permite copiar uma ou mais hierarquias entre coligadas.

Para garantir o correto funcionamento do processo de cópia de hierarquia entre coligadas, é fundamental que os seguintes pré-requisitos e comportamentos do sistema sejam observados.

## **01.** **PRÉ-REQUISITOS**

Antes de executar o processo de cópia de hierarquias, certifique-se de que os seguintes pré-requisitos foram atendidos:

* A **coligada de destino** deve ter a **Gestão de Hierarquia habilitada**, assim como a **coligada de origem**.

## **02.** **COMPORTAMENTO DA ROTINA DE CÓPIA**

A rotina de cópia de hierarquia foi desenvolvida para permitir e executar as seguintes ações:

* **Seleção Múltipla:** Permite a seleção de **uma ou mais hierarquias** para serem copiadas.
* **Inclusão Automática:** A hierarquia copiada será automaticamente incluída nas coligadas de destino selecionadas ao final do processo.
* **Criação de Níveis:** Caso o nível da hierarquia copiada não exista na coligada de destino, ele será **criado automaticamente**.
* **Alteração e Sobrescrita:** Permite a alteração (sobrescrita) das hierarquias que já existem nas coligadas de destino.
* **Criação de Histórico:** Será criado o histórico da hierarquia na coligada de destino.
* **Hierarquias Filhas:** Ao executar o processo de cópia de uma hierarquia **Pai**, **todas as suas hierarquias filhas** também serão copiadas, sobrescritas e atualizadas automaticamente conforme parametrização do processo.
* **Processamento da Estrutura:** Ao manipular uma hierarquia **Pai**, todas as suas hierarquias filhas também serão alteradas e replicadas conforme a estrutura da coligada de origem em todas as coligadas de destino selecionadas no processo.

Atenção a Opção de Sobrescrita

A seleção da opção de **Sobrescrever** uma hierarquia existente na coligada de destino é uma ação que deve ser utilizada com cautela, pois pode acarretar as seguintes consequências:

* **Perda de Históricos:** Perda de registros de históricos associados às hierarquias anteriores.
* **Perda de Dados Associados:** Perda de dados ou associações vinculadas às hierarquias previamente existentes.
* **Ajuste de Associações:** Perda ou ajuste nos registros de Pessoas e/ou Coligadas Externas que estavam associados às hierarquias anteriores, sendo reajustados conforme a nova estrutura.

**Certifique-se de que a substituição das hierarquias é realmente necessária antes de prosseguir com a execução do processo, uma vez executado os registros pai e filhos serão atualizados assim como os seus anexos e este processo é irreversível.**

## **03.** **ETAPAS DE EXECUÇÃO DO PROCESSO: CÓPIA DE HIERARQUIA ENTRE COLIGADAS**

1fade

A seguir, estão os passos detalhados para a execução do processo de cópia de hierarquia entre coligadas:

1Seleção e Início do Processo

### 1. Seleção e Início do Processo

1. **Selecione os Registros:** No cadastro da hierarquia, escolha e selecione os registros (hierarquias) que você deseja copiar.
2. **Acesse o Menu de Processos:** Vá até o menu **PROCESSOS** e selecione a opção: **“Processo Cópia de Hierarquia entre Coligadas”**.
3. **Assistente de Boas-Vindas:** Avance pela tela de Boas-Vindas do Assistente de Cópias de Hierarquias entre Coligadas.

2Configuração e Parâmetros

### 2. Configuração dos Parâmetros da Cópia

Nesta etapa, você deverá configurar os parâmetros necessários para a execução:

* **Coligada(s) de Destino:** Selecione a(s) coligada(s) para onde a hierarquia será copiada.
* **Opção de Sobrescrita:** Selecione se os registros encontrados serão **Sobrescritos**.

  + **Atenção:** Ao marcar a opção "Sobrescrever", as hierarquias existentes na coligada de destino serão atualizadas, assim como os registros filhos e registros correlatos selecionados.
* **Registros Correlatos para Cópia:** Selecione os anexos e registros correlatos que você deseja incluir no processo:

  + Pessoa / Coligada Externa
  + Substituto
  + Copiar Somente Hierarquia Selecionada
    - Ao habilitar este parâmetro, a operação de cópia ou sobrescrita atualizará **exclusivamente** a hierarquia selecionada, mantendo seus registros filhos inalterados no destino.
* Após a configuração, clique em **Avançar**.

Importante

***Alerta de Sobrescrita:** Confirmação dos Riscos e Implicações da Ação*

3Execução

### 3. Execução

1. **Execute o Processo:** Na tela final do assistente, clique em **Executar** para iniciar a cópia.

4Resultado

### 4. Resultado

**Resultado do Processo:**

* Ao copiar ou sobrescrever, os dados da hierarquia cadastrada serão levados para a coligada de destino.

* Os níveis hierárquicos existentes na coligada de destino serão **criados** ou **substituídos** conforme o cadastro da coligada de origem.

* Se, na tela de parâmetros, estiver marcada a opção "**Pessoa / Coligada Externa**" e/ou "**Substituto**", esses anexos também serão incluídos ou atualizados na cópia.

## **04. VALIDAÇÕES E CENÁRIOS DE INCONSISTÊNCIAS NA CÓPIA DE HIERARQUIAS**

2101-Hierarquia Existente

Essa mensagem ocorre ao executar o processo sem a opção "Sobrescrever" marcada, quando já existe uma hierarquia na coligada de destino com o mesmo **ID**.

**Tratativa:**

Marcar a opção **sobrescrever** ao executar o processo ou realizar os devidos ajustes na coligada de destino.

202-Nível Hierárquico Existente

Essa mensagem é exibida ao executar o processo **sem a opção "Sobrescrever" marcada**, quando já existe um nível hierárquico na coligada de destino com o **mesmo ID**.

**Tratativa:**

Marcar a opção **sobrescrever** ao executar o processo ou realizar os devidos ajustes na coligada de destino.

303-Gestão de Hierarquia Não Habilitada

Essa mensagem ocorre quando o processo é executado e a coligada de destino **não possui a Gestão de Hierarquia habilitada**.

**Tratativa:**

Acessar a coligada de destino e habilitar a [Hierarquia por posição.](https://tdn.totvs.com/pages/viewpage.action?pageId=653572529)

404-Código de externo já existente

Essa mensagem aparece quando **já existe um externo na coligada de destino com o mesmo código de externo** que está sendo copiado.

**Mensagem exibida:**

*"Externo já cadastrado na coligada destino!*

*Detalhes: Externo da coligada de origem: 6 | Código Externo: 00001*

*Já cadastrado na coligada destino 1 com outro código de pessoa."*

**Tratativa:**

Não é possível copiar automaticamente o externo, pois já existe um com o **mesmo código de externo** na coligada de destino.

Você deve:

1. **Criar o externo manualmente** na coligada de destino.
2. **Ajustá-lo na estrutura hierárquica** conforme necessário.

505-Coligada da Chapa

Essa mensagem ocorre quando você tenta copiar uma **Pessoa de outra Coligada**, mas seleciona como destino **a mesma coligada onde essa pessoa é locada.**

**Exemplo:**

Na **Coligada 01**, existe um registro de pessoa (funcionário) vinculado à **Coligada Externa 06**.

Ao tentar copiar esse registro para a **Coligada 06**, o sistema impede a cópia, pois a pessoa **é funcionário alocado** a essa coligada.

**Mensagem exibida:**

*"Pessoa/Coligada Externa: 6 | Hierarquia: 14 | Chapa: 00001 inválida! - Detalhes: A coligada da chapa não pode ser a mesma da coligada de origem. A pessoa não foi copiada para a coligada de destino."*

**Tratativa:**

Esse funcionário **não pode ser cadastrado como "Pessoa de outra Coligada"** em uma coligada onde ele **já pertence diretamente**.

606-Regras Substituto

Esse erro é exibido porque, na execução do processo, foi marcada a opção de cópia do Substituto e, na hierarquia de destino (Hierarquia 07), o substituto está vinculado a outra hierarquia (Hierarquia 2). Dessa forma, na coligada de destino (Coligada 07), é necessário copiar também a Hierarquia 2 com o respectivo registro de Pessoa/Coligada Externa, ou já existir, nessa coligada de destino, uma Pessoa/Coligada Externa previamente vinculada à Hierarquia 2.

**Mensagem exibida:**

### RESUMO DE ERROS ###

- Erro ao validar regras de negócio do substituto de ID: 4 e hierarquia substituta: 2. - Detalhes: coligada destino: 7 | hierarquia: 7 - Diretor Marketing  | ID Substituição: 4 | Erro: Atenção! Para definir o substituto a hierarquia/posição deve possuir um funcionário vinculado.

Erro ao executar processo!

Cópia Hierarquias entre coligadas finalizada.

**Tratativa:**

Na coligada de destino (**Coligada 07**), é necessário copiar também a **Hierarquia 2** com o respectivo registro de **Pessoa/Coligada Externa**, ou já existir, nessa coligada de destino, uma **Pessoa/Coligada Externa** previamente vinculada à **Hierarquia 2**.

**Links Importantes e Complementares:**
