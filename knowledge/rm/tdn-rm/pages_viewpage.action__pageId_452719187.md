---
content_hash: d95dbe475766f7f844adf48968a6e439e1bf2d0a5f75a5e5ca3deee60034f2e3
fetched_at: '2026-06-29T00:10:04.031073+00:00'
page_id: '452719187'
product: rm
source: tdn-rm
title: Importação de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719187
version: 52
---

A importação de Movimento é uma funcionalidade que deverá ser utilizada para alimentar o envelope de pagamento por meio de um arquivo texto cujas informações deverão estar de acordo com o layout de importação.  
No campo "Arquivo" é necessário referenciar o arquivo texto que constam as informações de acordo com o layout, para que seja realizada a importação.  
   
Ao importar o movimento utilizando um arquivo texto local (máquina cliente), o arquivo texto será transferido para o servidor  de aplicação onde o processo é executado.  
Também poderá ser utilizado quando o arquivo texto está em outra máquina e o usuário mapeia um drive apontando para esta máquina.  
   
No campo layout, é possível selecionar:  
1 - RM LABORE   
2 - RM FOLHA  
   
Utilização das Ações:  
 "Substituir": o evento importado do arquivo substituirá o evento de mesmo código, caso exista no envelope de pagamento do período atual.  
"Ignorar" : o evento importado do arquivo não será importado se existir o mesmo evento no envelope de pagamento do período atual.  
" Somar": o evento importado do arquivo somará o valor e referencia do evento de mesmo código, caso exista no envelope de pagamento do período atual.  
A data de pagamento poderá ser definida, caso não seja, o movimento será importado com a data informada no arquivo de importação quando utilizado o Layout RM LABORE ou a data de pagamento estabelecida nos parâmetros do sistema, quando a utilização for do Layout RM FOLHA.  
   
layout de Importação de Movimento  
**Layout de Importação do Movimento (RM Labore)**

|  |  |  |  |
| --- | --- | --- | --- |
| Coluna | Tamanho | Tipo | Descrição |
| 01 | 16 | String | Chapa do Funcionário |
| 17 | 08 | String | Data pagamento (DDMMAAAA) |
| 25 | 04 | Alfanumérico | Código do evento |
| 29 | 06 | String | Hora (HHH:MM) |
| 35 | 15 | Real | Referência (999999999999.99) |
| 50 | 15 | Real | Valor (999999999999.99) |
| 65 | 15 | Real | Valor original (999999999999.99) |
| 80 | 01 | Caractere | Dados foram alterados manualmente (S ou N) |
| 81 | 01 | Caractere | Dados de férias (S ou N)\* |

   
 **Layout de Importação do Movimento (RM FOLHA/RM PONTO) - para o usuário que selecionar esta opção**  
Primeira linha é ignorada  
Da segunda linha em diante, o formato é o seguinte:

|  |  |  |  |
| --- | --- | --- | --- |
| Coluna | Tamanho | Tipo | Descrição |
| 01 | 16 | String | Chapa do funcionário |
| 17 | 09 | Inteiro | Mês-caixa |
| 26 | 04 | Alfanumérico | Código do evento |
| 30 | 15 | Real | Valor do evento |
| 45 | 15 | Real | Número de horas |
| 60 | 01 | Caractere | Dados foram alterados manualmente (S ou N) |

**Atenção:**  
É imprescindível que a exportação do RM FOLHA/RM PONTO para o RM Labore seja através de chapa.
