---
content_hash: 456025310f05538ad8aa616c5fcea9aa49f30c5632149f41c56917185d82e4ec
fetched_at: '2026-06-29T00:06:23.348675+00:00'
page_id: '224100790'
product: rm
source: tdn-rm
title: TU8414_DT_Rescisao_Transferencia_Passa_Funcao_Chapa_Demitida
type: documentation
url: https://tdn.totvs.com/display/LRM/TU8414_DT_Rescisao_Transferencia_Passa_Funcao_Chapa_Demitida
version: 2
---

# RESCISÃO POR TRANSFERÊNCIA ESTÁ PASSANDO COMO PARÂMETRO A FUNÇÃO DA CHAPA DEMITIDA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Na rescisão por transferência está chamando o serviço do Vitae para atualizar dados da tabela de recrutamento, passando a função da chapa demitida.*  *Com isto, quando a transferência é para outra Coligada, onde não existe o mesmo código de função, retorna erro de foreing key.* |
| **Solução/Implementação:** | *Ajuste na passagem de parâmetros para o serviço do Vitae que atualiza dados da tabela de recrutamento, para informar a função da nova chapa, que será admitida na outra Coligada.* |
| **Chamados   relacionados:** | *TU8414, TUAZYO* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
