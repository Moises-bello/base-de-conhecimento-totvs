---
article_id: 360058922053
category: RH - Ponto Eletrônico
content_hash: 5203ad82f28381f6f8c927986b43e4832b03a20682912efb34cabd266213bf00
fetched_at: '2026-06-28T22:44:58.315081+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Forma correta de cadastro para valorizar evento
  de Banco de Horas
type: support-article
updated_at: '2021-10-01T17:07:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058922053-RH-Linha-Protheus-PON-Forma-correta-de-cadastro-para-valorizar-evento-de-Banco-de-Horas
---

**Dúvida**Como valorizar um evento de banco de horas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**No cadastro dos eventos no Ponto Eletrônico, temos duas formas de cadastro para calcular o evento.   
A primeira é com uma **Verba de Folha de Pagamento** para, após o Cálculo Mensal, contabilizar a verba em Resultados e consequentemente integrar com a tabela RGB - Pré-Cálculo de Folha.  
A segunda possibilidade, é cadastrar o **evento** para **Banco de Horas**, onde após o Cálculo Mensal, será lançado o evento e somará o saldo de Banco até que, o Fechamento seja efetuado.    
  
Porém, algumas dúvidas sempre surgem de como cadastrar os eventos para Banco de Horas de forma correta e, que a valorização seja feita de maneira exata.  
  
Segue abaixo, **como devem ser cadastrados os eventos para que contabilizem corretamente no Banco de Horas e some no saldo valorizado de Banco de Horas**.  
  
Eventos de provento, como Hora Extra e Adicional Noturno:  
Hora Extra 100%:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099150753/mceclip0.png)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096835174/mceclip1.png)  
  
Detalhe **importante**:  
Veja o **exemplo** acima, de um evento **Hora Extra 100%**, ou seja, **valorizando** em **100%.**   
No **campo Percentual** é necessário cadastrar 100 + 100 = **200%**, ou seja, sempre somar a valorização a 100% assim como o cadastramento de verbas.  
  
Consequentemente, se tivermos um evento de Hora Extra a 50%, o campo Percentual terá 150 no cadastro, assim como se tivermos um evento de Provento que não tenha valorização, o campo será cadastrado como apenas 100%, ou seja, sempre 100 + a valorização.  
  
Eventos de **desconto**, sempre **cadastrar** com a **valorização** em **100**, pois com isso, no momento do Cálculo de Banco de Horas, teremos o desconto do absenteísmo sendo deduzido 1 por 1, ou seja, sendo diminuído do saldo valorizado do funcionário.  
  
Exemplo de evento de atraso:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151093/mceclip2.png)  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151113/mceclip3.png)  
  
Assim, quando a Hora Extra e o Atraso for contabilizado e calculado nos lançamentos do funcionário, o saldo valorizado estará como exemplifico abaixo, sendo um exemplo de um funcionário que fez um dia de 2 horas extras a 100% e no dia seguinte teve dois atrasos de 2 horas para compensação:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151553/mceclip5.png)  
  
**Após o reapontamento e o cálculo mensal**, teremos dessa forma nos lançamentos de Banco de Horas:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151613/mceclip6.png)  
  
Assim, quando realizar o Fechamento de Banco de Horas, na opção por Horas Valorizadas, teremos a seguinte situação no Lançamentos de Resultados para o funcionário em questão:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151693/mceclip7.png)  
  
Impressão do Relatório de Banco de Horas:  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096836134/mceclip8.png)  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099151793/mceclip9.png)  
  
Veja que nessa opção Horas Valorizadas, tanto o evento de Provento (Hora Extra) quanto o evento de Desconto (Atraso) são impressos no relatório de Banco de Horas.  
  
**Saiba Mais**Para mais documentações, acesse a **Carolina** via Protheus ou Central de Atendimento.  
Veja como acessar: <https://www.youtube.com/watch?v=T7b4zMlphTI>
