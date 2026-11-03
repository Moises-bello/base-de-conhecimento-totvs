---
content_hash: f644c873fe2830e86fd02f4faa23bd525cf3035096c3077e6517879b001bed84
fetched_at: '2026-06-29T00:09:27.930688+00:00'
page_id: '423938576'
product: rm
source: tdn-rm
title: Layout de Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938576
version: 3
---

O layout de importação é o local onde devem ser fornecidas informações do tipo de arquivo a ser importada, qual a estrutura do arquivo e a localização deste. Veja a função de alguns recursos dessa janela:

**Importação do Tipo CTF**: Marcando o parâmetro, você define que a importação será a partir de arquivos tipo CTF.   
***Observação***: O sistema abrirá uma pasta CTF ao lado da pasta identificação do cadastro Posição dos Campos no Layout de Importação do Indicador de Uso, para preenchimento das informações deste tipo de importação.

**Separador do Campo**: Informa ao sistema como ocorre a separação dos campos no arquivo a importar.  
Exemplo: Um arquivo tem seus campos separados por ponto e vírgula (';'), ele tem este aspecto: INDICE;NUMABAST;PLACA; 1001;3010;QWE9012; 1002;3011;MNO8901;  
Já o arquivo que tem seus campos separados por sustenido (jogo da velha, '#'): INDICE#NUMABAST#PLACA# 5111#110#RTY7080# 5112#111#LKJ0001#

**Desconsiderar linha de cabeçalho**: Se o arquivo de importação possuir cabeçalho, é preciso marcar este parâmetro. Isso fará com que o sistema não importe o cabeçalho do arquivo, dado desnecessário para importação.

**Desconsiderar linha de rodapé**: Como no cabeçalho, é preciso marcar este parâmetro para que o sistema não importe o rodapé do arquivo, dado também desnecessário para importação.  
Id. do Objeto Utilizado: Informe aqui qual identificador do arquivo fará referência ao identificador do objeto de manutenção do sistema. Há três tipos de associação: pelo 1º Identificador, pelo 2º Identificador ou por algum Campo Complementar cadastrado, que deve ser informado ao lado.  
Exemplo: Um arquivo do tipo CTF carrega dados da Placa do veículo. Se o sistema trabalha com veículos cujo 1º identificador é a Placa do Veículo, devemos marcar que o Id. do Objeto Utilizado é o 1º Identificador.

**Caminho padrão do Layout**: local onde os arquivos de importação estão. Este recurso facilita a localização dos arquivos no momento da importação.
