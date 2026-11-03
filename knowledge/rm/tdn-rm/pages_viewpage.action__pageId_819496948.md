---
content_hash: bcc06f4569a2d9447764d010876a816a37bafb6e0dc6229b50019c80ed593120
fetched_at: '2026-06-29T00:11:45.120376+00:00'
page_id: '819496948'
product: rm
source: tdn-rm
title: Importação de Indicadores de Uso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819496948
version: 3
---

O CTF é um arquivo gerado pelos postos da Petrobrás e Ipiranga. Quando um Objeto de Manutenção passa em um dos postos dessas distribuidoras o sistema ler os dados da placa e o medidor atual.  
Assim através do site das distribuidoras é possível ter acesso ao arquivo (.txt) para se ter controle dos indicadores de uso de uma frota de Objetos de Manutenção que estão em circulação. Um arquivo do tipo CTF carrega os principais dados para importação de indicadores de uso no RM Officina. O layout abaixo deve ser cadastrado no menu Atividades/ Importação de Lançamento de Indicadores de Uso / Layout de Importação. Essa funcionalidade não é especifica para importação de arquivo de CTF, poderá ser usada para importar arquivo de indicadores de uso de acordo com a necessidade da Empresa.

Considere o exemplo da estrutura do arquivo texto abaixo, o mesmo foi configurado de acordo com o layout citado acima.

**Pasta Identificação**  
Na tela é possível visualizar a configuração do layout de importação para o exemplo do arquivo “ArquivoCTF.txt” . Como no arquivo o “Separador de Campo” usado foi “;” marcar para “Desconsiderar cabeçalho e rodapé” e “Id. do Objeto Utilizado” será o primeiro identificador do objeto.“Caminho Padrão do Layout” será o caminho, no qual o arquivo de importação será armazenado.

**Pasta Posição dos Campos**

Permite cadastrar os campos informados no cabeçalho do arquivo de importação. No exemplo do arquivo “ArquivoCTF.txt” os campos INDICE, NUMABAST e STATUS são apenas informativos, ou seja, não serão inseridos na tabela OFHISTINDICADOR.

Os campos PLACA, MEDIDOR e DATACOLETA serão inseridos na tabela OFHISTINDICADOR. Considere que a importação seja de arquivo CTF e marque a opção “Importação do Tipo CTF”.

Ao marcar essa opção no cadastro das Posições de Campos será habilitado uma Pasta chamada CTF como mostra as figuras abaixo.

* Para o campo **INDICE** não informe a tabela **OFHISTINDICADOR** e na Pasta CTF marque a opção apontador.
* Para o campo **NUMABAST** não informe a tabela **OFHISTINDICADOR** e na Pasta CTF marque a opção Nenhum.
* Para o campo **STATUS** não informe a tabela **OFHISTINDICADOR** e na Pasta CTF marque a opção status.
* Para o campo **PLACA** informe a tabela **OFHISTINDICADOR**, coluna Identificador do Objeto (IDOBJOF) e na Pasta CTF marque a opção Nenhum.
* Para o campo **MEDIDOR** informe a tabela **OFHISTINDICADOR**, coluna Valor Medidor 1(VALOR MEDIRO 1) e na Pasta CTF marque a opção Nenhum.
* Para o campo **DATA DA COLETA** informe a tabela **OFHISTINDICADOR**, coluna Data da Coleta (DATACOLETA) e na Pasta CTF marque a opção Nenhum.

Após cadastrar o layout acesse o menu Operações / Importação de Lançamento de Indicador de Uso / Importação e importe o arquivo “ArquivoCTF.txt”. O sistema armazena um histórico de todas as importações no menu Operações / Importação de Lançamento de Indicador de Uso / Histórico de Importação.
