---
content_hash: 7b1aa4f3fef526247e6d0a03e5f1dd91501f42138105d0a8c564f654b4f54ccd
fetched_at: '2026-06-29T00:11:17.256291+00:00'
page_id: '678572080'
product: rm
source: tdn-rm
title: 'Bloco K: Conglomerados Econômicos'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=678572080
version: 41
---

K030: Período da Escrituração Contábil Consolidada

O registro K030 identifica o período da escrituração contábil consolidada.

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | DT\_INI | Data inicial gerada a partir da data informada no cadastro da Escrituração Contábil. |
| 03 | DT\_FIN | Data final gerada a partir da data informada no cadastro da Escrituração Contábil |

K100: Relação das Empresas Consolidadas

Este Registro identifica todas as empresas que fazem parte da escrituração contábil consolidada.

Ele será gerado com os dados das empresas que fazem parte do  que foi associado ao **Plano de Contas Paralelo** (Saldo Consolidado) utilizado para geração do Bloco K.

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_PAIS | O país deve ser informado nos Parâmetros do Módulo Contábil (Processo 01.06, Etapa 1). Clique aqui para expandir  É importante ressaltar que o país deve estar associado a classificação (Ato Cotepe 35/2008) informada na tela de parâmetros do SPED Contábil, esta associação pode ser realizada através do anexo Codificação de País, existente no cadastro de país. |
| 03 | EMP\_COD | Estes campos são gerados, respectivamente, com o **Código da Coligada**, **CNPJ** e **Razão Social** informados no Cadastro de Coligadas. |
| 04 | CNPJ |
| 05 | NOME |
| 06 | PER\_PART | Neste campo, deve ser informado o percentual de participação acionária da **empresa titular da ECD** na empresa investida. Logo, se a Coligada Holding do Grupo Empresarial for a Investidora da empresa, este campo será preenchido com o Percentual da Participação informado no Anexo de Movimentações dos Investimentos Societários.  Se a Coligada Holding do Grupo Empresarial NÃO for a Investidora da empresa, este campo será preenchido com zero. Clique para expandir a imagem   **Atenção!**   * Este campo de percentual de participação não existe na base de dados. Ele é calculado pelo sistema conforme . * O sistema sempre irá considerar a última movimentação para a empresa informada no K100 até o limite da data fim da escrituração que está sendo gerada. |
| 07 | EVENTO | Este campo será preenchido com "S - Sim" se houver Movimentações dentro do período da escrituração.  Caso contrário, será preenchido com "N - Não". |
| 08 | PER\_CONS | Neste campo deve ser informado o percentual do resultado da empresa que foi para a consolidação.  Para gerá-lo o sistema vai verificar o Tipo de Consolidação da última movimentação para a empresa informada no K100 até o limite da data fim da escrituração que está sendo gerada:   * **Consolida Integralmente**: este campo será preenchido com 100% * **Consolida Proporcionalmente**: este campo será preenchido com o Percentual da Participação informado no Anexo de Movimentações dos Investimentos Societários. |
| 09 | DATA\_INI\_EMP | Data inicial gerada a partir da data informada no cadastro da Escrituração Contábil. |
| 10 | DATA\_FIN\_EMP | Data final gerada a partir da data informada no cadastro da Escrituração Contábil |

IMPORTANTE!

Este processo ocorre dessa forma a partir do Release 12.1.33. Em versões anteriores, o Registro é gerado com base no .

K110: Relação dos Eventos Societários

Considerando que este Registro é "filho" do K100, ele será gerado quando houver alguma  informada para a empresa informada no K100, cuja **Data da Movimentação** esteja dentro do período da ECD que está sendo gerada (Campo 7 do K100 = S).

Se houver mais de uma Movimentação no período da ECD, será gerado um registro K100 para cada uma delas.

Clique aqui para expandir a imagem

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema |
| 02 | EVENTO | Será preenchido com o Tipo do Evento informado na Movimentação |
| 03 | DT\_EVENTO | Data da Movimentação |

IMPORTANTE!

Este processo ocorre dessa forma a partir do Release 12.1.33. Em versões anteriores, o Registro é gerado com base no .

K115: Empresas Participantes do Evento Societário

Neste Registro constam as empresas que participaram das relacionadas no K110.

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | EMP\_COD\_PART | Código da empresa envolvida na operação. Corresponde ao código da coligada. |
| 03 | COND\_PART | Este campo será gerado automaticamente pelo sistema de acordo com o Tipo de Evento informado na Movimentação Societária, cuja **Data da Movimentação** esteja dentro do período da ECD que está sendo gerada (Campo 7 do K100 = S).  1 – **Sucessora** quando o Evento for de Fusão, Cisão Parcial, Cisão Total ou Incorporação. 2 – **Adquirente** para Evento de Aquisição 3 – **Alienante** para Evento de Alienação Clique para expandir |
| 04 | PER\_EVT | Percentual da empresa participante envolvida na operação, cuja **Data da Movimentação** esteja dentro do período da ECD que está sendo gerada (Campo 7 do K100 = S). Clique para expandir |

IMPORTANTE!

Este processo ocorre dessa forma a partir do Release 12.1.33. Em versões anteriores, o Registro é gerado com base no .

K200: Plano de Contas Consolidado

O registro K200 apresenta o plano de contas utilizado nas escriturações contábeis consolidadas. Ele será gerado com as informações do **Plano de Contas Paralelo** (Plano Consolidado - Bloco K) informado no processo de geração do SPED Contábil. Haverá uma linha para cada conta do plano de contas paralelo.

Clique para expandir

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente  pelo sistema. |
| 02 | COD\_NAT | Este dado é recuperado do Cadastro de Contas Paralelas.  Código da natureza da conta/grupo de contas, conforme tabela publicada pelo Sped: 01 Contas de Ativo 02 Contas de Passivo 03 Patrimônio Líquido 04 Contas de Resultado 05 Contas de Compensação 09 Outras |
| 03 | IND\_CTA | Este dado é recuperado do Cadastro de Contas Paralelas, sendo preenchido com "S" para Conta Sintética e "A" para Conta Analítica. |
| 04 | NIVEL | Estes campos são gerados, respectivamente, com o **Nível do** **Código da Conta**, o **Código da Conta Paralela**, o **Conta da Conta Superior** e o **Nome da Conta Paralela** informados no Cadastro de Contas Paralelas. |
| 05 | COD\_CTA |
| 06 | COD\_CTA\_SUP |
| 07 | CTA |

K210: Mapeamento para Planos de Contas das Empresas Consolidadas

O registro K210 apresenta o mapeamento das contas analíticas do plano de contas consolidado informado no registro K200 para as contas dos planos de contas das empresas consolidadas.

No sistema ele é gerado a partir da associação das Contas Contábeis nas Contas Paralelas. Para cada registro K210, que representa a Conta Paralela, poderão haver uma ou mais linhas.

Clique aqui para expandir

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente  pelo sistema. |
| 02 | COD\_EMP | Corresponde ao código da coligada e será recuperado da Associação do Plano Contábil, existente no Cadastro de Contas Paralelas. |
| 03 | COD\_CTA\_EMP | Corresponde ao **Código da Conta** contábil e será recuperado da Associação do Plano Contábil, existente no Cadastro de Contas Paralelas. |

K300: Saldos das Contas Consolidadas

Este registro é gerado a partir do Saldo Consolidado calculado pelo sistema através do processo de , que deverá ser executado para a data final utilizada na geração da ECD.

Clique para expandir

Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | COD\_CTA | Todos esses campos são recuperadas do cadastro do cálculo consolidado, anexo ao Plano Referencial. |
| 03 | VAL\_AG |
| 04 | IND\_VAL\_AG |
| 05 | VAL\_EL |
| 06 | IND\_VAL\_EL |
| 07 | VAL\_CS |
| 08 | IND\_VAL\_CS |

K310: Empresas Detentoras das Parcelas do Valor Eliminado Total

O registro K310 apresenta as empresas detentoras das parcelas do valor eliminado total, com os respectivos valores eliminados.

Para gerar esse registro o sistema verifica o parâmetro "Eliminação pelo Lançamento Contábil":

* Se o período da ECD for anterior a data parametrizada as informações desse registro serão recuperadas da aba Eliminação do Cadastro de Contas Paralelas, onde os dados são informados manualmente.
* Se o período for posterior ao parâmetro as informações virão automaticamente da Partida.

Clique para expandir

### Origem dos Dados

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | EMP\_COD\_PARTE | No modelo manual esta informação será recuperada do campo **Coligada Detentora,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar a coligada em que o lançamento foi incluído. |
| 03 | VALOR | No modelo manual esta informação será recuperada do campo **Valor** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar o valor informado na partida. |
| 04 | IND\_VALOR | No modelo manual esta informação será recuperada do campo **Natureza,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar a natureza da partida. |

K315: Empresas Contrapartes das Parcelas do Valor Eliminado Total

O registro K315 apresenta as empresas contrapartes das parcelas do valor eliminado total, com os respectivos valores eliminados.

Para gerar esse registro o sistema verifica o parâmetro "Eliminação pelo Lançamento Contábil":

* Se o período da ECD for anterior a data parametrizada as informações desse registro serão recuperadas da aba Eliminação do Cadastro de Contas Paralelas, onde os dados são informados manualmente.
* Se o período for posterior ao parâmetro as informações virão automaticamente da aba Eliminação existente na Partida.

Clique para expandir

| Nº | Campo | Origem |
| --- | --- | --- |
| 01 | REG | Gerado automaticamente pelo sistema. |
| 02 | EMP\_COD\_CONTRA | No modelo manual esta informação será recuperada do campo **Coligada Contrapartida,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar a **Coligada Contrapartida** informada na aba Eliminação, existente na Partida. |
| 03 | COD\_CONTRA | No modelo manual esta informação será recuperada do campo **Conta Contrapartida,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar a **Conta Contrapartida** **da Eliminação** informada na aba Eliminação, existente na Partida. |
| 04 | VALOR | No modelo manual esta informação será recuperada do campo **Valor,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar o valor informado na Partida. |
| 05 | IND\_VALOR | No modelo manual será considera a natureza inversa da informada no campo **Natureza,** existente no cadastro de Eliminação. Para o modelo automático o sistema irá considerar a natureza inversa da partida. |
