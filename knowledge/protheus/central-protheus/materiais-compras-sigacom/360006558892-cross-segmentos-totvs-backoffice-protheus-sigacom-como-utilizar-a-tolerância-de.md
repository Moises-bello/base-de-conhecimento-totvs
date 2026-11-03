---
article_id: 360006558892
category: Materiais - Compras (SIGACOM)
content_hash: 88ff8273c0c7aeeb5f526b4ee1dbb1c08b596c5c516469629ecc1fc950253aaa
fetched_at: '2026-06-28T22:41:08.705307+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como utilizar a Tolerância
  de Recebimento no módulo de Compras ?
type: support-article
updated_at: '2025-11-11T13:34:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006558892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-utilizar-a-Toler%C3%A2ncia-de-Recebimento-no-m%C3%B3dulo-de-Compras
---

**Dúvida**

Como utilizar a Tolerância de Recebimento no módulo de Compras ?

**Ambiente**

Protheus - Compras - A partir da versão 11.80

**Solução**

O controle de tolerância de recebimento, permite cadastrar regras de tolerância de recebimento de materiais, com o objetivo de validar as entregas realizadas pelo fornecedor (durante a digitação do documento de entrada) com preço e/ou quantidade e/ou prazo em desacordo com o pedido.

No cadastro devem ser definidas as regras para aceite de divergências entre pedidos de compra e documentos de entrada, identificadas por fornecedor, produto e/ou grupo de materiais.

Quando a diferença entre o Documento Entrada e o Pedido Compra for maior do que a tolerância cadastrada na rotina, o documento de entrada entrará no sistema bloqueado, sendo necessário libera-lo pela rotina de Liberação de Documentos (MATA094).

Para utilização é necessário:

• Cadastrar aprovadores (MATA095);

• Cadastrar um grupo de aprovação (MATA114), na aba **Tipo de Documentos**, selecionar a opção **Nota Fiscal;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36252045510807)

***OBS:** Para habilitar a aba “Tipo de documentos” no cadastro de grupo de aprovação basta ativar o parâmetro **MV\_ALTPDOC** = T*

• No SIGACFG (configurador) informar no parâmetro **MV\_NFAPROV** o número do grupo de aprovação para liberação dos documentos entradas;

• Cadastrar Tolerância de Recebimento (**COMA020**), para quantidade e/ou valor. Caso desejar cadastrar uma única tolerância para todas as entradas, deve-se deixar os campos de fornecedor e produto em branco;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058314573)

• Após entrar com o Documento Entrada, se a tolerância cadastrada for ultrapassada (o Documento Entrada for maior que Pedido Compra), o Documento Entrada entrará bloqueado no sistema. A validação da tolerância é feita por quantidade e/ou valor. Caso desejar que a tolerância seja feita também quando o Documento de Entrada for menor que o Pedido de Compra, deve-se alterar o valor do parâmetro MV\_TOLENEG;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057471854)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057471654)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058313953)

• Para realizar a liberação o Documento Entrada, deve-se entrar com os aprovadores do grupo cadastrado anteriormente na rotina de Liberação de Documentos, localizar o Documento Entrada e liberar.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057472634)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058315373)

Após a liberação no caso do Documento de Entrada é necessário fazer a classificação novamente do documento, uma vez que ao cair para tolerância de recebimento entende-se que há divergências entre pedido x nota fiscal a serem analisadas e conferidas pelo aprovador, sendo assim o documento cairá no status "Docto Não Classificado".

**Obs1.:**

A Regra da tolerância de recebimento se enquadra apenas para os itens que forem comprados (informados na Pré-Nota/Documento de entrada). Caso não for informado alguns dos itens do documento, como por exemplo itens deletados, estes não entrarão na regra da tolerância de recebimento.

**Obs2.**:

Para utilização da Tolerância de Recebimento por "Dias de Atraso ou Antecipação" (Campo ***AIC\_TOLENT***) deve-se utilizar do **parâmetro MV\_TOLENT**que define se o Sistema controlará a tolerância de recebimento por data de entrega somente para atrasos (1), antecipações (2) ou ambos (3). Segue abaixo exemplo de utilização desse parâmetro:

Data de Entrega = 22/10

Dias de Tolerância = 5 

|  |  |
| --- | --- |
| • | Parâmetro MV\_TOLENT = 1 (Atraso) - Bloqueia documento após o dia 27/10; |

|  |  |
| --- | --- |
| • | Parâmetro MV\_TOLENT = 2 (Antecipado) - Bloqueia documento antes do dia 17/10; |

|  |  |
| --- | --- |
| • | Parâmetro MV\_TOLENT = 3 (Ambos) - Bloqueia documento após o dia 27/10 ou antes do dia 17/10. |

**Obs3.:**

Em casos de que se utilize o cadastro de tolerância por dias com campo ZERO, é necessário criar o parâmetro MV\_TOLZERO:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6215449997079)

[Configuração de tolerância de recebimento de zero dias.](https://tdn.totvs.com/pages/releaseview.action?pageId=641449871)

**Obs4.**:

A tolerância de recebimento não leva em consideração o perfil do aprovador, sendo assim, não será definido limites de aprovação e a aprovação não será utilizado o saldo do aprovador. ( caso o mesmo usuário esteja como sendo 2 compradores diferentes, será necessário efetuar 2x a aprovação da NF, independente do perfil do aprovador).

[Procedimentos para configurar Tolerância de Recebimento.](https://tdn.totvs.com/pages/viewpage.action?pageId=233744273)

**Obs5.:**Caso queira que seja considerado o saldo do pedido de compras na tolerância de recebimento foi criado o parâmetro **MV\_PCTOSAL**para realizar a verificação da quantidade de tolerância do parâmetro MV\_PCTOLER.

[Criação do parâmetro MV\_PCTOSAL](https://tdn.totvs.com/pages/releaseview.action?pageId=642972481)

**Obs6.:**Para que o sistema apresente corretamente os motivos de bloqueio do documento de entrada é necessário ter em seu ambiente o campo **CR\_NFMOTBL**e o sistema estar atualizado com o último pacote de expedição contínua do compras. A criação desse campo só será contemplada no dicionário padrão a partir do release 2210, caso esteja em um release anterior a criação precisará ocorrer de forma manual via configurador conforme informações que constam no documento abaixo :

[Motivos de bloqueio por tolerância no documento de entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=697268263)

[Expedição Contínua do Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

**Obs7.: Considerar descontos na regra de tolerância no recebimento.**

Quando há desconto no documento de entrada, para que o sistema considere desconto na tolerância de recebimento é necessário verificar o parâmetro MV\_DESCTOL.

[**MV\_DESCTOL**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029046472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Considerar-Desconto-do-Item-na-Toler%C3%A2ncia-de-Recebimento-MV-DESCTOL?source=search)

Quando há desconto no pedido de compras, para que o sistema considere esse desconto no processo de tolerância no recebimento, deve-se habilitado o parâmetro MV\_PCDETOL.

**[MV\_PCDETOL](https://tdn.totvs.com/pages/viewpage.action?pageId=838936989)**

**Obs8.:** Parâmetro **MV\_TOREGGR,** define a sequência de validação da tolerância no recebimento :

**[MV\_TOREGGR](https://tdn.totvs.com/pages/viewpage.action?pageId=625169084)**

**Obs9.:** Não há disponível no módulo de Compras funcionalidade de Tolerância de Recebimento referente a Solicitação de Compras.

**Obs10 :** No padrão temos um parâmetro que conforme sua configuração, a nota bloqueada por tolerância, poderá ser classificada.  **[MV\_RESTCLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018981691-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Permitir-a-Classifica%C3%A7%C3%A3o-de-um-Documento-de-Entrada-pendente-de-Aprova%C3%A7%C3%A3o-Bloqueado-MV-RESTCLA)**

**Obs11 :** Tolerância no recebimento x MV\_PCTOLER x Recebimento parcial do PC.

A tolerância é sempre calculada com base na **quantidade original do pedido (C7\_QUANT)**.Dessa forma, mesmo que ocorram consumos parciais do saldo, o sistema **não recalcula** a quantidade de tolerância com base no saldo restante.

[**PCOM12085 - Funcionamento do parâmetro MV\_PCTOLER no consumo parcial do saldo do pedido de compra**](https://tdn.totvs.com/pages/viewpage.action?pageId=967114032)

**Essa documentação foi gerada em virtude da abertura da ISSUE DMANMAT02-53384.**

**Materiais de Apoio - Vídeos How To.**

[Tolerância no Recebimento na prática](https://www.youtube.com/watch?v=mP1YsGyMoAQ)

[Tolerância no Recebimento MV\_TOLENEG](https://www.youtube.com/watch?v=igo2xcFylz0)

[Definindo regras na tolerância](https://www.youtube.com/watch?v=x78BZbmH14A)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Tolerância de Recebimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491238180631)

[Definindo controle de tolerância por dias de atraso ou antecipação](https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/coma020_tolerancia_recebimento.htm)

[PCOM15003 - Regras de Tolerância de Recebimento](https://tdn.totvs.com/pages/releaseview.action?pageId=625169084)

[MP - SIGACOM - Permitir a Classificação de um Documento de Entrada pendente de Aprovação ( Bloqueado ) - MV\_RESTCLA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018981691)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
