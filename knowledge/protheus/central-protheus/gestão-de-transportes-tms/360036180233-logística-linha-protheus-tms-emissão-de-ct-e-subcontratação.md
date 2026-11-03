---
article_id: 360036180233
category: Gestão de Transportes (TMS)
content_hash: 522a24a2bc93be93dd9b060f3cc3ce4f6c0de78e9cc3495d83044bd6ab93d0c7
fetched_at: '2026-06-28T22:45:27.692506+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Emissão de CT-e - Subcontratação
type: support-article
updated_at: '2024-05-23T12:49:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036180233-Log%C3%ADstica-Linha-Protheus-TMS-Emiss%C3%A3o-de-CT-e-Subcontrata%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23687051165975)***Tempo aproximado para leitura: 00:04:00 min  
  
**Dúvida**Qual o fluxo básico para emissão de um **CT-e - Subcontratação**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Com as parametrizações e cadastros básicos efetuados siga o seguinte fluxo de processo:

* Acessar menu **Atualizações / Recebimento / Entrada Documentos de Clientes - TMSA050:**
* Selecionar a opção **incluir**;
* No campo **No.lote**utilize a tecla **F3** e inclua um novo lote;
* Na tela de inclusão do lote, defina a quantidade de **NF - Notas Fiscais** no campo **Qtd.Lote**e indique a emissão de um documento eletrônico com o campo **Tipo Lote=3 - Eletrônico**e salve a inclusão do lote**;**
  + **Remetente -** Emissor da **NF** da mercadoria que será transportada;
  + **Destinatário -**Destinatário indicado na **NF**;
  + **Consignatário -**Deve ser utilizado quando há um responsável pelo pagamento de frete diferente das outras partes envolvidas;
  + **Despachante -**Deve ser utilizado quando outra empresa efetua parte do Transporte. Quando informado é necessário indicar informações do**CT-e** emitido por ele;
  + **Expedidor -**Utilizado quando a mercadoria não é retirada no **Remetente;**
  + **Recebedor -**Utilizado quando a mercadoria deve ser entregue em outra empresa.
* Indicar no campo **Dev. Frete**qual dos envolvidos será o **Tomador**do frete. Na emissão de CT-e Subcontratação, o tomador do Serviço a ser informado será o **Consignatário**.
* Preencher os campos **Serv.Transp,****Tipo transp.** e **Serviço**;
* No campo **Tipo Nf Cli.** = **DTC\_TIPNFC**, selecionar a opção **2 - Subcontratação**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046544914)

* No campo **Selec.Origem** é necessário indicar qual será a origem do **CT-e**;
* Após informar o cabeçalho, indique os dados do produto no *grid* e salve a digitação da **NF***.*As informações principais são:
  + **Doc.cliente** **-**Informe o **Nº do documento** **do cliente**para Transporte;
  + **Serie Dc.Cli -** Informe a **Série do Documento** **do Cliente**para Transporte;
  + **Cod. Produto -**Informe o **Código do Produto da Nota Fiscal**;
  + **Embalagem -**Selecione o **Tipo da Embalagem** que está sendo utilizada na Nota Fiscal;
  + **Dt missão - Data de Emissão da Nota Fiscal** do Cliente;
  + **Qtd. Volumes - Quantidade de Volumes** da Nota Fiscal do Cliente;
  + **Peso - Peso da Nota Fiscal** do Cliente;
  + **Valor -**Informe o**Valor da Nota Fiscal** do Cliente;
  + **Cod. Fiscal -**Informe o **Código Fiscal de Operações e Prestações**;
  + **Chave Nf-e -**Informar a chave da **NFe SEFAZ - Secretaria de Estado da Fazenda;**
  + **Tp.Doc. Ant -** Informar o Tipo de Documento Anterior; Documento emitido pelo Tomador de Serviço;
  + **Dt.Doc. Ant -** Informar Data de Emissão do Documento Anterior;
  + **CTe.Doc. Ant -** Informar a Chave de Acesso do Documento Anterior.
* Com o lote digitado, deve ser efetuado o **Cálculo do frete**. Este é o processo responsável pela geração do documento. É possível efetuá-lo de 3 formas:
  + **Atualizações / Recebimento / Calculo de Frete - TMSA200**Na tecla **F12** é possível parametrizar alguns comportamentos a serem adotados no momento do cálculo. Como por exemplo **Transmissão automática** e **Preview do frete.** Após definir estes parâmetros, pesquise o lote e efetue o cálculo;
  + **Atualizações / Recebimento / Entrada Documentos de Clientes - TMSA050**  
    Posicionado sobre o lote desejado e entre em **Outras ações /** **Cálculo de Frete / Cálculo** e efetue o cálculo.
  + Em ambas as rotinas citadas acima, existe a opção **Selecionar Lotes**, que permite calcular diversos lotes de uma única vez. Esta opção fica localizada em **Outras ações.**
* **Transmissão manual.**  
  Pode ser efetua pelo cálculo de frete, ou pela entrada de documento através da opção **CT-e**localizada em **Outras ações.** Defina o filtro de para encontrar o documento a ser transmitido. Ao confirmar a tela será apresentado o **Browse** ***-*****TMSAE70**com os documentos filtrados. Selecione o documento para transmissão e clique em **Transmitir**. Após a aprovação, selecione a opção **DACTE** e efetue a impressão.

**Importante**Para a emissão de **CTe** Subcontratação, deve-se criar uma regra de Tributação por cliente no programa **TMSA600** onde o Tipo da **NFC** **DV1\_TIPNFC** seja igual a 2 - Subcontratação.   
  
**Saiba mais**Para dúvidas do processo, consulte a documentação informada a seguir:  
[Exemplo - Processo de Subcontratação (TMSA050 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=518465278)  
[Logística - Linha Protheus - TMS - Principais parâmetros CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024942253-MP-SIGTATMS-Principais-par%C3%A2metros-CT-e?source=search)  
[Logística - Linha Protheus - TMS - Cadastros básicos para emissão de documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024800734-MP-TMS-Cadastros-b%C3%A1sicos-para-emiss%C3%A3o-de-documento?source=search)
