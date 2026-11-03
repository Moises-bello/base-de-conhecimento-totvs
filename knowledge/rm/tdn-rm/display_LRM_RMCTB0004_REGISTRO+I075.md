---
content_hash: 8f99bb7f65d9ed32a8d4ef1754437cbb7323f2d566545b7a44a10d4ae3afe127
fetched_at: '2026-06-29T00:08:57.225534+00:00'
page_id: '353283984'
product: rm
source: tdn-rm
title: RMCTB0004_REGISTRO I075
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB0004_REGISTRO+I075
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Erro no Registro I075 |
| **Ambiente:** |  |
| **Passo a passo:** | **Processo:**  Erro apresentado ao validar o arquivo da ECD no PGE (Programa Gerador de Escrituração):  ****REGISTRO I075**  CAMPO OBRIGATÓRIO NÃO PREENCHIDO - DESCR\_HIST**  **Análise/Solução**  Essa inconsistência é apresentada devido ao não preenchimento do campo Descrição do Histórico Padrão.  Para preencher, deverá acessar o cadastro de Histórico padrão e informar a descrição.  Acesse o menu Cadastros / Histórico Padrão / Edite o respectivo código / Preencha o campo Descrição e salve.    Para saber qual o código que esta sem descrição, na linha do SPED, o segundo campo do registro I075 informa qual é o código.  No exemplo abaixo, o código do histórico padrão é o 2017.  |I075|**2017**|ARE 2017| |
| **Observações:** |  |
