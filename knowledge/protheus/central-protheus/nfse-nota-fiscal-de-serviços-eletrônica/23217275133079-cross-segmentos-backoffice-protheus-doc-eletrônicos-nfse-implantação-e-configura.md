---
article_id: 23217275133079
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 672435048a826cd9cc08c7e34c0f76a5c57258c6076082f18bb97ede2d22deb1
fetched_at: '2026-06-28T22:39:57.499650+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Implantação
  e Configuração de Impressão de NFSE (DANFSE)
type: support-article
updated_at: '2026-05-21T14:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23217275133079-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Implanta%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-de-Impress%C3%A3o-de-NFSE-DANFSE
---

**Dúvida**  
Como realizar a configuração para impressão do DANFSE (PDF da NFS-e)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões  
  
**Solução**  
Para a**Nota técnica - 008/2026**, temos a issue **DSERTSS1-36609** em aberto para tratar o novo layout do DANFSE. Portanto, caso seja necessário a associação à ela, acionar a equipe de suporte do TSS.  
  
Segue abaixo o passo à passo para realização da **configuração atual (ainda não contemplando a NT 008/2026)** do **DANFSE sem customização** no Protheus:  
  
**1.** Primeiramente deverá ser compilado o rdmake **DANFSEII.PRW** no RPO do Protheus através da documentação abaixo:  
- [Clique aqui.](https://suporte.totvs.com/portal/p/10098/download#detail/1152109)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217277811351)

**2.** Aplicar o último **Pacote Acumulado do Protheus** (Expedição Contínua) conforme release:  
- [12.1.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1124963) | [12.1.2410](https://suporte.totvs.com/portal/p/10098/download#detail/1171486)  
  
**3.** Após isso, deverá colocar o arquivo **printer.exe** dentro da pasta appserver e smartclient do Protheus:  
- [Clique aqui.](https://suporte.totvs.com/portal/p/10098/download#detail/693168)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217275084311)  
  
**4.** Também precisará realizar o **Cadastro de Perguntas** via Configurador (SIGACFG), conforme documentação: [DT - Impressão DANFSE.](https://tdn.totvs.com/pages/viewpage.action?pageId=815577333)  
*Obs.: Para a a utilização desse recurso, é necessário que o TSS esteja com data igual ou superior a 28/12/2023.*  
  
**5.** Feito esses procedimentos, basta acessar a rotina **FISA022** e acessar o menu **Outras Ações -> DANFSE:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217275087895)

**6.** Será aberta a tela abaixo para selecionar conforme desejado. Porém vale ressaltar que para DANFSE, **somente está disponível a orientação 'Retrato':**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217275089431)

**7.** Por último será solicitado o preenchimento dos parâmetros com o filtro da nota que deseja realizar a impressão.  
Neste ponto é de extrema importância se atentar para o correto preenchimento de TODOS os dados, principalmente no range de data, que deverá respeitar a **data de emissão,** e não transmissão do documento:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217275093783)

**8.** Após preenchido e clicar em OK, a nota será impressa em PDF:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23217277819287)

**Importante:** A impressão do DANFSE está disponível apenas para o modelo nacional ou municípios que possuem **integração via webservice**, os municípios que geram arquivos txt ou xml (upload de arquivo) não imprimem o DANFSE.
