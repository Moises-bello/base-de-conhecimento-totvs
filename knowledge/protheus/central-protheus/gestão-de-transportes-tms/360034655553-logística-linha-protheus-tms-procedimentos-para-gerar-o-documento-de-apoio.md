---
article_id: 360034655553
category: Gestão de Transportes (TMS)
content_hash: b188c2b041bc8a01e29fc526bca49357a25604270a7dfb1c90eb15ca96da712a
fetched_at: '2026-06-28T22:45:32.495853+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Procedimentos para gerar o Documento de
  Apoio
type: support-article
updated_at: '2026-06-12T18:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034655553-Log%C3%ADstica-Linha-Protheus-TMS-Procedimentos-para-gerar-o-Documento-de-Apoio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23702083600663)** Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Quais os procedimentos para gerar o **Documento de Apoio**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**  
Segue abaixo os procedimentos para emissão de **Documento de Apoio** pelo módulo **SIGATMS**:

* **Atualizações/ Cadastros/ Produto - MATA010:**Cadastrar um produto de cálculo. Este produto de cálculo será associado no cadastro a seguir no campo **Cod.Produto - DUI\_CODPRO**. Este produto de cálculo é utilizado para cálculo dos impostos e escriturado nos Livros Fiscais. Ele será gravado nos registros da tabela SD2, campo **D2\_COD**.
* **Atualizações/ Doctos e Regras/ Configuração de Documentos - TMSA150:**No campo **Docto. Transp** **DUI\_DOCTMS**, informar B-ACT, C-Apoio 2, H-Apoio 3, I-Apoio 4, N-Apoio 5 ou O-Apoio 6. Todos estes tipos de documentos são considerados como documentos de apoio. Informar a serie e produto de cálculo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41180653868567)

* Através do **Configurador - SIGACFG/ Base de dados/ Dicionário/ Base de dados/ Tabelas Genéricas/L4**, que pertence a tabela **SX5**, cadastrar o **Tipo de Serviço**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044158374)

* **Atualizações/ Serviços/ Serviços x Tarefas - DLGA070:**Cadastrar um **Serviços x Tarefas** de categoria **Negociação**, e no campo **Docto. Transp - DC5\_DOCTMS**, informar o mesmo tipo de documento de apoio que foi cadastrado na **Configuração de Documentos:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045020953)

* **Atualizações/ Comercial/ Contrato Cliente - TECA250:**Relacionar o **Serviços x Tarefas** cadastrado anteriormente ao Contrato do Cliente tomador do serviço ou ao cliente genérico - **MV\_CLIGEN:**

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41180700542487)
* **Atualizações/ Comercial/ Perfil do Cliente - TMSA480**: Configurar o **Perfil do Cliente**, a aba **Financeiro**, informando principalmente os campos **Base Fatura.** e **Tipo Fatura** conforme desejada. É com base nessas informações que será possível gerar a fatura dos documentos de apoio:

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41180700542999)
* **Atualizações/ Cadastros/ Tipos de Entrada e Saída - MATA080**: Cadastrar um **TES**conforme regras fiscais de sua operação;
* **Atualizações/ Doctos e Regras/ Regras de Tributação - TMSA410:** Criar uma **Regra de tributação** para o **TES** criado anteriormente;
* **Atualizações/ Doctos e Regras/ Regras de Tributação por Cliente - TMSA600:** Criar uma **Regra por cliente** para o tipo de documento de transporte de apoio cadastrado na **Configuração de Documentos.** Esta regra pode ser para o cliente tomador de serviço ou para o cliente genérico - **MV\_CLIGEN.**

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41180700545559)

Após efetuar os cadastros acima, incluir o documento do cliente na rotina **Entrada de Documentos do Cliente - TMSA050** utilizando Lotes do tipo **Normal - DTP\_TIPLOT = 1** einformando o Serviço de Negociação cadastrado. Assim que o Serviço for informado, o campo **Docto. Transp** ficará com tipo do documento de apoio.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044168274)

Ao calcular e gerar o documento de apoio, ele estará apto para ser utilizado em viagens e para gerar faturas via **Fatura por Documento - TMSA850**.  
  
**Documentos de Apoio** não possuem valor fiscal. Para escriturar nos Livros Fiscais, devemos executar a rotina de **Fatura automática - TMSA491** de Documentos de Apoio. Esta rotina permite faturar e agrupar os documentos de apoio, convertendo-os em um documento fiscal, podendo ser um CTe ou uma Nota Fiscal de Serviço. Para utilizar este recurso, no cadastro de **Configuração de Documentos - TMSA150,** no campo **Docto.Fatura** **- DUI\_DOCFAT** informar 2 para gerar CTe ou 5 para gerar Nota Fiscal de Serviço:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41180700546455)

Para gerar a fatura automática dos documentos de apoio e transformá-los em **CTe** ou **Nota Fiscal de Serviço**, basta executar a rotina **Fatura Automática - TMSA491**.  
  
**Saiba mais**  
Mais informações de como utilizar a rotina **Fatura automática TMSA491 de Documentos de Apoio** acesse o *link*: [Fatura de Documentos do Tipo Apoio.](https://tdn.totvs.com/pages/releaseview.action?pageId=499356855)  
  
**Glossário**  
**CTe** - Conhecimento de Transporte Eletrônico  
**SIGATMS** - Gestão de Transportes  
**TES** - Tipo de Entrada e Saída
