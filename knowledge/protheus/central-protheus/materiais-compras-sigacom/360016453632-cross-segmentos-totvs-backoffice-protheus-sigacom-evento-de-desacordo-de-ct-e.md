---
article_id: 360016453632
category: Materiais - Compras (SIGACOM)
content_hash: 5cdf7a04dd5dd3813389ebb863abed194a30dfa1041cc838107238669686f68c
fetched_at: '2026-06-28T22:41:08.855644+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Evento de Desacordo
  de CT-e
type: support-article
updated_at: '2025-02-24T12:54:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016453632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Evento-de-Desacordo-de-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30192763795351)*** Tempo aproximado para leitura: **00:02:30 min****Dúvida**Evento de Desacordo de **CT-e**. Se no **XML** houver alguma divergência com relação aos dados do tomador do documento, orientamos que entre em contato com seu departamento **Fiscal** para validar o caso com a Transportadora.   
Se houver necessidade de emitir o **Documento Desacordo do CT-e** no módulo **Compras**, siga orientação a seguir.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - Compras - A partir da versão 12.  
  
**Solução**Orientações básicas para emitir o documento:

Via configurador crie os campos **F1\_IDDES** e **F1\_OBSDES**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055984453)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055985533)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055984893)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055985013)

No cadastro do Fornecedor deve constar preenchido a informação de Inscrição Estadual:

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055998173)

Na rotina **MATA103** verificar se a chave consta correta:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085466694)

Através da rotina **MATA103** posicione no documento e configure os parâmetros em **Outras Ações** > **Ev. Desacordo** >  **Parâmetros**.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055113474)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055991393)

Se o parâmetro **MV\_ADMNFE** estiver habilitado, pode apresentado Help **SEMPERM** que é validado através da função **SpedEpecPar** do fonte **SPEDNFE** conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081114154)

* O Fuso horário deve ser configurado com base na localização de sua filial.
* O pergunte relacionado ao Ambiente deve ser configurado com a mesma informação do documento.

**Exemplo:** Se o **CT-e** for de **homologação** o ambiente deve constar também em **homologação**, caso o documento esteja em **Produção**, a configuração dos parâmetros deve constar com a mesma informação.

Através da rotina de **Documento de Entrada -** **MATA103** posicione no documento e após configuração prévia dos parâmetros clique em **Outras Ações** > **Ev. Desacordo** >  **Ev. Desacordo**.

Informe a justificativa e confirme:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055115534)

![mceclip24.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056005613)

 Nesse momento o registro é enviado para o **TSS** processar a transmissão para a SEFAZ.  
 Através da rotina **Documento de Entrada - MATA103** posicione no documento e após configuração prévia dos parâmetros clique em **Outras Ações** > **Ev. Desacordo** > **Monitor Desacordo**.

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055999173)

Os registros relacionados à Eventos são gravados na tabela **SPED150**, os principais campos que podem ser consultados caso seja necessário executar alguma validação junto à SEFAZ:

* **ID\_EVENTO** - Chave do desacordo;
* **TPEVENTO** - Tipo de Evento do desacordo (6101110);
* **NFE\_CHV** - Chave do CTE;
* **AMBIENTE** - 1 (Produção) ou 2 (homologação);
* **XML\_ERP** - xml de envio;
* **XML\_SIG** - xml da assinatura;
* **XML\_RET** - xml de retorno;
* **PROTOCOLO** - Número do protocolo do registro.

Na consulta da [Sefaz](http://www.cte.fazenda.gov.br/portal/) é possível verificar o vínculo do desacordo ao documento conforme exemplo da imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059822074)

Nesse momento o registro aguarda retorno do **TSS** sobre a transmissão da SEFAZ.

![mceclip25.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055130154)

Após pressionar **Refresh** o registro é atualizado com o **Evento** vinculado.

![mceclip26.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056007513)

Quando o registro é vinculado a legenda é alterada conforme imagem abaixo:

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055124214)

O Sistema apresenta o alerta para exclusão do **CT-e** para que não haja inconsistência de dados para quando o documento correto for lançado no ambiente:

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055116054)

Quando há rejeição de **Evento de Desacordo** o Sistema altera a legenda do Documento de Entrada.

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055993973)

Para consultar o motivo é possível acessar o **Monitor de Desacordo**.

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055116254)

![mceclip27.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055132054)

**Possíveis erros:**

* **755 - Rejeição: Autor do evento prestação do serviço em desacordo deve ser o tomador do****serviço do CT-e**

O responsável pela transmissão deve ser o Tomador do Serviço com base no [Manual do Contribuinte](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=) disponível no [Portal da Sefaz](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=33ol5hhSYZk=) para *download* caso seja necessário:

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056001933)

No exemplo do **XML** abaixo quem ficará responsável por enviar o **Evento de Desacordo** será o Remetente:

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056002433)

### **Atenção**

Se for realizar apenas teste em seu ambiente, deve ser solicitada ao emitente do Conhecimento de Transporte Eletrônico que envie um **CT-e** no ambiente de HOMOLOGAÇÃO da SEFAZ, assim ao enviar o evento em ambiente de homologação irá ser autorizada ou caso seja uma chave de PRODUÇÃO precisa enviar o evento de desacordo em produção, basta entrar nos parâmetros, imagem abaixo, e informar o ambiente de Produção para retransmitir o evento, ou seja se o **CT-e** for de homologação o ambiente deve constar também em homologação, caso o documento esteja em Produção, a configuração dos parâmetros deve constar com a mesma informação.

![](https://totvssuporte.zendesk.com/attachments/token/mquCi6QU2o2psBiEKXTYSfRnm/?name=inline70046165.png)

**Para mais detalhes sobre o Evento [clique aqui](https://tdn.totvs.com/display/public/PROT/1553966+DMANMAT02-6506+DOCUMENTO+ENTRADA+DESACORDO+CTE)**

Caso necessário teste em ambiente de homologação:

* Pacote acumulado **TSS - [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493-MP-NFE-Documentos-Eletr%C3%B4nicos-NFe-NFSe-MDFe-MDe-?source=search)**
* Pacote acumulado **COMPRAS -** **[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**
* Pacote acumulado **TMS -** [**Clique Aqui**](https://tdn.totvs.com/pages/releaseview.action?pageId=553908682)

**Saiba mais**

[Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGACOM - Ao clicar no monitor do Evento de Desacordo Cte não ocorre nenhuma ação. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419852717207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Ao-clicar-no-monitor-do-Evento-de-Desacordo-Cte-n%C3%A3o-ocorre-nenhuma-a%C3%A7%C3%A3o-O-que-fazer-?source=search)

**[Implementação do processo de CTE Substituto na opção Desacordo do CTE](https://tdn.totvs.com.br/display/public/PROT/PCOM12079+-+CT-e+Substituto)**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
