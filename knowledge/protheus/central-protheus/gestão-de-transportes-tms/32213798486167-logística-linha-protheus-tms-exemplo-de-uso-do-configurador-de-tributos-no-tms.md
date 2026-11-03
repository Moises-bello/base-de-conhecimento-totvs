---
article_id: 32213798486167
category: Gestão de Transportes (TMS)
content_hash: 28d07a65d5530536fcc5a04bf7525911d8c66bab62e55de1a0581af6fab23bae
fetched_at: '2026-06-28T22:45:27.754803+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Exemplo de uso do Configurador de Tributos
  no TMS
type: support-article
updated_at: '2026-01-27T13:56:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32213798486167-Log%C3%ADstica-Linha-Protheus-TMS-Exemplo-de-uso-do-Configurador-de-Tributos-no-TMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32213798470807) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Como cadastrar o **Configurador de Tributos** para obter os impostos no cálculo do frete do **TMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para que o cálculo do frete a receber no **TMS** considere os impostos cadastrados no **Configurador de Tributos**, utilizamos quatro variáveis:

* Tomador de serviço;
* Produto de cálculo;
* CFOP;
* Região de Origem e Região de Cálculo do documento.

Caso necessite de uma quinta variável, temos o novo campo **DV1\_OPER** **- Tipo Operação** para utilizar em cenários específicos. Mais informações no artigo **Logística - Linha Protheus - TMS - Regras de tributação por cliente no Configurador de Tributos.**  
  
Para isso, devemos realizar e validar os seguintes cadastros:  
  
**Processo para utilização:**

No **Configurador de Tributos - FISA170**, para a utilização do cálculo do frete no **TMS**, utilizaremos apenas duas pastas cadastrais:

1. **Perfis**
2. **Regras de Cálculo Documento Fiscal**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32214849704471)**

**Cadastros da pasta Regras Fiscais -  Perfis**  
O cadastro de Perfis determina quando o tributo ou imposto será utilizado no cálculo do frete conforme a combinação entre **tomador de serviço**, **produto de cálculo**, **origem/destino** e **CFOP**, ou seja, se não tivermos os devidos cadastros nesta pasta, o cálculo de frete continuará utilizando as regras de impostos definidos no **TES**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32215372059287)**

**Perfil de Produto**  
Produto de cálculo utilizado no cálculo do frete. O produto informado neste cadastro deve ser o mesmo utilizado no campo **Cod. Produto - DUI\_CODPRO** do cadastro de **Configuração de Documentos** - **TMSA150**, caso contrário, se o cliente utilizar o produto de transporte informado na digitação do **Documento do Cliente - DTC\_CODPRO**, o cálculo do frete não considerará as regras do **Configurador de Tributos**.   
Uma outra forma de identificar qual o código de produto para informar neste cadastro é, pesquise um documento de exemplo na tabela **SD2**, no campo **D2\_COD**, teremos o código do produto a ser utilizado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32215372060951)

Na seção **Origens dos Produtos**, deixar somente o **NACIONAL**:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32215387157527)**

Ao configurar o **Perfil de Produto** para uso na geração do **CTe**, o produto de cálculo utilizado não deve ter nenhuma informação relacionado a **ISS** cadastrado no cadastro de **Produto - MATA10**, caso contrário, o cálculo do frete não considerará as regras do **Configurador de Tributos**.  
  
**Perfil de Operação**  
Relação de **CFOPs** que serão utilizados na geração dos documentos de saída. Este cadastro está associado ao **CFOP** utilizado no cadastro do **TES**, campo **Cod. Fiscal -** **F4\_CF.** Este é um dos motivos para a continuidade do uso do **TES** no cálculo do frete com o uso do **Configurador de Tributos**.  
Uma outra forma de identificar qual o **CFOP** para informar neste cadastro é, pesquise um documento de exemplo na tabela **SD2**, no campo **D2\_CF**, teremos o **CFOP** a ser utilizado  
No **Perfil de Operação**, podemos incluir manualmente cada **CFOP** desejado, ou então, utilizar a carga inicial contendo todos os **CFOPs** de saída disponível com o código **000050 - Todas as saídas:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32215787049367)

**Perfil de Participante**  
Neste cadastro serão definidos os participantes (clientes e/ou fornecedores) envolvidos na operação. Para identificar qual é o cliente tomador de serviço de um **CTe**, na tabela **DT6**, utilizamos os campos **DT6\_CLIDEV** e **DT6\_LOJDEV**.  
Neste cadastro, podemos informar o cadastro do cliente tomador de serviço ou utilizar um único cadastro de Participante para todos os clientes da base. Para isso, basta cadastrar da seguinte forma:

**Campo Participante = TODOS**  
**Loja = ZZ**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32215951962391)

**Perfil de Origem/Destino**  
Similar ao cadastro de **Regras de tributação - TMSA410**, este cadastro define as combinações de estados de origem e destino utilizados nas operações de transportes baseado nas **UFs** referentes aos **Grupos de Regiões - TMSA115** presentes nos campos **DT6\_CDRORI** e **DT6\_CDRCAL**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32216130427927)

Podemos utilizar a carga inicial contendo todas as combinações de **UFs** disponível em **000002 - Todas as UFs:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32216111510167)

Para utilizar o **TMS** com o **Configurador de Tributos**, ainda será necessário utilizar os cadastros de **Regras de Tributação - TMSA410** e **Regras Por Cliente** - **TMSA600** para determinação do **TES**, pois é a partir do **TES** que se estabelece o **CFOP** utilizado no cadastro de **Perfil de Operação**.   
O cadastro do **TES** continuará sendo utilizado, mas com um outro direcionamento, entre eles, o uso do **CFOP**, e, a partir da **release 12.1.2510**, serão desativados os campos do **TES** que configuram os impostos.

**Cadastros da pasta Regras Fiscais - Regras de Cálculo Documento Fiscal**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32216557747863)**

Nesta pasta existem os cadastros que definem as informações relacionadas ao cálculo do imposto ou tributo, como base de cálculo, alíquota, escrituração e amarração dos cadastros definidos nas etapas anteriores.  
Durante o processo de cadastros das regras fiscais, quando se depararem com o termo **Valor da Mercadoria**, para o **TMS**, este termo se refere ao **Valor do Frete** referente ao campo **DT6\_VALFRE**.  
Neste artigo focaremos apenas nos cadastros que devem ser realizados para que o **TMS** considere o **Configurador de Tributos**. Os demais cadastros relacionados aos impostos estarão descritos nas documentações disponíveis na seção **Anexo**.  
Para que o **TMS** acate o **Configurador de Tributos**, todos os cadastros realizados anteriormente devem ser associados em **Regra de Cálculo - Documentos Fiscais** na seção **Definição dos Perfis:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32216763146007)

Ao calcular e gerar o documento de transporte, para identificar se o cálculo do frete acatou o **Configurador de Tributos**, na consulta do documento, aba **Impostos**, teremos os tributos que foram incluídos no cadastro de **Regra de Cálculo - Documentos Fiscais:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35865752354583)

Caso a aba **Impostos** não seja visualizada ao consultar o documento, basta habilitar o parâmetro **MV\_TMSCFIS**.  
Pode-se também consultar o documento na tabela **SD2 - Itens de Venda da NF**, onde teremos o novo campo **Id. Tributos - D2\_IDTRIB** preenchido. Se este campo **D2\_IDTRIB** estiver vazio, o cálculo do frete não considerou o **Configurador de Tributos**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32216715217303)

**Glossário**  
**CFOP** - Código Fiscal de Operações e de Prestações  
**TES** - Tipos de Entrada e Saída  
**UF** - Unidade Federativa  
  
**Anexo**  
Para mais informações sobre os demais cadastros necessários para o uso do **Configurador de tributos - FISA170****,** acesse os *links*:  
[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)  
[Logística - Linha Protheus - TMS - Como gerar CBS e IBS no XML do CTe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35970385689623-Log%C3%ADstica-Linha-Protheus-TMS-Como-gerar-CBS-e-IBS-no-XML-do-CTe)  
[Logística - Linha Protheus - TMS - Regras de tributação por cliente no Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34664608748951-Log%C3%ADstica-Linha-Protheus-TMS-Regras-de-tributa%C3%A7%C3%A3o-por-cliente-no-Configurador-de-Tributos)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar o cálculo do IBS e CBS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS)  
[Webinar TOTVS | Configurador de tributos no TMS](https://www.youtube.com/watch?v=RmTKha1aBvY)  
[Webinar TOTVS | Treinamento configurador de tributos](https://www.youtube.com/watch?v=msMdG2FEe1U)  
[Playlist Configurador de Tributos - Protheus](https://www.youtube.com/playlist?list=PLXa8l0dq5zRmE7w09pc7BvMmYxPA4e58f)  
Para mais informações sobre a nova **Reforma Tributária** acesse nosso [Espaço Reforma Tributária](https://espacolegislacao.totvs.com/reforma-tributaria/).  
Para receber todas as noticias da **TOTVS** sobre a **Reforma Tributária** e novidades do **Protheus** **TMS**, participe de nossas comunidades no **WhatsApp**, para isso, acesse:  
[Comunidade TOTVS Backoffice Informa Reforma Tributária](https://chat.whatsapp.com/GZcXEDSwlLRBdK1RHlqHy3)  
[Comunidade TOTVS Logística Informa](https://chat.whatsapp.com/DvAw2fomRHU0sqaQl6nsNA)
