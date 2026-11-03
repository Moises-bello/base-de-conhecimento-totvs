---
article_id: 360047562333
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 2f9f3f18ed29eaea6eb58eb9be29b0069c3759dd72062376e4101369e22b678a
fetched_at: '2026-06-28T22:40:44.370666+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB ECD/ECF CARÁCTER ESPECIAL
  NO HISTÓRICO
type: support-article
updated_at: '2025-05-02T20:03:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047562333-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-ECF-CAR%C3%81CTER-ESPECIAL-NO-HIST%C3%93RICO
---

**Dúvida**

Históricos dos lançamento que serão gerado para ECD ou ECF podem ter carácter especial ?  
  
**Ambiente**

Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

Caso exista um "***| "*** e o Espaço em branco em no histórico do lançamento o validador pode apresenta erros de validação

Ex: [ECD I250 O REGISTRO LIDO TEM QUANTIDADE DE CAMPOS DIFERENTE DO ESPECIFICADO NO LAYOUT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047283673-MP-SIGACTB-ECD-I250-O-REGISTRO-LIDO-TEM-QUANTIDADE-DE-CAMPOS-DIFERENTE-DO-ESPECIFICADO-NO-LAYOUT?source=search)

Erro apresentado no validador esta sendo ocasionado devido algum conteúdo no histórico do lançamento contábil "algum carácter especial" ,"/","%", "Espaço em branco" ,"-" , ":".

Para corrigir o erro acesse a rotina de Lançamento Contábil (CTBA102) :

* Selecionei o lançamento contábil e altere
* Exclua do campo CT2\_HIST o carácter especial ou o Espaço

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31832999449879)

Cadastro do histórico padrão ( CTBA070) - o histórico também deve ser avaliado  
  
![](https://totvssuporte.zendesk.com/attachments/token/ZNovR57WpK5yLKJ3KJtzkyMBz/?name=inline872900570.png)

Em caso de duvidas verifique regras descritas no manual da receita

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31832999453335)

Saiba mais:

[ECD0039\_USO\_DE\_HISTORICOS\_PADRONIZADOS\_NA\_ECD\_REGISTRO\_I075](https://tdn.totvs.com/pages/releaseview.action?pageId=619765270)

<http://tdn.totvs.com/display/tec/AllTrim>  
<http://tdn.totvs.com/pages/viewpage.action?pageId=23889114>
