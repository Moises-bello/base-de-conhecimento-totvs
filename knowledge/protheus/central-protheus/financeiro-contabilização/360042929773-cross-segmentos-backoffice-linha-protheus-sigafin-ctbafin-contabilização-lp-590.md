---
article_id: 360042929773
category: Financeiro - Contabilização
content_hash: b69caeecf09acf84dfd9eefe6b96c821b860e15994f77072b6a9c03cb39610e6
fetched_at: '2026-06-28T22:38:05.327110+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Contabilização
  LP 590 com a data do campo EF_LIBER e o LP 566 '
type: support-article
updated_at: '2022-07-28T00:57:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042929773-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Contabiliza%C3%A7%C3%A3o-LP-590-com-a-data-do-campo-EF-LIBER-e-o-LP-566
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03 min  
  
Dúvida**Como efetuar a contabilização do LP 590 mais a  data do campo EF\_LIBER E O LP 566 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - Todas as versões  
  
**Solução**Ao contabilizar *off-line* o LP 566, o sistema está posicionado no registro do cheque aglutinador na tabela **SEF** podendo utilizar os campos da própria tabela, exemplo **EF\_VALOR**.

Ao contabilizar *off-line* o LP 590, o sistema primeiramente posiciona nos registros da **SEF** de cada título, bem como no registro da **SE2** do título correspondente, podendo utilizar os campos da própria tabela **SEF**, exemplo **EF\_VALOR**. E ao final alimenta a variável **VALOR** com o valor do cheque aglutinador, pois neste momento estão disposicionados as tabelas **SEF** e **SE2** permitindo contabilizar ou não o cheque aglutinador.

**Exemplo**TIT A no valor 1000,00 e o TIT B no valor de 2000,00, ao realizar uma baixa automática desses dois títulos com o motivo de baixa Normal e informando o número de cheque 0001, sistema irá gravar na **SEF** três registros para o cheque 0001:

1º registro referente ao TIT A no valor de 1000,00, FORNECEDOR A.

2º registro referente ao TIT B no valor de 2000,00, FORNECEDOR B.

3º registro referente ao total do cheque no valor de 3000,00.

No momento da contabilização serão chamados os três registros, pois o cliente pode DEBITAR o valor de cada título em seus respectivos fornecedores e CREDITAR o total do cheque no banco na geração do cheque, isso será tratado na configuração do Lançamento Padrão.

A rotina **Contábil** *Off Line* não valida o campo **EF\_LIBER**, ou seja, não verifique se o cheque a pagar foi ou não liberado, e sim se o cheque foi gerado. Devido isso, que é contabilizado a geração do cheque.

Através do **Lançamento Padrão** 566, é contabilizado *Offline* Geração de Cheque de Títulos a Pagar Aberto, que é gerado pela rotina **Cheques S/ Título**(**FINA390**).

O **Lançamento Padrão** 590 contabiliza *Offline* Geração de Cheque de Títulos Baixado, gerado pela rotina **Baixa Pagar Manual**(**FINA080**)

Para efetuar Liberação do cheque a pagar manualmente, o parâmetro **MV\_LIBCHEQ** deve ser preenchido igual N.

Através do parâmetro **MV\_SLDBXCR**, é possível gerar movimento bancário de títulos a receber apenas quando o cheque for compensado. Neste caso deve preencher C no parâmetro **MV\_SLDBXCR**, e com isso será ativado o botão **Compensar** na rotina **Cheques Recebido**s, conforme a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056759574/mceclip0.png)

**Observação:**

Após compensar o cheque, será preenchido na tabela **SEF**(**Cheques**) no campo **EF\_DTCOMP**, a data base que foi feito compensação do cheque recebidos.

**Saiba mais:**  
Segue o link dos pontos de entrada da rotina que talvez pode lhe auxiliar.  
[https://tdn.totvs.com/display/public/PROT/FIN0084\_CPAG\_Pontos\_de\_Entrada\_FINA190](https://www.google.com/url?q=https://tdn.totvs.com/display/public/PROT/FIN0084_CPAG_Pontos_de_Entrada_FINA190&sa=D&source=hangouts&ust=1580838287543000&usg=AFQjCNGg8EF19i-lOBOElgZK5ygpddzOKQ)
