---
content_hash: 05d4f857838dd66dc4f2857c2f0793ec97630fb7607c1848ff35518d2d80fe49
fetched_at: '2026-06-29T00:08:57.282526+00:00'
page_id: '353289158'
product: rm
source: tdn-rm
title: RMCTB0006_REGISTRO 0007
type: documentation
url: https://tdn.totvs.com/display/LRM/RMCTB0006_REGISTRO+0007
version: 1
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Contábil |
| **Versões:** | 12.1.XX |
| **Ocorrência:** | Erro no Registro 0007 |
| **Ambiente:** |  |
| **Passo a passo:** | **Processo:**  Erro apresentado ao validar o arquivo da ECD no Pré-Validador:  **CÓDIGO DA INSTITUIÇÃO NÃO ENCONTRADO NA TABELA DE INSTITUIÇÕES RESPONSÁVEIS PELA ADMINISTRAÇÃO DO CADASTRO DAS ENTIDADES**  **Análise/Solução**  Esta mensagem ocorre por 2 situações:  1-  O código informado não é válido  ou  2- O pré - validador não consegue consistir o código cadastral informado por não ter acesso a estas informações, neste caso, orientamos que desconsidere esta mensagem e faça a validação no PGE (Programa de Gerador de Escrituração).  Para acerto do caso 1:  Acesse Obrigações Acessórias/Cadastros/Outras Inscrições Cadastrais   * Caso a sua empresa possua alguma Instituição que irá ter acesso aos seus livros além da Receita Federal ela deverá ser cadastrada nesse menu. O ‘Código Cadastral’ dessa Instituição é obtido com a Receita Federal.  * Caso a sua empresa não possua nenhuma outra Instituição que irá ter acesso aos seus livros além da Receita Federal, você deverá indicar em INSTITUIÇÃO a opção “00 – Sem inscrição em Secretarias de Fazenda Estaduais”, o ‘Código Cadastral’ deve ser 0000 e a filial a matriz (a qual o SPED está sendo gerado). |
| **Observações:** |  |
