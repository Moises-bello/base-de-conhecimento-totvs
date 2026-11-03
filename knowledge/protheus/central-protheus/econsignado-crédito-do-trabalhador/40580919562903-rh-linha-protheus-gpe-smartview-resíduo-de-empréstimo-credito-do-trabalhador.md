---
article_id: 40580919562903
category: eConsignado (Crédito do Trabalhador)
content_hash: 562334ae5f3f13692c1bb00df714f4aa37e0df95c431422eb98d722458a7849f
fetched_at: '2026-06-28T22:43:07.151171+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH  - Linha Protheus - GPE - Smartview - Resíduo de Empréstimo Credito do Trabalhador
type: support-article
updated_at: '2026-05-19T13:54:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40580919562903-RH-Linha-Protheus-GPE-Smartview-Res%C3%ADduo-de-Empr%C3%A9stimo-Credito-do-Trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40580919539095) Tempo aproximado para leitura: **03:00:00min**  
  
**Dúvida**  
Como gerar o a relação com todos os funcionários que possuem valor residual do Crédito do Trabalhador, isto é, valores que não foram descontados na folha de pagamento e deverão ser quitados diretamente na instituição financeira  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310  
  
**Solução**  
Com o objetivo de controlar melhor a existência dos valores residuais dos empréstimos do e-Consignado por funcionário e a comunicação destes, foi desenvolvida a nova rotina de "**Resíduos do Crédito do Trabalhador**", que deverá permitir o envio de e-mail para comunicação sobre a existência destes resíduos aos funcionários.

A nova rotina estará disponível no menu a partir da release 12.1.2610, porém, caso deseje utilizar nas releases anteriores, pode ser feita a inclusão da rotina **GPEM947**no menu - [RH - Linha Protheus - GPE - Como excluir ou incluir rotinas no menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013342191-RH-Linha-Protheus-GPE-Como-excluir-ou-incluir-rotinas-no-menu) como Função Protheus.

**- Importante**

Pré-requisitos para a funcionamento da rotina:

* A integração depende da aplicação da atualização liberada no pacote de expedição do módulo RH a partir de 06/03/2026 e da execução do UPDDISTR com o dicionário diferencial para os releases iguais ou superiores a versão 12.1.2310 (para criação do campo **RCK\_MAIL**);  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40580919540759)

Foi efetuado a criação do campo no dicionário SX3 conforme estrutura abaixo:RCK24RCK\_MAILC1Statu.e-mailStatus e-mail resíduo

* Ativação do servidor REST na [porta multiprotocolo](https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo), pelo uso da chave [app\_environment](https://tdn.totvs.com/pages/viewpage.action?pageId=556382089).
* Configuração do serviço de envio de e-mail do Protheus: [Configuração de E-mail / Proxy](https://tdn.totvs.com/pages/viewpage.action?pageId=271166884) ;
* O usuário deve possuir permissão de acesso à rotina de Lançamento de Valores Futuros (GPEA110) [Controle de acessos do usuário (GPEA270 - SIGAGPE - V12)](https://tdn.totvs.com/pages/viewpage.action?pageId=435115342);

Através de uma interface moderna e intuitiva, foi disponibilizada a rotina com as principais funcionalidades:

* Visualização da listagem de empréstimos com resíduo do Crédito do Trabalhador, agrupados por funcionário, após o fechamento do período;
* Ao acessar a rotina, a tela apresentará as informações referentes ao último período fechado da folha, da filial logada pelo usuário;
* Fazer a busca pelos resíduos, filtrando pela Filial, Período de a Período até, e Exibir apenas os registros com status igual a 'Enviado' ou não;
* Controle do envio da comunicação de resíduo por e-mail através da legenda presente na coluna 'Status do e-mail;
* Possibilidade de exportar dados da tela para um arquivo .csv;
* Possibilidade de comunicado aos funcionários via e-mail, informando o valor a pagar ao banco por empréstimo
  + Se o funcionário selecionado não possui e-mail cadastrado, ou o status do empréstimo estiver igual a 'Enviado', os registros serão desconsiderados;
* Possibilidade de alterar o status do envio do empréstimo, de 'Enviado' para 'Não enviado', e vice versa;
* Totalizador de empréstimos com resíduo filtrados;
* Por padrão, a API, retornará 50 funcionários por vez, sendo possível retornar mais através do botão ‘Carregar mais resultados’ da tabela;
* Possibilidade de filtrar campos da tabela já carregada na tela, através do campo 'Pesquisar'.

Benefícios da rotina de **Resíduos do Crédito do Trabalhador**:

* **Controle do processo**  
  Controle da existência dos resíduos após o fechamento da folha;
* **Comunicação eficiente**  
  Já que no recibo de pagamento informa apenas sobre a existência de resíduos, e não detalha sobre quais contratos, valor, instituição financeira e etc;
* **Experiência do Usuário**  
  Interface mais moderna e intuitiva;

  ![chrome_McgfSpiMWD.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/40580905925527)

  Após o envio, chegará o e-mail para o funcionário neste formato:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40580919543063)

**Observações**

* Caso seja enviado um registro já com status 'enviado', será apresentado o alerta: "Registro com status 'Enviado'. Caso Queira enviar o e-mail novamente, redefinir o status do registro para 'Não Enviado'".
* Se o funcionário não tiver e-mail no cadastro e tentar enviar, será apresentado o alerta: "Funcionário selecionado sem e-mail cadastrado, será desconsiderado.
* Caso seja selecionado um empréstimo com status 'enviado' e outro com status 'não enviado', ao realizar o envio será apresentada a mensagem em tela solicitando a confirmação para envio somente dos empréstimos com status 'não enviado'.
* É possível alterar manualmente o status do empréstimo para 'enviado' ou 'não enviado' de acordo com a necessidade, por exemplo, caso não queira enviar por e-mail o resíduo de terminado período, basta alterar o status para 'enviado' ou caso queira reenviar, basta alterar para 'não enviado'
* Caso seja encontrado algum problema na configuração do serviço de envio de e-mail do Protheus, será apresentado a mensagem: "E-mail não enviado. Verifique a configuração de e-mail/proxy no configurador" [Configuração de E-mail / Proxy](https://tdn.totvs.com/pages/viewpage.action?pageId=271166884)

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=1041790094>  
[Crédito do Trabalhador - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
