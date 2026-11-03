---
article_id: 360006602612
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 3e262f4c0f19be57e442ffd5e2a9c54eb88a7713c1c1169a5e6853a425b960e9
fetched_at: '2026-06-28T22:41:43.270163+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 mensagem 050UTDEPR
  no ativo fixo
type: support-article
updated_at: '2025-05-09T18:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006602612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-mensagem-050UTDEPR-no-ativo-fixo
---

**Ocorrência:**Na execução das rotinas de Cálculo de Depreciação (ATFA050) ou Descálculo de Depreciação (ATFA070) é apresentada a mensagem "05OUTDEPR":  
  
![05OUTDEPR.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360007102992)  
  
  
**Ambiente:**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - Versão  12

**Causas:**A mensagem é apresentada devido a existência de movimentos de depreciação, baixa e/ou transferências na mesma data do cálculo e/ou em data posterior, ou devido a queda de energia, *errorlog* ou *perda de conexão* durante o **Cálculo**.

Outra causa para esta mensagem ocorrer em outros processos no ativo, é o compartilhamento das tabelas  **FN6, FN7 FN8 e FN9** diferentes das tabelas **SN1, SN2, SN3, SN4 e SN5**. 

As tabelas FN's devem ter e mesmo modo de compartilhamento das tabelas SN's do ativo.

Tipos de **movimentos que impedem o Cálculo e/ou Descalculo**:

* -**N4\_OCORR= "01", "03", "04", "06" e "20"**  
  [ATF0014 - Tipos de movimentos N4\_OCORR](http://tdn.totvs.com/display/public/PROT/ATF0014+-+Tipos+de+movimentos+N4_OCORR)
* **N5\_TIPO= "4", "K", "L" e "Y"**  
  [Conteudo do campo Tipo Registro N5\_TIPO](http://tdn.totvs.com/display/public/PROT/Conteudo+do+campo+Tipo+Registro+N5_TIPO+--+116166)

**Ex.: Cenário : realizando calculo de depreciação de 28/02/15 , ocorreu uma interrupção:**

* Ultima depreciação realizada MV\_ULTDEPR = 31/01/15
* Últimos movimentos existentes nas tabelas SN4 e SN5 – movimento de depreciação 31/01/15
* Através da rotina ATFA050 foi realizado o calculo 28/02/15
* O processo foi interrompido devido algum problema (queda de energia, queda de sistema..)
* O parâmetro MV\_ULTDEPR = 31/01/15  permaneceu com a mesma data após a interrupção do calculo
* Porém os últimos movimentos de depreciação nas tabelas SN4 e SN5 –  ficaram com a data  28/02/15
* Ao tentar realizar a depreciação com a data 28/02/15 o sistema não permite , apresentando assim a mensagem "050UTDEPR"

**Solução:**Nos casos onde ocorre queda do *sistema/error.log* durante o processo de **Depreciação** **(ATFA050)**, é necessário atualizar manualmente o parâmetro *MV\_ULTDEPR* para o período que estava em processamento, e executar o **Descálculo Mensal (ATFA070)** para o período.

Desta forma, o sistema estornará as depreciações efetuadas até a queda do sistema.

**Porém, caso a mensagem ainda persista, será necessário efetuar ajuste manual no ambiente, onde deverá seguir as orientações abaixo:**

* Verificar a existência de movimentos de depreciação, com data posterior da informada no parâmetro *MV\_ULTDEPR*, nas tabelas *SN4* e *SN5*;
* Neste caso, deverá cancelar as baixas e transferências realizadas em data posterior;
* Lembrando, para que possa cancelar as transferências, é necessário avaliar a configuração do parâmetro *MV\_ATFCATR*.

**Ex.: Continuando o exemplo do erro inicial , onde durante o calculo de depreciação de 28/02/15, ocorreu uma interrupção**

1. Emita o relatório ATFR150 (movimentos) e verifique os últimos registros de depreciação (ex: 28/02/15) ou movimento que posteriores ao último calculo;
2. Altere o parâmetro para MV\_ULTDEPR para data  28/02/15
3. Através da rotina ATFA070 – execute o Descálculo de depreciação – para que o sistema estorne as depreciações realizadas para alguns bens;
4. Verifique se os lançamento existente nas Tabelas SN4 e SN5 foram descálculados
5. Através da rotina ATFA050 – Realize a depreciação novamente

**Observação :**  
[ATFA070 QUANTOS DESCALCULOS DE DEPRECIAÇÃO O SISTEMA PERMITIR REALIZAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020379891-MP-SIGAATF-ATFA070-QUANTOS-DESCALCULOS-DE-DEPRECIA%C3%87%C3%83O-O-SISTEMA-PERMITIR-REALIZAR-?source=search)

[COMPARTILHAMENTO DAS TABELAS FNs no P12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006982571-MP-SIGAATF-COMPARTILHAMENTO-DAS-TABELAS-FNs-no-P12?source=search)

[Quais as opções que existem de preenchimento do campo N5\_TIPO.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017722312-MP-SIGAATF-Quais-as-op%C3%A7%C3%B5es-que-existem-de-preenchimento-do-campo-N5-TIPO-?source=search)  
[O QUE TRATA O CAMPO N4\_OCORR ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-MP-SIGAATF-O-QUE-TRATA-O-CAMPO-N4-OCORR-?source=search)

**Informações Relacionadas:**-Cálculo de Depreciação (ATFA050) e Descalculo da Depreciação (ATFA070):<http://tdn.totvs.com/display/public/PROT/ATF0006_QUEDA_ERRO_05OUTDEPR_CALCULO_MENSAL_ATFA050>-Cancelamento da Transferência de Bens (ATFA060):  
<http://tdn.totvs.com/display/PROT/ATF0029_Regra_do_Cancelamento_da_Tranferencia>  
  
-Configurações do parâmetro MV\_ULTDEPR:  
<http://tdn.totvs.com/pages/releaseview.action?pageId=6067587>
