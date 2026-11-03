---
article_id: 360025588954
category: Gestão de Transportes (TMS)
content_hash: 407559d6307268bb0995e649dfe892bbf248fd2cfe878a87db3d97351579b229
fetched_at: '2026-06-28T22:45:27.681143+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Emissão de CT-e
type: support-article
updated_at: '2025-10-31T11:26:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025588954-Log%C3%ADstica-Linha-Protheus-TMS-Emiss%C3%A3o-de-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Qual o fluxo básico para emissão de um **CT-e - Conhecimento de Transporte Eletrônico**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Com as parametrizações e cadastros básicos efetuados siga o seguinte fluxo de processo:

1. Acessar menu **Atualizações / Recebimento / Entrada Documentos de Clientes - TMSA050:**
2. Selecionar a opção **incluir**;
3. No campo **No.lote**utilize a tecla **F3** e inclua um novo lote;
   1. Na tela de inclusão do lote, defina a quantidade de **NF - Notas Fiscais** no campo **Qtd.Lote** e indique a emissão de um documento eletrônico com o campo **Tipo Lote** igual a **3 - Eletrônico** e salve a inclusão do lote;
4. Informe os campos abaixo referente as partes integrantes do documento. Somente o campo Remetente e Destinatário são obrigatórios. Os demais campos somente devem ser preenchidos caso o documento se enquadre neste cenário:
   * **Remetente -** Emissor da **NF** da mercadoria que será transportada;
   * **Destinatário -** Destinatário indicado na **NF**;
   * **Consignatário -**Deve ser utilizado quando há um responsável pelo pagamento de frete diferente das outras partes envolvidas;
   * **Despachante -** Deve ser utilizado quando outra empresa efetua parte do Transporte. Quando informado é necessário indicar informações do **CT-e** emitido por ele;
   * **Expedidor -** Utilizado quando a mercadoria não é retirada no **Remetente;**
   * **Recebedor -**Utilizado quando a mercadoria deve ser entregue em outra empresa.
5. Indicar no campo **Dev. Frete**qual dos envolvidos será o **Tomador**do frete;
6. Preencher os campos **Serv.Transp**, **Tipo transp.** e **Serviço**;
7. No campo **Selec.Origem** é necessário indicar qual será a origem do **CT-e**;
8. Após informar o cabeçalho, indique os dados do produto no *grid* e salve a digitação da **NF***.* As informações principais são:
   1. **Doc.cliente** **-**Informe o **número do documento** **do cliente**para Transporte;
   2. **Serie Dc.Cli -** Informe a **Série do Documento** **do Cliente**para Transporte;
   3. **Cod. Produto -**Informe o **Código do Produto da Nota Fiscal**;
   4. **Embalagem -**Selecione o **Tipo da Embalagem** que está sendo utilizada na Nota Fiscal;
   5. **Dt missão - Data de Emissão da Nota Fiscal** do Cliente;
   6. **Qtd. Volumes - Quantidade de Volumes** da Nota Fiscal do Cliente;
   7. **Peso - Peso da Nota Fiscal** do Cliente;
   8. **Valor -**Informe o **Valor da Nota Fiscal** do Cliente;
   9. **Cod. Fiscal -**Informe o **Código Fiscal de Operações e Prestações**;
   10. **Chave NF-e -** Informar a chave da **NF-e SEFAZ - Secretaria de Estado da Fazenda.**
9. Com o lote digitado, deve ser efetuado o **Cálculo do frete**. Este é o processo responsável pela geração do documento. É possível efetuá-lo de 3 formas:
   1. **Atualizações / Recebimento / Calculo de frete - TMSA200**Na tecla **F12** é possível parametrizar alguns comportamentos a serem adotados no momento do cálculo. Como por exemplo **Transmissão automática** e ***Preview* do frete.** Após definir estes parâmetros, pesquise o lote e efetue o cálculo;
   2. **Atualizações / Recebimento / Entrada Documentos de Clientes - TMSA050**  
      Posicionado sobre o lote desejado e entre em **Outras ações /** **Cálculo de Frete / Cálculo** e efetue o cálculo.
   3. Em ambas as rotinas citadas acima, existe a opção **Selecionar Lotes**, que permite calcular diversos lotes de uma única vez. Esta opção fica localizada em **Outras ações.**
10. **Transmissão manual.**  
    Pode ser efetua pelo cálculo de frete, ou pela entrada de documento por meio da opção **CT-e**localizada em **Outras ações.** Defina o filtro para encontrar o documento a ser transmitido. Ao confirmar a tela será apresentado o ***Browse -*** **TMSAE70**com os documentos filtrados. Selecione o documento para transmissão e clique em **Transmitir**. Após a aprovação, selecione a opção **DACTE** e efetue a impressão.

**Saiba mais:**[Logística - Linha Protheus - TMS - Principais parâmetros CT-e](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024942253-MP-SIGTATMS-Principais-par%C3%A2metros-CT-e?source=search)  
[Logística - Linha Protheus - TMS - Cadastros básicos para emissão de documento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024800734-MP-TMS-Cadastros-b%C3%A1sicos-para-emiss%C3%A3o-de-documento?source=search)
