---
content_hash: f8ddc99a2c8d96ca558224fc59f0d869a7ca860726a5860e65313c72618fae14
fetched_at: '2026-06-29T00:09:26.509683+00:00'
page_id: '423938308'
product: rm
source: tdn-rm
title: Exportação de Lançamentos Contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938308
version: 9
---

Com a disponibilização do layout de gerador de saídas "CTBLAY0003 - Exportacao Lançamento Contábil.TotvsGen", é possível que o usuário faça exportação dos lançamentos contábeis, para isto, basta:

* Acessar o Gerador de Saída presente na aba "Gestão";
* Importar o layout disponibilizado para exportação, este se encontra na pasta "Objetos Gerenciais > Layout";
* Com o layout importado, acesse o processo de geração de saídas. Será exibido em uma das etapas, filtros onde o usuário irá informar quais os lançamentos serão exportados, sendo eles:

  - **Lote Contábil:** Deve ser informado o lote onde o lançamento contábil está localizado;

  **- Filial:** Possibilita informar a filial das partidas que compõe o lançamento contábil. Esse filtro pode gerar diferenças de débito e crédito, pois as partidas podem pertencer a filiais diferentes.  
  - **ID Lançamento inicial e final:** Possibilita que o usuário informe uma faixa de lançamentos que serão exportados (Ex.: ID 1 ao 10);  
  - **Data inicial e final:** O sistema utiliza esse intervalo de data para selecionar lançamentos que compreendam o período informado;  
  - **Exportar Campos Complementares:** As informações presentes nos campos complementares dos lançamentos só serão exportados caso essa opção seja marcada;  
  **- Salvar os parâmetros de geração:** Caso a opção seja marcada, os filtros utilizados ficarão salvos para uma futura exportação.
* Com os filtros informados, execute o processo;
* Será gerado o arquivo com as informações dos lançamentos que foram filtrados no processo. O arquivo é gerado no formato de importação de lançamentos. Para mais informações sobre o layout de importação de lançamentos,  
  Clique aqui.

**Observação**

* Caso não sejam informados os filtros de ID de lançamento, o processo irá exportar todos os lançamentos presente no lote informado para o período informado;
* O diretório onde o arquivo é gerado pode ser visualizado e editado na primeira etapa da execução do processo.

Informações complementares


* Importação de Lançamento Contábil
Veja também

* [TDN - Exportação de lançamentos contábeis](http://tdn.totvs.com/pages/viewpage.action?pageId=329035481)
