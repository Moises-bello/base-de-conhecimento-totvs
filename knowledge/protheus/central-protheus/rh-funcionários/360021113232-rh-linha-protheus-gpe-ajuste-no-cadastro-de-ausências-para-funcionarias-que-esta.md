---
article_id: 360021113232
category: RH - Funcionários
content_hash: 2f85775b81fccb05ea14d8d6b1108dba074ab36a9cc69f0b2c95583a947e3c44
fetched_at: '2026-06-28T22:43:27.323516+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Ajuste no cadastro de ausências para funcionarias
  que estavam de férias e entraram de licença maternidade
type: support-article
updated_at: '2025-08-04T19:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021113232-RH-Linha-Protheus-GPE-Ajuste-no-cadastro-de-aus%C3%AAncias-para-funcionarias-que-estavam-de-f%C3%A9rias-e-entraram-de-licen%C3%A7a-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33939101411095) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Em situação que a funcionária estava no período de férias e entra de licença maternidade, o período de férias no cadastro de afastamento deve ser ajustado, mas o sistema não permite a alteração do afastamento das férias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Será necessário realizar ajuste no cadastro de afastamento para permitir alteração do campo **R8\_STATUS**.

Quando for necessário ajustar o período de férias cadastrado devido situação que a funcionária entra de licença maternidade durante o gozo das férias, o registro das férias deverá ter o campo **Status** preenchido com **Calculado** e a **Data Final Afastamento** das férias ajustada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412015809687)

No exemplo abaixo a funcionária teve gozo de férias a partir do dia 07/11/2022 porém entrou em licença maternidade dia 22/11/2022. Alteramos o campo **Data fim Afastamento** para **21/11/2022** e o campo **Status** para **Calculado.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412065999127)

Depois do ajuste do lançamento das férias, deverá ser incluído o registro da licença maternidade normalmente com a data do afastamento 22/11/2022.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10412233886999)

Após a funcionária voltar da licença maternidade realize o lançamento do outro registro de férias com os dias de gozo restante, e com o campo ***Status***preenchido com **Calculado.**   
  
**Obs.: A configuração "calculado" do campo "*Status*" somente deverá ser utilizada para os casos de ajuste no registro de férias.**  
  
Os dias que foram pagos a mais por causa da interrupção das férias devem ser lançados após o afastamento por licença maternidade. Este afastamento deve ser lançado com o tipo 001 (Férias) com os dias restantes que foram pagos a mais no início da licença maternidade.   
  
É importante que o funcionário seja informado que receberá o valor a maior por causa da interrupção das férias que não estavam programadas, mas este valor será abatido após o seu retorno.    
  
**Exemplo:**  
Férias: 07/11 à 06/12  
Afastamento de férias: 07/11 à 06/12  
Licença Maternidade: 22/11 à 20/03  
  
No cálculo da folha de Novembro será pago 30 dias de férias e 10 dias de licença maternidade (pagamento de 10 dias a mais que será descontado após o retorno)  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Sequência de afastamento Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050439054-RH-Linha-Protheus-GPE-Sequ%C3%AAncia-de-afastamento-Licen%C3%A7a-Maternidade?source=search)  
[RH - Linha Protheus - GPE - Como lançar ausência por Licença Maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053399713-RH-Linha-Protheus-GPE-Como-lan%C3%A7ar-aus%C3%AAncia-por-Licen%C3%A7a-Maternidade-?source=search)  
[RH - Linha Protheus - GPE - Como configurar Licença Maternidade por Adoção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051079813-RH-Linha-Protheus-GPE-Como-configurar-Licen%C3%A7a-Maternidade-por-Ado%C3%A7%C3%A3o?source=search)
