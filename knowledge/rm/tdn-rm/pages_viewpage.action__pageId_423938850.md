---
content_hash: 18211c7d54979ff00d24c7034fc687c6a5580a24f0236921cd37c227de215665
fetched_at: '2026-06-29T00:09:29.247546+00:00'
page_id: '423938850'
product: rm
source: tdn-rm
title: Parâmetros por Filial (MDF-e - Manifesto de Destinatário Eletrônica)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938850
version: 7
---

Menu Ambiente | Parâmetros | TOTVS Gestão de Estoque, Compras e Faturamento | Integração | Fiscal | Dados Fiscais   
Nesta Etapa deverá ser informada a versão do Totvs Colaboração. No campo Versão, há as opções:

* **Não Utilizada**: Quando não há Totvs Colaboração e se utiliza TSS sem integração com a Neogrid;
* **1.00**: Quando há Totvs Colaboração e a integração com a Neogrid é feita pela ferramenta TSS;
* **2.00**: Quando há Totvs Colaboração e a integração com a Neogrid é feita pela ferramenta Client Neogrid.
* **Parâmetros por Filial**: Nesta Etapa deverão ser informados os dados fiscais de integração do MD-e.

O campo Diretório deve ser preenchido quando for utilizado o Client Neogrid. Nele deve constar o caminho onde a ferramenta está instalada. No caso do MD-e não é realizado o processo com a versão 1.00 (TSS mais integração Neogrid).

**Parametrização a ser realizada com TSS (Não Utilizada):** Manifestação Destinatário

**Ambiente Produção**: Se o manifesto for feito oficialmente junto a SEFAZ (Secretaria da Fazenda) Homologação. Se o manifesto for feito somente para homologação do processo.

**Versão de Sincronização de Documentos**: Deve-se informar a versão atual do Layout de sincronização de documentos fornecidos pela SEFAZ.

**Parametrização a ser realizada com Client Neogrid (Totvs Colaboração 2.00)**

**Informações TOTVS Colaboração**

**Usuário TOTVS Colaboração**: Usuário para integração com a Neogrid.

**Senha TOTVS Colaboração**: Senha do usuário para integração com a Neogrid.

**Ambiente TOTVS Colaboração**: Recebimento

* **Produção**: Se o manifesto for feito oficialmente junto a Neogrid e SEFAZ (Secretaria da Fazenda)
* **Homologação**: Se o manifesto for feito somente para homologação do processo.

**Número Máximo de Documentos para Retorno**: Quantidade máxima de documentos para retorno

**Tipo Documento Integração TOTVS Colaboração**: Quais documentos estão habilitados para serem utilizando na integração da Neogrid e ERP, sendo que não basta só habilitar os mesmo sem está realmente integrado com a Neogrid.

**Manifestação Destinatário**

**Ambiente Produção**: Se o manifesto for feito oficialmente junto a SEFAZ (Secretaria da Fazenda)

**Homologação**: Se o manifesto for feito somente para homologação do processo.

**Versão de Sincronização de Documentos**: Deve-se informar a versão atual do Layout de sincronização de documentos fornecidos pela SEFAZ.

Informações Adicionais

* [Boletim Técnico - Manifestação do destinatário Eletrônica (MD-e](http://tdn.totvs.com/display/LRM/MOV_BT_Manifestacao+do+Destinatario_BRA_118X))
* [Monitor de Arquivos TOTVS Colaboracão](http://tdn.totvs.com/display/LRM/Monitor+de+Arquivos)
