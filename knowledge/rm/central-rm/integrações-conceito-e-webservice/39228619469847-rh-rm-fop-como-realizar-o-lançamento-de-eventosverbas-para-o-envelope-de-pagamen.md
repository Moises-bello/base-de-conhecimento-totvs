---
article_id: 39228619469847
category: Integrações - Conceito e WebService
content_hash: 1f3f92a30dccac5c4cf8b27cdf1f86cba551a1cb8ed51de9f63f237bf343ac45
fetched_at: '2026-06-28T22:46:44.844280+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Como realizar o lançamento de eventos/verbas para o envelope
  de pagamento via DataServer ou API?
type: support-article
updated_at: '2026-03-24T17:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39228619469847-RH-RM-FOP-Como-realizar-o-lan%C3%A7amento-de-eventos-verbas-para-o-envelope-de-pagamento-via-DataServer-ou-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39228610811671) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Como realizar o lançamento de eventos/verbas para o envelope de pagamento via DataServer ou API? **FopLancExternoData**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
O DataServer/API indicado nesta documentação é o **recomendado pela TOTVS**, pois incorpora uma camada adicional de **segurança**. Nesse fluxo, após o lançamento das verbas via WebService, o Departamento Pessoal (DP) pode visualizar a movimentação por meio da tela de **Consulta de Movimento de Integração** e, caso esteja correta, realizar a aprovação para inclusão no envelope dos funcionários, pelo **Grupo de Eventos**.  
  
Para realizar o lançamento de eventos/verbas para o envelope de pagamento através de API ou Webservice, a inserção deverá ser feita através de um lançamento externo (Consulta Movimento Integração). Abaixo, exemplificamos esse processo utilizando as ferramentas **SoapUI** e **Postman**:

**🔹**[**Lançamento via SoapUI (Dataserver)**](#SoapUI)

**🔹**[**Lançamento via Postman (Api rest)**](#Postman)

**🔹**[**Efetivação dos lançamentos no envelope**](#Envelope)

### 🔹Lançamento via Dataserver (SoapUI):

Para obter um XML exemplo, execute via SOAP um **ReadRecord (Função de consultar dados)** no dataserver **FopLancExternoData**. Para executar este método, devem ser fornecidas em "PrimaryKey" as chaves primárias:

* **CODCOLIGADA;**
* **CHAPA;**
* **ANOCOMP;** (Ano competência)
* **MESCOMP;** (Mês competência)
* **CODEVENTO;** (Código do evento/verba)
* **IDMOVTEMP; (**Id do lançamento externo**)**

Em "DataServerName" informe o valor **FopLancExternoData**.

Em contexto, forneça os seguintes parâmetros:

* **CODCOLIGADA**
* **CODUSUARIO**
* **CODSISTEMA**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234506324247)

XML exemplo:

```
<![CDATA[<FopLancExterno >
  <PFMOVTEMP>
    <CODCOLIGADA>1</CODCOLIGADA>
    <CHAPA>00001</CHAPA>
    <ANOCOMP>2026</ANOCOMP>
    <MESCOMP>6</MESCOMP>
    <CODEVENTO>0005</CODEVENTO>
    <IDMOVTEMP>-1</IDMOVTEMP>
    <HORA>300</HORA>
    <REF>0.00</REF>
    <VALOR>0.00</VALOR>
    <ORIGEMEVENTO>7</ORIGEMEVENTO>
    <DATAINCLUSAO>2026-02-26T11:23:13</DATAINCLUSAO>
    <CODUSUARIO>mestre</CODUSUARIO>
    <TIPOLANCAMENTO>15</TIPOLANCAMENTO>
    <HORAFORMATADA>005:00</HORAFORMATADA>
  </PFMOVTEMP>
</FopLancExterno>]]
```

Após o obter o XML exemplo, para inserir um novo registro, utilize o método **SaveRecord**. Atualize os valores base do XML para as informações do novo registro que será inserido. Atente-se ao formato exigido pelas tags, seguindo o mesmo padrão da estrutura XML obtida no ReadRecord.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234515943319)

**Observação:**

Utilize `IDMOVTEMP`**= -1** para geração do ID sequencial automático

`ORIGEMEVENTO` = 7 (Sistema Externo)

`TIPOLANCAMENTO` = 16 (Lançamento Sistema Externo)

Após execução, o lançamento ficará disponível na tela "**Consulta Movimento Integração**" em "**Folha Mensal**":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234506328599)

### 🔹Lançamento via API Rest (Postman):

Para obter um "Json" exemplo, execute o método GET no endopint "/rmsrestdataserver/rest/FopLancExternoData". Exemplo:

`http://localhost:8051/rmsrestdataserver/rest/FopLancExternoData`

Observação: Inclua no **Headers** a chave **CodColigada** com o valor correspondente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234515947543)

JSON Exemplo:

```
 {
         
            "CODCOLIGADA": 1,
            "CHAPA": "00001",
            "NOME": "ITAMAR MENDES",
            "ANOCOMP": 2026,
            "MESCOMP": 7,
            "CODEVENTO": "0005",
            "DESCRICAO": "SALARIO FAMILIA",
            "IDMOVTEMP": -1,
            "HORA": 300,
            "HORAFORMATADA": "005:00",
            "REF": 0.00,
            "VALOR": 0.00,
            "VALORFORCADO": 0,
            "CODCCUSTO": null,
            "ORIGEMEVENTO": 7,
            "DATAINCLUSAO": "2026-02-26T11:23:13-03:00",
            "CODUSUARIO": "mestre",
            "TIPOLANCAMENTO": 15,
            "IDITEMCONTABIL": null,
            "IDCLASSEVALOR": null
        }
```

Após obter o JSON exemplo, atualize os valores mantendo o mesmo padrão e execute método Post para inserir um novo registro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234506333975)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39234515954327)

### 🔹 Efetivação dos lançamentos no envelope:

Para lançar os eventos para o envelope, realize os seguintes passos:

Acesse: **Folha Mensal** **| Lançamento | Grupo de Eventos**. Ao parametrizar o grupo de eventos, será necessário marcar a flag**"Lançar eventos da integração com outros aplicativos".**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39235127332247)

Será habilitada a aba**Integração com outros aplicativos.** Marque a flag "**Sistemas Externos".**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39235135837207)

Após realizar o lançamento do grupo de evento parametrizado, o evento ficará disponível no envelope de pagamento do funcionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39236520720535)

Saiba mais:

[RH - RM - FOP - Como identificar e consumir DataServer e API disponíveis nos produtos de RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37535317324823-RH-RM-FOP-Como-identificar-e-consumir-DataServer-e-API-dispon%C3%ADveis-nos-produtos-de-RH)
