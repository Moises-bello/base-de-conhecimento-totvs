---
content_hash: fdb586cf13a664198163cff2174215923d253c1b299646502be44f8791b54d7c
fetched_at: '2026-06-29T00:08:22.165111+00:00'
page_id: '269078444'
product: rm
source: tdn-rm
title: TWBTG2 ER Bloco K - Registros K260 e K265
type: documentation
url: https://tdn.totvs.com/display/LRM/TWBTG2+ER+Bloco+K+-+Registros+K260+e+K265
version: 140
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão do Planejamento e Controle da Produção | **Módulo** | Ordem de Produção |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | TWBTG2 | | |
| **País** | (X) Brasil | | |

   

### Objetivo

Efetuar a geração das Ordens de Produção de reprocessamento, e consequentemente possibilitar a geração dos Registros K 260 e K 265 do Bloco K, conforme disposto no Ato COTEPE/ICMS 7 de 13 de maio de 2016.

### Definição da Regra de Negócio

O Ato COTEPE/ICMS 7 de 13 de maio de 2016 altera a redação de alguns artigos do Ato COTEPE/ICMS 09/08, que dispõe sobre as especificações técnicas para a geração de arquivos da Escrituração Fiscal Digital - EFD, acrescentando alguns dispositivos ao Manual de Orientação do Leiaute da Escrituração Fiscal - EFD, entre eles os seguintes registros do Bloco K:

 

| Bloco | Descrição | Registro | Nível | Ocorrência | Obrigatoriedade do bloco (Todos os contribuintes) |
| --- | --- | --- | --- | --- | --- |
| K | Desmontagem de mercadorias – Item de Origem | K210 | 3 | 1:N | OC |
| K | Desmontagem de mercadorias – Item de Destino | K215 | 4 | 1:N | OC |
| K | Reprocessamento/Reparo de Produto/Insumo | K260 | 3 | 1:N | OC |
| K | Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas | K265 | 4 | 1:N | OC |
| K | Correção de Apontamento dos Registros K210, K220, K230, K250 e K260 | K270 | 3 | 1:N | OC |
| K | Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235, K255 e K265 | K275 | 4 | 1:N | OC |
| K | Correção de Apontamento – Estoque Escriturado | K280 | 3 | 1:N | OC |

### Reprocessamento

O reprocessamento trata-se de um ponto da maior relevância, pois afeta praticamente todas as indústrias. Com a inclusão desses novos registros no Bloco K, foi criada a possibilidade de apontamento do reprocessamento industrial, o que não poderia ser apresentado de forma assertiva no modelo anterior, visto que sempre exigia lista técnica e consumo mínimo, além do impedimento de utilização de um produto resultante como componente/insumo.

Essas informações foram divididas em dois registros:

* K260 – Reprocessamento de Produto/Insumo: Esse registro informa o produto que será reprocessado ou que foi reprocessado no período de apuração do registro K100 – Período de Apuração do ICMS/IPI, ou seja, informa os produtos que serão retirados do estoque para o devido reprocessamento;
* K265 – Reprocessamento – Mercadorias Consumidas e/ou Retornadas: Nesse registro é informado o consumo de mercadoria e/ou o retorno de mercadoria ao estoque, ocorrido no reprocessamento de produto/insumo informado no Registro K260 – Reprocessamento de Produto/Insumo – Produtos Acabados/Insumos, ou seja, esse registro trata da quantidade de insumos utilizados no reprocessamento, bem como do retorno de sobras, quando for o caso.

### Registro K 260: Reprocessamento de Produto / Insumo

Este registro tem o objetivo de informar o produto que será reprocessado ou que foi reprocessado no período de apuração do Registro K100.

As quantidades de saída ou retorno ao estoque devem ser expressas, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.

Quando houver identificação da ordem de produção ou serviço, a chave deste registro são os campos: COD\_OP\_OS e COD\_ITEM.

No caso em que a ordem de produção ou serviço não for identificada, o campo chave passa a ser COD\_ITEM.

  

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K260" | C | 004 | - | O |
| 02 | COD\_OP\_OS | Código de identificação da ordem de produção de reprocessamento | C | 030 | - | OC |
| 03 | COD\_ITEM | Código do produto/insumo a ser reprocessado ou já reprocessado (campo 02 do Registro 0200) | C | 060 | - | O |
| 04 | DT\_SAÍDA | Data de saída do estoque | N | 008\* | - | O |
| 05 | QTD\_SAÍDA | Quantidade de saída do estoque | N | - | 03 | O |
| 06 | DT\_RET | Data de retorno ao estoque (entrada) | N | 008\* | - | OC |
| 07 | QTD\_RET | Quantidade de retorno ao estoque (entrada) | N | - | 03 | OC |

Observações:

Nível hierárquico - 3  
Ocorrência – 1:N

Descrição dos campos do registro K260:

* Campo 01 (REG) - Valor Válido: [K260];

* Campo 02 (COD\_OP\_OS) – Preenchimento: informar o código de identificação da ordem de produção, no reprocessamento, caso exista. Validação: obrigatório se o campo DT\_RET não for preenchido e o campo DT\_SAÍDA estiver no período de apuração do K100;

* Campo 03 (COD\_ITEM) – Validação: o código do produto/insumo a ser reprocessado ou já processado deverá existir no campo COD\_ITEM do Registro 0200;

* Campo 04 (DT\_SAÍDA) - Validação: a data informada deve ser menor ou igual a DT\_FIN do registro K100;

* Campo 05 (QTD\_SAÍDA) – Preenchimento: não é admitida quantidade negativa;

* Campo 06 (DT\_RET) – Validação: a data deve estar compreendida no período de apuração – K100 e ser maior que DT\_SAÍDA;

  Campos 04 e 06 (DT\_SAÍDA e DT\_RET) – as datas de saída e retorno ao estoque do produto/insumo substituem, respectivamente, as datas de início e conclusão da ordem de produção/serviço;

* Campo 07 (QTD\_RET) – Preenchimento: não é admitida quantidade negativa. Validação: este campo será obrigatório caso o campo DT\_RET estiver preenchido.

### Registro K 265: Reprocessamento - Mercadorias Consumidas e/ou Retornadas

Este registro tem o objetivo de informar o consumo de mercadoria e/ou o retorno de mercadoria ao estoque, ocorridos no reprocessamento de produto/insumo informado no Registro K260.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.

A chave deste registro é o campo COD\_ITEM.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **Campo** | **Descrição** | **Tipo** | **Tam** | **Dec** | **Obrig** |
| 01 | REG | Texto fixo contendo "K265" | C | 004 | - | O |
| 02 | COD\_ITEM | Código da mercadoria (campo 02 do Registro 0200) | C | 060 | - | O |
| 03 | QTD\_CONS | Quantidade consumida – saída do estoque | N | - | 03 | OC |
| 03 | QTD\_RET | Quantidade retornada – entrada em estoque | N | - | 03 | OC |

Observações:

Nível hierárquico - 4  
Ocorrência – 1:N

Descrição dos campos do registro K265:

* Campo 01 (REG) - Valor Válido: [K265];

* Campo 02 (COD\_ITEM) – Validações: a) o código da mercadoria deverá existir no campo COD\_ITEM do Registro 0200;  
  b) o código da mercadoria deve ser diferente do código do produto/insumo reprocessado (COD\_ITEM do Registro K260);  
  c) o tipo da mercadoria (campo TIPO\_ITEM do Registro 0200) deve ser igual a 00, 01, 02, 03, 04, 05 ou 10;

* Campos 03 (QTD\_CONS) e 04 (QTD\_RET) – Preenchimento: não é admitida quantidade negativa. Validação: pelo menos um dos campos é obrigatório.

Para possibilitar a inclusão do processo de reprocessamento no TOTVS Gestão do Planejamento e Controle da Produção, foi realizada, na tela de abertura da Ordem de Produção, a criação do campo 'Ordem é de Reprocessamento?'. Com a implementação dessa informação, a rotina de criação da "Ordem de Prodção" passa a atender ao processo de reprocessamento, que é relativo aos Registros K260 e K265 do Bloco K do SPED Fiscal.

Quando da criação de uma Ordem de Produção, o campo 'Ordem é de Reprocessamento?' virá desmarcado, indicando que a Ordem de Produção que está sendo criada se trata de uma Ordem de Produção normal, ou seja uma Ordem de Produção de fabricação. Portanto, para utilizar o processo de Reprocessamento, será necessário marcar este campo.

Na Ordem de Produção de Reprocessamento deverá ser informada a estrutura que será reprocessada. O sistema irá permitir que seja efetuada a manutenção nos componentes e atividades dessa estrutura, para que sejam excluídos da Ordem de Produção aqueles que não serão utilizados no reprocessamento.

A partir daí será efetuado o processo normal de qualquer Ordem de Produção.

No registro K260 serão informados:

* Código da Ordem de Produção;
* Código do Item - Item a ser reprocessado, e que é obrigatoriamente uma estrutura;
* Data Saída – Data em que foi efetuada a saída da estrutura a ser reprocessada do estoque para a produção;
* Quantidade de Saída – Quantidade dessa estrutura que saiu do estoque e foi para a produção;
* Data Retorno – Data de término da Ordem de Produção;
* Quantidade de Retorno – Quantidade dessa estrutura que retornou ao estoque após o reprocessamento.

No registro K265 serão informados:

* Código do Item – Código do insumo que foi consumido ou retornado para o estoque após o reprocessamento (neste caso serão considerados todos os itens que estiverem na Ordem de Produção e que forem do tipo P - Produto);
* Quantidade Consumida – Quantidade consumida do insumo no reprocessamento;
* Quantidade Retornada – Quantidade do insumo que retornou ao estoque após o reprocessamento.

Irão gerar os registros K260 e K265 as Ordens de Produção com o status "concluída" e cuja data de conclusão esteja compreendida entre as datas inicial e final do período de apuração do SPED Fiscal (bloco K100).

Após a conclusão da Ordem de Produção, o conteúdo do campo 'Ordem é de Reprocessamento?' somente poderá ser alterado por um usuário que seja supervisor.

**Para realizar a implantação da funcionalidade na versão 12.1.14, é necessário executar o script****[SCRIPTBLOCOK210E260.ZIP](https://suporte.totvs.com/portal/p/10098/download)****disponível no pacote, já para as versões superiores à 12.1.14 não há necessidade de execução de script específico.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Ordem de Produção | Alteração | Produção > Ordem de Produção | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* KORDEM - Ordem de Produção

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
