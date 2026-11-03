---
content_hash: 7c2ff6528f67342d24bb968c9198c7440035816b0944ed193f50a1b5e26bc5c0
fetched_at: '2026-06-29T00:12:09.126105+00:00'
page_id: '939252927'
product: rm
source: tdn-rm
title: Cadastro de Regras Tributárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939252927
version: 60
---

# Conteúdo

Conteúdonone

# 1. Visão Geral

O cadastro de Regras Tributárias foi criado com o propósito de facilitar a parametrização de cenários de tributação para a Reforma Tributária, permitindo criar regras específicas para os tributos do IVA (IBS e CBS).

false

* Esse cadastro está disponível à partir de ***Cadastros** > **Regras Tributárias***.

# 2. Informações sobre os campos

Tela do sistema

O cadastro é organizado em três pastas "**Identificação**", "**Detalhes Tributos**" e **"Regras de Seleção"**

CadastroIdentificaçãoIdentificação

| Campo | Descrição do Campo |
| --- | --- |
| **Coligada** | Define a coligada à qual a regra tributária pertence. Este campo só pode ser editado **durante a criação da regra**.  ⚠️ **Atenção:** Caso a coligada seja alterada após o início do cadastro (por exemplo, se a regra estiver em rascunho e não for salva antes), **todos os tributos já adicionados na aba *Detalhes dos Tributos e as regras adicionadas na aba Regras de Seleção* serão apagados automaticamente**, para garantir consistência com a nova coligada. |
| **Ativo** | Indica se a regra está ativa e pode ser aplicada nas operações. |
| **Código** | Código único da Regra Tributaria. |
| **Descrição** | Texto explicativo sobre a Regra Tributaria. |
| **Fórmula de base de Cálculo Fiscal** | Expressão ou referência usada para o cálculo da base fiscal.   * É possível vincular fórmulas para base de cálculo, do módulo Fiscal. |
| **Situação Tributária** | Código da situação tributária conforme Tabela publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica. |
| **Classificação Tributária** | Categoria que representa o tipo ou natureza da operação conforme Tabela publicada na aba “Documentos”, opção “Diversos” do Portal Nacional da Nota Fiscal Eletrônica. |
| **Regra Tributária Regular** | O campo **Regra Tributária Regular** deve ser preenchido quando a **tabela de CST/cClassTrib** publicada pelo Fisco indicar esta obrigação.  Deve ser associada outra Regra Tributária que contenha a parametrização da tributação numa operação "normal". Ela será utilizada para gerar o grupo "**gTribRegular - Grupo de informações da Tributação Regular**" na NF-e. Neste grupo serão geradas as informações da tributação que vai incidir na operação caso a condição resolutória dos tributos não seja cumprida.   Exemplo **CST 550 / cClassTrib 550002 - Regime de Trânsito:**Para este CST/cClassTrib, a administração tributária exige o preenchimento do grupo de tributação regular na NF-e.    Para que o sistema consiga gerar este grupo corretamente na NF-e, deve-se informar na Regra Tributaria  do Regime de Transito a Regra Tributária da tributação normal da operação. Digamos que seja uma mercadoria sujeita à redução de 60% da alíquota do IBS/CBS.  O Cadastro da Regra Tributária do regime de trânsito ficaria assim cadastrada:  → |
| **Inicio da Vigência** | Data a partir da qual a regra entra em vigor. |
| **Fim da Vigência** | Data limite para a validade da regra. Se em branco, considera-se uma vigência com fim indefinido. |

Detalhes TributosDetalhes Tributos

| Campo | Descrição do Campo |
| --- | --- |
| **Coligada** | Exibe a coligada herdada da aba **Identificação**.   * 🚫 Este campo **não pode ser editado** diretamente, pois os tributos disponíveis no lookup estão vinculados à coligada definida na regra principal. |
| **Tributo** | Seleção de um tributo previamente cadastrado.   * É possível adicionar **apenas um tributo** de cada tipo entre os seguintes: **IBS Municipal**, **IBS Estadual** ou **CBS**. * ⚠️ Este cadastro é **multicoligadas**, mas o lookup apresenta **somente os tributos cadastrados na coligada** informada no cadastro da regra tributária.  Para mais informações sobre o cadastro desses tributos, consulte: |
| **Tipo de tributação** | Define a forma de incidência do tributo nesta regra. |
| **% de Redução de alíquota** | Percentual de redução aplicado sobre a alíquota padrão do tributo. |
| **% do Diferimento** | Percentual do imposto diferido. |
| **Gera CashBack** | Indica se a operação gera direito a crédito devolutivo (cashback) para o contribuinte final. |
| **Código Crédito Presumido** | O campo indica o código correspondente ao Crédito Presumido, conforme definido em sua própria documentação.   * O campo **“Código Crédito Presumido”** possui seu valor é compartilhado entre os tributos **IBS** e **CBS**. Portanto, ao alterar o valor em um deles, a modificação será aplicada automaticamente aos demais.  Para mais informações sobre Crédito Presumido, consulte: |
| **% do Crédito Presumido** | O campo representa o Percentual do Crédito Presumido, correspondente ao **Código do Crédito Presumido** informado na coluna anterior.   * Nos casos em que os tributos forem **IBS Municipal** e **IBS Federal**, seus valores serão sempre iguais. Portanto, ao alterar um deles, a modificação será refletida automaticamente no outro. |
| **Deduz Crédito Presumido** | Indica se o valor do Crédito Presumido deve ser deduzido do valor total dos tributos.   * O campo **“Deduz Crédito Presumido”** possui seu valor é compartilhado entre os tributos **IBS** e **CBS**. Portanto, ao alterar o valor em um deles, a modificação será aplicada automaticamente aos demais.   ⚠️ Quando habilitado, o valor deduzido será refletido no XML da NF-e nas tags **`<vIBS>`** e **`<vCBS>`**. |

Regra de Seleção CamposRegra de Seleção

Nesta pasta serão definidos os critérios de dependência para as regras de seleção.

| Campo | Descrição do Campo |
| --- | --- |
| **Regra de Tributação** | Tipo de regra de seleção a ser vinculada na regra tributária. O tipo escolhido define o que estará disponível no campo **Valor Regra** |
| **Valor Regra** | 3leftEmpresa **Empresa**  A regra de Empresa irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal. Exemplo  Cliente/Fornecedor **Cliente/Fornecedor**  A regra de Cliente/Fornecedor irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal. Exemplo  Produto **Produto**  A regra de Produto irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal. Exemplo  Classificação fiscal de bens e serviços **Classificação Fiscal de Bens e Serviços**  A regra de Classificação Fiscal de Bens e Serviços faz parte do grupo Produto e irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal. Exemplo  Estado **Estado**  A regra de Estado irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal quando o estado correspondente estiver informado no local da operação. É possível informar mais de um estado na regra de seleção conforme exemplo, porém o sistema não permite registro duplicado, ou seja, não permite inserir o mesmo estado que já está na regra. Exemplo  Município **Município**  A regra de Município irá afetar na seleção da Regra Tributária do movimento e do lançamento fiscal quando o município correspondente estiver informado no local da operação. É possível informar mais de um município na regra de seleção conforme exemplo, porém o sistema não permite registro duplicado, ou seja, não permite inserir o mesmo município que já está na regra. Exemplo |
| **Regras Associadas** | Lista com as regras de seleção associadas na regra tributária |

# 3. Detalhes da Regra Tributária

Pastas da Regra Tributária

## 3.1. Regras de seleção

Regra de SeleçãoRegras de Seleção

As **regras de seleção** são um **conjunto de critérios** aplicados a um Movimento ou Lançamento Fiscal com o objetivo de determinar **qual regra tributária** deve ser usada. Estão disponíveis no sistema os seguintes grupos:

Grupos

|  |  |
| --- | --- |
| **Grupo** | **Dependência** |
| **A** | Estado |
| Município |
| **B** | Empresa |
| Cliente / Fornecedor |
| **C** | Produto |
| Classificação de Bens e Serviços |
| **D** | Tipo de Operação |

***⚠️ Observações*:**

* Elementos do Grupo A, exceto Estado, se relacionam com quaisquer elemento dos Grupos B, C e D.
Peso dos Grupos

Cada Regra de Seleção possui um peso associado, ou seja, para cada regra selecionada na regra tributária, esta se tornará mais ou menos seletiva.   
No momento da inclusão do lançamento fiscal, dependendo da regra de seleção na regra tributária parametrizada, o sistema irá listar as naturezas de maior peso, ou seja, as mais seletivas.

| Grupo | Dependência | Peso |
| --- | --- | --- |
| **A** | Estado | 100 |
| Município | 100 |
| **B** | Empresa | 100 |
| Cliente/Fornecedor | 100 |
| **C** | Produto | 100 |
| Classificação Fiscal de Bens e Serviços | 100 |
| **D** | Tipo de Operação | 10 |

Para saber sobre o **Serviço de seleção da Regra Tributária**, clique .

# 4. Processo: Cópia de Regras Tributárias (outras coligadas)

## 4.1. Sobre

Este processo possibilita ao usuário o reaproveitamento dos registros de regras tributárias que foram criadas e organizadas em uma coligada através da cópia para outras coligadas evitando assim retrabalho e erros.

## 4.2. Informações sobre a execução do processo

O processo pode ser acessado através do TOTVS Gestão Fiscal | *Cadastros | Regras Tributárias* e então na menu de processos *"Cópia de Regras Tributárias".*

Tela do sistema

Registros de Regras Tributárias

Acionamento do processo

Seleção das coligadas destino

## 4.3. Regras do processo de Cópia de Regras Tributárias

Para acessar o processo não há nenhuma regra específica que precise ser observada.

No caso da cópia — ou seja, a inclusão dos registros de regras tributárias nas demais coligadas — o sistema seguirá as regras definidas no cadastro de regras tributárias. Nas abas de *Detalhes Tributos* e *Regras de Seleção.* Caso já exista uma regra com o mesmo código na coligada de destino, não será copiado e será exibido no log.

**Aba: Identificação**

* Campos de fórmula fiscal, caso o código exista na coligada de destino, o registro será copiado;
  + Caso não exista, será registrado no log quando a fórmula não for encontrada na coligada de destino;
* O campo "Regra Tributária Regular" não é copiado.

**Aba: Detalhes dos tributos**

* Caso o código do tributo exista na coligada de destino, será copiado;
  + Caso não exista, será registrado no log quando o tributo não for encontrado na coligada de destino;

**Aba: Regras de seleção**

No contexto da regra tributária o processo é para coligadas distintas, ou seja, coligadas diferentes. Sendo assim, será realizado a cópia somente para as regras de seleção de *Localidade* (*Estado* e *Município) e Classificação de Bens e Serviço (NCM/NBS).*
