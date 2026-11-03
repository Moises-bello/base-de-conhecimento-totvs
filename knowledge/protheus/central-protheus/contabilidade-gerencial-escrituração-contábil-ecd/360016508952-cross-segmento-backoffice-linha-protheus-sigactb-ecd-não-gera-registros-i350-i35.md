---
article_id: 360016508952
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: e5b19818b12aa9bc9781c85f1e85a8367fbb394bbf442a582399c972588721c0
fetched_at: '2026-06-28T22:40:44.332220+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD NÃO GERA REGISTROS
  I350 - I355 - I150 - I155
type: support-article
updated_at: '2024-06-04T13:38:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016508952-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-N%C3%83O-GERA-REGISTROS-I350-I355-I150-I155
---

**Ocorrência**Geraçâo da ECD, registros I350 e I355 não foram gerados

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Requisitos**

Os registros são gerados com base em lançamento de apuração de resultado , diante disso necessário verificar se a apuração de resultado foi devidamente realizada

* [Exemplo - Apuração Trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)e [Exemplo - Apuração Anual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041555313-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Anual-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* [O SISTEMA NÃO ESTA ZERANDO AS CONTAS DE RECEITA E DESPESA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046954954-MP-SIGACTB-CTBA211-O-SISTEMA-N%C3%83O-ESTA-ZERANDO-AS-CONTAS-DE-RECEITA-E-DESPESA?source=search)
* Veja como sistema preenche os campos[\_LP e \_DTLP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630411-MP-SIGACTB-PREENCHIMENTO-DO-CAMPO-CQ0-LP-e-CQ0-DTLP?source=search)
* Caso tenha gerado a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)
* Verifique na tabela CSA e CSB se o campo de numero de lote esta diferente para o lote/lançamento de apuração de resultado
* CVD CVN E CT1 - verifique o compartilhamento
* CT2, CTF, CTC, CSA e CSB  Verifique  se gerou o lote
* CSA\_NUMLOT e CSB\_NUMLOT Veja se as tabelas CSA e CSB o numero no lote de apuração esteja igual , caso esteja diferente o sistema não ira gerar
* veja se  os campos [X2\_AUTREC, X2\_TAMFIL, X2\_TAMUN, X2\_TAMEMP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018497311-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA190-Campo-Filial-das-tabelas-CQ-n%C3%A3o-est%C3%A3o-sendo-alimentadas?source=search) , das tabelas CT2, CTC, CTF, CQO,CQ1...CQ9 e CQA , CS0....CSZ e CW0 e da tabela CS0...CSZ estão corretos em comparação da SIGAMAT
* CT2, CTF, CTC ,CQ0...CQ9 Verifique o [Compartilhamento de Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007377851-MP-SIGACTB-Compartilhamento-de-Tabelas-?source=search)
* Verifique o compartilhamento das [TABELAS ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-ECD-TABELAS-ECD?source=search)
* Verifique também no plano de contas a classificação das contas (passivo,ativo..etc) e [NATUREZA CONTA CONTABIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006887272-MP-SIGACTB-CTBA020-NATUREZA-CONTA-CONTABIL-ECD-ECF?source=search)
* [Realize o reprocessamento de saldos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-MP-SIGACTB-CTBA-190-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-?source=search)
* Veja se o procedure da ECD [MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search) esta configurado
* Aplique [Pacote atualizado da ECD](https://suporte.totvs.com/portal/p/10098/download?e=955972) seguindo as instruções [Aqui descritas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* Veja [os Blocos I150 e I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007744371-MP-SIGACTB-ECD-Registro-Blocos-I150-e-I155-?source=search)
* **rpocustom.rpo renomeado**
* **customização desativada**[Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus?source=search)
* renomeia o arquivo respecd\_01 , da pasta Profiler
* **Execute o Diagnóstico**

  + Execute o  [**\*Diagnóstico de Dicionário\***](https://tdn.totvs.com/pages/releaseview.action?pageId=725728577)**pois ele p**ermite fazer uma verificação na base em busca de possíveis erros que podem causar problemas na base ou impedir a correta execução de rotinas de atualização , como UPDDISTR por exemplo. Utilizando a rotina de Diagnostico é possível identificar problemas de integridade para uma tabela especifica em sua base de dados , que podem estar ocasionando erros.
* **Aplique o Pacote Acumulado Contábil + [Instalação de Procedure nele existente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410951-MP-SIGACTB-SIGAATF-Instala%C3%A7%C3%A3o-de-Procedure-?source=search):**

  [**Pacotes de Atualização - Contabilidade**](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)

**Solução**

# Verifique quanto aos procedimentos que seguem

|  |  |
| --- | --- |
| **Ocorrência:** | ECD não gera registros I350 / I355    Pode ser aplicado também para os registros I150 e I155 |
| **Ambiente:** | SIGACTB |
| **Passo a passo:** | 1)  Pela própria rotina Central de Escrituração verifique na tabela CSA (CSA\_INDTIP) se foi gerado na coluna **Indic. Lcto** a letra E no último registro que deve ser o último dia do mês em que foi feito a apuração do exercício.    2) Caso não esteja preenchida favor verificar os passos abaixo:       2.1)  Os registros só são gerados para contas de resultados, Despesa e Receita (que possuam movimentos).       2.2)  É necessário que o campo CT1\_NTSPED esteja configurado corretamente para as contas de Receita e Despesas, como Contas de Resultado.        2.3)  É necessário que exista na tabela CW0 a tabela LP a chave com data da apuração, para cada filial apurada (EX: CW0\_TABELA = LP, CW0\_CHAVE = 0101 (empresa+filial), CW0\_DESC01 = 20151231011Z (data da apuração+moeda+tipo de saldo+ Z) 20151231 01 1 Z = (zerado)). Se a apuração foi feita apenas para uma determinada filial (exemplo: Filial de: 01 Filial Até: 01), na tabela LP deverá conter um único registro referente a esta filial. Caso a apuração tenha sido feita para diversas filiais (exemplo: Filial de: 01 Filial Até: 99) a tabela CW0 deverá conter um registro para cada filial, determinada no campo CW0\_CHAVE.        2.4) As contas de resultado devem estar zeradas (apuradas) tanto na CT2 (Razão Contábil - CTBR400), quanto na CT7 (Balancete -  CTBR040)        2.5) É necessário existir na tabela CT2 o campo CT2\_DTLP preenchido. Este campo é alimentado quando executado a rotina CTBA211 (Apuração de Resultados).  2.6) Não podem existir lançamentos "manuais" de transferência de saldo da conta de apuração para o Passivo (através das rotinas CTBA101 ou CTBA102). Todo processo de Apuração de Resultados deve ser feito pela rotina CTBA211. Para isso Verificar o campo CT2\_ROTINA:           2.7) Caso os itens mencionados acima estejam de acordo, será preciso reprocessar os saldos contábeis (rotina Reprocessamento - CTBA190) no mínimo a partir de 01/01/14, pois os registros I350 e I355 são referentes a saldos anteriores.       2.8) Em alguns casos, poderá ser necessário estornar a apuração de resultados e apurar novamente, para que os registros sejam criados corretamente.  3) Caso tenha sido gerado verifique na SX2 se o compartilhamento das tabelas CSA e CSB estão correspondentes:    4) Abra as tabelas em TOP (APSDU) e verifique como a revisão gravou os campos CSA\_FILIAL e CSB\_FILIAL:      5) Caso haja divergência será necessária manutenção para ambos os compartilhamentos/preenchimentos ficarem da mesma forma e o fonte conseguir localizar os registros e exporta-los para o arquivo TXT. |
| **Observações:** | Obs.: o compartilhamento de todas as tabelas da família [TABELAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026989572-MP-SIGACTB-TABELAS-ECD-E-ECF?source=search) CS´s devem ser iguais para que as informações saiam corretamente no arquivo .TXT. |

Importante :

[EMPRESA CONSOLIDADORA COMO GERAR REGISTROS I350 - I355 - I150 - I155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045923434-MP-SIGACTB-ECD-EMPRESA-CONSOLIDADORA-COMO-GERAR-REGISTROS-I350-I355-I150-I155-?source=search)

[I155 trás contas que tiveram movimentações em anos anteriores porém estão com saldos zerados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028711472-MP-SIGACTB-ECD-I155-tr%C3%A1s-contas-que-tiveram-movimenta%C3%A7%C3%B5es-em-anos-anteriores-por%C3%A9m-est%C3%A3o-com-saldos-zerados?source=search)

[I155 Pelo menos um dos campos (saldo inicial, total de débitos, total de créditos ou saldo final) deve conter valor diferente de zero.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028360771-MP-SIGACTB-ECD-I155-Pelo-menos-um-dos-campos-saldo-inicial-total-de-d%C3%A9bitos-total-de-cr%C3%A9ditos-ou-saldo-final-deve-conter-valor-diferente-de-zero-?source=search)

[ECD registro J150 - 7-VL\_CTA e 2-COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-registro-J150-7-VL-CTA-e-2-COD-AGL?source=search)
