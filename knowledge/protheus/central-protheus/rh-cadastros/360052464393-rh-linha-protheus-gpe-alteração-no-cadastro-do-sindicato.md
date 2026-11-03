---
article_id: 360052464393
category: RH - Cadastros
content_hash: 71962bbed33bbac2c0e9d30743155df393fb561a67db3cf1be71170d392242b4
fetched_at: '2026-06-28T22:43:25.816835+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Alteração no cadastro do Sindicato
type: support-article
updated_at: '2026-06-24T19:30:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052464393-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-no-cadastro-do-Sindicato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26454242824983)  Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como o sistema valida as informações do cadastro de sindicatos e suas alterações  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
No Protheus temos a tabela de **Histórico de Sindicatos (RG4).**  
Esta tabela grava as **alterações** realizadas no **cadastro de** **sindicato** tendo como referência a **data base** do sistema.   
Este histórico é tido como **referência** para os **cálculos**realizados, o qual observa as informações contidas na **RG4** e ignora o que está atualmente dentro do cadastro do sindicato.

Por isso, quando é feita **qualquer alteração** no cadastro, o Sistema emite o seguinte **alerta** antes de confirmar o ajuste:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26457127026967)

Caso o usuário selecione a opção **Não e abrir documentação**, será aberta uma nova guia no navegador de internet com o artigo [Cadastro de Sindicatos](https://tdn.totvs.com/display/PROT/GPE001CAD12_Cadastro_de_Sindicatos), e em seguida a indicação que a operação foi cancelada pelo usuário, não salvando as alterações realizadas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26457149596311)  
  
**Exemplo**  
O período aberto para cálculo da Folha de Pagamento é **202408,** e a data base do sistema está em 18/09/2024**.**

Após calcular a **férias** para um funcionário, notou-se que a configuração para **médias** estava incorreta, sendo necessário **ajustar** o **Cadastro do Sindicato.**  
Realizada alteração no cadastro, o Sistema **gravará** as informações na **RG4** com data de **18/09/2024,** porém o **cálculo do período em aberto** (202408) **não sofrerá alteração.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26457127037591)

**Atenção**

É importante analisar o Histórico de alterações do (RG4) **sempre** que o cálculo não assumir a alteração realizada.   
Esta verificação pode ser feita através da opção de **Histórico,** dentro do próprio cadastro de sindicatos, como demonstrado na imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26457149609239)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26457127047063)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Pontos de Entrada Cadastro de Sindicato - GPEA340](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4957736954007-RH-Linha-Protheus-GPE-Pontos-de-Entrada-Cadastro-de-Sindicato-GPEA340)  
[RH - Linha Protheus - GPE - Quais são as mudanças existentes no cadastro de sindicatos na versão 12](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020377312-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-mudan%C3%A7as-existentes-no-cadastro-de-sindicatos-na-vers%C3%A3o-12)  
[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
