---
article_id: 360028611131
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 9d77c428dcbd5a6debae103113d485b17becbef6131269042c3ad014ecee6249
fetched_at: '2026-06-28T22:43:32.398546+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Configurações para gerar GRRF
type: support-article
updated_at: '2025-06-26T13:33:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028611131-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%B5es-para-gerar-GRRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069364420375) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Quais as configurações necessárias para gerar um arquivo da GRRF, seja normal ou complementar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Solução**O que é GRRF?

**GRRF é a sigla para Guia de Recolhimento Rescisório do FGTS**. O FGTS, como você já sabe, é o Fundo de Garantia de Tempo e Serviço, formado a partir de depósitos mensais que podem ser de 8% ou 2% do [salário](http://www.metadados.com.br/blog/index.php/2016/07/18/gestao-de-carreira-qual-a-importancia-do-plano-de-cargos-e-salarios/) do empregado, conforme o caso. Esse fundo busca ajudar o profissional em casos de demissão sem justa causa e é uma obrigação do empregador realizar estes depósitos.

Assim, a GRRF é o **documento que vai permitir ao profissional retirar o dinheiro armazenado no seu fundo de garantia e também os valores que são pagos em caso de desligamento**.  
  
Pra quem a GRRF se destina?

A GRRF é destinada para**todos aqueles que têm direito à retirada do FGTS**, ou seja, que estão em processo de desligamento dentro das seguintes condições:

* Rescisão sem justa causa ou antecipada do contrato a termo por iniciativa do empregador;
* Rescisão por término do contrato a termo;
* Rescisão por culpa recíproca (tanto do empregador quanto do empregado);
* Dispensa por força maior, como falência da organização, entre outros;
* Rescisão indireta, que é quando o empregador comete uma falta grave.

1º Passo: Para geração do arquivo no Protheus são necessárias algumas configurações especificas como:

Preenchimento de alguns campos do Parâmetro tabela S043.

**IMPORTANTE**: Caso seja identificado que algum campo esteja com preenchimento errado, deve ser corrigido e será necessário excluir a rescisão e calcular novamente. Para que assim o sistema, acate a alteração efetuada.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4699045032343)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-0-21.png?version=1&modificationDate=1510083044000&api=v2)

**Campo de aviso prévio**: Quando o funcionário é dispensado pelo empregador é pago o aviso prévio em carater indenizatório (TIPO I) com isso estes valores referentes ao aviso são enviados para GRRF. (Não é obrigatório possuir aviso prévio indenizado para gerar a GRRF, porém quando o tipo de rescisão possui o cálculo o mesmo é levado para GRRF);

**Campo FGTS mês rescisão:** Este campo define se o FGTS gerado na rescisão será enviado para GRRF ou para SEFIP. Todos os tipos de rescisão que devem ser quitados por meio da **GRRF** devem estar preenchidos com **S** neste campo.

**Campo FGTS mês anterior:** Este campo é preenchido quando a demissão é feita antes do dia 07, para que os valores da folha do mês anterior seja levada para o cálculo da GRRF.

**Campo FGTS MULTA 40%:** Este campo deve estar preenchido quando o empregador dispensa o funcionário sem justa causa e paga a multa de 40% ao empregado em carater indenizatório.

**Campo % FGTS:** É o percentual de multa pago ao funcionário pela dispensa sem justa causa (complemento do campo FGTS MULTA 40%)

**Campo Cód rescisão RAIS:** Este campo não é tão relevante para geração da GRRF, porém é importante que o mesmo esteja com preenchimento correto de acordo com seu delisgamento.

**Campo Cod. Afastamento FGTS:** Este campo deternina o tipo de desligamento, é partir dele que o sistema sub-entende que aquele funcionário possui direito ao SAQUE do FGTS. Funciona como se fosse a justificativa para geração da GRRF.

**Campo Código A.M.:** Este campo leva o código de SAQUE do funcionário a conta do FGTS, ele este ligado diretamente ao campo Cod. Afastamento FGTS.

 

2º Passo:

Após as devidas configurações o cálculo de rescisão é efetivado de forma correta e deve gerar os identificadores de cálculo:

**ID - Identificado de calculo obrigatório ao calcular a rescisão para gerar a multa do FGTS (GRRF) (demissão sem justa causa)**

0118 – FGTS deposito (refere-se o que esta depositado na CEF) > Este ID é informado manualmente ou é tratado por meio da rotina de SALDO FGTS.

0119 – FGTS Rescisão (8% normal)

0120 – FGTS artigo 22 (40%)

0214 – FGTS 13º rescisão (8% 13º)

0297 – 10% FGTS (10%)

0293 –FGTS rescisão desp. (Base normal)

0294 – FGTS 13º (Base 13º)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-28-9.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-28-35.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-28-58.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-29-19.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-29-40.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-30-5.png?version=1&modificationDate=1510083044000&api=v2)

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-30-31.png?version=1&modificationDate=1510083044000&api=v2)

3º Após o cálculo de rescisão em que todas as verbas estão corretas, e o sistema esta gerando os valores devidos é necessário configurar a geração do arquivo:

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-24-4.png?version=1&modificationDate=1510083044000&api=v2)![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-24-27.png?version=1&modificationDate=1510083044000&api=v2)![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-24-50.png?version=1&modificationDate=1510083044000&api=v2)![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-25-12.png?version=1&modificationDate=1510083044000&api=v2)

**Importante:**

* Preencher as datas de forma genérica e informar matricula especifica;
* Atentar-se ao tipo de RESCISÃO que esta solicitando;
* Só informar data de Homologação DISSIDIO, se a GRRF for de uma complementar por dissidio.

Após estes passos o sistema irá gerar o arquivo de acordo com o cálculo de rescisão:

![](http://tdn.totvs.com/download/attachments/311631246/image2017-11-7_17-27-8.png?version=1&modificationDate=1510083044000&api=v2)

**Saiba mais:**

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
