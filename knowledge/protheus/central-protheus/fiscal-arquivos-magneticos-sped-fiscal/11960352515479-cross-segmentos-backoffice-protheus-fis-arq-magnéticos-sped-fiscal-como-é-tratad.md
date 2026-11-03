---
article_id: 11960352515479
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: c1f1ce826b298deca0c7f9b1a27a468e627d1174f42c58ffc8868ed33fc9e1ae
fetched_at: '2026-06-28T22:42:01.008742+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL  -
  Como é tratada a informação do Nome Fantasia no campo 02 do registro 0005 no Sped
  Fiscal?
type: support-article
updated_at: '2023-02-01T12:49:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11960352515479-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-%C3%A9-tratada-a-informa%C3%A7%C3%A3o-do-Nome-Fantasia-no-campo-02-do-registro-0005-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ambiente**

**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão 12.1.25**

**Ocorrência**

O **campo 02** do **registro 0005** no Sped Fiscal está apresentando com o nome incorreto, o que fazer?

**Solução**

Verifique o conteúdo do campo **M0\_CODFIL**, se ele for 1 ou 2 ele irá pegar o nome do conteúdo do campo **M0\_FILIAL**.

Se o conteúdo do campo **M0\_CODFIL** for maior que 2 ele irá pegar do **M0\_NOME**.

O sistema valida o tamanho do campo **M0\_CODFIL**:

se for >2 valida o parâmetro **MV\_USAXX8** e se estiver = .F. pega do **M0\_FILIAL**  
se for <2 busca do **M0\_NOME**  
  
Diferente disso somente com o ponto de entrada **SPEDFANT**, segue documentação:  
  
<https://tdn.totvs.com/display/public/PROT/SPEDFANT+-+Alterar+Nome+Fantasia+do+SPEDFISCAL>
