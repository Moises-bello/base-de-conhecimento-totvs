---
content_hash: 538f09d55e7b7ed307f1637f6abe10777d15f35a6078f42fa52c380eb1596db3
fetched_at: '2026-06-29T00:09:55.698310+00:00'
page_id: '450142789'
product: rm
source: tdn-rm
title: Parametrizar CT-e/CT-e OS para Anulação e Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450142789
version: 33
---

As informações descritas neste documento são válidas tanto para Conhecimento de Transporte Eletrônico (CT-e) quanto Conhecimento de Transporte Eletrônico - Outros Serviços (CT-e OS).  
São processos distintos por movimentos no sistema e são realizados via 'Cópia por Referência', onde os motivos de referência são:

* **'16- Conhecimento Transporte Eletrônico (CT-e) – Anulação'**
* **'17 - Conhecimento Transporte Eletrônico (CT-e) – Substituição'**

Lembrando que somente pode ser selecionado um Motivo de Referência por Tipo de Movimento.

**Parâmetros**

**Anulação - Tipo 1.2.XX**

Para a correta emissão de um Movimento de Anulação, o mesmo deve obedecer à seguinte parametrização:

* **Etapa 1 - Movimento - Identificação**
  + Edita Numeração: Edita;
  + Série: Edita ou Mostra.
* **Etapa 2 - Movimento - Emitente e Destinatário 1/2**
  + Emitente: Empresa;
  + Destinatário: Empresa.
* **Etapa 4 - Movimento - Datas**
  + Data de Emissão: Edita.
* **Etapa 6 - Movimento - Outros Dados**
  + Usar Cópia de Movimentos por Referência: Habilitado;
  + Motivo de Referência: 16 - Conhecimento Transporte Eletrônico (CT-e) - Anulação.
* **Etapa 18 - Movimento - Transporte 1/3**
  + Editar Espécie: Habilitado;
  + Editar Quantidade: Habilitado.
* **Etapa 19 - Movimento - Transporte 2/3**
  + Tipo de Frete (CIF / FOB / Terceiros): Edita;
  + Editar Dados de Cálculo do Frete da Mercadoria: Habilitado.
* **Etapa 26 - Item - Identificação 1/2**
  + Tipos dos Itens: Ambos.
* **Etapa 60 - Fiscal - Natureza**
  + Natureza: Edita;
  + Seleção Automática da Natureza: Seleciona por Movimento;
  + Edita Cliente/Fornecedor Origem/Destino: Habilitado.
* **Etapa 62 - Fiscal - Escrituração Fiscal 1/2**
  + Gerar Escrituração: Habilitado;
  + Tipo de Documento Escrituração: 57 (*Este valor deve estar preenchido no campo "Código do Modelo do Documento", que está localizado no cadastro do Tipo de Documento escolhido)*.
* **Etapa 68 - Fiscal - Conhecimento de Transporte**
  + Tipo de Operação do Conhecimento de Transporte: Emitir CT-e;
  + Modal: Rodoviário (pode variar de acordo com o contexto).

**Substituição - Tipo 2.2.XX**

Apenas alguns parâmetros diferem do Movimento de Anulação, que são:

* **Etapa 2 - Movimento - Emitente e Destinatário 1/2**
  + Emitente: Empresa;
  + Destinatário: Cliente.
* **Etapa 6 - Movimento - Outros Dados**
  + Usar Cópia de Movimentos por Referência: Habilitado;
  + Motivo de Referência: 17 - Conhecimento Transporte Eletrônico (CT-e) - Substituição.
* **Etapa 60 - Fiscal - Natureza**
  + Edita Cliente/Fornecedor Origem/Destino: Desabilitado.

**Procedimentos**

**Tomador NÃO Contribuinte de ICMS**

1. 1. O tomador deverá emitir uma declaração informando o número e a data de emissão do CT-e inconsistente, assim como o motivo da inconsistência.
   2. De posse deste documento, a empresa transportadora cria um movimento de CT-e do tipo Anulação através de cópia por referência (motivo 16) do movimento de **CT-e Original** que foi emitido com erro**.**
      1. No menu Processos, deve-se executar o "Assistente de Cópia por Referência".
      2. Na aba Transporte | Identificação, o campo Tipo de CT-e deverá estar preenchido com o valor 'Anulação'.
   3. Transmitir o CT-e de Anulação para a SEFAZ origem.
   4. A empresa transportadora cria um movimento de CT-e do tipo Substituto, através de cópia por referência (motivo 17) do movimento de **CT-e de Anulação** citado no item anterior.
      1. Executar o mesmo assistente referenciado no item 'b.i'.
      2. Na aba Transporte | Identificação, o campo Tipo de CT-e deverá estar preenchido com o valor 'Substituto'.
   5. Transmitir o CT-e de Substituição para a SEFAZ origem.

**Tomador Contribuinte de ICMS**

**Primeira forma**

1. 1. O tomador deverá registrar o evento de "Prestação de Serviço em Desacordo", justificando o porquê do serviço executado não ter sido como o acordado.
      1. No cadastro de Filiais, abrir o anexo "Prestações em Desacordo (CT-e / CT-e OS)".
         1. Preencher a Chave de Acesso do CT-e em questão e também a Justificativa do evento.
         2. Realizar o Envio e Consulta do registro incluído, através do menu de Processos deste Anexo.
   2. Somente após a autorização do evento citado no item 'a', a empresa transportadora cria um movimento de CT-e do tipo Anulação através de cópia por referência (motivo 16) do movimento de **CT-e Original** que foi emitido com erro**.**
      1. No menu Processos, deve-se executar o "Assistente de Cópia por Referência".
      2. Na aba Transporte | Identificação, o campo Tipo de CT-e deverá estar preenchido com o valor 'Anulação'.
   3. Transmitir o CT-e de Anulação para a SEFAZ origem.
   4. A empresa transportadora cria um movimento de CT-e do tipo Substituto, através de cópia por referência (motivo 17) do movimento de **CT-e de Anulação** citado no item anterior.
      1. Executar o mesmo assistente referenciado no item 'b.i'.
      2. Na aba Transporte | Identificação, o campo Tipo de CT-e deverá estar preenchido com o valor 'Substituto'.
   5. Transmitir o CT-e de Substituição para a SEFAZ origem.

**Segunda forma**

1. 1. O tomador deverá emitir um documento com valor fiscal, cujo Código do Modelo do Documento represente uma NF-e (55), CT-e (57) ou NF de papel (01 ou 04), que servirá como confirmação da anulação à ser realizada.
   2. Somente após a emissão do documento, a empresa transportadora cria um movimento de CT-e do tipo Substituição através de cópia por referência (motivo 17) do movimento de **CT-e Original** que foi emitido com erro**.**
      1. No menu Processos, deve-se executar o "Assistente de Cópia por Referência".
      2. Na aba Transporte | Identificação, o campo Tipo de CT-e deverá estar preenchido com o valor 'Substituto'.
      3. Na aba CTRC Saída | CTRC, deve-se associar o(s) documento(s) citado no item 'a', cujo Tipo de Vínculo seja 'Documento Anulação - Contribuinte ICMS'.

Segue abaixo um fluxograma para melhor entendimento.
