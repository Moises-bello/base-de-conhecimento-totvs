---
content_hash: d016f430218e06937eca1175933950d3922183224c2d44e2064faa492a3ce952
fetched_at: '2026-06-29T00:09:53.788467+00:00'
page_id: '441821682'
product: rm
source: tdn-rm
title: Ressarcimento/Complemento de ICMS ST - São Paulo (CAT 42)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=441821682
version: 13
---

Será necessário apurar os valores de ICMSST suportado na entrada com os valores efetivos da saída por período e por produto para então calcular o valor de ressarcimento ou complemento de ICMSST. 

Encerramento do Período de Apuração

Para as filiais que estiverem com o parâmetro *"Controla Ressarcimento de ICMS ST"* marcado, o calculo será realizado automaticamente durante o encerramento do período de apuração de ICMSST, considerando todas as entradas nas quais ocorreu antecipação ou substituição de ICMSST e as saída dos produtos cujo a tributação foi suportada na entrada.

1. Serão selecionadas as movimentações de entrada e saída com DATALF compreendida no período que está sendo encerrado e com produtos cuja opção "Tributado pelo ICMS-ST" esteja marcada para o estado da Filial no cadastro do produto Anexo "Dados Fiscais por UF"
2. Serão selecionados Lançamentos associados aos CFOPs cujo Flag "FISCAL" esteja marcado e não serão considerados lançamentos cancelados.
3. Para cada lançamento de entrada selecionado, cujo item tenha valor de ICMS-ST maior do que Zero (0), deverá ser incluído um registro na DPERIODORESSARCIMENTOICMSST conforme abaixo:

   1. NUMITEM: Número do Item no Lançamento Fiscal
   2. QUANTIDADE: Quantidade do Item no Lançamento Fiscal
   3. VLRUNSUPORTADO: Valor unitário do ICMSST + ICMS suportado na compra ((DITEM.VLRICMSSTPRD + DITEM.VLRICMSPRD) / QUANTIDADE)
      * Cada operação gerará um valor do ICMS suportado pelo contribuinte. Este item será a soma de todos os valores de ICMS que compõe a operação.
      * Nas hipóteses de aquisição de mercadoria de substituído, o ICMS suportado será o declarado pelo remetente em informações complementares e nas TAG´s especificas do grupo da NF-e <ICMS60> (Este valor estará no campo de Valor do ST).
      * No caso de incidência do FECP o mesmo deverá ser considerado na composição do ICMS Suportado. Como a orientação neste caso é majorar a alíquota do ST, o valor do FECP já está incluso no valor do ICMS-ST.
   4. VLRUNCONFRONTO: zero
   5. VLRTOTSUPORTADO: Valor total do suportado na compra (VLRUNSUPORTADO \* QUANTIDADE)
   6. VLRTOTCONFRONTO: zero
   7. VLRRESSARCIMENTOAPURADO: zero
   8. ENQUADRAMENTOLEGAL: em branco
4. Serão selecionados lançamento de saída que estejam nas regras 1 e 2 cujos itens tenham referência com itens de entrada. Para cada lançamento de saída selecionado deverá ser incluído um registro na DPERIODORESSARCIMENTOICMSST conforme abaixo:  
   1. NUMITEM: Número do Item no Lançamento Fiscal
   2. QUANTIDADE: Quantidade do Item no Lançamento Fiscal
   3. VLRUNSUPORTADO: Valor unitário do ICMS total suportado na compra
      * O item do lançamento de saída deverá ser referenciado a um ou mais itens dos lançamentos de entrada
      * No caso de incidência do FECP, o mesmo deverá ser considerado na composição do ICMS Suportado. Como a orientação neste caso é majorar a alíquota do ST, o valor do FECP já está incluso no valor do ICMS-ST.
      * O valor unitário suportado será uma média ponderada entre os itens de compra referenciados: **(****(****(**"Valor do ST da Compra" + "Valor do ICMS da Compra"**)** / "Quantidade da Venda"**)** / "Quantidade da Compra"**)** \* "Quantidade Referenciada na nota de Saída".
   4. VLRUNCONFRONTO:
      1. O valor deverá ser calculado nos casos abaixo conforme a seguinte regra: Valor unitário do ICMSST + ICMS na operação ((DITEM.VLRICMSSTPRD + DITEM.VLRICMSPRD) / QUANTIDADE) (No caso de incidência do FECP o mesmo já está sendo considerado na composição do ICMS de Confronto, uma vez que a alíquota está majorada)  
         * Operação destinada a consumidor final; **OU**
         * Operação destinada à pessoa jurídica amparada pela isenção.
      2. Para operações **"Isentas"** ou **"Não Incidência"** com a Flag **consumidor Final marcada**, e **Pessoa Jurídica,** será aplicado o seguinte Cálculo:   
         **((Isento ICMS \* Alíquota) + Valor de ICMS ST) / Quantidade**
      3. Quando a operação for **interestadual** destinada à**pessoa jurídica** o valor de confronto será o valor do ICMS unitário das compras relacionadas (item da entrada referenciado, campo DITEM.VLRICMSPRD); e deverá ser lançado como crédito de ICMS (o usuário deverá criar um lançamento de ajuste manualmente);
      4. Caso não se encaixe nos casos acima, será calculado de acordo com o item "i".
   5. VLRTOTSUPORTADO: Valor total do ICMS suportado na compra (VLRUNSUPORTADO \* QUANTIDADE)
   6. VLRTOTCONFRONTO: Valor total do ICMS na operação (VLRUNCONFRONTO \* QUANTIDADE)
   7. VLRRESSARCIMENTOAPURADO: Gerar apenas para lançamentos de saída deverá receber o resultado da conta VLRTOTSUPORTADO - VLRTOTCONFRONTO. Se o resultado for positivo existe valor para ressarcimento, se for negativo o valor será de complemento. O valor será gravado no Banco de Dados com sinal.
   8. ENQUADRAMENTOLEGAL:   
      **Se**Operação com Ressarcimento/Complemento de ST desmarcado  
      **Então**0

      **Senão Se**Regra ICMS Isento OU Não incidência **Então**3  
        
      **Senão Se**Venda Interestadual  
      **Então**4

      **Senão****Se** Consumidor Final  
      **Então** 1

      **Senão****Então**2

Abertura do Período de Apuração

Ao abrir o Período de Apuração, os registros criados na tabela DPERIODORESSARCIMENTOICMSST serão apagados.

Outras Informações relacionadas
