---
content_hash: 5c254a286d4e706752da088cefd606e95bfadcf231635e36803e91bbbf7ce458
fetched_at: '2026-06-29T00:09:28.670624+00:00'
page_id: '423938745'
product: rm
source: tdn-rm
title: Sincroniza Documento (MD-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938745
version: 2
---

Neste processo serão sincronizados as NF'es que foram emitidas para o destinatário do Manifesto.

**Filial** - Informe a filial que deseja sincronizar

**Indicador da nota Fiscal** - Informe a opção de quais documentos deseja sincronizar todas as NF'es:

* NF'e com Ciência da Emissão,
* Confirmada,
* Desconhecida,
* e Operação não realizada.

**Somente as NF'es que não tiveram Manifestação do Destinatário** - (NF'es pendentes manifestos e com Ciência da Emissão) Somente as NF'es que não tiveram Manifestação do Destinatário e não tiveram Ciência da Emissão - (Somente NF'es Pendentes).

**Indicador do Emissor da Nota Fiscal** - Informe a opção de remetente dos documentos que deseja sincronizar todos os Emitentes/Remetentes.

**Busca todas as NF'es Somente as NF'es emitidas por emissores/remetentes que não tenham a mesma raiz do CNPJ do Destinatário** - Somente NF'es de Terceiros.  
***Observação***: Para se utilizar o MD-e com o client NeoGrid é necessário parametrizar da seguinte forma:

1. Na etapa "Integrações → Fiscal → Importação/Envio de Arquivos XML" o parâmetro "Versão TOTVS Colaboração", deve ser marcado com o valor "2.00".
2. Nos parâmetros fiscais da Filial, etapa "Importação/Envio de Arquivos XML 1/2" o parâmetro "MD-e dentro do campo "Tipo Documento Integração TOTVS Colaboração" deve estar MARCADO.  
   Quando utilizado o Client Neogrid, para sincronizanação, o arquivo xml das NF'es devem estar na pasta IN, no diretório onde o client está instalado e o mesmo iniciado. Já com o TSS basta está com o mesmo iniciado para realizar a sincronização.
