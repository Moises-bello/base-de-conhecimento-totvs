---
content_hash: 79dc5d92960e6126906fe1722583634ac5b7624bf68ca499724084706c30bcce
fetched_at: '2026-06-29T00:08:08.641180+00:00'
page_id: '239016141'
product: rm
source: tdn-rm
title: TUTOPT_DT_Funcao_Formula_Dados_Rescisao_Coletiva
type: documentation
url: https://tdn.totvs.com/display/LRM/TUTOPT_DT_Funcao_Formula_Dados_Rescisao_Coletiva
version: 2
---

# CRIAÇÃO DE FUNCÃO DE FÓRMULA PARA RETORNAR DADOS DA TELA DE RESCISÃO COLETIVA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Coletiva* |
| **Situação/Requisito:** | *Quando é utilizada a função TABFUNC acessando os dados de rescisão, na fórmula para dias de aviso prévio, o cálculo não fica correto no módulo de Rescisão Coletiva.*  *Isto ocorre, porque a TABFUNC busca as informações direto da tabela PFUNC, e no caso de Rescisão Coletiva os dados são salvos no banco somente no final do processo.* |
| **Solução/Implementação:** | *Será criada uma nova função de fórmula para considerar os dados de rescisão informados pelo usuário.*  *A função DADOSRESCISAO(NomeCampo) será válida somente no módulo de Rescisão Coletiva, para campos informados nesta tela.*  *O nome do campo a ser passado no parâmetro deve ser o mesmo utilizado na TABFUNC.* |
| **Chamados   relacionados:** | *TUTOPT* |
| **Versões/Release:** | *12.1.12* |
