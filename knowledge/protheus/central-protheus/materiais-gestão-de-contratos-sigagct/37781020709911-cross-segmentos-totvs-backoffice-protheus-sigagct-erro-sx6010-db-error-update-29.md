---
article_id: 37781020709911
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: fb60cf07aa2b42148aec2d4677bd3a3b00b7976871f6fe440f57f3247e2b15be
fetched_at: '2026-06-28T22:37:22.749259+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro SX6010: DB error
  (Update): -29 File: SX6010 -  on PUTMV(PUTMV.PRG) ao Tentar abrir a Rotina Manutenção
  de Contratos (CNTA300)'
type: support-article
updated_at: '2026-01-19T17:39:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37781020709911-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-SX6010-DB-error-Update-29-File-SX6010-on-PUTMV-PUTMV-PRG-ao-Tentar-abrir-a-Rotina-Manuten%C3%A7%C3%A3o-de-Contratos-CNTA300
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37781020698903) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
 Erro SX6010: DB error (Update): -29 File: SX6010 -  on PUTMV(PUTMV.PRG) ao Tentar abrir a Rotina Manutenção de Contratos (CNTA300)   
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**  
Uma das Possibilidades da causa do erro é do uso incorreto do ponto de entrada [AfterLogin - Execução após abertura de SXs](https://tdn.totvs.com/pages/releaseview.action?pageId=6815186)  
  
**Solução**  
Segue algumas possibilidades para solução do erro abaixo:

1. Peço por gentileza, que realize os testes desativando as customizações do ambiente através dos [3 métodos indicados nesta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292), impreterivelmente.

1 - Através da chave IXBLOG no arquivo APPSERVER.ini

2 - Através do Configurador CFG - Catálogo de Personalizações

3 - Desabilitar customizações chamadas no dicionário de dados

2. Verifique se as configurações do parâmetro **MV\_ATUGCT** estão conforme o padrão do sistema.Conforme print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37781037471895)  
Verifique se não possui registros duplicados do parâmetro **MV\_ATUGCT** com filiais diferentes , caso possua teste em ambiente de teste com o campo filial em branco.

3.Por gentileza realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Gestão de Contratos conforme sua versão](https://tdn.totvs.com/pages/viewpage.action?pageId=679961416)  
- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168420)

- Smartclient WebApp - [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

- DBAccess - [MP - FRAME - Atualização do DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033789713-MP-FRAME-Atualiza%C3%A7%C3%A3o-do-DBAccess?source=search)

Obs: Recomendamos backup e validação primeiramente em ambiente teste.

Caso ainda assim o erro persista abra um ticket em um de nossos canais de atendimento com o arquivo de erro atualizado e com o resultado das informações acima.

**Saiba Mais:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Documentação Gestão de Contratos do TDN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441027145623)

[Guia de Referencia - Gestão de Contratos - Protheus 12](https://tdn.totvs.com/pages/viewpage.action?pageId=224127467)

[FAQs - Gestão de Contratos](https://tdn.totvs.com/x/O_tgDQ)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
