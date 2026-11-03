---
article_id: 13519151002263
category: Gestão de Armazenagem (WMS)
content_hash: 457cb75544fa939dffc67c386ea3b7961c7e6e09767d5e93295e62f6f2609963
fetched_at: '2026-06-28T22:45:48.076578+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: 'Logística - Linha Protheus - WMS - Percentual de tolerância na separação de
  quantidades '
type: support-article
updated_at: '2023-03-31T18:51:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13519151002263-Log%C3%ADstica-Linha-Protheus-WMS-Percentual-de-toler%C3%A2ncia-na-separa%C3%A7%C3%A3o-de-quantidades
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como aplicar o Ponto de Entrada **WMSQMSEP** - Permite configurar um percentual de tolerância para a separação de quantidade superior a original do movimento?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (SIGAWMS) -  A partir da versão 12.  
  
**Solução**Este Ponto de Entrada permite configurar um percentual de tolerância para a separação de quantidade superior a original do movimento.  
Possui funcionalidade semelhante ao parâmetro **MV\_WMSQSEP**, porém, permite variar o percentual de tolerância de acordo com determinadas regras.  
  
Exemplo:  
Se estiver executando um serviço de expedição convencional, não permite que seja separada uma quantidade maior do que a original do movimento. Contudo, se for um serviço de requisição para produção, permite separar até o dobro da quantidade original da movimentação.  
Localizado na função que verifica a permissão para alterar as quantidades de separação.  
  
**Parâmetro**

![parametro.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13519351784471)

**Retorno**

![retorno.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13519412473367)

**Saiba mais**  
Todos os parâmetros são recebidos na ***User Function*** via **PARAMIXB**. Para mais informações verifique a documentação [Execblock / Customização](https://tdn.totvs.com/pages/releaseview.action?pageId=43550096).  
  
**Exemplo:**

------

**#INCLUDE "PROTHEUS.CH"**

**User Function WMSQMSEP()**  
**Local oMovimento := PARAMIXB[1]**  
**Local nPerToler := SuperGetMV('MV\_WMSQSEP',.F., 0 )**

**// Se for serviço de requisição para produção, considera tolerância de 100%**  
**// Caso contrário, mantém o valor configurado no parâmetro MV\_WMSQSEP**  
**If oMovimento:oOrdServ:GetServico() == "018"**  
**nPerToler := 100**  
**EndIf**

**Return nPerToler**

------
