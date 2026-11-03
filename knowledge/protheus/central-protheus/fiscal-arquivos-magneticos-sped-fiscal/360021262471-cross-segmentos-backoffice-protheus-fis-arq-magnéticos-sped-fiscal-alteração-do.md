---
article_id: 360021262471
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ef232ae54b4f72c3bbb0b7cb5236ac7d051fba3b8923f28fe3d7bfef2632f9c9
fetched_at: '2026-06-28T22:42:01.030140+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Alteração do campo CDL_INDDOC para o correto preenchimento da DU-E.
type: support-article
updated_at: '2025-02-11T20:12:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021262471-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Altera%C3%A7%C3%A3o-do-campo-CDL-INDDOC-para-o-correto-preenchimento-da-DU-E
---

**Ocorrência**O campo Declaração Única de Importação (**DUE**) não está habilitado dentro do complemento fiscal.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.17.  
 **Causa**  
Esse incidente ocorre, pois a opção "2-Declaração Única de Exportação" no campo **CDL\_INDDOC** não está disponível.  
   
**Solução**Para correção do incidente, será necessário a aplicação do dicionário de dados contido no pacote.   
  
*Atenção: Para a versão 012 do guia prático da EFD ICMS/IPI é necessário que o UPDDISTR tenha sido executado com os dicionários da patch abaixo.* *[Protheus 12.1.17 - PACOTE DE ATUALIZAÇÃO  
Protheus 12.1.16 - PACOTE DE ATUALIZAÇÃO  
Protheus 11.80 - PACOTE DE ATUALIZAÇÃO](https://suporte.totvs.com/portal/p/10098/download?e=663833)*Realize o download do pacote, e salve o diferencial de dicionário **SDFBRA** na pasta system. Depois, execute o compatibilizador **UPDDISTR** para criação da opção conforme abaixo:  
  
![](http://tdn.totvs.com/download/attachments/378277294/image2018-6-26_13-53-17.png?version=1&modificationDate=1530031998000&api=v2)
