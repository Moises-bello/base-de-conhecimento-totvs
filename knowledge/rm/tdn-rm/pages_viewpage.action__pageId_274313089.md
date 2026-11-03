---
content_hash: 645d04604885f3c75b48cf50335e0c1699c8321d52950ddf28acf84245a82c16
fetched_at: '2026-06-29T00:08:33.337253+00:00'
page_id: '274313089'
product: rm
source: tdn-rm
title: RMFIS00007_Registro F500 Pedido/Medição INSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274313089
version: 9
---

# Assunto:

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 11.52./11.82 |
| **Ocorrência:** | Geração do registro F500  - Pedido/Medição INSS dos lançamentos fiscais |
| **Ambiente:** |  |
| **Passo a passo:** | Implementado a geração do registro F500 da rotina EFD Contribuições com base nos valores do tributo INSS nos lançamentos fiscais e geração do registro 1900 com base nos movimentos de pedido/medição.  **1 – INSS**  Com base no tributo INSS dos lançamentos fiscais de saída no período de geração da rotina será gerado um registro F500 considerando o total do tributo como base de calculo, para isto é necessário que seja feito as seguintes parametrizações:  Opções -> parâmetros -> Processo -> Registro F500.  Criar um documento fictício e marcar como base de calculo a opção “Utiliza INSS para o cálculo” conforme exemplo abaixo:   Figura     OBS: O tipo de documento não interfere de nenhuma forma na geração do registro, é necessário associar devido ser chave deste cadastro.  •Depois na pasta Tributos deve ser inserido os tributos PIS\COFINS para o tipo de documento cadastrado  •O lançamento de saída deve ter o tributo de INSS na pasta Outros Tributos.  •Efetuado a geração da rotina foi destacado o registro:  |F500|165,00|01|0,00|165,00|0,65|1,07|01|0,00|165,00|7,60|12,54|||||  |F525|165,00|99||||165,00|01|01|Total de PIS e COFINS Calculado Sobre o Valor do INSS||    **2 – Movimento pedido/medição**  Implementado a geração do registro 1900 da rotina EFD Contribuições com base nos movimentos de pedido/medição do Totvs Gestão de estoque, Compras e Faturamento, para isto é necessário que seja feito as seguintes parametrizações:  Cliente/Fornecedor das movimentações órgão público:   Figura     • Inserir Tributos PIS\COFINS nos itens do movimento  • Cód. Natureza de Operação deve ser preenchida na pasta Fiscal do Movimento.    A opção “Fatura o Movimento” deve estar habilitada, e deve possuir um “Tipo de Documento Duplicata Default” onde serão selecionadas algumas informações do registro conforme mapeamento:   Figura     No momento da geração deve ser informado no campo “Tipo de movimento (Pedido/Medição) a ser considerado registro 1900” os tipos de movimentos de pedido/medição, estes devem estar no formato 2.1.01 caso houver mais de um deve ser estar separados por ponto e vírgula conforme modelo 2.1.01;2.2.02 e imagem abaixo:   Figura     **IMPORTANTE: Os tipos de movimento devem ser separados apenas por ponto e vírgula para que não ocorram inconsistências no processo. Exemplo: 2.1.01;2.2.02;2.2.03**  Após parametrização as informações do movimento serão geradas no arquivo registro 1900:  |1900|21867387000158|01|||00|6000,00|2|01|01||||  O pedido/medição gravado no registro 1900 conforme processo descrito acima será faturado dando origem a outro movimento. A venda gerada e integrada ao TOTVS gestão Financeira será informado na rotina EFD Contribuições no registro F500, para isto o lançamento financeiro deve estar parametrizado pelo tipo de documento na parametrização normal (opções -> parâmetros -> processos) regime de caixa no TOTVS Gestão Fiscal.  Quando feita esta parametrização para considerar os lançamentos financeiros gerados a  partir da venda, as informações serão gravadas novamente no registro 1900 da rotina para que isto não ocorra, será necessário informar nos parâmetros de geração os tipos de documentos de faturamento, estes devem estar no formato 2.1.01 caso houver mais de um deve ser estar separados por ponto e vírgula conforme modelo 2.1.01;2.2.02. |
| **Observações:** | •OBS: Caso no período de geração da rotina existam informações apenas para geração do registro F500, seja com base no INSS ou no faturamento das medições e não existam movimentações no período, será gerado um registro 1900 em branco conforme orienta guia pratico e erros apresentados no validador. |
