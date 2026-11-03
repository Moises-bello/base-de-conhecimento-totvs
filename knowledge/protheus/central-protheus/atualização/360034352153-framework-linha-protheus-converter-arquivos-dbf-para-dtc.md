---
article_id: 360034352153
category: Atualização
content_hash: 825fa0b6c8e16fe37a20ae671ab6030ec1da492f4eb918763f093df3daef6179
fetched_at: '2026-06-28T22:42:21.317786+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - Converter arquivos DBF para DTC
type: support-article
updated_at: '2024-03-26T13:23:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034352153-Framework-Linha-Protheus-Converter-arquivos-DBF-para-DTC
---

**Dúvida**Como fazer para converter arquivos do tipo DBF para o formato DTC?  
   
 **Ambiente**Protheus - APSDU - Até a Release 17 do Protheus 12  
  
**Solução**Segue abaixo o procedimento para conversão dos arquivos:  
  
01. Primeiramente, faça um ***backup*** das pastas **System** (ou Sigaadv) e **Profile**. Efetue cópia com os serviços parados, para evitar corromper arquivos.

02. Exclua todos arquivos \*.cdx, sigamat.ind e sigaadv.bmi(se tiver), mpupdlog.log (se tiver) da pasta **System**, e os arquivos \*.cdx da pasta **Profile**

03. Na pasta **System**, renomeie o arquivo sigamat.emp para sigamat.dbf e o arquivo sigaadv.bmd (se tiver) para sigaadv.dbf. Na pasta **Profile** renomeie o arquivo profile.usr para profile.dbf.

04. Acesse o APSDU e siga o procedimento abaixo:  
- Clique em Arquivo / **Importar**  
  
![CAF_01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044412133)  
  
![CAF_02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044412153)  
  
- Em **Rdd Origem**, selecione DBF  
- Em **Informe o diretório**, selecione a pasta System  
- Em **Mascara**, informe \*.DBF  
  
05. Clique em **Avançar**06. Na tela seguinte, marque a caixinha **Todos**, e clique em **Avançar**  
  
![CAF_03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044412193)  
  
- Em **Rdd Destino**, selecione **Ctree**  
- Em **Informe o diretório**, selecione a pasta **System**  
  
07. Clique em **Finalizar  
  
![CAF_04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044412173)**08. Será apresentada uma janela questionando se **Deseja utilizar a importação multi-processo**. Selecione **Sim** ou **Não** conforme sua necessidade.  
  
09. Aguarde o processo de importação. O processo pode demorar um pouco dependendo da quantidade de empresas e do servidor.

|  |
| --- |
| **Aviso**:  Poderão ser exibidas mensagens de falta de acesso exclusivo a alguma tabela, conforme imagem de exemplo abaixo. Se for uma tabela irrelevante, como essa de backup, pode prosseguir. Caso contrário, é necessário abandonar o processo e conceder acesso exclusivo às tabelas.  CAF_05.png |

10. **Repita o procedimento acima para a pasta Profile**.  
  
Após ter executado todo o procedimento, execute os seguintes passos nas pastas:  
  
**Na pasta System:**  
- Renomeie o arquivo **sigamat.dtc** para **sigamat.emp**  
- Renomeie o arquivo **sigaadv.dtc** para **sigaadv.bmd**  
- Remova os arquivos **\*.dbf**

**Na pasta Profile:**  
- Renomeie o arquivo **profile.dtc** para **profile.usr**Segue abaixo um exemplo de configuração do arquivo **appserver.ini** para base em **Ctree**:  
  
[ENVIRONMENT]  
SourcePath=C:\TOTVS 11\apo  
RootPath=C:\TOTVS 11\Protheus\_Data  
StartPath=\system\  
RpoDb=top  
RpoLanguage=Portuguese  
RpoVersion=110  
LocalFiles=CTREE  
LocalDBextension=.dtc  
  
  
**Observação**  
A partir da Release 23 do Protheus 12 não é possível manipular arquivos DBF via APSDU.
