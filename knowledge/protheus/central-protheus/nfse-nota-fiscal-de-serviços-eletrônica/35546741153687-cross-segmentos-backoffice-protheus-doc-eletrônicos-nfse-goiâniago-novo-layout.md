---
article_id: 35546741153687
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 95a83e6bd24913b47e939f38d064ae8ebb7edcf16d8ec30da10660103878a83b
fetched_at: '2026-06-28T22:39:57.472247+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Goiânia/GO
  (Novo Layout)
type: support-article
updated_at: '2026-01-15T18:41:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35546741153687-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Goi%C3%A2nia-GO-Novo-Layout
---

**Dúvida**  
Quais atualizações ou configurações necessárias para se adequar ao novo layout da prefeitura de Goiânia?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Para atender ao novo layout que a prefeitura de Goiânia adequou para atender ao layout nacional, se fazem necessários:  
  
**TSS**  
**1.****Atualização do RPO:-** [**MP - TSS - Atualização do Appserver (binário) do TSS**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Appserver-bin%C3%A1rio-do-TSS?source=search)  
**2.** **Atualização das URLs:-** [**TSS Transmissão de Documentos Eletronicos - NFSe - Configuração do NEWNFSE**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16784834285847-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletronicos-NFSe-Configura%C3%A7%C3%A3o-do-NEWNFSE)   
**3.** **Atualização do .XSD:**-[**TSS - Atualização dos SCHEMAS**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**IMPORTANTE**: Ambientes com TSS TOTVS Compartilhado já contemplam essas atualizações do TSS.  
  
**PROTHEUS**  
**1.** **Configuração de Versão:**Dentro da rotina FISA022, refazer o wizard.cfg por completo, informando envio Prefeitura e a nova versão de layout '2.04'   
  
**Particularidades**  
**Série da RPS**: o provedor utiliza como padrão para envio em **homologação Serie "3" e produção a série “1”** para RPS, tanto em homologação como produção a serie deve ser NUMERICA;  
  
**Sequencia de RPS:** o provedor consiste número de RPS, que devem primeiro ser solicitadas através do portal no seguinte caminho “Solicitação de Documentos Fiscais” -> “ Solicitação”, nesta opção será gerado números de RPS a serem consumidos, exemplo de 1 a 50;  
  
**Tag ItemListaServico** deve ser sempre com 5 digitos e "." (ponto) no meio. Exemplo: '7.03' deverá ficar '07.03';   
  
**Tag CodigoTributacaoMunicipio:** Deve ser o mesmo ItemListaServiço, porém sem "." e o 0. Ex: 703  
  
**Código do município do tomador:** Esse conteúdo agora é composto pelos campos **A1\_EST e A1\_COD\_MUN**, que juntos formam o código de **7 dígitos conforme o padrão do IBGE**.  
O campo **A1\_OUTRMUN**, que anteriormente armazenava um código específico de Goiânia, **não será mais utilizado**, uma vez que a prefeitura passou a adotar o padrão IBGE.  
  
**Documentação:** https://tdn.totvs.com/pages/releaseview.action?pageId=580483698
