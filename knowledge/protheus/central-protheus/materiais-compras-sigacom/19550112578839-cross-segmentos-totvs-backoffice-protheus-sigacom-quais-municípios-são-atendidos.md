---
article_id: 19550112578839
category: Materiais - Compras (SIGACOM)
content_hash: 123186fd5383411f7e5c734f0cac4ec60de55a665321bda62baac8d932d922f4
fetched_at: '2026-06-28T22:41:24.143454+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais Municípios são
  atendidos pelo TOTVS Transmite?
type: support-article
updated_at: '2024-03-28T12:43:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19550112578839-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-Munic%C3%ADpios-s%C3%A3o-atendidos-pelo-TOTVS-Transmite
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19550054903831) Tempo aproximado para leitura: **00:05 min** **Dúvida**Quais Municípios são atendidos pelo TOTVS Transmite?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução:**

**Serviços de recebimento Nota Fiscal de Serviços (NFSe)**

Nesta página você encontra a relação de municípios que são atendidos pelo TOTVS Transmite para o recebimento de NFSe. Abaixo você pode consultar a relação de municípios para importação manual e/ou sincronização automática de NFSe(s) recebidas para o TOTVS Transmite.

Para melhor entendimento vamos detalhar algumas das colunas da planilha:

#### **Sincroniza Município Automaticamente:**Identifica o status do recebimento automático de NFSe do município para o TOTVS Transmite via Web Service, os status possíveis são:

* **Homologado:**Já fizemos a homologação junto a respectiva prefeitura e com isso a busca automática de NFSe(s) está 100% validada para uso do cliente;
* **Implementado:**O município em questão utiliza o mesmo provedor que já homologamos por outro município, ou seja, caso não existam especificidades ele já esta preparado para integrar as NFSe(s) com o produto TOTVS Transmite;
* **Planejado:**O município esta planejado para ser implementado no Produto TOTVS Transmite, avaliar a coluna prazo para verificar quando será disponibilizado;
* **RoadMap:**O município em questão ainda não esta preparado para integrar NFSe automaticamente via Web Service com o TOTVS Transmite. Caso queria sugerir a inclusão de novos municípios favor utilizar a central colaborativa no link a seguir: [Sugestão Município NFSe - TOTVS Transmite - Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/9387074194967-Cross-Segmentos-TOTVS-Transmite-Nota-Fiscal-de-Servi%C3%A7os-Eletr%C3%B4nica-NFS-e-);
* **Serviço Não Disponibilizado pela Prefeitura:**Significa que esse modelo de integração não é disponibilizado pela referida prefeitura e com isso não é possível sincronizar as NFSE(s) via Web Service.

#### **Importa XML Manualmente:**Identifica se o Município em questão já pode ter sua NFSe importada manualmente no produto TOTVS Transmite, os status possíveis são:

* **Homologado:**Já fizemos a homologação completa da importação manual da NFSE da prefeitura e está 100% validada para uso do cliente;
* **Implementado:**Significa que o município em questão utiliza o mesmo provedor que já homologamos por outro município, ou seja, caso não existam especificidades ele já esta preparado para importar manualmente as NFSe(s) com o produto TOTVS Transmite;
* **Planejado:**O município esta planejado para ser implementado no Produto TOTVS Transmite, avaliar a coluna prazo para verificar quando será disponibilizado;
* **RoadMap:**O município em questão ainda não esta preparado para importação manual da NFSe com o TOTVS Transmite.

#### **Integração por e-mail(.xml):**Permite que o XML da NFSe do município seja importada diretamente da caixa de e-mail do cliente/fornecedor para o produto TOTVS Transmite, os status possíveis são: (**Essa funcionalidade encontra-se em homologação**);

* **Homologado:**Já fizemos a homologação completa da importação do XML da NFSE por e-mail e está 100% validada para uso do cliente;
* **Implementado:**Significa que o município em questão utiliza o mesmo provedor que já homologamos por outro município, ou seja, caso não existam especificidades ele já esta preparado para receber o XML das NFSe(s) via e-mail e integrar com o produto TOTVS Transmite;
* **Planejado:**O recebimento de XML da NFSE via e-mail do município esta planejado para ser implementado no Produto TOTVS Transmite, avaliar a coluna prazo para verificar quando será disponibilizado;
* **RoadMap:**O recebimento de XML da NFSE via e-mail do município ainda não esta preparado para integração no TOTVS Transmite.

#### **Integração por e-mail(.pdf): Permite que o PDF da NFSe do município seja importada diretamente da caixa de e-mail do cliente/fornecedor para o produto TOTVS Transmite, os status possíveis são:**

* **Homologado:**Já fizemos a homologação completa da importação do PDF da NFSE por e-mail e está 100% validada para uso do cliente;
* **Implementado:**Significa que o município em questão utiliza o mesmo provedor que já homologamos por outro município, ou seja, caso não existam especificidades ele já esta preparado para receber o PDF das NFSe(s) via e-mail e integrar com o produto TOTVS Transmite;
* **Planejado:**O recebimento de PDF da NFSE via e-mail do município esta planejado para ser implementado no Produto TOTVS Transmite, avaliar a coluna prazo para verificar quando será disponibilizado;
* **RoadMap:**O recebimento de PDF da NFSE via e-mail do município ainda não esta preparado para integração no TOTVS Transmite;
* **Indisponível:**O TOTVS Transmite não irá fornecer a importação via PDF do respectivo Município.

**Prazo de Implementação da próxima funcionalidade:**Sempre que o status de algum item for "planejado" aqui se encontra quando aquele município será entregue no produto TOTVS Transmite, no caso de Municípios que possuam o status "Planejado" em mais de uma coluna assume-se a maior data de entrega neste campo. (**O prazo pode sofrer variações, quando ocorrer será atualizada com antecedência**);

Documentação Completa : [Serviços de recebimento Nota Fiscal de Serviços (NFSe)](https://tdn.totvs.com/pages/releaseview.action?pageId=682452818)

***Saiba Mais:***

* [TOTVS Transmite - Base de Conhecimento](https://tdn.totvs.com/display/public/TTE/TOTVS+Transmite+-+Base+de+Conhecimento)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
