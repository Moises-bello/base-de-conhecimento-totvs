---
article_id: 360018825292
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9a5b0d64fb8179eca95a67b81a03ddad011ca3f46aba7d3f846f63b5e5dc6dac
fetched_at: '2026-06-28T22:42:03.676322+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice Linha Protheus - Arq. Magnéticos - Notas
  Inutilizadas Sendo Carregadas Para o SPED Fiscal ou Contribuições Como Canceladas
type: support-article
updated_at: '2026-05-15T20:22:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018825292-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Arq-Magn%C3%A9ticos-Notas-Inutilizadas-Sendo-Carregadas-Para-o-SPED-Fiscal-ou-Contribui%C3%A7%C3%B5es-Como-Canceladas
---

**Dúvida**As notas fiscais inutilizadas estão sendo levadas para o arquivo SPED Fiscal ou SPED Contribuições com o campo **COD\_SIT** = **02 (Documento Cancelado)** ao invés de levar como **05 (NF-e ou CT-e - Numeração inutilizada)**.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**A solução deste incidente, é a validação dos fontes **FISA008** e **SPEDFISCAL**, onde a NF Inutilizada deve estar com os campos devidamente preenchidos, com o seguinte conteúdo:  
  
Tabela SF3:  
  
**F3\_OBSERV**= NF CANCELADA ou NF INUTILIZADA;  
**F3\_DTCANC** = Data de Inutilização da nota;   
**F3\_CODRSEF** = 102 (102 = Inutilização de NF-e);  
**F3\_CHVNFE** = Não existe Chave NF-e.  
  
Tabela SFT :  
  
**FT\_OBSERV** = NF CANCELADA ou NF INUTILIZADA;  
**FT\_DTCANC**= Data de Inutilização da nota;  
**FT\_CHVNFE** = Não existe Chave NF-e.

Importante: Após a conferência dos campos, deverá ser gerado um novo arquivo magnético.

Abaixo lista de códigos de Situação do Documento conforme tabela 4.1.2:

**Código Descrição**  
00        Documento regular  
01        Escrituração extemporânea de documento regular  
02        Documento cancelado  
03        Escrituração extemporânea de documento cancelado  
04        NF-e ou CT-e – denegado  
05        NF-e ou CT-e - Numeração inutilizada  
06        Documento Fiscal Complementar  
07        Escrituração extemporânea de documento complementar  
08        Documento Fiscal emitido com base em Regime Especial ou Norma Específica
