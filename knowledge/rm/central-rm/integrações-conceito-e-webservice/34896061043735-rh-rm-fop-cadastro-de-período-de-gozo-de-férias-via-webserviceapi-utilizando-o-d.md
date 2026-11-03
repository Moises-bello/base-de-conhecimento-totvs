---
article_id: 34896061043735
category: Integrações - Conceito e WebService
content_hash: f451677357ba56a137a078a522ae42c2741fe4eec68b517bc01c98a3d9344472
fetched_at: '2026-06-28T22:46:44.873756+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Cadastro de Período de gozo de férias via WebService/API utilizando
  o DataServer FopFuFeriasPerDataBR
type: support-article
updated_at: '2025-09-15T11:43:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34896061043735-RH-RM-FOP-Cadastro-de-Per%C3%ADodo-de-gozo-de-f%C3%A9rias-via-WebService-API-utilizando-o-DataServer-FopFuFeriasPerDataBR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34896031809687)** Tempo aproximado para leitura:**00:08:00 min**

**Dúvida**  
Como cadastrar um período de gozo de férias no módulo Folha de Pagamento utilizando API / Web Service via SoapUI ou Postman  
  
**Ambiente**

* TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Para cadastrar um período de gozo no RM via WebService/API, utiliza-se o **DataServer FopFuFeriasPerDataBR**.

Antes de cadastrar um novo período de gozo, recomenda-se **consultar os dados de um já existente**. Isso retorna um XML ou JSON pronto, que pode ser utilizado como base para o cadastro de um novo.

Abaixo, exemplificamos esse processo utilizando as ferramentas **SoapUI** e **Postman**:

[1- Consulta e cadastro via SoapUI](#soap)

[2- Consulta e cadastro via Postman](#post)

Processo via **SoapUI**

1. Para realizar o consumo dos dados, é necessário, primeiramente, executar um **ReadRecord** para obter as informações base.

   Para isso, devem ser fornecidas as chaves primárias:

   * **CODCOLIGADA** (código da coligada do funcionário)
   * **CHAPA** (chapa do funcionário em questão)
   * FIMPERAQUIS (data fim do período aquisitivo)
   * DATAPAGTO (data de pagamento das férias)

   Além das chaves primárias, é imprescindível informar o nome do **DataServer** correspondente, que, neste caso, é o **FopFuFeriasPerDataBR**.

   Por fim, deve-se especificar o contexto do consumo, fornecendo os seguintes parâmetros:

   * **CODCOLIGADA**
   * **CODUSUARIO**
   * **CODSISTEMA**

   Abaixo, segue um exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34896061031319)

OBS: Lembre-se de colocar a autenticação (basic), no canto inferior esquerdo

        2. Em seguida, será necessário obter o **XML** gerado após o consumo do **DataServer**. Para isso, deve-se acessar a aba **XML** e extrair as informações disponíveis na tag **"ReadRecordResult"**, a partir da tag  "<![CDATA[", conforme o exemplo abaixo:

![Gravar_2025_09_12_10_01_41_685-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34896061032343)

       3. Após copiar o XML, vamos acessar o método SaveRecord e informar o DataServer em questão (FopFuFeriasPerDataBR), o XML que copiamos e também o contexto da mesma forma que fizemos no ReadRecord, conforme o exemplo a baixo:

![Gravar_2025_09_12_11_53_44_439-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34896061033367)

      4. Em quarto passo você deve alterar as informações base para as informações do novo funcionário que será cadastrado, se atente ao formato que as tags pedem para serem inseridas, conforme está na documentação do DataServer.

***Clique aqui para ver o conteúdo de um XML pronto de exemplo !*** 

```
<<![CDATA[;
        

  <FopPFUFeriasPer>
  <PFUFeriasPer>
    <CODCOLIGADA>1</CODCOLIGADA>
    <CHAPA>00004</CHAPA>
    <FIMPERAQUIS>2001-05-31T00:00:00</FIMPERAQUIS>
    <DATAPAGTO>2011-09-30T00:00:00</DATAPAGTO>
    <DATAINICIO>2011-10-01T00:00:00</DATAINICIO>
    <DATAFIM>2011-10-05T00:00:00</DATAFIM>
    <DATAAVISO>2011-09-02T00:00:00</DATAAVISO>
    <NRODIASABONO>0.00</NRODIASABONO>
    <SITUACAOFERIAS>M</SITUACAOFERIAS>
    <NRODIASFERIAS>5.00</NRODIASFERIAS>
    <NRODIASFERIADO>0.00</NRODIASFERIADO>
    <NRODIASFERIASCORRIDOS>0.00</NRODIASFERIASCORRIDOS>
    <NRODIASABONOCORRIDOS>0.00</NRODIASABONOCORRIDOS>
    <POSICAOABONO>0</POSICAOABONO>
    <PERMITEFINALIZARFERIAS>false</PERMITEFINALIZARFERIAS>
    <PERMITELANCAMENTOFERIAS>false</PERMITELANCAMENTOFERIAS>
    <PERMITEANTECIPARFERIAS>false</PERMITEANTECIPARFERIAS>
    <NOME>ADALBERTO DE JESUS LIMA</NOME>
    <MOTIVOMUDANCASITUACAO>1</MOTIVOMUDANCASITUACAO>
    <MOTIVOMUDANCASITUACAORETORNO>1</MOTIVOMUDANCASITUACAORETORNO>
  </PFUFeriasPer>

  <PFuFerias>
    <CODCOLIGADA>1</CODCOLIGADA>
    <CHAPA>00004</CHAPA>
    <FIMPERAQUIS>2001-05-31T00:00:00</FIMPERAQUIS>
    <INICIOPERAQUIS>2000-06-01T00:00:00</INICIOPERAQUIS>
    <FALTAS>0</FALTAS>
    <PERMITEANTECIPARFERIAS>false</PERMITEANTECIPARFERIAS>
    <LIMITEGOZO>2002-05-02T00:00:00</LIMITEGOZO>
    <ESTAVENCIDO>true</ESTAVENCIDO>
    <DIASAMARCAR>20.00</DIASAMARCAR>
    <SALDOTOTAL>340.0</SALDOTOTAL>
    <SALDOPOSSIVEL>30.0</SALDOPOSSIVEL>
    <SALDOPERIODO>30.0</SALDOPERIODO>
    <PERIODOABERTO>1</PERIODOABERTO>
    <FALTASPROP>14.18</FALTASPROP>
    <FIMPROXPERAQUIS>2002-05-31T00:00:00</FIMPROXPERAQUIS>
    <LOGLIMITEGOZO xsi:type="xs:string" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Período das Férias: 01/06/2000 a 31/05/2001

Total de dias a mais na contagem do período dobrado: 0 

Data de Vencimento do período aquisitivo: 31/05/2001
Data Limite para o Final das férias: 31/05/2002

Data Limite para Início das férias, considerando o saldo de 30 dias: 02/05/2002</LOGLIMITEGOZO>
    <CODTIPO>N</CODTIPO>
    <CODTIPOCONTRATO>false</CODTIPOCONTRATO>
    <NAOCALCULARECIBOFERIAS>false</NAOCALCULARECIBOFERIAS>
    <FERIASDIASUTEIS>false</FERIASDIASUTEIS>
  </PFuFerias>

  <PFunc>
    <CODCOLIGADA>1</CODCOLIGADA>
    <CHAPA>00004</CHAPA>
    <NOME>ADALBERTO DE JESUS LIMA</NOME>
    <CODSITUACAO>A</CODSITUACAO>
    <CODTIPO>N</COD
  </PFunc>
</FopPFUFeriasPer>]]>
```

Processo via **Postman**

1. 1. Assim como no **SOAP**, o primeiro passo é obter as informações do **JSON** base para realizar o envio. Para isso, deve-se utilizar a **URL** do exemplo abaixo e informar o **DataServer** correspondente no método **GET**.

      *Além disso, caso desejem pode ser aplicado um filtro por **ID**, pois, caso o **GET** seja executado sem filtros, todos os funcionários serão retornados por padrão. Isso pode impactar o desempenho e resultar em alguns campos sendo carregados como **nulos**. Portanto, a aplicação de um **filtro por ID** pode ajudar nesse caso*

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34896031811991)

             2. Após essa etapa, copie apenas as informações que antecedem a chave **"{"** da tag **"id"** e finalize a cópia ao final dessa chave.

   ![Gravar_2025_09_12_12_23_29_202-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34896031813143)

            3. Após copiar os dados base utilizando o método **GET**, é necessário alterar o método para **POST** e informar no **body** o **JSON** base copiado.

   Diferente do **GET**, no **POST** **não** é necessário informar o **ID** nem aplicar um **filtro**.

   Ao finalizar a estrutura do **JSON**, certifique-se de incluir a chave de fechamento corretamente e garantir que não haja uma vírgula antes dessa chave, evitando erros de formatação.

   Segue um exemplo abaixo:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/34896031813655)

            4. Em quarto passo você deve alterar as informações base para as informações do novo funcionário que será cadastrado, se atente ao formato que as tags pedem para serem inseridas, por isso tomamos como base o Json de outro funcionário. Feito as alterações pode consumir normalmente.

   ***Clique aqui para ver o conteúdo de um JSON pronto de exemplo !***

   ```
    {
               "CODCOLIGADA": 1,
               "CHAPA": "00004",
               "FIMPERAQUIS": "2001-05-31T00:00:00-03:00",
               "DATAPAGTO": "2011-11-01T00:00:00-03:00",
               "DATAINICIO": "2011-11-01T00:00:00-03:00",
               "DATAFIM": "2011-11-05T00:00:00-02:00",
               "SITUACAOFERIAS": "M",
               "NRODIASFERIAS": 5.00,
               "NRODIASABONO": 0.00,
               "IMAGEMSITUACAO": "Marcadas"
           }
   ```

   **Saiba mais**

   [Cross Segmentos - Backoffice RM - Integração - WebServices - Lista de DataServers Web Services](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5275823964567-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Lista-de-DataServers-Web-Services)

   [Cross Segmentos - Backoffice RM - Integração - WebServices - Utilizando o SoapUI para consumir DataServers RM via WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices)
