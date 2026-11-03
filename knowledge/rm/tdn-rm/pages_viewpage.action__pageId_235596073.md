---
content_hash: 699faa21a29f1d9ba581797dda2873311f79f62377107d7b189987ab8758a4c2
fetched_at: '2026-06-29T00:08:05.494440+00:00'
page_id: '235596073'
product: rm
source: tdn-rm
title: SAU0073_Como_Calcular_O_Valor_do_Filme_Radiológico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235596073
version: 2
---

# Como calcular o valor do filme radiológico

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO HOSPITALAR |
| **Versões:** | Todas |
| **Passo a passo:** | 1° Passo)  No menu Faturamento -> Condições Contratuais com Convênios -> Tabelas de Procedimentos e Serviços  Acesse o Procedimento de Exame o qual você gostaria de parametrizar o valor do filme.  Neste exemplo, o valor do filme é 0,3080, que será multiplicado pelo valor do metro no passo 2    **2º) Passo:**  Acesse o menu Cadastros -> Faturamento -> Condição Financeira Com convênio.  Acesse a condição financeira com o convênio desejado  Clique em “Anexos” -> Valores de Filme  Veja que o valor do filme é R$17,00      **3°) Passo:**  Calculando o filme  0,3080 \* 17 = 5,24 (arredondando)      **4°) Passo:**  Como saber se o valor do filme está sendo calculado corretamente?  Acesse o menu Cadastros -> Faturamento -> Condição Contratual com Convênio  Acesse a condição contratual com o convênio desejado  Na aba “Parâmetros 3”, marque o parâmetro Valor do Filme destacado.  Agora, ao lançar o exame, o valor do filme virá separado na conta      **5°) Passo:**  Na conta do paciente, ao lançar o procedimento, veja que o filme radiológico saiu destacado.      **Nota:** Para que serve o campo incidências?  O campo incidências, no cadastro do procedimento na tabela de procedimentos e serviços, tem como finalidade definir o número de incidências padrão  para o procedimento em específico, logo, caso no lançamento de conta o número de incidências ultrapasse o valor estipulado no cadastro do procedimento,  será lançado na conta do paciente as "incidências extras", que será o número de incidências restantes multiplicado pelo fator do filme.  Exemplo: Nesta simulação dos passos anteriores, o campo "Incidências" consta como 2.  Logo, se na elaboração de contas fossem lançadas 3 incidências havia um lançamento automático de um novo item "Incidências Extras" no valor de 5,24  (valor do filme) |
| **Observações:** | Sem o parâmetro marcado, o valor deve ser o valor do procedimento + o valor do filme |
