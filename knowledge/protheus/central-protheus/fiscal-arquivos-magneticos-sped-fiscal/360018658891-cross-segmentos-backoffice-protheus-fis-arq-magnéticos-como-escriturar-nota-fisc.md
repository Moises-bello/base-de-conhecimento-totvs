---
article_id: 360018658891
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 7a8a9a140617bd251859222ccd2f3b160dadd459d8acfec3db3437126862d0cd
fetched_at: '2026-06-28T22:42:00.904794+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como escriturar
  nota fiscal extemporânea.
type: support-article
updated_at: '2025-02-11T20:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018658891-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-escriturar-nota-fiscal-extempor%C3%A2nea
---

**Dúvida**Como escriturar Nota Fiscal Extemporânea?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**Escrituração de Documentos extemporâneos  
  
1. Escriture uma nota fiscal de entrada;

2. Realize complemento de nota fiscal pela rotina MATA910 selecionando a nota fiscal;  
Ações relacionadas/ Complementos / Informações complementares.

3. Preencha o campo Extemporânea (**CDT\_SITEXT**) = Ex Regular e Data recebimento (**CDT\_DTAREC**) = ? – Data do recebimento do documento;

4. Após confirmação verifique se na tabela **CDT** os campos **CDT\_SITEXT** = R, **CDT\_TPMOV** = E e **CDT\_CTAREC** = ? data recebimento, Tabela **SFT** campo **FT\_TIPOMOV** = E;  
5. Ao gerar o arquivo do SPEDFISCAL no Registro C100, o campo 06\_COD\_SIT será preenchido com:   
01 - Escrituração extemporânea de documento regular.  
ou  
07 - Escrituração extemporânea de documento complementar.
