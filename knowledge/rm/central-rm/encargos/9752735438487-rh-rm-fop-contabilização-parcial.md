---
article_id: 9752735438487
category: Encargos
content_hash: bf19557bec3238d3b290804bba05d2c55e4f94ff035b2a6af96f3581fae9cd06
fetched_at: '2026-06-28T22:46:52.419104+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Contabilização parcial
type: support-article
updated_at: '2025-03-11T10:35:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9752735438487-RH-RM-FOP-Contabiliza%C3%A7%C3%A3o-parcial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a contabilização parcial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A contabilização parcial é considerada quando a empresa trabalha com apenas uma conta de debito ou  uma conta de credito para classificar eventos ou encargos.

A parametrização dos grupos contábeis terá o mesmo tratamento de uma contabilização normal.

- Terá que criar os Grupos na Tabela Dinâmicas (GRPCONT);

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9750123943063)

- Caso a empresa trabalha com integração Contábil, terá que criar o grupo CODINTCONT na Tabela Dinâmica, de acordo com a distribuição da empresa;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9757491089303)

Informar os códigos da integração contábil em todas as seções ou centro de custo.

Caso a empresa não trabalha com integração contábil, desconsiderar a parametrização.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9752534916119)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9758145088791)  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9752568408343)

Nos eventos informar as respectivas contas de Débito ou de  Crédito, marcar a flag contabilização parcial em todos os eventos da folha de pagamento.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9752931410711)  
  
Quando a empresa trabalha com contabilização parcial, para que seja realizado o fechamento da conta débito com a conta credito, terá que criar um Encargo, através de formula, onde a mesma irá retornar o valor liquido da folha de pagamento, segue um exemplo de formula onde a mesma irá retornar o valor liquido acumulado do mês.

Exemplo de contabilização parcial:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9752610090007)  
Segue exemplo de uma formula para retornar o período 1 da folha.  
Veja exemplos referente aos períodos da variável  
  
**Função LIQUIDOFF**  
Função que apresenta o líquido do funcionário em um determinado ano, mês e período  
LIQUIDOFF (VALOR, VALOR, VALOR)  
Onde:  
1º parâmetro é o ano  
2º parâmetro é o mês  
3º parâmetro é o período.   
  
  
**Exemplo**  
LIQUIDOFF (2013, 8, 2) O sistema apresentará o líquido do funcionário do período 2 de 08/2013.  
  
**Observação:**  
Caso o usuário deseja o líquido de todos os períodos, deve-se informar o valor 0 (zero) no 3º parâmetro da função.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9757892158231)

Criar o encargo que será a contrapartida e associar um código ativo ao mesmo:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9750903733271)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9751314358423)  
  
Gerar o Histórico de provisão, encargos e gerar o lançamento:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9751055059735)

Dessa forma o lançamento será gerado:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9758357760279)
