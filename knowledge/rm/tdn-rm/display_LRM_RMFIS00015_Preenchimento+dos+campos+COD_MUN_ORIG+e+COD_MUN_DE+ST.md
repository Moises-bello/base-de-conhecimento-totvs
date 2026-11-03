---
content_hash: 15f2dfb07fe3d5db25c8733170fe80c937a466309cefe02e03042c1a4a3ce98e
fetched_at: '2026-06-29T00:08:52.757240+00:00'
page_id: '342306409'
product: rm
source: tdn-rm
title: RMFIS00015_Preenchimento dos campos COD_MUN_ORIG e COD_MUN_DE ST
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00015_Preenchimento+dos+campos+COD_MUN_ORIG+e+COD_MUN_DE+ST
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X. |
| **Ocorrência:** | Parametrização para gerar os campos **COD\_MUN\_ORIG** e **COD\_MUN\_DE ST** do Registro D100 - SPED FISCAL. |
| **Ambiente:** |  |
| **Passo a passo:** | Para gerar os campos 24 (**COD\_MUN\_ORIG - Código do município de origem do serviço, conforme a tabela IBGE**) e 25 (**COD\_MUN\_DE ST - Código do município de destino, conforme a tabela IBGE**) do SPED FISCAL, o sistema irá considerar os lançamentos fiscais de **NOTA FISCAL DE SERVIÇO DE TRANSPORTE(D100)**, cujo o **"Código do Modelo de Documento"** seja **“57”, “63” ou “67”**.  CONHECIMENTO DE TRANSPORTE ELETRÔNICO – CT-e (**CÓDIGO 57**); CONHECIMENTO DE TRANSPORTE ELETRÔNICO PARA OUTROS SERVIÇOS - CT-e OS (**CÓDIGO 67**); BILHETE DE PASSAGEM ELETRÔNICO – BP-e (**CÓDIGO 63**).  Seguem os passos para preencher os campos 24 (**COD\_MUN\_ORIG**) e 25 (**COD\_MUN\_DE ST**) do registro D100 no arquivo gerado do SPED FISCAL:  1. O tipo de documento deverá estar preenchido com os códigos de modelo de documento **57, 63 ou 67**      2. No lançamento fiscal na aba, "**Coleta e Entrega"**, deverá estar com os campos dos Municípios preenchidos:    3. É necessário que no cadastro do município a codificação esteja preenchida corretamente, conforme o código específico do mesmo:    4. Na tela de geração da rotina, o campo **"Codificação do Município"**, deverá ser preenchido com o mesmo que foi preenchido no **Cadastro de Município** informado em seu lançamento:    ***Segue abaixo exemplo do resultado do lançamento fiscal no arquivo gerado:*** |
| **Observações:** |  |
