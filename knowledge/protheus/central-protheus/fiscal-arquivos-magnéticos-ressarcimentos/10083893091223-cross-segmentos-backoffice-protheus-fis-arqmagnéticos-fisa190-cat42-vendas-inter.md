---
article_id: 10083893091223
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 2cb3cb259d96c8a4ef24ab39d9a73cf5f1b427f23e50853f41dc540aaa625856
fetched_at: '2026-06-28T22:42:12.718591+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - FISA190-CAT42-
  Vendas Internas destinadas à Consumidor Final.
type: support-article
updated_at: '2022-11-09T12:28:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10083893091223-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-FISA190-CAT42-Vendas-Internas-destinadas-%C3%A0-Consumidor-Final
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**

Qual a configuração Das Vendas Internas Destinadas a Consumidor Final - Enquadramento Legal 1?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

O código de **enquadramento 1**, dentro da **portaria CAT42,** é definido com base nas operações ensejadora de **Ressarcimento ou Complemento de ICMSST na hipótese do Inciso I do Art. 269 do RICMS** quando o valor do imposto retido à maior, correspondente à diferença entre o valor que serviu de base à retenção e o valor da operação ou prestação realizada com consumidor ou usuário final;

Para ser gerado o ressarcimento de **ICMS-ST (CAT42) nas operação com CFOP 5405**, é necessário  informar no **pedido de venda que o cliente é consumidor ou usuário final;**

Quando isso ocorrer deverão ser  alimentadas as seguintes tags:  **tag indFinal, Tag vBCSTRet,Tag pST,Tag vICMSSTRe no XML.**

Será necessário configurar o **parâmetro MV\_ULTAQUI**, para que as informações alimentada nas **Tag vBCSTRet,Tag pST,Tag vICMSSTRe sejam levadas para a tabela SFT nos seguintes campos FT\_BSTANT , FT\_PSTANT , FT\_VSTANT.**

Obs: Quando a aquisição for oriunda das operações provenientes do CST 60, é fundamental que os campos **D1\_ICMNDES, D1\_BASNDES e D1\_ALQNDES**, estejam preenchidos na tabela SD1.

Segue abaixo um demonstração da validações das **informações na rotina FISA190**, com base nas diretrizes determinadas pela **CAT42**.

1) - Carga de Saldo Inicial;

Para a utilização dessa opção, é necessário o **fechamento do estoque do período imediatamente anterior ao de ingresso no sistema de ressarcimento**, além do processamento do relatório **MATR460 - Registro de Inventário Modelo P7**.

![image2018-12-3_11-48-40.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10083161812503)

Ao utilizar a opção **Carregar Saldos Iniciais**, será solicitada a **data de fechamento do estoque.** Essa será a data de referência da rotina para a carga automática do saldo inicial dos produtos. A rotina também buscará informações resultantes do processamento do relatório acima citado, além de retroagir, a partir da data informada, nos movimentos de entrada, para a composição dos campos de valor.

![image2018-12-3_11-51-36.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10083184348567)

Obs: Caso apresente alguma duvida quanto a realização do **fechamento do estoque**, além do processamento do relatório **MATR460 - Registro de Inventário Modelo P7,**segue link contendo o roteiro com todos os passos.

<https://tdn.totvs.com/pages/releaseview.action?pageId=284352086>

2) - Configuração da Regra.

Dentro a **rotina FISA190, a Regra** possui a característica de **definir quais os CFOPS e CST** que serão considerados na composição do **cálculo de ressarcimento do ICMS-ST**.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10083001406231)

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10083286550679)

3) - Relatório.

Para fins de conferência dos valores apurados, é possível extrair, em formato de planilha, um relatório detalhando cada movimentação do produto no período selecionado.

![image2022-10-28_13-5-7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10083422307863)

Abaixo podemos observar um demonstrativo do relatório, contemplando as informações referente as vendas internas destinadas consumidor ou usuário final.

![inline-1647432813.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10083381416983)

4) Geração do Arquivo.

Rotina **FISA190** responsável pela geração do arquivo no formato texto, de acordo com Manual De Orientação da formação do Arquivo Digital Do Sistema de Apuração do Ressarcimento ou complemento Do ICMS Retido Por Substituição Tributaria ou Antecipado.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/10083601723543)

Abaixo podemos observar um demonstrativo do arquivo TXT gerado, contemplando as informações referente as vendas internas destinadas consumidor ou usuário final.

Podemos observar que no **registro 1200 campo 15 o enquadramento legal esta como 1**, e desta forma atendendo todos o requisitos  da **CAT42**.

![inline-78757420.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10083722546455)

Para facilitar todo o entendimento acima, segue abaixo link, contemplando vídeo demonstrando a funcionalidade da rotina **FISA190.**

<http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20221108/TTVFLGP1J001-1667911815419-236478.rar>

Para mais Informações, segue link referente a documentação da rotina **FISA190.**

<https://tdn.totvs.com/pages/releaseview.action?pageId=698292557#SPRESSTRessarcimentodeICMSSTdoEstadodeS%C3%A3oPaulo-Gera%C3%A7%C3%A3odoArquivo>
