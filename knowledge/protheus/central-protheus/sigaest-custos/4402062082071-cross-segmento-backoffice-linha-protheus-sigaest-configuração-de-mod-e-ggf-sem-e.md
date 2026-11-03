---
article_id: 4402062082071
category: SIGAEST - CUSTOS
content_hash: 83451616332c99c66585833222d893fc942014838625a7f68996a0574a857530
fetched_at: '2026-06-28T22:39:00.557667+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Configuração de MOD
  e GGF "Sem" e "Com" integração contábil
type: support-article
updated_at: '2026-05-27T14:16:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil
---

O artigo explica como configurar o cálculo do custeio de Mão de Obra (MOD) e Gastos Gerais de Fabricação (GGF) no Protheus, detalhando dois métodos: sem integração contábil, usando custo médio manual, e com integração contábil, com lançamentos contábeis manuais rateados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29996531388439) Tempo aproximado para leitura: **00:15:00 min**

**Dúvida**

Como configurar o Cálculo do Custeio de Mão de Obra, produtos do tipo **MOD** e Gastos Gerais de Fabricação **GGF** no Protheus **(B1\_CCCUSTO, B1\_GCCUSTO, MOD e GGF)** com e sem integração contábil

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
 Configuração correta para o calculo de produtos MOD+CC e produto GGF, seguindo a orientação de cadastros e parametrização do recalculo do custo médio.

**Vídeos explicativo sobre a configuração do produto MOD quando há integração contábil sendo o segundo método:**

***How To | SIGAEST - Custeio MOD/GGF na Integração com Contábil #TOTVS\_Backoffice\_Linha\_Protheus***

**Link:** [**https://www.youtube.com/watch?v=7XaCxZ\_6TAg**](https://www.youtube.com/watch?v=7XaCxZ_6TAg)

**Informações importantes:**

 \* **Existem** **02 (dois) métodos** **para custeio do produto MOD e GGF** **(Sem Integração Contábil, e Com Integração Contábil)**

**-> Sem Integração Contábil** considera o Custo da MOD sempre pelo campo **Custo Médio (B2\_CM1)**, é possível definir manualmente na rotina SALDO EM ESTOQUE (MATA225).

**->** **Com Integração Contábil** considera o Custo da MOD referenciando os Lançamentos Contábeis manuais que são informados na rotina **CTBA102** para que o mesmo seja rateado entre todas as requisições de MOD no período de processamento do Custo Médio.

**Caso,** no padrão a utilização das configurações dos métodos disponíveis no Protheus "**Com Integração Contábil"** e "**Sem Integração Contábil"** **não seja atendido a regra de Negócio da Empresa**. É necessário apoio de Analista Desenvolvedor para Customizar conforme necessidade específica utilizando o [***Ponto de Entrada MA330MOD***](https://tdn.totvs.com/x/oz_hMQ).

***PE MA330MOD Customiza cálculo do custo de mão de obra***  
[***https://tdn.totvs.com/x/oz\_hMQ***](https://tdn.totvs.com/x/oz_hMQ)

**Distribuição de Custos por Grupo Contábil (B1\_GCCUSTO)**

É importante observar que a distribuição dos valores lançados por **centro de custo**, em casos em que os produtos pertencem a **diferentes grupos, mas compartilham o mesmo centro de custo**, segue uma regra específica para produtos do tipo **MO**.

Caso o código inicial do cadastro do produto seja **MOD**, ocorrerá uma amarração específica no código-fonte, resultando na alocação integral do valor para o produto enquadrado nessa condição, sem a distribuição desejada.

**Exemplo:**

| Código do Produto | Centro de Custo (CC) | Grupo Contábil | Conta Contábil |
| --- | --- | --- | --- |
| MOD9900 | 9900 | 7070 | 99MO |
| GGF9900 | 9900 | 8080 | 99GGF |

Considerando um lançamento no centro de custo **9900** no valor de **R$100,00**, a expectativa de distribuição seria:

* **MOD** deveria absorver **R$40,00** no custo da requisição.
* **GGF** deveria absorver **R$60,00** no custo da requisição.

Entretanto, devido à amarração existente, o sistema avalia o centro de custo sem considerar a distinção entre grupos contábeis. Dessa forma, **o produto MOD será custeado integralmente com o valor total de R$100,00**.

**Solução:**  
Para evitar essa situação, recomenda-se que os códigos de produtos do tipo **MO** não sejam iniciados com a sigla "**MOD**".

**\* Observação:** **É muito importante validar** **qual o método** **utilizado, que se adeque hoje ao seu escopo de negócio.**

|  |
| --- |
| **\*** **É possível utilizar** ***apenas 01 (um)*** **dos 2 métodos no ambiente.** |

Apostila com orientações sobre os conceitos de utilização do Calculo de MOD e GGF, Link abaixo para download [**Clique aqui**](https://tdn.totvs.com/pages/releaseview.action?pageId=366649055#:~:text=Link%20abaixo%20para%20download%3A)

|  |
| --- |
| **VEJA ABAIXO PROCEDIMENTOS PASSO-A-PASSO PARA INCLUSÃO DE MOD E/OU GGF NOS 2 MÉTODOS DISPONÍVEIS NO PROTHEUS** |

## **1° Método - Utilizando o código do produto iniciando com MOD+CC (Cód. Centro de Custos)** **Sem Integração Contábil.**

a) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e cadastrar o Calendário Contábil (CTBA010).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062113687)

b) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Incluir uma Moeda Contábil (CTBA140)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062140823)

c) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Incluir a amarração Moeda x Calendário (CTBA200)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062169623)

d) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua o Centro de Custos (CTBA030)

**Centro de Custos 10002000 - Despesa**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402073898263)

**Centro de Custos 10003000 - Receita**  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402073910039)

**Resultado esperado:**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062391831)

e) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua os Planos de Contas (CTBA020)

Conta Devedora Sintética 100

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062332951)

Conta Devedora Analítica 100100

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402073957783)

Conta Credora Sintética 200

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402073969815)

Conta Credora Analítica 200100

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062379543)

**Resultado esperado:**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402073976599)

f) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua um Histórico padrão (CTBA070)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062411671)

g) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o produto MOD+CC (MATA010)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377414679)

h) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o Saldo Inicial com quantidade zero e "custo unitário" que será atribuído para o produto MOD10002000 (MATA220)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402370773271)

i) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o produto PA-0003 conforme abaixo (MATA010)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377528599)

j) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua a estrutura conforme abaixo (MATA200)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377514519)

Clique depois em OK, após em Cancelar, veja a estrutura criada e clique no "x".

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062907799)

Será perguntado se deseja recalcular os níveis do produto na estrutura, clique em ok.

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402062917655)

k) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua a Ordem de Produção (MATA650)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377557911)

Observação: Não se Esqueça de habilitar o parâmetro **MV\_REQAUT = A**

l) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua os 2 apontamentos de produção (MATA250)

Inclua o cadastro de Tipo de Movimento (MATA230)  
![mceclip28.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063133975)

Inclua o apontamento de Produção de 2 peças  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402370856087)

\*\* Após a confirmação do apontamento de produção, verifique se a requisição do produto MOD foi incluído no sistema, veja abaixo (MATA241):

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377646999)

Inclua o segundo apontamento de produção com uma peça.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377654679)

\*\* Após a confirmação do apontamento de produção, verifique se a requisição do produto MOD foi incluído no sistema, veja abaixo (MATA241):

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377678103)

**m)** Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Execute a rotina de Custo Médio (MATA330) e **configure as seguintes perguntas da Rotina do custo médio**:

**\* Atualiza Arquivos de Movimentos = Sim**

![MOD 001 AT ARQ.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30139181816599)

**-Centro de Custo Contábil**

  Contas a Inibir De: (Branco)

  Contas a Inibir Ate: ZZZZZZZZZZZZZZZZZZZZZ

**-Centro de Custo ExtraContábil**

  Contas a Inibir De: (Branco)

  Contas a Inibir Ate: (Branco)

**-Calcula Mão de Obra = NÃO** **(Pois o calculo é SEM Integração contábil)**

**![MOD IGUAL  ANAO.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30139181817111)**

**Observação**: Caso o cliente desejar customizar o calculo de mão de obra ele poderá utilizar o ponto de entrada [**MA330MOD**](https://tdn.totvs.com/x/oz_hMQ).

n) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Imprima o relatório "Detalhamento da Ordem de Produção (MATR860)"

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402377969815)

**Importante**: Veja o que valor foi apurado de acordo com os campos **B2\_CM1** e **B2\_CMFIM1** nas requisições dos produtos MOD.

O Produto do tipo MOD também integra com o contábil, se for informado o campo **B1\_CCCUSTO** no cadastro do produto MOD, porém não será filtrado o grupo contábil se for informado no cadastro de produto "**B1\_GCCUSTO**", caso o cliente necessite que seja filtrado o grupo contábil, utilizar um produto diferente da sigla inicial "**MOD**".

## **2° Método - Não utilizando o Código do produto iniciando com MOD e informando no Cadastro de Produtos os campos B1\_CCCUSTO e B1\_GCCUSTO** **(Com integração contábil)**

**Antes de efetuar esse metodo, avaliar se o parametro MV\_PRODMOD esta ativo, para que o produto que não seja iniciado como MOD seja considerado como um serviço.**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025776011-Manufatura-Linha-Protheus-SIGAPCP-Finalidade-do-par%C3%A2metro-MV-PRODMOD> 

a) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e cadastrar o Calendário Contábil (CTBA010)

![mceclip36.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063679767)

b) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Incluir uma Moeda Contábil (CTBA140)

![mceclip37.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063692183)

c) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Incluir a amarração Moeda x Calendário (CTBA200)

![mceclip38.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063707415)

d) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua o Centro de Custos (CTBA180)

**Centro de Custos 20002000 - Despesa**  
**![mceclip39.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063715095)**

**Centro de Custos 20003000 - Receita**  
**![mceclip40.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063724695)**

**Resultado esperado:**

**![mceclip41.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074674711)**

f) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua os Planos de Contas (CTBA020)

Conta Sintética Devedora 300

![mceclip42.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074678807)

Conta Analítica Devedora 300100

![mceclip43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063765783)

![mceclip44.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063784599)

Conta Sintética Credora 400

![mceclip45.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074704663)

Conta Analítica Credora 400100

![mceclip46.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074722199)

**Resultado esperado:**

![mceclip47.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074725015)

g) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua um Histórico padrão (CTBA070)

![mceclip48.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074726935)

**h) Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Inclua um lançamento contábil manual a débito (CTBA102)**

Configurar a pergunta pressione F12 ao entrar no Browser da rotina.

![](https://tdn.totvs.com/download/thumbnails/366649055/image2018-6-4_10-41-33.png?version=1&modificationDate=1528119694000&api=v2)

**Clicar em Incluir e faça o processo para incluir o valor ao centro de custo desejado.**

![mceclip49.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402063858327)

![MOD 003.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/28400602793879)

Lançamento a Debito incluído no sistema.

**SEMPRE:** O lançamento a **DEBITO** para o produto **MOD** ***deve ser maior que o lançamento a CREDITO***, ou isso vai ocasionar custos **NEGATIVOS** do produto com a integração contabil.

Se acaso voce tiver duvidas, sobre ao conceito de distribuilção dos valores contabeis, seja a debito ou credito, deve tratar diretamente com o seu time contabil, ou area contabil Protheus Ativo e Contabil da TOTVS em caso de duvidas, sobre a utilização de lançamentos: Debito/Credito/Partida dobrada  
![mceclip50.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074734615)

i) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o produto com a amarração dos campos **B1\_CCCUSTO e B1\_GCCUSTO(se utilizar grupo contábil) (MATA010).**

**Atenção:** O produto não precisa ter a nomenclatura MOD+CC quando utilizamos os campos B1\_CCCUSTO e B1\_GCCUSTO.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14754727340183)

Preencher os campos B1\_CCUSTO e B1\_GCCUSTO na aba Outros.  
![mceclip54.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074838423)

j) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o Saldo Inicial Zerado para o produto P00001-TST (MATA220)

![mceclip55.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074842647)

l) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e visualize o custo unitário do produto P000001-TST através da rotina "Saldo em estoque (MATA225)"

![mceclip56.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074844567)

m) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua o produto PA-0002 conforme abaixo (MATA010)

![mceclip57.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064056215)

n) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua a estrutura conforme abaixo (MATA200)

![mceclip58.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074885015)

o) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua a Ordem de Produção (MATA650)

![mceclip59.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064107159)

Observação: Não se Esqueça de habilitar o parâmetro **MV\_REQAUT = A**

p) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Inclua os 2 apontamentos de produção (MATA250)

Inclua o cadastro de Tipo de Movimento (MATA230) o campo **Transf. MOD (F5\_TRANMOD)** deve estar igual a **Sim**

![MATA230 MOD.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/28400602796951)

Inclua o apontamento de Produção de 2 peças

![mceclip60.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074906775)

\*\* Após a confirmação do apontamento de produção, verifique se a requisição do produto P00001-TST foi incluído no sistema, veja abaixo (MATA241):

![mceclip61.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064140055)

Inclua o segundo apontamento de produção com uma peça.

![mceclip62.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402074923927)

\*\* Após a confirmação do apontamento de produção, verifique se a requisição do produto P00001-TST foi incluído no sistema, veja abaixo (MATA241):

![mceclip63.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064155671)

q) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Execute a rotina de Custo Médio (MATA330)

Configure as perguntas da Rotina:

-Na rotina de custo médio deve-se atentar as perguntas abaixo:  
  
**-Centro de Custo ExtraContábil**

  Contas a Inibir De: (Branco)

  Contas a Inibir Ate: (Branco)

![MATA330 MOD.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/28400592483095)

ou **-Centro de Custo Contábil**

  Contas a Inibir De: **(Branco)**

  Contas a Inibir Ate: **ZZZZZZZZZZZZZZZZZZZZZ**

![MATA330 MOD 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/28400602804887)

**-Calcula Mão de Obra = SIM** **(Sim, pois agora esta utilizando a MOD com Integração Contábil)**

**![MATA330 MOD 3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/28400602807063)**

r) Acessar o modulo 04 "Estoque e Custos (SIGAEST)" e Imprima o relatório "Detalhamento da Ordem de Produção (MATR860)"

![mceclip65.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402064228247)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402115334295)

**Importante**: Caso não tenha sido custeado, avalie se o parâmetro **MV\_PRODMOD = .T.** Veja o que valor de $ 10.000,00 apurado nas requisições do produto P00001-TST é o mesmo valor que foi lançado no módulo Contábil (Consultar item h).

**Nesse processo o cálculo do custo da MOD é feito da seguinte forma pelo sistema:**

* Custo da Movimentação do MOD = (Soma dos Lançamentos Contábeis no Centro de Custo (CT2\_VALOR) / Soma das Quantidades Requisitadas do produto MOD para a OP (D3\_QUANT)) \* Quantidade da Requisição do produto MOD para a OP (D3\_QUANT)

Importante: Ao executar o Recálculo do Custo Médio, a pergunta "Calcula MOD" deve estar como "Sim", pois o custeamento das requisições de MOD e do produto acabado é realizado ao rodar o Recálculo do Custo Médio, através da obtenção do saldo no centro de custo atrelado, e valorizando os movimentos de MOD de acordo com os valores obtidos.

**Caso,** no padrão a utilização das configurações dos métodos disponíveis no Protheus "**Com Integração Contábil"** e "**Sem Integração Contábil"****não seja atendido a regra de Negócio da Empresa**.

É necessário apoio de Analista Desenvolvedor para Customizar conforme necessidade específica utilizando o [***Ponto de Entrada MA330MOD***](https://tdn.totvs.com/x/oz_hMQ).

***PE MA330MOD Customiza cálculo do custo de mão de obra***  
[***https://tdn.totvs.com/x/oz\_hMQ***](https://tdn.totvs.com/x/oz_hMQ)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MOD/GGF - Conceito e Usabilidade*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402117444247)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*MA330MOD - Customiza calculo do custo de mão-de-obra*](https://tdn.totvs.com/pages/releaseview.action?pageId=6087637)
