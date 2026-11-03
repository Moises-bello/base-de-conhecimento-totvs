---
content_hash: 6bb532314dd92f8b02d8042955837b13c5840de7d46f82ff9deccafac9567105
fetched_at: '2026-06-29T00:12:10.783169+00:00'
page_id: '953003702'
product: rm
source: tdn-rm
title: Grupo Y - Dados da Cobrança
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003702
version: 7
---

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo Y - Dados da Cobrança** | | | | | | | | |
| **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Ocorrência** | **Observação** | **Campo de Origem** | **Mais Informações** |
| Y01 | cobr | Grupo Cobrança | G | A01 | 0-1 |  |  | A TAG será montada concatenando as seguintes informações: - Se algum produto tiver CST 60 de ICMS será colocada a informação de CST 60: Informações da saída ST 60 (Produto - Base ICMS ST - Valor ICMS ST) : CÓDIGO DO PRODUTO - BASE ST RETIDO = VALOR ST RETIDO;  - Informações Complementares do Contribuinte (INFCOMPLCONTRIBUINTE); - Histórico do Movimento; - Dispositivo Legal da Natureza (Se o parâmetro "inicializa observação" estiver marcado).  Se o ultrapassar o limite de 5000 Caracteres o campo será truncado.  Obs.: Dados de Cobrança com apenas uma ocorrência não devem ser informados quando o [Indicador da Forma de Pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=953003707) for "Pagamento à Vista". |
| Y02 | fat | Grupo Fatura | G | Y01 | 0-1 |  |  |  |
| Y03 | nFat | Número da Fatura | E | Y02 | 0-1 |  |  | Deverão ser criados campos no complementares no movimento com a seguinte nomenclatura: Nome da coluna: XCAMPONFE + nomedocampo. Exemplo: XCAMPONFEDESCRICAO, XCAMPONFECORPRODUTO etc. Descrição: deverá ser preenchida com o nome que será levado para o atributo xcampo. Exemplo: Ao criar o campo complementar XCAMPONFEPRODUTO e descrição Produto no XML será gerado "Produto" na TAG xCampo. O Conteudo preenchido no campo complementar no movimento será levado na TAG xTexto.  **Onde**: Todos os campos iniciados com XCAMPONFE serão levados na NF-e no grupo obsCont (Z04) desde que estejam visíveis para o movimento e com valor preenchido.  Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual do contribuinte. |
| Y04 | vOrig | Valor Original da Fatura | E | Y02 | 0-1 |  |  |  |
| Y05 | vDesc | Valor do desconto | E | Y02 | 0-1 |  |  |  |
| Y06 | vLiq | Valor Líquido da Fatura | E | Y02 | 0-1 |  |  |  |
| Y07 | dup | Grupo Parcelas | G | Y01 | 0-120 |  |  | Não é gerado quando indPag é igual a zero (pagamento à vista) |
| Y08 | nDup | Número da Parcela | E | Y07 | 0-1 | Obrigatória informação do número de parcelas com 3 algarismos, sequenciais e consecutivos. Ex.: “001”,”002”,”003”,... Observação: este padrão de preenchimento será obrigatório somente a partir de 03/09/2018 | NUMERODOCUMENTO |  |
| Y09 | dVenc | Data de vencimento | E | Y07 | 0-1 | Formato: “AAAA-MM-DD”. Obrigatória a informação da data de vencimento na ordem crescente das datas. Ex.: “2018-06-01”,”2018-07-01”, “2018-08-01”,... | DATAVENCIMENTO |  |
| Y10 | vDup | Valor da Parcela | E | Y07 | 1-1 |  | Valor Líquido do Lançamento |  |
