---
content_hash: 9e0175c4098f120408df457ad6a8c785ef265a6767a27aad5941947028fe8762
fetched_at: '2026-06-29T00:10:07.344426+00:00'
page_id: '452719407'
product: rm
source: tdn-rm
title: Seguro Desemprego - SDWEB
type: documentation
url: https://tdn.totvs.com/display/LRM/Seguro+Desemprego+-+SDWEB
version: 3
---

O novo relatório do seguro desemprego foi instituído pela  **RESOLUÇÃO CODEFAT Nº 620, DE 5 DE NOVEMBRO DE 2009.**     
No TOTVS Folha de Pagamento, através deste módulo será gerado para os funcionários demitidos o relatório seguro desemprego.  
   
Ao iniciar a parametrização do relatório, será necessário gravar um Perfil de Parâmetros para que todos os parâmetros definidos fiquem "salvos" para futuras gerações do relatório Seguro desemprego.  
   
Para gravar o perfil, na primeira tela do wizard deverá inserir uma descrição no campo "Perfil de Parâmetros" e clicar no Box "Salvar perfil ao concluir".  
   
Se desejar, poderá informar uma Descrição do Processo, para que no histórico de processo executados seja identificado com a descrição.   
   
Na geração do seguro deverá definir: Quebra de seção e a grade de Seleção de Funcionários. Esta parametrização servirá como filtro, ou seja, serão gerados Relatórios seguro desemprego cujas seções dos funcionários correspondam à quebra informada e os funcionários tenham dados compatíveis com a grade de seleção definida.  
   
Também será possível selecionar se deseja que o relatório seja gerado para funcionários que tiveram rescisão do tipo T - Término de Contrato marcando o parâmetro "Considerar Rescisão Tipo T".  
   
O MTE promoveu alterações no Sistema de Processamento do Benefício Seguro-Desemprego, e com essas alterações os arquivos deixaram de ser validados. Fizemos diversas pesquisas e contatos sobre o assunto, e não conseguimos obter nenhuma informação oficial do MTE sobre a possível disponibilização de novo layout.  
   
Na busca de solução para essa situação, identificamos que alterando o campo telefone para 9 dígitos e diminuindo 1 dígito no campo filler o arquivo passa a ser validado com sucesso.  
Com isso, mesmo sem a liberação de novo layout pelo MTE, disponibilizamos no sistema o parâmetro "Considerar 9º dígito para telefone" para que as empresas possam ter a possibilidade de validação do arquivo.  
   
Marcando esse parâmetro, para os funcionários que possuem o telefone cadastrado com nove dígitos, o sistema levará para o arquivo os nove últimos dígitos cadastrados. Para os funcionários que possuem oito dígitos, levará os oito dígitos e acrescentará um zero à esquerda.  
Sem a marcação do parâmetro, o sistema continua levando apenas oito dígitos para o campo de telefone, independente se o funcionário possuir oito ou nove dígitos no número de seu cadastro.

Observação: Para os funcionários que utilizam a CTPS Digital serão considerados os 7 (sete) primeiros dígitos do CPF do trabalhador para o número e os 4 (quatro) últimos dígitos do CPF do trabalhador para série na geração do arquivo Seguro Desemprego.   
  
**Atenção**   
   
A competência e ano são obrigatórios  para que somente funcionários demitidos na competência e ano informado tenham o relatório gerado.

|  |  |
| --- | --- |
|  | Veja Também |

---

[MTE - Ministério do Trabalho e Emprego](http://portal.mte.gov.br/data/files/FF8080812BCB2790012BD009DFEC650E/r_20091105_620.pdf)
