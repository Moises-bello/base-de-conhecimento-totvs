---
article_id: 360027275412
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 4ba27bb14183ad85564630f21d497bda3587135260dc7cc75d75159c3f16dc55
fetched_at: '2026-06-28T22:40:44.727321+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD Registro I250 :
  CODIGO PARTICIPANTE'
type: support-article
updated_at: '2022-05-20T18:36:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027275412-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Registro-I250-CODIGO-PARTICIPANTE
---

**Dúvida**

Como gerar o Código de participante (COD\_PART) no registro I250 do arquivo da ECD  
   
 **Ambiente**

Microsiga Protheus  – Contabilidade  – A partir da versão 11.80  
  
**Solução**

* Através da rotina CTBA016 realize o cadastro do participante  : [MP - SIGACTB - ECD Registro 0150: Tabela de Cadastro do Participante como gerar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023383752-MP-SIGACTB-ECD-Registro-0150-Tabela-de-Cadastro-do-Participante-como-gerar-?source=search)
* Através da rotina de lançamento contábeis automáticos (CTBA102) Informe o " Cod.Partic" através do campo CT2\_CODPAR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027040271/mceclip2.png)

* Ao gerar o arquivo o sistema irá gerar o código no campo 09 (COD\_PART)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027040411/mceclip3.png)

Campo 01 – Tipo de Registro: I250  
Campo 02 – Código da Conta Analítica Debitada/Creditada: 11101002  
Campo 03 – Código do Centro de Custos: não há.  
Campo 04 – Valor da Partida: 2500,00 (corresponde a 2.500,00)  
Campo 05 – Indicador da Natureza da Partida: D (Débito)  
Campo 06 – Número, Código ou Caminho de Localização dos Documentos Arquivados: 120180101000001001000001001001D0119901  
Campo 07 – Código do Histórico Padronizado: não há.  
Campo 08 – Histórico Completo da Partida ou Histórico Complementar: RECEBIMENTO DE FORNECEDOR  
Campo 09 – Código de Identificação do Participante (Registro 0150): 03 (COD\_PART )
