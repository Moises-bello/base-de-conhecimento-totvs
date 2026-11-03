---
content_hash: 3fa130028c87cd20cfc48d9c1862bac5cceae12e07fc3d4de94bbd835e672416
fetched_at: '2026-06-29T00:10:04.601713+00:00'
page_id: '452719225'
product: rm
source: tdn-rm
title: Fórmulas / Funções – P
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719225
version: 4
---

**Função PAR**  
Esta variável retorna o valor de um campo complementar a ser validado.  
PAR  
   
**Exemplo:**  
Se PAR > 30 e PAR < 50  
Entao verdade  
Senao falso  
Fimse

**Observação:**  
**-** Esta fórmula deverá ser informada no campo "Fórmula de Validação" no cadastro de Campos Complementares. No momento da informação no campo complementar do funcionário o sistema irá acatar ou não o valor de acordo com a fórmula acima.

* A variável PAR apresenta resultados específicos para o campo "Fórmula para Complemento de Histórico" dos lançamentos contábeis e campos de "Fórmula" na Emissão da Folha Analítica.
* A função PAR também pode ser usada em Lançamentos Financeiros. Para isto, deverá ser parametrizado um lançamento financeiro do Tipo "Valor Calculado por fórmula".  
  **Exemplo:**  
  **Cadastrar as fórmulas:**  
  FOR1  
  COLIGADACORRENTE  
  FOR2  
  CHAPA  
     
  **FOR3**  
  Decl VALORFGTS;  
  Setvar(VALORFGTS,0);  
  Se (EXECSQL ('SQL1') = Verdade) Entao   
  Repita  
  Se RESULTSQL ('SQL1' , 'ANOCOMP') = VAL(SUBSTR(PAR,4,4)) Entao  
  Se RESULTSQL ('SQL1' , 'MESCOMP') = VAL(SUBSTR(PAR,1,2)) Entao  
  Setvar(VALORFGTS, RESULTSQL ('SQL1' , 'BASEFGTS'))  
  FimSe  
  FimSe  
  Ate ProxRegSQL('SQL1' ) = Falso  
  FimSe;  
  VALORFGTS  
  + Cadastrar a sentença:\*  
    SQL1  
    SELECT ANOCOMP,MESCOMP,BASEFGTS FROM PFPERFF WHERE  
    CODCOLIGADA = :FRM\_FOR1  
    AND CHAPA = :FRM\_FOR2  
       
    Ao emitir a folha analítica selecionar um campo de Fórmula e informar o código FOR3.  
       
       
       
    **Atenção:**  
    A função PAR com os parâmetros do exemplo 2 deverá ser utilizada exclusivamente na Folha analítica.  
       
    **Observação:**  
    A função PAR também pode ser usada em Lançamentos Financeiros. Para isto, deverá ser parametrizado um lançamento financeiro do Tipo "Valor Calculado por fórmula".  
       
    **Exemplo:**  
    Cadastrar as seguintes fórmulas:  
    MESPAR => VAL(SUBSTR(PAR,1,2))  
    ANOPAR => VAL(SUBSTR(PAR,4,4))  
    FORPAR => BASEINSSFF(FOR('ANOPAR') ,FOR('MESPAR'))  
    Parametrizar um lançamento financeiro do Tipo: Valor Calculado por Fórmula e incluir a fórmula "FORPAR" no campo "Fórmula". Após esta parametrização, gerar os lançamentos financeiros preenchendo mês e ano de competência. O sistema retornará a base de INSS no Mês e Ano conforme solicitado.  
       
       
    **Função PARMQRY**  
    Esta variável retorna o valor de um campo da query de um relatório.   
    PARMQRY (STRING)  
       
       
    **Exemplo:**  
    **1** - Criar Fórmula XXX  
    PARMQRY ('DATAADMISSAO')  
       
    **2** - Criar Sentença SQL XXX  
    SELECT PFUNC.CHAPA, PFUNC.NOME, PFUNC.CODFUNCAO, PFUNC.DATAADMISSAO  
    FROM PFUNC  
    WHERE CHAPA = 'ZZZZ' AND CODCOLIGADA = 'Y'   
    (Onde 'ZZZZ' será o número da chapa do funcionário que será filtrada a SQL e 'Y' será o número da coligada do funcionário do filtro)  
       
    **3** - Criar Relatório XXX com a seguinte LD:  
    CHAPA  NOME   CÓDIGO DA FUNÇÃO  DATA DE ADMISSÃO  
    SQL#1  SQL#2   SQL#3    SQL#4     
    (Onde é feita a chamada da Sentença SQL criada anteriormente e corresponde ao número de campos da sentença)  
    RESULTADO DA FÓRMULA XXX  
    FÓRMULA#1   
    (Onde é feita a chamada da fórmula criada anteriormente)  
       
    4 - O relatório será emitido da seguinte forma:  
     CHAPA  NOME    CÓDIGO DA FUNÇÃO  DATA DE ADMISSÃO  
    XXX   NOME DO FUNCIONÁRIO   LLL    DD/MM/AAAA  
    (Onde XXX é o número da chapa do funcionário, Nome do funcionário, LLL é o código do funcionário e DD/MM/AAAA a data de admissão do funcionário)  
    RESULTADO DA FÓRMULA XXX  
    DD/MM/AAAA   
    (Onde DD/MM/AAAA a data de admissão do funcionário conforme a fórmula criada)  
       
       
       
    **Função PERCINSS**  
    PERCINSS (VALOR, VALOR, VALOR)  
    Retorna o percentual de INSS informado na seção do funcionário de acordo com o parâmetro passado na fórmula.  
    Onde  
    **Valor1** - Acidente de trabalho  
    **Valor2** - Terceiros  
    **Valor3** –Funcionário  
       
    **Exemplo**  
    PERCINSS 1 = PERCINSS (1, MES, ANO)   
    Retornará o percentual de "Acidente de Trabalho" da seção atual do funcionário.  
       
    PERCINSS 2 = PERCINSS (2, MES, ANO)   
    Retornará o percentual de "Terceiros" da seção atual do funcionário.  
       
    PERCINSS 3 = PERCINSS (3, MES, ANO)   
    Retornará o percentual informado em "Percentuais de acréscimo – Aposentadoria especial" da seção atual do funcionário. Será verificado também o código de ocorrência cadastrado no histórico de ocorrências do funcionário.  
       
    **Função PERIODO**  
    Esta variável retorna o período atual.  
    PERIODO  
       
    **Função PROCESSO**  
    Retorna qual o processo que está sendo executado no momento da execução da formula.  
    PROCESSO  
       
    **RETORNOS POSSÍVEIS DA VARIAVEL DE FORMULA 'PROCESSO'**  
    'FOLHA'     //Processo de lançamento de folha de pagamento  
    '1A\_PARCELA\_13';  //Processo de lançamento de 1a Parcela de 13   
    '2A\_PARCELA\_13';  //Processo de lançamento de 2a Parcela de 13  
    'DIFERENCA\_13'     //Processo de lançamento de diferença de 13  
    'RESCISAO'    //Processo de Rescisão   
    'RESCISAO\_COMPLEMENTAR' // Processo de Rescisão complementar  
    'FERIAS'     //Lançamento de Férias  
    'DIFERENCA\_SALARIAL';   //Lançamento de diferença salarial  
    'PROVISAO'     //Geração de Histórico de Provisões  
    'DIFERENCA\_FERIAS'    //Lançamento de diferença de férias  
    'PASSIVO'     //Geração do Passivo Trabalhista  
    'CANCELA\_MOVIMENTO'    //Cancelamento de Movimento  
    'IMPORTA\_MOVIMENTO'    //Importação de Movimento  
       
    **Exemplo:**  
    SE (PROCESSO <> 'PROVISAO')  
    ENTAO  
    SE (RC/3) > 700  
    ENTAO 700  
    SENAO (RC/3) / 30 \* (TABFUNC ('NRODIASABONO', 'I') + TABFUNC ('NRODIASFERIAS', 'I'))  
    SENAO  
    SE (RC/3) > 700  
    ENTAO 700  
    SENAO (RC/3) FIMSE  
    FIMSE  
       
    /\*Se o processo for diferente de provisão, férias, por exemplo, executa considerando dias de abono e dias de férias. Se o processo for provisão executa a fórmula com o salário contratual apenas. \*/  
       
       
       
       
    **Função PROXREGSQL**  
    Esta variável avança para o próximo registro da sentença SQL  
    PROXREG (String)
