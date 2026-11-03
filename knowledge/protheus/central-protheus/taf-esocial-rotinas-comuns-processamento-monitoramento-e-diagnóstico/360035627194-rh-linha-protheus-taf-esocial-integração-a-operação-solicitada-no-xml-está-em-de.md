---
article_id: 360035627194
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 630e028f50a729576ab354a89cd0817099a14e8b438b8e81385d374605560784
fetched_at: '2026-06-28T22:45:20.991056+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - A operação solicitada no
  XML está em desacordo com o cenário do registro na base de dados do TAF
type: support-article
updated_at: '2026-06-26T12:02:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035627194-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-A-opera%C3%A7%C3%A3o-solicitada-no-XML-est%C3%A1-em-desacordo-com-o-cen%C3%A1rio-do-registro-na-base-de-dados-do-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25280614828439)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**

Ao realizar integração dos registros do ERP para o TAF, ocorre a mensagem abaixo:  
**"A operação solicitada no XML está em desacordo com o cenário do registro na base do TAF"**

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões

**Causas**

Este erro acontece quando tentamos integrar um registro que já faz parte da base de dados do TAF, ou seja, já foi integrado ao TAF onde carrega exatamente a mesma informação.

**Solução**Uma vez que o XML/Evento já tenha sido integrado ao TAF e transmitido com sucesso, só pode ser enviado a retificação se o evento estiver ativo na base de dados do TAF, não deve-se mais enviá-lo como inclusão, somente alteração ou exclusão para que não haja esse retorno de rejeição por parte do TAF.

1 - Acesse o XML do seu ERP de origem do evento **(RM, Datasul ou Protheus)**;

2 - Localize a TAG **<indRetif>**:  
![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360046653794)

3 - Verifique qual valor está nesta TAG **(****1 - Inclusão; 2 - Retificação)**;

4 - Se estiver **incluindo** o(s) evento(s) que não foi(ram) transmitido(s), a TAG deverá ficar deste jeito:  
**<indRetif>1</indRetif>**  
Se estiver incluindo de fato, verifique se já não existe o evento que está inserindo na base do TAF e aceito pelo RET;

5 - Se estiver **retificando** o(s) evento(s) que foi(ram) transmitido(s) anteriormente, a TAG deverá ficar desta forma:  
**<indRetif>2</indRetif>**  
Se estiver retificando de fato, verifique se o evento de inclusão existe na base do TAF e aceito pelo RET.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
