---
content_hash: af716c90452dd08e8c0897af0294b89183e90c825381d36a3e1c662abce03ca9
fetched_at: '2026-06-29T00:09:26.759771+00:00'
page_id: '423938411'
product: rm
source: tdn-rm
title: Posição dos Campos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938411
version: 3
---

Aqui você informará ao sistema a posição de cada campo no arquivo, aquele que contiver as informações a serem importadas para o sistema. Essa operação é necessária principalmente para determinar quais campos importar e qual fim o dado do arquivo a importar terá. São apresentadas as seguintes abas neste anexo:  
   
 **Pasta Identificação**  
    
 Aqui serão preenchidos os detalhes do campo a ser importado, a partir do arquivo de importação.

*Exemplo 1:*O arquivo a importar possui uma coluna chamada DATABASTECIMENTO e desejamos fazer referência ao campo Data de Coleta, do Histórico de Indicador de Uso.   
 Isso significa que ao solicitar a importação do arquivo texto, a data da coluna DATAABASTECIMENTO irá preencher o campo Data de Coleta do Histórico de Indicador de Uso.   
 A coluna DATAABASTECIMENTO fica na posição 18 do arquivo, então a ordem deve ser ajustada para o número 18.  
    
*Exemplo 2:*No mesmo arquivo, existe a coluna NUMABAST, que retém o número de identificação de todos os abastecimentos. Por ser identificador destes registros, devemos informar isso ao sistema, marcando o parâmetro "Campo Identificador do Registro no Arquivo Texto".   
 No arquivo do padrão "CTF", o campo NUMABAST originalmente é Identificador do Registro.   
 O motivo de classificarmos estes campos como Identificadores é para que, no momento da importação, um histórico de indicador de uso não seja importado mais de uma vez.  
 Concluindo, a coluna NUMABAST fica na posição 2 do arquivo, então a ordem deve ser ajustada para o número 2.  
    
 **Pasta CTF**  
 Esta pasta é destinada à configuração da importação de arquivos do tipo CTF (Controle de Telefrotas), sistema que foi desenhado com base no conceito de Banco de Dados distribuído e que visa controlar   
 Para maiores detalhes relacionado ao Controle de Telefrotas (CTF), acesse: <http://www.portalctf.com.br>  
 Uma vez verificado que o arquivo a importar é do tipo CTF é preciso que os campos sejam relacionados a este padrão:  
 Nenhum: quando o campo não se relaciona a nenhum dos tipos descritos abaixo.  
 Apontador: o campo do tipo apontador do arquivo a importar.  
 Status: registro que informa se o abastecimento foi feito total ou parcialmente.  
***Atenção!***  Para que essa pasta seja habilitada, é necessário que no Layout de Importação do Indicador de Uso (Operações | Importação de Lançamento de Indicadores de Uso | Layout de Importação, edição do Layout) seja habilitado o parâmetro "Importação do Tipo CTF".
