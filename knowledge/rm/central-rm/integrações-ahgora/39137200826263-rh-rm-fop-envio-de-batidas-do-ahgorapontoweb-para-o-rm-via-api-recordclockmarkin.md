---
article_id: 39137200826263
category: Integrações - Ahgora
content_hash: 6a4355415aa838987c9a7b498e079efb9cc9e92425e05b12c385283872ef035d
fetched_at: '2026-06-28T22:46:39.910854+00:00'
product: rm
section_id: 36553540355351
source: central-rm
title: RH - RM - FOP - Envio de batidas do Ahgora(PontoWeb) para o RM via API recordClockMarkings
type: support-article
updated_at: '2026-03-19T15:00:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39137200826263-RH-RM-FOP-Envio-de-batidas-do-Ahgora-PontoWeb-para-o-RM-via-API-recordClockMarkings
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39137200819863) Tempo aproximado para leitura: **00:03:40 min**  
  
**Dúvida**  
Como funciona a API **recordClockMarkings** para envio de batidas do ponto web(Ahgora) para o RM?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.2506.263  
  
**Solução**  
A API `v2/recordClockMarkings/integracaobatidas` foi disponibilizada para realizar a **integração de marcações de ponto em lote** com o RM.

Para realizar a chamada da **API REST,** o endpoint deve ser configurado da seguinte forma:

`{protocolo}://{host}:{porta}/api/rh/v2/recordClockMarkings/integracaobatidas`

Lembrando que o **host** e a **porta** devem ser configurados de acordo com o ambiente utilizado. Exemplo:

`http://localhost:8051/api/rh/v2/recordClockMarkings/integracaobatidas`

O método disponibilizado pela API é ***POST***, sendo obrigatório o preenchimento do corpo ***(body)***.

Segue exemplo de um JSON para requisição***:***

```
{ 
    "items" :[
        {
            "codRelogioExtChave": "PONTOWEB", 
            "codFuncMsa": ["00001","00002","00003"],
            "codNsr": 1,
            "datMarcacAces": "2025-09-02",
            "numHorarMarcacAces": 28800,
            "codRep": "55551234567895287",
            "codUsuarExtChave": ["1;00001","2;00002","2;00003"],
            "codPisMsa": "59008268339",
            "codCPF": "51427362653",
            "codFuso": "-0300",
            "inscrEmp": "01234567891234",
            "codCCT":"12345678914258778",
            "numVersLayout": "3"
        },
        {
            "codRelogioExtChave": "PONTOWEB", 
            "codFuncMsa": ["00004"],
            "codNsr": 1,
            "datMarcacAces": "2025-09-02",
            "numHorarMarcacAces": 28800,
            "codRep": "55551234567895287",
            "codUsuarExtChave": ["1;00004"],
            "codPisMsa": "59008268339",
            "codCPF": "51427362653",
            "codFuso": "-0300",
            "inscrEmp": "01234567891234" ,
            "codCCT":"12345678914258778",
            "numVersLayout": "3"
        }
    ]
 }
```

Uma marcação com dados errados ou incompletos não impede que outras marcações corretas sejam integradas. O motivo do erro será retornado na resposta da chamada, na propriedade "**message**". Segue exemplo de resposta:

```
{
    "items": [
        {
            "codRelogioExtChave": "PONTOWEB",
            "codFuncMSA": ["00001","00002","00003"],
            "codNSR": 1,
            "datMarcacAces": "2025-09-02",
            "numHorarMarcacAces": 28800,
            "codRep": "55551234567895287",
            "codUsuarExtChave": ["1;00001","2;00002","2;00003"],
            "codPisMSA": "59008268339",
            "codCPF": "51427362653",
            "codFuso": "-0300",
            "inscrEmp": "01234567891234",
            "codCCT": "12345678914258778",
            "numVersLayout": 3,
            "status": 200,
            "errorCode": "",
            "message": "Gravação efetuada com sucesso"
        },
        {
            "codRelogioExtChave": "PONTOWEB",
            "codFuncMSA": ["00004"],
            "codNSR": 1,
            "datMarcacAces": "2025-09-02",
            "numHorarMarcacAces": 28800,
            "codRep": "55551234567895287",
            "codUsuarExtChave": ["1;00004"],
            "codPisMSA": "59008268339",
            "codCPF": "51427362653",
            "codFuso": "-0300",
            "inscrEmp": "01234567891234",
            "codCCT": "12345678914258778",
            "numVersLayout": 3,
            "status": 400,
            "errorCode": "00002",
            "message": "NSR duplicado. Número já foi importado no codRep informado."
        }        
    ]
}
```

Para consultar os detalhes dos campos da API, consulte: [**Campos da API recordClockMarkings/integracaobatidas**](https://tdn.totvs.com/display/LRM/Campos+da+API)

As marcações enviadas pela API serão gravadas na tabela: **AINTEGRACAOBATIDAS.**

**Configurações RM**

É necessário realizar as seguintes configurações no RM para utilização desta API:

1. Acesse o módulo **Automação de Ponto** > **Configurações | Parametrizador**, no processo 08.01 - Iniciais, avance até a **Etapa 5** - **Integração - Integração Carol/TSA** e marque os parâmetro **"Utilizar integração com o TSA"** e **"Importar batidas integradas via API".**

   **![](https://tdn.totvs.com/download/attachments/682054374/image2022-4-20_18-31-33.png?version=1&modificationDate=1650490293983&api=v2)**
2. O usuário que for utilizado para autenticação na API, precisa estar vinculado em um Perfil do Automação de Ponto que possua as permissões de acesso "**API Integração Batidas**" e "**Desconsiderar Filtro de produto em WebService**" liberadas. O usuário deve ser vinculado no perfil em todas as coligadas que receberão as batidas.![](https://centraldeatendimento.totvs.com/hc/article_attachments/39137216529687)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39137216530327)
3. Para realizar a importação das batidas que estão na tabela **AINTEGRACAOBATIDAS**, acesse o menu **Entrada de Dados | Importar.** Na tela de importação, marque o parâmetro **"Utilizar integração com o TSA",** selecione o período de importação e execute a rotina.

   ![](https://tdn.totvs.com/download/attachments/682054374/image2022-4-20_18-31-56.png?version=1&modificationDate=1650490317120&api=v2)

   Ao final do processo de importação, será exibido um log contendo os detalhes da execução.

   ![](https://tdn.totvs.com/download/attachments/682054374/image-2025-10-15_18-17-14.png?version=1&modificationDate=1760563034203&api=v2)

   **Importante:** Após realizar a importação de batidas, o campo **'CODIMPORTPRODUT'** localizado na tabela **'AINTEGRACAOBATIDAS'** terá seu valor alterado para **'1'**, esse valor sinaliza que as batidas foram importadas. Caso as batidas sejam canceladas ou excluídas não poderão ser reimportadas.

   **Saiba Mais:**

   [**TDN API REST - recordClockMarkings/integracaobatidas (v2)**](https://tdn.totvs.com/pages/viewpage.action?pageId=993703600)
