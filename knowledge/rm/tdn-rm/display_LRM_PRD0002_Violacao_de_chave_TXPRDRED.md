---
content_hash: a3b01e21675bedb34df6519a0e054ad09877228f1f56cf49d699e1a13f5ca7b5
fetched_at: '2026-06-29T00:08:33.446543+00:00'
page_id: '274318049'
product: rm
source: tdn-rm
title: PRD0002_Violacao_de_chave_TXPRDRED
type: documentation
url: https://tdn.totvs.com/display/LRM/PRD0002_Violacao_de_chave_TXPRDRED
version: 5
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 11.82 e posteriores |
| **Ocorrência:** | Violação da chave TXPRDRED ao salvar o cadastro de um novo produto |
| **Ambiente:** | Cadastro de Produto |
| **Passo a passo:** | Ao salvar o cadastro de um novo produto é apresentado a mensagem:    O incidente é apresentado pois o valor atual do código reduzido é menor que o valor máximo encontrado na TPRODUTO para a coligada em questão. Com isso, ao salvar o produto o sistema está tentando gerar um valor de código reduzido automaticamente que já se encontra cadastrado na base de dados.  Para igualar os valores do MAX(CODIGOREDUZIDO) – **Maior valor encontrado para o código reduzido na coligada** - e da sequência atual nos parâmetros do sistema, basta executar a consulta abaixo:  SELECT MAX(CODIGOREDUZIDO) FROM TPRODUTO WHERE CODCOLPRD = X -- Onde X é o código da coligada que está cadastrando o produto.  De posse do último código reduzido, será necessário alterar a sequencial atual no parâmetro do sistema.  Segue abaixo a imagem de onde deve ser feito a alteração no parâmetro:    Realizando essa configuração, você irá igualar o último valor encontrado na tabela **TPRODUTO** em relação a **GAUTOINC**, e a inconsistência não deverá ser mais apresentada novamente.  **IMPORTANTE**  Pode ser que mesmo após seguir o procedimento acima, a mensagem continuará a ser apresentada.  Neste caso é necessário executar a consulta T-SQL abaixo novamente:  SELECT MAX(CODIGOREDUZIDO) FROM TPRODUTO WHERE CODCOLPRD = X -- Onde X é o código da coligada que está cadastrando o produto.  Verificar se o retorno da consulta é = 9999. Veja o exemplo abaixo:    Caso o retorno seja o mesmo da imagem acima, não poderemos afirmar que este é o último código reduzido gerado na tabela para a coligada em questão.  Provavelmente em sua base de dados existe mais de 9999 produtos cadastrados com códigos reduzidos maiores que este valor e por isso a mensagem continua sendo apresentada.  Entretanto, a consulta T-SQL retorna este valor pois este é o maior número que pode ser gerado de acordo com a máscara definida no parâmetro.  Neste exemplo, a máscara é #### (Verificar qual é a máscara definida no seu parâmetro):    Neste caso, é necessário executar a consulta abaixo para verificar o maior código reduzido da coligada.  SELECT MAX(CODIGOREDUZIDO) FROM TPRODUTO WHERE CODIGOREDUZIDO > 9999 AND CODCOLPRD = X -- Onde X é o código da coligada que está cadastrando o produto.  Feito isso, basta colocar o valor retornado na consulta acima no parâmetro do valor atual do código reduzido para que a mensagem de chave duplicada não seja apresentada.  Veja na continuação do exemplo anterior:    Aplicando a alteração no parâmetro: |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
