---
article_id: 10114013561367
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 55e3143fa6c73061cd5291e05e5bf3ea6be4a1c996beef18b81784125b5ce030
fetched_at: '2026-06-28T22:42:10.789844+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIME SC- geração
  dos NOVOS quadros 15,16,85 e 12 ref ao Fundo Social e FUMDES '
type: support-article
updated_at: '2022-11-10T14:19:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10114013561367-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIME-SC-gera%C3%A7%C3%A3o-dos-NOVOS-quadros-15-16-85-e-12-ref-ao-Fundo-Social-e-FUMDES
---

**Dúvida** **DIME SC**  como gerar os novos quadros 15,16, 85 e 12 referente ao **Fundo Social** e **FUMDES** na **DIME SC**?  
  
**Ambiente**TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão **12.1.25**.  
  
**Solução**

1. Aplique a Atualização e substitua o arquivo **DIMESC.ini** (em anexo) dentro da pasta *System*

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1087180>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1087175>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1087179>;

2. Verifique o Manual para a geração dos Registros. Para geração do arquivo no novo layout, foram introduzidas as seguintes modificações no arquivo:

1. **Inclusão do Quadro 15**- Demonstrativo dos valores devidos aos fundos por benefício fiscal;
2. **Inclusão do Quadro 16**- Demonstrativo da apuração de valores devidos de fundos ou saldo credor;
3. **Inclusão do Quadro 85**- Discriminação das contribuições ao FIA e FEI devidas no exercício anterior;
4. **Quadro 12**- Inclusão na tabela de nova origem para débito de Fundo apurado no Quadro 16 e os códigos de Receitas dos Fundos que deverão ser recolhidos.

Importante:

Inicialmente, a demonstração da **apuração** e **discriminação dos Fundos** será efetuada exclusivamente na **DIMESC**, não devendo ser replicada na **EFD ICMS/IPI**.  
  
**Registros Tipo 15/16 – Demonstrativo dos Valores Devidos aos Fundos como Contrapartida pela Utilização de Benefício Fiscal e Demonstrativo da Apuração de Valores Devidos ou Saldo Credor de Fundos**

3. Tem como base as informações preenchidas no assistente, após a Inclusão do **Registro Tipo 35**, selecione a **opção: Sim**  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-13-23.png?version=1&modificationDate=1667571203407&api=v2)  
  
4. Preencha as Informações referentes ao **Quadro 15 e 16**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-15-56.png?version=1&modificationDate=1667571357080&api=v2)  
  
5. Após a geração da **DIME**, as informações serão apresentadas no **Relatório de Conferência** no **MATA950**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-18-35.png?version=1&modificationDate=1667571515863&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-21-37.png?version=1&modificationDate=1667571697917&api=v2)  
  
6. Gere o **Arquivo txt da Dime**  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-24-33.png?version=1&modificationDate=1667571873593&api=v2)  
  
![](https://tdn.totvs.com/download/thumbnails/655881026/image2022-11-4_11-24-53.png?version=1&modificationDate=1667571893387&api=v2)  
  
7. **Registros Tipo 85/95 – Discriminação das Contribuições ao FIA e FEI Devidas no Exercício Anterior**

Preencha as informações no assistente, após a Inclusão do **Registro Tipo 15 e 16**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_10-4-49.png?version=1&modificationDate=1667567089563&api=v2)  
  
8. Após a geração da **DIME**, as informações serão apresentadas no **Relatório de Conferência no MATA950**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_10-0-14.png?version=1&modificationDate=1667566814407&api=v2)  
  
9. Gere o **Arquivo txt da Dime**  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_10-2-45.png?version=1&modificationDate=1667566965597&api=v2)  
  
**10. Registro tipo 33 – Discriminação dos pagamentos do imposto e dos débitos específicos**

Referente a geração dos registros sobre o **Fundo Social** e **FUMDES** (**Quadro 12**), preencha as por meio do assistente, no momento de geração do meio magnético, após ter marcado como **SIM** a opção de gerar os **Registros Tipo 15/16**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-36-13.png?version=1&modificationDate=1667572573350&api=v2)  
  
11. Após a geração da **DIME**, as informações serão apresentadas no **Relatório de Conferência no MATA950**:  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-37-13.png?version=1&modificationDate=1667572633970&api=v2)  
  
12. Gere o **Arquivo txt da Dime**  
  
![](https://tdn.totvs.com/download/attachments/655881026/image2022-11-4_11-37-46.png?version=1&modificationDate=1667572666287&api=v2)

Nos casos em que o validador da **DIME** relate Inconsistências na validação do arquivo, verificar se valores referente aos registros dos **tipos 36 (Quadro 15)**, **37 (Quadro 16)** e **85 (Quadro 85)** inseridos manualmente através do *Wizard* no **Protheus** estão de acordo com as validações abaixo.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Registro tipo 36 - DEMONSTRATIVO DOS VALORES DEVIDOS AOS FUNDOS POR BENEFÍCIO FISCAL** | | | | | |
| **Nº** | **Campo Protheus** | **Conteúdo** | **Validação** | | |
| 01 | XXX | Tipo de registro “36” | XXX | | |
| 02 | XXX | Quadro “15” | XXX | | |
| 03 | Seq | Sequência | Preencher com a sequência começando em 1 para o primeiro registro | | |
| 04 | Cod. Benef. TTD | Código do Benefício TTD | O código do Benefício TTD informado deve constar da Portaria SEF nº 143/22.  - Preencher com zero quando na Coluna 06 foi informado um subtipo de DCIP validado relativo a um benefício fiscal relacionado no Anexo III da Portaria SEF 123/22 | | |
| 05 | Nr. Conc. TTD | Número Concessão TTD | Número da concessão deve corresponder ao código de benefício TTD informado, pertencer ao contribuinte e encontrar-se vigente. - Preencher com zero quando na Coluna 06 foi informado um subtipo de DCIP validado relativo a um benefício fiscal relacionado no Anexo III da Portaria SEF 143/22. | | |
| 06 | Subtipo DCIP | Subtipo DCIP “Tipo 3 - Crédito Presumido” sem exigência de TTD | **IMPORTANTE:**Para cada subtipo de DCIP informado no Quadro 46, informar separadamente o valor do crédito presumido.  Informar com o código do subtipo de DCIP do “Tipo 3 - Crédito Presumido” sem exigência de TTD, cuja AUC-DCIP foi informado no Quadro 46 no mesmo arquivo da DIME. - preencher com 0 (zero) sempre informado um código de benefício e número de concessão TTD válido nas colunas 04 e 05. - quando subtipo DCIP informado nesta coluna for validado, na coluna 09 é obrigatório o preenchimento do código = (0)  e na coluna 11 é obrigatório o preenchimento do código = (1). | | |
|  |  | **DÉBITOS FUNDOS** |  | | |
| 07 | Vlr. BC ICMS | Valor da Base de Cálculo do ICMS da Operação ou Prestação Relativo a cada nº de concessão | Preencher com o valor da Base de Cálculo do ICMS da operação ou prestação relativo ao código do benefício TTD informado na coluna 4, sempre que na coluna 11 forem indicados os códigos (2) e (3). | | |
| 08 | Vlr. ICMS Eixo | Valor do ICMS Exonerado relativo a cada nº de concessão | Preencher com montante mensal o valor da exoneração ou do imposto diferido, conforme o caso, relativo ao código do benefício TTD informado na coluna “04 ou ao subtipo DCIP de Crédito Presumido informado na coluna 06. | | |
| 09 | Codigo FUMDES | Código do Cálculo FUMDES:  0 - Não exigido na Portaria SEF 143/22  1 - 2% do ICMS Exonerado | Preencher com o código de cálculo do FUMDES: (0) e (1) | | |
| 10 | Vlr. FUMDES | Valor do FUMDES | Preencher com o valor do FUNDES, quando na coluna 9 foi indicado o código (1), resultante da aplicação do percentual de 2% sobre o valor ICMS exonerado informado na coluna 8. | | |
| 11 | Cod. Fdo Social | Código do cálculo FUNDO SOCIAL:  0 - Não exigido na Portaria SEF 143/22;  1 - 2,5% do ICMS Exonerado;  2 - 0,4% da BC ICMS - FUMDES  3 - 0,4% da BC ICMS - (FUNDO SOCIAL + FUMDES)  4 - 4,5% do ICMS Exonerado | Preencher com o código de cálculo do FUNDO SOCIAL: (0), (1), (2), (3) e (4). | | |
| 12 | Vlr. Fdo Social | Valor do FUNDO SOCIAL | Preencher com o valor do FUNDO SOCIAL resultante do cálculo previsto para os códigos de cálculo informados na coluna 9 | | |
|  |  | **CRÉDITO FUNDOS** |  | | |
| 13 | Vlr. BC ICMS Dev | Valor Base de Cálculo do ICMS da NF de devolução relativo a cada nº concessão | Preencher, separadamente, com o Valor da Valor Base de Cálculo do ICMS constante da Nota Fiscal de devolução correspondente a cada benefício fiscal informado na coluna 04, para o qual se exige este parâmetro no cálculo do FUNDO SOCIAL devido. | | |
| 14 | Vlr. ICMS Exo Dev | Valor do ICMS exonerado correspondente a NF de devolução relativo a cada nº concessão | Preencher, separadamente, com o valor do ICMS exonerado ou diferido, proporcional as devoluções recebidas relativas a cada benefício fiscal do informado na coluna 04 ou na coluna 06, se for o caso. | | |
| 15 | Vlr. FUMDES Dev | Valor do FUMDES relativo a devolução | Preencher, separadamente, com o valor do FUMDES proporcional à devolução relativa a cada benefício fiscal informado na coluna 04 ou na coluna 06, se for o caso, correspondente ao montante calculado no período da saída da mercadoria. | | |
| 16 | Vlr. Fdo Soc. Dev | Valor do FUNDO SOCIAL relativo a devolução | Preencher, separadamente, com o valor do FUNDO SOCIAL proporcional à devolução relativa a cada benefício fiscal informado na coluna 04 ou na coluna 06, se for o caso, correspondente ao montante calculado no período da saída da mercadoria. | | |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Registro tipo 37 - Demonstrativo da Apuração de Valores Devidos ou Saldo Credor de Fundos** | | | | | |
| **Nº** | **Campo** | **Conteúdo** | **Tamanho** | **Posição** | **Formato** |
| 01 | Tipo de Registro | Preencher com "37" | 02 | 001/002 | C |
| 02 | Quadro | Preencher com “16” | 02 | 003/004 | C |
| 03 | Item | Número do item do Quadro 16 do Anexo I | 03 | 005/007 | N |
| 04 | Valor | Conteúdo da informação do Item | 17 | 008/024 | $ |

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Registro tipo 85 - Discriminação das Contribuições ao FIA e FEI Devidos no Exercício Anterior** | | | | | |
| **Nº** | **Campo** | **Conteúdo** | **Tamanho** | **Posição** | **Formato** |
| 01 | Tipo de Registro | Preencher com “85” | 02 | 001/002 | N |
| 02 | Quadro | Preencher com “85” | 02 | 003/004 | C |
| 03 | Item | Número do item do Quadro 85 do Anexo I | 03 | 005/007 | N |
| 04 | Valor | Conteúdo da informação do Item | 17 | 008/024 | $ |
