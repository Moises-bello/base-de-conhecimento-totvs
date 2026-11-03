---
content_hash: ed78a4564a7711af5a2924a3929e96a606d7d8e592354df8fffe3c6a85f95dba
fetched_at: '2026-06-29T00:10:08.071384+00:00'
page_id: '452719506'
product: rm
source: tdn-rm
title: Lançamento de Decimo Terceiro Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719506
version: 2
---

O 13º salário é uma gratificação natalina que pode ser paga em duas parcelas a todos os empregados. A primeira parcela é paga entre os meses de fevereiro e novembro de cada ano, e a segunda, até o dia 20 de dezembro. Dependerá da convenção coletiva da empresa. Se na convenção coletiva, nada for citado, prevalecerá o pagamento em duas parcelas.

Este processo irá lançar o pagamento da primeira e/ou segunda parcela. O sistema fará o cálculo e o lançamento automaticamente. O cálculo do 13º salário está relacionado aos parâmetros do sindicato em Administração de Pessoal| Sindicatos | Pasta 13ºSalário e aos parâmetros existentes em Configuração| Parametrizador| 13º Salário.  
 **1º Parcela:**   
 Na primeira parcela o sistema irá lançar o evento com código de cálculo 9.Para o lançamento da 1a parcela de 13o salário, o sistema busca o primeiro evento que tenha o CC 9 - 1ª Parcela de 13º Salário que ele encontrar, pois o sistema considera que deve haver apenas um evento para o cálculo da primeira parcela. O campo Ajustar 1º parcela já vem marcando.  
 O parâmetro Ajustar 1º parcela funciona da seguinte forma:   
 Suponhamos que a folha de pagamento esteja sendo processada em 11/2013 e que determinado funcionário tenha um aumento de seu salário R$ 1000,00 para R$1500,00 neste período. Se este funcionário já tiver tido a primeira parcela do 13º salário lançada em 06/2013, que no caso foi de R$ 500,00 e o parâmetro "**Utiliza Salário Atual para 1ª Parcela**" estiver marcado), o sistema irá fazer a reajuste da 1º parcela lançando os eventos abaixo:  
  -1ª Parcela de 13º Salário (Código de Cálculo 9) R$ 750,00 (Provento)  
  -Adiantamento de 13º Salário (Código de Cálculo 35) R$ 500,00 (Desconto)  
    
    
 **2ª Parcela**:  
    
 Selecionando a 2º parcela o sistema irá lançar o evento com código de cálculo 102(Segunda Parcela de 13º) e descontar o que já foi pago no evento com código de cálculo 35(Adiantamento de 13º).  
  **Lança Códigos Fixos**   
 Ao selecionar esta opção o sistema lançará os códigos fixos selecionados em Configurações l Parametrizador l 13º salário l Código Fixos  
 **Lança eventos programados**  
 Ao selecionar esta opção o sistema lançará os eventos programados selecionados em Configurações l Parametrizador l 13º salário l Eventos Programados  
 **Atenção:**  
 -Para os funcionários que foram admitidos até o dia 17 de janeiro (inclusive), o sistema calculará metade do salário. O salário poderá ser o do mês atual ou o do mês anterior, conforme definido em Configuração | Parametrizador| 13º Salário.  
 -Para os funcionários admitidos após 17 de janeiro, o sistema calculará o número de avos a que o funcionário tem direito conforme informado em Configuração | Parametrizador| 13º Salário.

* Funcionário comissionista, será efetuado o cálculo da média ou considerado o mínimo garantido do sindicato.
* A empresa não poderá estar trabalhando com as médias discriminadas apenas no 13º Salário ou apenas no 13º Rescisão, pois afeta o cálculo de INSS de ambas as partes.
* Lançamento de pensão alimentícia poderá ser feito através dos códigos fixos, lembrando que o evento deverá ter CC120.  
      
     -Para funcionários afastados por acidente de trabalho, o 13º será pago integralmente. Para descontar o 13º pago pela previdência, deverá ser lançado na movimentação do mês de dezembro, o evento de desconto com CC 101, com o valor de 13º pago pela previdência.  
   -O evento com CC 101 é um evento de Desconto tipo Valor. O valor informado neste código de cálculo será deduzido também da base de cálculo do 13º salário para o cálculo do IRRF e INSS.  
   -Para funcionários afastados pela previdência, o 13º será pago somente sobre os avos aos quais o funcionário terá direito. As incidências do FGTS, INSS, IRRF serão somente sobre o valor pago pelo sistema ao funcionário.  
   No Lançamento de 13º salário para afastados por previdência a contagem de avos será a partir do início do afastamento + 15 dias (empresa paga estes dias como atestado médico)  
   **Exemplo:**  
   1º afastamento = 03/01/2013 a 30/03/2013 = previdência social  
   2º afastamento = 05/11/2013 a sem "retorno" = previdência social  
   No 1º afastamento será considerado para contagem de avos: 03/01/2013 + 15 = 18/01/2013, portanto o funcionário terá direito ao avo deste mês (janeiro).  
   No 2º afastamento será considerado para contagem de avos: 05/11/2013 + 15 = 20/11/2013, portanto o funcionário terá direito ao avo deste mês (novembro).  
   Os avos perdidos: Meses de fevereiro, março e dezembro.  
   O Total de avos de direito: 9 avos.  
      
   \_Toc275336728-Para funcionárias que tiveram dias de afastamento por licença maternidade durante o ano o sistema irá calcular o valor normalmente (como é calculado para os demais funcionários), porém irá lançar um evento base de cálculo com código de cálculo 322 (2º parcela 13º salário Licença Maternidade) com o valor de 8/12 avos.
* No dia 20/12 deverá ser gerado SEFIP de 13º (módulo "Relatórios | SEFIP"), marcando o campo "SEFIP 13", Informe o percentual de INSS recolhido pela empresa. Este SEFIP não gera recolhimento de        FGTS, pois ele é utilizado apenas para declaração do valor de INSS de 13º salário que foi pago pela      empresa na guia de GPS 13 no dia 20/12.
