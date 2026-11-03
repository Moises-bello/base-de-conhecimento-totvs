---
article_id: 20039309735191
category: eSocial - Gerar XML/ Integração Evento
content_hash: c7105a0aef210726d292c93b545dca45be416795f46011d39a1fa870b39c0449
fetched_at: '2026-06-28T22:47:12.008759+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como cadastrar assistência de saúde nas férias do
  funcionário para correta geração da incidência no XML S-1210
type: support-article
updated_at: '2026-03-03T18:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20039309735191-RH-RM-FOP-eSocial-Como-cadastrar-assist%C3%AAncia-de-sa%C3%BAde-nas-f%C3%A9rias-do-funcion%C3%A1rio-para-correta-gera%C3%A7%C3%A3o-da-incid%C3%AAncia-no-XML-S-1210
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20039313364887)**Tempo aproximado para leitura**: 00:03:00 min**  
  
**Dúvida**  
Como cadastrar assistência de saúde nas férias do funcionário para correta geração da incidência no XML S-1210?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Solução**

Ao gerar o XML S-1210 a partir do leiaute S-1.2 é gerada a informação do Plano de Saúde do Titular e do Dependente.  
Para a correta geração do evento S-1210, quando o funcionário possuir férias, realize os seguintes passos:

1. Acesse **eSocial | Operadora Saúde | Cadastro Operadora de Saúde**, e verifique se os eventos relacionados à Operadora de Saúde com Natureza da Rubrica eSocial igual à 9219 para consideração para o eSocial e CC14 para consideração na DIRF constam salvos. Para mais informações de como acessar os eventos na Operadora de Saúde [CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003869592-RH-RM-FOP-eSocial-Operadoras-de-plano-de-sa%C3%BAde-no-eSocial?source=search);

2. Após, crie um novo evento coma Natureza de Rubrica eSocial diferente à 9219 e sem código de cálculo (este novo evento não deverá ser informado na Operadora de Saúde);

3. Acesse **Configurações | Parametrizador | Férias | Eventos Adicionais Globais** e informe os campos **Evento de Recibo** e **Eventos da Folha**;

No exemplo abaixo:

* Evento de Recibo = Evento com Natureza de Rubrica eSocial 9219 e CC14 (Evento 0014);
* Eventos da Folha = Evento com Natureza de Rubrica eSocial diferente de 9219 e sem código de cálculo (Evento 9014).

![](https://tdn.totvs.com/download/attachments/776113025/image-2023-12-21_16-3-33.png?version=1&modificationDate=1703185413394&api=v2)

4. Acesse o Cadastro do Titular - Anexos - Históricos - Histórico Assistência Saúde e verifique se o histórico foi preenchido com as devidas informações do titular e do dependente. O tipo de movimento será '1-Férias' e deverá constar o evento cadastrado com Natureza de Rubrica eSocial 9219 (Evento 0014). Saiba mais sobre a gravação automática do histórico [CLICANDO AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009552422);

![](https://tdn.totvs.com/download/attachments/776113025/image-2023-12-21_11-18-6.png?version=1&modificationDate=1703168287114&api=v2)

5. No Recibo de Férias constará lançado o evento com a rubrica 9219 (Evento 0014);

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20053111483927)

6. No envelope do funcionário constará o evento sem a rubrica 9219 (Evento 9014);

![](https://tdn.totvs.com/download/attachments/776113025/image-2023-12-21_11-21-36.png?version=1&modificationDate=1703168496494&api=v2)

6.1. Para os casos em que já houveram mudança de competência no produto e, não é possível cancelar o lançamento de férias e lançar novamente, será necessário alterar manualmente a informação na ficha financeira, alterando para o novo evento (9014);  
7. Após o processo acima, é necessário retificar o S-1200 correspondente;  
7.1. É importante identificar em qual período apuração foi gerado o XML S-1200. No exemplo supracitado o XML S-1200 foi gerado no mês 03/2023, porém por ter sido lançado no mesmo envelope do adiantamento, o sistema irá gerar um único XML S-1210 em 04/2023. Ou seja, para a correção do evento no XML S-1200 no período 2, será necessário:

* Reabrir o período 03/2023, através do S-1298;
* Enviar o S-3000 do S-1210 03/2023;
* Retificar o S-1200 03/2023 (verifique a necessidade de redistribuir SEFIP, caso trabalhe com tomador de serviços);
* Após será necessário conferir se o novo evento (9014) foi gerado no XML S-1200 e enviar novamente o S-1210 e S-1299 03/2023;
* Enviar o S-1210 04/2023.

8. O XML S-1210 será gerado com o valor e incidências da rubrica informada no Recibo de Férias.

![](https://tdn.totvs.com/download/attachments/776113025/image-2023-12-21_11-24-31.png?version=1&modificationDate=1703168671713&api=v2)

**Importante**

* Para evitar a duplicidade de informações no evento S-1210, é necessário garantir que a rubrica associada aos eventos em "Eventos do Recibo" e "Eventos da Folha" para assistência médica não seja a mesma, e que o evento de assistência médica a ser lançado na folha não tenha o mesmo código da natureza da rubrica eSocial 9219 - "Desconto de assistência médica ou odontológica". Escolha um código de rubrica diferente para o evento de assistência médica associado à folha, garantindo que não haja conflito com o desconto já presente no evento S-1210;
* Nos casos em que o funcionário trabalha e tira férias dentro do mesmo mês, por exemplo do dia 01/04/2023 a 15/04/2023 o funcionário gozou férias; do dia 16/04/2023 até 30/04/2023 trabalhou, será necessário colocar uma condição na fórmula, para que o valor descontado nas férias seja desconsiderado no lançamento do envelope dos dias trabalhados, para não causar duplicidade no desconto no envelope. Abaixo um exemplo da condição da fórmula:  
              SE MV (MES, ANO, 'XXXX') > 0,01 ENTAO 0 SENAO ... **(Continuar preenchendo com a fórmula que já utiliza)**  
             Informar onde xxxx é o código do evento de desconto de Assistência médica de férias no envelope.
