---
article_id: 360014263931
category: RH - GPS (Guia da Previdência Social)
content_hash: 577f4f729ac9ca6b5654642182ff5546e3bd747be1071c1592666bca262d4091
fetched_at: '2026-06-28T22:43:11.622891+00:00'
product: protheus
section_id: 360011996273
source: central-protheus
title: RH - Linha Protheus - GPE - Outras entidades não estão sendo geradas na guia
  GPS
type: support-article
updated_at: '2025-06-25T21:46:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014263931-RH-Linha-Protheus-GPE-Outras-entidades-n%C3%A3o-est%C3%A3o-sendo-geradas-na-guia-GPS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33057790972183) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida  
GPER240-** Outras entidades não estão sendo geradas na guia GPS - Guia da Previdência Social  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 11.80  
  
**Solução**>Cadastro verba 816 - Terceiros:  
![](https://totvssuporte.zendesk.com/attachments/token/DDIxAQ5QUZOtZ76dCNcQP8DxC/?name=inline909175023.png)  
![](https://totvssuporte.zendesk.com/attachments/token/SbX1VCvqgHvRZrKkjFx2cgxKA/?name=inline-1572696968.png)  
  
**Tabela S038:**O sistema buscará as informações do campo **%terceiros** para carregar os dados na **GPS**, porém, se os demais campos estiverem preenchidos o sistema fará a seguinte regra de cálculo para chegar na alíquota:  
 **%tercerios 5,8 - %senai 1,00 - %sesi 1,00 - %senac 1,00= 2,80%, pois entende-se que 2,80% é** o valor que será recolhido e pago pela empresa.  
Se o cliente manter o campo **%terceiros** em branco e preencher os demais, entende-se que o recolhimento do percentual informado será pago diretamente na entidade, ou seja, será recolhido na folha de pagamento e apresentado no **GPER040** mas não será apresentado na guia GPS emitida pelo sistema.  
O cliente também tem a opção de informar apenas o campo %terceiros que englobará o total da soma de todos os demais campos, com isto o sistema apresentará o conteúdo no **GPER040** e na guia de GPS para recolhimento.  
  
![](https://totvssuporte.zendesk.com/attachments/token/ipSZ9vqF7KJkpjJFBNHVFimjS/?name=inline-1083443173.png)  
  
**Cálculo da folha:**  
>Alimentou as informações da verba 816- Terceiros na tabela SRC.  
![](https://totvssuporte.zendesk.com/attachments/token/pg9YGSCg73JtNZq6LyhPSxFfV/?name=inline1667294670.png)  
Soma das verbas 816- Terceiros, para a totalização do valor apresentado na guia da GPS:  
37,42 + 318,86 + 20,48 + 688,79 + 20,67 + 239,27 + 98= 1.423,49.  
  
>Alimentou as informações da verba 816- Terceiros na tabela SRZ.  
![](https://totvssuporte.zendesk.com/attachments/token/vRJMk3jL1a7N40nFJZdAp0pnE/?name=inline-374810387.png)

Fonte **GPER240**:  
If !fGeraFolSRZ(cTipo,aTpc,cMesAnoGuia, aPerAberto, aPerFechado)  
      Return()  
  
**Resumo da Folha:**  
![](https://totvssuporte.zendesk.com/attachments/token/6HefT6PDrsagB86NZdp6pkIB3/?name=inline783077000.png)  
  
Parâmetros de impressão GPS:  
![](https://totvssuporte.zendesk.com/attachments/token/BqU5musndLCEpp6ruWAwW2SSl/?name=inline881335624.png)  
![](https://totvssuporte.zendesk.com/attachments/token/t9JVXOf6thRn4I1GsEG1NTbAh/?name=inline-603015009.png)  
![](https://totvssuporte.zendesk.com/attachments/token/rBuXBep83Bmj2R7fDT8bujS63/?name=inline-1942124329.png)  
  
GPS - Guia da Previdência Social:  
![](https://totvssuporte.zendesk.com/attachments/token/vzsSTTRPRtPE0IW5HCZZgQ7v2/?name=inline1151758179.png)  
  
Conferência GPS:  
Conforme o resumo da folha.  
6- Valor INSS: 9.288,09 (verba 815)  + 232,20 (verba 817) + 1.661,78 (verba 930) + 530,13 (verba 931) + 93,29 (verba 932) = 11.805,49.  
  
9- Valor do INSS: 1.423,49 (verba 816).  
  
**Saiba mais**  
Para adquirir informações adicionais, acesse o *link:*[MP- GPE0840 - GPER240- Outras entidades não estão sendo geradas na guia GPS](http://tdn.totvs.com/pages/viewpage.action?pageId=382536056)
