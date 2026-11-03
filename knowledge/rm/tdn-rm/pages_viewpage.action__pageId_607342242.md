---
content_hash: ced2be780ed81f8d73d7094563fa7ea44ec585cb41dba45b7d2c9a3e4a76ac98
fetched_at: '2026-06-29T00:10:58.838741+00:00'
page_id: '607342242'
product: rm
source: tdn-rm
title: Importação de Dados do Folha de Pagamento - Layout Horários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607342242
version: 24
---

Para realizar a importação de horários em .txt será necessário seguir o layout abaixo.

**Atenção:**

**-** O tamanho dos campos deve ser respeitados, pois o sistema válida pela posição do caractere, por exemplo: Código horário  é 0001, ele tem 4 caracteres, e o tamanho do campo é 10, o resto deverá ser preenchido com espaço, conforme o exemplo no final da página.

Por padrão ao utilizar a importação de horário em .txt o tipo de horário será definido como Rígido.  
Exceto nos casos que o arquivo contém o tipo 06 (Limite de refeição), obrigatoriamente em conjunto com o tipo 04 (Intervalo de refeição/Ausência Planejada), nesse caso o tipo de horário será definido como semi-fléxivel.

Usar o layout do Tipo 00 abaixo para versões superiores a 12.1.29. Para versões anteriores, omitir o campo **Data final como data referência**.

11Exemplo de criação layout para horário Diurno

**Atenção:** O usuário deverá criar o layout conforme necessidade. Abaixo segue modelo para melhor entendimento.

Será visualizado no cadastro de horários por intervalo o resultado do horário do exemplo acima

2Exemplo de criação layout para Horário Noturno

**Importante:**

Para horário noturno as batidas devem ser cadastradas no tipo 01 conforme o dia da jornada.

No exemplo a seguir, a batida fim do índice 1, deve ser cadastrada no índice 2, pois, corresponde ao índice da batida de saída. O mesmo comportamento deverá ser ajustado para os demais índices.

Resultado do horário do exemplo acima:

**Observação:**No tipo 01 será necessário repetir os campos "Horário da batida", "Natureza da batida" e "Ponto e vírgula" de acordo com a quantidade de batidas a serem inseridas no horário.

**Atenção:** A importação de horário em .txt deve ser realizada através do menu Folha de Pagamento | Configurações | Importações | Importação de dados do Folha de Pagamento.

Informações: [Base do conhecimento](https://tdn.totvs.com/pages/viewpage.action?pageId=415707918)
