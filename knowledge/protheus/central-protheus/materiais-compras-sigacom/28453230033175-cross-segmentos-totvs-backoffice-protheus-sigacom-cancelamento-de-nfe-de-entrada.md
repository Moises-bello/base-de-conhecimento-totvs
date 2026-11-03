---
article_id: 28453230033175
category: Materiais - Compras (SIGACOM)
content_hash: 018a6e08653c4863865cefea49161ec342c2ad47a7a6c6c87fc731843ea132f9
fetched_at: '2026-06-28T22:41:14.364496+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Cancelamento de Nfe
  de Entrada via Transmissão para SEFAZ
type: support-article
updated_at: '2024-12-11T19:28:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28453230033175-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Cancelamento-de-Nfe-de-Entrada-via-Transmiss%C3%A3o-para-SEFAZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28453229995927) Tempo aproximado para leitura: **00:04:00 min****Dúvida**  
Cancelamento de NF após verificação na SEFAZ.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Situação / Requisito**

* Implementação do cancelamento de NFe de entrada via transmissão para SEFAZ durante a exclusão do documento.

**Solução**

* Realizado desenvolvimento do cancelamento de documentos que tenham sido transmitidos para SEFAZ.

Para habilitar o cancelamento automático de documentos com transmissão para SEFAZ seguir os procedimentos a seguir:

**Passo 1 : Atualização do pacote, clicando nos links à seguir conforme a versão :**

[12.1.2210](https://suporte.totvs.com/portal/p/10098/download?e=1177402) [-](https://r.totvs.io/p/1177402)[12.1.2310 -](https://suporte.totvs.com/portal/p/10098/download?e=1177400)[12.1.2410 -](https://suporte.totvs.com/portal/p/10098/download?e=1177403)[12.1.33](https://suporte.totvs.com/portal/p/10098/download?e=1177401)

**Passo 2 :**Habilitar o cancelamento automático de documentos com transmissão para SEFAZ, será necessário possuir dois parâmetros:

- **MV\_NFENTCA**→ .T. habilita a transmissão de cancelamento ao excluir um documento.  
                           → .F. Sem alteração de comportamento, exclusão do documento sem conexão com a SEFAZ.  
**Default**: .F.   
  
- **MV\_CANTENT**→ Número de tentativas de consulta do retorno da SEFAZ.  
**Default**: 6 **Máximo**: 20 

* Quando a transmissão estiver habilitada, ao **excluir**um documento da espécie SPED e que tenha sido transmitido, será exibida a mensagem de confirmação a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28453190632343)

* **Não**→ Aborta a exclusão do documento e não transmite o cancelamento / **Sim**→ Realiza a transmissão do cancelamento da NFe e se autorizado, exclui o documento da base.
* Durante a transmissão, serão realizadas tentativas de consultas na SEFAZ para obter o retorno do status de cancelamento, exibindo a mensagem: "Consultando autorização de cancelamento". O número de tentativas será o valor que estiver no parâmetro **MV\_CANTENT,**respeitando um máximo de 20.
* Caso o cancelamento seja **bem-sucedido** será exibida a mensagem e o documento será excluído:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28453552559639)

**Importante - Rotina automática MATA103**:

* Este mesmo processo ocorre na rotina automática de exclusão de documentos do MATA103.   
  As mensagens das etapas são gravadas no console e poderão ser visualizadas se a tag FWLOGMSG\_DEBUG=1 existir no appserver.ini do ambiente.  
  Por padrão, se o parâmetro **MV\_NFENTCA**estiver habilitado e o documento for espécie SPED e tenha sido transmitido, automaticamente será efetuada a tentativa de transmissão de cancelamento deste documento.
* Caso o cancelamento **não**seja autorizado ou não tenha retorno da SEFAZ, será exibida a mensagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28453552566039)

* A mensagem de não autorização do cancelamento, será gravada na aba histórico dentro do Documento:  
  O Documento ficará com Status (F1\_STATUS = G) e Legenda Preta com a letra C representando que houve uma tentativa de transmissão de cancelamento mas não fora autorizada.

***Saiba Mais :***

[Cancelamento de NF após verificação na SEFAZ](https://tdn.totvs.com/pages/releaseview.action?pageId=896205860)

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
