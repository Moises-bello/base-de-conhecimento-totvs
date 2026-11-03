---
content_hash: 4a52e4106a641bb72c0dfad96d71537333b9f9fb976d853c0e9226f895740d65
fetched_at: '2026-06-29T00:08:45.527262+00:00'
page_id: '311632014'
product: rm
source: tdn-rm
title: RMFIS00007_Registro C114
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00007_Registro+C114
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.X |
| **Ocorrência:** | Geração do Registro C114 |
| **Ambiente:** |  |
| **Passo a passo:** | REGISTRO C114: CUPOM FISCAL REFERENCIADO  Este registro será utilizado para informar, detalhadamente, nas operações de saídas, cupons fiscais que tenham sido mencionados nas informações complementares do documento que está sendo escriturado no registro C100.  Nas operações de entradas, somente informar quando o emitente do cupom fiscal for o próprio informante do arquivo. Não podem ser informados para um mesmo documento fiscal, dois ou mais registros com a mesma combinação de conteúdo nos campos ECF\_FAB, NUM\_DOC e DT\_DOC."    Caso a inclusão de lançamento seja realizada diretamente no RM Liber ou via importação de arquivo, o sistema consistirá o lançamento da tela de Referências conforme imagem abaixo.   Figura     Para habilitar a tela de referência marque a opção: "Possui documentos relacionados" no cadastro da natureza de operação conforme imagem:   Figura     No lançamento fiscal informe o documento do cupom na tela de Referências - Lançamentos Fiscais, preencha o motivo da referência e Observação.    Caso a origem do lançamento seja o RM Nucleus é necessário parametrizar o tipo de movimento, utilizado na inclusão da nota que possui um cupom referenciado, etapa "Fis - Escrituração 1/2" informar o código 04 no campo "Código Motivo" da tela de "Referência entre Documentos" conforme imagem abaixo:   Figura     O movimento pode ser criado pelo assistente de cópia por referência, após escriturar os movimentos, cupom fiscal (redução z) e nota com cupom referenciado, será possível gerar o arquivo SPED FISCAL com o registro C114, segue trecho do arquivo gerado:    |C100|1|0|C00011|01|00|U|987654||25102017|25102017|100,00|2|0|0|100,00|9|0|0|0|100,00|18,00|0|0|0|1,65|7,60|0|0| |C110|1|| |C114|2D|12365412|001|000000001|25102017| |
| **Observações:** |  |
