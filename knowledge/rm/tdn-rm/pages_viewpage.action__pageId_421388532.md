---
content_hash: 05b5d7af710ad741959b368ee14739695555b27e64112f43c8b9a1e55ef25690
fetched_at: '2026-06-29T00:09:16.943910+00:00'
page_id: '421388532'
product: rm
source: tdn-rm
title: Captura Títulos em Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388532
version: 4
---

O processo de Captura dos Títulos em Cobrança visa realizar a importação dos títulos constantes no arquivo bancário para a base de dados do TOTVS Gestão Financeira. Para que o sistema encontre essas informações no arquivo é necessário o preenchimento do Layout de DDA no anexo "Layout Bancário" do cadastro do banco que está enviando as informações. São importadas as seguintes informações:

* Código de Barras
* Número do Documento
* Data de Emissão
* Data de Vencimento
* Valor
* Fornecedor
* Tipo Inscrição:

0 - Isento Não Informado;

1 - CPF;

2 - CGC CNPJ;

3 - PIS PASEP;

9 - Outros.

* Inscrição do Cedente

O TOTVS Gestão Financeira possibilita o usuário importar apenas um arquivo ou efetuar o processo para vários arquivos de retorno que estejam localizados num diretório em comum e que pertençam a um mesmo Banco. Ao selecionar a opção "Múltiplos arquivos", o sistema irá processar todos os arquivos de retorno deste diretório, de acordo com as opções selecionadas durante o processo.

Os logs do processo poderão ser salvos numa pasta, também definida pelo usuário, e o sistema irá gerar um log para cada arquivo processado. Além disso, é possível também ao usuário o agendamento e posterior execução (quando o ambiente está configurado em N camadas) em horário definido, poupando recursos e deixando o processo mais assertivo.

**Parâmetros e execução**

Para realizar a captura dos títulos em cobrança, basta acessar o Movimentações bancárias | DDA - Débito Direto Autorizado. Detalhamento das opções do processo:

Banco

Os arquivos processados serão somente do banco selecionado.

Pasta de leitura dos arquivos de retorno

Pasta que o sistema irá ler e processar os arquivos de retorno para captura dos títulos em cobrança. O sistema apenas irá processar os arquivos do banco que foi selecionado na opção "Banco". Caso existam arquivos de bancos diferentes no mesmo diretório, o sistema não processará os arquivos e apresentará os detalhes no log de execução do processo. O usuário deve ter permissão de leitura/escrita neste diretório onde o processo será executado.

Pasta onde o log do retorno será salvo (opcional)

Permite ao usuário salvar todos os logs de retorno gerados durante o processo, para conferência. É recomendado que esta opção seja sempre marcada caso o processo seja executado via agendamento.

Renomear arquivo de retorno processado para extensão .old

Quando marcada essa opção o sistema fará com que o arquivo processado tenha sua extensão alterada para .old, desta forma em importações subsequentes estes arquivos serão ignorados. Assim o arquivo processado será renomeado independente se o processamento foi bem sucedido.
