---
article_id: 360054351414
category: RH - Dissídio
content_hash: cd741a59bb53cf457841af5ecaf8239572bc380998af67f4f2a1915ecc5d8852
fetched_at: '2026-06-28T22:43:43.451808+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Qual a configuração que antecede o cálculo do dissídio
  retroativo
type: support-article
updated_at: '2026-05-05T13:43:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054351414-RH-Linha-Protheus-GPE-Qual-a-configura%C3%A7%C3%A3o-que-antecede-o-c%C3%A1lculo-do-diss%C3%ADdio-retroativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34214593234839) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Qual a configuração que antecede o cálculo do dissídio retroativo?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
**1**. Verifique se os funcionários que terão o reajuste estão com o salário e vinculo do sindicato correto:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950434)  
  
**2**. Verifique a configuração do sindicato (s):  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950414)  
  
**3**. Verifique se o histórico salarial está com as informações corretas:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950474)  
  
**4**. Verifique as configurações das seguintes verbas:  
Isso deve ser feito com todas as verbas calculadas na folha, seguindo as orientações do quadro abaixo:  
  
Obs. A verba de ID 0984 - Adicional de Cargo de Confiança deve estar atrelada a uma verba, caso contrario o sistema irá calcular apenas a verba de Salário Base <https://tdn.totvs.com/pages/releaseview.action?pageId=985693012>

|  |  |  |
| --- | --- | --- |
| Identificador de cálculo para dissídio retroativo. A verba vinculada a este identificador deve ser informada na configuração de verba da coluna seguinte, aba dissídio retroativo, campo Verba P. Dissídio | Identificador de cálculo das verbas demonstradas em sua folha, que serão vinculadas as verbas com os identificadores da coluna anterior | Observações importantes |
| 0337 | 0017 – Base FGTS | - Verbas de Base de FGTS, Base INSS, Depósito do FGTS e Desconto do INSS devem ser configuradas para que seja possível ao sistema apurar as diferenças relativas à previdência e ao FGTS. Se estas verbas não forem configuradas, não sairão no dissídio retroativo e, consequentemente, não serão tratadas as diferenças, pois isto somente ocorre na rotina GPEM690.  - Nas verbas em que serão apuradas as diferenças de dissídio, não pode haver incidência para FGTS e INSS. Esta verificação é muito importante para que não haja dupla tributação sobre os valores apurados como diferenças. Caso haja incidência para FGTS e/ou INSS nessas verbas, será gerado um arquivo de log de ocorrências informando as verbas de destino que estão com incidência.  -A tributação de Imposto de Renda é feita por data de pagamento, diferente do FGTS e INSS, que trabalham por competência. Portanto, as verbas que compõem o cálculo do IR, deverão possuir incidências para o IRRF, e, tratando-se das verbas de pagamento das diferenças dos valores de férias, no cadastro da verba, deverão ficar com “Sim” no campo “Ref. Férias”, e as verbas de pagamento das diferenças de 13º salário deverão fica com “Sim” no campo “Ref.13º”. O pagamento é feito na própria verba do IRRF na folha de pagamento (id 0066). |
| 0338 | 0013 – Salário Contribuição até Limite Base Folha 0014 - Salário Contribuição acima Limite Base Folha |
| 0339 | 0018 – Código FGTS Depósito |
| 0340 | 0064 - INSS 0065 – INSS Férias |
| 0398 | 0108 – Base FGTS 13º Salário |
| 0399 | 0019 - Salário Contribuição até Limite Base 13º Salário 0020 - Salário Contribuição acima Limite Base 13º Salário |
| 0400 | 0109 – Valor FGTS 13º Salário |
| 0401 | 0070 – INSS sobre 13º Salário |
| 0341 | 0001 - Anuênio 0002 - Biênio 0003 - Triênio 0004 - Quadriênio 0005 - Quinquênio 0031 – Salário Mensalista 0032 – Salário Horista 0033 – DSR Horista 0035 – DSR Hora Extra 0036 - Periculosidade 0037 – Insalubridade Mínima 0038 – Insalubridade Média 0039 – Insalubridade Máxima  **Verbas configuradas especificamente na versão 11** 0088 – Diferença de Férias\* 0089 – Diferença de Férias Mês Seguinte\* 0090 – Diferença de 1/3 Férias\* 0091 – Diferença de 1/3 Férias Mês Seguinte\* 0092 – Diferença de DSR sobre Férias\* 0093 – Diferença de DSR sobre Férias Mês Seguinte\* 0096 – Diferença de Média de Horas Extras no mês\* 0097 - Diferença de Média de Horas Extras mês seguinte\* 0098 – Diferença Outros Adicionais\* 0099 - Diferença Outros Adicionais Mês Seguinte\* 0227 – Diferença de Férias em Dobro\* 0228 - Diferença de 1/3 Férias em Dobro\*  **Verbas configuradas especificamente na versão 12** 0072 - Férias\*\* 0077 - 1/3 férias\*\* 0075 - Méd. Fer Valor\*\* 0082 - Méd. Fer Hor.\*\* 0084 - Out. Adic. Fer\*\* 1304 - Insal Fer \*\* 1306 - Insal Fer s/ Verb\*\* 1300 - Peric. Fer\*\* 1302 - Peric. Fer s/ Verb\*\* 1308 - Adic Confi. Fer\*\* 1310 - Adic Trans Fer\*\* 1296 - ATS Fer. \*\* 1298 - ATS Fer. s/ Verb\*\* | **Apenas para versão 11**  Na versão 11 para calcular as diferenças das férias, deve -se amarrar as verbas de diferença de dissidio as verbas de diferenças de férias e não nas próprias verbas calculadas nas férias, ou seja: A verba de id 0341 que é a verba de diferença de dissidio provento deve estar vinculada na aba dissidio retroativo da verba de id 0088 (Dif de férias) e não na verba de id 0072 (Férias mês)  **Apenas para versão 12**  Na versão 12 para calcular as diferenças das férias, deve -se amarrar as verbas de diferença de dissidio as verbas de Férias e não nas verbas de diferença de férias (contrário da versão 11), ou seja: A verba de id 0341 que é a verba de diferença de dissidio provento deve estar vinculada na aba dissidio retroativo da verba de id 0072 (Férias mês) e não na verba de id 0088 (Dif. Férias) |
| 0342 | 0054 - Faltas 0055 - Atrasos 0242 – Faltas II 0243 – Atrasos II |  |
| 0402 | 0028 – Diferença de 13º Salário | **Apenas para versão 11** Na versão 11, a verba de id 0402 deve estar vinculada a verba de id 0028 para calcular a diferença de 13º no dissídio.  **Apenas para versão 12** Na versão 12, a verba de id 0402 deve estar vinculada a verba de id 0024 para calcular a diferença de 13º no dissídio.  Na inexistência das verbas de média de 13º, ID's 0123 e 0124, esta verba deve ficar com "Não" para dissídio, do contrário as eventuais diferenças de médias calculadas na folha de dezembro serão calculadas em duplicidade no dissídio. |
| 0403 | 0348 – Valor da Diferença de 13º Salário Negativa |  |
| 0943 | 0148 - % Empresa |  |
| 0944 | 0149 - % Terceiros |  |
| 0945 | 0150 - % Acid. Trabalho |  |

Outros encargos:

|  |  |
| --- | --- |
| **Identificadores de encargos de dissídio.** **A verba vinculada a este identificador deve ser informada na configuração de verba da coluna seguinte, aba dissídio retroativo, campo Verba P. Dissídio** | **Identificadores de encargos apresentados na folha de pagamento** |
| 0946 - Contr. Incra Dissídio | 0184 - Contribuição INCRA |
| 0947 - Contr. Senai Dissídio | 0185 - Contribuição SENAI |
| 0948 - Contr. Sesi Dissídio | 0186 - Contribuição SESI |
| 0949 - Contr. Senac Dissídio | 0187 - Contribuição SENAC |
| 0950 - Contr. Sesc Dissídio | 0188 - Contribuição SESC |
| 0951 - Contr. Sebrae Dissídio | 0189 - Contribuição SEBRAE |
| 0952 - Contr. Dpc Dissídio | 0190 - Contribuição D.P.C |
| 0953 - Contr. Faer Dissídio | 0191 - Contribuição FAER |
| 0954 - Contr. Senar Dissídio | 0192 - Contribuição SENAR |
| 0955 - Contr. Seconc Dissídio | 0193 - Contribuição SECONC |
| 0956 - Contr. Sest Dissídio | 0200 - Contribuição SEST |
| 0957 - Contr. Senat Dissídio | 0201 - Contribuição SENAT |
| 0958 - Contr. Sescoop Dissídio | 0798 - Contribuição SESCOOP |
| 0959 - Contr. Sal. Educ. Dissídio | 0204 - Contribuição Sal. Educação |

**Observação:** Para calcular as diferenças de dissídio sobre as verbas de abono pecuniário, crie uma verba sem ID e sem incidências, e para as diferenças de dissídio de abono pecuniário use essa verba.  
  
**Atenção**:  
A atualização salarial do cadastro de funcionário ocorrerá apenas se o valor atual da salário for menor que o salário reajustado pelo percentual de dissidio. No caso de funcionário que tenha recebido aumento salarial no mês de cálculo do dissidio e cuja folha de pagamento ainda esteja aberta, será necessário executar a rotina de Reajuste Salarial, ou aumentar o salário manualmente pelo cadastro de funcionário, para que o percentual de reajuste seja aplicado no salário atual.  
  
Os encargos são calculados de forma independente, ou seja eles não se baseiam nas diferenças calculadas no dissídio, mais sim nos valores calculados na época.  
  
**4.1**. Configuração de verbas na pratica, utilizando como exemplo a verba de salário - id 0031:  
Se eu quero realizar a configuração de uma determinada verba é obrigatório que eu saiba o identificador da mesma, nesse caso a verba de salário possui o identificador de cálculo 0031.  
Sabendo o identificador da verba que eu quero configurar, eu vou buscar nesta documentação qual o identificador de dissídio que ela deve estar vinculada.  
  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950594)  
  
A partir dessa imagem podemos ver que a verba de id 0031 deve ser vinculada a verba de id 0341 na aba de dissídio.  
  
**Em Atualizações/ Definições de Cálculo/ Verbas:**  
Localize os identificadores de cálculo (ID.P/CALCULO - RV\_CODFOL) da primeira coluna e anote os códigos das verbas (CODIGO VERBA - RV\_COD):  
No **exemplo** abaixo eu vou anotar o código 341. Código da minha verba vinculada ao id 0341.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950634)  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950654)  
  
Após isso localize os identificadores de cálculo da segunda coluna e na aba DISSÍDIO preencha o campo Dissíd. Ret. (RV\_COMPL) com SIM e preencha o campo Verba p. Diss. (RV\_CODCOM) com o código da verba correspondente ao id para cálculo da primeira coluna:  
No **exemplo**vou pesquisar minha verba de salário, por código ou id e fazer a configuração na dissídio retroativo:  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094158253)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091950674)

**IMPORTANTE:** Verba de ID 0341:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12382905962903)  
Observação: A verba de provento de dissidio deve ser configurada como Não nos **campos de INSS e FGTS**, pois esses impostos são recalculados no dissidio. O IRRF deverá ser configurado como SIM , para que no cálculo de folha sejam apurados os valores corretamente.

**Esse processo deve ser realizado em todas as verbas que serão calculadas as diferenças de dissídio.**  
  
**5**. O último passo antes da execução da rotina de dissídio retroativo é os backups das tabelas envolvidas no cálculo:  
É necessário realizar os backups das tabelas abaixo, antes de qualquer execução de calculo seja de reajuste ou de Dissidio Retroativo.

* SRA;
* SR3 e SR7;
* SRC;
* RHH;
* RGB; \* Exclusiva P12
* SRK.

Se o dissídio retroativo for gerado incorretamente para folha de pagamento a única e mais segura forma de excluir é com o retorno das tabelas: [MP - GPE - Exclusão do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037259774-MP-GPE-Exclus%C3%A3o-do-c%C3%A1lculo-de-diss%C3%ADdio-?source=search)  
  
**Saiba mais**:

<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio>
