---
content_hash: 7c7766ea70f40aa1d7db8a4127659dd8a19dfeacfeb230cd043b9012029b3b81
fetched_at: '2026-06-29T00:09:29.170630+00:00'
page_id: '423938827'
product: rm
source: tdn-rm
title: Parâmetros por Filial (CT-e - Conhecimento de Transporte Eletrônico)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938827
version: 4
---

Para enviar CT-e (Conhecimento de Transporte Eletrônico) é necessário parametrizar os dados fiscais da filial. O envio de CT-e pode ser feito direto pela SEFAZ, utilizando o TSS ou utilizando uma das duas versões do TOTVS Colaboração que são a 1.00 (RM+TSS+Neogrid) e 2.00 (RM+Client Neogrid), que tem parametrizações diferentes.   
 Primeiramente deve-se escolher a versão. Ao acessar Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Fiscal | Dados Fiscais -> Importação/Envio de Arquivo XML é possível escolher:

* **Não Utiliza:** Quando não se utiliza o TOTVS Colaboração
* **1.00**: Quando se utiliza o TSS juntamente com o TOTVS Colaboração, além do Client Neogrid
* **2.00**: Quando se utiliza o somente Client Neogrid e o TOTVS Colaboração OBS: Ao escolher a versão 2.00 deve-se informar o caminho de onde o Client Neogrid fará a busca dos arquivos necessários, no campo Diretório Padrão para Importação dos Arquivos XML.

Em Parâmetros por Filial, deve ser selecionada Filial que irá enviar CT-e e preencher as etapas, que variam de acordo com a versão do Totvs Colaboração.  
 Quando o envio do CT-e é feito utilizando o TSS, seja direta (sem vinculo com o TOTVS Colaboração) ou indiretamente (TOTVS Colaboração 1.0), deve-se parametrizar a etapa do Certificado Digital.

**Certificado Digital 2/2 (CT-e):** Tipo do Certificado Digital: Informar, no ComboBox, o formato do certificado - Certificado Digital CT-e: Selecionar entre os Certificados Digitais cadastrados na base, por meio do módulo Gestão Fiscal. Ao utilizar o TOTVS Colaboração para o envio (versão 1.00 ou 2.00), deve-se parametrizar também a etapa correspondente.

**Importação/Envio de Arquivo XML 1/2**

**Usuário**: Usuário utilizado pela filial na Neogrid

**Senha**: Senha do usuário

**Ambiente TOTVS Colaboração**

1. Recebimento
2. Não utiliza
3. Homologação
4. Produção

Tipo Documento Integração TOTVS Colaboração: Pode-se escolher a opção Todos, ou marcar quais os documentos serão utilizados.   
Ressalta-se que o processo só obterá êxito se os documentos escolhidos estiverem integrados com a Neogrid.  
Independente da versão selecionada para o TOTVS Colaboração, a etapa de CT-e deve estar parametrizada para atender os requisitos de envio.

**Ambiente CT-e:**-Ambiente e Modalidade     Ambiente de envio: O envio pode ser feito em Homologação (Teste) ou Produção

**Modalidade de Operação**: Normal ou em Contingência - Versões de Layout Utilizados     CT-e: 3.00
