---
article_id: 360025730994
category: NFe - Nota Fiscal Eletrônica
content_hash: e88e19d1925eb9f9f92e573c7ec1d3847655ff6b7db7345e16009ac0f20690b1
fetched_at: '2026-06-28T22:40:03.335384+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  923 Rejeição :
  Referenciado documento de operação interna em operação interestadual ou com o exterior'
type: support-article
updated_at: '2025-06-25T12:16:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025730994-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-923-Rejei%C3%A7%C3%A3o-Referenciado-documento-de-opera%C3%A7%C3%A3o-interna-em-opera%C3%A7%C3%A3o-interestadual-ou-com-o-exterior
---

**Dúvida**

Como solucionar a rejeição abaixo:

923 Rejeição : Referenciado documento de operação interna em operação interestadual ou com o exterior ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Se informado a TAG  **refECF** modelo 65 ***Espécie =***  NFCE/SATCE a espécie da nota de origem realmente for **NFCE** ou **SATCE** a **UF não** permite mais que seja referenciada a uma ***NF-e em operações interestaduais ou com o exterior;***

2. Verifique com a Sefaz se deve ser gerado apenas em ***informações complementares a chave.***  
  
Se sim utilize o campo ***C5\_MENNOTA (nota de saída)*** ou ***F1\_MENNOTA (nota de entrada).***

Preencher o campo ***Mens. p/ Nota***  ***F1\_MENNOTA*** no complemento do Danfe em  ***Informações complementares*** no documento de entrada na aba Nota Fiscal eletrônica.

![F1_MENNOTA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040985841303)

ou

Preencher o campo ***Mens. p/ Nota** **C5\_MENNOTA*** Campo de complemento do Danfe do campo **Informações complementares** é preenchido no Pedido de Venda. Observação : Os campos ***F2\_MENNOTA e C5\_MENNOTA*** devem conter o mesmo tamanho no configurador.

![C5_MENNOTA.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33041007759255)

3. Verificar se o **CFOP** da nota está correto sendo iniciado por **2, 6, 3 ou 7**, caso esteja a nota não pode ser referenciada **refNF=** Modelo 01, 01A, 02 Espécie = ***NF, NFe, NFA ou NFCF*** em operações interestaduais;

4.  Caso o **CFOP** esteja errado alterar no cadastro do TES no campo ***Cod. Fiscal e refazer a nota;***

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11706997516695)

5. Para notas de modelo 55 espécie SPED, Verificar se a nota foi **referenciada ao documento**correto:

**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)**

![referecia_nt_entrada.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11706956443671)

**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)**

![referecia_nt_saida.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11706953756183)

Se a mesma for referenciada manualmente deve se preencher os campos ***NF . Ori , Serie Ori e Item Ori .*** Se for preenchido automaticamente pelo gatilho ***F4 (Nota de saída) ou F7 (Nota entrada)*** os campos são alimentados automaticamente;

6. A nota original para que traga de forma correta no XML a **chave** deverá estar gravada de forma correta nas tabelas ***SF3, SFT, SF1 ou SF2 nos campos* F3\_CHVNFE, FT\_CHVNFE, F1\_CHVNFE ou F2\_CHVNFE.**

7. Se a nota for formulário próprio = Sim e tenha sido transmitida pela empresa, na rotina de transmissão de nota ir em ***Outra ações -> Monitor -> faixa ou Monitor -> Consulta NF*** para que seja preenchida a chave nas tabelas corretamente.

![Monitor_-_faixa_-_consulta_NF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33040985846295)

8. Se a nota de origem for de entrada com ***formulário próprio = Não*** verifique se a chave no campo ***F1\_CHVNFE foi digitada*** de forma correta validando a chave no portal da Sefaz.
