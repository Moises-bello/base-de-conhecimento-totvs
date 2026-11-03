---
content_hash: 935ba800cab906ccedfb5a113691fbfed2d1051fe2be5eed54f5cf31e839c07a
fetched_at: '2026-06-29T00:08:17.813709+00:00'
page_id: '258835509'
product: rm
source: tdn-rm
title: TVZXFP ER Bloco K - Registros K210 e K215
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZXFP+ER+Bloco+K+-+Registros+K210+e+K215
version: 154
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Estoque > Produção > Movimentação |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | TVZXFP | | |
| **País** | (x) Brasil. | | |

   

## Objetivo

Facilitar para o usuário a geração dos registros de movimentação interna de desmontagem de estruturas e consequentemente possibilitar a geração dos Registros K 210 e K 215 do Bloco K conforme disposto no Ato COTEPE/ICMS 7 de 13 de maio de 2016.

 

## Definição da Regra de Negócio

*O*Ato COTEPE/ICMS 7 de 13 de maio de 2016 altera a redação de alguns artigos do Ato COTEPE/ICMS 09/08, que dispõe sobre as especificações técnicas para a geração de arquivos da Escrituração Fiscal Digital - EFD, acrescentando alguns dispositivos ao Manual de Orientação do Leiaute da Escrituração Fiscal - EFD, entre eles os seguintes registros do Bloco K:

| Bloco | Descrição | Registro | Nível | Ocorrência | Obrigatoriedade do bloco (Todos os contribuintes) |
| --- | --- | --- | --- | --- | --- |
| K | Desmontagem de mercadorias – Item de Origem | K210 | 3 | 1:N | OC |
| K | Desmontagem de mercadorias – Item de Destino | K215 | 4 | 1:N | OC |
| K | Reprocessamento/Reparo de Produto/Insumo | K260 | 3 | 1:N | OC |
| K | Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas | K265 | 4 | 1:N | OC |
| K | Correção de Apontamento dos Registros K210, K220, K230, K250 e K260 | K270 | 3 | 1:N | OC |
| K | Correção de Apontamento e Retorno de Insumos dos Registros K215, K220, K235, K255 e K265 | K275 | 4 | 1:N | OC |
| K | Correção de Apontamento – Estoque Escriturado | K280 | 3 | 1:N | OC |

### Desmontagem

Alguns segmentos, como o automobilístico, por exemplo, apresentam a figura da “desmontagem” e esse processo era tratado anteriormente no Bloco K (Controle da Produção e do Estoque) como movimentação interna de mercadorias, mas, com essa nova segmentação na obrigação, as empresas poderão tratar como uma “Industrialização”, ainda que caracterizada apenas como Ordem de Serviço (OS).

Essas informações foram divididas em dois registros:

K210 – Desmontagem de Mercadorias – Item de Origem: Esse registro trata de informações sobre as mercadorias, que serão destinadas ao desmonte, informando a data da retirada do estoque e a quantidade.

K215 – Desmontagem de Mercadorias – Item de Destino: Nesse registro o enfoque são as informações sobre as mercadorias que serão originadas com o desmonte, devendo ser elencado nesse registro todos os códigos e quantidades que resultaram desse desmonte.

Iremos descrever estes registros a seguir: 

### Registro K 210: Desmontagem de Mercadorias - Item de Origem

Este registro tem o objetivo de escriturar a desmontagem de mercadorias de tipos: 00 – Mercadoria para revenda; 01 – Matéria-Prima; 02 – Embalagem; 03 – Produtos em Processo; 04 – Produto Acabado; 05 – Subproduto e 10 – Outros Insumos – campo TIPO\_ITEM do Registro 0200, no que se refere à saída do estoque do item de origem.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.

Quando houver identificação da ordem de serviço, a chave deste registro são os campos: COD\_DOC\_OS e COD\_ITEM\_ORI.  
Nos casos em que a ordem de serviço não for identificada, o campo chave passa a ser COD\_ITEM\_ORI. 

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "K210" | C | 004 | - | O |
| 02 | DT\_INI\_OS | Data de início da ordem de serviço | N | 008\* | - | OC |
| 03 | DT\_FIN\_OS | Data de conclusão da ordem de serviço | N | 008\* | - | OC |
| 04 | COD\_DOC\_OS | Código de identificação da ordem de serviço | C | 030 | - | OC |
| 05 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 060 | - | O |
| 06 | QTD\_ORI | Quantidade de origem – saída do estoque | N | - | 03 | O |

Observações:

Nível hierárquico - 3  
Ocorrência – 1:N

Descrição dos campos do registro K210:

* Campo 01 (REG) - Valor Válido: [K210].

* Campo 02 (DT\_INI\_OS) - Preenchimento: a data de início deverá ser informada se existir ordem de serviço, ainda que iniciada em período de apuração (K100) anterior. Validação: obrigatório se informado o campo COD\_DOC\_OS ou o campo DT\_FIN\_OS. A data informada deve ser menor ou igual a DT\_FIN do registro K100 (Este campo, a princípio, não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).

* Campo 03 (DT\_FIN\_OS) - Preenchimento: informar a data de conclusão da ordem de serviço. Ficará em branco, caso a ordem de serviço não seja concluída até a data de encerramento do período de apuração. Validação: se preenchido, DT\_FIN\_OS deve estar compreendida no período de apuração do K100 e ser maior ou igual a DT\_INI\_OP (este campo, a princípio, não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).

* Campo 04 (COD\_DOC\_OS) – Preenchimento: informar o código da ordem de serviço, caso exista. Validação: obrigatório se informado o campo DT\_INI\_OS (este campo, a princípio, não será gerado pelo TOTVS Gestão de Estoque, Compras e Faturamento).

* Campo 05 (COD\_ITEM\_ORI) - Validação: o código do item de origem deverá existir no campo COD\_ITEM do Registro 0200.

* Campo 06 (QTD\_ORI) – Preenchimento: não é admitida quantidade negativa.

### Registro K 215: Desmontagem de Mercadorias - Item de Destino

Este registro tem o objetivo de escriturar a desmontagem de mercadorias de tipos: 00 – Mercadoria para revenda; 01 – Matéria-Prima; 02 – Embalagem; 03 – Produtos em Processo; 04 – Produto Acabado; 05 – Subproduto e 10 – Outros Insumos – campo TIPO\_ITEM do Registro 0200, no que se refere à entrada em estoque do item de destino.

Este registro é obrigatório caso exista o registro-pai K210 e o controle da desmontagem não for por ordem de serviço (campos DT\_INI\_OS, DT\_FIN\_OS e COD\_DOC\_OS do Registro K210 em branco). Nesse caso, a saída do estoque do item de origem e a entrada em estoque do item de destino têm de ocorrer no período de apuração do Registro K100.

A quantidade deve ser expressa, obrigatoriamente, na unidade de medida de controle de estoque constante no campo 06 do registro 0200: UNID\_INV.  
A chave deste registro é o campo COD\_ITEM\_DES.

| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "K215" | C | 004 | - | O |
| 02 | COD\_ITEM\_DES | Código do item de destino (campo 02 do Registro 0200) | C | 060 | - | O |
| 03 | QTD\_DES | Quantidade de destino  – entrada em estoque | N | - | 03 | O |

Observações:  
Nível hierárquico - 4  
Ocorrência – 1:N

Descrição dos campos do registro K215:

* Campo 01 (REG) - Valor Válido: [K215]

* Campo 02 (COD\_ITEM\_DES) - Validação: o código informado deve ser diferente do campo COD\_ITEM\_ORI do Registro K210, e o código do item de destino deverá existir no campo COD\_ITEM do Registro 0200.

* Campo 03 (QTD\_DES) – Preenchimento: não é admitida quantidade negativa.

Para facilitar a inclusão do processo de desmontagem no TOTVS Gestão de Estoque, Compras e Faturamento, será realizada a ampliação da rotina de "Cópia por Referência", que passa a atender ao processo de geração das movimentações internas relativas aos Registros K210 e K215. Assim, a partir da cópia por referência do movimento de baixa da estrutura de origem o sistema irá possibilitar a criação automática do movimento de entrada dos itens de destino, além de criar o vínculo entre estes movimentos.

Para a desmontagem do item de origem, que deve corresponder a uma estrutura ou semiacabado, poderá ser utilizado qualquer movimento de baixa (tipo 2.2) já atualmente em uso pela empresa, não sendo necessária nenhuma parametrização específica. Deverão ser informados nesta movimentação de baixa as estruturas que sairão do estoque da empresa (itens origem) devido ao seu desmonte.

Para utilizar o processo de desmontagem através da cópia por referência, será necessário criar um motivo de cópia de referência específico para esta situação (29 - Desmontagem de Mercadorias).

Assim, o sistema localizará em determinado período quais foram os movimentos de entrada gerados por cópia por referência com o motivo 29 e enviará os seus produtos para o Registro K215.

O sistema irá também a partir dos movimentos de entrada gerados por cópia por referência com o motivo 29, identificar os respectivos movimentos de baixa que os originaram e enviará todos os seus produtos para o Registro K210.

Apesar da rotina do SPED Fiscal (da qual o Bloco K faz parte) ser gerada no TOTVS Gestão Fiscal, os lançamentos relativos aos Registros K 210 e K 215 serão enviados diretamente pelo TOTVS Gestão de Estoque, Compras e Faturamento, portanto, os movimentos que irão gerar esses registros não serão escriturados e não conterão Natureza Fiscal. 

Para utilizar o processo de desmontagem através da cópia por referência, será necessário que o usuário crie em sua base de dados um novo tipo de movimento de entrada (1.2.XX) que utilize o motivo de cópia por referência 29. Este tipo de movimento será responsável por efetuar a entrada dos novos itens (itens destino) gerados a partir da desmontagem (baixa) do item de origem.

Para este tipo de Cópia por Referência poderá ser efetuada a cópia de apenas um movimento por vez, mas um mesmo movimento pode conter várias estruturas.

Quando a criação de um movimento for acionada através de cópia por referência com motivo 29, o sistema automaticamente deverá verificar os itens do movimento de origem e somente permitir a execução do processo, caso todos eles sejam estruturas. Assim, tão logo o usuário solicite a criação do movimento via cópia por referência o sistema deverá checar os itens de origem e caso algum deles não seja uma estrutura o sistema deverá apresentar mensagem de erro com essa informação e não poderá permitir a execução do processo.

Quando um movimento for criado através de cópia por referência com motivo 29, o sistema deverá explodir a estrutura e apresentar em tela os componentes da mesma. Para isso o sistema deverá apresentar uma mensagem perguntando se o usuário deseja explodir a(s) estrutura(s) do movimento de origem até o último nível.

Caso o usuário informe "Sim", optando pela explosão completa, o sistema apresentará em tela todos os níveis e subníveis da estrutura, chegando até o nível dos componentes definidos como matéria-prima. 

Caso o usuário informe "Não", optando pela explosão parcial, ela será feita apenas até o primeiro nível da estrutura e somente no movimento destino o usuário poderá intervir explodindo os semiacabados e chegando até outros níveis da estrutura, caso necessário.

Assim, como pudemos observar, na rotina de desmontagem os itens do movimento de origem têm obrigatoriamente que ser uma estrutura, enquanto que os itens do movimento de destino podem ser produtos (componentes), semiacabados (estrutura) ou ambos. 

Para os itens de destino apresentados através da explosão da estrutura de origem, será permitido ao usuário excluí-los, porém não será permitido alterar a quantidade dos mesmos e nem efetuar a inclusão de novos itens ou estruturas. Caso seja necessário realizar alguma alteração de quantidade, isso deverá ser feito diretamente no movimento destino.

Caso a desmontagem tenha ocorrido sem nenhum problema, tendo sido realmente gerados todos os itens decorrentes da mesma, não será necessária nenhuma intervenção do usuário que deverá apenas clicar em "Avançar" até que o processo seja finalizado e OK no tipo de movimento criado, porém, caso seja necessária alguma alteração na quantidade dos itens, o usuário deverá efetuá-la na tela do movimento destino.

Na geração do Registro K215 do Bloco K do SPED Fiscal, o sistema levará os dados relativos aos movimentos gerados com Motivo de Referência 29 no período de apuração do SPED, e na geração do Registro K210 serão levados os dados dos movimentos que os originaram, ou seja, do Registro K210 constará a estrutura que foi desmontada (baixada) e do Registro K215 constarão os componentes gerados pela desmontagem da mesma (entrada via cópia por referência com motivo 29).

Assim, após terem sido gravadas todas as movimentações internas de desmontagem do mês, o sistema estará apto a gerar os Registros K 210 e K 215 do Bloco K do SPED Fiscal no TOTVS Gestão Fiscal.

**Para realizar a implantação da funcionalidade na versão 12.1.14, é necessário executar o script****[SCRIPTBLOCOK210E260.ZIP](https://suporte.totvs.com/portal/p/10098/download)****disponível no pacote, já para as versões superiores à 12.1.14 não há necessidade de execução de script específico.**

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cópia por Referência | Alteração | Movimentações > Processos > Assistente de Cópia por Referência | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

 

* TMOTIVOREFMOV - Motivos de Cópia por Referência

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
