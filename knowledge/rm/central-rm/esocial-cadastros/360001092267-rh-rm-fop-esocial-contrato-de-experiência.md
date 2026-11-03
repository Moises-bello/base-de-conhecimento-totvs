---
article_id: 360001092267
category: eSocial - Cadastros
content_hash: 1ff40eaa241638e1458d7dcfd7cabc6473119fe336a952076a71522f68128a4b
fetched_at: '2026-06-28T22:47:14.573107+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP- eSocial - Contrato de Experiência
type: support-article
updated_at: '2026-01-26T15:55:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001092267-RH-RM-FOP-eSocial-Contrato-de-Experi%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17269007242391)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**  
Como o sistema irá considerar o contrato de experiência para o eSocial?   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
Para que o sistema pudesse atender à casos de contrato de experiência, foi realizada pela equipe de desenvolvimento a implementação de um novo campo para o usuário informar se o contrato com prazo trata-se de experiência ou não.

Acessando o cadastro do funcionário, menu lateral **Registro**, aba **Dados do Contrato**, o campo **Tipo de Contrato** poderá ser preenchido com as opções **Prazo Determinado** e **Experiência**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044078334)

Para gerar o XML do evento **S-2206** com a informação do campo  siga os passos abaixo:  
   1. Informe no cadastro do funcionário o **Tipo de Contrato** como **Experiência** e informe a data do fim do contrato;  
   2. No evento gerado (**S-2200** para novo registro ou **S-2206** para registros alterados), valide se a tag **tpContr** foi gerada como **2** (prazo determinado).  
   3. Transmita o evento com o governo;

 

**Importante**  
Em releases mais antigas, o campo poderá ser encontrado no cadastro do funcionário, menu lateral **Registro**.

No caso de prazo determinado:

Caso tenha havido ajuste para que os dias de afastamento não sejam computados na duração do contrato, o empregador tem de, até o dia 15 (quinze) do mês seguinte ao da data prevista para o término, enviar o evento S-2206, com a prorrogação do contrato por 60 dias. Ao final dessa prorrogação, o contrato é igualmente rescindido,  
devendo ser enviado o evento S-2299.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044938153)

**Saiba mais**  
Para mais informações acesse:  
- [Como informar ao governo que o contrato passou de prazo determinado para prazo indeterminado para contratos definidos em dias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23673296229783-RH-RM-FOP-eSocial-Como-informar-ao-governo-que-o-contrato-passou-de-prazo-determinado-para-prazo-indeterminado-para-contratos-definidos-em-dias)
