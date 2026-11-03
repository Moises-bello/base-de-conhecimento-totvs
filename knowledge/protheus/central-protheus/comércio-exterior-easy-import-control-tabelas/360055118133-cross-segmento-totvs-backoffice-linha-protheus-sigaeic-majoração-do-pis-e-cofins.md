---
article_id: 360055118133
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: f9dce87501ab40d38291d92f7399903c6a000914d701b85bfc4fc5a3c991ff56
fetched_at: '2026-06-28T22:39:47.774032+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Majoração do PIS
  e COFINS
type: support-article
updated_at: '2025-11-17T14:34:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055118133-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Majora%C3%A7%C3%A3o-do-PIS-e-COFINS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como incluir o valor no campo %M. COFINS (WZ\_ALCOFM) e/ou % M. PIS (WZ\_ALPISM) do cadastro de CFOP, rotina EICOP100?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - *Easy Import Control* - Todas as versões  
  
**Solução**Foi incluído um tratamento para permitir o controle de percentual de PIS e COFINS majorado, visando atender à MP 563/2012, publicada no DOU de 04/04/2012, onde em seu Art 43º, altera a lei 10.865/2004, acrescendo em um valor percentual a tributação do PIS e/ou COFINS Importação para a lista de produtos classificados conforme anexo único da MP 563/2012.  
  
COFINS  
Para habilitar o preenchimento do campo %M. Cofins (WZ\_ALCOFM) no cadastro de CFOP, é necessário preencher a informação do campo Tipo.Calc. (WZ\_TPCMCOF), neste terão as opções: 1- Padrão, 2-Calculado e 3-Não calculado.

![CFOP-_TIPO_CALC.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360090924193/CFOP-_TIPO_CALC.PNG)  
  
Cada opção irá realizar uma ação no sistema, são elas:

```
1=Padrão: O sistema irá verificar se o campo Al.M. COFINS? (YT_MJCOF) do cadastro de Importador  
está igual a Sim. Em caso positivo será considerado o valor do COFINS majorado cadastrado no   
campo % M. COFINS (YD_MAJ_COF) no cadastro da N.C.M., em caso negativo o sistema não irá   
considerar a alíquota majorada do COFINS.  
2=Calculado: O sistema irá considerar as informações do COFINS majorado cadastrado no campo  
 % M. COFINS (WZ_ALCOFM) no C.F.O.  
3=Não Calculado: O sistema não irá considerar a alíquota majorada do COFINS.   
Neste caso para que informação COFINS majorado seja preenchida é só escolher a opção   
2 - Calculado.
```

PIS  
Para habilitar o preenchimento do campo %M. Cofins (WZ\_ALPISM) no cadastro de CFOP, é necessário preencher a informação do campo Tipo.Calc. (WZ\_TPCMPIS), neste terão as opções: 1- Padrão, 2-Calculado e 3-Não calculado.  
![CFOP-_TIPO_CALC.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360090924193/CFOP-_TIPO_CALC.PNG)  
Cada opção irá realizar uma ação no sistema, são elas:

```
1 = Padrão: O Sistema irá verificar se o campo Al.M. PIS? (YT_MJPIS) está igual a Sim. Em caso  
positivo será considerado o valor do PIS majorado cadastrado no campo % M. PIS (YD_MAJ_PIS) no  
cadastro da N.C.M., em caso negativo o Sistema não irá considerar a alíquota majorada do PIS.  
2 = Calculado: O Sistema irá considerar as informações do PIS majorado cadastrado no campo % M.  
PIS (WZ_ALPISM) no C.F.O.  
3 = Não Calculado: O Sistema não irá considerar a alíquota majorada do PIS.
```

**Saiba mais**  
[Majoração de Cofins](https://tdn.totvs.com/pages/releaseview.action?pageId=271162785)  
[Majoração PIS](https://tdn.totvs.com.br/download/attachments/73074239/EIC_BT_Registro%20de%20Majoracao%20do%20PIS%20na%20Importacao_THKKDD.pdf?version=1&modificationDate=1374842022000&api=v2)
