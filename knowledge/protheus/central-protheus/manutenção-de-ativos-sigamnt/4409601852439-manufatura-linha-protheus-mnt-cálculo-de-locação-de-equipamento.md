---
article_id: 4409601852439
category: Manutenção de Ativos (SIGAMNT)
content_hash: 6bf338cb002567010077fd7da3066c48d00f92c366f5d4dba5b4e7cf1b05446b
fetched_at: '2026-06-28T22:42:32.860289+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Cálculo de Locação de Equipamento
type: support-article
updated_at: '2021-10-29T11:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409601852439-Manufatura-Linha-Protheus-MNT-C%C3%A1lculo-de-Loca%C3%A7%C3%A3o-de-Equipamento
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:08:30 min** **Dúvida**Como é realizado o cálculo de locação do equipamento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**Para realização do cálculo deverão ser seguidos os passos abaixo:

1. No módulo de **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**, acessar **Atualizações / Controle de Oficina / Bens / Família de Bens - MNTA050**, inserir uma família de bens se atentando aos campos **Base Hora** , **% Residual** e **Taxa de Loc**.
2. Em **Atualizações / Controle de Oficina / Bens / Veículos - MNTA084**, cadastrar um veículo e informar conforme *help* de cada campo.
3. Em **Atualizações / Construção Civil / Locação de Equip. / Custo de Locação de Equipamento -MNTA683**, clicar em **+ Calcular** e informar os dados da tela de **Parâmetros** conforme *help* de cada campo.
4. O Sistema irá gravar o **Custo de Locação do Equipamento - TVL** no cenário abaixo:

**Grupo Cons.**: grupo informado na tela de **Parâmetros****Código Bem**: bem considerado de acordo com os **Parâmetros****Ano Refer.**: ano referente ao cálculo  
**Mês Refer.**: mês referente ao cálculo  
**Grupo Oper.**: grupo no qual o bem está operando ou onde operou  
**Filial Oper.**: filial no qual o bem está operando ou onde operou  
**CC Operação**: centro de custo no qual o bem está operando ou onde operou  
**Valor Aquis.**: valor de aquisição do bem, obtido através do campo **Valor Compra - T9\_VALCPA****Vida Útil**: quantidade da vida útil do bem, obtido através do campo **Valor Vida - T9\_VALODES****Unid. Vida**: unidade da vida útil do bem, obtido através do campo **Unid.****Vida - T9\_UNIDDES****Vida U. Rem.\***: quantidade de horas restante de vida do bem. **Valor Vida - T9\_VALODES – Cont. Acum. - T9\_CONTACU****Valor Pres.\***: Valor presente do bem. **Val. Presente - T9\_VALPRES – ( ( Val. Presente - T9\_VALPRES / Vida U.Rem. - TVL\_DEPREM) \* Contador - TVL\_CONTAD)****Valor Resid.\***: Valor residual do bem. **(Valor Compra - T9\_VALCPA \* % Residual - T6\_PERESID) / 100****Parc. Dep/h.\***: Parcela de depreciação do bem por hora. **(Valor Aquis. - TVL\_VALAQU – Valor Resid. -  TVL\_VALRES) / Vida Útil - TVL\_VIDUTI****Fundo Manut.\***: Fundo de manutenção. **(% Manutenção - T9\_PERMAN / 100) \* Valor Compra - T9\_VALCPA****T. Cus. Cap.\***: Taxa de custo capital. **((Valor Pres. - TVL\_VALPRE – Valor Resid. - TVL\_VALRES) \* (( 1 + (Parâmetro Custo de Capital\*\* / 100)) elevado a potência de ( 1 / 12 ) – 1 )) / Base Hora - T6\_BASHMIN)****CLE Variável\***: Custo variável na locação do equipamento. **(Parc. Dep / h. - TVL\_PARDEP + Fundo Manut. - TVL\_FUNMNT + T. Cus. Cap. - TVL\_TAXCUS)****Seguro Lic.\***: Seguro licenciamento do bem. **(Valor Compra - T9\_VALCPA \* % Seg. Lic. - T9\_SEGLICE) / 100****Taxa Admin.\***: Taxa administrativa. **(( Parâmetro Taxa Administrativa\*\* / 100 ) \* (( CLE Variável - TVL\_CLEVAR \* Base Hora - T6\_BASHMIN) + Seguro Lic. - TVL\_SEGLIC))****Índ. Ocios.\***: Índice de Ociosidade. **(((CLE Variável - TVL\_CLEVAR \* Base Hora - T6\_BASHMIN) + Seguro Lic. - TVL\_SEGLIC + Taxa Admin. - TVL\_TAXADM) \* Parâmetro Índice de Ociosidade\*\*)****CLE Fixo.\***: Custo de locação de equipamento fixo. **Seguro Lic. - TVL\_SEGLIC****+ Taxa Admin. - TVL\_TAXADM + Índ. Ocios. - TVL\_INDOCI****Base Hr. Mi.\***: Quantidade base de horas. **(CLE Total - TVL\_CLETOT / Base Hr. Mi. - TVL\_BASHOR)****CLE Total\***: Custo de locação de equipamento total. **(CLE Variável - TVL\_CLEVAR \* Base Hr. Mi. - TVL\_BASHOR) + CLE Fixo - TVL\_CLEFIX****CLE Hora\***: Custo de locação de equipamento por hora. **(CLE Total - TVL\_CLETOT / Base Hr. Mi. - TVL\_BASHOR)****CLE Hora R.\***: Custo de locação de equipamento por horas reais trabalhadas. Quando **Base Hr. Mi. - TVL\_BASHOR** maior que **Contador - TVL\_CONTAD** é **(Base Hr. Mi. - TVL\_BASHOR \* CLE Hora - TVL\_CLEHOR)** e se **Base Hr. Mi. - TVL\_BASHOR** for menor que **Contador - TVL\_CONTAD** é **(Contador - TVL\_CONTAD \* CLE Hora - TVL\_CLEHOR)****Valor Fatur.\***:Valor Faturado. **(Val.Faturado - T9\_VALFAT / Número de dias do mês corrente\*\* ) \* Dias Aloc. - TVL\_DIALOC****Ind. Cálculo**: Indicador de cálculo proporcional ao tempo alocado, caso exista transferência no período. Pode ser alterado por meio do parâmetro **MV\_NGDTINC - Data de integração contábil. Limitará a alteração dos registros**.  
**Motivo\***: Motivo de alteração do indicador do cálculo do aluguel.  
**Dias Aloc.\***: Dias alocado na obra. **Número de dias do mês corrente – Período com suspensão de aluguel****Contador\***: Contador acumulado no período. **Maior contador acumulado do período – Menor contador acumulado do período****\***Calculado pelo Sistema**\*\***Tela de **Parâmetros** conforme **passo 3** acima

1. Em**Atualizações / Construção Civil / Locação de Equip. / Projeção Cle -** **MNTA684**
2. Clicar em **+ Projetar** e informar os dados da tela de **Parâmetros** conforme *help* de campo.
3. O Sistema irá gravar a **Projeção e Cálculo de Locação do Equipamento - TVA** no seguinte cenário:

**Código Bem\*\***: Código do bem  
**Ano Refer.**: Ano de referência do cálculo. O Sistema passa por todos os anos até o fim da vida útil do bem.  
**Mês Refer.**: Mês de referência do cálculo. O Sistema passa por todos os meses até o fim da vida útil do bem.  
**Valor Aquis.**: Valor de compra do bem. Carrega o valor do campo **Valor Compra - T9\_VALCPA.****Vida Útil**: Quantidade da vida útil do bem. Carrega o valor do campo **Valor Vida - T9\_VALODES.****Vida U.Rem.\***: Quantidade de horas restante de vida do bem. **Valor Vida - T9\_VALODES – Cont. Acum. - T9\_CONTACU****Valor Resid.\***: Valor residual do bem. **(Valor Compra - T9\_VALCPA \* % Residual - T6\_PERESID) / 100****Valor Pres.\***: Valor presente do bem. **Val. Presente T9\_VALPRES – ((Val. Presente - T9\_VALPRES / Vida U.Rem. - TVL\_DEPREM) \* Contador - TVL\_CONTAD)****Parcela Dep.\***: Parcela de depreciação do bem por hora. **(Valor Aquis. - TVL\_VALAQU – Valor Resid. - TVL\_VALRES) / Vida Útil - TVL\_VIDUTI****Fundo Manut.\***: Fundo de manutenção. **(% Manutenção - T9\_PERMAN / 100) \* Valor Compra - T9\_VALCPA****T. Cus. Cap.\***: Taxa de Custo Capital. **((Valor Pres. - TVL\_VALPRE – Valor Resid. - TVL\_VALRES) \* ((1 + (Parâmetro Custo de Capital\*\* / 100) ) elevado a potência de ( 1 / 12 ) – 1 )) / Base Hora - T6\_BASHMIN)****CLE Variável\***: Custo variável na locação do equipamento. **(Parc. Dep/h. - TVL\_PARDEP + Fundo Manut. - TVL\_FUNMNT + T. Cus. Cap. - TVL\_TAXCUS)****Seguro Lic.\***: Seguro licenciamento do bem. **(Valor Compra - T9\_VALCPA \* % Seg. Lic. - T9\_SEGLICE) / 100****Taxa Admin.\***: Taxa administrativa. **((Parâmetro Taxa Administrativa\*\* / 100 ) \* ((CLE Variável - TVL\_CLEVAR \* Base Hora - T6\_BASHMIN) + Seguro Lic. - TVL\_SEGLIC))****Ind. Ocios.\***: Índice de ociosidade. **(((CLE Variável - TVL\_CLEVAR \* Base Hora - T6\_BASHMIN) + Seguro Lic. - TVL\_SEGLIC + Taxa Admin. - TVL\_TAXADM) \* Parâmetro Índice de Ociosidade\*\*)****CLE Fixo\***: Custo de locação de equipamento fixo. **Seguro Lic. - TVL\_SEGLIC****+ Taxa Admin. - TVL\_TAXADM + Índ. Ocios. - TVL\_INDOCI****CLE Total\***: Custo de locação de equipamento total. **(CLE Variável - TVL\_CLEVAR \* Base Hr. Mi. - TVL\_BASHOR) + CLE Fixo - TVL\_CLEFIX****CLE Hora\***: Custo de locação de equipamento por hora. **(CLE Total - TVL\_CLETOT / Base Hr. Mi. - TVL\_BASHOR)****P. Cus. Cap.\*\***: Taxa de custo capital  
**P. Tx. Adm.\*\***: Taxa administrativa  
**P. Ind. Oc.\*\***: Percentual de ociosidade  
  
**\***Calculado pelo Sistema  
**\*\***Tela de **Parâmetros** conforme **passo 2** acima  
  
**Importante**A suíte de locação de equipamento tem como finalidade reportar suspensões de aluguel e utilizando destes registros efetuar o cálculo do **Custo de Locação - CLE** além de efetuar projeções de custo. Os bens com Categoria **T9\_CATBEM** igual a **4 - Frota Não Integrada ao TMS.** e **Aluguel** - **T9\_ALUGUEL** igual a **1 - Sim** estão aptos a utilizar este processo. As rotinas que compõem a suíte são:

* **Custo Locação Equipamento - MNTA683**Rotina responsável por calcular os custos de aluguel de equipamentos.

* **Projeção CLE - MNTA684**A projeção de custo de locação de equipamento faz o cálculo de todos os meses da data de compra até o fim da vida útil do bem com os dados já existentes e algumas informações passadas para o Sistema a partir da tela de parâmetros.

* **Motivos de Suspensão - MNTA687**Rotina responsável por cadastrar os motivos de suspensão de aluguel.

* **Suspensão de Aluguel - MNTA686**Rotina responsável por cadastrar as suspensões de aluguel. As suspensões serão utilizadas para determinar o tempo de aluguel do bem, sendo que o período em suspensão não será cobrado. Os registros inclusos nesta rotina serão utilizados no **CLE - Cálculo de Locação de Equipamento**.
