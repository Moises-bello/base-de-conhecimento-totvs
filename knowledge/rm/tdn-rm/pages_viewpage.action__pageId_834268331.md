---
content_hash: 05dcaac11fca69be0bbfbe16a7945503cb9bfcff1e0c591838addfd6ee3c2a15
fetched_at: '2026-06-29T00:11:49.492732+00:00'
page_id: '834268331'
product: rm
source: tdn-rm
title: Monitorar SEFAZ (CT-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=834268331
version: 2
---

Este processo é utilizado para informar ao contribuinte se a SEFAZ da UF da filial está operando normalmente, bem como validar se as parametrizações desta filial estão corretas. É aconselhável que ele seja executado sempre imediatamente antes dos conhecimentos serem enviados, pois este WebService disponibilizado pelo ambiente do CT-e informa o estado da SEFAZ e sugere a entrada em contingência ou não. Veja abaixo uma mensagem de retorno para uma UF onde o serviço estava fora do ar ao ser consultada: 

***"Conhecimento de Transporte Eletrônico - Modelo 57* *Versão da mensagem: 3.00* *Mensagem: 999 Erro na SEFAZ:*  *Sugestão: Autorizada operação contingência* *UF Origem: SP"*** 

Outra mensagem na execução do processo onde o serviço está em operação:

***"Conhecimento de Transporte Eletrônico - Modelo 57* *Versão da mensagem: 3.00* *Mensagem: 107 Serviço em operação* *Status do serviço: SERVICO EM OPERACAO* *UF Origem: SP"***

De qualquer forma o contribuinte ainda pode consultar o status de sua SEFAZ e a orientação do uso do serviço substituto no próprio [Portal Sefaz CT-e](https://www.cte.fazenda.gov.br/portal/disponibilidade.aspx?versao=4.00&tipoConteudo=XbSeqxE8pl8=).  
Este processo só está disponível para a integração com o TSS. Quando se usa a integração com o TOTVS Colaboração 2.0 o próprio ambiente já fornece esta informação.
