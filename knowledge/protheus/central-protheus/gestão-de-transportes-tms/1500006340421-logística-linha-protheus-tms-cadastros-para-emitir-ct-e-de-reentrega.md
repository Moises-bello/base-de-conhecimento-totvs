---
article_id: 1500006340421
category: Gestão de Transportes (TMS)
content_hash: 8f8101a1c78795299505392e0912689d291b90db55dc9e336d3f3bffaccdc046
fetched_at: '2026-06-28T22:45:27.337112+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros para emitir CT-e de Reentrega
type: support-article
updated_at: '2023-09-27T19:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006340421-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-para-emitir-CT-e-de-Reentrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Como gerar um **CT-e - Conhecimento de Transporte Eletrônico** do tipo **Reentrega**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Documento gerado a partir de um **CT-e** original que caracteriza a reentrega de uma mercadoria ao seu remetente.  
  
**Cadastros necessários:**

* **Tabela de Ocorrência**Acesse a rotina no menu **Atualizações/Ocorrências/Tabela de Ocorrências - TMSA020**É necessário cadastrar uma ocorrência conforme o exemplo a seguir e depois relacionar o código no parâmetro **MV\_OCORREE**.  
  O campo **Tipo da Ocorrência - DT2\_TIPOCO** deve ser **04-Retorna Documento** e o **Responsável** - **DT2\_RESOCO** pela ocorrência **2=Cliente**, conforme demonstra o exemplo a seguir.

![imagem01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009034441/imagem01.png)

* **Rotina Configuração de Documentos**   
  Acesse a rotina **Atualizações/Doctos e Regras/Config. documentos - TMSA150**  
  Para a rotina de **Reentrega**, é necessário cadastrar um documento de **Reentrega**, **CTRC** ou **Nota-Fiscal**, de acordo com a operação. No exemplo a seguir cadastramos um **CTRC** **Reentrega**, **DUI\_DOCTMS = 7**.

![imagem02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009034581/imagem02.png)

* **Regra de Tributação**   
  Acesse a rotina **Atualizações/Doctos e Regras/Regras Tributação - TMSA410**Conforme exemplo a seguir, vamos cadastrar uma regra de tributação, que será relacionado posteriormente no cadastro **Regra de Tributação por Cliente**.

![imagem03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009034721/imagem03.png)

* **Regra de Tributação por Cliente**   
  Acesse a rotina **Atualizações/Doctos e Regras/Regras Por Cliente - TMSA600**No exemplo a seguir, vamos relacionar o **CTRC Reentrega**, a **Regra de Tributação 01**, cadastrada anteriormente. Em nosso exemplo relacionamos esta regra ao **Cliente Genérico -** **MV\_CLIGEN**. Esta rotina, entre outras, nos dá esta facilidade, para evitar cadastrar a mesma regra a vários clientes, podemos cadastrar apenas uma regra para o **Cliente Genérico**.

![imagem04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009034801/imagem04.png)

* **Rotina Manutenção Doctos**   
  Acesse a rotina **Atualizações/Transporte/Manutenção de Documento - TMSA500**  
  Clique em **Outras Ações / Reentrega**

![imagem05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008759982/imagem05.png)

Clique em **Outras Opções / Reentre**.

![imagem06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008760042/imagem06.png)

Ao executar a opção **Reentrega**, será exibida ao usuário uma mensagem, solicitando a definição de como será calculado o valor da reentrega, ou seja, se o valor será calculado automaticamente ou digitado.

* Se o usuário escolher a opção **Calculado**, o Sistema selecionará os dados informados no **Perfil do Cliente** **- TMSA480** para a geração do documento de cobrança da reentrega.
* Se o usuário escolher a opção **Digitado**, o Sistema permitirá que seja informado um percentual ou valor fixo a ser cobrado pela reentrega.

![imagem07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008760122/imagem07.png)

![imagem08.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009035161/imagem08.png)

![imagem09.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008760142/imagem09.png)  
![imagem10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009035201/imagem10.png)

Verificar os parâmetros:

* **MV\_OCORREE - Código das ocorrências que geram Reentrega.**
* **MV\_COMPENT - Código do Componente de frete para a reentrega que será apresentado na composição do frete.**
* **MV\_OBSREEN - Observação do documento de Reentrega.**
* **MV\_TPDCREE - Quais os tipos de documentos de origem do TMS que Reentrega. 2 = CTRC e 5 = Nota Fiscal.**
* **​MV\_TMSUNFS - Informe se a filial utiliza nota fiscal ou Conhecimento para Documentos de Armazenagem, Reentrega e Refaturamento.**
* **MV\_DOCREE - Documento de reentrega na viagem.**
