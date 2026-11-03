---
article_id: 360035249033
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 685c1043a82a84b525ea4ca6253399bb28f22c9e2751f202d11dc3cd6014b1d1
fetched_at: '2026-06-28T22:39:47.679405+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC- Atualização do
  cadastro de NCM
type: support-article
updated_at: '2021-09-13T12:31:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035249033-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Atualiza%C3%A7%C3%A3o-do-cadastro-de-NCM
---

**Dúvida**Como realizar a atualização da NCM?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**No módulo Easy Import Control (SIGAEIC), o cadastro de NCM é padrão. Os dados ficam armazenados na tabela SYD e o sistema utiliza as alíquotas para o cálculo dos impostos incidentes na operação de importação. A tabela SYD, ao ser dropada/recriada, traz uma carga inicial de registros. Se o cliente quiser incluir novos registros e/ou atualizar os dados da tabela , os caminhos são os seguintes :

1. Por meio do portal da Receita Federal, onde o Governo disponibiliza informações sobre as NCM´s : (Processo manual, alterado em Atualizações \ tabelas \ NCM) - **Atualização Manual**.
2. Importar alíquotas atualizadas através do software Interfweb (Aduaneiras). O Interfweb possui integração com o SIGAEIC. Para isto, o cliente deve adquirir a licença de uso do software junto à Aduaneiras. Configuração interfweb: <https://tdn.totvs.com/pages/releaseview.action?pageId=453289361>
3. Importar alíquotas atualizadas através do TOTVS Comex Conteúdo. O TOTVS Comex Conteúdo é uma oferta que possibilita a atualização automática de conteúdo de alíquotas de impostos federais, exceções e taxas fiscais de câmbio, visando tornar o processo de importação de mercadorias mais seguro e ágil. Os assinantes do serviço recebem o conteúdo diariamente, de maneira automática a partir dos recursos de agendamento do próprio ERP com o SIGAEIC. Para isto, o cliente deve adquirir a licença de uso do software junto à Aduaneiras. <http://tdn.totvs.com/pages/releaseview.action?pageId=224119853>

**Observação :**  Caso não utilize o módulo SIGAEIC, para atualizar a tabela de NCM seria manualmente, conforme boletim: [Manutenção no cadastro NCM (Clientes que não utilizam o SIGAEIC)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007540511)
