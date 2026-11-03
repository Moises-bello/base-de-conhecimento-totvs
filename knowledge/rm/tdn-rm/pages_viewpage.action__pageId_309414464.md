---
content_hash: 9d40854e83139da6514f190a7aee6553f65877363610688d4c688dfbc59d675f
fetched_at: '2026-06-29T00:08:45.292784+00:00'
page_id: '309414464'
product: rm
source: tdn-rm
title: Como ativar a Reforma Trabalhista 2017 no RM?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=309414464
version: 4
---

**Assunto**

|  |  |
| --- | --- |
| **Produto:** | RM |
| **Ocorrência:** | Reforma Trabalhista 2017 |
| **Passo a passo:** | **Para ativar a Reforma Trabalhista 2017 no RM é necessário seguir os seguintes passos:**  **1 ) Executar o pacote de script**  Somente os clientes que já estão na versão 12.1.17 e 12.1.18 precisam fazer o processo de execução do pacote de script.  Clientes com versões anteriores a 12.1.17 não precisam executar o script abaixo.  **SQL**: RT\_2017  **ORACLE**: RT\_2017\_ORA  Caso tenha dificuldades em executar o pacote de script, pode seguir os passos do link:  <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM>  **Obs.:** Após executar o patch os Scripts ficam na pasta "**...\CorporeRM\RM.Net\Scripts Especificos".**  **2 ) Habilitar o parâmetro Reforma Trabalhista 2017**  Após executar o script entre no Parametrizador e habilite o parametro.  Configurações > Parametrizador > 06.01.03 - Folha Normal > Geral > 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017'    **Obs**: Caso tente habilitar o parâmetro antes de executar o script, será gerado a seguinte mensagem, e o parâmetro não será habilitado:    **ATENÇAO: A TOTVS recomenda que a reforma seja habilitada após 11/11/2017.** |
