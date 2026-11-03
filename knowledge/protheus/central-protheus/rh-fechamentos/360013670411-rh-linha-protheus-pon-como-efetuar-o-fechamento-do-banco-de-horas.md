---
article_id: 360013670411
category: RH - Fechamentos
content_hash: 162588055c1a0c0976e621b18c8fe1b85fee5794cbe42d00e4192796033df724
fetched_at: '2026-06-28T22:44:48.856985+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar o fechamento do banco de horas
type: support-article
updated_at: '2026-06-09T18:23:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013670411-RH-Linha-Protheus-PON-Como-efetuar-o-fechamento-do-banco-de-horas
---

**Dúvida**  
Como efetuar o Fechamento do banco de horas?    
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para que ocorra a **baixa** do **Banco de Horas**, é necessário que:  
  
**1.** No **cadastro** do **funcionário**, **aba** **Controle de Ponto**, informe **Sim** nos campos **Acumula BH** e **BH para Folha;**  
  
**2.** **Cadastre** os **eventos** **vinculados** aos **IDs de Ponto responsáveis pela baixa,** que são: **023A** e **024A**. Ambos eventos devem ter uma verba de folha vinculada, sendo uma do tipo Horas/Provento e Horas/Desconto respectivamente. Os cadastros devem estar conforme exemplo abaixo;  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100822773)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098586014)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098586034)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100822833)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100822873)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098586094)  
  
**3.** Para executar o **fechamento**, acesse Miscelânea - Fechamentos - Banco de Horas e preencha os parâmetros para processamento.  
  
**Fechamento por?**  
**- Por Período =** Será o resultado dos eventos Débito/Crédito de acordo com intervalo selecionado, independente do número de horas;  
**- Por Horas =** O banco será baixado de acordo com o número de horas determinado pelo usuário. Esse valor será definido mais a frente;  
**- Por Vencimento =** Ao selecionar o fechamento por vencimento o sistema irá baixar os eventos com data de vencimento menor ou igual a data do fechamento. Para mais detalhes referente ao fechamento por vencimento [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41052794384407-RH-Linha-Protheus-PON-Fechamento-do-Banco-de-Horas-por-Vencimento)  
  
**Fechamento Horas?**   
Esse parâmetro só terá efeito caso a pergunta “Fechamento Por” tenha a opção "Por Horas“  
**- Até limite =** Estabelece que será baixado apenas o saldo de horas inferior ao limite fornecido;  
**- Acima Limite =** Determina que será baixo o saldo que for superior ao limite;  
**- Ambos =** Não considera o limite de saldo. Baixa todas as horas existentes no banco.  
  
**Nº Horas Limite?**  
O valor preenchido neste campo influenciará a opção escolhida na pergunta anterior.  
  
**Utilizar Horas?**  
**- Normais =** Faz a baixa apenas do saldo de horas NORMAIS. Este sado será composto apenas pelo total horas normais realizadas, ou seja, 1 por 1;  
**- Valorizadas =** Faz a baixa apenas do saldo de horas VALORIZADAS. Este saldo será composto pelas horas normais somadas com a valorização da hora.  
  
**Resultado?**  
Poderá ser selecionado Credor, Devedor ou saldo (ambos).  
**- Credor =** Se esta opção for selecionada, apenas os funcionários que tiverem um saldo de horas credor terão o banco de horas baixado;  
**- Devedor =** Se esta opção for selecionada, apenas os funcionários que tiverem um saldo de horas devedor terão o banco de horas baixado;  
**- Saldo =** Todas as horas do banco de horas serão baixadas.  
  
**Data de Pagamento Folha?**  
Deve ser preenchida com o último dia do período de apontamento que está trabalhando.  
  
**Lançamentos BH?**   
**- Baixa =** Faz a baixa do banco de horas de acordo com as configurações definidas e mantém para fins de histórico os registros na tabela SPI, porém, com status de baixado e a data da baixa;  
**- Limpar =** Faz a baixa do banco de horas de acordo com as configurações definidas e exclui todos os registros baixados.  
  
**Provento Data Inicial/Final - Desconto Data Inicial/Final?**  
Esses campos só terão validade se a pergunta "Fechamento Por?" estiver com a opção "Período" selecionada.  
  
**Limita Lançamentos?**  
No **Fechamento de Banco de Horas**, existe a pergunta **Limita Lançamentos?**, que possui quatro opções:  
- **Proventos** = Se o **total** de **horas negativas**, for **maior** que o **total** de **horas positivas**, os **descontos** serão**limitados** ao valor **total** das **horas positivas**;  
- **Descontos** = Se o**total** de **horas positivas**, for **maior** que o **total** de **horas negativas**, os **descontos** serão **limitados** ao valor **total** das **horas negativas**;  
- **Ambos** = **Sempre limitar** os **proventos** e**descontos** de acordo com a **situação do BH** do funcionário, ou seja, se existirem **mais horas positivas** do que **negativas**, os **proventos** serão **limitados** de acordo com o **total de horas negativas**. Se existirem **mais horas negativas** do que **positivas**, os **descontos** serão **limitados** de acordo com o **total de horas positivas**;  
- **Nenhum** = **Não realiza** a **limitação de lançamentos**, ou seja, **todas** as horas **serão baixadas** de acordo com os parâmetros informados na rotina.

**Fecha Banco p/ Rescisão?**  
**- Sim =** Para efetuar o fechamento para Rescisão   
**- Não =** Para fechamentos conforme demanda  
  
**Saiba mais:**

[RH - Linha Protheus - PON - Fechamento de Banco de Horas Automático](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035725033-RH-Linha-Protheus-PON-Fechamento-de-Banco-de-Horas-Autom%C3%A1tico?source=search)

[RH - Linha Protheus - PON - Limita Lançamentos no Fechamento de Banco de Horas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060213973-RH-Linha-Protheus-PON-Limita-Lan%C3%A7amentos-no-Fechamento-de-Banco-de-Horas?source=search)

[RH - Linha Protheus - PON - Fechamento de Banco de Horas para funcionário com saldo final credor, devedor ou ambos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058399074-RH-Linha-Protheus-PON-Fechamento-de-Banco-de-Horas-para-funcion%C3%A1rio-com-saldo-final-credor-devedor-ou-ambos?source=search)
