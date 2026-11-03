---
content_hash: cdc460eb468d1b614c06f27ac543904f3ce8cde02eeb345b0db82f4ad16a34ca
fetched_at: '2026-07-02T19:24:26.013387+00:00'
page_id: '519714915'
product: protheus
source: tdn-tec
title: 10.4 Novo Fonte WSDL AdvPL
type: documentation
url: https://tdn.totvs.com/display/tec/10.4+Novo+Fonte+WSDL+AdvPL
version: 2
---

*Este tipo de assistente o auxilia na criação de arquivos-fontes, com a definição de um cliente de serviço web (*web service client*) a partir da sua definição WSDL*.

*Tela 100: Execução do assistente de geração de clientes de serviços web (web service client)*

Este assistente depende de uma definição de servidor *Protheus* e o selecionamento deste na barra de ferramentas. Caso o serviço web a ser utilizado esteja fora da rede do usuário, o servidor *Protheus* deverá ter privilégios de acesso.

Informe os dados solicitados:

* **Local** (*folder*) (Tela 100 A) – indica o local (*folder*) onde o arquivo-fonte será salvo
* **Nome do fonte** (Tela 100 B)**–** nome do arquivo-fonte que conterá a definição *WSDL*
* **URL** (Tela 100 C)– informe a URL de onde esta o serviço web desejado(\*)
* **Criar arquivo como referência** (Tela 100 D) – o arquivo será gravado no Diretório de Destino e no local será criado uma ligação simbólica (*link*).

O cliente de serviço web, também pode ser gerado a partir de um arquivo de definição no lugar de informar a URL.

1. O arquivo com a definição deve ser copiado para o servidor, dentro da pasta (ou uma subpasta) apontada na chave `rootPath`. Por exemplo:  
   `ROOTPATH=m:\protheus\data_110`
2. No campo URL do assistente, informar o caminho e nome do arquivo relativo ao `rootPath`. Por exemplo:
   * Copiar o arquivo de definição para `m:\protheus\data_110\ws`"
   * No assistente informe: `/ws/CurrencyService.svc.xml`
3. Prossiga com a geração

Após informar os dados solicitados, finalize e obterá algo semelhante a:

                   *Tela 101: Tela após a geração de um cliente de serviço web*

Consulte  para mais opções.
