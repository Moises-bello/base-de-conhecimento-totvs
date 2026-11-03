---
article_id: 12204910219671
category: Anuais
content_hash: 8b12ef889356007dfb9127f4f4b7e0725d662fb52975c56998a7bd89d1d2e78c
fetched_at: '2026-06-28T22:46:51.047832+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP - Informe de Rendimentos/Novo Modelo
type: support-article
updated_at: '2026-02-26T15:09:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12204910219671-RH-RM-FOP-Informe-de-Rendimentos-Novo-Modelo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38660845492759) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
O novo modelo do informe de Rendimentos encontra-se disponível a partir de qual release e patch e quais foram as implementações realizadas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir do release 12.1.2209.169 ou superiores  
  
**Solução**  
Foi disponibilizado o novo modelo do Informe de Rendimentos denominado como **FOPREL0008 - Informe de rendimentos - NOVO MODELO**, que deve ser importado através do menu **Gestão |  Totvs Compartilhamento** e será gerado através do menu **Anuais | DIRF/Informe de Rendimentos:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12204814982167)**

**Para mais informações sobre como importar o relatório acesse o link abaixo:**  
[Framework - Linha RM - Frame - TOTVS Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento)

**Importante**  
Devido a necessidade de reformulação do quadro 7 (Informações complementares), foi criada a tabela **PDIRFCOMPLEMENTO**, onde as informações passam a ser armazenadas em colunas ao invés de serem armazenada em apenas um campo; assim a impressão das informações deste campo ficarão alinhadas semelhante aos demais campos.  Lembrando que, essa tabela é preenchida durante o processamento do Informe de Rendimentos apenas quando marcadas as opções **Lançar Valores para o Gerador de Relatórios** e **Deletar Ano de Referência** conforme mostrado na imagem abaixo:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12204203964951)**

O informe de rendimentos que já esta processado e disponibilizado no portal antes da implementação, será exibido no leiaute antigo, devido ainda não existirem dados na tabela PDIRFCOMPLEMENTO. Caso deseje exibir esse informe no novo leiaute, deverá regera-lo para que a tabela seja preenchida.

**Saiba mais:**  
[**Framework - Linha RM - Frame - TOTVS Compartilhamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8876331402775-Framework-Linha-RM-Frame-TOTVS-Compartilhamento)

[**DIRF/Informe de Rendimentos**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719351)

[**DT - Informe de Rendimentos - Usar Responsável da DIRF em Arquivo**](https://tdn.totvs.com.br/pages/releaseview.action?pageId=735439697)

[**DT - Informe de Rendimentos - API Skip to end of metadata**](https://tdn.totvs.com/display/public/LRM/DT+-+Informe+de+Rendimentos+-+API)
