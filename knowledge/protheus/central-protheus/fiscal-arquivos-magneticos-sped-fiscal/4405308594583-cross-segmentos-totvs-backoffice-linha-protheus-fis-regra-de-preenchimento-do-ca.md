---
article_id: 4405308594583
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 948cc3ffd8b6e4409597242e196564cedf4643d82fd27fce242bb0c2ebba1809
fetched_at: '2026-06-28T22:42:03.747111+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Regra de Preenchimento
  do campo 17_TIPO_FRT - nos registros C100 e D100 No SPEDFISCAL e EFD Contribuições
type: support-article
updated_at: '2021-07-30T16:04:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405308594583-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Regra-de-Preenchimento-do-campo-17-TIPO-FRT-nos-registros-C100-e-D100-No-SPEDFISCAL-e-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**

Regra Preenchimento do campo 17\_TIPO\_FRT - nos registros C100 e D100 No SPEDFISCAL e EFD Contribuições

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**

Configuração pra preenchimento do campo Campo 17\_TIPO\_FRT para geração dos registros C100 e D100 no SPEDFISCAL e EFD Contribuições.

**1- Documento de Entrada**

Deve ser configurado na aba de informações da DANFE

**Campo**

Tipo de Frete (F1\_TPFRETE) = C - CIF  - > "Por conta do emitente"

Registro C100 ou D100 campo 17\_TIPO\_FRT = 0 - Por conta do emitente

**OU**

Tipo de Frete (F1\_TPFRETE) = F - FOB  - > "Por conta do destinatário/remetente"

Registro C100 ou D100 campo 17\_TIPO\_FRT = 1 - Por conta do destinatário/remetente

**OU**

Tipo de Frete (F1\_TPFRETE) = T - Por conta terceiros - >“ “Por conta de terceiros;"

Registro C100 ou D100 campo 17\_TIPO\_FRT = 2- Por conta de terceiros

**OU**

Tipo de Frete (F1\_TPFRETE) = S - Sem Frete - >“Sem cobrança de frete"

Registro C100 ou D100 campo 17\_TIPO\_FRT = 9- Sem cobrança de frete

**2- Documento de Saída**

Deve ser preenchido no pedido de venda

**Campo**

Tipo de Frete (C5\_TPFRETE) = 1 - CIF - > "Por conta do emitente"

Registro C100 ou "D100 via modulo TMS" campo 17\_TIPO\_FRT = 0 - Por conta do emitente

**OU**

Tipo de Frete (C5\_TPFRETE) = F – FOB - >  "Por conta do destinatário/remetente"

Registro C100 ou "D100 via modulo TMS" campo 17\_TIPO\_FRT = 1 - Por conta do destinatário/remetente

**OU**

Tipo de Frete (C5\_TPFRETE) = T - Por conta terceiros - >“ "Por conta de terceiros;"

Registro C100 ou "D100 via modulo TMS” campo 17\_TIPO\_FRT = 2- Por conta de terceiros

**OU**

Tipo de Frete (C5\_TPFRETE) = S - Sem Frete - > "Sem cobrança de frete"

Registro C100 ou "D100 via modulo TMS" campo 17\_TIPO\_FRT = 9- Sem cobrança de frete

**3- Complemento da Nota (Tabela CDT)**

Quando possui informações Complementares na CDT onde o campo CDT\_INDFRT estiver preenchido será considerado o Frete informado no Complemento.

*OBS: O campo CDT\_INDFRT no padrão do Protheus é inicializado como 'Branco' e permite Salva os Complemento com o mesmo em Branco.*

Tipo de Frete (CDT\_INDFRT) = "1" - Por conta do emitente

Registro C100 campo 17\_TIPO\_FRT = 0

**OU**

Tipo de Frete (CDT\_INDFRT) = "2" - Por conta do destinatário/remetente

Registro C100 campo 17\_TIPO\_FRT = 1

**OU**

Tipo de Frete (CDT\_INDFRT) = "0" - Por conta de terceiros

Registro C100 campo 17\_TIPO\_FRT = 2

**OU**

Tipo de Frete (CDT\_INDFRT) = "3" - Por conta remetente \*\*(somente para versão 012)

Registro C100 campo 17\_TIPO\_FRT = 3

**OU**

Tipo de Frete (CDT\_INDFRT) = "4" - Por conta destinatário \*\*(somente para versão 012)

Registro C100 campo 17\_TIPO\_FRT = 4

**Importante**

Qual é a diferença entre frete CIF e frete FOB, ou até mesmo o que seria um e outro:

CIF - O remetente se responsabiliza pelo pagamento do imposto quando a operação for contratada sob a cláusula CIF - neste caso o estabelecimento vendedor (remetente) responde pelo transporte da mercadoria até o estabelecimento destinatário, mediante contratação do serviço de transporte;

FOB - Destinatário se responsabiliza pelo pagamento do imposto quando a operação for contratada sob a cláusula FOB - caso em que o estabelecimento comprador (destinatário) assume a responsabilidade pela retirada da mercadoria adquirida, mediante contratação do serviço de transporte.

**Atenção**

**No Guia prático EFD ICMS/IPI e no Guia prático EFD Contribuições – C100**

Campo 17\_TIPO\_FRT do registro C100

Obs: A partir de 01/01/2018 passará a ser:

0 - Contratação do Frete por conta do Remetente (CIF);

1 - Contratação do Frete por conta do Destinatário (FOB);

2 - Contratação do Frete por conta de Terceiros;

3 - Transporte Próprio por conta do Remetente;

4 - Transporte Próprio por conta do Destinatário;

9 - Sem Ocorrência de Transporte

**No Guia prático EFD ICMS/IPI e no Guia prático EFD contribuições – D100**

Campo 17\_TIPO\_FRT do registro D100

Obs.: A partir de 01/07/2012 passará a ser:

Indicador do tipo do frete:

0- Por conta do emitente;

1- Por conta do destinatário/remetente;

2- Por conta de terceiros;

9- Sem cobrança de frete.

Documentação Técnica:

<https://tdn.totvs.com/pages/releaseview.action?pageId=243653535>
