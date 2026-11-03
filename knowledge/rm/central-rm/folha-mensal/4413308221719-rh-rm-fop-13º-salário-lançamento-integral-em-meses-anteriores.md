---
article_id: 4413308221719
category: Folha Mensal
content_hash: 265016f3bd5a975cd76347a4fd4c486cb06571180f4b9c9cac9365097dc36b38
fetched_at: '2026-06-28T22:46:59.333569+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - 13º Salário: lançamento integral em meses anteriores'
type: support-article
updated_at: '2024-09-10T12:37:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413308221719-RH-RM-FOP-13%C2%BA-Sal%C3%A1rio-lan%C3%A7amento-integral-em-meses-anteriores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26265776546199) Tempo aproximado para leitura: **00:17:14 min****Dúvida**Como realizar o lançamento integral do 13º salário em meses anteriores com discriminação de médias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para o pagamento da segunda parcela antecipadamente, é necessário que observe-se que os encargos de **INSS** e**IRRF**, pois eles serão recolhidos para os órgãos competentes apenas no mês de Dezembro, que de fato será o mês de quitação dos encargos. Isso é aplicado para os casos de pagamento do 13º em Novembro ou meses anteriores ao mês de Dezembro, pois são considerados como antecipação ou adiantamento.  
  
Para preparar o sistema é necessário que sejam cadastradas fórmulas básicas em: **Administração de Pessoal | Fórmulas.**  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413309727511)  
  
**1ª Fórmula básica:**

**Código:** CHAPA  
**Título:** Chapa  
**Texto:** Chapa  
  
**2ª Fórmula básica:**

**Código**: ANO  
**Título:** Ano  
**Texto:** Ano  
  
**3ª Fórmula básica:**

**Código:** MES  
**Título:** Mês de Competência  
**Texto:**MES  
  
**4ª Fórmula básica:**

**Código:**COLIGADA  
**Título:** Coligada  
**Texto:** Coligadacorrente  
  
**5ª Fórmula básica:**

**Código:** PERIODO  
**Título:**Período atual  
**Texto:** Periodo  
  
**Siga os passos abaixo:**1. Acesse: **Gestão | Visões de dados.**  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413309740695)  
  
Cadastre a consulta SQL:  
  
**Código:** 13SALARIO  
**Título:** 13º salário pago durante o ano  
**Texto:****SELECT SUM**(VALOR) VALOR **FROM PFFINANC** (**NOLOCK**), **PEVENTO** (**NOLOCK**), **PPARAM** (**NOLOCK**)  
**WHERE** PFFINANC.CODCOLIGADA=PEVENTO.CODCOLIGADA **AND** PPARAM.CODCOLIGADA=PFFINANC.CODCOLIGADA **AND** PEVENTO.CODIGO=PFFINANC.CODEVENTO **AND** PFFINANC.CHAPA=:FRM\_CHAPA **AND** PEVENTO.CODIGOCALCULO='9' **AND** (PFFINANC.MESCOMP<>PPARAM.MESCOMP **OR** PFFINANC.NROPERIODO<>:FRM\_PERIODO)  
**AND** PFFINANC.ANOCOMP=PPARAM.ANOCOMP **AND** PFFINANC.CODCOLIGADA=:FRM\_COLIGADA

2. Acesse: **Administração de Pessoal | Fórmulas.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413302677911)** **Importante**As fórmulas não consideram os meses de admissão caso o número de dias trabalhados sejam inferiores à 15 dias.  
  
Cadastre as seguintes fórmulas:  
  
**1ª Fórmula:****Código:**A0011  
**Título:** AVOS 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO  
**Texto:**SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          NROAVOS13+ABS(MES-12)

SENAO

          NROAVOS13

FIMSE  
  
**2ª Fórmula:**

**Código:**A0012  
**Título:**13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO  
**Texto:**execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          (RC/12)\*(NROAVOS13+ABS(MES-12))-resultsql('13SALARIO','valor')

SENAO

          (RC/12)\*(NROAVOS13)-resultsql('13SALARIO','valor')

FIMSE  
  
Caso queira que as fórmulas adicionais de 13º informadas nos módulos abaixo sejam consideradas, a fórmula anterior, A0012, deverá ser alterada da seguinte forma:   
  
**Fórmula:**execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          ((RC + FOR("XXXX") + FOR("YYYY"))/12) \* (NROAVOS13+ABS(MES-12))

SENAO

          ((RC + FOR("XXXX") + FOR("YYYY"))/12) \* (NROAVOS13)

FIMSE  
  
**Importante**  
Onde houver XXXX ou YYYY deverá ser alterado para as fórmulas adicionais existentes.  
  
**3ª Fórmula:****Código:**A0016  
**Título:**MEDIA DE 13 SALÁRIO INTEGRAL EM MESES ANTERIORES A DEZEMBRO  
**Texto:** execsql('13SALARIO');

SE SFUNC<>'P' E SFUNC<>'M' E SFUNC<>'R' E SFUNC<>'L' ENTAO

          (CALCMED(2)/12)\*(NROAVOS13+ABS(MES-12))

SENAO

          (CALCMED(2)/12)\*(NROAVOS13)

FIMSE  
  
**4ª Fórmula:****Código:** A0013  
**Título:** INSS DE ANTECIPAÇÃO DE 13º SALARIO  
**Texto:** execsql('13SALARIO');

TI(FOR('A0012') + FOR('A0016') - resultsql('13SALARIO','valor'))  
  
**Importante**A fórmula abaixo é uma sugestão de desconto referente a Pensão Alimentícia, onde o cliente poderá adaptar de acordo com os procedimentos da empresa.  
  
**5ª Fórmula:****Código:**PENS13PR  
**Título:** Pensão sobre líquido de 13º salário antecipado - liquido  
**Texto:**DECL PERC, CONT, X;  
SETVAR (CONT,1);  
SE TABDEP ('DTNASCIMENTO' ,'D' ,CONT) <> DATANULA ENTAO  
          REPITA  
                    SE TABDEP ('DTNASCIMENTO','D',CONT) <> DATANULA E TABDEP ('INCPENSAO','S',CONT) ='1' ENTAO  
                              SETVAR (PERC, TABDEP ('PERCENTUAL' , 'V', CONT) / 100);  
                              SETVAR (X,1)  
                    SENAO ''  
                    FIMSE;  
          SETVAR (CONT,CONT+1)  
          ATE X=1 OU TABDEP ('DTNASCIMENTO' ,'D' ,CONT) = DATANULA  
FIMSE;  
  
SE X>0 ENTAO  
          DECL LIQUIDO, VLRBASEIRRF, VLRINSS, VLRINSS2, VLR,CONTADOR;  
          SETVAR (LIQUIDO, C('8001') + C('8005')); /\*Se quiser deduzir o valor adiantado basta diminuir o valor do evento cc 35\*/  
          SETVAR (VLRINSS, TI (LIQUIDO));  
          SETVAR (VLRINSS2, TI2(LIQUIDO));  
          SETVAR (VLRBASEIRRF, LIQUIDO);  
          REPITA  
                    SETVAR (VLR, ((LIQUIDO-VLRINSS- TR (VLRBASEIRRF-VLRINSS2-VLR)) \* PERC)); SETVAR (CONTADOR, CONTADOR+1)  
          ATE CONTADOR= 7; VLR  
SENAO 0  
FIMSE  
  
**Importante**A fórmula acima somente deverá ser criada caso queira descontar a pensão sobre o pagamento do 13º salário integral. Neste, o usuário também deverá cadastrar um evento do tipo desconto/valor sem incidências e associar a fórmula PENS13PR.  
  
**6ª Fórmula:****Código:** A0014  
**Título:** IRRF DE ANTECIPAÇÃO DE 13º SALÁRIO  
**Texto:**EXECSQL('13SALARIO'); DECL BCALC;

SETVAR(BCALC,FOR('A0012')+FOR('A0016')+RESULTSQL('13SALARIO','VALOR'));

TR(BCALC-TI(BCALC)- FOR('PENS13PR'))  
  
**7ª Fórmula:****Código:** A0015  
**Título:** DESCONTO DE INSS E IRRF ANTECIPADO  
**Texto:** MV(15,ANO,'8003')+MV(15,ANO,'8002')  
  
**Importante** Em caso do desconto do evento de pensão, incluir na fórmula acima +MV(15,ANO,'XXXX'), onde XXXX deve ser substituído pelo código do evento de pensão criado conforme descrito na observação da fórmula PENS13PR.   
  
3. Acesse: **Administração de Pessoal | Eventos.**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413302739479)  
  
Cadastre os seguintes eventos:  
  
**1º Evento:****Código:** 8001  
**Descrição:** Adiantamento de 13º Salário Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS No campo **Fórmula valor** informar a fórmula de código A0012. No campo **Fórmula Referência** informar a fórmula de código A0011.  
  
**2º Evento:****Código:** 8005  
**Descrição:** Média de adiantamento de 13º Salário Provento/Valor, com Código de Cálculo 09. Incide FGTS e RAIS No campo **Fórmula valor** informar a fórmula de código A0016. No campo **Fórmula Referência** informar a fórmula de código A0011.  
  
**3º Evento:****Código:** 8002  
**Descrição:** INSS 13º Salário - antecipado - Desconto/Valor, sem Código de Cálculo. No campo **Fórmula valor** informar a fórmula de código A0013.  
  
**3º Evento:**  
**Código:** 8003  
**Descrição:** IRRF 13º Salário - antecipado - Desconto/Valor, sem Código de Cálculo. No campo **Fórmula valor** informar a fórmula de código A0014.  
  
**4º Evento:**  
**Código:** 8004  
**Descrição:** Desconto de INSS13º e IRRF13º - antecipado - Provento/Valor, sem Código de Cálculo. No campo **Fórmula valor** informar a fórmula de código A0015.  
  
4. Realize o lançamento dos eventos 8001, 8002, 8003 e 8005 através do caminho **Folha Mensal | Lançamentos | Grupo de Eventos.**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413296073751)  
  
**Importante**A partir desse ponto vamos falar sobre os procedimentos que deverão ser realizados na competência de **Dezembro.** Somente para quem efetuou o pagamento integral antecipado.  
  
5. Realize o lançamento do evento 8004 do caminho **Folha Mensal | Lançamentos | Grupo de Eventos.**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413296073751)  
  
6. Na competência de Dezembro deverá efetuar o processamento do 13º Salário através do módulo: **Folha Mensal | Cálculo 13°.****![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413296154519)**7. Efetuar a geração do **SEFIP** e todas as guias.  
  
**Importante**O recolhimento do INSS de 13º salário e IRRF de 13º salário deve ocorrer em dezembro, pois a legislação de IRRF, informa que o IRRF deve ser calculado no ato da quitação e na verdade a quitação só ocorre em dezembro, pois podem ocorrer diferenças salariais, diferenças de médias e até mesmo de tabelas de cálculo o que acarretaria problemas no cálculo da diferença de INSS e IRRF. O INSS só é aceito no SEFIP da competência 13, veja manual do SEFIP. Se recolhido anteriormente não será possível a geração deste SEFIP automaticamente na competência de dezembro. Lembramos que, ao emitir a DIRF, o IRRF e o INSS do funcionário irá aparecer na competência Dezembro.  
  
**Saiba Mais**  
[Geração de SEFIP](https://tdn.totvs.com/pages/releaseview.action?pageId=317323040)  
[GPS - Guia de INSS](https://tdn.totvs.com/display/public/LRM/GPS+-+Guia+de+INSS)
