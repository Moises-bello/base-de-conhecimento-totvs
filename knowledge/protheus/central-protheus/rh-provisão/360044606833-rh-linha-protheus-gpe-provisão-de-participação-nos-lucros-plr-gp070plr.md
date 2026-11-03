---
article_id: 360044606833
category: RH - Provisão
content_hash: 52cb80bceb4b6cde1e1167271bda6a0eb77ca3c6b8ccee9f55a7084af40e7e53
fetched_at: '2026-06-28T22:43:56.765425+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Provisão de Participação nos Lucros - PLR (GP070PLR)
type: support-article
updated_at: '2026-03-23T17:00:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044606833-RH-Linha-Protheus-GPE-Provis%C3%A3o-de-Participa%C3%A7%C3%A3o-nos-Lucros-PLR-GP070PLR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32879921247639)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como calcular Provisão de Participação nos Lucros - PLR?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**  
Por padrão, o Protheus não realiza Cálculo de Provisão de PLR, por serem valores definidos de acordo com a Convenção Coletiva da Categoria dos funcionários, configurados no Cadastro de Sindicato.

Foi disponibilizado o Ponto de Entrada **GP070PLR** para esta tratativa.

**Configuração:**  
Deverá ser criado 5 verbas para utilização na provisão de PLR, sendo:  
-para provisão do PLR;  
-para baixa por pagamento do PLR;  
-para provisão do PLR (referente ao lançamento mensal;  
-para baixa por transferência;  
-para baixa por rescisão.

* Essas verbas devem ser informadas no parâmetro MV\_PLRVER separadas por ";" (ponto e vírgula), conforme exemplo abaixo:   
  Z01;Z02;Z03;Z04;Z05
* No parâmetro MV\_PLRPER deve ser informado o mês ou os meses em que será realizado o fechamento do saldo provisionado da provisão. No caso de haver mais de um mês, deverá ser informado os meses separados por ";" (ponto e vírgula) com dois dígitos, conforme exemplo abaixo:  
  03;09
* O parâmetro **MV\_PLRVLBX**permite configurar a forma que será realizado a baixa da provisão. Se ativado, ou seja, configurado com .T., o sistema irá deixar no saldo o valor provisionado no mês e efetuará a baixa do saldo anterior; se desativado, ou seja, configurado com .F., o sistema efetuará a baixa do saldo anterior mais o valor provisionado no mês, deixando o saldo zerado

**Ponto de entrada GP070PLR:**  
Deverá ser codificado e compilado um ponto de entrada que deverá retornar o valor provisionado no mês em formato numérico dentro da posição 1 de um array.  
Além disso, o ponto de entrada enviará quatro informações que podem ser acessadas via Paramixb:  
  
Paramixb[1] - Filial do funcionário

Paramixb[2] - Matrícula do funcionário

Paramixb[3] - Saldo anterior da provisão de PLR

Paramixb[4] - Data de referência do cálculo

Já a lógica do ponto de entrada deverá ser implementada conforme regra de cálculo do PLR da empresa, mas a estrutura de retorno deverá ser um array com 1 posição contendo o saldo da provisão no mês conforme exemplo abaixo:

|  |
| --- |
| `User Function GP070PLR()`    `Local aAreaSRA  := SRA->( GetArea() )`  `Local aRet      := {}`  `Local cFilial   := PARAMIXB[1]`  `Local cMat      := PARAMIXB[2]`  `Local nSaldoAnt := PARAMIXB[3]`  `Local dDataRef  := PARAMIXB[4]`  `Local nProvMes  := 0`    `/*`  `Lógica para obter o valor provisionado do mês`  `*/`  `aAdd( aRet, nProvMes )`    `RestArea( aAreaSRA )`    `Return aRet` |

**Cálculo:**

1. Durante o processamento do cálculo da provisão (opção: Férias, 13 Salário ou Ambos) será verificado se o ponto de entrada foi compilado. Em caso positivo, o cálculo executará o ponto de entrada e receberá o valor devido de PLR para o mês em processamento do funcionário em avaliação. Os valores positivos recebidos serão provisionados e os valores negativos serão abatidos do acumulado e do saldo.  
   Obs.: saldo acumulado negativo não será permitido, o mesmo será zerado, caso seja inferior a zero.
2. Será verificado nas tabelas de movimentação(SRC/SRD) no roteiro PLR se existe algum lançamento de pagamento de PLR. Em seguida, será realizado a atualização do cálculo para o saldo acumulado.
3. Após o processamento, os resultados serão registrados nas tabelas:  
   Movimento de Provisões (SRT) com o novo tipo de provisão (ID 9 – PLR);  
   Movimento Mensal de Provisões (RHT) com o novo tipo (ID 4 – Mês PLR);

**Contabilização:**

1. Após o cálculo da provisão, durante a contabilização será gerado na tabela de resumo da folha (SRZ) os movimentos dos funcionários que receberam verbas de lançamento de PLR, assim como as verbas de baixa de PLR pagas.
2. Os registros serão gerados utilizando a informação “PP” (Provisão PLR) para o campo do tipo da SRZ (RZ\_TIPO).
3. Os valores negativos de PLR que foram recebidos também serão criados para o ‘desprovisionamento’ do saldo do funcionário, com sua respectiva verba de baixa.
4. As outras atividades do processo de contabilização, como por exemplo, configuração de lançamento padrão, continuarão a funcionar da forma atual do produto padrão.

**Relatório de provisão de PLR:**  
Foi disponibilizado a funcionalidade GPER095 para impressão do resultado da provisão calculada no mês. Essa funcionalidade irá aparecer no menu do cliente caso o ponto de entrada esteja compilado.

O layout utilizado como base para o desenvolvimento do resultado da PLR será o layout do 13 Salario, apresentando informações do mês anterior, movimento no mês e saldo atual.

**Importante!**  
Caso esteja efetuando migração da versão 11 para a versão 12, é importante executar o compatibilizador abaixo, pois o tipo de provisão de PLR foi alterado na versão 12.

**Na versão 11 os códigos eram:**  
1=Fer.Venc.;2=Fer.Prop.;3=13o.Sal.;4=14o.Sal.;5=Mes Ferias;6=Mes 13o.;7=Plr;8=Mes PLR;9=Rec.Venc.;A=Rec.Prop.

**Já na versão 12 são:**  
1=Fer.Venc.;2=Fer.Prop.;3=13o.Sal.;4=14o.Sal.;5=Mes Ferias;6=Mes 13o.;7=Rec.Venc.;8=Rec.Prop.;9=Plr;A=Mes PLR

Esse procedimento deve ser executado uma única vez.

1 - Aplicar pacote expedição continua do RH - [Como fazer o download baixar do pacote de expedição continua acumulado do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

2 - Adicionar no menu a rotina de usuário U\_M070CONV.

3 - Executar a rotina U\_M070CONV.

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=286739120>
