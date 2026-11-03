---
article_id: 1500001485501
category: Folha Mensal
content_hash: 5d6e91dd7309e17099622c9ecf39697db8a85e811d480fe110b9a3e4a9ac5a59
fetched_at: '2026-06-28T22:46:59.455628+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Importação do Movimento
type: support-article
updated_at: '2025-10-31T19:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001485501-RH-RM-FOP-Importa%C3%A7%C3%A3o-do-Movimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24143679328535)Tempo aproximado para leitura: **00:05:10 min**  
  
**Dúvida**Como realizar a Importação do Movimento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Solução**Para solucionar essa duvida, realize seguintes passos:  
  
1. Verifique a formatação do layout desejado para efetuar a importação do arquivo que deseja, conforme layout abaixo:  
  
***Layout* de Importação do Movimento - RM Labore**

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

***Layout* de Importação do Movimento - RM Folha/RM Ponto**

|  |  |  |  |
| --- | --- | --- | --- |
| Coluna | Tamanho | Tipo | Descrição |
| 01 | 16 | String | Chapa do funcionário |
| 17 | 09 | Inteiro | Mês-caixa |
| 26 | 04 | Alfanumérico | Código do evento |
| 30 | 15 | Real | Valor do evento |
| 45 | 15 | Real | Número de horas |
| 60 | 01 | Caractere | Dados foram alterados manualmente (S ou N) |

**Importante**  
É imprescindível que a exportação do RM Folha/RM Ponto para o RM Folha de Pagamento seja através de chapa.  
  
**Importante**  
Caso tenha dificuldades na elaboração do layout, é possível utilizar a rotina de Cancelamento do Movimento para cancelar um envelope, onde ao final da rotina será exibida a opção de salvar o layout daquele movimento.  
  
Abaixo como gerar o arquivo pronto:  
  
Pegue qualquer funcionário e realize o lançamento para ele:  
  
![](https://totvssuporte.zendesk.com/attachments/token/jr0rCxQgktgBhpZOPlWZ0pncz/?name=image.png)  
  
Após realize o cancelamento do movimento da seguinte forma:  
  
[RH - RM - FOP - Cancelamento do Movimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057701274-RH-RM-FOP-Cancelamento-do-Movimento?source=search)  
  
É preciso a seguinte flag marcada para gerar o arquivo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/MYcOUlC6gKgPMGkZc94LSf58m/?name=image.png)  
  
No caminho que salvou veja que o arquivo já retorna com layout pronto respeitando todos os parâmetros que seu sistema está parametrizado:   
  
![](https://totvssuporte.zendesk.com/attachments/token/IHOYUjmC4sKH3zBaXZEzsjY6K/?name=image.png)

2. Após verificação do layout, acesse: **Folha Mensal | Importação | Importação do Movimento**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074252182935)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074254498967)  
  
**Arquivo:** Neste campo é necessário referenciar o arquivo texto que constam as informações de acordo com o layout, para que seja realizada a importação.  
  
**Transfere arquivo para o servidor:** Deverá ser utilizado quando o ambiente de execução do sistema estiver configurado em 3 camadas. Exemplo: Ao importar o movimento utilizando um arquivo texto local, máquina cliente, caso marcado o parâmetro, o arquivo texto será transferido para o servidor  de aplicação onde o processo é executado. Também poderá ser utilizado quando o arquivo texto está em outra máquina e o usuário mapeia um drive apontando para esta máquina. Neste caso também tem que marcar o parâmetro transfere arquivo para o servidor.  
  
**Layout:** Neste campo, é possível selecionar o layout RM Labore ou RM Folha.  
  
**Ações**

* **Substituir:** o evento importado do arquivo substituirá o evento de mesmo código, caso exista no envelope de pagamento do período atual.
* **Ignorar:** o evento importado do arquivo não será importado se existir o mesmo evento no envelope de pagamento do período atual.
* **Somar:** o evento importado do arquivo somará o valor e referencia do evento de mesmo código, caso exista no envelope de pagamento do período atual.

3. Após o processos acima, pode informar a opção de pagamento ou não, e clicar em avançar.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12074257002007)  
  
**Saiba mais**  
[Importação de Movimento](https://tdn.totvs.com/pages/releaseview.action?pageId=452719187)

[Layout Para Importação do Movimento do Centro de Custo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719315)
